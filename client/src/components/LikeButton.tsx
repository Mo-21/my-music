import { Button } from "@radix-ui/themes";
import { useCurrentCustomer } from "../services/store";
import { useLikePost } from "../hooks/useLikePost";

const LikeButton = ({ postId }: { postId: number }) => {
  const { customer } = useCurrentCustomer();
  const { mutate } = useLikePost(postId);

  return (
    <Button
      onClick={() => mutate()}
      variant={customer?.liked_posts.includes(postId) ? "soft" : "solid"}
    >
      Like
    </Button>
  );
};

export default LikeButton;
