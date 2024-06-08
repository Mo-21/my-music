import { Box, Button, Container } from "@radix-ui/themes";
import { usePosts } from "../hooks/usePosts";
import React from "react";

const HomePage = () => {
  const { data, error, isLoading, hasNextPage, fetchNextPage } = usePosts();

  if (error) return <Container>Error: {error.message}</Container>;
  if (isLoading) return <Container>Loading...</Container>;

  return (
    <Container>
      <Box className="prose">
        <h1>Home Page</h1>
        <p>Welcome to the home page</p>
        {data?.pages.map((group, i) => (
          <React.Fragment key={i}>
            {group.results.map((post) => (
              <div className="border-2 border-red-500" key={post.id}>
                <h2>{post.id}</h2>
                <p>{post.content}</p>
              </div>
            ))}
          </React.Fragment>
        ))}
      </Box>
      {hasNextPage ? (
        <Button onClick={() => fetchNextPage()}>Load More</Button>
      ) : null}
    </Container>
  );
};

export default HomePage;
