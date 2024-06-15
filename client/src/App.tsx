import { Flex } from "@radix-ui/themes";
import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage";
import { useCurrentCustomer } from "./services/store";

const App = () => {
  const customer = useCurrentCustomer((c) => c.customer);

  return (
    <Flex direction="column">
      {customer && <Navbar />}
      <HomePage />
    </Flex>
  );
};

export default App;
