from .SQLModelAbstract import SQLModelAbstract


class SQLModel(SQLModelAbstract):

    def get_item(self, condition: dict) -> 'SQLModelAbstract':
        pass

    def get_items(self, condition: dict) -> list['SQLModelAbstract']:
        pass

    def first_or_create(self, condition: dict) -> 'SQLModelAbstract':
        pass

    def update_item(self, condition: dict, values: dict) -> 'SQLModelAbstract':
        pass

    def update_items(self, condition: dict, values: dict) -> list['SQLModelAbstract']:
        pass

    def upsert_item(self, condition: dict, values: dict) -> 'SQLModelAbstract':
        pass

    def upsert_items(self, condition: dict, values: dict) -> list['SQLModelAbstract']:
        pass

    def execute_raw(self, query: str) -> object:
        pass