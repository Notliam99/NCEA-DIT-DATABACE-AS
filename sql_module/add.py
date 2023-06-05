""" can create objects in the database """
import sqlite3


class Add:
    """ adds rows to the database """
    # pylint: disable=inconsistent-return-statements,too-few-public-methods

    def __init__(self, database_connection: sqlite3.Connection) -> None:
        """gets the connection and saves it to a var"""
        self.connection = database_connection

    def insert_to_table(self, table_name: str, items: list or tuple):
        """insert a list of data into a table."""
        # Disable all the unused-variable violations in this function
        # pylint: disable=unused-variable
        question_marks = str()
        for i in items:
            question_marks += '?, '
        question_marks = question_marks.removesuffix(", ")
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"INSERT INTO {table_name} VALUES({question_marks});",
                items,
            )
            self.connection.commit()
        except sqlite3.OperationalError as error:
            return error
