import abc


class DatabaseOptionsAbstract:
    __metaclass__ = abc.ABCMeta

    def __init__(self) -> None:
        super(DatabaseOptionsAbstract, self).__init__()
