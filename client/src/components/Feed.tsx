import { Box, Text, Spinner, Button, Flex } from "@radix-ui/themes";
import { usePosts } from "../hooks/usePosts";
import Posts from "./Posts";

const Feed = () => {
  const { data, error, isLoading, hasNextPage, fetchNextPage } = usePosts();

  if (error) return <Text>Error: {error.message}</Text>;
  if (isLoading) return <Spinner size="3" />;

  return (
    <Box>
      {data && data.pages.length === 0 && <Text>No posts found</Text>}
      {data && data.pages.map((group, i) => (
          <Flex mt="2" direction="column" gap="2" key={i}>
            <Posts posts={group.results} />
          </Flex>
        ))}

      {hasNextPage && (
        <Button className="mt-2" onClick={() => fetchNextPage()}>
          Load More
        </Button>
      )}
    </Box>
  );
};

export default Feed;
