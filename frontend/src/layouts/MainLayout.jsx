import { Outlet, useNavigate, useLocation } from "react-router-dom";

function MainLayout() {
  const navigate = useNavigate();
  const location = useLocation();

  const menu = [
    { name: "Dashboard", path: "/dashboard", icon: "🏠" },
    { name: "Files", path: "/files", icon: "📁" },
    { name: "Search", path: "/search", icon: "🔍" },
    { name: "History", path: "/history", icon: "🕒" },
    { name: "Logs", path: "/logs", icon: "📊" },
    { name: "Recycle Bin", path: "/recyclebin", icon: "🗑️" },
  ];

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        background:
          "linear-gradient(135deg,#071226,#0b1b36,#0a1730)",
      }}
    >
      {/* SIDEBAR */}
      <div
        style={{
          width: "280px",
          margin: "15px",
          borderRadius: "24px",
          background:
            "rgba(10,20,45,0.95)",
          border: "1px solid rgba(255,255,255,0.08)",
          backdropFilter: "blur(20px)",
          padding: "25px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          boxShadow:
            "0px 0px 40px rgba(0,100,255,0.15)",
        }}
      >
        <div>
          {/* LOGO */}
          <h1
            style={{
              color: "white",
              marginBottom: "40px",
              fontSize: "38px",
            }}
          >
            📁 PyOS
          </h1>

          {/* MENU */}
          {menu.map((item) => {
            const active =
              location.pathname.startsWith(
                item.path
              );

            return (
              <div
                key={item.path}
                onClick={() =>
                  navigate(item.path)
                }
                style={{
                  padding: "18px",
                  marginBottom: "14px",
                  borderRadius: "18px",
                  cursor: "pointer",
                  color: "white",
                  fontSize: "18px",
                  background: active
                    ? "linear-gradient(135deg,#4f46e5,#6366f1)"
                    : "transparent",
                  boxShadow: active
                    ? "0 0 25px rgba(99,102,241,.5)"
                    : "none",
                  transition: "0.3s",
                }}
              >
                {item.icon} {item.name}
              </div>
            );
          })}
        </div>

        {/* PROFILE + LOGOUT */}
        <div>
          <div
            style={{
              background:
                "rgba(255,255,255,0.05)",
              borderRadius: "18px",
              padding: "16px",
              marginBottom: "20px",
              color: "white",
            }}
          >
            <div
              style={{
                fontWeight: "bold",
                fontSize: "18px",
              }}
            >
              👤 Abhishek
            </div>

            <div
              style={{
                color: "#94a3b8",
                fontSize: "13px",
              }}
            >
              PyOS User
            </div>
          </div>

          <button
            onClick={() => {
              localStorage.clear();
              navigate("/");
            }}
            style={{
              width: "100%",
              padding: "16px",
              border: "none",
              borderRadius: "16px",
              background:
                "linear-gradient(135deg,#ef4444,#dc2626)",
              color: "white",
              fontSize: "17px",
              cursor: "pointer",
              fontWeight: "bold",
            }}
          >
            🚪 Logout
          </button>
        </div>
      </div>

      {/* CONTENT AREA */}
      <div
        style={{
          flex: 1,
          margin: "15px 15px 15px 0px",
          borderRadius: "24px",
          background:
            "rgba(15,25,50,0.95)",
          border: "1px solid rgba(255,255,255,0.08)",
          backdropFilter: "blur(20px)",
          overflowY: "auto",
        }}
      >
        <Outlet />
      </div>
    </div>
  );
}

export default MainLayout;