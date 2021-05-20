import csv
import numpy as np
import plotly.express as px

def getData():
    marks = []
    daysP = []
    with open ("dataMarks.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader :
            marks.append(float(row["Marks"]))
            daysP.append(float(row["DaysP"]))

    return {"x":marks, "y": daysP}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between marks average and days attended to school ==>", correlation[0,1])

def setup():
    dataSource = getData()
    findCorrelation(dataSource)

setup()