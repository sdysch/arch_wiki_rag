import pytest
from click.testing import CliRunner
from arch_wiki_rag.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "ArchWiki RAG CLI" in result.output


def test_cli_verbose_flag(runner):
    result = runner.invoke(cli, ["--verbose", "--help"])
    assert result.exit_code == 0
    assert "debug logging" in result.output


def test_ingest_command_exists(runner):
    result = runner.invoke(cli, ["ingest", "--help"])
    assert result.exit_code == 0
    assert "Ingest a page" in result.output


def test_query_command_exists(runner):
    result = runner.invoke(cli, ["query", "--help"])
    assert result.exit_code == 0
    assert "Query the indexed" in result.output


def test_query_top_k_option(runner):
    result = runner.invoke(cli, ["query", "--help"])
    assert result.exit_code == 0
    assert "-k" in result.output or "--top-k" in result.output
