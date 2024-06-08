import { Flex, Text, Card, Heading } from "@radix-ui/themes";
import { Song } from "../types/musicTypes";

const SongList = ({ songs }: { songs: Song[] }) => {
  return (
    <>
      {songs.map((song) => (
        <Card role="feed" className="h-40" key={song.id}>
          <Flex direction="column" gap="3">
            <Flex justify="between">
              <Flex gap="2">
                <Heading size="3">{song.title}</Heading>
                <Heading size="3">{song.artist.name}</Heading>
              </Flex>
              <Text>{song.created_at.split("T")[0]}</Text>
            </Flex>
            <Text>{song.duration}</Text>
          </Flex>
        </Card>
      ))}
    </>
  );
};

export default SongList;
