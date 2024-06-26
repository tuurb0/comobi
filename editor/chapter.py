from editor.page import Page


class Chapter:
    def __init__(self, name, work_path, position):
        self.name = name
        self.position = position
        self.__work_path = work_path
        self.__pages: list[Page] = []

    @property
    def work_path(self):
        return self.__work_path

    @property
    def pages(self):
        return self.__pages

    def add_page(self, page: Page):
        self.__pages.append(page)
