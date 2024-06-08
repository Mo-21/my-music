import { Box } from "@radix-ui/themes";
import Feed from "../components/Feed";

const HomePage = () => {
  return (
    <>
      <Box className="prose">
        <h1>Home Page</h1>
        <p>Welcome to the home page</p>
      </Box>
      <Feed />
    </>
  );
};

export default HomePage;
