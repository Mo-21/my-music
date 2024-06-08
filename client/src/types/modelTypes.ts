export interface Post {
  id: number;
  content: string;
  image?: string;
  author: Customer;
  created_at: string;
}

export interface Customer {
  id: number;
  phone: string;
  birthDate: string;
  membership_status: Membership;
  profile_image: string;
  user: User;
}

export interface User {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
}

enum Membership {
  Regular = "R",
  Prime = "P",
}
