from logic.libs.reflection import reflection
from logic.libs.sqliteAlchemy import sqliteAlchemy
from logic.libs.variables.variables import get_var

from .variables import Vars


def setup_sqlite():

    sqliteAlchemy.setup(
        url=get_var(Vars.DB_SQLITE_PATH),
        echo=bool(get_var(Vars.DB_SQLITE_LOGS)))

    sqliteAlchemy.create_engine()

    reflection.load_modules_by_path('logic/apps/repositories/entities')
