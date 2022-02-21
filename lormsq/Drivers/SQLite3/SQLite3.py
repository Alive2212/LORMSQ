# TODO Important It should encrypted library like pysqlcipher3
import sqlite3

from ...DatabaseSQLAbstract import DatabaseSQLAbstract
from .Options import Options


class SQLite3(DatabaseSQLAbstract):

    def __init__(
            self,
            options: Options
    ) -> None:
        self.__options = options
        super(SQLite3, self).__init__(

        )

    def init_cursor(self):
        self.cursor = self.connection.cursor()

    def init_connection(self):
        if self.__options.in_memory:
            self.connection = sqlite3.connect(":memory:")
        else:
            self.connection = sqlite3.connect(self.__options.path)

    def close(self):
        self.cursor.close()
