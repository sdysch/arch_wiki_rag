import logging
import click
from arch_wiki_rag.rag.pipeline import process_page

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Enable debug logging")
def cli(verbose):
    """ArchWiki RAG CLI"""
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)


@cli.command()
@click.argument("title")
def ingest(title):
    """Ingest a page from ArchWiki by TITLE."""
    process_page(title)
    click.echo(f"Ingested: {title}")


if __name__ == "__main__":
    cli()
