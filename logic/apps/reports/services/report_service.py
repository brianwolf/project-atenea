import os
from importlib.machinery import ModuleSpec
from typing import Tuple
from uuid import UUID, uuid4

from jinja2 import Template
from logic.apps.modules.services import module_service
from logic.apps.reports.models.module_model import Conf
from logic.apps.templates.services import template_service


def exec(conf: Conf) -> Tuple[UUID, str]:

    working_dir = template_service.template_path(conf.template)
    in_file = render_template(conf)
    out_file = conf.report

    module = module_service.search_module(conf.file, conf.report)

    final_path = module_service.exec(
        working_dir, module, in_file, out_file, conf.conf)

    os.remove(f'{working_dir}/{in_file}')

    return final_path


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
