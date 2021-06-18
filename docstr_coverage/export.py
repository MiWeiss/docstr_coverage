import csv
import os

from docstr_coverage import ResultCollection

CSV_FILE_HEADERS = ["folder", "file", "name", "needed", "bla"]


def export_csv(results: ResultCollection, path: str):
    with open("eggs.csv", "w", newline="") as csvfile:
        filewriter = csv.writer(csvfile)
        for file in results.files():
            filewriter.writ


def export(results: ResultCollection, path: str):
    extension = os.path.splitext(path)[1]
    if extension.lower() != ".json":
        # Note: Long-Term, we may want to export more file types
        raise NotImplementedError("Only .csv files are supported as export files.")
    export_csv(results, path)


if __name__ == "__main__":
    # TODO Delete this
    print("hi")
