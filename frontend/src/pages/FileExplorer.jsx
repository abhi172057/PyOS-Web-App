import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../services/api";

function FileExplorer() {
  const navigate = useNavigate();
  const { folderId } = useParams();

  const [files, setFiles] = useState([]);
  const [folders, setFolders] = useState([]);
  const [breadcrumb, setBreadcrumb] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeMenu, setActiveMenu] = useState(null);

  const currentDir = folderId || 1;

  useEffect(() => {
    fetchDirectory();
  }, [folderId]);

  const fetchDirectory = async () => {
    try {
      setLoading(true);

      const res = await api.get(
        `/filesystem/ls/${currentDir}/`
      );

      setFiles(res.data.files || []);
      setFolders(res.data.directories || []);
      setBreadcrumb(res.data.breadcrumb || []);

      setLoading(false);
    } catch (err) {
      console.log("FULL ERROR:", err);
      console.log("BACKEND RESPONSE:", err.response?.data);
      setLoading(false);
    }
  };

  const openFile = (file) => {
    navigate(`/files/open/${file.id}`);
  };

  const openFolder = (folder) => {
    navigate(`/files/folder/${folder.id}`);
  };

  const createFolder = async () => {
  const name = prompt("Enter folder name");

  if (!name) return;

  try {
    await api.post("/filesystem/mkdir/", {
      name: name,
      parent_id: currentDir,
    });

    fetchDirectory();
  } catch (err) {
    console.log(err);
    alert("Failed to create folder");
  }
};

const createFile = async () => {
  const name = prompt("Enter file name");

  if (!name) return;

  try {
    await api.post("/filesystem/touch/", {
      name: name,
      content: "",
      directory_id: currentDir,
    });

    fetchDirectory();
  } catch (err) {
    console.log(err);
    alert("File created successfully");
  }
};

const moveFile = async (fileId) => {
  const destinationFolderName = prompt(
    "Enter destination folder Name"
  );

  if (!destinationFolderName) return;

  try {
    await api.post("/filesystem/move-file/", {
      file_id: fileId,
      destination_folder_name: destinationFolderName,
    });

    alert("File moved successfully");

    fetchDirectory();
  } catch (err) {
    console.log(err);
    alert("Failed to move file");
  }
};

const moveFolder = async (folderId) => {
  const destinationFolderName = prompt(
    "Enter destination folder name"
  );

  if (!destinationFolderName) return;

  try {
    await api.post("/filesystem/move-directory/", {
      directory_id: folderId,
      destination_folder_name: destinationFolderName,
    });

    alert("Folder moved successfully");

    fetchDirectory();
  } catch (err) {
  console.log(err);

  console.log(
    "Backend Error:",
    err.response?.data
  );

  alert(
    JSON.stringify(
      err.response?.data
    )
  );
}
};

const deleteFile = async (fileId) => {
  if (!window.confirm("Move file to recycle bin?")) return;

  try {
    await api.delete(`/filesystem/delete/${fileId}/`);

    fetchDirectory();
  } catch (err) {
    console.log(err);
    alert("Delete failed");
  }
};

const deleteFolder = async (folderId) => {
  if (!window.confirm("Move folder to recycle bin?"))
    return;

  try {
    await api.delete(
      `/filesystem/delete-directory/${folderId}/`
    );

    fetchDirectory();
  } catch (err) {
    console.log(err);
    alert("Delete failed");
  }
};

const renameFolder = async (folder) => {
  const newName = prompt(
    "Enter new folder name",
    folder.name
  );

  if (!newName) return;

  try {
    await api.put(
      `/filesystem/rename-directory/${folder.id}/`,
      {
        name: newName,
      }
    );

    fetchDirectory();
  } catch (err) {
    console.log(err);
    alert("Rename failed");
  }
};

