import { Flex, Text, Card, Heading } from "@radix-ui/themes";
import { Song } from "../types/musicTypes";
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";

const SongList = ({ songs }: { songs: Song[] }) => {
  return (
    <>
      {songs.map((song) => (
        <Card role="feed" className="h-40 bg-green-100" key={song.id}>
          <Flex direction="column" gap="3">
            <Flex justify="between">
              <Flex direction="column">
                <Heading size="3">{song.title}</Heading>
                <Heading size="2">{song.artist.name}</Heading>
              </Flex>
              <Text>{song.created_at.split("T")[0]}</Text>
            </Flex>
            <AudioPlayer
              autoPlay={false}
              src={"http://localhost:8000" + song.item}
            />
          </Flex>
        </Card>
      ))}
    </>
  );
};

export default SongList;
