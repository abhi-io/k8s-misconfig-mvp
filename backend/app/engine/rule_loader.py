import yaml
from pathlib import Path


def load_rules(rule_dir: str):
    rules = []

    for file in Path(rule_dir).glob("*.yaml"):
        with open(file) as f:
            rules.append(yaml.safe_load(f))

    return rules
