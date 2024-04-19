import xml.etree.ElementTree as Xml
import uuid
import os
from editor.comic import Comic


class EPubFile:
    def __init__(self, comic: Comic):
        self.comic = comic
        self.__src_dir = os.path.join(self.comic.work_path.name, 'src')
        os.mkdir(self.__src_dir)
