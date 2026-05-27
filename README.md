# Consciousness Circle Metadata Specification

A metadata specification for annotating the question, friction, surface facts, deep context, relational dynamics, sovereignty control, trace governance, and allocation-readiness of a content item in AI-mediated knowledge ecosystems.

This specification is designed for environments where human-created knowledge is increasingly read, retrieved, summarized, referenced, transformed, and recomposed by AI systems.

It provides a structured way to describe not only what a content item says, but also the question, tension, semantic depth, interpretive movement, and creator-defined meaning boundaries behind it.

---

## Current Status

```text
Current documentation release: v0.1.3
Validated draft specification: v0.2.0
Validation status: Passing
Status: Draft
```

The v0.1.x series defines the initial metadata schema and documentation layer.

The v0.2.0 draft defines a validated Question OS object model with:

- a draft reference specification
- a JSON Schema
- validated YAML examples
- CI-based example validation

The v0.2.0 materials introduce:

- friction taxonomy
- recursive circle structure
- proto-friction handling
- silence nodes
- visibility scope
- sovereignty control
- RAG usage policy
- validated v0.2 examples

Current validation target:

```text
schemas/consciousness-circle-metadata-v0.2.schema.json
```

Current validated examples:

```text
examples/minimal-circle-v0.2.example.yaml
examples/extended-circle-v0.2.example.yaml
examples/proto-friction-v0.2.example.yaml
examples/silence-node-v0.2.example.yaml
```

Validation workflow:

```text
.github/workflows/validate-v0.2-examples.yml
```

Validation script:

```text
scripts/validate-v0.2-examples.py
```

---

## Purpose

The Consciousness Circle Metadata Specification defines a metadata layer for content such as articles, essays, notes, repository documents, book sections, social posts, specifications, and other knowledge artifacts.

Its purpose is to support:

- richer AI retrieval
- semantic traceability
- question-centered indexing
- surface/deep layer annotation
- creator-controlled deep metadata
- consent-aware RAG workflows
- trace governance
- sovereignty control
- allocation-readiness review
- privacy-preserving semantic metadata
- future Royalty OS and Trace Protocol workflows

This specification does not claim to store consciousness itself.

It annotates the structure behind content: the question that generated it, the friction that shaped it, the surface facts it refers to, and the deeper interpretive context that gives it meaning.

---

## Core Concept

Traditional metadata often describes content through simple tags:

```text
title
author
date
category
keywords
```

This specification adds a deeper structure:

```text
center question
initial friction
proto-friction
surface facts
deep context
layer connections
rotation dynamics
visibility scope
sovereignty control
trace governance
royalty-readiness signals
```

The goal is not to reduce living thought to dead tags.

The goal is to make the structure of meaning traceable while preserving creator agency, consent, privacy, and human review.

---

## Consciousness Circle

The specification models content as a circular semantic structure:

```text
center
↓
surface layer
↓
deep layer
↓
connections
↓
rotation dynamics
↓
sovereignty control
```

### Center

The center is the generative core of the content.

It contains:

- the core question
- the initial friction
- optional proto-friction
- optional bodily or affective signal
- notes about the content’s semantic epicenter

### Surface Layer

The surface layer contains:

- factual statements
- source references
- certainty levels
- surface-level summary

This is the layer most compatible with existing RAG systems.

### Deep Layer

The deep layer contains:

- context
- affective tags
- interpretive summary
- intensity
- personal resolution
- visibility controls
- private or protected meaning boundaries

This is the layer that existing search and RAG systems often fail to capture.

### Connections

Connections describe relationships between the center, surface, and deep layers.

Examples:

```text
tension
resonance
transformation
contradiction
clarification
amplification
suppression
contextualization
```

### Rotation Dynamics

Rotation dynamics describe how the content moves.

For example:

```text
from discomfort to question
from fact to interpretation
from criticism to system design
from tension to traceable structure
```

### Sovereignty Control

Sovereignty control defines how creator-declared meaning structures may be accessed, interpreted, summarized, transformed, or protected by AI systems.

It helps prevent creator sovereignty from becoming either:

```text
too weak = decorative metadata
too rigid = a cage
```

The intended model is:

```text
creator sovereignty as a living membrane
```

---

## v0.2 Design Direction

The v0.2.0 draft expands the specification from a minimal meaning record into a structured Question OS layer.

It introduces:

- friction taxonomy
- recursive circle structure
- proto-friction handling
- silence nodes
- visibility scope
- sovereignty control
- RAG usage policy
- formal validation through JSON Schema
- validated v0.2 examples

Conceptually:

```text
v0.1.x
= initial Consciousness Circle metadata

v0.2.0 draft
= validated Question OS object model

v0.3 and beyond
= runtime control, audit, RAG policy enforcement, trace integration, and review systems
```

The v0.2 reference specification is available at:

