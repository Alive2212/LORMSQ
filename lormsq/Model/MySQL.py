import sys

from Kernel.Database.Model.DBDriverModel import DBDriverModel
import mysql.connector


class MySQL(DBDriverModel):
    def __init__(
            self,
            host: str = 'http://localhost',
            port: int = 3306,
            db_name: str = 'sample_db',
            user: str = 'root',
            password: str = 'root',
    ) -> None:
        super().__init__(db_name, 'mysql', user, password)

        ssl_disable_values = {
            "win": False,
            "linux": True,
            "darwin": True,
        }

        if sys.platform.lower() in ssl_disable_values:
            ssl_disable_value = ssl_disable_values[sys.platform.lower()]
        else:
            ssl_disable_value = True

        self.__db_connection = mysql.connector.connect(
            user=user,
            host=host,
            port=port,
            database=db_name,
            password=password,
            ssl_disabled=ssl_disable_value
        )
        self.__db_cursor = self.__db_connection.cursor(buffered=True)
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    @property
    def db_cursor(self):
        return self.__db_cursor

    @property
    def db_connection(self):
        return self.__db_connection
