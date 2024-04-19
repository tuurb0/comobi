import os
import subprocess
from parsers.archive import Archive

from writers.epub import EPubFile


def explorer_open_folder(url):
    subprocess.Popen(f'explorer /open,"{url}"')


def main():
    # zip_comic = Archive('C:\\Users\\tuurb\\Desktop\\Человек Бензопила\\Том 4 (Глава 26-34)\\Том 4 (Глава 26-34).zip')
    zip_comic = Archive('C:\\Users\\tuurb\\Desktop\\Человек Бензопила\\Том 4 (Глава 26-34)\\Включая тома (Глава 26-34).zip')
    comic = zip_comic.comic

    print(f"Folder: {comic.work_path.name}")

    explorer_open_folder(comic.work_path.name)

    input("Enter anyone")


if __name__ == "__main__":
    main()
