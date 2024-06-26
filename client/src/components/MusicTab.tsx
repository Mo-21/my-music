import { Spinner, Flex, Button, Text } from "@radix-ui/themes";
import { useSongs } from "../hooks/useSongs";
import SongList from "./SongList";

const MusicTab = () => {
  const { data, error, isLoading, hasNextPage, fetchNextPage } = useSongs();

  if (error) return <Text>Error: {error.message}</Text>;
  if (isLoading) return <Spinner size="3" />;
  return (
    <Flex gap="2" direction="column">
      {data && data.pages.length === 0 && (
        <Text className="text-gray-500">No music found</Text>
      )}
      {data &&
        data.pages.map((group, i) => (
          <Flex mt="2" direction="column" gap="2" key={i}>
            <SongList songs={group.results} />
          </Flex>
        ))}

      {hasNextPage && (
        <Button className="mt-2" onClick={() => fetchNextPage()}>
          Load More
        </Button>
      )}
    </Flex>
  );
};

export default MusicTab;
