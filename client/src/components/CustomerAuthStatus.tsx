import { Text } from "@radix-ui/themes";
import { useGetCurrentCustomer } from "../hooks/useGetCurrentCustomer";
import CustomerAvatar from "./CustomerAvatar";

const CustomerAuthStatus = () => {
  const { data: customer } = useGetCurrentCustomer();

  if (!customer) return null;

  console.log(customer);

  return (
    <>
      <Text>{customer.user.first_name}</Text>
      <CustomerAvatar
        src={customer.profile_image}
        fallback={customer.user.first_name[0]}
      />
    </>
  );
};

export default CustomerAuthStatus;
