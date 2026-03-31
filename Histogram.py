import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.renderers.default = "browser"

pio.templates.default = "plotly_white"

data = pd.read_excel(r"C:/Users/Asus/Downloads/swiggy_data.xlsx",)
data.columns = data.columns.str.strip()
# print(data.columns)
# print(data.head(5))
# print(data[["Price (INR)","Rating"]].describe())
# print(data.info())

data["Order Date"] = pd.to_datetime(data["Order Date"])
data["Order_Month"]= data["Order Date"].dt.month
data["Order_Year"] = data["Order Date"].dt.year
data["order_Day_of_Week"] = data["Order Date"].dt.dayofweek

# print(data.head())
# print(data["Order_Month"].head())

sales_by_month = data.groupby("Order_Month")["Restaurant Name"].count().reset_index()
fig = px.line(sales_by_month,
              x="Order_Month",
              y="Restaurant Name",
              title="Monthly Sales Analysis")

fig.write_html("graph.html")
# print(sales_by_month)