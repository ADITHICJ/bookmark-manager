"use client";

import { useEffect, useState } from "react";
import { useAuth } from "@clerk/nextjs";

export default function HomePage() {
  const { getToken, isSignedIn } = useAuth();
  const [bookmarks, setBookmarks] = useState<any[] | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function loadBookmarks() {
      if (!isSignedIn) return;  // no fetch when logged out

      setLoading(true);

      const token = await getToken({ template: "fastapi" });
      const API_URL = process.env.NEXT_PUBLIC_API_URL;

      const res = await fetch(`${API_URL}/api/bookmarks/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();
      setBookmarks(data);
      setLoading(false);
    }

    loadBookmarks();
  }, [isSignedIn, getToken]);

  // ----------------------------
  // UI LOGIC
  // ----------------------------

  if (!isSignedIn) {
    return <p>Please sign in to view your bookmarks.</p>;
  }

  if (loading || bookmarks === null) {
    return <p>Loading...</p>;
  }

  if (bookmarks.length === 0) {
    return <p>No bookmarks found.</p>;
  }

  return (
    <div>
      <h1>Your Bookmarks</h1>
      {bookmarks.map((b) => (
        <div key={b.id}>
          <h3>{b.title}</h3>
          <p>{b.url}</p>
        </div>
      ))}
    </div>
  );
}
