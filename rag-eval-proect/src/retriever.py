from pathlib import Path
import re

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "chroma_store"

EMBED_MODEL = "all-MiniLM-L6-v2"
TIMESTAMP_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*.*$")


class LocalEmbeddings(Embeddings):
    def __init__(self, model_name: str = EMBED_MODEL):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts, normalize_embeddings=True).tolist()

    def embed_query(self, text):
        return self.model.encode([text], normalize_embeddings=True)[0].tolist()


def parse_vtt(path: Path) -> str:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    kept = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        if TIMESTAMP_RE.match(stripped):
            continue
        if stripped.isdigit():
            continue
        kept.append(stripped)
    return " ".join(kept)


def load_transcripts() -> list[Document]:
    docs = []
    for path in sorted(DATA_DIR.glob("*.vtt")):
        text = parse_vtt(path)
        if text:
            docs.append(
                Document(
                    page_content=text,
                    metadata={"session": path.stem, "source": str(path)},
                )
            )
    return docs


def load_store():
    embeddings = LocalEmbeddings(EMBED_MODEL)
    if DB_DIR.exists():
        db = Chroma(persist_directory=str(DB_DIR), embedding_function=embeddings)
        return db
    docs = load_transcripts()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    db = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory=str(DB_DIR),
        collection_name="transcripts",
    )
    return db


def build_retriever(k: int = 4):
    db = load_store()
    return db.as_retriever(search_kwargs={"k": k})


if __name__ == "__main__":
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"No data dir found at {DATA_DIR}")

    retriever = build_retriever()
    query = "what is retrieval augmented generation"
    results = retriever.invoke(query)
    for doc in results:
        print(doc.metadata)
        print(doc.page_content)
        print("-" * 60)
