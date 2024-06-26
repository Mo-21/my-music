import { Container, Flex } from "@radix-ui/themes";
import MusicTab from "../components/MusicTab";
import PostsTab from "../components/PostsTab";
import CreatePost from "../components/CreatePost";

const HomePage = () => {
  return (
    <Container>
      <Flex p="2" gap="5">
        <Flex mt="2" px="2" direction="column" className="w-full">
          <CreatePost />
          <PostsTab />
        </Flex>
        <MusicTab />
      </Flex>
    </Container>
  );
};

export default HomePage;
