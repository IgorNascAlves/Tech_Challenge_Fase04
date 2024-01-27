@echo off

REM Step 1: Activate Python virtual environment
call .venv\Scripts\activate

REM Step 2: Run pipeline.py script
python src\pipeline.py

REM Step 3: Run uvicorn for the app in the background
start uvicorn main:app --reload

REM Step 4: Deactivate virtual environment
deactivate
