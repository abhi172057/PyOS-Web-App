import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [stats, setStats] = useState({
    files: 0,
    folders: 0,
    logs: 0,
    recycle: 0,
    history: 0,
  });

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      console.log("Loading Dashboard Data...");

      const fileRes = await api.get("/filesystem/ls/1/");
      const logRes = await api.get("/logs/all/");
      const recycleRes = await api.get("/recyclebin/");
      const historyRes = await api.get("/history/");

      console.log("FILES API:", fileRes.data);
      console.log("LOGS API:", logRes.data);
      console.log("RECYCLE API:", recycleRes.data);
      console.log("HISTORY API:", historyRes.data);

      const filesCount =
        fileRes.data &&
        Array.isArray(fileRes.data.files)
          ? fileRes.data.files.length
          : 0;

      const foldersCount =
        fileRes.data &&
        Array.isArray(fileRes.data.directories)
          ? fileRes.data.directories.length
          : 0;

      const logsCount = Array.isArray(logRes.data)
        ? logRes.data.length
        : 0;

      const recycleCount = Array.isArray(recycleRes.data)
        ? recycleRes.data.length
        : 0;

      const historyCount = Array.isArray(historyRes.data)
        ? historyRes.data.length
        : 0;

      console.log("================================");
      console.log("Folder Count:", foldersCount);
      console.log("File Count:", filesCount);
      console.log("Logs Count:", logsCount);
      console.log("Recycle Count:", recycleCount);
      console.log("History Count:", historyCount);
      console.log("================================");

      setStats({
        files: filesCount,
        folders: foldersCount,
        logs: logsCount,
        recycle: recycleCount,
        history: historyCount,
      });
    } catch (err) {
      console.log("Dashboard Error:", err);
    }
  };
  console.log("Current Stats State:", stats);

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>🚀 Welcome to PyOS</h1>

      <p style={styles.subtitle}>
        Manage your system like a real OS
      </p>

      <div style={styles.statsGrid}>
        <div style={styles.card}>
          <div style={styles.icon}>📁</div>
          <h3>Total Folders</h3>
          <h2>{stats.folders}</h2>
        </div>

        <div style={styles.card}>
          <div style={styles.icon}>📄</div>
          <h3>Total Files</h3>
          <h2>{stats.files}</h2>
        </div>

        <div style={styles.card}>
          <div style={styles.icon}>🗑</div>
          <h3>Recycle Bin</h3>
          <h2>{stats.recycle}</h2>
        </div>

        <div style={styles.card}>
          <div style={styles.icon}>📜</div>
          <h3>Total Logs</h3>
          <h2>{stats.logs}</h2>
        </div>

        <div style={styles.card}>
          <div style={styles.icon}>🕒</div>
          <h3>Command History</h3>
          <h2>{stats.history}</h2>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    color: "white",
    padding: "25px",
  },

  heading: {
    marginBottom: "10px",
  },

  subtitle: {
    color: "#cbd5e1",
    marginBottom: "30px",
    fontSize: "18px",
  },

  statsGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
    gap: "20px",
  },

  card: {
    backgroundColor: "#334155",
    borderRadius: "12px",
    padding: "25px",
    textAlign: "center",
    boxShadow: "0px 2px 10px rgba(0,0,0,0.2)",
  },

  icon: {
    fontSize: "30px",
    marginBottom: "10px",
  },
};

export default Dashboard;