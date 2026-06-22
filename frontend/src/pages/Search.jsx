import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Search() {
  const [query, setQuery] = useState("");
  const [files, setFiles] = useState([]);
  const [folders, setFolders] = useState([]);
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  // 🔍 SEARCH FUNCTION
  const handleSearch = async (e) => {
    const value = e.target.value;
    setQuery(value);

    if (!value) {
      setFiles([]);
      setFolders([]);
      return;
    }

    try {
      setLoading(true);

      const res = await api.get(
        `/filesystem/search/?q=${value}`
      );

      setFiles(res.data.files);
      setFolders(res.data.directories);

      setLoading(false);
    } catch (err) {
      console.log("Search error:", err);
      setLoading(false);
    }
  };

  const openFile = (file) => {
    navigate(`/files/open/${file.id}`);
  };

  return (
    <div style={styles.container}>
      <h2>🔍 PyOS Search</h2>

      {/* SEARCH INPUT */}
      <input
        type="text"
        value={query}
        onChange={handleSearch}
        placeholder="Search files & folders..."
        style={styles.input}
      />

      {/* LOADING */}
      {loading && <p>Searching...</p>}

      {/* FOLDERS */}
      <h3 style={{ marginTop: "20px" }}>📁 Folders</h3>

      {folders.length === 0 ? (
        <p style={styles.empty}>No folders found</p>
      ) : (
        folders.map((folder) => (
          <div key={folder.id} style={styles.card}>
            📁 {folder.name}
          </div>
        ))
      )}

      {/* FILES */}
      <h3 style={{ marginTop: "20px" }}>📄 Files</h3>

      {files.length === 0 ? (
        <p style={styles.empty}>No files found</p>
      ) : (
        files.map((file) => (
          <div
            key={file.id}
            style={styles.card}
            onClick={() => openFile(file)}
          >
            📄 {file.name}
          </div>
        ))
      )}
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
    padding: "12px",
    borderRadius: "8px",
    border: "none",
    outline: "none",
    backgroundColor: "#0f172a",
    color: "white",
  },

  card: {
    padding: "12px",
    marginTop: "10px",
    backgroundColor: "#334155",
    borderRadius: "8px",
    cursor: "pointer",
  },

  empty: {
    opacity: 0.6,
  },
};

export default Search;