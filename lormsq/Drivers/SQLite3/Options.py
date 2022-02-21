from ...DatabaseOptionsAbstract import DatabaseOptionsAbstract


class Options(DatabaseOptionsAbstract):
    def __init__(
            self,
            path: str = "db.sqlite",
            in_memory: bool = False,
            password: str = '123Z@ngeMadre3!!',
    ) -> None:
        self.__path = path
        self.__in_memory = in_memory
        self.__password = password
        super(Options, self).__init__()

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def in_memory(self):
        return self.__in_memory

    @in_memory.setter
    def in_memory(self, value):
        self.__in_memory = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
