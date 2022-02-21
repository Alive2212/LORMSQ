from .DatabaseAbstract import DatabaseAbstract
from .DatabaseOptionsAbstract import DatabaseOptionsAbstract
from .DatabaseSQLAbstract import DatabaseSQLAbstract
from .Drivers.MySQL.MySQL import MySQL
from .Drivers.SQLite3.SQLite3 import SQLite3


class Database(DatabaseAbstract):

    def __init__(
            self,
            database_type: int,
            database_key: str,
            database_options: DatabaseOptionsAbstract,
    ) -> None:
        self.init_database()
        super(Database, self).__init__(
            database_type=database_type,
            database_key=database_key,
            database_options=database_options,
            database=None,
        )

    def init_database(self):
        if self.database_key == 'sqlite3':
            self.database = SQLite3(options=self.database_options)

        elif self.database_key == 'mysql':
            self.database = MySQL(options=self.database_options)

    def get_skeleton(self):
        self.database.get_skeleton()


class DatabaseSQL(DatabaseSQLAbstract):

    def init_connection(self):
        pass

    def init_cursor(self):
        pass

    def close(self):
        pass


class DatabaseNoSQL:

    def __init__(self) -> None:
        super().__init__()


class Type:
    SQL: int = 0
    NO_SQL: int = 1
    KEY_VALUE: int = 2
