from comic.comic import Comic
from comic.chapter import Chapter
import pathlib
import os
from zipfile import ZipFile


class ZipComic:
    def __init__(self, path):
        self.path = path
        self.comic = Comic()
        self.work_dir = os.path.join(self.comic.temp_dir.name, '_zipcomic')
        self.__is_several_volumes = None

        # Init
        self.__unpack_comic()
        self.__is_several_volumes = self.__volume_checker()

    def __unpack_comic(self):
        with ZipFile(self.path, "r") as comiczip:
            comiczip.extractall(path=self.work_dir)

    def __volume_checker(self):
        files = os.listdir(self.work_dir)

        volume_counter = 0
        for i in files:
            i_files = os.path.join(self.work_dir, i)

            for y in os.listdir(i_files):
                y_files = os.path.join(i_files, y)

                if os.path.isdir(y_files):
                    volume_counter += 1

            if volume_counter:
                return True

        return False
