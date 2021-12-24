import yaml
import os


def read_config():
    path = os.path.abspath(os.path.join(os.path.dirname("."), "config.yml"))
    with open(path, 'r') as f:
        config = f.read()
    if config is not None:
        c = yaml.load(config, yaml.Loader)
        return c
    else:
        raise RuntimeError