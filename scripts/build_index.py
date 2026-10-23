"""Rebuild index.json from the front matter of skills/*/SKILL.md."""
import json, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
items = []
for md in sorted(root.glob("skills/*/SKILL.md")):
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{md}: no front matter")
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        v = v.strip()
        meta[k.strip()] = [x.strip() for x in v[1:-1].split(",") if x.strip()] if v.startswith("[") else v
    for key in ("name", "description", "sites", "topics", "verified"):
        if key not in meta:
            raise SystemExit(f"{md}: missing {key}")
    items.append({**{k: meta[k] for k in ("name", "description", "sites", "topics", "verified")},
                  "path": str(md.relative_to(root))})
(root / "index.json").write_text(json.dumps({"version": 1, "skills": items}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{len(items)} skill(s)")
