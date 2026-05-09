import csv
from pathlib import Path
from typing import List, Dict


def read_csv(file: str | Path) -> List[Dict]:
    file = Path(file)
    if not file.exists():
        raise FileNotFoundError(f"File {file} does not exist")

    rows = []

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            rows.append(row)

    return rows
