-- 008_contributors_platforms.sql (SkillsContinuum)
-- Contributors are NOT "students" and not necessarily "staff".
-- They can still have an app_user (login) optionally.

BEGIN;

CREATE TABLE IF NOT EXISTS contributors (
  id            BIGSERIAL PRIMARY KEY,
  app_user_id   BIGINT UNIQUE REFERENCES app_users(id) ON DELETE SET NULL,
  display_name  TEXT NOT NULL,
  bio           TEXT,
  website       TEXT,
  status        TEXT NOT NULL DEFAULT 'active', -- active|suspended|archived
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT contributors_status_chk CHECK (status IN ('active','suspended','archived'))
);

CREATE INDEX IF NOT EXISTS idx_contributors_app_user_id ON contributors(app_user_id);
CREATE INDEX IF NOT EXISTS idx_contributors_status ON contributors(status);

-- Platform kinds: blog, podcast, reel/shorts, forum, gallery, etc.
CREATE TABLE IF NOT EXISTS platform_kinds (
  id          BIGSERIAL PRIMARY KEY,
  code        TEXT NOT NULL UNIQUE,  -- blog|podcast|reels|forum|gallery|newsletter|vlog|resources
  title       TEXT NOT NULL,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Core platforms (internal or external)
CREATE TABLE IF NOT EXISTS platforms (
  id            BIGSERIAL PRIMARY KEY,
  kind_id       BIGINT NOT NULL REFERENCES platform_kinds(id) ON DELETE RESTRICT,
  code          TEXT NOT NULL UNIQUE,      -- internal slug-ish
  title         TEXT NOT NULL,
  description   TEXT,
  is_internal   BOOLEAN NOT NULL DEFAULT TRUE,
  base_url      TEXT,                      -- for external platforms
  status        TEXT NOT NULL DEFAULT 'active', -- active|hidden|archived
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT platforms_status_chk CHECK (status IN ('active','hidden','archived'))
);

CREATE INDEX IF NOT EXISTS idx_platforms_kind_id ON platforms(kind_id);
CREATE INDEX IF NOT EXISTS idx_platforms_status ON platforms(status);

-- Contributor "presence" on a platform (e.g., blogger account, podcast host)
CREATE TABLE IF NOT EXISTS platform_accounts (
  id             BIGSERIAL PRIMARY KEY,
  platform_id    BIGINT NOT NULL REFERENCES platforms(id) ON DELETE CASCADE,
  contributor_id BIGINT NOT NULL REFERENCES contributors(id) ON DELETE CASCADE,
  handle         TEXT,
  profile_url    TEXT,
  role_label     TEXT,  -- host|editor|author|moderator etc (free text)
  status         TEXT NOT NULL DEFAULT 'active',
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(platform_id, contributor_id),
  CONSTRAINT platform_accounts_status_chk CHECK (status IN ('active','hidden','archived'))
);

CREATE INDEX IF NOT EXISTS idx_platform_accounts_platform_id ON platform_accounts(platform_id);
CREATE INDEX IF NOT EXISTS idx_platform_accounts_contributor_id ON platform_accounts(contributor_id);

-- Content contribution (generic): can target lessons/modules/tracks OR future "subjects/skills topics"
-- We keep targets polymorphic for flexibility; enforce via app rules + indexes.
CREATE TABLE IF NOT EXISTS contributions (
  id             BIGSERIAL PRIMARY KEY,
  contributor_id BIGINT NOT NULL REFERENCES contributors(id) ON DELETE CASCADE,

  -- Optional platform context (e.g., blog post vs forum post vs podcast episode)
  platform_id    BIGINT REFERENCES platforms(id) ON DELETE SET NULL,

  -- Generic target (where this contribution belongs)
  target_type    TEXT NOT NULL, -- lesson|unit|module|track|topic|skill|subject|platform|forum_thread etc.
  target_id      BIGINT NOT NULL,

  title          TEXT NOT NULL,
  body_md        TEXT,
  body_html      TEXT, -- optional pre-rendered cache
  status         TEXT NOT NULL DEFAULT 'draft', -- draft|published|hidden|archived
  published_at   TIMESTAMPTZ,

  meta           JSONB NOT NULL DEFAULT '{}'::jsonb,

  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT now(),

  CONSTRAINT contributions_status_chk CHECK (status IN ('draft','published','hidden','archived'))
);

CREATE INDEX IF NOT EXISTS idx_contributions_contributor_id ON contributions(contributor_id);
CREATE INDEX IF NOT EXISTS idx_contributions_platform_id ON contributions(platform_id);
CREATE INDEX IF NOT EXISTS idx_contributions_target ON contributions(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_contributions_status ON contributions(status);
CREATE INDEX IF NOT EXISTS idx_contributions_meta_gin ON contributions USING GIN (meta);

-- Seed platform kinds (idempotent)
INSERT INTO platform_kinds(code, title)
VALUES
  ('blog','Blog'),
  ('podcast','Podcast'),
  ('reels','Reels / Shorts'),
  ('forum','Forum'),
  ('gallery','Gallery'),
  ('newsletter','Newsletter'),
  ('vlog','Vlog'),
  ('resources','Resources Library')
ON CONFLICT (code) DO NOTHING;

COMMIT;
