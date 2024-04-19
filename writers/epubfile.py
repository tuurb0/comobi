import xml.etree.ElementTree as Xml
import uuid
import os
from editor.comic import Comic


class EPubFile:
    def __init__(self, comic: Comic):
        self.comic = comic
        self.__src_dir = os.path.join(self.comic.work_path.name, 'src')
        os.mkdir(self.__src_dir)
        self.__uuid = str(uuid.uuid4())
        self.__mimetype = "application/epub+zip"
        self.__meta_container = self.__create_meta_container()
        self.__toc_ncx = self.__create_toc_ncx()

    def get_data(self):
        print(f"{self.__mimetype}\n")
        print(f"{Xml.tostring(self.__meta_container, encoding='unicode')}\n")
        print(Xml.tostring(self.__toc_ncx, encoding='unicode'))

    @staticmethod
    def __create_meta_container():
        container = Xml.Element("container", attrib={
            'version': '1.0',
            'xmlns': 'urn:oasis:names:tc:opendocument:xmlns:container'
        })
        rootfiles = Xml.SubElement(container, "rootfiles")
        Xml.SubElement(rootfiles, "rootfile", attrib={
            'full-path': 'OEBPS/content.opf',
            'media-type': 'application/oebps-package+xml'
        })
        return container

    def __create_toc_ncx(self):
        comic = self.comic

        ncx_attributes = {
            'version': '2005-1',
            'xml:lang': comic.lang,
            'xmlns': 'http://www.daisy.org/z3986/2005/ncx/'
        }

        head_meta_attributes = [
            {'name': 'dtb:uid', 'content': f"urn:{self.__uuid}"},
            {'name': 'dtb:depth', 'content': '1'},
            {'name': 'dtb:totalPageCount', 'content': '0'},
            {'name': 'dtb:maxPageNumber', 'content': '0'},
            {'name': 'generated', 'content': 'true'},
        ]

        ncx = Xml.Element("ncx", attrib=ncx_attributes)
        head = Xml.Element("head")
        for head_meta_attrib in head_meta_attributes:
            Xml.SubElement(head, "meta", attrib=head_meta_attrib)

        doc_title = Xml.Element("docTitle")
        Xml.SubElement(doc_title, "text", value=comic.name)
        nav_map = Xml.Element("navMap")

        # If the book consists of several volumes
        if len(comic.volumes) > 1:
            point_counter = 0
            for volume in comic.volumes:
                point_counter += 1
                volume_nav_point = Xml.SubElement(nav_map, "navPoint", attrib={
                    'id': f"num_{point_counter}",
                    'playOrder': f"{point_counter}",
                    'class': 'chapter'
                })
                # TODO Add Content
                Xml.SubElement(Xml.SubElement(volume_nav_point, "navLabel"), "text", value=volume.name)

                for chapter in volume.chapters:
                    point_counter += 1
                    chapter_nav_point = Xml.SubElement(volume_nav_point, "navPoint", attrib={
                        'id': f"num_{point_counter}",
                        'playOrder': f"{point_counter}",
                        'class': 'chapter'
                    })
                    # TODO Add Content
                    Xml.SubElement(Xml.SubElement(chapter_nav_point, "navLabel"), "text", value=chapter.name)
        # If the book consists of one volume
        elif len(comic.volumes[0].chapters) > 1:
            point_counter = 0
            for chapter in comic.volumes[0].chapters:
                point_counter += 1
                chapter_nav_point = Xml.SubElement(nav_map, "navPoint", attrib={
                    'id': f"num_{point_counter}",
                    'playOrder': f"{point_counter}",
                    'class': 'chapter'
                })
                # TODO Add Content
                Xml.SubElement(Xml.SubElement(chapter_nav_point, "navLabel"), "text", value=chapter.name)
        # If the book consists of a single chapter
        else:
            print("Одна глава")

        ncx.append(head)
        ncx.append(doc_title)
        ncx.append(nav_map)

        return ncx
