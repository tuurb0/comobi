import utils.image as img

import os


class Page:
    def __init__(self, name, orig_path, position, src_path):
        self.name = name
        self.position = position
        self.__orig_path = orig_path
        self.__sources_path = {
            'images': src_path['images'],
            'pages': src_path['pages']
        }
        self.__isCover = False

        img.convert(self.__orig_path, self.src_image_path)

    @property
    def orig_path(self):
        return self.__orig_path

    @property
    def src_image_path(self):
        return os.path.join(self.__sources_path['images'], f"{self.position}.jpg")

    @property
    def src_page_path(self):
        return os.path.join(self.__sources_path['pages'], f"{self.position}.html")

    @property
    def is_cover(self):
        return self.__isCover

    def as_cover(self):
        self.__isCover = True
        self.position = 0
