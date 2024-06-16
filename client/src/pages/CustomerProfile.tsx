import { Flex, Grid, Heading, Text } from "@radix-ui/themes";
import { useCurrentCustomer } from "../services/store";
import PostsList from "../components/PostsList";
import CustomerAvatar from "../components/CustomerAvatar";
import MembershipBadge from "../components/MembershipBadge";
import FollowingsList from "../components/FollowingsList";

const CustomerProfile = () => {
  const { customer } = useCurrentCustomer();

  if (!customer) return null;

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
        <FollowingsList />
      </Flex>
      <Flex direction="column" gap="3" p="2" className="col-span-2">
        <Heading size="3">Your Posts</Heading>
        <PostsList posts={customer.authored_posts} />
      </Flex>
    </Grid>
  );
};

export default CustomerProfile;
