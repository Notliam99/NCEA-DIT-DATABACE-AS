import sqlite3

with sqlite3.connect("employee.sqlite3") as connection:
    cursor = connection.cursor()
    cursor.execute("create table cool (wow);")
    connection.commit()