```text
spec/consciousness-circle-metadata-specification-v0.2.yaml
```

The v0.2 JSON Schema is available at:

```text
schemas/consciousness-circle-metadata-v0.2.schema.json
```

The v0.2 examples are validated by GitHub Actions.

---

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
│
├── spec/
│   └── consciousness-circle-metadata-specification-v0.2.yaml
│
├── schemas/
│   ├── consciousness-circle-metadata.schema.json
│   └── consciousness-circle-metadata-v0.2.schema.json
│
├── examples/
│   ├── note-article-consciousness-circle.sample.json
│   ├── minimal-circle-v0.2.example.yaml
│   ├── extended-circle-v0.2.example.yaml
│   ├── proto-friction-v0.2.example.yaml
│   └── silence-node-v0.2.example.yaml
│
├── scripts/
│   └── validate-v0.2-examples.py
│
├── .github/
│   └── workflows/
│       └── validate-v0.2-examples.yml
│
└── docs/
    ├── field-definitions.md
    ├── privacy-consent-and-human-review.md
    ├── relationship-to-trace-protocol.md
    ├── relationship-to-royalty-os.md
    ├── rag-integration-notes.md
    ├── sovereignty-control-model.md
    ├── friction-taxonomy.md
    ├── circle-structure-model.md
    └── proto-friction-layer.md
