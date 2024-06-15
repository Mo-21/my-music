import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Registration from "./pages/Registration";
import CustomerProfile from "./pages/CustomerProfile";

export const router = createBrowserRouter([
  { path: "/", element: <App /> },
  { path: "/login", element: <Registration /> },
  { path: "/profile", element: <CustomerProfile /> },
]);
