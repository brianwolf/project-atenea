from io import BytesIO

from flask import Blueprint, jsonify, request, send_file
from logic.apps.files.services import file_service

blue_print = Blueprint(
    'files', __name__, url_prefix='/api/v1/templates/<template_name>/files')


@blue_print.route('', methods=['GET'])
def list_all(template_name: str):
    result = file_service.list_all(template_name)
    return jsonify(result), 200


@blue_print.route('/<file_name>', methods=['GET'])
def get(template_name: str, file_name: str):
    result = file_service.get(template_name, file_name)
    return result, 200


@blue_print.route('/<file_name>/bytes', methods=['GET'])
def get_bytes(template_name: str, file_name: str):
    result = file_service.get_bytes(template_name, file_name)

    return send_file(BytesIO(result),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=file_name)


@blue_print.route('/<file_name>/img', methods=['GET'])
def get_img(template_name: str, file_name: str):
    result = file_service.get_bytes(template_name, file_name)

    return send_file(BytesIO(result),
                     mimetype='image/jpeg',
                     as_attachment=True,
                     attachment_filename=file_name)


@blue_print.route('/<file_name>/base64', methods=['GET'])
def get_base64(template_name: str, file_name: str):
    result = file_service.get_base64(template_name, file_name)
    return result, 200


@blue_print.route('/<file_name>', methods=['POST'])
def post(template_name: str, file_name: str):
    content = request.data
    file_service.add(template_name, file_name, content)
    return '', 200


@blue_print.route('/<file_name>', methods=['DELETE'])
def delete(template_name: str, file_name: str):
    file_service.delete(template_name, file_name)
    return '', 200