```

### Directory Overview

| Path | Description |
|---|---|
| `spec/` | Reference specifications and draft specification files, including the v0.2 Question OS object model. |
| `schemas/` | JSON Schema definitions for validating Consciousness Circle metadata objects. |
| `examples/` | Example metadata objects showing how the specification may be used, including v0.2 circle, proto-friction, and silence-node examples. |
| `scripts/` | Validation scripts for local and CI-based checks. |
| `.github/workflows/` | GitHub Actions workflows for validating schemas and examples. |
| `docs/` | Design notes and relationship documents explaining how this specification connects to trace systems, RAG systems, creator sovereignty, friction taxonomy, circle structure, and proto-friction handling. |

---

## Key Files

| Path | Description |
|---|---|
| `README.md` | Overview of the specification, core concepts, usage notes, validation status, and repository structure. |
| `LICENSE` | License for the specification, schema, documentation, and associated materials. |
| `CITATION.cff` | Citation metadata for referencing this specification. |
| `CHANGELOG.md` | Version history and notable changes. |
| `schemas/consciousness-circle-metadata.schema.json` | Original v0.1-style JSON Schema definition for Consciousness Circle metadata. |
| `schemas/consciousness-circle-metadata-v0.2.schema.json` | Draft v0.2 JSON Schema for validating the proposed Question OS object model. |
| `spec/consciousness-circle-metadata-specification-v0.2.yaml` | Draft v0.2 reference specification, including circle structure, friction taxonomy, proto-friction, visibility scope, sovereignty control, RAG usage policy, and conformance profiles. |
| `examples/note-article-consciousness-circle.sample.json` | v0.1-style example metadata object for a note-style article. |
| `examples/minimal-circle-v0.2.example.yaml` | Minimal v0.2-compatible circle profile. |
| `examples/extended-circle-v0.2.example.yaml` | Extended v0.2 circle profile with proto-friction, sub-circles, temporal lineage, and sovereignty control. |
| `examples/proto-friction-v0.2.example.yaml` | Focused example for pre-question pressure, vibration logs, shadow friction, and proto-friction controls. |
| `examples/silence-node-v0.2.example.yaml` | Focused example showing how creator-defined silence may be declared as a boundary that AI systems should not infer from. |
| `scripts/validate-v0.2-examples.py` | Python validation script for v0.2 schema, v0.2 reference spec parsing, and v0.2 example validation. |
| `.github/workflows/validate-v0.2-examples.yml` | GitHub Actions workflow for validating the v0.2 schema and examples. |
| `docs/field-definitions.md` | Detailed explanation of fields, allowed values, score interpretation, and usage notes. |
| `docs/privacy-consent-and-human-review.md` | Privacy, consent, visibility control, human review, RAG safeguards, and allocation-readiness safeguards. |
| `docs/friction-taxonomy.md` | Initial taxonomy for `initial_friction`, including bodily friction, daily-life friction, social friction, cognitive dissonance, ethical conflict, and raw unresolved friction. |
| `docs/circle-structure-model.md` | Model of the Consciousness Circle as a layered and recursive structure connecting friction, questions, meaning boundaries, visibility scope, and sovereignty controls. |
| `docs/proto-friction-layer.md` | Pre-question layer for proto-friction, shadow friction, vibration logs, and silence nodes. |
| `docs/sovereignty-control-model.md` | Control layer for creator sovereignty, including access boundaries, temporal lineage, friction encapsulation, and semantic brake concepts. |
| `docs/relationship-to-trace-protocol.md` | Explains how Consciousness Circle Metadata relates to Trace Protocol and semantic trace workflows. |
| `docs/relationship-to-royalty-os.md` | Explains how Consciousness Circle Metadata may support Royalty OS review without becoming an automatic allocation engine. |
| `docs/rag-integration-notes.md` | Explains how the metadata may be integrated into RAG systems for meaning-aware retrieval with consent controls. |

---

## Start Here

Recommended reading order:

1. `README.md`  
   Start with the overview, core concept, repository structure, validation status, and intended use cases.

2. `schemas/consciousness-circle-metadata.schema.json`  
   Review the original v0.1-style JSON Schema definition for Consciousness Circle metadata.

3. `examples/note-article-consciousness-circle.sample.json`  
   See how the v0.1-style schema can be applied to a note-style article.

4. `docs/field-definitions.md`  
   Read the detailed field definitions, allowed values, score interpretation, and RAG / Royalty OS usage notes.

5. `docs/privacy-consent-and-human-review.md`  
   Review privacy, consent, visibility control, human final edit, AI-inferred metadata handling, and anti-gaming safeguards.

6. `docs/friction-taxonomy.md`  
   Read the initial friction taxonomy. This document explains how `initial_friction` may be classified without forcing creators to over-disclose private origin material.

7. `docs/circle-structure-model.md`  
   Review the circle structure model. This document explains how friction, questions, meaning boundaries, visibility scope, and sovereignty controls form a layered Consciousness Circle.

8. `docs/proto-friction-layer.md`  
   Read the proto-friction layer design note. This document explains how pre-verbal friction, silence, shadow friction, and early meaning pressure may be preserved before they become structured questions.

9. `docs/sovereignty-control-model.md`  
   Read the control-layer design note. This document explains how creator sovereignty can be protected without turning the metadata structure into a rigid cage.

10. `spec/consciousness-circle-metadata-specification-v0.2.yaml`  
    Review the v0.2 draft reference specification. This file translates the v0.2 design path into proposed fields, controlled vocabularies, validation rules, conformance profiles, and example structures.

11. `schemas/consciousness-circle-metadata-v0.2.schema.json`  
    Review the v0.2 JSON Schema used to validate the v0.2 YAML examples.

12. `examples/minimal-circle-v0.2.example.yaml`  
    Review a minimal v0.2 circle example with core question, initial friction, visibility scope, sovereignty control, trace governance, and RAG policy.

13. `examples/extended-circle-v0.2.example.yaml`  
    Review an extended v0.2 example including proto-friction, sub-circles, temporal relationship, circle layers, meaning boundaries, and royalty-readiness notes.

14. `examples/proto-friction-v0.2.example.yaml`  
    Review a focused example for pre-question pressure, vibration logs, shadow friction, and protected proto-friction.

15. `examples/silence-node-v0.2.example.yaml`  
    Review a focused example showing how creator-defined silence can be treated as a boundary rather than missing data.

16. `scripts/validate-v0.2-examples.py`  
    Review or run the local validation script for the v0.2 schema and examples.

17. `.github/workflows/validate-v0.2-examples.yml`  
    Review the GitHub Actions workflow for v0.2 validation.

18. `docs/relationship-to-trace-protocol.md`  
    Understand how Consciousness Circle Metadata acts as a semantic pre-trace layer for Trace Protocol workflows.

19. `docs/relationship-to-royalty-os.md`  
    Understand how the metadata may support Royalty OS and Allocation Readiness without directly triggering royalties.

20. `docs/rag-integration-notes.md`  
    Review how RAG systems may use the metadata for question-centered, meaning-aware retrieval while respecting consent and visibility controls.

21. `CHANGELOG.md`  
    Check the version history and notable changes for this specification.

22. `CITATION.cff`  
    Use this file when citing or referencing the specification in papers, repositories, articles, or derivative work.

23. `LICENSE`  
    Review the license terms before reuse, modification, redistribution, or integration.

---

## Key Documents

| Document | Role |
|---|---|
| `schemas/consciousness-circle-metadata.schema.json` | Provides the original v0.1-style machine-readable validation layer for Consciousness Circle metadata objects. |
| `schemas/consciousness-circle-metadata-v0.2.schema.json` | Provides the v0.2 JSON Schema for validating the proposed Question OS object model. |
| `spec/consciousness-circle-metadata-specification-v0.2.yaml` | Defines the proposed v0.2 reference specification, including circle structure, friction taxonomy, proto-friction, visibility scope, sovereignty control, RAG usage policy, and conformance profiles. |
| `examples/note-article-consciousness-circle.sample.json` | Demonstrates a v0.1-style valid Consciousness Circle metadata example for a note-style article. |
| `examples/minimal-circle-v0.2.example.yaml` | Demonstrates a minimal v0.2-compatible circle profile. |
| `examples/extended-circle-v0.2.example.yaml` | Demonstrates an extended v0.2 circle profile with proto-friction, sub-circles, temporal lineage, and sovereignty control. |
| `examples/proto-friction-v0.2.example.yaml` | Demonstrates how pre-question pressure, vibration logs, shadow friction, and proto-friction controls may be represented. |
| `examples/silence-node-v0.2.example.yaml` | Demonstrates how creator-defined silence may be declared as a boundary that AI systems should not infer from. |
| `scripts/validate-v0.2-examples.py` | Validates the v0.2 JSON Schema, parses the v0.2 reference specification, and validates v0.2 examples. |
| `.github/workflows/validate-v0.2-examples.yml` | Runs v0.2 schema and example validation on GitHub Actions. |
| `docs/field-definitions.md` | Defines fields, allowed values, scoring notes, and implementation guidance. |
| `docs/privacy-consent-and-human-review.md` | Defines privacy, consent, visibility, human review, and safeguard principles. |
| `docs/friction-taxonomy.md` | Defines the v0.2 design path for classifying initial friction without exposing private origin material. |
| `docs/circle-structure-model.md` | Defines the v0.2 design path for modeling Consciousness Circle metadata as a layered, recursive meaning structure. |
| `docs/proto-friction-layer.md` | Defines the v0.2 design path for recording pre-question pressure, shadow friction, vibration logs, and silence nodes. |
| `docs/sovereignty-control-model.md` | Defines the control layer for creator sovereignty, including access boundaries, temporal lineage, friction encapsulation, and semantic brake concepts. |
| `docs/relationship-to-trace-protocol.md` | Explains how Consciousness Circle Metadata relates to trace records, origin tracking, and provenance systems. |
| `docs/relationship-to-royalty-os.md` | Explains how declared meaning structures may connect to royalty, allocation, and creator value-circulation models. |
| `docs/rag-integration-notes.md` | Provides notes on how AI retrieval systems may consume or respect the metadata. |

---

## Schema

The original v0.1-style machine-readable schema is located at:

```text
schemas/consciousness-circle-metadata.schema.json
```

It defines the v0.1-style top-level structure:

```json
{
  "schema_version": "0.1.0",
  "content_identity": {},
  "consciousness_annotation": {},
  "trace_governance": {},
  "royalty_readiness": {}
}
```

The v0.2 JSON Schema is located at:

```text
schemas/consciousness-circle-metadata-v0.2.schema.json
```

It validates the v0.2 object model:

```json
{
  "schema_version": "0.2.0",
  "content_identity": {},
  "circle": {},
  "trace_governance": {},
  "privacy_and_consent": {},
  "rag_usage_policy": {},
  "royalty_readiness": {}
}
```

### v0.1 Main Sections

| Section | Description |
|---|---|
| `schema_version` | Version of the metadata schema. |
| `content_identity` | Identifies the content item being annotated. |
| `consciousness_annotation` | Describes the center, layers, connections, and rotation dynamics. |
| `trace_governance` | Defines annotation method, consent scope, review status, and provenance references. |
| `royalty_readiness` | Indicates whether the metadata may enter allocation-readiness review. |

### v0.2 Main Sections

| Section | Description |
|---|---|
| `schema_version` | Version of the v0.2 metadata object. |
| `content_identity` | Identifies the content item being annotated. |
| `circle` | Defines the core Consciousness Circle object, including friction, question, meaning structure, visibility scope, and sovereignty control. |
| `trace_governance` | Defines annotation method, consent scope, review status, and provenance references. |
| `privacy_and_consent` | Defines private fields, public fields, redaction needs, and creator approval rules. |
| `rag_usage_policy` | Defines RAG indexing, summarization, allowed fields, excluded fields, and retrieval notes. |
| `royalty_readiness` | Indicates whether the metadata may enter allocation-readiness review. |

---

## v0.2 Reference Specification

The v0.2 draft reference specification is located at:

```text
spec/consciousness-circle-metadata-specification-v0.2.yaml
```

It proposes the following top-level structure:

```text
schema_version
content_identity
circle
trace_governance
privacy_and_consent
rag_usage_policy
royalty_readiness
```

The central object is:

```text
circle
```

The `circle` object may contain:

```text
circle_id
circle_version
circle_lifecycle
circle_state
proto_friction
initial_friction
core_question
meaning_structure
meaning_boundary
visibility_scope
circle_layers
sovereignty_control
temporal_relationship
sub_circles
silence_node
```

This v0.2 reference specification introduces:

- controlled vocabularies
- validation rules
- minimal / standard / extended conformance profiles
- proto-friction handling
- visibility scope
- sovereignty control
- RAG usage policy
- examples for v0.2 object structures

Current status:

```text
v0.2 = validated draft specification
```

It is validated against the v0.2 example set through JSON Schema and GitHub Actions.

---

## Example

The main v0.1-style example is located at:

```text
examples/note-article-consciousness-circle.sample.json
```

It demonstrates how a note-style article may be annotated with:

- core question
- initial friction
- bodily sensation
- surface facts
- deep context
- affective tags
- center/surface/deep connections
- rotation dynamics
- trace governance
- royalty-readiness signals

Example core question:

```text
AIに読まれる知識は、無料素材のままでよいのか？
```

This sample shows how an article can be treated not only as text data, but also as a traceable semantic structure.

---

## v0.2 Examples

The v0.2 examples demonstrate the proposed Question OS structure.

All current v0.2 examples validate against:

```text
schemas/consciousness-circle-metadata-v0.2.schema.json
```

### Minimal Circle Example

```text
examples/minimal-circle-v0.2.example.yaml
```

Demonstrates a minimal v0.2-compatible profile including:

- core question
- initial friction
- meaning structure
- visibility scope
- sovereignty control
- trace governance
- RAG usage policy

### Extended Circle Example

```text
examples/extended-circle-v0.2.example.yaml
```

Demonstrates an extended profile including:

- proto-friction
- vibration logs
- shadow friction
- silence nodes
- circle layers
- meaning boundary
- temporal relationship
- sub-circles
- royalty-readiness notes

### Proto-Friction Example

```text
examples/proto-friction-v0.2.example.yaml
```

Demonstrates how to represent pre-question pressure, including:

- proto-friction
- vibration logs
- shadow friction
- protected ambiguity
- transition toward structured friction
- no-inference boundaries

### Silence Node Example

```text
examples/silence-node-v0.2.example.yaml
```

Demonstrates how creator-defined silence may be declared as:

```text
a boundary,
not missing data.
```

This example is intended to prevent AI systems from treating silence as permission to infer hidden meaning.

---

## v0.2 Design Notes

The following documents extend the conceptual model toward v0.2.

They define the design path that informs the v0.2 reference specification and schema.

### Friction Taxonomy

See:

```text
docs/friction-taxonomy.md
```

This document defines an initial taxonomy for `initial_friction`.

Suggested friction types include:

```text
bodily_friction
daily_life_friction
social_friction
cognitive_dissonance
ethical_conflict
raw_unresolved_friction
```

The goal is not to classify the creator.

The goal is to classify the origin pressure behind a question.

### Circle Structure Model

See:

```text
docs/circle-structure-model.md
```

This document defines Consciousness Circle metadata as a layered and recursive meaning structure.

Conceptual flow:

```text
initial_friction
↓
core_question
↓
meaning_structure
↓
visibility_scope
↓
sovereignty_control
```

The circle model supports:

- core layer
- inner layer
- outer layer
- circle depth
- visibility scope
- recursive sub-circles
- silence nodes
- temporal relationships
- circle lifecycle states

### Proto-Friction Layer

See:

```text
docs/proto-friction-layer.md
```

This document defines the layer before `initial_friction`.

It supports:

- proto-friction
- shadow friction
- vibration logs
- silence nodes
- pre-verbal pressure
- creator-controlled ambiguity
- transition into structured friction

The purpose is to protect meaning before it becomes language.

### Sovereignty Control Model

See:

```text
docs/sovereignty-control-model.md
```

This document defines how creator-declared meaning structures may be accessed, interpreted, summarized, transformed, or protected.

It introduces concepts such as:

- multi-circle access control
- temporal lineage control
- friction encapsulation
- semantic brake
- inference boundaries
- violation behavior

The core principle is:

```text
Sovereignty without control becomes a cage.
Sovereignty with control becomes a membrane.
```

---

## Privacy and Consent

This specification may include sensitive interpretive metadata.

Sensitive fields may include:

```text
bodily_sensation
initial_friction
deep.context
deep.affective_tags
deep.interpretive_summary
deep.personal_resolution
reviewer_notes
allocation_notes
proto_friction
shadow_friction
silence_node
sovereignty_control
```

For this reason, the specification includes:

- visibility controls
- consent scope
- human final edit
- review status
- provenance references
- anti-gaming flags
- dispute handling notes
- allocation-readiness safeguards
- sovereignty control
- AI inference boundaries

Publishing an article does not automatically mean that the creator has consented to expose deep-layer metadata.

Deep semantic metadata must remain creator-controlled.

---

## Human Review Principle

The specification is built around the following principle:

```text
AI may assist with annotation.
AI must not override the creator’s final interpretation.
```

AI-inferred metadata should be treated as provisional unless reviewed.

Systems should avoid statements such as:

```text
The creator truly felt...
The creator intended...
The creator’s hidden motive was...
```

Preferred language:

```text
The metadata suggests...
The annotation indicates...
The creator-approved metadata states...
The system estimates...
```

This distinction is essential.

The specification is designed to support traceable meaning, not automated inner-state extraction.

---

## Sovereignty Control Principle

The specification is also built around a sovereignty control principle:

```text
AI may read permitted structures.
AI must not infer beyond declared boundaries.
```

Creator-declared metadata may include public, private, abstract, encrypted, or silent layers.

AI systems should not treat missing information as permission to infer.

In particular, systems should respect:

```text
visibility_scope
consent_scope
human_final_edit
review_status
sovereignty_control
ai_inference_allowed
silence_node
```

A creator may declare that something exists but should not be reconstructed.

This is especially important for:

- raw friction
- proto-friction
- shadow friction
- private origin notes
- silence nodes
- unresolved meaning pressure

The goal is not to prevent all interpretation.

The goal is to preserve the creator’s declared boundary.

---

## RAG Usage

In RAG systems, this metadata can support retrieval beyond simple keyword or vector similarity.

Possible retrieval signals include:

```text
core_question
initial_friction
surface facts
deep context
affective tags
connection strength
relation type
resonance points
depth signal score
review status
consent scope
visibility scope
sovereignty control
```

Example filter logic:

```text
consent_scope = rag_reference
review_status = reviewed
human_final_edit = true
depth_signal_score > 0.7
connection.relation_type = resonance
connection.strength > 0.6
```

RAG systems should not expose private or restricted fields unless explicitly permitted.

For detailed guidance, see:

```text
docs/rag-integration-notes.md
```

---

## RAG Boundary Principle

RAG systems should not treat all metadata as equally retrievable.

Suggested behavior:

| Metadata Area | RAG Behavior |
|---|---|
| Public surface metadata | May be indexed if consent permits. |
| Creator-approved summary | May be retrieved if visibility allows. |
| Deep context | Should require explicit permission. |
| Initial friction | Should respect disclosure level. |
| Proto-friction | Private by default. |
| Shadow friction | Should not be inferred from. |
| Silence node | Should be treated as a boundary, not missing data. |
| Sovereignty control | Should guide summarization, transformation, and inference behavior. |

The core rule is:

```text
Existence does not equal permission.
```

---

## Trace Protocol Relationship

Consciousness Circle Metadata can act as a semantic pre-trace layer.

```text
Consciousness Circle Metadata
= describes the semantic structure behind content

