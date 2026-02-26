import click
from arch_wiki_rag.rag.pipeline import process_page

@click.group()
def cli():
    """ArchWiki RAG CLI"""
    pass

@cli.command()
@click.argument('title')
def ingest(title):
    """Ingest a page from ArchWiki by TITLE."""
    process_page(title)
    click.echo(f"Ingested: {title}")

if __name__ == "__main__":
    cli()
