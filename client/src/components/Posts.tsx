import { Flex, Text, Card, Heading, Avatar } from "@radix-ui/themes";
import { Post } from "../types/modelTypes";

const Posts = ({ posts }: { posts: Post[] }) => {
  return (
    <>
      {posts.map((post) => (
        <Card role="feed" className="h-40" key={post.id}>
          <Flex direction="column" gap="3">
            <Flex justify="between">
              <Flex gap="2">
                <Avatar
                  src={"http://localhost:8000" + post.author.profile_image}
                  fallback={post.author.user.first_name[0]}
                />
                <Heading size="3">
                  {post.author.user.first_name} {post.author.user.last_name}
                </Heading>
              </Flex>
              <Text>{post.created_at.split("T")[0]}</Text>
            </Flex>
            <Text>{post.content}</Text>
          </Flex>
        </Card>
      ))}
    </>
  );
};

export default Posts;
