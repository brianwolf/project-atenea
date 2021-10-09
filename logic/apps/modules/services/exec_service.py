import os
from importlib.machinery import ModuleSpec
from typing import Any, Dict, Tuple
from uuid import UUID, uuid4

from jinja2 import Template
from logic.apps.filesystem.services import workingdir_service
from logic.apps.modules.errors.module_error import ModuleError
from logic.apps.modules.models.module_model import Conf
from logic.apps.templates.services import template_service
from logic.libs.exception.exception import AppException
from logic.libs.reflection import reflection

from .garbage_collector import add_to_delete

_MODULES_PATH = '/logic/apps/repo_modules'


def exec(conf: Conf) -> Tuple[UUID, str]:

    id = workingdir_service.create()

    workindir = workingdir_service.fullpath(id)
    original_workindir = os.getcwd()

    template_path = template_service.template_path(conf.template)
    workingdir_service.copy_to_workingdir(id, template_path)

    try:
        os.chdir(workindir)

        in_path = _render_template(conf)
        out_path = conf.report

        module = _search_module(conf.from_var, conf.to_var)
        module.exec(in_path, out_path, conf.conf)

        os.chdir(original_workindir)

    except Exception as e:

        os.chdir(original_workindir)
        workingdir_service.delete(id)

        msj = str(e)
        raise AppException(ModuleError.CONVERT_ERROR, msj)

    add_to_delete(id)

    return id


def _search_module(from_var: str, to_var: str) -> ModuleSpec:

    modules = reflection.load_modules_by_path(_MODULES_PATH)
    for m in modules:
        if m.from_var == from_var.lower() and m.to_var == to_var.lower():
            return m

    msj = f'El modulo que cumpla con una conversion desde {from_var} a {to_var} no fue encontrado'
    raise AppException(ModuleError.MODULE_NOT_FOUND_ERROR, msj)


def _render_template(conf: Conf) -> str:

    with open(conf.file, 'r') as f:
        in_content = f.read()

    rendered_content = Template(in_content).render(conf.data)

    rendered_path = str(uuid4())
    with open(rendered_path, 'w') as f:
        f.write(rendered_content)

    return rendered_path
