import { Button } from "@radix-ui/themes";
import { useCurrentCustomer } from "../services/store";

const LikeButton = ({ postId }: { postId: number }) => {
  const { customer } = useCurrentCustomer();
  return (
    <Button variant={customer?.liked_posts.includes(postId) ? "soft" : "solid"}>
      Like
    </Button>
  );
};

export default LikeButton;
