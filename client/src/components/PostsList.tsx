import { Flex, Text, Card, Heading, Avatar } from "@radix-ui/themes";
import { Post } from "../types/socialTypes";
import LikeButton from "./LikeButton";

const PostsList = ({ posts }: { posts: Post[] }) => {
  return (
    <>
      {posts.map((post) => (
        <Card role="feed" className="min-h-[10rem] mb-4" key={post.id}>
          <Flex direction="column" gap="3" p="2">
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
            <Flex align="center" gap="4">
              <Text className="text-lg">{post.likes_count}</Text>
              <LikeButton postId={post.id} />
            </Flex>
          </Flex>
        </Card>
      ))}
    </>
  );
};

export default PostsList;
