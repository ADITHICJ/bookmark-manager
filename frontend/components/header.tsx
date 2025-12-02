"use client";

import {
  SignedIn,
  SignedOut,
  SignInButton,
  SignUpButton,
  UserButton,
} from "@clerk/nextjs";
import { Button } from "./ui/button";
import { ModeToggle } from "./mode-toggle";

export default function Header() {
  return (
    <header className="w-full bg-[#6C47FF] shadow-md">
      {" "}
      {/* PURPLE HEADER */}
      <div className="max-w-6xl mx-auto flex items-center justify-between px-4 py-4">
        {/* Logo */}
        <h1 className="text-xl sm:text-2xl font-semibold text-white tracking-wide">
          Bookmark Manager
        </h1>

        <div className="flex items-center gap-3">
          {/* Theme Toggle */}
          <ModeToggle />

          {/* LOGGED OUT */}
          <SignedOut>
            <SignInButton>
              <Button className="bg-white text-[#6C47FF] hover:bg-gray-200 font-semibold">
                Sign In
              </Button>
            </SignInButton>

            <SignUpButton>
              <Button className="bg-white text-[#6C47FF] hover:bg-gray-200 font-semibold">
                Sign Up
              </Button>
            </SignUpButton>
          </SignedOut>

          {/* LOGGED IN */}
          <SignedIn>
            <UserButton
              appearance={{
                elements: {
                  avatarBox: "border-2 border-white", // purple theme match
                },
              }}
              afterSignOutUrl="/"
            />
          </SignedIn>
        </div>
      </div>
    </header>
  );
}
