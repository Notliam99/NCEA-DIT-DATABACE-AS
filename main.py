"""main file for the project"""

import sqlite3

with sqlite3.connect("employee.sqlite3") as connection:
    """
        connects and runs a qureie the resault
        of witch is saved to the var resault.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees_table")
    resault = cursor.fetchall()  # the resault where the reault is saved.

for person in resault:
    """lists through the pepole in the table"""
    for item in person:
        """lists through the items of info mation about each person."""
        print(item)
