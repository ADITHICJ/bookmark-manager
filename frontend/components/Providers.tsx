"use client";

import { BookmarkProvider } from "@/context/BookmarkContext";

export function AppProviders({ children }: { children: React.ReactNode }) {
  return <BookmarkProvider>{children}</BookmarkProvider>;
}
