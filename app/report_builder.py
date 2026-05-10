from dataclasses import dataclass
from typing import Callable


@dataclass
class ReportBuilder:
    data: list
    sorting_parameter: Callable

    def build(self):
        return sorted(self.data, key=self.sorting_parameter, reverse=True)
