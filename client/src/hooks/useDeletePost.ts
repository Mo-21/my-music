import { useQueryClient, useMutation } from "@tanstack/react-query";
import { ReactQueryTData } from "./usePosts";
import { axiosInstance } from "../services/axiosInstance ";

export const useDeletePost = () => {
  const queryClient = useQueryClient();

  return useMutation<
    void,
    Error,
    { postId: number },
    { previousPosts: ReactQueryTData | undefined }
  >({
    mutationKey: ["posts"],
    mutationFn: async ({ postId }) => {
      return axiosInstance.delete(`/social/posts/${postId}/`);
    },
    onMutate: async ({ postId }) => {
      await queryClient.cancelQueries({ queryKey: ["posts"] });

      const previousPosts = queryClient.getQueryData<ReactQueryTData>([
        "posts",
      ]);

      if (previousPosts) {
        queryClient.setQueryData<ReactQueryTData>(["posts"], (old) => {
          if (!old) return previousPosts;
          return {
            ...old,
            pages: old.pages.map((page) => ({
              ...page,
              results: page.results.filter((post) => post.id !== postId),
            })),
            pageParam: old.pageParam || [],
          };
        });
      }
      return { previousPosts };
    },
    onError: (_err, _variables, context) => {
      queryClient.setQueryData(["posts"], context?.previousPosts);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["posts"] });
    },
  });
};
