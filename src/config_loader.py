import yaml
from types import SimpleNamespace

#load data into config
def load_config(path="config/config.yaml") -> SimpleNamespace:
    with open(path, "r") as f:
        config = SimpleNamespace(**yaml.safe_load(f))
        return config