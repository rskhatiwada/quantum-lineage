---
title: "Lineage Graph"
description: "An interactive, click-through map of every paper's backward and forward edges."
weight: 5
---

Nodes are colored by Epoch; core papers render as larger circles, supplemental papers as smaller rounded squares. Click any node to open its entry. Drag to pan, scroll to zoom.

{{< lineage-graph >}}

This graph is generated from the same front matter as the [Library](/library) — regenerate `static/graph.json` with `python3 scripts/build-graph.py` after editing any paper's `edges_backward` / `edges_forward`. If JavaScript fails to load, the same edges are readable directly on each paper's entry, or as prose in the [Epoch I](/epochs/epoch-1) essay.
