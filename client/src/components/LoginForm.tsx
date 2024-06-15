import { Button, Spinner, TextField } from "@radix-ui/themes";
import { useRef } from "react";
import { useLogin } from "../hooks/useLogin";
import { useNavigate } from "react-router-dom";

const LoginForm = () => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  const { mutateAsync, isPending } = useLogin();
  const nav = useNavigate();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    e.stopPropagation();

    if (!usernameRef.current || !passwordRef.current) return;

    await mutateAsync({
      username: usernameRef.current.value,
      password: passwordRef.current.value,
    });

    nav("/");
  };

  return (
    <form onSubmit={(e) => handleSubmit(e)} className="flex flex-col gap-2">
      <TextField.Root ref={usernameRef} placeholder="Username" />
      <TextField.Root
        ref={passwordRef}
        placeholder="Password"
        type="password"
      />
      <Button>{isPending ? <Spinner /> : "Submit"}</Button>
    </form>
  );
};

export default LoginForm;
