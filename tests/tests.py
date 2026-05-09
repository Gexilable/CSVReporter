import csv

from main import read_csv


def test_read_one_csv_return_content(tmp_path):
    file = tmp_path / "test.csv"
    with open(file, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Ivan", "10"])

    result = read_csv(file)

    assert result[0]["name"] == "Ivan"
    assert result[0]["age"] == "10"


