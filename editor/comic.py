from tempfile import TemporaryDirectory
from editor.volume import Volume


class Comic:
    def __init__(self, name='Untitled'):
        self.name = name
        self.description = None
        self.volumes: list[Volume] = []
        self.lang = 'en-US'

        self.__work_path = TemporaryDirectory('.tmp', 'COMOBI~')

    @property
    def work_path(self):
        return self.__work_path
