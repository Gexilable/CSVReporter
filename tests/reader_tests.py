import csv

import pytest

from app.csv_reader import CsvReader
from app.exceptions import HeadersError

test_schema = ["test_col", "another_test_col"]
reader_with_scheme = CsvReader(schema=test_schema)
reader_without_scheme = CsvReader()


def test_read_one_csv_return_content(tmp_path):
    file = tmp_path / "test.csv"
    with open(file, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Ivan", "10"])

    result = reader_without_scheme.read(file)

    assert result[0]["name"] == "Ivan"
    assert result[0]["age"] == "10"


def test_read_non_existent_csv_raises_notfound_exception(tmp_path):
    file = tmp_path / "test.csv"

    with pytest.raises(FileNotFoundError) as e:
        reader_without_scheme.read(file)


def test_read_csv_raises_type_error_on_invalid_type():
    with pytest.raises(TypeError) as e:
        reader_without_scheme.read(123)  # type: ignore[arg-type]


def test_read_few_csv(tmp_path):
    first_file = tmp_path / "first.csv"
    second_file = tmp_path / "second.csv"

    with (
        open(first_file, "w", encoding='utf-8', newline='') as f1,
        open(second_file, "w", encoding='utf-8', newline='') as f2,
    ):
        writer = csv.writer(f1)
        writer.writerow(["name", "age"])
        writer.writerow(["Ivan", "10"])

        writer = csv.writer(f2)
        writer.writerow(["name", "age"])
        writer.writerow(["Olga", "12"])

    result = reader_without_scheme.read(first_file, second_file)

    assert result[0]["name"] == "Ivan"
    assert result[0]["age"] == "10"
    assert result[1]["name"] == "Olga"
    assert result[1]["age"] == "12"


def test_read_csv_file_with_invalid_headers_raises_headers_error(tmp_path):
    file = tmp_path / "test.csv"

    with open(file, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Ivan", "10"])

    with pytest.raises(HeadersError, match=f'File .+ does not have the correct schema'):
        reader_with_scheme.read(file)


def test_read_csv_file_with_valid_headers_not_raises_headers_error(tmp_path):
    file = tmp_path / "test.csv"

    with open(file, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["test_col", "another_test_col"])
        writer.writerow(["Ivan", "10"])

    result = reader_with_scheme.read(file)

    assert result[0]["test_col"] == "Ivan"
    assert result[0]["another_test_col"] == "10"
