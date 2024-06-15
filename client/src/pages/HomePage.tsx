import { Flex } from "@radix-ui/themes";
import MusicTab from "../components/MusicTab";
import PostsTab from "../components/PostsTab";
import CreatePost from "../components/CreatePost";

const HomePage = () => {
  return (
    <Flex justify="center" p="2">
      <MusicTab />
      <Flex mt="2" px="2" direction="column">
        <CreatePost />
        <PostsTab />
      </Flex>
      <MusicTab />
    </Flex>
  );
};

export default HomePage;
