import abc


class DBDriverModel:
    __metaclass__ = abc.ABCMeta

    def __init__(
            self,
            db_name: str = 'sample_db',
            db_type: str = 'mysql',
            user: str = 'root',
            password: str = 'root',
    ) -> None:
        self.__db_name = db_name
        self.__db_type = db_type
        self.__user = user
        self.__password = password
        super(DBDriverModel, self).__init__()

    @property
    def db_name(self):
        return self.__db_name

    @db_name.setter
    def db_name(self, value):
        self.__db_name = value

    @property
    def db_type(self):
        return self.__db_type

    @db_type.setter
    def db_type(self, value):
        self.__db_type = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

