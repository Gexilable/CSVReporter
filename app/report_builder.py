import csv
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

    def save_to_csv(self, filepath: str, fieldnames: list[str]):
        result = self.build()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result)


@dataclass
class ClickbaitReportBuilder(BaseReportBuilder):
    descending_order: bool = True
    sorting_parameter: Callable = lambda row: float(row['ctr'])
    filtering_parameter: Callable = lambda row: float(row["ctr"]) > 15 and float(row["retention_rate"]) < 40
