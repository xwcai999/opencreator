import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
data = json.loads((root / "ecosystem.json").read_text(encoding="utf-8"))
assert data["schemaVersion"] == 1
assert data["name"] == "OpenCreator"
names = [item["name"] for item in data["projects"]]
assert len(names) == len(set(names))
assert "OpenCreator Novel" in names
required_projects = {
    "OpenCreator Novel": {"version": "0.4.0", "status": "released"},
    "opencreator-music": {"version": "0.1.1", "status": "released"},
    "opencreator-dashboard": {"version": "0.3.0", "status": "released"},
    "OpenCreator Publishers": {
        "repository": "https://github.com/xwcai999/opencreator-publishers",
        "kind": "publisher-suite",
        "version": "0.1.0",
        "status": "released",
    },
}
projects_by_name = {item["name"]: item for item in data["projects"]}
for name, expected in required_projects.items():
    assert name in projects_by_name, f"missing required project: {name}"
    for key, value in expected.items():
        assert projects_by_name[name].get(key) == value, (
            f"{name} {key} must be {value!r}"
        )
for item in data["projects"]:
    assert {"name", "repository", "kind", "status", "version"} <= item.keys()
    assert item["repository"].startswith("https://github.com/xwcai999/")
    assert item["status"] in {"preparing", "released", "archived"}
print(f"validated {len(names)} projects")
