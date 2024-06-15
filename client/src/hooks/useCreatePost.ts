import { useMutation, useQueryClient } from "@tanstack/react-query";
import { ReactQueryTData } from "./usePosts";
import { Membership, Post } from "../types/socialTypes";
import { axiosInstance } from "../services/axiosInstance ";

export const useCreatePost = () => {
  const queryClient = useQueryClient();

  return useMutation<
    Post,
    Error,
    { content: string },
    { previousPosts: ReactQueryTData | undefined }
  >({
    mutationKey: ["posts"],
    mutationFn: async ({ content }: { content: string }) =>
      axiosInstance.post("/social/posts/", { content }).then((res) => res.data),
    onMutate: async (newPost) => {
      await queryClient.cancelQueries({
        queryKey: ["posts"],
      });

      const previousPosts = queryClient.getQueryData<ReactQueryTData>([
        "posts",
      ]);

      if (previousPosts) {
        queryClient.setQueryData<ReactQueryTData>(["posts"], (old) => {
          if (!old) return previousPosts;
          const tempPost = getTemporaryPost(newPost.content);
          return {
            ...old,
            pages: old.pages.map((page) => ({
              ...page,
              results: [...page.results, tempPost],
            })),
            pageParam: old.pageParam || [],
          };
        });
      }
      return { previousPosts };
    },
    onError: (_err, _newPost, context) => {
      queryClient.setQueryData(["posts"], context?.previousPosts);
    },
    onSettled: () => {
      queryClient.invalidateQueries({
        queryKey: ["posts"],
      });
    },
  });
};

const getTemporaryPost = (content: string): Post => ({
  id: Date.now(),
  content,
  image: undefined,
  author: {
    id: Date.now(),
    membership_status: Membership.Regular,
    profile_image: "",
    user: {
      id: Date.now(),
      first_name: "John",
      last_name: "Doe",
      email: "email@example.com",
    },
  },
  likes_count: 0,
  comments_count: 0,
  comments: null,
  created_at: new Date().toISOString(),
});
