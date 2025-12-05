import { ExternalLink, Trash2 } from 'lucide-react';
import { Bookmark, Tag, Category } from '@/types/bookmark';
import { TagBadge } from '@/components/ui/tag-badge';
import { cn } from '@/lib/utils';

interface BookmarkCardProps {
  bookmark: Bookmark;
  tags: Tag[];
  category?: Category;
  onDelete: () => void;
}

export function BookmarkCard({ bookmark, tags, category, onDelete }: BookmarkCardProps) {
  const bookmarkTags = tags.filter((t) => bookmark.tagIds.includes(t.id));

  const getFaviconUrl = (url: string) => {
    try {
      const domain = new URL(url).hostname;
      return `https://www.google.com/s2/favicons?domain=${domain}&sz=32`;
    } catch {
      return null;
    }
  };

  return (
    <article className="group bg-card rounded-xl border border-border p-5 shadow-sm hover:shadow-md transition-all duration-200 animate-fade-in">
      <div className="flex items-start gap-4">
        <div className="w-10 h-10 rounded-lg bg-muted flex items-center justify-center flex-shrink-0 overflow-hidden">
          {getFaviconUrl(bookmark.url) ? (
            <img
              src={getFaviconUrl(bookmark.url)!}
              alt=""
              className="w-5 h-5"
              onError={(e) => {
                e.currentTarget.style.display = 'none';
              }}
            />
          ) : (
            <ExternalLink className="w-4 h-4 text-muted-foreground" />
          )}
        </div>

        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1">
            <h3 className="font-semibold text-foreground truncate">
              {bookmark.title}
            </h3>
            {category && (
              <span className="text-sm text-muted-foreground flex-shrink-0">
                {category.icon} {category.name}
              </span>
            )}
          </div>

          <a
            href={bookmark.url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-primary hover:underline truncate block mb-2"
          >
            {bookmark.url}
          </a>

          {bookmark.description && (
            <p className="text-sm text-muted-foreground mb-3 line-clamp-2">
              {bookmark.description}
            </p>
          )}

          {bookmarkTags.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {bookmarkTags.map((tag) => (
                <TagBadge key={tag.id} name={tag.name} color={tag.color} />
              ))}
            </div>
          )}
        </div>

        <button
          onClick={onDelete}
          className={cn(
            'p-2 rounded-lg opacity-0 group-hover:opacity-100 transition-all duration-200',
            'hover:bg-destructive/10 text-muted-foreground hover:text-destructive'
          )}
          aria-label="Delete bookmark"
        >
          <Trash2 className="w-4 h-4" />
        </button>
      </div>
    </article>
  );
}
