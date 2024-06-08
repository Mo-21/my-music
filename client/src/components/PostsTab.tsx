import { Button, Flex, Spinner, Text } from "@radix-ui/themes";
import { usePosts } from "../hooks/usePosts";
import PostsList from "./PostsList";

const PostsTab = () => {
  const { data, error, isLoading, hasNextPage, fetchNextPage } = usePosts();

  if (error) return <Text>Error: {error.message}</Text>;
  if (isLoading) return <Spinner size="3" />;
  return (
    <>
      {data && data.pages.length === 0 && <Text>No posts found</Text>}
      {data &&
        data.pages.map((group, i) => (
          <Flex mt="2" direction="column" gap="2" key={i}>
            <PostsList posts={group.results} />
          </Flex>
        ))}

      {hasNextPage && (
        <Button className="mt-2" onClick={() => fetchNextPage()}>
          Load More
        </Button>
      )}
    </>
  );
};

export default PostsTab;
