from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Conf:
    from_var: str
    to_var: str
    template: str
    file: str
    report: str = 'report'
    data: Dict[str, object] = field(default_factory={})
    conf: Dict[str, object] = field(default_factory={})
