import React from "react";
import ReactDOM from "react-dom/client";
import { Theme } from "@radix-ui/themes";
import "@radix-ui/themes/styles.css";
import ReactQueryProviders from "./providers/ReactQueryProviders.tsx";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes.tsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ReactQueryProviders>
      <Theme accentColor="green">
        <RouterProvider router={router} />
      </Theme>
    </ReactQueryProviders>
  </React.StrictMode>
);
