from readers.zipcomic import ZipComic
from writers.epubfile import EPubFile


def main():
    # zip_comic = ZipComic('C:\\Users\\tuurb\\Desktop\\Человек Бензопила\\Том 4 (Глава 26-34)\\Том 4 (Глава 26-34).zip')
    zip_comic = ZipComic('C:\\Users\\tuurb\\Desktop\\Человек Бензопила\\Том 4 (Глава 26-34)\\Включая тома (Глава 26-34).zip')
    comic = zip_comic.comic


    epub = EPubFile(comic)
    epub.get_data()
    # print(comic.comic.name)
    # print(comic.work_dir)

    # for volume in comic.comic.volumes:
    #     print(f"{volume.position}: {volume.name}")
    #     for chapter in volume.chapters:
    #         print(f"   {chapter.position}: {chapter.name}")
    #         # for page in chapter.pages:
    #         #     print(f"              {page}")


if __name__ == "__main__":
    main()
