
import base64
from typing import List

from logic.apps.files.errors.file_error import FileError
from logic.apps.filesystem.services import filesystem_service
from logic.apps.templates.services import template_service
from logic.libs.exception.exception import AppException


def get(template_name: str, file_name: str) -> str:

    template_service.get(template_name)

    path = f'{template_service.template_path(template_name)}/{file_name}'
    if not filesystem_service.exist_path(path):
        raise AppException(
            code=FileError.FILE_NOT_EXIST_ERROR,
            msj=f'No existe el archivo de nombre {file_name}'
        )
    return filesystem_service.get_file(path).decode('utf8')


def get_bytes(template_name: str, file_name: str) -> bytes:

    template_service.get(template_name)

    path = f'{template_service.template_path(template_name)}/{file_name}'
    if not filesystem_service.exist_path(path):
        raise AppException(
            code=FileError.FILE_NOT_EXIST_ERROR,
            msj=f'No existe el archivo de nombre {file_name}'
        )
    return filesystem_service.get_file(path)


def get_base64(template_name: str, file_name: str) -> bytes:

    template_service.get(template_name)

    result = get_bytes(template_name, file_name)
    return base64.b64encode(result)


def add(template_name: str, file_name: str, content: bytes):

    template_service.get(template_name)

    path = f'{template_service.template_path(template_name)}/{file_name}'
    if filesystem_service.exist_path(path):
        raise AppException(
            code=FileError.FILE_ALREADY_EXIST_ERROR,
            msj=f'El archivo de nombre {file_name} ya existe'
        )
    filesystem_service.create_file(path, content)


def delete(template_name: str, file_name: str):

    template_service.get(template_name)

    path = f'{template_service.template_path(template_name)}/{file_name}'
    if not filesystem_service.exist_path(path):
        raise AppException(
            code=FileError.FILE_NOT_EXIST_ERROR,
            msj=f'No existe el archivo de nombre {file_name}'
        )
    filesystem_service.delete_path(path)


def list_all(template_name: str) -> List[str]:

    return template_service.list_all()
