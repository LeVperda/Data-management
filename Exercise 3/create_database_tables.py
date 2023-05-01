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

artist_table = "CREATE TABLE artist (id INT AUTO_INCREMENT PRIMARY KEY,\
                 name VARCHAR(255) NOT NULL)"

CD_table = "CREATE TABLE CD (id INT AUTO_INCREMENT PRIMARY KEY,\
             artist_id INT NOT NULL,\
             title VARCHAR(255) NOT NULL,\
             genre VARCHAR(255) NOT NULL,\
             price INT(10) NOT NULL,\
             FOREIGN KEY (artist_id) REFERENCES artist(id))"

track_table = "CREATE TABLE track (id INT AUTO_INCREMENT PRIMARY KEY,\
                 CD_id INT NOT NULL,\
                 title VARCHAR(255) NOT NULL,\
                 runtime INT(5) NOT NULL,\
                 FOREIGN KEY (CD_id) REFERENCES CD(id))"

cursor.execute(artist_table)
cursor.execute(CD_table)
cursor.execute(track_table)

mydb.commit()
mydb.close()