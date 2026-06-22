import { useEffect, useState } from "react";
import api from "../services/api";

function Logs() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    try {
      const res = await api.get("/logs/all/");

      console.log("LOG API RESPONSE:", res.data);

      setLogs(res.data || []);
    } catch (err) {
      console.log("Logs Error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>📊 System Logs</h2>

      <p style={styles.subtitle}>
        PyOS kernel activity monitor
      </p>

      <div style={styles.box}>
        {loading ? (
          <p>Loading logs...</p>
        ) : logs.length === 0 ? (
          <p style={styles.empty}>No logs found</p>
        ) : (
          logs.map((log) => (
            <div key={log.id} style={styles.row}>
              <span
                style={{
                  ...styles.level,
                  color:
                    log.action === "ERROR"
                      ? "#ef4444"
                      : log.action === "WARNING"
                      ? "#f59e0b"
                      : log.action === "DELETE_FILE" ||
                        log.action === "DELETE_DIRECTORY"
                      ? "#f87171"
                      : log.action === "CREATE_FILE" ||
                        log.action === "CREATE_DIRECTORY"
                      ? "#22c55e"
                      : "#38bdf8",
                }}
              >
                [{log.action}]
              </span>

              <span style={styles.message}>
                {log.description}
              </span>

              <span style={styles.user}>
                {log.user || "System"}
              </span>

              <span style={styles.time}>
                {new Date(log.timestamp).toLocaleString()}
              </span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "20px",
    backgroundColor: "#1e293b",
    height: "100%",
    color: "white",
  },

  title: {
    marginBottom: "5px",
    fontSize: "36px",
  },

  subtitle: {
    opacity: 0.7,
    marginBottom: "20px",
    fontSize: "18px",
  },

  box: {
    backgroundColor: "#0f172a",
    padding: "15px",
    borderRadius: "12px",
    maxHeight: "75vh",
    overflowY: "auto",
  },

  row: {
    display: "grid",
    gridTemplateColumns: "180px 1fr 180px 220px",
    gap: "15px",
    padding: "12px",
    borderBottom: "1px solid #334155",
    alignItems: "center",
    fontFamily: "monospace",
  },

  level: {
    fontWeight: "bold",
    fontSize: "14px",
  },

  message: {
    color: "#e2e8f0",
    fontSize: "14px",
  },

  user: {
    opacity: 0.8,
    textAlign: "center",
  },

  time: {
    opacity: 0.7,
    textAlign: "right",
    fontSize: "12px",
  },

  empty: {
    opacity: 0.6,
    textAlign: "center",
    padding: "20px",
  },
};

export default Logs;