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
import { Menu } from "lucide-react";

export default function Header({
  toggleSidebar,
}: {
  toggleSidebar: () => void;
}) {
  return (
    <header className="fixed top-0 left-0 right-0 h-16 bg-[#6C47FF] shadow-md z-40">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-4 h-full">
        {/* LEFT */}
        <div className="flex items-center gap-3">
          {/* Sidebar Toggle */}
          <button
            onClick={toggleSidebar}
            className="p-2 rounded-md hover:bg-white/10 transition"
          >
            <Menu className="w-6 h-6 text-white" />
          </button>

          {/* Logo */}
          <h1 className="text-xl sm:text-2xl font-semibold text-white tracking-wide">
            Bookmark Manager
          </h1>
        </div>

        {/* RIGHT */}
        <div className="flex items-center gap-3">
          <ModeToggle />

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

          <SignedIn>
            <UserButton
              appearance={{
                elements: {
                  avatarBox: "border-2 border-white",
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
