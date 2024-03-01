import csv
rows = [["Model Name","Last Submitted Win Rate","Number of Wins","Number of Draws","Total Runs"]]

with open("logfile.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Model Name"] != "NULL":
            rows.append(list(row.values()))
with open("logfile.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(len(rows))
print(rows)