from editor.chapter import Chapter


class Volume:
    def __init__(self, name, work_dir, position=0):
        self.name = name
        self.__work_dir = work_dir
        self.position = position
        self.__chapters: list[Chapter] = []

    @property
    def work_dir(self):
        return self.__work_dir

    @property
    def chapters(self):
        return self.__chapters

    def add_chapter(self, chapter: Chapter):
        self.__chapters.append(chapter)
