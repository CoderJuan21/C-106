import csv
import plotly.express as px

with open ("dataTv.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Size", y = "Average")
    fig.show()
