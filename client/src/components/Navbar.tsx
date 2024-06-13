import { Box, Flex } from "@radix-ui/themes";

const Navbar = () => {
  return (
    <Flex
      role="navigation"
      className="bg-black text-white p-4 justify-between items-center"
    >
      <Box className="text-xl font-bold">My Music</Box>
    </Flex>
  );
};

export default Navbar;
