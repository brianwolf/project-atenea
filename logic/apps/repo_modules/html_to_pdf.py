import os
from typing import Dict

import pdfkit

from_var = 'HTML'
to_var = 'PDF'


def exec(in_path: str, out_path: str, conf: Dict[str, str]):

    pdfkit.from_file(in_path, out_path, options=conf)
