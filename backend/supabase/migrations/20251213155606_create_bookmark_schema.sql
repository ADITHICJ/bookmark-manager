-- categories
create table public.categories (
  id uuid primary key default gen_random_uuid(),
  user_id text not null,
  name text not null,
  created_at timestamptz not null default now()
);

-- bookmarks
create table public.bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id text not null,
  title text not null,
  url text not null,
  description text,
  category_id uuid references public.categories(id),
  created_at timestamptz not null default now()
);

-- tags
create table public.tags (
  id uuid primary key default gen_random_uuid(),
  user_id text not null,
  name text not null,
  color text not null
);

-- bookmark_tags
create table public.bookmark_tags (
  bookmark_id uuid references public.bookmarks(id) on delete cascade,
  tag_id uuid references public.tags(id) on delete cascade,
  primary key (bookmark_id, tag_id)
);
