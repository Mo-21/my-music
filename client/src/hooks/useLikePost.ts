import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useCurrentCustomer } from "../services/store";
import { ReactQueryTData } from "./usePosts";
import { axiosInstance } from "../services/axiosInstance ";

interface LikeResponse {
  id: number;
  user: number;
  post: string;
  created_at: string;
}

export const useLikePost = (postId: number) => {
  const queryClient = useQueryClient();
  const { customer, setCustomer } = useCurrentCustomer();

  return useMutation<
    LikeResponse,
    Error,
    void,
    {
      previousPosts: ReactQueryTData | undefined;
      previousCustomer: typeof customer | undefined;
    }
  >({
    mutationKey: ["post-like"],
    mutationFn: async () => {
      return axiosInstance
        .post(`/social/posts/${postId}/likes/`)
        .then((res) => res.data);
    },
    onMutate: async () => {
      await queryClient.cancelQueries({ queryKey: ["posts"] });
      await queryClient.cancelQueries({ queryKey: ["current_customer"] });

      const previousPosts = queryClient.getQueryData<ReactQueryTData>([
        "posts",
      ]);
      const previousCustomer = customer;

      if (previousPosts && customer) {
        queryClient.setQueryData<ReactQueryTData>(["posts"], (old) => {
          if (!old) return old;
          const updatedPages = old.pages.map((page) => ({
            ...page,
            results: page.results.map((post) => {
              if (post.id === postId) {
                return {
                  ...post,
                  likes_count: customer.liked_posts.includes(postId)
                    ? post.likes_count - 1
                    : post.likes_count + 1,
                };
              }
              return post;
            }),
          }));
          return { ...old, pages: updatedPages };
        });

        const updatedLikedPosts = customer.liked_posts.includes(postId)
          ? customer.liked_posts.filter((id) => id !== postId)
          : [...customer.liked_posts, postId];

        setCustomer({
          ...customer,
          liked_posts: updatedLikedPosts,
        });
      }

      return { previousPosts, previousCustomer };
    },
    onError: (_err, _variables, context) => {
      if (context?.previousPosts) {
        queryClient.setQueryData<ReactQueryTData>(
          ["posts"],
          context.previousPosts
        );
      }
      if (context?.previousCustomer) {
        setCustomer(context.previousCustomer);
      }
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["posts"] });
      queryClient.invalidateQueries({ queryKey: ["current_customer"] });
    },
  });
};
