import { Avatar, Text } from "@radix-ui/themes";
import { useGetCurrentCustomer } from "../hooks/useGetCurrentCustomer";

const CustomerAuthStatus = () => {
  const { data: customer } = useGetCurrentCustomer();

  if (!customer) return null;

  return (
    <>
      <Text>{customer.user.first_name}</Text>
      <Avatar
        src={customer.profile_image}
        fallback={customer.user.first_name[0]}
        variant="solid"
        size="2"
      />
    </>
  );
};

export default CustomerAuthStatus;
