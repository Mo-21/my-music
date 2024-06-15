import { TextField, Button } from "@radix-ui/themes";

const RegistrationForm = () => {
  return (
    <form className="flex flex-col gap-2">
      <TextField.Root placeholder="Email" />
      <TextField.Root placeholder="Username" />
      <TextField.Root placeholder="Password" />
      <TextField.Root placeholder="Confirm Password" />
      <Button>Submit</Button>
    </form>
  );
};

export default RegistrationForm;