Trace Protocol
= records how that content is referenced, reused, transformed, or connected
```

Recommended flow:

```text
Semantic Epicenter Layer
↓
Trace Layer
↓
Review / Dispute Layer
↓
Allocation Readiness
↓
Royalty OS
```

For detailed guidance, see:

```text
docs/relationship-to-trace-protocol.md
```

---

## Royalty OS Usage

This specification may support future Royalty OS workflows.

However, it does not allocate royalties by itself.

Correct flow:

```text
Consciousness Circle Metadata
↓
Trace review
↓
Allocation-readiness review
↓
Human or multi-wing judgment
↓
Possible royalty allocation
```

Incorrect flow:

```text
high depth_signal_score
↓
automatic royalty increase
```

The metadata provides signals.

It does not create entitlement by itself.

For detailed guidance, see:

```text
docs/relationship-to-royalty-os.md
```

---

## Allocation-Readiness

The `royalty_readiness` section may indicate whether a metadata object can be considered for allocation-readiness review.

It includes:

```text
eligible_for_allocation_review
depth_signal_score
requires_human_review
scoring_method
allocation_notes
anti_gaming_flags
```

Important safeguards:

- high depth does not equal legal proof
- high resonance does not equal ownership
- high intensity does not equal entitlement
- AI-estimated scores require review
- allocation decisions must remain separate from metadata annotation
- sovereignty controls should be considered before reuse
- creator boundaries should be respected before allocation review

The core principle is:

```text
Depth is a signal.
Trace is evidence.
Review is the gate.
Allocation is a separate decision.
```

---

## Anti-Gaming Safeguards

Semantic metadata can be gamed.

For example, a system or user may inflate:

```text
depth_signal_score
intensity
connection strength
openness_score
certainty_level
friction_intensity
```

The schema therefore supports anti-gaming flags such as:

```text
score_inflation
low_confidence_high_depth
missing_sources
unreviewed_ai_inference
privacy_sensitive_claim
contradictory_metadata
other
```

These flags do not automatically invalidate the metadata.

They indicate that review is needed.

---

## Design Philosophy

This specification is based on the following design philosophy:

```text
Do not reduce living thought to dead tags.
Do not extract inner meaning without consent.
Do not expose deep metadata without visibility control.
Do not convert semantic depth into automatic entitlement.
Do not override the creator’s final interpretation.
Do not infer private friction from silence.
Do not treat ambiguity as permission to reconstruct hidden meaning.
```

The Consciousness Circle is not:

- a psychological profile
- a diagnosis tool
- a claim of literal consciousness
- a legal authorship proof
- an automatic royalty engine
- a persuasion targeting system
- a tool for extracting hidden motives
- a mechanism for forcing creators to disclose private friction

It is:

- a semantic metadata layer
- a traceability support structure
- a RAG enhancement layer
- a creator-controlled annotation format
- an allocation-readiness signal layer
- a sovereignty control layer
- a bridge between content, context, trace, and review

---

## Use Cases

### 1. AI Retrieval

RAG systems can retrieve content not only by topic, but also by question, semantic depth, and contextual resonance.

### 2. Creator Dashboards

Platforms can show creators how their content is structured semantically:

```text
main question
deep context
resonance points
surface/deep relationships
visibility scope
sovereignty controls
```

### 3. Trace Protocol Integration

Trace systems can use the metadata to connect content items by question, friction, resonance, and interpretive transformation.

### 4. Royalty OS Preparation

Allocation-readiness systems can use the metadata as one signal among many, while preserving human review.

### 5. Multi-Wing Review

Multiple AI models, human reviewers, or domain perspectives can review the same metadata object before high-impact use.

### 6. Meaning-Aware RAG

RAG systems can use creator-approved metadata to retrieve not only relevant text, but also relevant questions, semantic movement, and contextual structure.

### 7. Question-Centered Indexing

Systems can index content by the question that generated it, rather than only by keywords, topics, or surface summaries.

### 8. Creator Sovereignty Control

Creators can define which parts of their meaning structure may be public, AI-readable, summary-only, private, encrypted, or silent.

---

## Minimal Safe Implementation

A minimal safe implementation should include:

```text
schema validation
visibility controls
consent scope
human final edit
review status
annotation method
provenance references
anti-gaming flags
sovereignty control
AI inference boundaries
```

Recommended defaults:

```text
review_status = draft
consent_scope = private
human_final_edit = true
deep.visibility = restricted
bodily_sensation.visibility = private
eligible_for_allocation_review = false
requires_human_review = true
ai_inference_allowed = false for private or silent fields
```

These defaults protect the creator while allowing future expansion.

---

## Validation

This repository uses JSON Schema Draft 2020-12.

### v0.1 Validation

A v0.1-style metadata object should validate against:

```text
schemas/consciousness-circle-metadata.schema.json
```

Example validation target:

```text
examples/note-article-consciousness-circle.sample.json
```

### v0.2 Validation

A v0.2 metadata object should validate against:

```text
schemas/consciousness-circle-metadata-v0.2.schema.json
```

Current validation targets:

```text
examples/minimal-circle-v0.2.example.yaml
examples/extended-circle-v0.2.example.yaml
examples/proto-friction-v0.2.example.yaml
examples/silence-node-v0.2.example.yaml
```

The v0.2 validation script is:

```text
scripts/validate-v0.2-examples.py
```

Run locally:

```bash
python scripts/validate-v0.2-examples.py
```

Expected successful output:

```text
OK: Schema is valid JSON Schema Draft 2020-12: schemas/consciousness-circle-metadata-v0.2.schema.json
OK: Spec YAML parsed: spec/consciousness-circle-metadata-specification-v0.2.yaml
OK: Example validates: examples/minimal-circle-v0.2.example.yaml
OK: Example validates: examples/extended-circle-v0.2.example.yaml
OK: Example validates: examples/proto-friction-v0.2.example.yaml
OK: Example validates: examples/silence-node-v0.2.example.yaml

