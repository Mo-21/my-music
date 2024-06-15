import { useMutation } from "@tanstack/react-query";
import axios from "axios";

interface LoginPayload {
  username: string;
  password: string;
}

interface LoginResponse {
  access: string;
  refresh: string;
}

export const useLogin = () =>
  useMutation<LoginResponse, Error, LoginPayload>({
    mutationKey: ["auth"],
    mutationFn: async ({ username, password }: LoginPayload) => {
      const response = await axios.post("/auth/jwt/create/", {
        username,
        password,
      });

      const data = response.data;

      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);

      return data;
    },
  });
