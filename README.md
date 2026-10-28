# Python-101

Learning playground for LangGraph / LangChain / LangSmith workflows with Gemini and OpenAI models.

## Structure

- `*_workflow.ipynb`, `batsman.ipynb`, `score.ipynb` — LangGraph state-machine notebooks (BMI, chat, tools, parallel stats, UPSC essay evaluation, etc.)
- `chatbot/` — LangGraph chatbot backend + Streamlit frontend, persisted to SQLite
- `mcp/` — FastMCP calculator server
- `langsmith/langsmith-masterclass/` — cloned course repo (local changes are kept, not pushed; its `.env` holds providers keys and must stay out of version control)
- `docker-compose.yml` — Postgres 16 on host port 5442 for the checkpoint notebooks

## Setup

1. Create `.env` with `GOOGLE_API_KEY` (and/or `OPENAI_API_KEY`) — never commit it
2. `docker compose up -d postgres` when running `shortTermMemory.ipynb`
3. Use the bundled `venv/` python (`venv\Scripts\python.exe`) for Jupyter
