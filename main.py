import csv
from pathlib import Path
from typing import List, Dict


def read_csv(file: Path) -> List[Dict] :
    rows = []

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            rows.append(row)

    return rows
