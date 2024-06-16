import { useQuery } from "@tanstack/react-query";
import { Customer } from "../types/socialTypes";
import { axiosInstance } from "../services/axiosInstance ";
import { useCurrentCustomer } from "../services/store";

export const useGetCurrentCustomer = () => {
  const setCustomer = useCurrentCustomer((c) => c.setCustomer);

  return useQuery<Customer, Error>({
    queryKey: ["current_customer"],
    queryFn: async () => {
      const response = await axiosInstance
        .get<Customer>("/social/customers/me/")
        .then((res) => res.data);

      setCustomer(response);
      return response;
    },
  });
};

export const useCustomerProfile = ({ customerId }: { customerId: number }) => {
  return useQuery<Customer, Error>({
    queryKey: ["current_customer"],
    queryFn: async () => {
      const response = await axiosInstance
        .get<Customer>(`/social/customers/${customerId}/`)
        .then((res) => res.data);

      return response;
    },
  });
};
