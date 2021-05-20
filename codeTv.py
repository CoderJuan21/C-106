import csv
import numpy as np
import plotly.express as px

def getData():
    sizetv = []
    watchaverage = []
    with open ("dataTv.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader :
            sizetv.append(float(row["Size"]))
            watchaverage.append(float(row["Average"]))

    return {"x":sizetv, "y": watchaverage}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between average watch time and tv size ==>", correlation[0,1])

def setup():
    dataSource = getData()
    findCorrelation(dataSource)

setup()