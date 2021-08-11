import pandas as pd
import plotly_express as px

dataFrame = pd.read_csv("data.csv")
figure = px.scatter(dataFrame, x= "Date", y= "Cases", color= "Country")
figure.show()