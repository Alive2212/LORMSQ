from Kernel.Database.Migration.MigrationForeginKey import MigrationForeignKey


class MigrationColumn:
    def __init__(
            self,
            column: str,
            data_type: str,
            options: list,
            prefixes: list = None,
            index: bool = False,
            unique: bool = False,
            foreign: MigrationForeignKey = None
    ) -> None:
        self.__prefixes = prefixes
        self.__column = column
        self.__data_type = data_type
        self.__options = options
        self.__index = index or unique
        self.__unique = unique
        self.__foreign = foreign
        super().__init__()

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        self.__column = value

    @property
    def data_type(self):
        return self.__data_type

    @data_type.setter
    def data_type(self, value):
        self.__data_type = value

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, value):
        self.__options = value

    @property
    def prefixes(self):
        return self.__prefixes

    @prefixes.setter
    def prefixes(self, value):
        self.__prefixes = value

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, value):
        if value:
            self.__index = True
        self.__unique = value

    @property
    def foreign(self):
        return self.__foreign

    @foreign.setter
    def foreign(self, value):
        self.__foreign = value
