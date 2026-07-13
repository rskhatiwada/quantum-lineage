# Quantum Lineage

**A genealogy of quantum information science — from the EPR paradox to topological quantum computation.**

Quantum Lineage is a lineage-tracked personal research library: roughly 1,000 papers in quantum information science, organized into eight historical Epochs, each defined by the mathematical object at the center of the field and the crisis that forced it into existence. Every paper is a node in a directed graph — its entry states precisely which prior formal structure it consumed and which later construction it enabled — rather than a standalone summary.

The founding document is the "Russell Blueprint," which defines the Epoch ontology, the per-paper entry template, and the three-tier Active Replication program (analytic derivation → numerical experiment → cluster-scale simulation) used to certify that a paper has actually been understood, not just read.

Built with [Hugo](https://gohugo.io/) and the [Hextra](https://github.com/imfing/hextra) theme, authored as plain Markdown so the `content/` directory doubles as an [Obsidian](https://obsidian.md/) vault.

## Site structure

| Section | Path | Description |
|---|---|---|
| Ontology | `content/ontology.md` | The eight-Epoch master table and the inevitability argument tying them together. |
| Framework | `content/framework.md` | The entry template, ID conventions, and the three Replication Tiers. |
| Epochs | `content/epochs/` | One landing page per Epoch (crisis, central object, why the math evolved). Only Epoch I is fully processed; Epochs II–VIII are stubs. |
| Library | `content/library/e{n}/` | One Markdown file per paper, front matter as the machine-readable graph node (`id`, `epoch`, `core`, `status`, `tier`, `edges_backward`, `edges_forward`, `tags`). |
| Lineage Graph | `content/graph.md` | An interactive, click-through DAG of every paper's edges, rendered client-side with Cytoscape.js from `static/graph.json`. |

Currently populated: **Epoch I** in full — 10 core papers, 14 supplemental papers, 43 lineage edges.

## Local development

Requires [Hugo Extended](https://gohugo.io/installation/) (≥ 0.146.0) and [Go](https://go.dev/) (theme is pulled in via Hugo Modules, not vendored).

```bash
hugo server
```

Visit `http://localhost:1313/quantum-lineage/`.

```bash
hugo --gc --minify   # production build → public/
```

## Adding or editing a paper

1. Create `content/library/e{n}/e{n}-{c|s}{nn}.md` following the front matter schema of an existing entry (see [`content/framework.md`](content/framework.md) for the full entry template).
2. Fill in `edges_backward` / `edges_forward` with the IDs of papers actually consumed or enabled — never fabricate a lineage edge.
3. Regenerate the lineage graph data:
   ```bash
   python3 scripts/build-graph.py
   ```
   This reads front matter across the library and rewrites `static/graph.json`. It is not required for `hugo server` to work day-to-day — only for the `/graph` page to reflect new edges.

## Deployment

Pushes to `main` trigger `.github/workflows/pages.yml`, which builds the site with Hugo and deploys to GitHub Pages. `baseURL` in `hugo.yaml` is the single place controlling the deployed URL.

## License

Content and configuration in this repository are personal research material. The Hextra theme is MIT-licensed by [imfing](https://github.com/imfing/hextra).
