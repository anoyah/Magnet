import logging


def logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        # format=
        # "%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",
        # datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logger
