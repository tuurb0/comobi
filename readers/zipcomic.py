from editor.comic import Comic
from editor.chapter import Chapter
from editor.volume import Volume
from editor.page import Page

import os
from zipfile import ZipFile


class ZipComic:
    def __init__(self, file):
        self.file = file
        self.comic = Comic(self.__get_file_name())
        self.__work_dir = os.path.join(self.comic.work_path.name, '.zip')
        self.__unpack_comic_to_temp_folder()
        self.__is_several_volumes = self.__volume_check()
        self.comic.volumes = self.__load_comic_structure()

    @property
    def work_dir(self):
        return self.__work_dir

    def __unpack_comic_to_temp_folder(self):
        with ZipFile(self.file, "r") as comic_zip:
            comic_zip.extractall(path=self.__work_dir)

    def __get_file_name(self):
        file_name = os.path.basename(self.file)
        i = file_name.rfind('.')
        if i != -1:
            return file_name[:i]

    def __volume_check(self):
        files = os.listdir(self.__work_dir)
        volume_counter = 0

        for i in files:
            i_files = os.path.join(self.__work_dir, i)

            for y in os.listdir(i_files):
                y_files = os.path.join(i_files, y)
                if os.path.isdir(y_files):
                    volume_counter += 1
            if volume_counter:
                return True

        return False

    def __load_comic_structure(self):
        volumes = []
        # If more than one volume
        page_counter = 0
        if self.__is_several_volumes:
            files = os.listdir(self.__work_dir)
            # Volumes
            for i in files:
                i_files = os.path.join(self.__work_dir, i)
                volume = Volume(i, i_files, files.index(i))
                # Chapters
                for y in os.listdir(i_files):
                    y_files = os.path.join(i_files, y)
                    chapter = None
                    # Pages
                    if os.path.isdir(y_files):
                        chapter = Chapter(y, y_files, os.listdir(i_files).index(y))
                        for z in os.listdir(y_files):
                            z_files = os.path.join(y_files, z)
                            page_counter += 1
                            chapter.add_page(Page(z, z_files, page_counter))
                    elif len(list(os.listdir(i_files))) == 1:
                        chapter = Chapter(y, i_files, 0)
                        page_counter += 1
                        chapter.add_page(Page(y, y_files, page_counter))
                    else:
                        print('Error: Failure structure')

                    volume.add_chapter(chapter)
                volumes.append(volume)
        # If only one volume
        else:
            volume = Volume(self.__get_file_name(), self.work_dir, 0)
            files = os.listdir(self.__work_dir)

            # Chapter
            for i in files:
                i_files = os.path.join(self.__work_dir, i)
                chapter = Chapter(i, i_files, files.index(i))
                # Pages
                for y in os.listdir(i_files):
                    y_files = os.path.join(i_files, y)
                    page_counter += 1
                    chapter.add_page(Page(y, y_files, page_counter))
                volume.add_chapter(chapter)

            volumes.append(volume)

        return volumes
