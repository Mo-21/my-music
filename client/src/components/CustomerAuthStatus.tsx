import { useGetCurrentCustomer } from "../hooks/useGetCurrentCustomer";

const CustomerAuthStatus = () => {
  const { data: customer } = useGetCurrentCustomer();

  return <div>{customer?.user.first_name}</div>;
};

export default CustomerAuthStatus;
