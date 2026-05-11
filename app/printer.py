import sys
from dataclasses import dataclass

from tabulate import tabulate


@dataclass
class Printer:
    data: list[dict]
    keys: list[str]

    def _filter_data(self) -> list[list]:
        result = []
        for row in self.data:
            result.append([row[k] for k in row if k in self.keys])
        return result

    def show_report(self):
        filtered_data = self._filter_data()
        print(tabulate(filtered_data, headers=self.keys, tablefmt="fancy_grid"))
