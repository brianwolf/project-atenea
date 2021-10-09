#!env/bin/python
from flask.app import Flask

from logic.apps.admin.config.logger import setup_loggers
from logic.apps.admin.config.rest import setup_rest
from logic.apps.admin.config.variables import Vars, setup_vars
from logic.apps.reports.services.garbage_collector import start_garbage_thread
from logic.libs.variables.variables import get_var

app = Flask(__name__)

setup_vars()
setup_loggers()
setup_rest(app)

start_garbage_thread()


if __name__ == "__main__":
    flask_host = get_var(Vars.PYTHON_HOST)
    flask_port = int(get_var(Vars.PYTHON_PORT))

    app.run(host=flask_host, port=flask_port, debug=False)
