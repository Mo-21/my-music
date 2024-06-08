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
    queryFn: fetchPosts,
    getNextPageParam: (lastPage) => lastPage.next || undefined,
    initialPageParam: "/social/posts?limit=10",
  });

const fetchPosts = async ({ pageParam }: { pageParam: unknown }) => {
  const url =
    typeof pageParam === "string" ? pageParam : "/social/posts?limit=10";
  return await axios.get<InfinitePosts>(url).then((res) => res.data);
};
