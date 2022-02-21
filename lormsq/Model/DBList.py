import Kernel.Database.Model.DBDriverModel as DBModel
from Kernel.Database import DBSQLAbstract
from Kernel.Database.Model.MySQL import MySQL


class DBList:

    def __init__(self, database_list: list = []) -> None:
        self.__database_list = database_list
        super().__init__()

    @property
    def database_list(self):
        return self.__database_list

    @database_list.setter
    def database_list(self, value: list):
        self.__database_list = value

    def add_database_to_list(self, database_model: DBModel):
        self.__database_list.append(database_model)

    def get_mysqls(self) -> list:
        results = []
        for __database in self.__database_list:
            if __database.db_type in ['mysql', 'sqlite3']:
                tmp = __database.db_type
                results.append(__database)
        return results

    # TODO important set type of output
    def get_primary_sql(self) -> DBSQLAbstract:
        if len(self.get_mysqls()):
            return self.get_mysqls()[0]
        return None

    # TODO important set type of output
    def get_primary_db(self):
        return self.database_list[0]
