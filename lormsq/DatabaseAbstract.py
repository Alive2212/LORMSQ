import abc

from .DatabaseOptionsAbstract import DatabaseOptionsAbstract
from .SkeletonAbstract import SkeletonAbstract


class DatabaseAbstract:
    __metaclass__ = abc.ABCMeta

    def __init__(
            self,
            database_type: int,
            database_key: str,
            database_options: DatabaseOptionsAbstract,
            database=None,
    ) -> None:
        self.__database_type = database_type
        self.__database_key = database_key
        self.__database_options = database_options
        self.__database = database
        self.init_database()
        super(DatabaseAbstract, self).__init__()

    @abc.abstractmethod
    def init_database(self):
        pass

    @abc.abstractmethod
    def get_skeleton(self):
        return self.database_skeleton.get_skeleton()

    @property
    def database_type(self):
        return self.__database_type

    @database_type.setter
    def database_type(self, value):
        self.__database_type = value

    @property
    def database_key(self):
        return self.__database_key

    @database_key.setter
    def database_key(self, value):
        self.__database_key = value

    @property
    def database_options(self):
        return self.__database_options

    @database_options.setter
    def database_options(self, value):
        self.__database_options = value

    @property
    def database_skeleton(self) -> SkeletonAbstract:
        return self.__database_skeleton

    @database_skeleton.setter
    def database_skeleton(self, value: SkeletonAbstract):
        self.__database_skeleton = value

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value
