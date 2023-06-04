"""helps people with gruby hands get data"""
import sqlite3


class Get:
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
        cursor = self.connection.cursor()
        try:
            contents = cursor.execute(
                "SELECT * FROM {} ;".format(table)
            )

            return tuple(
                contents.fetchall()
            )
        except Exception as exception:
            return exception.__repr__()

    def __str__(self) -> str:
        return str("hello this dose nothing but you can run other functions")
