import { render, screen } from "@testing-library/react";
import { db } from "../mocks/db";
import HomePage from "../../src/pages/HomePage";
import AllProviders from "./AllProviders";

describe("HomePage", () => {
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
    render(<HomePage />, { wrapper: AllProviders });

    const posts = await screen.findAllByRole("feed");
    expect(posts.length).toBeGreaterThan(0);
  });
});