All v0.2 examples validated successfully.
```

GitHub Actions workflow:

```text
.github/workflows/validate-v0.2-examples.yml
```

Validation status:

```text
Passing
```

---

## Relationship to Other Systems

This specification is designed to be compatible with or extendable toward:

- RAG ecosystems
- Trace Protocol
- Structure Fingerprint
- Royalty OS
- Allocation Readiness
- Multi-Wing Review
- creator-controlled metadata systems
- provenance and audit systems
- semantic indexing systems
- sovereignty control systems
- dispute and review systems

It can be used independently, but its full value appears when connected to trace, review, retrieval, control, and allocation-readiness layers.

---

## Citation

Citation metadata is provided in:

```text
CITATION.cff
```

Use this file when citing or referencing the specification in academic work, repositories, articles, documentation, or derivative projects.

---

## License

This project is licensed under the MIT License.

See:

```text
LICENSE
```

The license covers the specification, schema files, documentation, and associated materials.

Use of this specification does not imply endorsement by the original author or contributors of any derivative work, implementation, platform integration, allocation system, royalty system, or AI-mediated retrieval system.

---

## Changelog

Version history is documented in:

```text
CHANGELOG.md
```

The current documentation release is:

```text
v0.1.3
```

The current validated draft specification is:

```text
v0.2.0
```

---

## Status

```text
Documentation release: 0.1.3
Validated draft specification: 0.2.0
Validation status: Passing
Scope: Initial metadata schema, v0.2 draft reference specification, v0.2 JSON Schema, validated v0.2 examples, field definitions, privacy/human-review principles, Trace Protocol relationship, Royalty OS relationship, RAG integration notes, sovereignty control notes, license, citation metadata, and changelog
```

This is still a draft specification.

The current version focuses on:

- defining the core metadata structure
- separating annotation from allocation
- preserving privacy and consent
- supporting future RAG and Royalty OS workflows
- documenting relationship to Trace Protocol
- documenting relationship to Royalty OS
- documenting RAG integration principles
- documenting sovereignty control principles
- preparing the v0.2 design path
- introducing a v0.2 draft reference specification
- adding a v0.2 JSON Schema
- validating v0.2 examples through GitHub Actions
- preventing premature automation
- documenting citation, licensing, and change history

---

## Non-Goals

This specification does not aim to:

- prove legal authorship
- diagnose creators
- infer hidden motives as facts
- automatically allocate royalties
- replace human review
- expose private deep-layer metadata
- convert emotional intensity into entitlement
- define consciousness scientifically or metaphysically
- define a complete RAG architecture
- define a complete Trace Protocol schema
- define a complete Royalty OS payment engine
- enforce runtime compliance by metadata alone
- force creators to disclose private friction

It is a practical metadata specification, not a claim about the nature of consciousness.

---

## Future Extensions

Possible future documentation extensions include:

```text
docs/multi-wing-review-notes.md
docs/depth-signal-scoring.md
docs/semantic-epicenter-layer.md
docs/dispute-handling-notes.md
docs/redaction-and-public-summary.md
docs/platform-implementation-guide.md
docs/friction-encapsulation-model.md
docs/semantic-brake-notes.md
docs/circle-visualization-notes.md
docs/rag-policy-profile.md
docs/v0.2-migration-notes.md
```

Possible future examples include:

```text
examples/minimal-private-metadata.sample.json
examples/public-rag-reference.sample.json
examples/royalty-readiness-review.sample.json
examples/trace-protocol-reference.sample.json
examples/rag-retrieval-event.sample.json
examples/redacted-public-summary.sample.json
examples/recursive-circle-v0.2.example.yaml
examples/private-core-circle-v0.2.example.yaml
examples/friction-taxonomy-v0.2.example.yaml
examples/semantic-brake-v0.2.example.yaml
examples/rag-policy-v0.2.example.yaml
```

Possible future schema extensions include:

```text
trace_reference
dispute_status
multi_wing_review_result
public_summary
private_layer_redaction
depth_signal_breakdown
semantic_resonance_map
rag_usage_policy
allocation_review_state
visibility_scope
sovereignty_control
proto_friction
shadow_friction
silence_node
circle_lifecycle
temporal_relationship
sub_circles
circle_layers
meaning_boundary
```

Possible future specification files include:

```text
spec/consciousness-circle-metadata-specification-v0.3.yaml
spec/semantic-brake-profile-v0.1.yaml
spec/rag-usage-policy-profile-v0.1.yaml
spec/friction-encapsulation-profile-v0.1.yaml
```

Future work may add:

```text
semantic brake runtime behavior
audit trace references
dispute registry integration
multi-wing review profiles
RAG enforcement profiles
migration notes from v0.1 to v0.2
```

Current status:

```text
v0.1.x
= initial metadata schema and documentation

