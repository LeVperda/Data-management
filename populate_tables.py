import mysql.connector as mysql

# Not using actual info as I am just writing a script, not actually making a database
mydb = mysql.connect(
    host="host",
    port="port",
    user="user",
    password="password",
    database="database",
)

cursor = mydb.cursor()

insert = "INSERT INTO artist (name) VALUES (%s)"
data = [
    ('Architects'),
    ('Bring me the Horizon'),
    ('ERRA')
]

cursor.execute(insert, data)

insert = "INSERT INTO CD (artist_id, title, genre, price)\
        VALUES (%s, %s, %s, %s)"
data = [
    (1, "For Those That Wish To Exist", "Mathcore", 19)
    (2, "SEMPITERNAL", "Metalcore", 9)
    (2, "POST HUMAN: SURVIVAL HORROR", "Alternative", 19)
]

cursor.execute(insert, data)

insert = "INSERT INTO track (CD_id, title, runtime)\
        VALUES (%s, %s, %s)"
data = [
    (3, "Dear Diary,", 164),
    (3, "Kingslayer feat. BABYMETAL", 220),
    (3, "Ludens", 280)
]

cursor.execute(insert, data)