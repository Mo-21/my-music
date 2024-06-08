import { render, screen } from "@testing-library/react";
import Posts from "../../src/components/Posts";
import { Membership, Post } from "../../src/types/modelTypes";

describe("Posts", () => {
  it("should render posts lists", () => {
    const posts: Post[] = [
      {
        id: 1,
        content: "Hello",
        author: {
          id: 1,
          phone: "123",
          birthDate: "2021-10-10",
          membership_status: Membership.Regular,
          profile_image: "image",
          user: { id: 1, first_name: "John", last_name: "Doe", email: "" },
        },
        created_at: "2021-10-10",
      },
    ];
    render(<Posts posts={posts} />);

    const feed = screen.getByRole("feed");
    expect(feed).toBeInTheDocument();
  });
});
