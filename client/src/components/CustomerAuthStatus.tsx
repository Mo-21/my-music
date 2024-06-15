import { Text } from "@radix-ui/themes";
import { useGetCurrentCustomer } from "../hooks/useGetCurrentCustomer";
import CustomerAvatar from "./CustomerAvatar";
import { useCurrentCustomer } from "../services/store";

const CustomerAuthStatus = () => {
  const { data: customer } = useGetCurrentCustomer();
  const setCustomer = useCurrentCustomer((c) => c.setCustomer);

  if (!customer) return null;
  setCustomer(customer);

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
