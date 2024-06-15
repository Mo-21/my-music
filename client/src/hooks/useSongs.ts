import { useInfiniteQuery } from "@tanstack/react-query";
import { Song } from "../types/musicTypes";
import { axiosInstance } from "../services/axiosInstance ";

interface InfiniteSongs {
  count: number;
  next: string | null;
  previous: string | null;
  results: Song[];
}

interface ReactQueryTData {
  pageParam: number[];
  pages: InfiniteSongs[];
}

const baseUrl = "http://localhost:5173/music/songs/?limit=10";

export const useSongs = () =>
  useInfiniteQuery<InfiniteSongs, Error, ReactQueryTData, [string]>({
    queryKey: ["songs"],
    queryFn: fetchSongs,
    getNextPageParam: (lastPage) => lastPage.next || undefined,
    initialPageParam: baseUrl,
  });

const fetchSongs = async ({ pageParam }: { pageParam: unknown }) => {
  const url = typeof pageParam === "string" ? pageParam : baseUrl;
  return await axiosInstance.get<InfiniteSongs>(url).then((res) => res.data);
};
