import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import { Theme } from "@radix-ui/themes";
import "@radix-ui/themes/styles.css";
import "./index.css";
import ReactQueryProviders from "./providers/ReactQueryProviders.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ReactQueryProviders>
      <Theme accentColor="green">
        <App />
      </Theme>
    </ReactQueryProviders>
  </React.StrictMode>
);
