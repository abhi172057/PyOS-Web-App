import { useState } from "react";
import api from "../services/api";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    setLoading(true);

     console.log("USERNAME:", username);
     console.log("PASSWORD:", password);

    try {
      const res = await api.post("/token/", {
        username,
        password,
      });

      // store JWT tokens
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);

      alert("Login successful 🚀");

       // 👇 THIS IS WHERE YOU ADD IT
      window.location.href = "/dashboard";

      console.log("TOKEN:", res.data);

      // later we will redirect to dashboard
      // window.location.href = "/dashboard";

    } catch (err) {
      console.log("FULL ERROR:", err);
      console.log("RESPONSE DATA:", err.response?.data);
      console.log("STATUS:", err.response?.status);

      alert("Login failed ❌");
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#0f172a",
      }}
    >
      <div
        style={{
          width: "400px",
          padding: "30px",
          borderRadius: "12px",
          backgroundColor: "#1e293b",
          color: "white",
        }}
      >
        <h1 style={{ textAlign: "center" }}>PyOS</h1>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "20px",
            marginBottom: "15px",
          }}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginBottom: "20px",
          }}
        />

        <button
          onClick={handleLogin}
          disabled={loading}
          style={{
            width: "100%",
            padding: "10px",
            cursor: "pointer",
            backgroundColor: loading ? "#64748b" : "#3b82f6",
            color: "white",
            border: "none",
            borderRadius: "6px",
          }}
        >
          {loading ? "Logging in..." : "Login"}
        </button>
      </div>
    </div>
  );
}

export default Login;