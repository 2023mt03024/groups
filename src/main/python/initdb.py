import sqlite3

connection = sqlite3.connect('database.db')


with open('src/main/scripts/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO groups (name, member1, member2, member3, member4, member5) VALUES (?, ?, ?, ?, ?, ?)",
            ('Group 1',	'2022MT03577 - Puneet Singh', '2022MT03599 - Murtaz Mastim', '2022MT03564 - Shivraj Dagadi', 
             '2022MT03537 - Paras Jain', '2022MT03593 - Sherine Evangeline Arunodhaya R')
            )

cur.execute("INSERT INTO groups (name, member1, member2, member3, member4, member5) VALUES (?, ?, ?, ?, ?, ?)",
            ('Group 2', '2022MT03527 - Anirudh Uppal', '2022MT03589 - KARMAKAR ANKITA ASHOK', '2022mt03573 - DAYALAN P',
             '2022mt03545 - DILIP K.G.', None)
            )

connection.commit()
connection.close()