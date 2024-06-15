import { DropdownMenu, Flex } from "@radix-ui/themes";
import CustomerAuthStatus from "./CustomerAuthStatus";

const UserActionsDropdown = () => {
  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger className="cursor-pointer">
        <Flex align="center" justify="between" gap="4">
          <CustomerAuthStatus />
        </Flex>
      </DropdownMenu.Trigger>
      <DropdownMenu.Content sideOffset={5} align="end">
        <DropdownMenu.Group>
          <DropdownMenu.Item className="cursor-pointer">
            Profile
          </DropdownMenu.Item>
          <DropdownMenu.Item className="cursor-pointer">
            Settings
          </DropdownMenu.Item>
          <DropdownMenu.Item className="cursor-pointer">
            Logout
          </DropdownMenu.Item>
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  );
};

export default UserActionsDropdown;
