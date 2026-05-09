import csv
from dataclasses import dataclass
from pathlib import Path

from app.exceptions import HeadersError


@dataclass
class CsvReader:
    schema: str | None

    def read(self, *files: str | Path):
        for file in files:
            file = Path(file)
            if not file.exists():
                raise FileNotFoundError(f"File {file} does not exist")

        rows = []
        for file in files:
            with open(file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames is not self.schema:
                    raise HeadersError(f'File {file} does not have the correct schema')
                for row in reader:
                    rows.append(row)
        return rows
