import csv
from collections import defaultdict
from datetime import datetime

INPUT_FILE = "/home/ubuntu/HW5_data/311_records_2024.csv"
OUTPUT_FILE = "/home/ubuntu/HW5_data/monthly_response_times.csv"

zip_totals = defaultdict(float)
zip_counts = defaultdict(int)

overall_totals = defaultdict(float)
overall_counts = defaultdict(int)

with open(INPUT_FILE, "r", encoding="utf-8", newline="") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        created = row["Created Date"].strip()
        closed = row["Closed Date"].strip()
        zipcode = row["Incident Zip"].strip()

        if not created or not closed or not zipcode:
            continue

        try:
            created_dt = datetime.strptime(
                created,
                "%m/%d/%Y %I:%M:%S %p"
            )

            closed_dt = datetime.strptime(
                closed,
                "%m/%d/%Y %I:%M:%S %p"
            )

        except ValueError:
            continue

        response_hours = (
            closed_dt - created_dt
        ).total_seconds() / 3600

        if response_hours < 0:
            continue

        # FAQ says the incident belongs to the month it was closed
        month = closed_dt.strftime("%Y-%m")

        zip_totals[(zipcode, month)] += response_hours
        zip_counts[(zipcode, month)] += 1

        overall_totals[month] += response_hours
        overall_counts[month] += 1


with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as outfile:
    writer = csv.writer(outfile)

    writer.writerow([
        "zipcode",
        "month",
        "average_response_hours"
    ])

    for (zipcode, month), total in sorted(zip_totals.items()):
        average = total / zip_counts[(zipcode, month)]

        writer.writerow([
            zipcode,
            month,
            average
        ])

    for month, total in sorted(overall_totals.items()):
        average = total / overall_counts[month]

        writer.writerow([
            "ALL",
            month,
            average
        ])
