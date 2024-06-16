import { Flex, Heading } from "@radix-ui/themes";
import { useCustomerRelations } from "../hooks/useCustomerRelations";
import { useMemo } from "react";
import { useCurrentCustomer } from "../services/store";
import CustomerAvatar from "./CustomerAvatar";

const FollowingsList = () => {
  const customer = useCurrentCustomer((c) => c.customer);
  const { data: relations } = useCustomerRelations();

  const followings = useMemo(() => {
    return relations?.filter(
      (relation) => relation.follower_user.id === customer?.id
    );
  }, [relations, customer]);

  const followers = useMemo(() => {
    return relations?.filter(
      (relation) => relation.following_user.id === customer?.id
    );
  }, [relations, customer]);

  if (!relations) return null;

  return (
    <Flex direction="column" gap="5">
      <Flex direction="column" gap="2">
        <Heading size="3">Followings</Heading>
        {followings?.map((following) => (
          <Flex key={following.id} direction="column" gap="2">
            <CustomerAvatar
              src={following.following_user.profile_image}
              fallback={following.following_user.user.first_name}
            />
            <span>
              {following.following_user.user.first_name}{" "}
              {following.following_user.user.last_name}
            </span>
          </Flex>
        ))}
      </Flex>
      <Flex direction="column" gap="2">
        <Heading size="3">Followers</Heading>
        {followers?.map((follower) => (
          <Flex key={follower.id} direction="column" gap="2">
            <CustomerAvatar
              src={follower.follower_user.profile_image}
              fallback={follower.follower_user.user.first_name}
            />
            <span>
              {follower.follower_user.user.first_name}{" "}
              {follower.follower_user.user.last_name}
            </span>
          </Flex>
        ))}
      </Flex>
    </Flex>
  );
};

export default FollowingsList;
