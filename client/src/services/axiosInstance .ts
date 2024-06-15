import axios from "axios";

export const axiosInstance = axios.create();

axiosInstance.interceptors.request.use(
  (config) => {
    const accessToken = localStorage.getItem("access");

    if (accessToken) config.headers.Authorization = `JWT ${accessToken}`;

    return config;
  },
  (error) => Promise.reject(error)
);
