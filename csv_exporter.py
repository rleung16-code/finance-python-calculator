import csv
from datetime import datetime
from pathlib import Path


def save_result(calculation_type: str, input_summary: str, result: str, filename: str = "results.csv") -> None:
    """Save a calculation result to a CSV file.

    Args:
        calculation_type: Name of the calculation.
        input_summary: Short summary of the inputs.
        result: Calculation result as text.
        filename: CSV file name.
    """
    file_path = Path(filename)
    file_exists = file_path.exists()

    with file_path.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        if not file_exists:
            writer.writerow(["timestamp", "calculation_type", "input_summary", "result"])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            calculation_type,
            input_summary,
            result,
        ])