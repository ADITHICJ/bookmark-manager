"use client";
import { useState } from 'react';
import { Trash2 } from 'lucide-react';
import { useBookmarks } from '@/context/BookmarkContext';
import { Layout } from '@/components/layout/Layout';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import { TagBadge } from '@/components/ui/tag-badge';
import { TAG_COLORS, TagColor } from '@/types/bookmark';
import { toast } from 'sonner';
import { cn } from '@/lib/utils';

const colorStyles: Record<TagColor, string> = {
  red: 'bg-tag-red',
  orange: 'bg-tag-orange',
  yellow: 'bg-tag-yellow',
  green: 'bg-tag-green',
  teal: 'bg-tag-teal',
  blue: 'bg-tag-blue',
  purple: 'bg-tag-purple',
  pink: 'bg-tag-pink',
};

const AddTag = () => {
  const { tags, addTag, deleteTag } = useBookmarks();
  const [name, setName] = useState('');
  const [selectedColor, setSelectedColor] = useState<TagColor>('teal');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!name.trim()) {
      toast.error('Please enter a tag name');
      return;
    }

    addTag({
      name: name.trim(),
      color: selectedColor,
    });

    toast.success('Tag created successfully!');
    setName('');
  };

  return (
    <Layout>
      <div className="max-w-2xl animate-slide-up">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-2">Add Tag</h1>
          <p className="text-muted-foreground">
            Create colorful tags to label your bookmarks
          </p>
        </header>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="bg-card rounded-xl border border-border p-6 space-y-5">
            <div className="space-y-2">
              <Label htmlFor="name">Tag Name</Label>
              <Input
                id="name"
                placeholder="e.g., Important, Read Later, Tutorial"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>

            <div className="space-y-3">
              <Label>Color</Label>
              <div className="flex flex-wrap gap-3">
                {TAG_COLORS.map((color) => (
                  <button
                    key={color}
                    type="button"
                    onClick={() => setSelectedColor(color)}
                    className={cn(
                      'w-8 h-8 rounded-full transition-all',
                      colorStyles[color],
                      selectedColor === color
                        ? 'ring-2 ring-offset-2 ring-foreground/30 scale-110'
                        : 'hover:scale-105'
                    )}
                    aria-label={`Select ${color} color`}
                  />
                ))}
              </div>
            </div>

            {name && (
              <div className="pt-2">
                <Label className="mb-2 block">Preview</Label>
                <TagBadge name={name || 'Tag Preview'} color={selectedColor} />
              </div>
            )}
          </div>

          <Button type="submit" className="w-full">
            Create Tag
          </Button>
        </form>

        {tags.length > 0 && (
          <div className="mt-10">
            <h2 className="text-lg font-semibold text-foreground mb-4">
              Existing Tags
            </h2>
            <div className="flex flex-wrap gap-3">
              {tags.map((tag) => (
                <div
                  key={tag.id}
                  className="group flex items-center gap-1 animate-scale-in"
                >
                  <TagBadge name={tag.name} color={tag.color} />
                  <button
                    onClick={() => {
                      deleteTag(tag.id);
                      toast.success('Tag deleted');
                    }}
                    className="p-1 rounded opacity-0 group-hover:opacity-100 hover:bg-destructive/10 text-muted-foreground hover:text-destructive transition-all"
                  >
                    <Trash2 className="w-3 h-3" />
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

export default AddTag;
