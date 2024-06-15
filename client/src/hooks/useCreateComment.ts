import { useMutation, useQueryClient } from "@tanstack/react-query";
import { Comment } from "../types/socialTypes";
import { useCurrentCustomer } from "../services/store";
import { ReactQueryTData } from "./usePosts";
import { axiosInstance } from "../services/axiosInstance ";

interface CommentDetails {
  text: string;
  postId: number;
}

interface CommentContext {
  previousPosts: ReactQueryTData | undefined;
}

export const useCreateComment = () => {
  const queryClient = useQueryClient();
  const { customer } = useCurrentCustomer();

  return useMutation<Comment, Error, CommentDetails, CommentContext>({
    mutationKey: ["comments"],
    mutationFn: async ({ text, postId }: CommentDetails) =>
      await axiosInstance
        .post(`/social/posts/${postId}/comments/`, { text })
        .then((res) => res.data),
    onMutate: async ({ text, postId }) => {
      await queryClient.cancelQueries({ queryKey: ["posts"] });

      const previousPosts = queryClient.getQueryData<ReactQueryTData>([
        "posts",
      ]);

      if (previousPosts && customer) {
        queryClient.setQueryData<ReactQueryTData>(["posts"], (old) => {
          if (!old) return old;

          const updatedPages = old.pages.map((page) => ({
            ...page,
            results: page.results.map((post) => {
              if (post.id === postId) {
                const newComment = {
                  id: Date.now(), // Temporary ID for the new comment
                  user: customer,
                  text,
                  created_at: new Date().toISOString(),
                };

                return {
                  ...post,
                  comments_count: post.comments_count + 1,
                  comments: post.comments
                    ? [newComment, ...post.comments]
                    : [newComment],
                };
              }
              return post;
            }),
          }));

          return { ...old, pages: updatedPages };
        });
      }

      return { previousPosts };
    },
    onError: (_err, _variables, context) => {
      if (context?.previousPosts) {
        queryClient.setQueryData<ReactQueryTData>(
          ["posts"],
          context.previousPosts
        );
      }
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["posts"] });
    },
  });
};
