from flask import Blueprint, request
from flask.json import jsonify
from logic.apps.templates.services import template_service

blue_print = Blueprint('templates', __name__, url_prefix='/api/v1/templates')


@blue_print.route('/<name>', methods=['GET'])
def get(name: str):
    result = template_service.get(name)
    return jsonify(result), 200


@blue_print.route('/<name>', methods=['POST'])
def add(name: str):
    template_service.add(name)
    return '', 201


@blue_print.route('/<name>', methods=['DELETE'])
def delete(name: str):
    template_service.delete(name)
    return '', 200


@blue_print.route('/', methods=['GET'])
def list_all():
    result = template_service.list_all()
    return jsonify(result), 200
