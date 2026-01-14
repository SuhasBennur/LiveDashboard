import pandas as pd
from typing import Dict

EXCEL_FILE = "oil_production_data.xlsx"

def init_excel():
    try:
        pd.read_excel(EXCEL_FILE)
    except Exception:
        df_init = pd.DataFrame(columns=["timestamp", "well_id", "flow_rate", "pressure", "temperature"])
        df_init.to_excel(EXCEL_FILE, index=False)

def append_to_excel(row: Dict):
    df = pd.DataFrame([row])
    with pd.ExcelWriter(EXCEL_FILE, mode="a", if_sheet_exists="overlay", engine="openpyxl") as writer:
        sheet = writer.sheets.get("Sheet1")
        start_row = sheet.max_row if sheet else 0
        df.to_excel(writer, index=False, header=False, startrow=start_row)