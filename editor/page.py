class Page:
    def __init__(self, name, work_path, position):
        self.name = name
        self.position = position
        self.__work_path = work_path
        self.__isCover = False

    @property
    def work_path(self):
        return self.__work_path

    @property
    def is_cover(self):
        return self.__isCover

    def as_cover(self):
        self.__isCover = True
        self.position = 0
