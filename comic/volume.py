class Volume:
    def __init__(self, name, work_dir, position=0):
        self.name = name
        self.__work_dir = work_dir
        self.position = position
        self.__chapters = []

    @property
    def work_dir(self):
        return self.__work_dir

    @property
    def chapters(self):
        return self.__chapters

    def add_chapter(self, chapter):
        self.__chapters.append(chapter)
