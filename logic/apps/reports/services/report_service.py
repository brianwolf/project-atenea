import os
from typing import Dict
from uuid import uuid4

from jinja2 import Template
from logic.apps.modules.services import module_service
from logic.apps.reports.models.module_model import Conf


def exec(conf: Conf) -> str:

    in_file = render_template_by_conf(conf)
    out_file = conf.report

    module = module_service.search_module(conf.file, conf.report)

    final_path = module_service.exec(
        conf.workingdir, module, in_file, out_file, conf.conf)

    os.remove(f'{conf.workingdir}/{in_file}')

    return final_path


def render_template_by_conf(conf: Conf) -> str:

    in_path = os.path.join(conf.workingdir, conf.file)
    return render_template_in_new_file(in_path, conf.data)


def render_template_in_new_file(file_path: str, data: Dict[str, str]) -> str:

    with open(file_path, 'r') as f:
        in_content = f.read()

    rendered_content = Template(in_content).render(data)

    _, extension = os.path.splitext(file_path)

    file_rendered_name = str(uuid4()) + extension
    rendered_path = os.path.join(
        os.path.dirname(file_path), file_rendered_name)

    with open(rendered_path, 'w') as f:
        f.write(rendered_content)

    return file_rendered_name
