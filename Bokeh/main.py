import csv

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure


DATA_FILE = "/home/ubuntu/HW5_data/monthly_response_times.csv"


# ---------------------------------------------------------
# Load the preprocessed monthly averages
# ---------------------------------------------------------

data = {}

with open(DATA_FILE, "r", encoding="utf-8", newline="") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        zipcode = row["zipcode"]
        month = row["month"]
        average = float(row["average_response_hours"])

        if zipcode not in data:
            data[zipcode] = {}

        data[zipcode][month] = average


# ---------------------------------------------------------
# Prepare dropdown options
# ---------------------------------------------------------

zipcodes = sorted(
    zipcode for zipcode in data.keys()
    if zipcode != "ALL"
)

zip1_default = zipcodes[0]
zip2_default = zipcodes[1]


# ---------------------------------------------------------
# Determine months
# ---------------------------------------------------------

months = sorted(data["ALL"].keys())


def values_for_zip(zipcode):
    return [
        data.get(zipcode, {}).get(month, float("nan"))
        for month in months
    ]


# ---------------------------------------------------------
# Data sources
# ---------------------------------------------------------

overall_source = ColumnDataSource(
    data={
        "month": months,
        "response": values_for_zip("ALL")
    }
)

zip1_source = ColumnDataSource(
    data={
        "month": months,
        "response": values_for_zip(zip1_default)
    }
)

zip2_source = ColumnDataSource(
    data={
        "month": months,
        "response": values_for_zip(zip2_default)
    }
)


# ---------------------------------------------------------
# Dropdowns
# ---------------------------------------------------------

zip1_select = Select(
    title="ZIP Code 1",
    value=zip1_default,
    options=zipcodes
)

zip2_select = Select(
    title="ZIP Code 2",
    value=zip2_default,
    options=zipcodes
)


# ---------------------------------------------------------
# Plot
# ---------------------------------------------------------

plot = figure(
    title="Monthly Average 311 Complaint Response Time",
    x_range=months,
    width=900,
    height=500,
    x_axis_label="Month",
    y_axis_label="Average response time (hours)"
)

plot.line(
    x="month",
    y="response",
    source=overall_source,
    line_width=3,
    legend_label="All ZIP Codes"
)

zip1_line = plot.line(
    x="month",
    y="response",
    source=zip1_source,
    line_width=3,
    legend_label=f"ZIP {zip1_default}"
)

zip2_line = plot.line(
    x="month",
    y="response",
    source=zip2_source,
    line_width=3,
    legend_label=f"ZIP {zip2_default}"
)

plot.legend.location = "top_left"


# ---------------------------------------------------------
# Update function
# ---------------------------------------------------------

def update_plot(attr, old, new):
    zip1 = zip1_select.value
    zip2 = zip2_select.value

    zip1_source.data = {
        "month": months,
        "response": values_for_zip(zip1)
    }

    zip2_source.data = {
        "month": months,
        "response": values_for_zip(zip2)
    }

    zip1_line.legend_label = f"ZIP {zip1}"
    zip2_line.legend_label = f"ZIP {zip2}"


zip1_select.on_change("value", update_plot)
zip2_select.on_change("value", update_plot)


# ---------------------------------------------------------
# Dashboard layout
# ---------------------------------------------------------

layout = column(
    zip1_select,
    zip2_select,
    plot
)

curdoc().add_root(layout)
curdoc().title = "NYC 311 Response Time Dashboard"
