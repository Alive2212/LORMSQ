import abc

from .SQLModelColumnAbstract import SQLModelColumnAbstract



class SQLModelAbstract:
    __metaclass__ = abc.ABCMeta

    __query: str = ''

    def __init__(
            self,
            table_name: str,
            columns: list[SQLModelColumnAbstract] = []
    ) -> None:
        self.__table_name = table_name
        self.__columns = columns
        super().__init__()

    @property
    def table_name(self):
        return self.__table_name

    @table_name.setter
    def table_name(self, value):
        self.__table_name = value

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        self.__columns = value

    @abc.abstractmethod
    def get_item(self, condition: dict) -> 'SQLModelAbstract':
        """This methode should implement"""
        return

    @abc.abstractmethod
    def get_items(self, condition: dict) -> list['SQLModelAbstract']:
        """This methode should implement"""
        return []

    @abc.abstractmethod
    def first_or_create(self, condition: dict) -> 'SQLModelAbstract':
        """This methode should implement"""
        return

    @abc.abstractmethod
    def update_item(self, condition: dict, values: dict) -> 'SQLModelAbstract':
        """This methode should implement"""
        return

    @abc.abstractmethod
    def update_items(self, condition: dict, values: dict) -> list['SQLModelAbstract']:
        """This methode should implement"""
        return []

    @abc.abstractmethod
    def upsert_item(self, condition: dict, values: dict) -> 'SQLModelAbstract':
        """This methode should implement"""
        return

    @abc.abstractmethod
    def upsert_items(self, condition: dict, values: dict) -> list['SQLModelAbstract']:
        """This methode should implement"""
        return []

    @abc.abstractmethod
    def execute_raw(self, query: str) -> object:
        """This methode should implement"""
        return
