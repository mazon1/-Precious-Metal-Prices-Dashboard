import streamlit as st
import pandas as pd
import plotly.express as px

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")

# Clean the "DateTime" column
data["DateTime"] = pd.to_datetime(data["DateTime"], errors="coerce")

# Remove rows with missing or invalid date values
data = data.dropna(subset=["DateTime"])

# Set the title and description
st.title("Precious Metal Prices 2018-2021")
st.markdown("The cost of precious metals between 2018 and 2021")

# Create a sidebar with filters
st.sidebar.header("Filters")
metal = st.sidebar.selectbox("Metal", data.columns[1:], index=0)
start_date = st.sidebar.date_input("Start Date", min_value=data.DateTime.min().date(), max_value=data.DateTime.max().date(), value=data.DateTime.min().date())
end_date = st.sidebar.date_input("End Date", min_value=data.DateTime.min().date(), max_value=data.DateTime.max().date(), value=data.DateTime.max().date())

filtered_data = data.loc[(data.DateTime >= start_date) & (data.DateTime <= end_date)]

# Create a plotly plot
fig = px.line(
    filtered_data,
    title=f"Precious Metal Prices for {metal} ({start_date} to {end_date})",
    x="DateTime",
    y=metal,
    color_discrete_map={metal: "gold"}
)

# Customize the plot
fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title=f"Price ({metal})",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color="white"
    ),
)

# Display the plot
st.plotly_chart(fig)
