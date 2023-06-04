"""main file for the project"""

import sqlite3
from sql_module import grubs

with sqlite3.connect("employee.sqlite3") as connection:
    # connects to the database and creates a grub
    my_grub = grubs(database_connection=connection)
    # saves the requested table to the var table
    table = my_grub.get_all_of_table("employees_tables")

# checks for error from the get_all_of_table method
if isinstance(table, sqlite3.OperationalError):
    print(table, type(table))
else:
    # loops through the people and items of info from the above table.
    for person in table:
        for item in person:
            print(item)
