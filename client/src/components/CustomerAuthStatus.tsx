import { Flex, Text } from "@radix-ui/themes";
import { useGetCurrentCustomer } from "../hooks/useGetCurrentCustomer";
import { Link } from "react-router-dom";
import LogoutButton from "./LogoutButton";

const CustomerAuthStatus = () => {
  const { data: customer } = useGetCurrentCustomer();

  if (!customer) return null;

  return (
    <Flex align="center" gap="4">
      <Text className="text-green-300">{customer.user.first_name}</Text>
      <Link to={`/profile/${customer.id}`}>Profile</Link>
      <LogoutButton />
    </Flex>
  );
};

export default CustomerAuthStatus;
