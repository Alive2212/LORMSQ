class QueryCondition:
    def __init__(
            self,
            key: str,
            operator: str,
            value: str,
    ) -> None:
        self.__key = key,
        self.__operator = operator,
        self.__value = value
        super().__init__()

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        self.__operator = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value