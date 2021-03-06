from io import BytesIO

from flask import Blueprint, jsonify, request, send_file
from logic.apps.reports.models.module_model import Conf
from logic.apps.reports.services import report_service
from logic.apps.templates.services import template_service

blue_print = Blueprint(
    'report', __name__, url_prefix='/api/v1/reports')


@blue_print.route('/', methods=['POST'])
def post():
    j = request.json
    conf = Conf(
        template=j['template'],
        file=j['file'],
        report=j.get('report', 'report'),
        data=j.get('data', {}),
        conf=j.get('conf', {}),
        workingdir=template_service.template_path(j['template'])
    )
    path = report_service.exec(conf)

    with open(path, 'rb') as f:
        result = f.read()

    return send_file(BytesIO(result),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=conf.report)
