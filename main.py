from fastapi import FastAPI, File, UploadFile, Form
import pandas as pd
from utils.parse_excel import parse_excel
from utils.web_search import fill_missing_with_web
from utils.coda_client import push_to_coda

app = FastAPI()

@app.post("/transcribe")
async def transcribe_excel(
    file: UploadFile = File(...),
    coda_token: str = Form(...),
    doc_id: str = Form(...),
    table_name: str = Form(...),
    web_search_columns: str = Form(...),  # comma-separated
):
    # Save uploaded file
    contents = await file.read()
    with open("temp.xlsx", "wb") as f:
        f.write(contents)
    df = parse_excel("temp.xlsx")
    ws_cols = [col.strip() for col in web_search_columns.split(",")]
    df_filled = fill_missing_with_web(df, ws_cols)
    result = push_to_coda(df_filled, coda_token, doc_id, table_name)
    return {"status": "complete", "result": result}