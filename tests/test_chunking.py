from unittest.mock import patch
from arch_wiki_rag.rag.chunking import chunk_page


def test_chunk_page_empty():
    from arch_wiki_rag.rag.fetch import FetchError

    with patch("arch_wiki_rag.rag.chunking.fetch_page") as mock_fetch:
        mock_fetch.side_effect = FetchError("test")
        result = chunk_page("test")
        assert result == []


def test_chunk_page_single_paragraph():
    with patch("arch_wiki_rag.rag.chunking.fetch_page") as mock_fetch:
        mock_fetch.return_value = "This is a short paragraph."
        result = chunk_page("test")
        assert len(result) == 1
        assert result[0] == "This is a short paragraph."


def test_chunk_page_multiple_paragraphs():
    with patch("arch_wiki_rag.rag.chunking.fetch_page") as mock_fetch:
        mock_fetch.return_value = (
            "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        )
        result = chunk_page("test", max_chunk_size=20)
        assert len(result) == 3


def test_chunk_page_respects_max_size():
    with patch("arch_wiki_rag.rag.chunking.fetch_page") as mock_fetch:
        mock_fetch.return_value = "Short.\n\nSecond short paragraph."
        result = chunk_page("test", max_chunk_size=50)
        assert all(len(chunk) <= 50 for chunk in result)


def test_chunk_page_handles_unicode():
    with patch("arch_wiki_rag.rag.chunking.fetch_page") as mock_fetch:
        mock_fetch.return_value = "Hello 你好 🌍"
        result = chunk_page("test")
        assert len(result) == 1
        assert "你好" in result[0]
