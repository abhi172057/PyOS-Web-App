import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import FileExplorer from "./pages/FileExplorer";
import FileEditor from "./pages/FileEditor";

import Search from "./pages/Search";
import History from "./pages/History";
import Logs from "./pages/Logs";
import RecycleBin from "./pages/RecycleBin";

import MainLayout from "./layouts/MainLayout";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* ================= PUBLIC ================= */}
        <Route path="/" element={<Login />} />

        {/* ================= PROTECTED LAYOUT ================= */}
        <Route element={<MainLayout />}>

          {/* DASHBOARD */}
          <Route path="/dashboard" element={<Dashboard />} />

          {/* FILE SYSTEM */}
          <Route path="/files" element={<FileExplorer />} />
          <Route
            path="/files/folder/:folderId"
            element={<FileExplorer />}
          />
          <Route
            path="/files/open/:id"
            element={<FileEditor />}
          />

          {/* SEARCH */}
          <Route path="/search" element={<Search />} />

          {/* HISTORY */}
          <Route path="/history" element={<History />} />

          {/* LOGS */}
          <Route path="/logs" element={<Logs />} />

          {/* RECYCLE BIN */}
          <Route
            path="/recyclebin"
            element={<RecycleBin />}
          />

        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;