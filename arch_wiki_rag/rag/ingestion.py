from arch_wiki_rag.rag.fetch import fetch_and_save


def download_page(title: str) -> str:
    return fetch_and_save(title)
