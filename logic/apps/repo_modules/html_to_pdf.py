import os
from typing import Dict

import pdfkit

from_var = 'HTML'
to_var = 'PDF'


def exec(in_path: str, out_path: str, conf: Dict[str, str]):

    if not in_path.endswith('.html'):
        os.rename(in_path, f'{in_path}.html')
        in_path += '.html'

    pdfkit.from_file(in_path, out_path, options=conf)
