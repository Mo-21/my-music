export interface Post {
  id: number;
  content: string;
  image?: string;
  author: Customer;
  createdAt: string;
}

export interface Customer {
  id: number;
  phone: string;
  birthDate: string;
  membership: Membership;
  profileImage: string;
}

enum Membership {
  Regular = "R",
  Prime = "P",
}
