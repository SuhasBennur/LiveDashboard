Oil Production Dashboard

Overview
This project is a **real‑time oil production monitoring dashboard** built with **FastAPI (Python)** on the backend and **React (JavaScript)** on the frontend. It streams live production data via WebSockets, stores historical records in Excel, and provides analytics charts for performance insights.

The dashboard is organized into **three tabs**:
1. **Live Data** → Real‑time metrics and charts from active wells.  
2. **Historical Data** → Scrollable table of past records with filtering options.  
3. **Analytics** → Aggregated insights such as highest flow rates, average pressure/temperature, and well performance comparisons.

---

Tech Stack
- **Backend:** FastAPI, WebSockets, Pandas, OpenPyXL  
- **Frontend:** React, Axios, Recharts  
- **Data Storage:** Excel file (`oil_production_data.xlsx`) for demo persistence  
- **Communication:** REST API for history/analytics, WebSocket for live stream  

---

Features
- **Live Streaming:** Simulated oil well data (flow rate, pressure, temperature) pushed every second via WebSocket.  
- **Historical Records:** Data stored in memory and appended to Excel for persistence.  
- **Analytics:** Backend computes aggregates (max flow, average pressure/temperature, per‑well totals).  
- **Interactive Dashboard:**  
  - Tabbed navigation for clean separation of views.  
  - Auto‑scroll toggle for historical table.  
  - Well filter dropdown to focus on specific wells.  
  - Charts powered by Recharts (line chart for live data, bar chart for analytics).  

---

Project Structure

backend/
  app.py                # FastAPI server with WebSocket + REST endpoints
frontend/
  src/
    App.jsx             # Entry point, manages state and data flow
    pages/
      Dashboard.jsx     # Tabbed layout orchestrating components
    components/
      Live/             # LiveControls, LiveMetrics, LiveChart
      History/          # HistoryTable
      Analytics/        # AnalyticsSummary, AnalyticsChart
      Tabs/             # Tabs, TabPanel
    hooks/
      useWebSocket.js   # Custom hook for WebSocket connection
      useAnalytics.js   # Custom hook for analytics polling

---

How to Run

Backend (FastAPI)
---terminal
cd backend
pip install fastapi uvicorn pandas openpyxl
uvicorn app:app --reload
```
Backend runs at: `http://localhost:8000`

Frontend (React)
---terminal
cd frontend
npm install
npm run dev
```
Frontend runs at: `http://localhost:5173`

---

Demo Flow
1. Start FastAPI backend → generates simulated oil well data every second.  
2. React frontend connects via WebSocket → displays live metrics and charts.  
3. Historical data is stored and can be browsed in the History tab.  
4. Analytics tab shows aggregated insights and well performance charts.  

---