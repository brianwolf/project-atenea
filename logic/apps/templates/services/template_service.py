
from datetime import datetime
from pathlib import Path
from typing import List
from uuid import uuid4

from logic.apps.filesystem.services import filesystem_service
from logic.apps.templates.errors.template_error import TemplateError
from logic.libs.exception.exception import AppException

_TEMPLATES_PATH = f'{Path.home()}/.atenea/templates'


def get(name: str) -> List[str]:

    path = f'{_TEMPLATES_PATH}/{name}'
    if not filesystem_service.exist_path(path):
        raise AppException(
            code=TemplateError.TEMPLATE_NOT_EXIST_ERROR,
            msj=f'No existe el template de nombre {name}'
        )

    return filesystem_service.name_files_from_path(path)


def add(name: str):
    path = f'{_TEMPLATES_PATH}/{name}'
    if filesystem_service.exist_path(path):
        raise AppException(
            code=TemplateError.TEMPLATE_ALREADY_EXIST_ERROR,
            msj=f'El template de nombre {name} ya existe'
        )
    filesystem_service.create_folder(path)


def delete(name: str):

    path = f'{_TEMPLATES_PATH}/{name}'
    if not filesystem_service.exist_path(path):
        raise AppException(
            code=TemplateError.TEMPLATE_NOT_EXIST_ERROR,
            msj=f'No existe el template de nombre {name}'
        )

    filesystem_service.delete_path(path)


def edit(name: str, new_name: str):

    path_old = f'{_TEMPLATES_PATH}/{name}'
    if not filesystem_service.exist_path(path_old):
        raise AppException(
            code=TemplateError.TEMPLATE_NOT_EXIST_ERROR,
            msj=f'No existe el template de nombre {name}'
        )
    path_new = f'{_TEMPLATES_PATH}/{new_name}'

    filesystem_service.move_file(path_old, path_new)


def list_all() -> List[str]:
    return filesystem_service.name_dirs_from_path(_TEMPLATES_PATH)


def template_path(name: str):
    return f'{_TEMPLATES_PATH}/{name}'
