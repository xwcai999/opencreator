import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
data = json.loads((root / "ecosystem.json").read_text(encoding="utf-8"))
assert data["schemaVersion"] == 1
assert data["name"] == "OpenCreator"
names = [item["name"] for item in data["projects"]]
assert len(names) == len(set(names))
assert "novel-studio-skill" in names
for item in data["projects"]:
    assert item["repository"].startswith("https://github.com/xwcai999/")
    assert item["status"] in {"preparing", "released", "archived"}
print(f"validated {len(names)} projects")

