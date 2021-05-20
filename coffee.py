import csv
import plotly.express as px

with open ("dataCoffee.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Coffee", y = "Sleep")
    fig.show()
