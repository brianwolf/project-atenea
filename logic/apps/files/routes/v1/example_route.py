from flask import Blueprint, request
from flask.json import jsonify
from logic.apps.example.errors.example_error import ExampleError
from logic.apps.example.routes.v1.dtos import example_dto
from logic.apps.example.services import example_service
from logic.libs.exception.exception import AppException

blue_print = Blueprint('example', __name__, url_prefix='/api/v1/examples')


@blue_print.route('/', methods=['GET'])
def get():
    result = example_service.get_example()
    return example_dto.example_to_json(result)


@blue_print.route('/', methods=['POST'])
def post():
    m = example_dto.json_to_example(request.json)
    m = example_service.add(m)
    return example_dto.example_to_json(m), 201


@blue_print.route('/all', methods=['GET'])
def get_all():
    result = example_service.get_all()
    return jsonify([example_dto.example_to_json(o) for o in result]), 200


@blue_print.route('/errors/unknow', methods=['GET'])
def error_unknow():
    boom = 1 / 0
    return '', 200


@blue_print.route('/errors/business', methods=['GET'])
def error_business():
    try:
        1 / 0

    except Exception as e:
        raise AppException(
            code=ExampleError.EXAMPLE_RANDOM_ERROR,
            msj='BOOM...!!!',
            exception=e
        )

    return '', 200
