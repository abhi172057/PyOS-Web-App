import { useEffect, useState } from "react";
import api from "../services/api";

function History() {
  const [history, setHistory] = useState([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    fetchHistory();
  }, []);

  // 📜 GET ALL HISTORY
  const fetchHistory = async () => {
    try {
      const res = await api.get("/history/");
      setHistory(res.data);
    } catch (err) {
      console.log("History error:", err);
    }
  };

  // 🔍 FILTER HISTORY
  const filterHistory = async (value) => {
    setQuery(value);

    if (!value) {
      fetchHistory();
      return;
    }

    try {
      const res = await api.get(`/history/filter/?q=${value}`);
      setHistory(res.data);
    } catch (err) {
      console.log("Filter error:", err);
    }
  };

  return (
    <div style={styles.container}>
      <h2>⌨ Command History</h2>

      {/* 🔍 SEARCH BOX */}
      <input
        value={query}
        onChange={(e) => filterHistory(e.target.value)}
        placeholder="Search commands (ls, mkdir...)"
        style={styles.input}
      />

      {/* 📜 HISTORY LIST */}
      <div style={styles.box}>
        {history.length === 0 ? (
          <p>No history found</p>
        ) : (
          history.map((item) => (
            <div key={item.id} style={styles.row}>
              <span>$ {item.command}</span>
              <span>{item.status}</span>
              <span style={{ opacity: 0.6 }}>
                {item.timestamp}
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
    color: "white",
    height: "100%",
  },

  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "15px",
    borderRadius: "8px",
    border: "none",
    outline: "none",
    backgroundColor: "#0f172a",
    color: "white",
  },

  box: {
    backgroundColor: "#0f172a",
    padding: "15px",
    borderRadius: "10px",
    maxHeight: "70vh",
    overflowY: "auto",
  },

  row: {
    display: "grid",
    gridTemplateColumns: "1fr 100px 200px",
    padding: "10px",
    borderBottom: "1px solid #334155",
    fontFamily: "monospace",
  },
};

export default History;