import { Box, Flex, Text } from "@radix-ui/themes";
import CustomerAuthStatus from "./CustomerAuthStatus";

const Navbar = () => {
  return (
    <Flex
      role="navigation"
      className="bg-black text-white p-4 justify-between items-center"
    >
      <Box className="text-xl font-bold">My Music</Box>
      <Text>
        <CustomerAuthStatus />
      </Text>
    </Flex>
  );
};

export default Navbar;
