import os
from importlib.machinery import ModuleSpec
from typing import Dict, Tuple
from uuid import UUID, uuid4

from jinja2 import Template
from logic.apps.modules.services import module_service
from logic.apps.reports.models.module_model import Conf
from logic.apps.templates.services import template_service


def exec(conf: Conf) -> Tuple[UUID, str]:

    working_dir = template_service.template_path(conf.template)
    in_file = render_template_by_conf(conf)
    out_file = conf.report

    module = module_service.search_module(conf.file, conf.report)

    final_path = module_service.exec(
        working_dir, module, in_file, out_file, conf.conf)

    os.remove(f'{working_dir}/{in_file}')

    return final_path


def render_template_in_new_file(template_path: str, data: Dict[str, str]) -> str:

    with open(template_path, 'r') as f:
        in_content = f.read()

    rendered_content = render_template(in_content, data)

    _, extension = os.path.splitext(template_path)

    id = str(uuid4()) + extension
    rendered_path = os.path.join(os.path.dirname(template_path), id)
    with open(rendered_path, 'w') as f:
        f.write(rendered_content)

    return id


def render_template(template_content: str, data: Dict[str, str]) -> str:
    return Template(template_content).render(data)


def render_template_by_conf(conf: Conf) -> str:

    working_dir = template_service.template_path(conf.template)

    in_path = os.path.join(working_dir, conf.file)
    return render_template_in_new_file(in_path, conf.data)
