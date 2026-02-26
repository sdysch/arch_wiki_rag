# ArchWiki RAG

_Disclaimer_ I am using this project to learn more about RAG, so it is not expected to be fully functional

**Retrieval-Augmented Generation (RAG) system for Arch Linux wiki articles**.  
This project demonstrates a production-style Python RAG pipeline for technical documentation. It includes:

- Section-aware ingestion of ArchWiki pages
- Chunking and embedding of text for semantic search
- FAISS-based retrieval for fast similarity queries
- LLM query generation using retrieved context
- Terminal-first CLI interface

---

## Installation

Requires Python ≥3.13 and `uv`:

```bash
uv sync
```

## Usage

### Ingest a page
```bash
arch_rag ingest "Systemd"
arch_rag ingest "Tmux"
arch_rag ingest "Installation"
```

### Query the RAG system
* Currently a dummy implementation
```bash
arch_rag query "How do I enable systemd-resolved?"
arch_rag query "how to install arch" -k 10
```