v0.2.0 draft
= reference specification + JSON Schema + validated examples

future v0.3
= runtime control, audit, semantic brake enforcement, and integration profiles
```

---

## Summary

The Consciousness Circle Metadata Specification provides a structured way to annotate the deeper semantic structure behind content.

It allows AI systems to understand content through:

- the question that generated it
- the friction that shaped it
- the facts that support it
- the context that deepens it
- the connections that move it
- the governance that protects it
- the retrieval layer that uses it carefully
- the review layer that prevents abuse
- the sovereignty controls that define interpretation boundaries

Its purpose is simple:

```text
to preserve the human-originated structure of meaning
without exposing private depth,
without automating entitlement,
and without allowing AI systems to override creator-defined interpretation.
```

The Consciousness Circle is a bridge between:

```text
content
context
question
friction
trace
retrieval
review
sovereignty
allocation-readiness
```

The v0.1 series defines the initial metadata layer.

The v0.2 validated draft model prepares the structure for a more mature Question OS:

```text
friction taxonomy
circle structure
proto-friction layer
sovereignty control
JSON Schema validation
GitHub Actions validation
```

In short:

```text
The answer may be generated.
The question may be declared.
The friction must be protected.
The silence must not be inferred.
The circle must remain creator-controlled.
The structure must be validated.
```


