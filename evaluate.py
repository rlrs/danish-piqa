import json
from pathlib import Path

with Path("piqa-dan.json").open() as f:
    data = json.load(f)

print(len(data))
