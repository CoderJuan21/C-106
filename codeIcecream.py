import csv
import numpy as np
import plotly.express as px

def getData():
    icecream_sales = []
    colddrink_sales = []
    with open ("dataIce.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader :
            icecream_sales.append(float(row["Temperature"]))
            colddrink_sales.append(float(row["Ice-cream Sales"]))

    return {"x":icecream_sales, "y": colddrink_sales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between tempeture and icecream sales ==>", correlation[0,1])

def setup():
    dataSource = getData()
    findCorrelation(dataSource)

setup()