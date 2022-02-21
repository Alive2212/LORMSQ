import abc

from .Model.SQLModel import SQLModel


class SkeletonAbstract:
    __metaclass__ = abc.ABCMeta

    def __init__(
            self,
            models: list[SQLModel] = []
    ) -> None:
        self.__models = models
        super(SkeletonAbstract, self).__init__()

    @abc.abstractmethod
    def get_skeleton(self):
        pass

    @property
    def models(self):
        return self.__models

    @models.setter
    def models(self, value):
        self.__models = value
