import { render, screen } from "@testing-library/react";
import Registration from "../../src/pages/Registration";

describe("Registration", () => {
  it("should render an image with correct src", () => {
    render(<Registration />);

    const image = screen.getByRole("img");

    expect(image).toBeInTheDocument();
  });
});
