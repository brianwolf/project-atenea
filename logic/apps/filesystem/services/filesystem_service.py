import os
import shutil
from typing import List


def get_file(path: str) -> bytes:
    with open(path, 'rb') as file:
        return file.read()


def create_file(path: str, content: bytes):
    with open(path, 'w') as file:
        file.write(content.decode('utf8'))


def delete_path(path: str):

    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.remove(path)


def move_file(path_in: str, path_out: str):
    shutil.move(path_in, path_out)


def name_files_from_path(path: str) -> List[str]:
    result = []
    for _, _, name_files in os.walk(path):
        result += name_files
    return result


def name_dirs_from_path(path: str) -> List[str]:
    result = []
    for _, name_dir, _ in os.walk(path):
        result += name_dir
    return result


def create_folder(path: str):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def exist_path(path: str) -> bool:
    return os.path.exists(path)
