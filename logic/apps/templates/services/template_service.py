
from datetime import datetime
from pathlib import Path
from typing import List
from uuid import uuid4

from logic.apps.filesystem.services import filesystem_service

_TEMPLATES_PATH = f'{Path.home()}/.atenea/templates'


def get(name: str) -> List[str]:
    """
    Devuelve un objeto de ejemplo
    """
    path = f'{_TEMPLATES_PATH}/{name}'
    return filesystem_service.name_files_from_path(path)


def add(name: str):
    path = f'{_TEMPLATES_PATH}/{name}'
    filesystem_service.create_folder(path)


def delete(name: str):
    path = f'{_TEMPLATES_PATH}/{name}'
    filesystem_service.delete_path(path)


def edit(name: str, new_name: str):
    path_old = f'{_TEMPLATES_PATH}/{name}'
    path_new = f'{_TEMPLATES_PATH}/{new_name}'
    filesystem_service.move_file(path_old, path_new)


def list_all() -> List[str]:
    return filesystem_service.name_files_from_path(_TEMPLATES_PATH)
