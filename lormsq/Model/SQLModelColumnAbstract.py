from .SQLModelColumnTypeAbstract import SQLModelColumnTypeAbstract


class SQLModelColumnAbstract:
    def __init__(
            self,
            table_id: int,
            title: str,
            data_type: SQLModelColumnTypeAbstract,
            primary: bool = False,
            nullable: bool = True,
            index: bool = False,
    ) -> None:
        self.__table_id = table_id
        self.__title = title
        self.__data_type = data_type
        self.__primary = primary
        self.__nullable = nullable
        self.__index = index
        super().__init__()

    @property
    def table_id(self):
        return self.__table_id

    @table_id.setter
    def table_id(self, value):
        self.__table_id = value

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def data_type(self):
        return self.__data_type

    @data_type.setter
    def data_type(self, value):
        self.__data_type = value

    @property
    def primary(self):
        return self.__primary

    @primary.setter
    def primary(self, value):
        self.__primary = value

    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, value):
        self.__nullable = value

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value
