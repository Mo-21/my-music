import { Flex } from "@radix-ui/themes";
import PostsTab from "./PostsTab";
import MusicTab from "./MusicTab";

const Feed = () => {
  return (
    <Flex justify="center" gap="2">
      <PostsTab />
      <MusicTab />
    </Flex>
  );
};

export default Feed;
