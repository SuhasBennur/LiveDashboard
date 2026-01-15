import { useEffect, useState } from "react";

const WS_ANALYTICS = "ws://localhost:8000/ws/analytics";

export default function useAnalytics() {
  const [analytics, setAnalytics] = useState(null);

  useEffect(() => {
    const ws = new WebSocket(WS_ANALYTICS);

    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setAnalytics(data);
      } catch (err) {
        console.error("Failed to parse analytics message", err);
      }
    };

    ws.onclose = () => {
      console.log("Analytics WebSocket closed");
    };

    return () => ws.close();
  }, []);

  return analytics;
}