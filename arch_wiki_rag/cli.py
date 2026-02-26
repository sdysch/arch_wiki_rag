import logging
import click
from arch_wiki_rag.rag.pipeline import process_page
from arch_wiki_rag.rag.embeddings import query_index

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


@cli.command()
@click.argument("query")
@click.option("-k", "--top-k", default=5, help="Number of results to return")
def query(query, top_k):
    """Query the indexed ArchWiki pages."""
    results = query_index(query, k=top_k)

    for i, (text, score) in enumerate(results):
        click.echo(f"\n--- Result {i + 1} (score: {score:.4f}) ---")
        click.echo(text[:500] + "..." if len(text) > 500 else text)


if __name__ == "__main__":
    cli()
