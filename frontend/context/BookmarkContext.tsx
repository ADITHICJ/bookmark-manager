import React, { createContext, useContext, useState, ReactNode } from 'react';
import { Bookmark, Tag, Category } from '@/types/bookmark';

interface BookmarkContextType {
  bookmarks: Bookmark[];
  tags: Tag[];
  categories: Category[];
  addBookmark: (bookmark: Omit<Bookmark, 'id' | 'createdAt'>) => void;
  addTag: (tag: Omit<Tag, 'id'>) => void;
  addCategory: (category: Omit<Category, 'id'>) => void;
  deleteBookmark: (id: string) => void;
  deleteTag: (id: string) => void;
  deleteCategory: (id: string) => void;
}

const BookmarkContext = createContext<BookmarkContextType | undefined>(undefined);

const initialCategories: Category[] = [
  { id: '1', name: 'Work', icon: '💼' },
  { id: '2', name: 'Personal', icon: '🏠' },
  { id: '3', name: 'Learning', icon: '📚' },
];

const initialTags: Tag[] = [
  { id: '1', name: 'Important', color: 'red' },
  { id: '2', name: 'Read Later', color: 'blue' },
  { id: '3', name: 'Reference', color: 'green' },
];

const initialBookmarks: Bookmark[] = [
  {
    id: '1',
    url: 'https://react.dev',
    title: 'React Documentation',
    description: 'The official React documentation',
    categoryId: '3',
    tagIds: ['2', '3'],
    createdAt: new Date(),
  },
  {
    id: '2',
    url: 'https://tailwindcss.com',
    title: 'Tailwind CSS',
    description: 'A utility-first CSS framework',
    categoryId: '3',
    tagIds: ['3'],
    createdAt: new Date(),
  },
];

export function BookmarkProvider({ children }: { children: ReactNode }) {
  const [bookmarks, setBookmarks] = useState<Bookmark[]>(initialBookmarks);
  const [tags, setTags] = useState<Tag[]>(initialTags);
  const [categories, setCategories] = useState<Category[]>(initialCategories);

  const addBookmark = (bookmark: Omit<Bookmark, 'id' | 'createdAt'>) => {
    const newBookmark: Bookmark = {
      ...bookmark,
      id: Date.now().toString(),
      createdAt: new Date(),
    };
    setBookmarks((prev) => [newBookmark, ...prev]);
  };

  const addTag = (tag: Omit<Tag, 'id'>) => {
    const newTag: Tag = {
      ...tag,
      id: Date.now().toString(),
    };
    setTags((prev) => [...prev, newTag]);
  };

  const addCategory = (category: Omit<Category, 'id'>) => {
    const newCategory: Category = {
      ...category,
      id: Date.now().toString(),
    };
    setCategories((prev) => [...prev, newCategory]);
  };

  const deleteBookmark = (id: string) => {
    setBookmarks((prev) => prev.filter((b) => b.id !== id));
  };

  const deleteTag = (id: string) => {
    setTags((prev) => prev.filter((t) => t.id !== id));
  };

  const deleteCategory = (id: string) => {
    setCategories((prev) => prev.filter((c) => c.id !== id));
  };

  return (
    <BookmarkContext.Provider
      value={{
        bookmarks,
        tags,
        categories,
        addBookmark,
        addTag,
        addCategory,
        deleteBookmark,
        deleteTag,
        deleteCategory,
      }}
    >
      {children}
    </BookmarkContext.Provider>
  );
}

export function useBookmarks() {
  const context = useContext(BookmarkContext);
  if (!context) {
    throw new Error('useBookmarks must be used within a BookmarkProvider');
  }
  return context;
}
