from tempfile import TemporaryDirectory
import os
from editor.volume import Volume


class Comic:
    def __init__(self, name='Untitled'):
        self.name = name
        self.description = None
        self.volumes: list[Volume] = []
        self.lang = 'en-US'

        self.__temp_dir = TemporaryDirectory('.tmp', 'COMOBI~')
        self.__src_dir = os.path.join(self.__temp_dir.name, '.src')

    @property
    def temp_dir(self):
        return self.__temp_dir
