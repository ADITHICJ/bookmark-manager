alter table public.tags
add column created_at timestamptz not null default now();
