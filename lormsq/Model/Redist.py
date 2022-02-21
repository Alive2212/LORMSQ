from Kernel.Database.Model.DBDriverModel import DBDriverModel


class Redis(DBDriverModel):
    def __init__(
            self,
            host: str = 'http://localhost',
            port: int = 6379,
            db_name: str = '0',
            user: str = '',
            password: str = ''
    ) -> None:
        super().__init__(db_name, 'redis', user, password)
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
