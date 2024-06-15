import { Button, TextArea } from "@radix-ui/themes";
import { useRef } from "react";
import { useCreateComment } from "../hooks/useCreateComment";
import { PaperPlaneIcon } from "@radix-ui/react-icons";

const CommentForm = ({ postId }: { postId: number }) => {
  const ref = useRef<HTMLTextAreaElement>(null);
  const { mutate } = useCreateComment();

  return (
    <form
      onSubmit={(e) => {
        e.stopPropagation();
        e.preventDefault();

        if (!ref.current || ref.current.value === "") return;

        mutate({ text: ref.current.value, postId });
        ref.current.value = "";
      }}
      className="grid grid-cols-12 gap-2"
    >
      <TextArea ref={ref} placeholder="Comment" className="col-span-11" />
      <Button className="h-full col-span-1" variant="soft">
        <PaperPlaneIcon />
      </Button>
    </form>
  );
};

export default CommentForm;
