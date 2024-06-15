import { Button } from "@radix-ui/themes";
import { useNavigate } from "react-router-dom";

const LogoutButton = () => {
  const navigate = useNavigate();
  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    sessionStorage.removeItem("customer");
    navigate("/login");
  };

  return (
    <Button
      onClick={() => handleLogout()}
      variant="ghost"
      color="red"
      className="cursor-pointer"
    >
      Logout
    </Button>
  );
};

export default LogoutButton;
