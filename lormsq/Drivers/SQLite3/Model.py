from Model.SQLModelAbstract import SQLModelAbstract


class SQLite3Model(SQLModelAbstract):
    def get_item(self, condition: dict) -> 'DBModel':
        pass

    def get_items(self, condition: dict) -> list['DBModel']:
        pass

    def first_or_create(self, condition: dict) -> 'DBModel':
        pass

    def update_item(self, condition: dict, values: dict) -> 'DBModel':
        pass

    def update_items(self, condition: dict, values: dict) -> list['DBModel']:
        pass

    def upsert_item(self, condition: dict, values: dict) -> 'DBModel':
        pass

    def upsert_items(self, condition: dict, values: dict) -> list['DBModel']:
        pass

    def execute_raw(self, query: str) -> object:
        pass
