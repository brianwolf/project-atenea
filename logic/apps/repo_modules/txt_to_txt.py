import os
import shutil
from typing import Dict

from_var = 'TXT'
to_var = 'TXT'


def exec(in_path: str, out_path: str, conf: Dict[str, str]):
    shutil.copy(in_path, out_path)
