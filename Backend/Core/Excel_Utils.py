import pandas as pd
from typing import Dict
from datetime import datetime
import os

# Base folder for Excel files
BASE_FOLDER = r"..\\Backend\\Oil_Production_Data"

# Make sure folder exists
os.makedirs(BASE_FOLDER, exist_ok=True)

# Create timestamped Excel file name inside that folder
timestamp_str = datetime.now().strftime("%d%m%Y_%H-%M")
EXCEL_FILE = os.path.join(BASE_FOLDER, f"oil_production_data_{timestamp_str}.xlsx")



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