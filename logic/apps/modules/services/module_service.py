import os
import shutil
from asyncio.log import logger
from types import ModuleType
from typing import Dict

from logic.apps.reports.errors.report_error import ModuleError
from logic.libs.exception.exception import AppException


def exec(working_dir: str, module: ModuleType, in_file: str, out_file: str, conf: Dict[str, str]) -> str:

    original_workindir = os.getcwd()
    in_path = f'{working_dir}/{in_file}'
    out_path = f'{working_dir}/{out_file}'

    try:
        os.chdir(working_dir)
        module.exec(in_path, out_path, conf)
        os.chdir(original_workindir)

    except Exception as e:

        os.chdir(original_workindir)

        logger.exception(e)
        raise AppException(ModuleError.CONVERT_ERROR, str(e))

    final_path = f'/tmp/{out_file}'
    shutil.move(out_path, final_path)

    return final_path
