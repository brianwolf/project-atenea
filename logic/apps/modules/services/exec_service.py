import os
from importlib.util import module_from_spec, spec_from_file_location
from typing import Dict, List, Sized, Tuple
from uuid import UUID

from logic.apps.filesystem.services import workingdir_service
from logic.apps.modules.services import module_service
from logic.libs.exception.exception import AppException

from .garbage_collector import add_to_delete


def exec(module_name: str, data: Dict[str, str], in_path: str, out_path: str = 'report', conf: Dict[str, str] = {}) -> Tuple[UUID, str]:

    id = workingdir_service.create()

    try:
        original_workindir = os.getcwd()
        workindir = workingdir_service.fullpath(id)
        os.chdir(workindir)

        module_path = f'{module_service.get_path()}/{module_name}.py'

        spec = spec_from_file_location(module_name, module_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        result_paths =  module.exec(workindir, data, in_path, out_path, conf)

        os.chdir(original_workindir)

    except Exception as e:

        os.chdir(original_workindir)
        workingdir_service.delete(id)

        msj = str(e)
        raise AppException(PipelineError.EXECUTE_PIPELINE_ERROR, msj, e)

    if len(result_paths) > 1:
        any
        #zip
        out_path = 'zip path'

    add_to_delete(id)

    return id, out_path
