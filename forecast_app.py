import streamlit as st
import requests
import locale
import pandas as pd
import matplotlib.pyplot as plt

# Set the locale for currency formatting (you can adjust this based on your region)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Streamlit app
st.title("Forecast API Visualization")

# API URL
api_url = "http://127.0.0.1:8000/forecast"

# Function to get forecast data from the API
def get_forecast_data(forecast_steps):
    params = {"forecast_steps": forecast_steps}
    response = requests.get(api_url, params=params)
    return response.json()["value"]

# User input for forecast days
forecast_days = st.slider("Select number of forecast days (1-30)", 1, 30, 10)

# Fetch forecast data
forecast_data = get_forecast_data(forecast_days)

# Format "valor" values as currency
formatted_data = [{"data": entry["data"], "valor": locale.currency(entry["valor"], grouping=True)} for entry in forecast_data]

# Display formatted data in a table and plot side by side
columns = st.columns(2)

# Column 1: Display formatted data in a table
columns[0].table(formatted_data)

# Column 2: Plot the data and "valor" values
columns[1].subheader("Line Chart")
# Convert the data to a DataFrame for plotting
df = pd.DataFrame(forecast_data)
df["data"] = pd.to_datetime(df["data"], format='%d/%m/%Y')

# Plot the data and "valor" values
columns[1].line_chart(df.set_index("data")["valor"])

# Optionally, display a downloadable CSV link for the data
st.markdown("### Download Data")
csv_export = df.to_csv(index=False)
st.download_button("Download Forecast Data", csv_export, "forecast_data.csv", "text/csv")
