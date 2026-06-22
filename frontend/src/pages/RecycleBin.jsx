import { useEffect, useState } from "react";
import api from "../services/api";

function RecycleBin() {
  const [deletedItems, setDeletedItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRecycleBin();
  }, []);

  // 📥 FETCH RECYCLE BIN ITEMS
  const fetchRecycleBin = async () => {
    try {
      const res = await api.get("/recyclebin/");
      setDeletedItems(res.data);
    } catch (err) {
      console.log("Recycle Bin Error:", err);
    } finally {
      setLoading(false);
    }
  };

  // ♻ RESTORE ITEM
  const restoreItem = async (item) => {
    try {
      await api.post(`/recyclebin/restore/${item.id}/`);

      setDeletedItems(
        deletedItems.filter(
          (i) => i.id !== item.id
        )
      );

      alert(`${item.item_name} restored successfully`);
    } catch (err) {
      console.log("Restore Error:", err);
      alert("Restore failed");
    }
  };

  // ❌ DELETE FOREVER
  const deleteForever = async (id) => {
    try {
      await api.delete(
        `/recyclebin/delete/${id}/`
      );

      setDeletedItems(
        deletedItems.filter(
          (item) => item.id !== id
        )
      );
    } catch (err) {
      console.log("Delete Error:", err);
      alert("Delete failed");
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🗑 Recycle Bin</h2>

      <p style={styles.subtitle}>
        Deleted files and folders (OS-style trash system)
      </p>

      <div style={styles.box}>
        {loading ? (
          <p>Loading...</p>
        ) : deletedItems.length === 0 ? (
          <p style={styles.empty}>
            Recycle Bin is empty
          </p>
        ) : (
          deletedItems.map((item) => (
            <div
              key={item.id}
              style={styles.row}
            >
              <div>
                {item.item_type === "directory"
                  ? "📁"
                  : "📄"}{" "}
                {item.item_name}

                <div style={styles.time}>
                  Deleted at: {item.deleted_at}
                </div>
              </div>

              <div style={styles.actions}>
                <button
                  onClick={() =>
                    restoreItem(item)
                  }
                  style={styles.restoreBtn}
                >
                  ♻ Restore
                </button>

                <button
                  onClick={() =>
                    deleteForever(item.id)
                  }
                  style={styles.deleteBtn}
                >
                  ❌ Delete
                </button>
              </div>
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
  },

  subtitle: {
    opacity: 0.6,
    marginBottom: "20px",
  },

  box: {
    backgroundColor: "#0f172a",
    padding: "15px",
    borderRadius: "10px",
    maxHeight: "70vh",
    overflowY: "auto",
  },

  row: {
    display: "flex",
    justifyContent: "space-between",
    padding: "12px",
    borderBottom: "1px solid #334155",
    alignItems: "center",
  },

  time: {
    fontSize: "12px",
    opacity: 0.6,
    marginTop: "5px",
  },

  actions: {
    display: "flex",
    gap: "10px",
  },

  restoreBtn: {
    padding: "6px 10px",
    backgroundColor: "#22c55e",
    border: "none",
    borderRadius: "6px",
    color: "white",
    cursor: "pointer",
  },

  deleteBtn: {
    padding: "6px 10px",
    backgroundColor: "#ef4444",
    border: "none",
    borderRadius: "6px",
    color: "white",
    cursor: "pointer",
  },

  empty: {
    opacity: 0.6,
  },
};

export default RecycleBin;