class MigrationForeignKey:

    def __init__(
            self,
            local_key: str,
            foreign_key: str,
            foreign_table: str,
            on_delete: str = 'SET NULL',
            on_update: str = 'CASCADE',
    ) -> None:
        self.__local_key = local_key
        self.__foreign_key = foreign_key
        self.__foreign_table = foreign_table
        self.__on_delete = on_delete
        self.__on_update = on_update
        super(MigrationForeignKey, self).__init__()

    @property
    def local_key(self):
        return self.__local_key

    @local_key.setter
    def local_key(self, value):
        self.__local_key = value

    @property
    def foreign_key(self):
        return self.__foreign_key

    @foreign_key.setter
    def foreign_key(self, value):
        self.__foreign_key = value

    @property
    def foreign_table(self):
        return self.__foreign_table

    @foreign_table.setter
    def foreign_table(self, value):
        self.__foreign_table = value

    @property
    def on_delete(self):
        return self.__on_delete

    @on_delete.setter
    def on_delete(self, value):
        self.__on_delete = value

    @property
    def on_update(self):
        return self.__on_update

    @on_update.setter
    def on_update(self, value):
        self.__on_update = value
