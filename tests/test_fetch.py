import pytest
from arch_wiki_rag.rag.fetch import fetch_page, FetchError


def test_fetch_error_is_exception():
    assert issubclass(FetchError, Exception)


def test_fetch_error_message():
    err = FetchError("test error")
    assert str(err) == "test error"


def test_fetch_page_invalid_title_raises():
    with pytest.raises(FetchError):
        fetch_page("Nonexistent_Page_That_Does_Not_Exist_12345")
