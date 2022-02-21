from Kernel.Database.Model.DBDriverModel import DBDriverModel


class Postgres(DBDriverModel):
    def __init__(
            self,
            host: str = 'http://localhost',
            port: int = 5432,
            db_name: str = 'sample_db',
            user: str = 'root',
            password: str = 'root'
    ) -> None:
        super().__init__(db_name, 'postgres', user, password)
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

