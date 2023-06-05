"""tests my sql_module"""

import sqlite3
from sql_module import grubs
from sql_module import seed


def test_get_all_of_table():
    """
    Creates a test tabel in a memory database.
    Since this table is in a memory database it is non-presistant.
    """
    # creates a data base in memory meaning it non-presistant.
    with sqlite3.connect(":memory:") as connection:
        # creates the cursor object.
        cursor = connection.cursor()
        # describes the specifcation of the test tabel.
        cursor.executescript(
            """
            CREATE TABLE test(verify);
            INSERT INTO test VALUES('True');
            """
        )
        # commits the changes for the test table.
        connection.commit()
        my_grub = grubs(database_connection=connection)
        # the function in question for this test.
        table = my_grub.get_all_of_table("test")
        # table should be: (('True',))
        assert bool(table[0][0] == 'True')


def test_adding_people():
    """
    test the module seed by creating a memory database and
    using the function seed with the memory data base.
    """
    with sqlite3.connect(":memory:") as connection:
        # The setup for the test table
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE test(verify);")
        connection.commit()
        # End
        # Creates a instance of the seed class
        my_seed = seed(database_connection=connection)
        # Runs the metod that im testing
        my_seed.insert_to_table(table_name="test", items=("True",))
        # Test that the method works
        resalt = cursor.execute("SELECT * FROM test")
        resalt = resalt.fetchall()
        assert resalt[0][0] == "True"
        # End
