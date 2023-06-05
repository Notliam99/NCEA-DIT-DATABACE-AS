"""helps people with gruby hands get data"""
import sqlite3


class Get:
    """Class for getting things from a database"""
    # disable the violation bellow becuse i have not time
    # pylint: disable=too-few-public-methods

    def __init__(self, database_connection: sqlite3.Connection) -> None:
        self.connection = database_connection

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
