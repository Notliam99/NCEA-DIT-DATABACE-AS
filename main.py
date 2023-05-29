"""main file for the project"""

import sqlite3

with sqlite3.connect("employee.sqlite3") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees_table")
    resault = cursor.fetchall()

for person in resault:
    for item in person:
        print(item)
