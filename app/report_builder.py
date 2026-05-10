from dataclasses import dataclass
from typing import Callable


@dataclass
class ReportBuilder:
    data: list
    descending_order: bool = None
    sorting_parameter: Callable = None
    filtering_parameter: Callable = None

    def build(self) -> list[dict]:
        filtered_data = list(filter(self.filtering_parameter, self.data))
        if self.sorting_parameter:
            return sorted(filtered_data, key=self.sorting_parameter, reverse=self.descending_order)
        return filtered_data
