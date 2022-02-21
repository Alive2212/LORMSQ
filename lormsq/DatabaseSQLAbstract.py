import abc


class DatabaseSQLAbstract:
    __metaclass__ = abc.ABCMeta

    __cursor = None
    __connection = None

    def __init__(self) -> None:
        super(DBSQLAbstract, self).__init__()
        self.init_db()

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, value):
        self.__cursor = value

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value

    def init_db(self):
        self.init_connection()
        self.init_cursor()

    @abc.abstractmethod
    def init_connection(self):
        pass

    @abc.abstractmethod
    def init_cursor(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass
