import pandas as pd

chat = pd.read_csv('test_chat_export.csv', header = None)
chat = chat.iloc[:, -2:]
f = open("test_chat_export.txt", 'w')
for l in chat.values:
    for ll in l:
        f.writelines(ll + '\n')



