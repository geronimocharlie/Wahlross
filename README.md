# Liebe Hochschulpolitikbegeisterte...
### (und andere interessierte)
Dieses python script unterstützt uns bei der Wahlauszählung über Big Blue Button.

### How To
Als erster Schritt muss die csv angepasst werden. Öffnet die .ods und tragt eure Mitglieder entsprechend der Vorlage ein.
Unter der Spalte "standard" habe ich vermerkt, wer fest gewähltes Mtiglied ist. Unter der "stimmberechtigt" Spalte könnt ihr die modifizierte Stimmberechtigung anpassen, um Vertreter miteinzubeziehen. Exportiert die .ods als .csv.
Nun könnt ihr rauskopierten BBB chat in die .txt einfügen und das wahlross.py script ausführen.
Wenn ihr chat über das BBB tool exportiert, ist das Format ein bischen anderes. Dann könnte ihr das export_chat_to_copy_chat.py script benutzen, um es in ein für das Wahlross einlesbares Format umzuwandeeln.

### Mögliche Ergebnisse

#### Gültiges Wahlergebenis
In dem Fall kriegt ihr das totale Wahlergebnis und auch eine nach HSGs gruppierte Übersicht.
Außerdem wird euch angezeigt, ob ein Mitgliede versucht hat abzustimmen, was zurzeit nicht wahlberechtigt ist. Diese Stimme wurde nicht mitgezählt.
Zudem werden alle als unpassend empfundende Redebeiträge zusätlich gezeigt. Das ist wichtig um noch einmal nachzuprüfen ob das Wahlross nichts übersehen hat. Hier werden aber vor allem die ganzen Kürzel gezeigt.

#### Ungültiges Wahlergebnis: Mehrfache Stimmabgabe
Wenn ein Mitgliede mehrfach unterschiedliche Stimmen abgegeben hat, ist die Wahl ungültig. Das totale Ergebnis inklusive dieser Person wird angezeigt und eine übersicht welche Person mehrfach abgestimmt hat und was sie abgestimmt hat.

#### Ungültiges Wahlergebnis: Mehr Stimmen als Sitze
Wenn das passiert ist etwas grundlegend schief gelaufen und eine HSG hat mehr Stimmen abgegeben, als sie Sitze hat. Wenn das passiert, kann eigentlich nur ein Fehler in der Mitglieder.csv vorliegen, also überprüft dies nocheinmal.

### Beispiel Ergebnis
Die momentanen Dummy .txt und .csv sollten dieses Ergebnis liefern.

```console

(scientific_programming) codingaway@mypersonaltardis:~/Wahlross$ python wahlross.py 

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
                    
Wahlross zählt...


Warnung: Diese StuRa Mitglieder sind momentan nicht stimmberechtig:
['Martha Müller']


Gültiges Abstimmungsergebnis


--- Ergebnis nach HSG ----
           Ja   Nein  Enthaltung  Total  Passt
HSG                                           
Andere  False   True       False      1   True
Partei   True  False       False      1   True
Party   False  False       False      0   True
Party   False  False        True      1   True


----- Gesamtergebnis -----
Enthaltung    1
Ja            1
Nein          1
dtype: int64


--Unpassende Redebeiträge--
Böse : ma 

Böse : ma 

Böse : ja 

Böse : ol 

Böse : ja 
```
### Requirements
Bei mir läutf das Wahross unter Ubuntu 18.04.4 LTS, Python 3.8.3. Benötigt wird das pandas package.
Wenn ihr conda habt, könnt ihr die bereitgestellte environment.yml benutzen.
```console

foo@bar: conda env create -f environment.yml
foo@bar: conda activate wahlross
(wahlross) foo@bar: python wahross.py
```
