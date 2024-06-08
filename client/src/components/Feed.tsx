import { Box } from "@radix-ui/themes";
import PostsTab from "./PostsTab";
import MusicTab from "./MusicTab";

const Feed = () => {
  return (
    <Box>
      <PostsTab />
      <MusicTab />
    </Box>
  );
};

export default Feed;
