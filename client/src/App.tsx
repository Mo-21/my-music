import { Flex } from "@radix-ui/themes";
import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage";

const App = () => {
  return (
    <Flex direction="column">
      <Navbar />
      <HomePage />
    </Flex>
  );
};

export default App;
