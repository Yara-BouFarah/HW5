import argparse
import csv
from collections import defaultdict
from datetime import datetime


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Count 311 complaint types by borough for a given creation date range."
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Input CSV file"
    )

    parser.add_argument(
        "-s",
        "--start",
        required=True,
        help="Start date in MM/DD/YYYY format"
    )

    parser.add_argument(
        "-e",
        "--end",
        required=True,
        help="End date in MM/DD/YYYY format"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Optional output CSV file"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    start_date = datetime.strptime(args.start, "%m/%d/%Y").date()
    end_date = datetime.strptime(args.end, "%m/%d/%Y").date()

    counts = defaultdict(int)

    with open(args.input, "r", encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            created = row["Created Date"].strip()

            if not created:
                continue

            try:
                created_date = datetime.strptime(
                    created,
                    "%m/%d/%Y %I:%M:%S %p"
                ).date()
            except ValueError:
                continue

            if start_date <= created_date <= end_date:
                complaint_type = row["Complaint Type"].strip()
                borough = row["Borough"].strip()

                counts[(complaint_type, borough)] += 1

    if args.output:
        outfile = open(args.output, "w", encoding="utf-8", newline="")
    else:
        import sys
        outfile = sys.stdout

    writer = csv.writer(outfile)
    writer.writerow(["complaint type", "borough", "count"])

    for (complaint_type, borough), count in sorted(counts.items()):
        writer.writerow([complaint_type, borough, count])

    if args.output:
        outfile.close()


if __name__ == "__main__":
    main()
