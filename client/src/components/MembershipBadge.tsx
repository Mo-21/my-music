import { Badge } from "@radix-ui/themes";

interface MembershipBadgeProps {
  membershipStatus: "R" | "P";
}

const MembershipBadge = ({ membershipStatus }: MembershipBadgeProps) => {
  return (
    <Badge color={membershipStatus === "P" ? "green" : "pink"}>
      {membershipStatus}
    </Badge>
  );
};

export default MembershipBadge;
