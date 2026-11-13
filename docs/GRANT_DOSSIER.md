# SKILLSCONTINUA & NKÒ MÍ IGBO: MASTER TECHNICAL & GRANT DOSSIER
**Ecosystem Architecture, Automated Pipelines, and Scalable Educational Infrastructure**

---

## 1. Executive Summary
`skillscontinua` and `nkọ mị igbo` form a dual-platform digital ecosystem engineered to preserve indigenous knowledge graphs and deliver high-utility technical, vocational, and professional training (spanning 317+ technical skills and 22 calendrical domains). Designed for low-bandwidth environments (such as Abiapolis/Abia State technical frameworks), the platforms optimize server performance, minimize infrastructure costs via YouTube media offloading, and guarantee data integrity through automated CI/CD management tools.

---

## 2. System Architecture & Tech Stack
* **Framework:** Django 5.0.9 (Python 3.11.11)
* **Design Pattern:** "Convention-over-configuration" leveraging generic multi-tier subject views to eliminate boilerplate.
* **Database & Hosting:** PostgreSQL / SQLite dynamic environment toggling; deployed on PythonAnywhere.
* **Localization:** Multi-language schema support (`en`, `fr`, `es`, `pt`, `sw`, `ar`) built natively into model attributes.

---

## 3. Core Engineering & Management Innovations

### 3.1 Idempotent Ingestion Pipeline (`sync_curriculum`)
To ingest large-scale technical curricula without human error or database duplication, the platform utilizes a robust custom management command:
* **Multi-Encoding Fallback:** Automatically detects and decodes files stored in UTF-8, Latin-1, or CP1252.
* **Atomic Updates:** Executes `update_or_create` transactions across categories, courses, and lessons, ensuring safe iterative updates from JSON fixture datasets.

### 3.2 Automated Quality Assurance & Schema Compliance (`verify_courses`)
To maintain elite engineering standards and satisfy institutional reporting requirements, the system features a continuous database auditing command:
* **Health Metrics:** Evaluates metadata completeness, missing learning objectives, and orphaned records in real time.
* **Curriculum Health Score:** Computes a quantitative health rating, ensuring 100% schema compliance before public or donor demonstrations.

### 3.3 Enterprise Administrative Control (`admin.py`)
* Configured with inline relational editing, advanced multi-parameter indexing, and custom list filters to empower academic stakeholders and regional administrators to manage global cohorts securely.

---

## 4. Scalability & Social Impact Roadmap
* **Vocational Integration:** Direct alignment with regional market needs (Aba technical youths, market women, and tech entrepreneurs).
* **Cost Efficiency:** Zero-cost video hosting architecture utilizing embedded streaming references.
* **Funding Utilization:** Grants will directly accelerate server migration, multi-language expansion, and physical deployment nodes across partner institutions.