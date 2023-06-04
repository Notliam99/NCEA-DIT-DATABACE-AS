"""helps people with gruby hands get data"""
import sqlite3


class Get:
    """Class for getting things from a database"""

    def __init__(self, database_connection: sqlite3.Connection) -> None:
        self.connection = database_connection

    def __doc__(self) -> str:
        """this is a doc method :)"""

        return str(
            """
            this class is a little grub
            this is becuse it will exfultrate
            any info in a supplyed database
            """
        )

    def get_all_of_table(self, table: str) -> tuple or str:
        """methoud that gets all items in table"""
        cursor = self.connection.cursor()
        try:
            contents = cursor.execute(
                f"SELECT * FROM {table};"
            )

            return tuple(
                contents.fetchall()
            )
        # checks that the qurie was sucsessful if not it will pass the excetion
        except sqlite3.OperationalError as error_message:
            return error_message

    def __str__(self) -> str:
        """if you print the class you get a pointless string"""
        return str("hello this dose nothing but you can run other functions")
