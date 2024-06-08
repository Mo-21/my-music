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
  useInfiniteQuery<InfinitePosts, Error, ReactQueryTData, [string]>({
    queryKey: ["posts"],
    queryFn: async ({ pageParam }) => {
      const url =
        typeof pageParam === "string" ? pageParam : "/social/posts?limit=10";
      return await axios.get<InfinitePosts>(url).then((res) => res.data);
    },
    getNextPageParam: (lastPage) => lastPage.next || undefined,
    initialPageParam: "/social/posts?limit=10",
  });
