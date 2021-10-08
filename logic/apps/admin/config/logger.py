from logic.libs.logger.logger import Config, setup
from logic.libs.variables.variables import get_var

from .variables import Vars


def setup_loggers():
    setup([
        Config(
            name='app',
            path=get_var(Vars.LOGS_PATH),
            level=get_var(Vars.LOGS_LEVEL),
            file_backup_count=int(get_var(Vars.LOGS_BACKUPS))
        )
    ])
