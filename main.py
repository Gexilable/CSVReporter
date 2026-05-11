import argparse

from app.csv_reader import CsvReader
from app.models import base_schema
from app.printer import Printer

from app.report_builders import REPORT_BUILDERS

reader = CsvReader(schema=base_schema)

parser = argparse.ArgumentParser()
parser.add_argument("--files", nargs="+")
parser.add_argument("--report")
args = parser.parse_args()

list_files = args.files
report = args.report
if report not in REPORT_BUILDERS:
    raise ValueError(f"Unknown type of report '{report}'")

data = reader.read(*list_files)

builder = REPORT_BUILDERS[report](data)
result_report = builder.build()

output_path = f"{report}_report.csv"
builder.save_to_csv(output_path, base_schema)
print(f"Report saved to {output_path}")

keys = ["title", "ctr", "retention_rate"]
pr = Printer(result_report, keys)
pr.show_report()
