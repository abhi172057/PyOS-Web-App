import axios from "axios";

const api = axios.create({
  baseURL:import.meta.env.VITE_API_URL ?  `${import.meta.env.VITE_API_URL}/api` :"http://127.0.0.1:8000/api",
});

api.interceptors.request.use((config) => {
  config.headers.Authorization =
    `Bearer ${localStorage.getItem("access")}`;
  return config;
});

export default api;
