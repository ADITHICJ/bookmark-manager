"use client";

import {
  SignedIn,
  SignedOut,
  SignInButton,
  SignUpButton,
  UserButton,
} from "@clerk/nextjs";
import { Button } from "./ui/button";

export default function Header() {
  return (
    <header className="w-full bg-linear-to-r from-[#6C47FF] to-[#8B5CFF] shadow-md">
      <div className="max-w-6xl mx-auto flex items-center justify-between px-4 py-4">
        {/* Logo / App Name */}
        <h1 className="text-xl sm:text-2xl font-semibold text-white tracking-wide">
          Bookmark Manager
        </h1>

        <div className="flex items-center gap-3">
          {/* Logged OUT Section */}
          <SignedOut>
            <SignInButton>
              <Button
                variant="outline"
                className="text-white border-white hover:bg-white/20"
              >
                Sign In
              </Button>
            </SignInButton>

            <SignUpButton>
              <Button
                variant="default"
                className="bg-white text-[#6C47FF] hover:bg-gray-100 font-medium"
              >
                Sign Up
              </Button>
            </SignUpButton>
          </SignedOut>

          {/* Logged IN Section */}
          <SignedIn>
            <UserButton
              appearance={{
                elements: {
                  userButtonAvatarBox: "ring-2 ring-white",
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
