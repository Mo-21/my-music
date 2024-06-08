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
  profileImage: string;
}

enum Membership {
  Regular = "R",
  Prime = "P",
}
