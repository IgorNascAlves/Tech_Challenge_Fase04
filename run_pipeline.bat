@echo off

REM Step 1: Check if .venv exists, create it if not
if not exist .venv (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate
)

REM Step 2: Run pipeline.py script
python src\pipeline.py

REM Step 3: Run uvicorn for the app in the background
start uvicorn main:app --reload

REM Step 4: Include Streamlit
streamlit run forecast_app.py

REM Step 5: Deactivate virtual environment
deactivate
