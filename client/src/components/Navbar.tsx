import { Box, Flex, Text } from "@radix-ui/themes";
import UserActionsDropdown from "./UserActionsDropdown";

const Navbar = () => {
  return (
    <Flex
      role="navigation"
      className="bg-black text-white p-4 justify-between items-center"
    >
      <Box className="text-xl font-bold">My Music</Box>
      <Text>
        <UserActionsDropdown />
      </Text>
    </Flex>
  );
};

export default Navbar;
