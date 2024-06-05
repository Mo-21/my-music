import registrationImage from "../assets/mymusic-homepage-photo.jpg";

const Registration = () => {
  return (
    <div>
      <img
        className="w-full h-screen object-cover"
        src={registrationImage}
        alt="registrationImage"
      />
    </div>
  );
};

export default Registration;
