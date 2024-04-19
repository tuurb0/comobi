from tempfile import TemporaryDirectory
import random


class Comic:
    def __init__(self, name='Untitled'):
        self.__name = name
        self.__description = None
        self.__chapters = None

        self.__temp_dir = TemporaryDirectory('.tmp', 'COMOBI~')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def chapters(self):
        return self.__chapters


    @property
    def temp_dir(self):
        return self.__temp_dir
