import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

function FileEditor() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [fileName, setFileName] = useState("");
  const [content, setContent] = useState("");

  // 🔥 MOCK LOAD FILE (frontend only for now)
  useEffect(() => {
    // simulate backend response
    const mockFiles = {
      1: { name: "hello.txt", content: "Hello PyOS 👋" },
      2: { name: "notes.md", content: "My notes..." },
      3: { name: "project.js", content: "console.log('PyOS');" },
    };

    const file = mockFiles[id];

    if (file) {
      setFileName(file.name);
      setContent(file.content);
    }
  }, [id]);

  // 💾 SAVE (frontend mock)
  const saveFile = () => {
    console.log("Saving file:", {
      id,
      fileName,
      content,
    });

    alert("File saved (frontend mock) ✅");
  };

  return (
    <div
      style={{
        height: "100vh",
        backgroundColor: "#0f172a",
        color: "white",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {/* HEADER */}
      <div
        style={{
          padding: "15px",
          backgroundColor: "#1e293b",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h3>📄 {fileName || "Untitled File"}</h3>

        <div style={{ display: "flex", gap: "10px" }}>
          <button
            onClick={() => navigate("/files")}
            style={btnStyle}
          >
            ⬅ Back
          </button>

          <button
            onClick={saveFile}
            style={{ ...btnStyle, backgroundColor: "#22c55e" }}
          >
            💾 Save
          </button>
        </div>
      </div>

      {/* EDITOR AREA */}
      <div style={{ flex: 1, padding: "10px" }}>
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          style={{
            width: "100%",
            height: "100%",
            backgroundColor: "#0f172a",
            color: "#e2e8f0",
            border: "none",
            outline: "none",
            fontSize: "16px",
            padding: "15px",
            resize: "none",
            fontFamily: "monospace",
          }}
        />
      </div>
    </div>
  );
}

// 🎨 BUTTON STYLE
const btnStyle = {
  padding: "8px 12px",
  backgroundColor: "#3b82f6",
  border: "none",
  borderRadius: "6px",
  color: "white",
  cursor: "pointer",
};

export default FileEditor;