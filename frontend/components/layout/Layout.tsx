"use client";

import { useState } from "react";
import { Sidebar } from "./Sidebar";
import { Menu } from "lucide-react";

interface LayoutProps {
  children: React.ReactNode;
}

export function Layout({ children }: LayoutProps) {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSidebar = () => setIsOpen((prev) => !prev);

  return (
    <div className="min-h-screen bg-background">
      {/* Sidebar */}
      <Sidebar isOpen={isOpen} toggleSidebar={toggleSidebar} />

      {/* Toggle Button */}
      <button
        onClick={toggleSidebar}
        className="fixed top-4 left-4 lg:left-72 z-50 p-2 rounded-md bg-primary text-primary-foreground shadow hover:opacity-90 transition lg:hidden"
      >
        <Menu className="w-6 h-6" />
      </button>

      {/* Main Content shifts based on sidebar */}
      <main
        className={`transition-all duration-300 p-8 ${
          isOpen ? "lg:ml-64" : "ml-0"
        }`}
      >
        <div className="max-w-5xl mx-auto">{children}</div>
      </main>
    </div>
  );
}
