import { useQuery } from "@tanstack/react-query";
import { Customer } from "../types/socialTypes";
import { axiosInstance } from "../services/axiosInstance ";

export const useGetCurrentCustomer = () => {
  return useQuery<Customer, Error>({
    queryKey: ["current_customer"],
    queryFn: async () => {
      const response = await axiosInstance
        .get<Customer>("/social/customers/me/")
        .then((res) => res.data);

      return response;
    },
  });
};
