from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class BaseReportBuilder():
    data: list[dict]
    descending_order: Optional[bool] = None
    sorting_parameter: Callable = None
    filtering_parameter: Callable = None

    def build(self) -> list[dict]:
        filtered_data = list(filter(self.filtering_parameter, self.data))
        if self.sorting_parameter and self.descending_order:
            return sorted(filtered_data, key=self.sorting_parameter, reverse=self.descending_order)
        return filtered_data


@dataclass
class ClickbaitReportBuilder(BaseReportBuilder):
    descending_order: bool = True
    sorting_parameter: Callable = lambda row: float(row['ctr'])
    filtering_parameter: Callable = lambda row: float(row["ctr"]) > 15 and float(row["retention_rate"]) < 40
