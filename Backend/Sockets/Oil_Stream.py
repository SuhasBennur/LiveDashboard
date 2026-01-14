import asyncio, random
from datetime import datetime
from fastapi import WebSocket
from Core.Data_Store import historical_data
from Core.Excel_Utils import append_to_excel

async def oil_stream(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data_point = {
                "timestamp": datetime.utcnow().isoformat(),
                "well_id": f"WELL-{random.randint(1, 5)}",
                "flow_rate": round(random.uniform(800, 1200), 2),
                "pressure": round(random.uniform(1800, 2200), 2),
                "temperature": round(random.uniform(60, 90), 2),
            }
            historical_data.append(data_point)
            append_to_excel(data_point)
            await ws.send_json(data_point)
            await asyncio.sleep(1)
    except Exception:
        await ws.close()