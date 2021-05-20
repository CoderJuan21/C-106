import csv
import plotly.express as px

with open ("dataMarks.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "DaysP", y = "Marks")
    fig.show()
