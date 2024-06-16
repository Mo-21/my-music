import { Flex, Grid, Heading, Text } from "@radix-ui/themes";
import { useCurrentCustomer } from "../services/store";
import PostsList from "../components/PostsList";
import CustomerAvatar from "../components/CustomerAvatar";
import MembershipBadge from "../components/MembershipBadge";
import FollowingsList from "../components/FollowingsList";
import { useCustomerProfile } from "../hooks/useGetCurrentCustomer";
import { useParams } from "react-router-dom";

const CustomerProfile = () => {
  const { customerId } = useParams();
  const { customer: currentCustomer } = useCurrentCustomer();
  const {
    data: customer,
    isLoading,
    isFetching,
  } = useCustomerProfile({
    customerId: parseInt(customerId!) || currentCustomer!.id,
  });

  if (!currentCustomer || !customer) return null;
  if (isLoading || isFetching) return <Text>Loading...</Text>;

  return (
    <Grid p="3" className="grid-cols-4">
      <Flex direction="column" gap="3" p="2" className="col-span-1">
        <Flex direction="column" gap="2">
          <CustomerAvatar
            src={customer.profile_image}
            fallback={customer.user.first_name[0]}
            size="7"
          />
          <Heading size="5">
            {customer.user.first_name} {customer.user.last_name}
          </Heading>
        </Flex>
        <Text>{customer.user.email}</Text>
        <Flex>
          <MembershipBadge membershipStatus={customer.membership_status} />
        </Flex>
        <Text>{customer.phone}</Text>
        <Text>{customer.birthdate}</Text>
        {currentCustomer.id === customer.id && <FollowingsList />}
      </Flex>
      <Flex direction="column" gap="3" p="2" className="col-span-2">
        <Heading size="3">Your Posts</Heading>
        <PostsList posts={customer.authored_posts} />
      </Flex>
    </Grid>
  );
};

export default CustomerProfile;
