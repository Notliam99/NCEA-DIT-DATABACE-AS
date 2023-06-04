import sqlite3
from sql_module import grubs


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
