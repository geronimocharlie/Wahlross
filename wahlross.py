import pandas as pd
import time

mit = pd.read_csv('Mitglieder_dummy_github.csv', encoding='utf-8')
mit['Enthaltung'] = False
mit['Ja'] = False
mit['Nein'] = False

# was zachlt
zustimmung = ['ja', 'jo', 'j', 'yes', 'zustimmung', 'ich stimme zu']
ablehnung = ['nein', 'n', "no"
, "dagegen", "ich lehne ab", "ich stimme nicht zu"]
enthaltung = ['e', 'enth', 'enthaltung', 'ich enthalte mich']

chat = pd.read_fwf('sitzung_dummy.txt', header=None)
#chat = pd.read_fwf('test_chat_export.txt', header=None, delimiter=' ')

# copied chat has the following structure:
# kürzel
# Name
# time
# empy line
# Redebeiträge (can be multiples)


others = []
mit = mit.reset_index()
mit = mit.set_index('Name')

defn = 'Böse'
name = defn
unberechtigt = []
waiting_for_vote = False
for E in chat[0]:
    # skipping time and emty lines
    if (E[0].isdigit()) or ((len(E) == 0)): #& ~(E[0:2].lower() in ['ja', 'ne', 'en'])):
        continue
    e = E.lower()
    # if Mitglied found that may vote wat for vote
    if (E in mit.index):
         if mit.at[E, "wahlberechtigt"]=='x':
             name=E
             waiting_for_vote = True
         else:
            # if Mitglied but not stimmberechtigf (nur vertreter etc)
            unberechtigt.append(E)
    elif (e in enthaltung) & ~(name == defn) & waiting_for_vote:
        mit.at[name, 'Enthaltung'] = True
        name = defn
        waiting_for_vote = False
    elif (e in zustimmung) & ~(name == defn) & waiting_for_vote:
        mit.at[name, 'Ja'] = True
        name = defn
        waiting_for_vote = False
    elif (e in ablehnung) & ~(name == defn) & waiting_for_vote:
        mit.at[name, 'Nein']  = True
        name = defn
        waiting_for_vote = False
    else:
        others.append((name, e))


HSG_ergebnis = mit.groupby('HSG')[['Ja', 'Nein', 'Enthaltung']].agg('sum')
HSG_ergebnis['Total'] = HSG_ergebnis.sum(axis=1)

total = HSG_ergebnis[['Enthaltung', 'Ja', 'Nein']].sum()

# prüfe ob mehrfache stimmabgaben
mit['Anzahl Abstimmungen'] = mit[['Enthaltung', 'Ja', 'Nein']].sum(axis=1)
mit['Richtig Abgestimmt'] = mit['Anzahl Abstimmungen'] <= 1
anz_stimmen_passt = mit['Richtig Abgestimmt']
passt_sitze = mit.groupby('HSG')['Sitze'].agg('count') >= HSG_ergebnis['Total']
HSG_ergebnis['Passt'] = anz_stimmen_passt.all()


print(r"""
               ___
            .-9 9 `\
          =(:(::)=  ;
            ||||     \
            ||||      `-.
           ,\|\|         `,
          /                \
         ;                  `'---.,
         |                         `\
         ;                     /     |
         \                    |      /
  jgs     )           \  __,.--\    /
       .-' \,..._\     \`   .-'  .-'
      `-=``       `:    |  /-/-/`
                    `.__/
                    """)
print("Wahlross zählt...")
time.sleep(1)

if HSG_ergebnis['Passt'].all() == True:
    if unberechtigt:
        print("\n")
        print("Warnung: Diese StuRa Mitglieder sind momentan nicht stimmberechtig:")
        print(unberechtigt)
    print("\n")
    print("Gültiges Abstimmungsergebnis")
    print("\n")
    print("--- Ergebnis nach HSG ----")
    print(HSG_ergebnis)
    print("\n")
    print("----- Gesamtergebnis -----")
    print(total)
    print("\n")
    print("--Unpassende Redebeiträge--")
    for p,i in others:
        print(f"{p} : {i} \n")
else:
    print("Ungültiges Ergebnis")
    print('\n')
    print(total)
    print('\n')
    if not passt_sitze.all():
        print("Die abgegbenen Stimmen stimmen nicht mit den Sitzen überein.")
        print(passt_sitze == False)
    if not anz_stimmen_passt.all():
        print("Folgende Mitglieder haben mehrfach abgestimmt:")
        print("\n")
        print(mit[mit['Anzahl Abstimmungen'] > 1][['HSG', 'Nein', 'Ja', 'Enthaltung']])
    print("--Unpassende Redebeiträge--")
    for p,i in others:
        print(f"{p} : {i} \n")
