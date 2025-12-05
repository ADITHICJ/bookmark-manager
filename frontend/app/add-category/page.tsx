"use client";
import { useState } from 'react';
import { usePathname } from "next/navigation";
import { FolderOpen, Trash2 } from 'lucide-react';
import { useBookmarks } from '@/context/BookmarkContext';
import { Layout } from '@/components/layout/Layout';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import { toast } from 'sonner';

const EMOJI_OPTIONS = ['📁', '💼', '🏠', '📚', '🎮', '🎬', '🎵', '💡', '🔧', '🌐', '📰', '🛒'];

const AddCategory = () => {
  const pathname = usePathname();
  const { categories, addCategory, deleteCategory } = useBookmarks();
  const [name, setName] = useState('');
  const [selectedEmoji, setSelectedEmoji] = useState('📁');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!name.trim()) {
      toast.error('Please enter a category name');
      return;
    }

    addCategory({
      name: name.trim(),
      icon: selectedEmoji,
    });

    toast.success('Category created successfully!');
    setName('');
    setSelectedEmoji('📁');
  };

  return (
    <Layout>
      <div className="max-w-2xl animate-slide-up">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-2">
            Add Category
          </h1>
          <p className="text-muted-foreground">
            Create categories to organize your bookmarks
          </p>
        </header>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="bg-card rounded-xl border border-border p-6 space-y-5">
            <div className="space-y-2">
              <Label htmlFor="name">Category Name</Label>
              <Input
                id="name"
                placeholder="e.g., Development, Design, News"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>

            <div className="space-y-3">
              <Label>Icon</Label>
              <div className="flex flex-wrap gap-2">
                {EMOJI_OPTIONS.map((emoji) => (
                  <button
                    key={emoji}
                    type="button"
                    onClick={() => setSelectedEmoji(emoji)}
                    className={`w-10 h-10 rounded-lg text-xl flex items-center justify-center transition-all ${
                      selectedEmoji === emoji
                        ? 'bg-primary/10 ring-2 ring-primary'
                        : 'bg-muted hover:bg-muted/80'
                    }`}
                  >
                    {emoji}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <Button type="submit" className="w-full">
            Create Category
          </Button>
        </form>

        {categories.length > 0 && (
          <div className="mt-10">
            <h2 className="text-lg font-semibold text-foreground mb-4">
              Existing Categories
            </h2>
            <div className="space-y-2">
              {categories.map((category) => (
                <div
                  key={category.id}
                  className="flex items-center justify-between bg-card rounded-lg border border-border p-4 group"
                >
                  <div className="flex items-center gap-3">
                    <span className="text-xl">{category.icon}</span>
                    <span className="font-medium text-foreground">
                      {category.name}
                    </span>
                  </div>
                  <button
                    onClick={() => {
                      deleteCategory(category.id);
                      toast.success('Category deleted');
                    }}
                    className="p-2 rounded-lg opacity-0 group-hover:opacity-100 hover:bg-destructive/10 text-muted-foreground hover:text-destructive transition-all"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default AddCategory;
