import { Box, Container } from "@radix-ui/themes";
import Feed from "../components/Feed";

const HomePage = () => {
  return (
    <Container>
      <Box className="prose">
        <h1>Home Page</h1>
        <p>Welcome to the home page</p>
      </Box>
      <Feed />
    </Container>
  );
};

export default HomePage;
