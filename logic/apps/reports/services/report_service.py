import os
from importlib.machinery import ModuleSpec
from typing import Tuple
from uuid import UUID, uuid4

from jinja2 import Template
from logic.apps.modules.services import module_service
from logic.apps.reports.errors.report_error import ModuleError
from logic.apps.reports.models.module_model import Conf
from logic.apps.templates.services import template_service
from logic.libs.exception.exception import AppException
from logic.libs.reflection import reflection

_MODULES_PATH = 'logic/apps/repo_modules'


def exec(conf: Conf) -> Tuple[UUID, str]:

    working_dir = template_service.template_path(conf.template)
    in_file = render_template(conf)
    out_file = conf.report

    module = _search_module(conf.file, conf.report)

    final_path = module_service.exec(
        working_dir, module, in_file, out_file, conf.conf)

    os.remove(f'{working_dir}/{in_file}')

    return final_path


def _search_module(in_file: str, out_file: str) -> ModuleSpec:

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


def render_template(conf: Conf) -> str:

    working_dir = template_service.template_path(conf.template)

    in_path = f'{working_dir}/{conf.file}'
    with open(in_path, 'r') as f:
        in_content = f.read()

    rendered_content = Template(in_content).render(conf.data)

    _, extension = os.path.splitext(conf.file)

    id = str(uuid4()) + extension
    rendered_path = f'{working_dir}/{id}'
    with open(rendered_path, 'w') as f:
        f.write(rendered_content)

    return str(id)
