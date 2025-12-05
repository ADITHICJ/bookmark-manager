"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Bookmark, Plus, Tag, FolderOpen, Home, X } from "lucide-react";
import { cn } from "@/lib/utils";

const navItems = [
  { path: "/", label: "All Bookmarks", icon: Home },
  { path: "/add-bookmark", label: "Add Bookmark", icon: Plus },
  { path: "/add-category", label: "Add Category", icon: FolderOpen },
  { path: "/add-tag", label: "Add Tag", icon: Tag },
];

export function Sidebar({
  isOpen,
  toggleSidebar,
}: {
  isOpen: boolean;
  toggleSidebar: () => void;
}) {
  const pathname = usePathname();

  return (
    <aside
      className={cn(
        "fixed top-0 left-0 h-screen bg-card border-r border-border p-6 flex flex-col shadow-lg transition-all duration-300",
        isOpen ? "w-64" : "w-0 overflow-hidden"
      )}
    >
      {/* Close button (mobile) */}
      <button
        onClick={toggleSidebar}
        className="lg:hidden absolute top-4 right-4 p-2 rounded-md bg-muted text-muted-foreground hover:bg-accent transition"
      >
        <X className="w-5 h-5" />
      </button>

      <div className="flex items-center gap-3 mb-10">
        <div className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center">
          <Bookmark className="w-5 h-5 text-primary-foreground" />
        </div>
        <span className="text-xl font-semibold text-foreground">Markly</span>
      </div>

      <nav className="flex-1 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = pathname === item.path;

          return (
            <Link
              key={item.path}
              href={item.path}
              className={cn(
                "flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200",
                "hover:bg-accent hover:text-accent-foreground",
                isActive
                  ? "bg-primary text-primary-foreground shadow-md"
                  : "text-muted-foreground"
              )}
            >
              <Icon className="w-5 h-5" />
              <span className="font-medium">{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="pt-6 border-t border-border">
        <p className="text-sm text-muted-foreground">
          Organize your web with ease
        </p>
      </div>
    </aside>
  );
}
