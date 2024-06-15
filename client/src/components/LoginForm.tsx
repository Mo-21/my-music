import { Button, TextField } from "@radix-ui/themes";

const LoginForm = () => {
  return (
    <form className="flex flex-col gap-2">
      <TextField.Root placeholder="Username" />
      <TextField.Root placeholder="Password" />
      <Button>Submit</Button>
    </form>
  );
};

export default LoginForm;
