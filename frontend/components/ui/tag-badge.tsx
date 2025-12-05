import { cn } from '@/lib/utils';
import { TagColor } from '@/types/bookmark';

interface TagBadgeProps {
  name: string;
  color: TagColor;
  onRemove?: () => void;
  className?: string;
}

const colorClasses: Record<TagColor, string> = {
  red: 'bg-tag-red/15 text-tag-red border-tag-red/30',
  orange: 'bg-tag-orange/15 text-tag-orange border-tag-orange/30',
  yellow: 'bg-tag-yellow/15 text-tag-yellow border-tag-yellow/30',
  green: 'bg-tag-green/15 text-tag-green border-tag-green/30',
  teal: 'bg-tag-teal/15 text-tag-teal border-tag-teal/30',
  blue: 'bg-tag-blue/15 text-tag-blue border-tag-blue/30',
  purple: 'bg-tag-purple/15 text-tag-purple border-tag-purple/30',
  pink: 'bg-tag-pink/15 text-tag-pink border-tag-pink/30',
};

export function TagBadge({ name, color, onRemove, className }: TagBadgeProps) {
  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border',
        colorClasses[color],
        className
      )}
    >
      {name}
      {onRemove && (
        <button
          onClick={onRemove}
          className="hover:opacity-70 transition-opacity"
          type="button"
        >
          ×
        </button>
      )}
    </span>
  );
}
