"use client";
import { useState } from 'react';
import { Search, Filter } from 'lucide-react';
import { useBookmarks } from '@/context/BookmarkContext';
import { BookmarkCard } from '@/components/bookmark/BookmarkCard';
import { Layout } from '@/components/layout/Layout';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';

const Index = () => {
  const { bookmarks, tags, categories, deleteBookmark } = useBookmarks();
  const [search, setSearch] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');

  const filteredBookmarks = bookmarks.filter((bookmark) => {
    const matchesSearch =
      bookmark.title.toLowerCase().includes(search.toLowerCase()) ||
      bookmark.url.toLowerCase().includes(search.toLowerCase());
    const matchesCategory =
      selectedCategory === 'all' || bookmark.categoryId === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <Layout>
      <div className="animate-slide-up">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-2">
            All Bookmarks
          </h1>
          <p className="text-muted-foreground">
            {bookmarks.length} bookmark{bookmarks.length !== 1 ? 's' : ''} saved
          </p>
        </header>

        <div className="flex flex-col sm:flex-row gap-4 mb-8">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <Input
              placeholder="Search bookmarks..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="pl-10"
            />
          </div>

          <Select value={selectedCategory} onValueChange={setSelectedCategory}>
            <SelectTrigger className="w-full sm:w-48">
              <Filter className="w-4 h-4 mr-2" />
              <SelectValue placeholder="Category" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Categories</SelectItem>
              {categories.map((category) => (
                <SelectItem key={category.id} value={category.id}>
                  {category.icon} {category.name}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {filteredBookmarks.length === 0 ? (
          <div className="text-center py-16">
            <div className="w-16 h-16 rounded-2xl bg-muted flex items-center justify-center mx-auto mb-4">
              <Search className="w-8 h-8 text-muted-foreground" />
            </div>
            <h2 className="text-xl font-semibold text-foreground mb-2">
              No bookmarks found
            </h2>
            <p className="text-muted-foreground">
              {search || selectedCategory !== 'all'
                ? 'Try adjusting your filters'
                : 'Start by adding your first bookmark'}
            </p>
          </div>
        ) : (
          <div className="space-y-4">
            {filteredBookmarks.map((bookmark) => (
              <BookmarkCard
                key={bookmark.id}
                bookmark={bookmark}
                tags={tags}
                category={categories.find((c) => c.id === bookmark.categoryId)}
                onDelete={() => deleteBookmark(bookmark.id)}
              />
            ))}
          </div>
        )}
      </div>
    </Layout>
  );
};

export default Index;
