import { create } from "zustand";
import { createJSONStorage, persist } from "zustand/middleware";
import { Customer } from "../types/socialTypes";

interface CustomerStore {
  customer: Customer | null;
  setCustomer: (customer: Customer) => void;
  removeCustomer: () => void;
}

export const useCurrentCustomer = create<CustomerStore>()(
  persist(
    (set) => ({
      customer: null,
      setCustomer: (customer) => set(() => ({ customer })),
      removeCustomer: () => set(() => ({ customer: null })),
    }),
    {
      name: "customer",
      storage: createJSONStorage(() => sessionStorage),
    }
  )
);
