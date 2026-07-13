#!/usr/bin/env python3
"""Generate static/graph.json (nodes + edges) from content/library/**/*.md front matter.

Run manually or pre-commit: `python3 scripts/build-graph.py`
Not required for `hugo server` to work — static/graph.json is committed
alongside the content it is derived from, and only needs regenerating when
paper front matter (ids, edges_backward, edges_forward) changes.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "content" / "library"
OUT = ROOT / "static" / "graph.json"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s*-\s+(.*)$")
FLOW_ITEM_RE = re.compile(r'"[^"]*"|[^,]+')


def parse_scalar(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1].replace('\\"', '"')
    if value == "true":
        return True
    if value == "false":
        return False
    if value in ("null", ""):
        return None
    try:
        return int(value)
    except ValueError:
        return value


def parse_flow_list(value):
    inner = value.strip()
    if inner.startswith("[") and inner.endswith("]"):
        inner = inner[1:-1].strip()
    if not inner:
        return []
    return [parse_scalar(part.strip().rstrip(",")) for part in FLOW_ITEM_RE.findall(inner)]


def parse_frontmatter(text):
    fields = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = KEY_RE.match(line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2)
        if rest.strip().startswith("["):
            fields[key] = parse_flow_list(rest)
            i += 1
        elif rest.strip() == "":
            items, j = [], i + 1
            while j < len(lines) and LIST_ITEM_RE.match(lines[j]):
                items.append(parse_scalar(LIST_ITEM_RE.match(lines[j]).group(1)))
                j += 1
            fields[key] = items or None
            i = j if items else i + 1
        else:
            fields[key] = parse_scalar(rest)
            i += 1
    return fields


def main():
    node_ids = set()
    parsed = []

    for path in sorted(LIBRARY.glob("e*/e*-*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m:
            print(f"warning: no front matter in {path}", file=sys.stderr)
            continue
        fm = parse_frontmatter(m.group(1))
        if "id" not in fm:
            print(f"warning: no id field in {path}", file=sys.stderr)
            continue
        parsed.append(fm)
        node_ids.add(fm["id"])

    nodes, edges = [], set()
    for fm in parsed:
        node_id = fm["id"]
        nodes.append({
            "id": node_id,
            "label": fm.get("label") or fm.get("title") or node_id,
            "epoch": fm.get("epoch"),
            "core": bool(fm.get("core")),
            "status": fm.get("status"),
            "slug": node_id.lower(),
        })
        for backward in fm.get("edges_backward") or []:
            if backward in node_ids:
                edges.add((backward, node_id))
        for forward in fm.get("edges_forward") or []:
            if forward in node_ids:
                edges.add((node_id, forward))

    graph = {
        "nodes": nodes,
        "edges": [{"source": s, "target": t} for s, t in sorted(edges)],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(nodes)} nodes and {len(graph['edges'])} edges to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
