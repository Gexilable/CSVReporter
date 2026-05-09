import csv
from pathlib import Path


def read_csv(*files: str | Path) -> list[dict]:
    for i in files:
        file = Path(i)
        if not file.exists():
            raise FileNotFoundError(f"File {file} does not exist")

    rows = []
    for file in files:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rows.append(row)
    return rows
