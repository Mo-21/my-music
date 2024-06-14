import axios from "axios";
import { useMutation } from "@tanstack/react-query";
import { Comment } from "../types/socialTypes";

interface CommentDetails {
  text: string;
  postId: number;
}

export const useCreateComment = () =>
  useMutation<Comment, Error, CommentDetails>({
    mutationKey: ["comments"],
    mutationFn: async ({ text, postId }: CommentDetails) =>
      await axios
        .post(`/social/posts/${postId}/comments/`, { text })
        .then((res) => res.data),
  });
