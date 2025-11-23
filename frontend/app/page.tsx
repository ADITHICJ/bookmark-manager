"use client";

import { useEffect, useState } from "react";
import { useAuth } from "@clerk/nextjs";

export default function HomePage() {
  const { getToken, isSignedIn } = useAuth();
  const [bookmarks, setBookmarks] = useState([]);

  useEffect(() => {
    async function loadBookmarks() {
      if (!isSignedIn) return;

      // Get JWT from Clerk (fastapi = your template name)
      const token = await getToken({ template: "fastapi" });

      console.log("JWT:", token); // debug

      const res = await fetch("http://127.0.0.1:8000/api/bookmarks/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();
      console.log("Bookmarks:", data);
      setBookmarks(data);
    }

    loadBookmarks();
  }, [isSignedIn, getToken]);

  return (
    <div>
      <h1>Your Bookmarks</h1>

      {bookmarks.length === 0 ? (
        <p>No bookmarks found.</p>
      ) : (
        bookmarks.map((b: any) => (
          <div key={b.id}>
            <h3>{b.title}</h3>
            <p>{b.url}</p>
          </div>
        ))
      )}
    </div>
  );
}
