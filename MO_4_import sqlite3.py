import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS books
                (title TEXT, author TEXT, year INTEGER)''')
conn.commit()
import csv

with open('books2.csv', 'r') as file:
    books_data = csv.DictReader(file)
    to_db = [(i['title'], i['author'], i['year']) for i in books_data]

curs.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?);", to_db)
conn.commit()
curs.execute('SELECT title FROM books ORDER BY title ASC')
for row in curs.fetchall():
    print(row[0])
    curs.execute('SELECT * FROM books ORDER BY year')
for row in curs.fetchall():
    print(row)
conn.close()
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///books.db')
with engine.connect() as connection:
    query = sqlalchemy.text("SELECT title FROM books ORDER BY title ASC")
    result = connection.execute(query)
    for row in result:
        print(row[0])