import { User } from "./socialTypes";

export interface Genre {
  id: number;
  name: string;
  description?: string;
}

export interface Artist {
  id: number;
  name: string;
  bio: string;
  created_at: string;
}

export interface Song {
  id: number;
  title: string;
  duration: string;
  item: string;
  genre: Genre;
  artist: Artist;
  created_at: string;
}

export interface Playlist {
  id: number;
  name: string;
  user: User;
  created_at: string;
}

export interface PlaylistItem {
  id: number;
  playlist: Playlist;
  song: Song;
}
