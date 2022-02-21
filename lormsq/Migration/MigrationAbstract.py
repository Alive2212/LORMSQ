import abc

from Bootstrap import App
from Kernel.Database.Migration import MigrationColumn


class MigrationAbstract:
    __metaclass__ = abc.ABCMeta
    __primary_keys: list[str]
    __column_list: list[str]

    def __init__(
            self,
            table_name: str,
    ) -> None:
        self.__primary_keys = []
        self.__column_list = []
        self.__table_name = table_name
        super(MigrationAbstract, self).__init__()

    def run(self, state: str = 'up'):
        if state == 'up':
            self.up()
        elif state == 'down':
            self.down()
        else:
            print("Noting to Do in Migrations")
            return
        self.exec()

    def exec(self):
        column_query_list = []
        column_foreign_query_list = []
        index_query_list = []
        for __column in self.column_list:
            prefix_str = " ".join(__column.prefixes)
            option_str = " ".join(__column.options)
            column_query = """{} {} {} {}""".format(
                str(prefix_str).upper(),
                __column.column,
                __column.data_type,
                option_str,
            )
            column_query_list.append(column_query.strip())
            if __column.foreign:
                column_foreign_query_list.append(
                    """,FOREIGN KEY ({}) REFERENCES {} ({}) ON DELETE {} ON UPDATE {}""".format(
                        __column.foreign.local_key,
                        __column.foreign.foreign_table,
                        __column.foreign.foreign_key,
                        __column.foreign.on_delete,
                        __column.foreign.on_update,
                    ))
            if __column.unique or __column.index:
                index_query_list.append("""CREATE {0} INDEX IF NOT EXISTS idx_{1}_{2} ON {1} ({2});""".format(
                    "UNIQUE" if __column.unique else "",
                    self.__table_name,
                    __column.column,
                ))

        query = """CREATE TABLE IF NOT EXISTS {} ({}, PRIMARY KEY ({}) {})""".format(
            self.__table_name,
            ",".join(column_query_list),
            ",".join(self.primary_keys),
            ",".join(column_foreign_query_list),
        )
        tmp = App.App().database.get_primary_sql().cursor.execute(query)
        print("here")

        # Execute Indexes
        for index_query in index_query_list:
            tmp = App.App().database.get_primary_sql().cursor.execute(index_query)
            print("here")

        print("test")

    @property
    def table_name(self):
        return self.__table_name

    @table_name.setter
    def table_name(self, value):
        self.__table_name = value

    @property
    def primary_keys(self):
        return self.__primary_keys

    @primary_keys.setter
    def primary_keys(self, value):
        self.__primary_keys = value

    @abc.abstractmethod
    def up(self):
        pass

    @abc.abstractmethod
    def down(self):
        pass

    @property
    def column_list(self):
        return self.__column_list

    @column_list.setter
    def column_list(self, value):
        self.__column_list = value
