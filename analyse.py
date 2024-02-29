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
            d[row["Model Name"]].append(int(row["Number of Wins"]))
    # Get highest and lowest for each one, average, and standard deviation
    rows = [["Mean", "Highest","Lowest", "Standard Deviation", "Count"]]
    for job, win_list in d.items():
        data = np.array(win_list)
        std_dev = np.std(data)
        mean = np.mean(data)
        highest = np.max(data)
        lowest = np.min(data)
        count = len(win_list)
        row = [job, mean, highest, lowest, std_dev, count]
        rows.append(row)
    with open("analysis.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

        
analyse()