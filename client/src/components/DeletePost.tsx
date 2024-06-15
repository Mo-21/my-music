import { Button, Spinner } from "@radix-ui/themes";
import { useCurrentCustomer } from "../services/store";
import { Post } from "../types/socialTypes";
import { useDeletePost } from "../hooks/useDeletePost";

const DeletePost = ({ post }: { post: Post }) => {
  const customer = useCurrentCustomer((c) => c.customer);
  const { mutateAsync, isPending } = useDeletePost();

  if (!customer || customer.id !== post.author.id) return null;

  return (
    <Button
      onClick={async () => await mutateAsync({ postId: post.id })}
      color="red"
    >
      {isPending ? <Spinner /> : "Delete"}
    </Button>
  );
};

export default DeletePost;
