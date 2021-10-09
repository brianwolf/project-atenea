from dataclasses import dataclass
from typing import Dict


@dataclass
class Conf:
    from_var: str
    to_var: str
    template: str
    file: str
    report: str = 'report'
    data: Dict[str, object] = {}
    conf: Dict[str, object] = {}
