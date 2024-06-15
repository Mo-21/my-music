import { Flex } from "@radix-ui/themes";
import MusicTab from "../components/MusicTab";
import PostsTab from "../components/PostsTab";

const HomePage = () => {
  return (
    <Flex justify="center" p="2">
      <MusicTab />
      <PostsTab />
      <MusicTab />
    </Flex>
  );
};

export default HomePage;
