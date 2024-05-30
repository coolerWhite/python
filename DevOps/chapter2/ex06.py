import yaml
from pprint import pprint

with open("file.yaml", "r") as open_file:
    yaml_file = yaml.safe_load(open_file)
    pprint(yaml_file)