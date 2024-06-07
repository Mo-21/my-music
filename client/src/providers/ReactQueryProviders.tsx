import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools/production";
import { PropsWithChildren } from "react";

const ReactQueryProviders = ({ children }: PropsWithChildren) => {
  const queryClient = new QueryClient();
  return (
    <QueryClientProvider client={queryClient}>
      {children}
      {import.meta.env.MODE === "development" && <ReactQueryDevtools />}
    </QueryClientProvider>
  );
};

export default ReactQueryProviders;
