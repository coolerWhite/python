import json
from pprint import pprint
with open("file.json", "r") as open_file:
    policy = json.load(open_file)

policy["glossary"]["title"] = "Changed"

print(policy)