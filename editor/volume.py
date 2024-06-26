from editor.chapter import Chapter


class Volume:
    def __init__(self, name, work_path, position=0):
        self.name = name
        self.__work_path = work_path
        self.position = position
        self.__chapters: list[Chapter] = []

    @property
    def work_path(self):
        return self.__work_path

    @property
    def chapters(self):
        return self.__chapters

    def add_chapter(self, chapter: Chapter):
        self.__chapters.append(chapter)
