from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
from datetime import datetime

app = FastAPI()

class ForecastResponse(BaseModel):
    model: str
    forecast_steps: int
    predictions: List[float]

def load_model(file_path):
    return joblib.load(file_path)

def forecast_loaded_model(model, last_date, forecast_steps):
    forecast = model.get_forecast(steps=forecast_steps)
    return forecast.predicted_mean.values

@app.get("/forecast", response_model=ForecastResponse)
def forecast(forecast_steps: int):
    # Assuming `preco` is the column name in your DataFrame, replace it with the actual column name.
    # df['preco'] = ... 

    file_path = 'modelos/best_model.pkl'  # Adjust the path accordingly
    loaded_model = load_model(file_path)

    # Use the last date from your data or generate it based on the available data
    last_date = datetime.now()  # Replace this with the actual last date

    forecast_values = forecast_loaded_model(loaded_model, last_date, forecast_steps)

    response = ForecastResponse(
        model='Best Model (SARIMA)',  # Adjust accordingly based on your analysis
        forecast_steps=forecast_steps,
        predictions=forecast_values.tolist()
    )

    return response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
