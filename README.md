# Consciousness Circle Metadata Specification v0.1

A metadata specification for annotating the question, friction, surface facts, deep context, relational dynamics, trace governance, and allocation-readiness of a content item in AI-mediated knowledge ecosystems.

This specification is designed for environments where human-created knowledge is increasingly read, retrieved, summarized, referenced, transformed, and recomposed by AI systems.

It provides a structured way to describe not only what a content item says, but also the question, tension, semantic depth, and interpretive movement behind it.

---

## Purpose

The Consciousness Circle Metadata Specification defines a metadata layer for content such as articles, essays, notes, repository documents, book sections, social posts, and other knowledge artifacts.

Its purpose is to support:

- richer AI retrieval
- semantic traceability
- question-centered indexing
- surface/deep layer annotation
- creator-controlled deep metadata
- consent-aware RAG workflows
- trace governance
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
surface facts
deep context
layer connections
rotation dynamics
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
```

### Center

The center is the generative core of the content.

It contains:

- the core question
- the initial friction
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

---

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── schemas/
│   └── consciousness-circle-metadata.schema.json
├── examples/
│   └── note-article-consciousness-circle.sample.json
└── docs/
    ├── field-definitions.md
    ├── privacy-consent-and-human-review.md
    ├── relationship-to-trace-protocol.md
    ├── relationship-to-royalty-os.md
    └── rag-integration-notes.md
```

### Key Files

| Path | Description |
|---|---|
| `README.md` | Overview of the specification, core concepts, usage notes, and repository structure. |
| `LICENSE` | License for the specification, schema, documentation, and associated materials. |
| `CITATION.cff` | Citation metadata for referencing this specification. |
| `CHANGELOG.md` | Version history and notable changes. |
| `schemas/consciousness-circle-metadata.schema.json` | JSON Schema definition for Consciousness Circle metadata. |
| `examples/note-article-consciousness-circle.sample.json` | Example metadata object for a note-style article. |
| `docs/field-definitions.md` | Detailed explanation of fields, allowed values, score interpretation, and usage notes. |
| `docs/privacy-consent-and-human-review.md` | Privacy, consent, visibility control, human review, RAG safeguards, and allocation-readiness safeguards. |
| `docs/relationship-to-trace-protocol.md` | Explains how Consciousness Circle Metadata relates to Trace Protocol and semantic trace workflows. |
| `docs/relationship-to-royalty-os.md` | Explains how Consciousness Circle Metadata may support Royalty OS review without becoming an automatic allocation engine. |
| `docs/rag-integration-notes.md` | Explains how the metadata may be integrated into RAG systems for meaning-aware retrieval with consent controls. |

---

## Start Here

Recommended reading order:

1. `README.md`  
   Start with the overview, core concept, repository structure, and intended use cases.

2. `schemas/consciousness-circle-metadata.schema.json`  
   Review the formal JSON Schema definition for Consciousness Circle metadata.

3. `examples/note-article-consciousness-circle.sample.json`  
   See how the schema can be applied to a note-style article.

4. `docs/field-definitions.md`  
   Read the detailed field definitions, allowed values, score interpretation, and RAG / Royalty OS usage notes.

5. `docs/privacy-consent-and-human-review.md`  
   Review privacy, consent, visibility control, human final edit, AI-inferred metadata handling, and anti-gaming safeguards.

6. `docs/relationship-to-trace-protocol.md`  
   Understand how Consciousness Circle Metadata acts as a semantic pre-trace layer for Trace Protocol workflows.

7. `docs/relationship-to-royalty-os.md`  
   Understand how the metadata may support Royalty OS and Allocation Readiness without directly triggering royalties.

8. `docs/rag-integration-notes.md`  
   Review how RAG systems may use the metadata for question-centered, meaning-aware retrieval while respecting consent and visibility controls.

9. `CHANGELOG.md`  
   Check the version history and notable changes for this specification.