const renameFile = async (file) => {
  const newName = prompt(
    "Enter new file name",
    file.name
  );

  if (!newName) return;

  alert(
    "Rename API backend banana baki hai"
  );
};

  const goToBreadcrumb = (folderId) => {
    navigate(`/files/folder/${folderId}`);
  };

  if (loading) {
    return (
      <div style={styles.loading}>
        Loading directory...
      </div>
    );
  }

  return (
    <div style={styles.container}>

      {/* HEADER */}
      <div style={styles.header}>
        <div>
          <h2 style={styles.heading}>📁 File Explorer</h2>

          <p style={styles.subHeading}>
            Manage your files and folders
          </p>

          <div style={styles.breadcrumbContainer}>
            <span
              style={styles.breadcrumbLink}
              onClick={() => navigate("/files/folder/1")}
            >
              🏠 Home
            </span>

            {breadcrumb.map((item) => (
              <span key={item.id}>
                <span style={styles.separator}> &gt; </span>

                <span
                  style={styles.breadcrumbLink}
                  onClick={() => goToBreadcrumb(item.id)}
                >
                  {item.name}
                </span>
              </span>
            ))}
          </div>
        </div>

        <div style={styles.headerActions}>
          <button
            style={styles.refreshButton}
            onClick={fetchDirectory}
          >
            🔄 Refresh
          </button>

          {folderId && (
            <button
              style={styles.backButton}
              onClick={() => navigate(-1)}
            >
              ⬅ Back
            </button>
          )}

          <input
            type="text"
            placeholder="Search files and folders..."
            style={styles.searchInput}
          />
        </div>
      </div>

      {/* FOLDERS */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>
          📁 Folders ({folders.length})
        </h3>

        {folders.length === 0 ? (
          <div style={styles.emptyState}>
            No folders found
          </div>
        ) : (
          <div style={styles.grid}>
            {folders.map((folder) => (
              <div
                key={folder.id}
                style={styles.folderCard}
              >
                <div style={styles.menuWrapper}>
                  <button
                    style={styles.menuButton}
                    onClick={(e) => {
                      e.stopPropagation();
                      setActiveMenu(
                        activeMenu === `folder-${folder.id}`
                          ? null
                          : `folder-${folder.id}`
                      );
                    }}
                  >
                    ⋮
                  </button>

                  {activeMenu === `folder-${folder.id}` && (
                    <div style={styles.dropdown}>
                      <div
                        style={styles.dropdownItem}
                        onClick={() => moveFolder(folder.id)}
                      >
                        Move
                      </div>

                      <div
                        style={styles.dropdownItem}
                        onClick={() => renameFolder(folder)}
                      >
                        Rename
                      </div>

                      <div
                        style={styles.dropdownDelete}
                        onClick={() => deleteFolder(folder.id)}
                      >
                        Delete
                      </div>
                    </div>
                  )}
                </div>

                <div
                  onClick={() => openFolder(folder)}
                  style={{
                    flex: 1,
                    display: "flex",
                    alignItems: "center",
                    gap: "12px",
                    cursor: "pointer",
                  }}
                >
                  <div style={styles.icon}>📁</div>

                  <div style={styles.name}>
                    {folder.name}
                  </div>
                </div>
              </div>
            ))}

            <div
              style={styles.addFolderCard}
              onClick={createFolder}
            >
              <div style={styles.icon}>➕</div>

              <div style={styles.name}>
                New Folder
              </div>
            </div>
          </div>
        )}
      </div>

      {/* FILES */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>
          📄 Files ({files.length})
        </h3>

        {files.length === 0 ? (
          <div style={styles.emptyState}>
            No files found
          </div>
        ) : (
          <div style={styles.grid}>
            {files.map((file) => (
              <div
                key={file.id}
                style={styles.fileCard}
              >
                <div style={styles.menuWrapper}>
                  <button
                    style={styles.menuButton}
                    onClick={(e) => {
                      e.stopPropagation();
                      setActiveMenu(
                        activeMenu === `file-${file.id}`
                          ? null
                          : `file-${file.id}`
                      );
                    }}
                  >
                    ⋮
                  </button>

                  {activeMenu === `file-${file.id}` && (
                    <div style={styles.dropdown}>
                      <div
                        style={styles.dropdownItem}
                        onClick={() => moveFile(file.id)}
                      >
                        Move
                      </div>

                      <div
                        style={styles.dropdownItem}
                        onClick={() => renameFile(file)}
                      >
                        Rename
                      </div>

                      <div
                        style={styles.dropdownDelete}
                        onClick={() => deleteFile(file.id)}
                      >
                        Delete
                      </div>
                    </div>
                  )}
                </div>

                <div
                  onClick={() => openFile(file)}
                  style={{
                    flex: 1,
                    display: "flex",
                    alignItems: "center",
                    gap: "12px",
                    cursor: "pointer",
                  }}
                >
                  <div style={styles.icon}>📄</div>

                  <div style={styles.name}>
                    {file.name}
                  </div>
                </div>
              </div>
            ))}
            <div
              style={styles.addFileCard}
              onClick={createFile}
            >
              <div style={styles.icon}>➕</div>

              <div style={styles.name}>
                New File
              </div>
            </div>
          </div>
        )}
      </div>

    </div>
  );
}

const styles = {
  container: {
    padding: "25px",
    color: "white",
    backgroundColor: "#1e293b",
    minHeight: "100vh",
  },

  loading: {
    color: "white",
    padding: "30px",
    fontSize: "18px",
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "30px",
  },

  headerActions: {
  display: "flex",
  alignItems: "center",
  gap: "12px",
},

  heading: {
    margin: 0,
    fontSize: "32px",
  },

  subHeading: {
  color: "#94a3b8",
  marginTop: "8px",
  fontSize: "14px",
},

  breadcrumbContainer: {
    marginTop: "12px",
    fontSize: "15px",
    color: "#cbd5e1",
    display: "flex",
    flexWrap: "wrap",
    alignItems: "center",
  },

  breadcrumbLink: {
    cursor: "pointer",
    color: "#60a5fa",
    fontWeight: "500",
  },

  separator: {
    color: "#94a3b8",
    margin: "0 6px",
  },

  backButton: {
    backgroundColor: "#3b82f6",
    color: "white",
    border: "none",
    padding: "10px 18px",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "600",
    fontSize: "14px",
  },

  refreshButton: {
  background: "#2563eb",
  color: "white",
  border: "none",
  borderRadius: "10px",
  padding: "10px 15px",
  cursor: "pointer",
  fontWeight: "600",
},

searchInput: {
  width: "280px",
  padding: "10px 14px",
  borderRadius: "10px",
  border: "1px solid rgba(255,255,255,0.1)",
  background: "#0f172a",
  color: "white",
  outline: "none",
},

  section: {
    marginBottom: "35px",
  },

  sectionTitle: {
  marginBottom: "20px",
  fontSize: "24px",
  fontWeight: "700",
},

  grid: {
  display: "grid",
  gridTemplateColumns:
    "repeat(auto-fill,minmax(260px,1fr))",
  gap: "15px",
},

  folderCard: {
    position: "relative",
    background:
      "linear-gradient(145deg,#253855,#324867)",
    borderRadius: "16px",
    padding: "12px",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    minHeight: "65px",
    border: "1px solid rgba(255,255,255,0.08)",
    boxShadow:
      "0 10px 30px rgba(0,0,0,0.35)",
    transition: "all .3s ease",
  },

  fileCard: {
    position: "relative",
    background:
      "linear-gradient(145deg,#1f3148,#2c425e)",
    borderRadius: "16px",
    padding: "12px",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    minHeight: "65px",
    border: "1px solid rgba(255,255,255,0.08)",
    boxShadow:
      "0 10px 30px rgba(0,0,0,0.35)",
    transition: "all .3s ease",
  },

  icon: {
    fontSize: "28px",
  },

  moveButton: {
    background:
      "linear-gradient(135deg,#f59e0b,#d97706)",
    border: "none",
    color: "white",
    padding: "10px 16px",
    borderRadius: "10px",
    cursor: "pointer",
    fontSize: "13px",
    fontWeight: "600",
  },

  name: {
    fontSize: "14px",
    fontWeight: "500",
    wordBreak: "break-word",
  },

  emptyState: {
    backgroundColor: "#334155",
    padding: "20px",
    borderRadius: "10px",
    color: "#cbd5e1",
  },

  addFolderCard: {
    background:
      "linear-gradient(135deg,#2563eb,#1d4ed8)",
    borderRadius: "16px",
    padding: "15px",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    gap: "15px",
    minHeight: "85px",
    boxShadow:
      "0 10px 30px rgba(37,99,235,.35)",
  },

  addFileCard: {
    background:
      "linear-gradient(135deg,#16a34a,#15803d)",
    borderRadius: "16px",
    padding: "15px",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    gap: "15px",
    minHeight: "85px",
    boxShadow:
      "0 10px 30px rgba(22,163,74,.35)",
  },

menuWrapper: {
  position: "absolute",
  top: "10px",
  right: "10px",
},

menuButton: {
  background: "transparent",
  border: "none",
  color: "white",
  fontSize: "18px",
  cursor: "pointer",
},

dropdown: {
  position: "absolute",
  top: "25px",
  right: 0,
  background: "#0f172a",
  borderRadius: "10px",
  minWidth: "120px",
  overflow: "hidden",
  zIndex: 100,
  boxShadow: "0 8px 20px rgba(0,0,0,.4)",
},

dropdownItem: {
  padding: "10px",
  cursor: "pointer",
  color: "white",
},

dropdownDelete: {
  padding: "10px",
  cursor: "pointer",
  color: "#ef4444",
},
  
};

export default FileExplorer;