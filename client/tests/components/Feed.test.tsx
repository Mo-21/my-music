import { render, screen } from "@testing-library/react";
import { db } from "../mocks/db";
import AllProviders from "../pages/AllProviders";
import Feed from "../../src/components/Feed";

describe("Feed", () => {
  const postIds: number[] = [];

  beforeAll(() => {
    [1, 2, 3].forEach(() => {
      const post = db.post.create();
      postIds.push(post.id);
    });
  });

  afterAll(() => {
    db.post.deleteMany({ where: { id: { in: postIds } } });
  });

  it("should render posts", async () => {
    render(<Feed />, { wrapper: AllProviders });

    const posts = await screen.findAllByRole("feed");
    expect(posts.length).toBeGreaterThan(0);
  });
});
