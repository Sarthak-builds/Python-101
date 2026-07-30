# Python-101 Curriculum Plan

Full roadmap from zero to production-grade Python, focused on backend
infrastructure and applied AI. Work through modules in order — each topic
gets `notes.md` (concept), `example.py` (worked demo), `practice.py`
(exercise). Attempt `practice.py` before checking `solutions/`.

Check items off as we complete them.

## Module 00 — Setup & Environment
- [ ] Installing Python & version management (pyenv)
- [ ] Virtual environments (venv)
- [ ] Package management: pip, requirements.txt, pyproject.toml
- [ ] Modern tooling: uv / ruff / black
- [ ] Running code: REPL, scripts, `python -m`

## Module 01 — Foundations
- [x] Variables, naming, dynamic typing
- [ ] Numbers & arithmetic operators
- [ ] Strings, string methods, f-strings
- [ ] Booleans & truthiness
- [ ] Type conversion/casting
- [ ] Basic I/O (input/print)
- [ ] Comments & docstrings

## Module 02 — Control Flow & Functions
- [ ] if/elif/else, conditional expressions
- [ ] while loops
- [ ] for loops & range
- [ ] break/continue/else on loops
- [ ] Functions: args, kwargs, defaults, *args/**kwargs
- [ ] Scope (LEGB) & closures
- [ ] Lambda functions
- [ ] Recursion

## Module 03 — Data Structures
- [ ] Lists (methods, slicing, comprehensions)
- [ ] Tuples & immutability
- [ ] Dictionaries (methods, comprehensions)
- [ ] Sets & set operations
- [ ] Nested data structures
- [ ] Choosing the right structure & time complexity basics

## Module 04 — Object-Oriented Programming
- [ ] Classes, objects, `__init__`
- [ ] Instance vs. class attributes/methods
- [ ] Inheritance, MRO, `super()`
- [ ] Polymorphism & duck typing
- [ ] Magic/dunder methods (`__str__`, `__repr__`, `__eq__`, `__len__`, ...)
- [ ] Properties & descriptors
- [ ] Composition vs. inheritance
- [ ] Abstract base classes (`abc`)
- [ ] Dataclasses

## Module 05 — Modules & Packaging
- [ ] Modules & imports, `__name__ == "__main__"`
- [ ] Packages & `__init__.py`
- [ ] Relative vs. absolute imports
- [ ] Building a distributable package (pyproject.toml)
- [ ] Publishing to PyPI (test index)
- [ ] Dependency locking (uv/poetry)

## Module 06 — Errors & Debugging
- [ ] Exceptions: try/except/else/finally
- [ ] Custom exceptions
- [ ] Raising, re-raising, exception chaining
- [ ] Debugging with `pdb` / `breakpoint()`
- [ ] Assertions

## Module 07 — Files & Serialization
- [ ] File I/O & context managers (`with`)
- [ ] `pathlib`
- [ ] CSV handling
- [ ] JSON serialization
- [ ] Pickle (and its dangers)
- [ ] YAML/TOML configs

## Module 08 — Testing
- [ ] `unittest` basics
- [ ] pytest fundamentals, fixtures, parametrize
- [ ] Mocking (`unittest.mock`)
- [ ] Test coverage
- [ ] TDD workflow
- [ ] Property-based testing (hypothesis) intro

## Module 09 — Concurrency & Async
- [ ] Threads & the GIL
- [ ] Multiprocessing
- [ ] asyncio fundamentals (event loop, coroutines, tasks)
- [ ] async/await patterns, `asyncio.gather`
- [ ] Queues & producer-consumer patterns
- [ ] Threads vs. processes vs. async — when to use which

## Module 10 — Networking & HTTP
- [ ] Sockets basics
- [ ] HTTP fundamentals & the `requests` library
- [ ] Building an HTTP client
- [ ] Web scraping (requests + BeautifulSoup)
- [ ] WebSockets basics

## Module 11 — Databases
- [ ] SQL recap
- [ ] `sqlite3` stdlib
- [ ] SQLAlchemy Core & ORM
- [ ] Migrations with Alembic
- [ ] NoSQL intro (Redis, MongoDB)
- [ ] Connection pooling

## Module 12 — Web Backend (FastAPI)
- [ ] HTTP APIs & REST fundamentals
- [ ] FastAPI basics: routes, path/query params, request bodies
- [ ] Pydantic models & validation
- [ ] Dependency injection
- [ ] Async endpoints & background tasks
- [ ] Authentication (JWT, OAuth2)
- [ ] Middleware & CORS
- [ ] Building a full CRUD API

## Module 13 — Infra & DevOps
- [ ] Docker basics: images, containers, Dockerfile for Python
- [ ] Docker Compose (app + database)
- [ ] CI/CD basics (GitHub Actions)
- [ ] Config/secrets management & the 12-factor app
- [ ] Cloud deployment basics
- [ ] Infrastructure as Code intro (Terraform)
- [ ] Kubernetes concepts overview

## Module 14 — Observability
- [ ] Logging deep dive (handlers, formatters, structured logs)
- [ ] Metrics (Prometheus client basics)
- [ ] Tracing concepts (OpenTelemetry intro)
- [ ] Health checks & readiness probes
- [ ] Debugging production issues

## Module 15 — Applied AI
- [ ] LLM APIs (Anthropic SDK basics, prompts, streaming)
- [ ] Structured output & tool/function calling
- [ ] Embeddings & similarity search
- [ ] Vector databases (Chroma/FAISS/pgvector)
- [ ] Retrieval-Augmented Generation (RAG) pipeline
- [ ] Building simple agents & tool-use loops
- [ ] Prompt engineering & evaluation basics
- [ ] Cost, latency, and caching considerations

## Module 16 — Production Patterns
- [ ] Configuration & secrets management
- [ ] Multi-stage Docker builds for production
- [ ] Performance profiling & optimization
- [ ] Security basics (input validation, secrets, dependency scanning)
- [ ] Rate limiting & caching strategies
- [ ] Scaling patterns (horizontal scaling, load balancing concepts)
- [ ] Capstone: production-grade backend service with an AI feature
