import os
import shutil
from asyncio.log import logger
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import Dict

from logic.apps.reports.errors.report_error import ModuleError
from logic.libs.exception.exception import AppException
from logic.libs.reflection import reflection

_MODULES_PATH = 'logic/apps/repo_modules'


def exec(working_dir: str, module: ModuleType, in_file: str, out_file: str, conf: Dict[str, str]) -> str:

    original_workindir = os.getcwd()
    try:
        os.chdir(working_dir)
        module.exec(in_file, out_file, conf)
        os.chdir(original_workindir)

    except Exception as e:

        os.chdir(original_workindir)

        logger.exception(e)
        raise AppException(ModuleError.CONVERT_ERROR, str(e))

    final_path = f'/tmp/{out_file}'
    out_path = os.path.join(working_dir, out_file)
    shutil.move(out_path, final_path)

    return final_path


def search_module(in_file: str, out_file: str) -> ModuleSpec:

    _, from_var = os.path.splitext(in_file)
    _, to_var = os.path.splitext(out_file)

    from_var = from_var.replace('.', '').upper()
    to_var = to_var.replace('.', '').upper()

    modules = reflection.load_modules_by_path(_MODULES_PATH)
    for m in modules:
        if m.from_var == from_var and m.to_var == to_var:
            return m

    msj = f'El modulo que cumpla con una conversion desde {from_var} a {to_var} no fue encontrado'
    raise AppException(ModuleError.MODULE_NOT_FOUND_ERROR, msj)
