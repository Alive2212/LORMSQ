class SQLModelColumnTypeAbstract:
    def __init__(
            self,
            title: str,
            len_values,
            attributes: str = None
    ) -> None:
        self.__title = title
        self.__len_values = len_values
        self.__attributes = attributes
        super().__init__()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def len_values(self):
        return self.__len_values

    @len_values.setter
    def len_values(self, value):
        self.__len_values = value

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        self.__attributes = value
