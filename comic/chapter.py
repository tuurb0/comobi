from comic.volume import Volume
from pathlib import Path


class Chapter:
    def __init__(self, name, work_dir, position, volume=None):
        self.name = name
        self.position = position
        self.__work_dir = work_dir
        self.__volume = volume
        self.__pages = []
        self.__isCover = False

        if volume is None:
            self.__volume = Volume('Untitled', Path(self.__work_dir).parent.absolute())

    @property
    def volume(self):
        return self.__volume

    @property
    def pages(self):
        return self.__pages

    @property
    def work_dir(self):
        return self.__work_dir

    @property
    def isCover(self):
        return self.__isCover

    def add_page(self, page):
        self.__pages.append(page)

    def as_cover(self):
        self.__isCover = True
