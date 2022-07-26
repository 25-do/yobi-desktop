import logging
import sqlite3
class SQLite_CONTEX_MANAGER:
    """contex manager class to ensure the database connection is always closed
        Basic Usage
>>>       with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\stats\\yobi_database.db") as cusr:
    """
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)
    def __enter__(self):
        logging.info("calling __enter__")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("calling __exit__")
        self.connection.commit()
        self.connection.close()