-- 007_students.sql (SkillsContinuum)
-- Students are domain entities. Authentication remains in app_users.

BEGIN;

CREATE TABLE IF NOT EXISTS students (
  id            BIGSERIAL PRIMARY KEY,
  app_user_id   BIGINT NOT NULL UNIQUE REFERENCES app_users(id) ON DELETE CASCADE,
  student_code  TEXT UNIQUE,
  status        TEXT NOT NULL DEFAULT 'active', -- active|suspended|archived
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT students_status_chk CHECK (status IN ('active','suspended','archived'))
);

CREATE INDEX IF NOT EXISTS idx_students_app_user_id ON students(app_user_id);
CREATE INDEX IF NOT EXISTS idx_students_status ON students(status);

-- Optional profile layer (keeps student table slim; expandable without churn)
CREATE TABLE IF NOT EXISTS student_profiles (
  student_id      BIGINT PRIMARY KEY REFERENCES students(id) ON DELETE CASCADE,
  first_name      TEXT,
  last_name       TEXT,
  other_names     TEXT,
  gender          TEXT,
  date_of_birth   DATE,
  phone           TEXT,
  country         TEXT,
  region          TEXT,
  city            TEXT,
  address         TEXT,
  school_name     TEXT,
  school_level    TEXT,   -- e.g., primary|jss|sss|tertiary (free text for now)
  guardian_name   TEXT,
  guardian_phone  TEXT,
  meta            JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_student_profiles_name ON student_profiles(last_name, first_name);
CREATE INDEX IF NOT EXISTS idx_student_profiles_meta_gin ON student_profiles USING GIN (meta);

COMMIT;
