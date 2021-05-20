import csv
import numpy as np
import plotly.express as px

def getData():
    coffee = []
    sleep = []
    with open ("dataCoffee.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader :
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["Sleep"]))

    return {"x":coffee, "y": sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between amount of coffee drinken and hours of sleep ==>", correlation[0,1])

def setup():
    dataSource = getData()
    findCorrelation(dataSource)

setup()