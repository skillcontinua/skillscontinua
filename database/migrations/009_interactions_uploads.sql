-- 009_interactions_uploads.sql (SkillsContinuum)
-- Interactions: comments + reactions + moderation flags
-- Uploads: extend attachments + link attachments to contributions and other targets.

BEGIN;

-- ------------------------------------------------------------
-- Extend attachments (single unified upload system)
-- ------------------------------------------------------------
ALTER TABLE attachments
  ADD COLUMN IF NOT EXISTS storage_backend TEXT NOT NULL DEFAULT 'local', -- local|s3|gcs|external
  ADD COLUMN IF NOT EXISTS storage_key TEXT,       -- path/object key (for local/s3)
  ADD COLUMN IF NOT EXISTS external_url TEXT,      -- when storage_backend=external
  ADD COLUMN IF NOT EXISTS original_filename TEXT,
  ADD COLUMN IF NOT EXISTS mime_type TEXT,
  ADD COLUMN IF NOT EXISTS byte_size BIGINT,
  ADD COLUMN IF NOT EXISTS checksum_sha256 TEXT,
  ADD COLUMN IF NOT EXISTS kind TEXT NOT NULL DEFAULT 'file', -- file|image|audio|video|pdf|link
  ADD COLUMN IF NOT EXISTS uploaded_by_user_id BIGINT REFERENCES app_users(id) ON DELETE SET NULL,
  ADD COLUMN IF NOT EXISTS uploaded_by_staff_id BIGINT REFERENCES staff_users(id) ON DELETE SET NULL,
  ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ NOT NULL DEFAULT now();

CREATE INDEX IF NOT EXISTS idx_attachments_kind ON attachments(kind);
CREATE INDEX IF NOT EXISTS idx_attachments_uploaded_by_user_id ON attachments(uploaded_by_user_id);
CREATE INDEX IF NOT EXISTS idx_attachments_uploaded_by_staff_id ON attachments(uploaded_by_staff_id);
CREATE INDEX IF NOT EXISTS idx_attachments_storage_backend ON attachments(storage_backend);

-- ------------------------------------------------------------
-- Attachments linked to contributor contributions
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS contribution_attachments (
  contribution_id BIGINT NOT NULL REFERENCES contributions(id) ON DELETE CASCADE,
  attachment_id   BIGINT NOT NULL REFERENCES attachments(id) ON DELETE CASCADE,
  sort_order      INT NOT NULL DEFAULT 0,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (contribution_id, attachment_id)
);

CREATE INDEX IF NOT EXISTS idx_contribution_attachments_attachment_id ON contribution_attachments(attachment_id);

-- ------------------------------------------------------------
-- Interactions: comments (actor always app_users)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS comments (
  id             BIGSERIAL PRIMARY KEY,
  actor_user_id  BIGINT NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,

  target_type    TEXT NOT NULL,   -- contribution|lesson|unit|module|track|platform|thread|etc
  target_id      BIGINT NOT NULL,

  parent_id      BIGINT REFERENCES comments(id) ON DELETE CASCADE, -- threaded replies
  body_md        TEXT NOT NULL,
  body_html      TEXT,

  status         TEXT NOT NULL DEFAULT 'visible', -- visible|hidden|deleted
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT now(),

  CONSTRAINT comments_status_chk CHECK (status IN ('visible','hidden','deleted'))
);

CREATE INDEX IF NOT EXISTS idx_comments_actor_user_id ON comments(actor_user_id);
CREATE INDEX IF NOT EXISTS idx_comments_target ON comments(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_comments_parent_id ON comments(parent_id);
CREATE INDEX IF NOT EXISTS idx_comments_status ON comments(status);

-- ------------------------------------------------------------
-- Interactions: reactions (like, agree, helpful, etc.)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS reactions (
  id             BIGSERIAL PRIMARY KEY,
  actor_user_id  BIGINT NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,

  target_type    TEXT NOT NULL,
  target_id      BIGINT NOT NULL,

  reaction_type  TEXT NOT NULL, -- like|agree|helpful|insightful|bookmark etc
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),

  UNIQUE(actor_user_id, target_type, target_id, reaction_type)
);

CREATE INDEX IF NOT EXISTS idx_reactions_target ON reactions(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_reactions_actor ON reactions(actor_user_id);

-- ------------------------------------------------------------
-- Moderation flags (report/abuse)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS moderation_flags (
  id               BIGSERIAL PRIMARY KEY,
  reporter_user_id BIGINT NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,

  target_type      TEXT NOT NULL,
  target_id        BIGINT NOT NULL,

  reason_code      TEXT NOT NULL, -- spam|abuse|hate|copyright|other
  detail           TEXT,
  status           TEXT NOT NULL DEFAULT 'open', -- open|reviewing|closed
  created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now(),

  CONSTRAINT moderation_flags_status_chk CHECK (status IN ('open','reviewing','closed'))
);

CREATE INDEX IF NOT EXISTS idx_moderation_flags_target ON moderation_flags(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_moderation_flags_status ON moderation_flags(status);
CREATE INDEX IF NOT EXISTS idx_moderation_flags_reporter ON moderation_flags(reporter_user_id);

COMMIT;
