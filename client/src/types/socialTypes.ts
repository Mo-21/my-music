export interface Post {
  id: number;
  content: string;
  image?: string;
  author: PostAuthor;
  likes_count: number;
  comments_count: number;
  comments: Comment[] | null;
  created_at: string;
}

export interface PostAuthor {
  id: number;
  membership_status: Membership;
  profile_image: string;
  user: User;
}

export interface Customer {
  id: number;
  phone: string;
  birthdate: string | null;
  membership_status: Membership;
  profile_image: string;
  user: User;
  authored_posts: Post[];
  liked_posts: number[];
}

export interface User {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
}

export enum Membership {
  Regular = "R",
  Prime = "P",
}

export interface Comment {
  id: number;
  user: Customer;
  text: string;
  created_at: string;
}
