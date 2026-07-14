---
title: "Framework"
description: "The entry template, identifier conventions, and the three Replication Tiers that make the library a directed graph rather than a pile of summaries."
weight: 2
---

## How to Read This Library

Three principles govern everything in this library.

1. **Ideas have ancestries, not birthdays.** Every paper in this library is documented as a node in a directed acyclic graph. The edges are the content. A summary that cannot state precisely which prior formal structure a paper consumed, and which later formal structure it enabled, has not understood the paper.
2. **The mathematics evolves under pressure.** Formalism is never adopted for elegance alone. Hilbert spaces were forced by the failure of classical phase space; density operators were forced by the existence of subsystems; operator algebras of stabilizers were forced by the impossibility of cloning; modular tensor categories were forced by the existence of anyons. Each Epoch is defined by the crisis that forced its mathematics.
3. **Understanding is certified by replication.** Every core paper carries an Active Replication task: an analytic derivation, a numerical experiment, or a cluster-scale simulation. A paper is not "read" until its task is complete. The tasks are graded in three tiers (below) so that the library doubles as a training program in the computational methods of the field.

## Identifier and File Conventions

Every paper receives a permanent identifier `[E#-C##]` (core) or `[E#-S##]` (supplemental): Epoch number, then serial within the Epoch. Example: `E1-C04` is the fourth core paper of Epoch I. The identifier is the node name in the lineage graph; never rename it. One file per paper, named by identifier; one master index file per Epoch listing all nodes and edges (the edge list is what makes the library queryable: a plain two-column file `source → target` suffices and can be rendered with Graphviz or networkx at any time).

## Replication Tiers

- **Tier 1 (analytic).** A closed-form derivation reproduced by hand: a Hamiltonian diagonalization, an inequality proof, a bound. Deliverable: a short note in the entry.
- **Tier 2 (numerical).** A single-machine computation: a Python notebook that reconstructs a figure, verifies a bound numerically, or simulates a small instance. Deliverable: a script committed alongside the entry, with the reproduced figure.
- **Tier 3 (cluster-scale).** A parameter sweep or ensemble average requiring batch computation (HTCondor / OSPool): finite-size scaling, trajectory ensembles, phase-diagram scans. Deliverable: the worker script, submit file, and the collected data product. Tier 3 tasks are the bridge between the library and thesis-grade research practice.

## The Entry Template

The template below is reproduced verbatim in every entry. Fields are mandatory; "none" is an acceptable but deliberate answer.

```
ID: [E#-C## or E#-S##]
Citation: authors, title, journal, volume, page (year); arXiv/DOI.
Epoch: #.   Status: unread / task-pending / certified.

THE CRUX: one paragraph, mathematically precise, stating the exact
object constructed or theorem proved, with the key equation(s)
transcribed in the paper's own notation and, where the notation is
archaic, a translation into modern notation.

LINEAGE (BACKWARD): list of IDs (or external anchors for
pre-library works), each with one line stating precisely which formal
structure was consumed.

LINEAGE (FORWARD): list of IDs, each with one line stating
precisely which later construction this paper made possible. Include at
least one edge into your active research area when honest; never
fabricate one.

PREREQUISITE FORMALISM: the specific mathematics required to read
the paper without external help, stated as checkable items (e.g.,
"spectral theorem for self-adjoint operators on finite-dimensional
Hilbert spaces", not "linear algebra").

ACTIVE REPLICATION: the task, its tier, the acceptance criterion
(what output certifies success), and the estimated effort.

CONSENSUS SHIFT: two sentences: what the field believed before,
and what it believed after (with a realistic account of the delay).

NOTES AND CROSS-EXAMINATION: standing objections, errors later
found, modern hindsight.
```

Two disciplinary rules. First, backward edges must point to formal structures, not vibes: "uses the density operator of [E1-C01](e1-c01.md)" is an edge; "inspired by the Copenhagen spirit" is not. Second, forward edges are written in pencil: they are revised every time a later Epoch is processed, and the revision dates are kept. A lineage graph that never gets re-drawn is a decoration, not an instrument.

See also: the [Ontology](ontology.md) for the eight Epochs this template is applied across, and the [Lineage Graph](graph.md) for the resulting directed graph rendered interactively.
