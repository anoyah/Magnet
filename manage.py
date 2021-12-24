import click
from magnet.server.run import run
from magnet.core.config.read_config import read_config
from magnet.spider.duo33 import Duo33
from magnet.core.logging.logger import *
import logging

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--p", "-p", "port", help="Run port.")
def runserver(**kwargs):
    port = kwargs.get("port", None)
    run(port)


@cli.command()
def config():
    c = read_config()
    logger.info(c)


@cli.command()
def runspider():
    duo = Duo33()
    duo.main()


if __name__ == "__main__":
    cli()