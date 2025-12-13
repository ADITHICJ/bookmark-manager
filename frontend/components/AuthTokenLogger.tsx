"use client";

import { useEffect } from "react";
import { useAuth, SignedIn } from "@clerk/nextjs";

export default function AuthTokenLogger() {
  const { isSignedIn, getToken } = useAuth();

  useEffect(() => {
    let active = true;

    async function logTokenWhenSignedIn() {
      try {
        const token = await getToken({ template: "fastapi" });

        if (!token) {
          console.warn("No token returned by Clerk");
          return;
        }

        if (active) {
          console.log("Clerk FASTAPI bearer token:", token);
          console.log("JWT parts:", token.split(".").length); // should be 3
        }
      } catch (err) {
        console.warn("Failed to fetch Clerk token", err);
      }
    }

    if (isSignedIn) {
      logTokenWhenSignedIn();
    }

    return () => {
      active = false;
    };
  }, [isSignedIn, getToken]);

  return <SignedIn><span style={{ display: "none" }} /></SignedIn>;
}
