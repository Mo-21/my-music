import { Box, Flex, Grid, Tabs } from "@radix-ui/themes";
import registrationImage from "../assets/mymusic-homepage-photo.jpg";
import musicLogo from "../assets/music-play.svg";
import LoginForm from "../components/LoginForm";
import RegistrationForm from "../components/RegistrationForm";

const Registration = () => {
  return (
    <Flex
      justify="center"
      align="center"
      className="w-full h-screen bg-cover"
      style={{ backgroundImage: `url(${registrationImage})` }}
    >
      <Grid className="w-full max-w-4xl grid-cols-1 md:grid-cols-4 lg:grid-cols-5">
        <img
          src={musicLogo}
          alt="musicLogo"
          className="w-24 h-24 md:w-60 md:h-60 col-span-1 justify-self-center"
        />

        <div className="col-span-1"></div>

        <Box className="bg-white p-8 rounded-lg shadow-md w-full col-span-2 lg:col-span-2">
          <RegistrationTabs />
        </Box>
      </Grid>
    </Flex>
  );
};

const RegistrationTabs = () => {
  return (
    <Tabs.Root defaultValue="login">
      <Tabs.List className="flex justify-center space-x-4">
        <Tabs.Trigger value="login">Log In</Tabs.Trigger>
        <Tabs.Trigger value="register">Register</Tabs.Trigger>
      </Tabs.List>

      <Box pt="3">
        <Tabs.Content value="login">
          <LoginForm />
        </Tabs.Content>

        <Tabs.Content value="register">
          <RegistrationForm />
        </Tabs.Content>
      </Box>
    </Tabs.Root>
  );
};

export default Registration;
