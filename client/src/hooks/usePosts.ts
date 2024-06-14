import { useInfiniteQuery } from "@tanstack/react-query";
import axios from "axios";
import { Post } from "../types/socialTypes";

interface InfinitePosts {
  count: number;
  next: string | null;
  previous: string | null;
  results: Post[];
}

export interface ReactQueryTData {
  pageParam: number[];
  pages: InfinitePosts[];
}

const baseUrl = "http://localhost:5173/social/posts?limit=10";

export const usePosts = () =>
  useInfiniteQuery<InfinitePosts, Error, ReactQueryTData, [string]>({
    queryKey: ["posts"],
    queryFn: fetchPosts,
    getNextPageParam: (lastPage) => lastPage.next || undefined,
    initialPageParam: baseUrl,
  });

const fetchPosts = async ({ pageParam }: { pageParam: unknown }) => {
  const url = typeof pageParam === "string" ? pageParam : baseUrl;
  return await axios.get<InfinitePosts>(url).then((res) => res.data);
};
