from tinydb import TinyDB, Query
from Kernel.Database.Model.DBDriverModel import DBDriverModel


class TinyDB(DBDriverModel):
    __db = None

    def __init__(
            self,
            path: str = "Store/DBs/local_nosql.json",
            db_name: str = 'sample_db',
            user: str = 'root',
            password: str = 'root',
    ) -> None:
        super().__init__(db_name, 'tinydb', user, password)
        self.__path = path
        self.init_db()

    def init_db(self):
        self.__db = TinyDB(self.__path)

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value
