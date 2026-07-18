BEGIN;

CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS citext;

CREATE TABLE IF NOT EXISTS users (
  id            BIGSERIAL PRIMARY KEY,
  uuid          UUID NOT NULL DEFAULT gen_random_uuid(),
  email         CITEXT UNIQUE,
  phone         TEXT UNIQUE,
  full_name     TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  is_active     BOOLEAN NOT NULL DEFAULT TRUE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS roles (
  id        BIGSERIAL PRIMARY KEY,
  code      TEXT NOT NULL UNIQUE,
  name      TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS user_roles (
  user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  role_id BIGINT NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
  PRIMARY KEY (user_id, role_id)
);

CREATE TABLE IF NOT EXISTS programs (
  id        BIGSERIAL PRIMARY KEY,
  code      TEXT NOT NULL UNIQUE,
  name      TEXT NOT NULL,
  level     TEXT NOT NULL DEFAULT 'pathway',
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS tracks (
  id         BIGSERIAL PRIMARY KEY,
  program_id BIGINT NOT NULL REFERENCES programs(id) ON DELETE CASCADE,
  code       TEXT NOT NULL,
  name       TEXT NOT NULL,
  is_active  BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(program_id, code)
);

CREATE TABLE IF NOT EXISTS courses (
  id         BIGSERIAL PRIMARY KEY,
  track_id   BIGINT NOT NULL REFERENCES tracks(id) ON DELETE CASCADE,
  code       TEXT NOT NULL,
  title      TEXT NOT NULL,
  summary    TEXT NOT NULL DEFAULT '',
  difficulty TEXT NOT NULL DEFAULT 'beginner',
  hours_est  INT NOT NULL DEFAULT 0,
  is_active  BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(track_id, code)
);

CREATE TABLE IF NOT EXISTS modules (
  id         BIGSERIAL PRIMARY KEY,
  course_id  BIGINT NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  code       TEXT NOT NULL,
  title      TEXT NOT NULL,
  summary    TEXT NOT NULL DEFAULT '',
  ord        INT NOT NULL DEFAULT 0,
  is_active  BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(course_id, code)
);

CREATE TABLE IF NOT EXISTS lessons (
  id         BIGSERIAL PRIMARY KEY,
  module_id  BIGINT NOT NULL REFERENCES modules(id) ON DELETE CASCADE,
  code       TEXT NOT NULL,
  title      TEXT NOT NULL,
  content_md TEXT NOT NULL DEFAULT '',
  ord        INT NOT NULL DEFAULT 0,
  is_active  BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(module_id, code)
);

CREATE TABLE IF NOT EXISTS assessments (
  id          BIGSERIAL PRIMARY KEY,
  course_id   BIGINT NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  code        TEXT NOT NULL,
  title       TEXT NOT NULL,
  kind        TEXT NOT NULL DEFAULT 'project',
  instructions_md TEXT NOT NULL DEFAULT '',
  rubric_md   TEXT NOT NULL DEFAULT '',
  max_score   INT NOT NULL DEFAULT 100,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(course_id, code)
);

CREATE TABLE IF NOT EXISTS submissions (
  id            BIGSERIAL PRIMARY KEY,
  assessment_id BIGINT NOT NULL REFERENCES assessments(id) ON DELETE CASCADE,
  user_id       BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  status        TEXT NOT NULL DEFAULT 'submitted',
  score         INT,
  feedback_md   TEXT NOT NULL DEFAULT '',
  submitted_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  reviewed_at   TIMESTAMPTZ,
  UNIQUE(assessment_id, user_id)
);

CREATE TABLE IF NOT EXISTS portfolio_items (
  id          BIGSERIAL PRIMARY KEY,
  user_id     BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title       TEXT NOT NULL,
  description TEXT NOT NULL DEFAULT '',
  url         TEXT,
  repo_url    TEXT,
  tags        TEXT[] NOT NULL DEFAULT '{}',
  is_public   BOOLEAN NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS certificates (
  id            BIGSERIAL PRIMARY KEY,
  user_id       BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  program_id    BIGINT REFERENCES programs(id) ON DELETE SET NULL,
  track_id      BIGINT REFERENCES tracks(id) ON DELETE SET NULL,
  code          TEXT NOT NULL UNIQUE,
  title         TEXT NOT NULL,
  issued_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  meta          JSONB NOT NULL DEFAULT '{}'::jsonb
);

INSERT INTO roles(code, name)
VALUES
 ('admin','Administrator'),
 ('instructor','Instructor'),
 ('learner','Learner'),
 ('reviewer','Reviewer')
ON CONFLICT (code) DO NOTHING;

INSERT INTO programs(code, name, level)
VALUES ('WEB_FOUNDATION','Web Development Foundation','pathway')
ON CONFLICT (code) DO NOTHING;

WITH p AS (SELECT id FROM programs WHERE code='WEB_FOUNDATION' LIMIT 1)
INSERT INTO tracks(program_id, code, name)
SELECT p.id, 'WEB_DEV', 'Web Development'
FROM p
ON CONFLICT (program_id, code) DO NOTHING;

COMMIT;
