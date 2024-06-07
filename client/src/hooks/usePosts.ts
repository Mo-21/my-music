import { useInfiniteQuery } from "@tanstack/react-query";
import axios from "axios";
import { Post } from "../types/modelTypes";

interface InfinitePosts {
  count: number;
  next: string | null;
  previous: string | null;
  results: Post[];
}

interface ReactQueryTData {
  pageParam: number[];
  pages: InfinitePosts[];
}

export const usePosts = () =>
  useInfiniteQuery<InfinitePosts, Error, ReactQueryTData>({
    queryKey: ["posts"],
    queryFn: async () =>
      await axios.get<InfinitePosts>("/social/posts").then((res) => res.data),
    getNextPageParam: (lastPage) => lastPage.next ?? false,
    initialPageParam: 1,
  });
