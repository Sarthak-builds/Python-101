# Python-101

A from-scratch-to-production Python curriculum, focused on backend
infrastructure and applied AI.

## How this repo is organized

```
docs/
  PLAN.md          Full syllabus as a checklist — the source of truth for progress.
  README.md        This file.
modules/
  NN-topic-name/
    <lesson>/
      notes.md       Concept explanation for one lesson.
      example.py     Worked, runnable demonstration.
      practice.py    Exercise with TODOs — attempt this yourself first.
solutions/
  NN-topic-name/
    <lesson>/
      practice.py    Solved version of the matching practice file.
```

Modules are numbered in the order we work through them (`00-setup` through
`16-production-patterns`). Lesson subfolders inside each module are created
as we reach them, not all up front.

## Workflow for each lesson

1. Read `notes.md` for the concept.
2. Run and read through `example.py`.
3. Do `practice.py` yourself — don't peek at `solutions/` first.
4. Check your attempt against `solutions/<same path>/practice.py`.
5. Check the topic off in `docs/PLAN.md`.

## Setup

- Python version and environment tooling are covered in `modules/00-setup/`.
- Each module that needs extra packages includes its own
  `requirements.txt` (or notes on installing what's needed) rather than one
  global dependency file, so the repo stays easy to work through
  incrementally.
