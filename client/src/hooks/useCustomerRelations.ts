import { useQuery } from "@tanstack/react-query";
import { axiosInstance } from "../services/axiosInstance ";
import { Customer } from "../types/socialTypes";

interface Relations {
  id: number;
  follower_user: Customer;
  following_user: Customer;
}

export const useCustomerRelations = () =>
  useQuery<Relations[], Error>({
    queryKey: ["customer-relations"],
    queryFn: async () =>
      await axiosInstance.get("/social/followers/").then((res) => res.data),
  });
