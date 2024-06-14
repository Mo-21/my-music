import { Button, TextArea } from "@radix-ui/themes";
import { useRef } from "react";
import { useCreateComment } from "../hooks/useCreateComment";

const CommentForm = ({ postId }: { postId: number }) => {
  const ref = useRef<HTMLTextAreaElement>(null);
  const { mutate } = useCreateComment();

  return (
    <form
      onSubmit={(e) => {
        e.stopPropagation();
        e.preventDefault();

        if (!ref.current) return;

        mutate({ text: ref.current.value, postId });
        ref.current.value = "";
      }}
    >
      <TextArea ref={ref} placeholder="Comment" />
      <Button>Create</Button>
    </form>
  );
};

export default CommentForm;