10. `CITATION.cff`  
    Use this file when citing or referencing the specification in papers, repositories, articles, or derivative work.

11. `LICENSE`  
    Review the license terms before reuse, modification, redistribution, or integration.

---

## Schema

The main schema is located at:

```text
schemas/consciousness-circle-metadata.schema.json
```

It defines the top-level structure:

```json
{
  "schema_version": "0.1.0",
  "content_identity": {},
  "consciousness_annotation": {},
  "trace_governance": {},
  "royalty_readiness": {}
}
```

### Main Sections

| Section | Description |
|---|---|
| `schema_version` | Version of the metadata schema. |
| `content_identity` | Identifies the content item being annotated. |
| `consciousness_annotation` | Describes the center, layers, connections, and rotation dynamics. |
| `trace_governance` | Defines annotation method, consent scope, review status, and provenance references. |
| `royalty_readiness` | Indicates whether the metadata may enter allocation-readiness review. |

---

## Example

The main example is located at:

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
```

The Consciousness Circle is not:

- a psychological profile
- a diagnosis tool
- a claim of literal consciousness
- a legal authorship proof
- an automatic royalty engine
- a persuasion targeting system

It is:

- a semantic metadata layer
- a traceability support structure
- a RAG enhancement layer
- a creator-controlled annotation format
- an allocation-readiness signal layer
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
```

### 3. Trace Protocol Integration

Trace systems can use the metadata to connect content items by question, friction, resonance, and interpretive transformation.

### 4. Royalty OS Preparation

Allocation-readiness systems can use the metadata as one signal among many, while preserving human review.

### 5. Multi-Wing Review

Multiple AI models, human reviewers, or domain perspectives can review the same metadata object before high-impact use.

### 6. Meaning-Aware RAG

RAG systems can use creator-approved metadata to retrieve not only relevant text, but also relevant questions, semantic movement, and contextual structure.

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
```

These defaults protect the creator while allowing future expansion.

---

## Validation

This repository uses JSON Schema Draft 2020-12.

A metadata object should validate against:

```text
schemas/consciousness-circle-metadata.schema.json
```

Example validation target:

```text
examples/note-article-consciousness-circle.sample.json
```

A future version of this repository may include CI-based validation for examples and schemas.

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

It can be used independently, but its full value appears when connected to trace, review, retrieval, and allocation-readiness layers.

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

The current release is:

```text
v0.1.1
```

---

## Status

```text
Version: 0.1.1
Status: Draft
Scope: Initial metadata schema, example, field definitions, privacy/human-review principles, Trace Protocol relationship, Royalty OS relationship, RAG integration notes, license, citation metadata, and changelog
```

This is an early specification.

The current version focuses on:

- defining the core metadata structure
- separating annotation from allocation
- preserving privacy and consent
- supporting future RAG and Royalty OS workflows
- documenting relationship to Trace Protocol
- documenting relationship to Royalty OS
- documenting RAG integration principles
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
```

Possible future examples include:

```text
examples/minimal-private-metadata.sample.json
examples/public-rag-reference.sample.json
examples/royalty-readiness-review.sample.json
examples/trace-protocol-reference.sample.json
examples/rag-retrieval-event.sample.json
examples/redacted-public-summary.sample.json
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
```

---

## Summary

The Consciousness Circle Metadata Specification v0.1.1 provides a structured way to annotate the deeper semantic structure behind content.

It allows AI systems to understand content through:

- the question that generated it
- the friction that shaped it
- the facts that support it
- the context that deepens it
- the connections that move it
- the governance that protects it
- the retrieval layer that uses it carefully
- the review layer that prevents abuse

Its purpose is simple:

```text
Make meaning traceable.
Keep the creator sovereign.
Retrieve meaning with consent.
Separate depth from automatic entitlement.
Prepare knowledge for AI-era retrieval, trace, and value circulation.
```
