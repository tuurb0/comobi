from tempfile import TemporaryDirectory
from editor.volume import Volume
from xml.dom import minidom
import xml.etree.ElementTree as Xml
import uuid
import os


class Comic:
    def __init__(self, name='Untitled'):
        self.name = name
        self.description = None
        self.volumes: list[Volume] = []
        self.lang = 'en-US'
        self.__work_path = TemporaryDirectory('.tmp', 'COMOBI~')
        self.__src_dir = os.path.join(self.__work_path.name, 'src')
        self.__uuid = str(uuid.uuid4())
        self.__mimetype = "application/epub+zip"

        self.__sources_path = {
            'container.xml': os.path.join(os.path.join(self.__src_dir, "META-INF"), 'container.xml'),
            'content.opf': os.path.join(self.__src_dir, 'content.opf'),
            'toc.ncx': os.path.join(self.__src_dir, 'toc.ncx'),
            'style.css': os.path.join(self.__src_dir, 'style.css'),
            'mimetype': os.path.join(self.__src_dir, 'mimetype'),
            'pages': os.path.join(self.__src_dir, 'pages'),
            'images': os.path.join(self.__src_dir, 'images'),
            'META-INF': os.path.join(self.__src_dir, 'META-INF')
        }

        for volume in self.volumes:
            print(volume.name)

        os.mkdir(self.__src_dir)
        os.mkdir(self.__sources_path['META-INF'])
        os.mkdir(self.__sources_path['pages'])
        os.mkdir(self.__sources_path['images'])
        self.__create_meta_container(self.__sources_path['container.xml'])
        with open(self.__sources_path['mimetype'], "w", encoding='utf-8') as f:
            f.write(self.__mimetype)


    @property
    def work_path(self):
        return self.__work_path

    @property
    def sources_path(self):
        return self.__sources_path

    @staticmethod
    def __create_meta_container(path):
        container = Xml.Element("container", attrib={
            'version': '1.0',
            'xmlns': 'urn:oasis:names:tc:opendocument:xmlns:container'
        })
        rootfiles = Xml.SubElement(container, "rootfiles")
        Xml.SubElement(rootfiles, "rootfile", attrib={
            'full-path': 'content.opf',
            'media-type': 'application/oebps-package+xml'
        })

        file = minidom.parseString(Xml.tostring(container)).toprettyxml(indent="   ", encoding='utf-8')
        with open(path, "wb") as f:
            f.write(file)

    def __create_toc_ncx(self, path):
        ncx_attributes = {
            'version': '2005-1',
            'xml:lang': self.lang,
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
        Xml.SubElement(doc_title, "text", value=self.name)
        nav_map = Xml.Element("navMap")

        # If the book consists of several volumes
        if len(self.volumes) > 1:
            point_counter = 0
            for volume in self.volumes:
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
        elif len(self.volumes[0].chapters) > 1:
            point_counter = 0
            for chapter in self.volumes[0].chapters:
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

        file = minidom.parseString(Xml.tostring(ncx)).toprettyxml(indent='   ', encoding='utf-8')
        with open(path, "wb") as f:
            f.write(file)

    def make_navigation(self):
        self.__create_toc_ncx(self.__sources_path['toc.ncx'])


