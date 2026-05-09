import csv


def read_csv(file):
    rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            rows.append(row)

    return rows
