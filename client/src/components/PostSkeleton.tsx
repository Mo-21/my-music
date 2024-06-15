import { Flex, Card, Container, Separator } from "@radix-ui/themes";
import Skeleton from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";

const PostSkeleton = () => {
  const posts = [1, 2, 3, 4];
  return (
    <Container>
      <Flex direction="column">
        <Flex mt="2" direction="column" gap="2">
          <>
            {posts.map((post) => (
              <Card role="feed" className="min-h-[10rem] mb-4" key={post}>
                <Flex direction="column" gap="3" p="2">
                  <Flex justify="between">
                    <Flex align="center" gap="2">
                      <Skeleton />
                    </Flex>
                    <Flex align="center" gap="4">
                      <Skeleton />
                    </Flex>
                  </Flex>
                  <Skeleton count={4} />
                  <Flex justify="between">
                    <Flex align="center" gap="4">
                      <Skeleton className="text-lg" />
                      <Skeleton />
                    </Flex>
                    <Flex align="center" gap="4">
                      <Skeleton />
                    </Flex>
                  </Flex>
                  <Separator size="4" />
                  <form className="grid grid-cols-12 gap-2">
                    <Skeleton count={4} />
                  </form>
                </Flex>
              </Card>
            ))}
          </>
        </Flex>
      </Flex>
    </Container>
  );
};

export default PostSkeleton;
