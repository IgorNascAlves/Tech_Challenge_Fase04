from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
from datetime import datetime
import pandas as pd

app = FastAPI()

class Previsao(BaseModel):
    data: str
    valor: float

class ForecastResponse(BaseModel):
    value: List[Previsao]

def load_model(file_path):
    return joblib.load(file_path)

def forecast_loaded_model(model, last_date, forecast_steps):
    dates = pd.date_range(start=last_date, periods=forecast_steps, freq='B').to_list()
    forecast = model.get_forecast(steps=forecast_steps)

    values = [Previsao(data=dates[i].strftime('%d/%m/%Y'), valor=forecast.predicted_mean.values[i]) for i in range(len(dates))]

    return values

def get_last_date():
    path = 'data\ipeadata_last.csv'  # Adjust the path accordingly
    #read the first value of the csv file
    with open(path, 'r') as f:
        first_line = f.readline()
        #get the date of the first value
        first_date = first_line.split(';')[0]
        last_date = datetime.strptime(first_date, '%Y-%m-%d') + pd.DateOffset(days=1)
    return last_date.date().strftime('%d/%m/%Y')

@app.get("/forecast", response_model=ForecastResponse)
def forecast(forecast_steps: int):
    # Assuming `preco` is the column name in your DataFrame, replace it with the actual column name.
    # df['preco'] = ... 

    file_path = 'modelos/best_model.pkl'  # Adjust the path accordingly
    loaded_model = load_model(file_path)

    # Use the last date from your data or generate it based on the available data
    last_date = get_last_date()
    values = forecast_loaded_model(loaded_model, last_date, forecast_steps)

    response = ForecastResponse(
        value=values
    )

    return response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
