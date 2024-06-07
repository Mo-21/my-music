import { Container } from "@radix-ui/themes";
import { usePosts } from "../hooks/usePosts";
import React from "react";

const HomePage = () => {
  const { data, error, isLoading } = usePosts();

  if (error) return <Container>Error: {error.message}</Container>;
  if (isLoading) return <Container>Loading...</Container>;

  return (
    <Container>
      <h1>Home Page</h1>
      <p>Welcome to the home page</p>
      {data?.pages.map((group, i) => (
        <React.Fragment key={i}>
          {group.results.map((post) => (
            <div key={post.id}>
              <h2>{post.createdAt}</h2>
              <p>{post.content}</p>
            </div>
          ))}
        </React.Fragment>
      ))}
    </Container>
  );
};

export default HomePage;
