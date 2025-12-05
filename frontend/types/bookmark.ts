export interface Tag {
  id: string;
  name: string;
  color: TagColor;
}

export interface Category {
  id: string;
  name: string;
  icon?: string;
}

export interface Bookmark {
  id: string;
  url: string;
  title: string;
  description?: string;
  categoryId: string;
  tagIds: string[];
  createdAt: Date;
  favicon?: string;
}

export type TagColor = 'red' | 'orange' | 'yellow' | 'green' | 'teal' | 'blue' | 'purple' | 'pink';

export const TAG_COLORS: TagColor[] = ['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'pink'];
