import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (name, email, password, data_nasc) VALUES (?, ?, ?, ?)",
            ('Monike Freitas', 'monike.ftsousa@gmail.com', 'monike123', '30/07/2003')
            )

connection.commit()
connection.close()