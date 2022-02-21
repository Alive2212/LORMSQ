from ...DatabaseOptionsAbstract import DatabaseOptionsAbstract


class Options(DatabaseOptionsAbstract):
    def __init__(
            self,
            host: str = "localhost",
            port: int = 3306,
            user: str = 'root',
            password: str = '123Z@ngeMadre3!!',
            database: str = 'my_db'
    ) -> None:
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        super(Options, self).__init__()

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
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value
