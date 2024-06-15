import { Button, Container, TextArea } from "@radix-ui/themes";
import { useRef } from "react";
import { useCreatePost } from "../hooks/useCreatePost";

const CreatePost = () => {
  const ref = useRef<HTMLTextAreaElement>(null);
  const { mutateAsync } = useCreatePost();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    e.stopPropagation();

    if (!ref.current || ref.current.value === "") return;

    await mutateAsync({ content: ref.current.value });

    ref.current.value = "";
  };

  return (
    <Container>
      <form onSubmit={(e) => handleSubmit(e)} className="flex flex-col gap-1">
        <TextArea
          ref={ref}
          size="3"
          placeholder="What's on your mind?"
          className="rounded-md"
        />
        <Button>Post</Button>
      </form>
    </Container>
  );
};

export default CreatePost;
