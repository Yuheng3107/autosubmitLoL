import csv
from collections import defaultdict 
import numpy as np
def analyse():
    # Have
    d = defaultdict(list)
    # Key is model name
    # Value is dictionary with values being list of win rate
    with open("logfile.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Model Name"] != "NULL":
                d[row["Model Name"]].append(int(row["Number of Wins"]))
    # Get highest and lowest for each one, average, and standard deviation
    rows = []
    for job, win_list in d.items():
        data = np.array(win_list)
        std_dev = np.round(np.std(data),2)
        mean = np.round(np.mean(data),1)
        highest = np.max(data)
        lowest = np.min(data)
        count = len(win_list)
        row = [job, mean, highest, lowest, std_dev, count]
        rows.append(row)
    
    def sort_func(item):
        parts = item[0].split("-")
        return (parts[1], int(parts[2]))

    rows.sort(key=sort_func)

    with open("analysis.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Job", "Mean", "Highest","Lowest", "Standard Deviation", "Count"])
        writer.writerows(rows)
        
analyse()