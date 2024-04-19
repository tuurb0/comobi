from readers.zipcomic import ZipComic


def main():
    comic = ZipComic('C:\\Users\\tuurb\\Desktop\\Человек Бензопила\\Том 4 (Глава 26-34)\\Том 4 (Глава 26-34).zip')
    # comic = ZipComic('C:\\Users\\tuurb\\Desktop\\Человек Бензопила\\Том 4 (Глава 26-34)\\Включая тома (Глава 26-34).zip')

    # print(comic.comic.name)
    # print(comic.work_dir)

    for volume in comic.comic.volumes:
        print(f"{volume.work_dir}")
        for chapter in volume.chapters:
            print(f"       {chapter.work_dir}")
            for page in chapter.pages:
                print(f"              {page}")


if __name__ == "__main__":
    main()
