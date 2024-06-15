import { Avatar } from "@radix-ui/themes";
import { Responsive } from "@radix-ui/themes/props";

interface CustomerAvatarProps {
  src: string;
  fallback: string;
  size?: Responsive<"1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9">;
  variant?: "solid" | "soft";
}

const CustomerAvatar = ({
  src,
  fallback,
  size,
  variant,
}: CustomerAvatarProps) => {
  return (
    <Avatar
      src={"http://localhost:8000" + src}
      fallback={fallback}
      size={size || "2"}
      variant={variant || "solid"}
    />
  );
};

export default CustomerAvatar;
