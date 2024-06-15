import { Flex, Text, Card, Heading, Separator } from "@radix-ui/themes";
import { Post, Comment, PostAuthor } from "../types/socialTypes";
import LikeButton from "./LikeButton";
import CommentForm from "./CommentForm";
import CustomerAvatar from "./CustomerAvatar";
import MembershipBadge from "./MembershipBadge";

const PostsList = ({ posts }: { posts: Post[] }) => {
  return (
    <>
      {posts.map((post) => (
        <Card role="feed" className="min-h-[10rem] mb-4" key={post.id}>
          <Flex direction="column" gap="3" p="2">
            <Flex justify="between">
              <CustomerDetails author={post.author} />
              <Text>{post.created_at.split("T")[0]}</Text>
            </Flex>
            <Text>{post.content}</Text>
            <PostStats post={post} />
            <Separator size="4" />
            <CommentForm postId={post.id} />
            {post.comments_count > 0 && post.comments && (
              <Flex direction="column">
                <Comments comments={post.comments} />
              </Flex>
            )}
          </Flex>
        </Card>
      ))}
    </>
  );
};

const CustomerDetails = ({ author }: { author: PostAuthor }) => {
  return (
    <Flex align="center" gap="2">
      <CustomerAvatar
        src={author.profile_image}
        fallback={author.user.first_name[0]}
      />
      <Heading size="3">
        {author.user.first_name} {author.user.last_name}
      </Heading>
    </Flex>
  );
};

const PostStats = ({ post }: { post: Post }) => {
  return (
    <Flex justify="between">
      <Flex align="center" gap="4">
        <Text className="text-lg">{post.likes_count}</Text>
        <LikeButton postId={post.id} />
      </Flex>
      <Flex align="center" gap="4">
        <Text>Comments</Text>
        <Text className="text-lg">{post.comments_count}</Text>
      </Flex>
    </Flex>
  );
};

const Comments = ({ comments }: { comments: Comment[] }) => {
  return (
    <>
      {comments.map((c) => (
        <Flex mt="3" align="center" key={c.id} gap="2">
          <CustomerDetails author={c.user} />
          <MembershipBadge membershipStatus={c.user.membership_status} />
          <Text>{c.text}</Text>
        </Flex>
      ))}
    </>
  );
};

export default PostsList;
