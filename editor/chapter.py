from pathlib import Path


class Chapter:
    def __init__(self, name, work_dir, position):
        self.name = name
        self.position = position
        self.__work_dir = work_dir
        self.__pages = []
        self.__isCover = False

    @property
    def pages(self):
        return self.__pages

    @property
    def work_dir(self):
        return self.__work_dir

    @property
    def is_cover(self):
        return self.__isCover

    def add_page(self, page):
        self.__pages.append(page)

    def as_cover(self):
        self.__isCover = True
