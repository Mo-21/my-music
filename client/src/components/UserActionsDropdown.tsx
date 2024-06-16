import { DropdownMenu, Flex } from "@radix-ui/themes";
import CustomerAuthStatus from "./CustomerAuthStatus";
import LogoutButton from "./LogoutButton";
import { Link } from "react-router-dom";

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
            <Link to="/profile">Profile</Link>
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <LogoutButton />
          </DropdownMenu.Item>
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  );
};

export default UserActionsDropdown;
