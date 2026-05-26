# Circle Structure Model

## Status

Draft: v0.1  
Document type: Design note  
Related specification: `consciousness-circle-metadata-specification v0.1`

---

## 1. Purpose

This document defines the structural model of a Consciousness Circle.

A Consciousness Circle is a metadata structure that records the origin, question, meaning boundary, visibility scope, and sovereignty control of a human-originated work.

The purpose of this model is to describe how the inner structure of meaning can be represented as a circle rather than a flat metadata object.

A circle is not merely a container.

It is a boundary system.

It defines:

- what gives birth to the work,
- what question stands at the center,
- what meaning structure emerges from it,
- what may be interpreted,
- what must remain private,
- what AI systems may or may not do.

This document prepares the conceptual foundation for `consciousness-circle-metadata-specification v0.2`.

---

## 2. Why a Circle Structure Is Necessary

In v0.1, the metadata model defines core elements such as:

- `core_question`,
- `initial_friction`,
- `meaning_boundary`,
- `creator_sovereignty`.

However, these elements require a clearer structural relationship.

Without a circle model, the metadata may remain a list of fields.

A list of fields is not enough to represent human meaning.

Human-originated meaning has:

- an origin,
- a center,
- an inside,
- an outside,
- a boundary,
- a silence,
- a public surface,
- a private depth,
- a temporal evolution.

The circle structure gives these elements a coherent form.

It allows the system to represent meaning as a layered, recursive, and controlled structure.

---

## 3. Design Principles

The Circle Structure Model follows seven principles.

### 3.1 Origin-Centered

Every circle begins from an origin pressure.

This origin pressure may be an initial friction, a silence, an unresolved tension, or a pre-verbal discomfort.

The circle does not begin from an answer.

It begins from the pressure that gives birth to a question.

### 3.2 Question-Centered

The `core_question` is the center of the circle.

It is not a tag, topic, or title.

It is the central inquiry around which the work is organized.

### 3.3 Boundary-Aware

A circle defines boundaries.

It should clearly distinguish between:

- what is public,
- what is AI-readable,
- what is summary-only,
- what is private,
- what is intentionally silent,
- what should not be inferred.

### 3.4 Recursive

A circle may contain sub-circles.

A major question may contain smaller questions.

A friction source may generate multiple branches.

A work may contain nested meaning structures.

### 3.5 Revisable

A circle may evolve.

A creator may revise, expand, withdraw, or supersede a circle over time.

### 3.6 Privacy-Preserving

The circle should allow creators to protect private origin material.

A creator should not be forced to reveal raw friction in order to declare meaning sovereignty.

### 3.7 AI-Readable but Creator-Controlled

The circle may be readable by AI systems, but the creator defines how it may be interpreted.

AI systems may assist with navigation, retrieval, and recognition.

They should not override the creator-defined circle structure.

---

## 4. Basic Circle Flow

A Consciousness Circle follows this conceptual flow:

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

### 4.1 Initial Friction

`initial_friction` records the origin pressure behind the work.

It may be bodily, social, cognitive, ethical, daily-life-based, or unresolved.

### 4.2 Core Question

`core_question` records the central question born from the friction.

### 4.3 Meaning Structure

`meaning_structure` records the creator-defined structure of interpretation.

It may include key concepts, intended scope, excluded interpretations, and conceptual dependencies.

### 4.4 Visibility Scope

`visibility_scope` defines what parts of the circle may be public, AI-readable, summary-only, private, or encrypted.

### 4.5 Sovereignty Control

`sovereignty_control` defines what AI systems may do with the circle.

This includes interpretation, summarization, transformation, inference, and violation behavior.

---

## 5. Core Circle Object

A minimal circle may be represented as:

```yaml
circle:
  circle_id: "circle-2026-001"
  circle_version: "0.2"

  core_question: "Who owns the question in the age of AI?"

  initial_friction:
    primary_friction_type: ethical_conflict
    friction_state: structured
    disclosure_level: abstract_public

  meaning_structure:
    central_claim: "Human-originated questions require creator-defined meaning sovereignty."
    intended_scope:
      - AI interpretation
      - creator sovereignty
      - metadata design
    excluded_interpretations:
      - "This is an anti-AI framework."
      - "This is a copyright enforcement system only."

  visibility_scope: "ai_read"

  sovereignty_control:
    interpretation_allowed: true
    summarization_allowed: false
    inference_boundary: no_private_inference
```

This object is only a conceptual model.

The formal schema may be defined in a later version.

---

## 6. Circle Layers

A Consciousness Circle may be understood as three major layers.

```text
core layer
inner layer
outer layer
```

These layers correspond to different levels of access, meaning, and control.

---

## 7. Core Layer

The core layer contains the deepest origin material.

It may include:

- raw initial friction,
- private notes,
- unresolved discomfort,
- shadow friction,
- silence nodes,
- private trace references,
- encrypted origin material.

The core layer should be protected by default.

### Suggested Fields

```yaml
core_layer:
  raw_friction_access: private
  private_trace_uri: "local://private-notes/friction-001"
  private_friction_hash: "sha256:..."
  shadow_friction:
    present: true
    ai_inference_allowed: false
  silence_node:
    present: true
    reason_type: creator_boundary
    ai_inference_allowed: false
```

### Principle

The core layer exists to protect the creator’s private origin.

AI systems should not infer, reconstruct, summarize, or expose this layer unless explicitly permitted.

---

## 8. Inner Layer

The inner layer contains the declared meaning structure.

It may include:

- core question,
- abstracted friction label,
- central claim,
- meaning boundary,
- intended scope,
- excluded interpretations,
- creator-defined interpretive notes.

### Suggested Fields

```yaml
inner_layer:
  core_question: "Who owns the question in the age of AI?"

  abstracted_friction_label: "ethical discomfort regarding AI interpretation and meaning sovereignty"

  meaning_structure:
    central_claim: "The origin of questions should remain visible in AI-mediated interpretation."
    intended_scope:
      - creator sovereignty
      - AI metadata
      - meaning preservation
    excluded_interpretations:
      - "This framework rejects AI."
      - "This framework claims absolute control over all reader interpretation."
```

### Principle

The inner layer may be readable by AI systems, but it should be treated as creator-declared structure.

AI may recognize it.

AI should not overwrite it.

---

## 9. Outer Layer

The outer layer contains public-facing material.

It may include:

- published text,
- public summary,
- tags,
- references,
- approved descriptions,
- public metadata,
- citation information.

### Suggested Fields

```yaml
outer_layer:
  title: "The OS of Questions"
  public_summary: "A framework for protecting question sovereignty and creator-defined meaning in the age of AI."
  tags:
    - artificial_intelligence
    - creator_sovereignty
    - metadata
    - question_os
  public_references:
    - "https://example.org/article"
```

### Principle

The outer layer supports circulation, retrieval, citation, and discovery.

It is the part of the circle most suitable for RAG systems, search systems, and public indexing.

---

## 10. Circle Depth

Circle depth defines how far inward a metadata element exists.

Suggested values:

```text
depth_0_public
depth_1_structural
depth_2_private
depth_3_silent
```

### Definitions

| Depth | Meaning |
| --- | --- |
| `depth_0_public` | Public-facing material suitable for indexing, citation, or summarization. |
| `depth_1_structural` | Creator-declared meaning structure readable by AI with restrictions. |
| `depth_2_private` | Private or protected origin material not available for AI interpretation. |
| `depth_3_silent` | Declared silence or intentionally non-disclosed meaning. |

### Example

```yaml
circle_depth:
  public_summary: depth_0_public
  core_question: depth_1_structural
  raw_friction: depth_2_private
  silence_node: depth_3_silent
```

---

## 11. Visibility Scope

`visibility_scope` defines how a circle or sub-circle may be accessed.

Suggested values:

```text
public
abstract_public
ai_read
ai_summary_only
private
encrypted
silent
```

### Definitions

| Value | Meaning |
| --- | --- |
| `public` | Fully public and readable. |
| `abstract_public` | Only abstracted labels or summaries are public. |
| `ai_read` | AI may read declared structure but should not expose raw content. |
| `ai_summary_only` | AI may use only a creator-approved summary. |
| `private` | Not available to public or AI systems. |
| `encrypted` | Available only as encrypted or hashed reference. |
| `silent` | Intentionally non-disclosed; AI inference should be prohibited. |

### Example

```yaml
visibility_scope:
  circle: ai_read
  initial_friction: abstract_public
  raw_friction: private
  silence_node: silent
```

---

## 12. Circle Openness

A circle may be open, semi-open, closed, or sealed.

Suggested values:

```text
open
semi_open
closed
sealed
```

### Definitions

| Value | Meaning |
| --- | --- |
| `open` | The circle may be interpreted, summarized, and expanded with minimal restriction. |
| `semi_open` | The circle may be read and cited, but interpretation or derivation is limited. |
| `closed` | The circle may be recognized but should not be summarized, transformed, or inferred from. |
| `sealed` | The circle exists only as a protected reference; AI should not access or infer content. |

### Example

```yaml
circle_state:
  openness: semi_open
  interpretation_allowed: true
  derivation_allowed: false
  inference_boundary: no_private_inference
```

### Principle

A circle should not be assumed open simply because it exists.

Existence does not equal permission.

---

## 13. Recursive Circles

A Consciousness Circle may contain sub-circles.

This allows complex works to represent multiple questions, friction sources, or meaning structures.

### Example

```yaml
circle:
  circle_id: "circle-main-001"
  core_question: "Who owns the question in the age of AI?"

  sub_circles:
    - circle_id: "circle-sub-001"
      core_question: "How should AI handle creator-defined silence?"
      visibility_scope: ai_read

    - circle_id: "circle-sub-002"
      core_question: "How can friction be preserved without exposing private details?"
      visibility_scope: abstract_public
```

### Principle

Recursive circles allow a work to contain multiple meaning centers.

A single essay, specification, book, or protocol may contain several nested questions.

---

## 14. Sub-Circle Dependency Types

Sub-circles may relate to the parent circle in different ways.

Suggested values:

```text
derives_from
supports
contrasts_with
extends
refines
protects
questions
supersedes
```

### Example

```yaml
sub_circles:
  - circle_id: "circle-sub-001"
    core_question: "How should AI handle creator-defined silence?"
    dependency_type: protects

  - circle_id: "circle-sub-002"
    core_question: "How can friction become structured metadata?"
    dependency_type: extends
```

### Definitions

| Value | Meaning |
| --- | --- |
| `derives_from` | The sub-circle emerges directly from the parent. |
| `supports` | The sub-circle supports the parent structure. |
| `contrasts_with` | The sub-circle introduces tension or contrast. |
| `extends` | The sub-circle expands the parent. |
| `refines` | The sub-circle clarifies or narrows the parent. |
| `protects` | The sub-circle defines a boundary or protection mechanism. |
| `questions` | The sub-circle challenges the parent. |
| `supersedes` | The sub-circle replaces or updates the parent. |

---

## 15. Meaning Structure

`meaning_structure` defines how the creator wants the work’s meaning architecture to be recognized.

It is not a command to readers.

It is a creator-declared structure for AI systems, metadata processors, trace systems, and review layers.

### Suggested Fields

```yaml
meaning_structure:
  central_claim: "AI should support human-originated questions without erasing their origin."

  key_concepts:
    - question_sovereignty
    - initial_friction
    - creator_defined_meaning
    - semantic_boundary

  intended_scope:
    - AI metadata design
    - creator sovereignty
    - RAG interpretation
    - provenance extension

  excluded_interpretations:
    - "This framework rejects AI."
    - "This framework requires creators to disclose private emotions."
    - "This framework is only about copyright."

  interpretation_notes:
    - "The framework protects the origin of meaning, not absolute control over all future interpretation."
```

### Principle

Meaning structure helps AI systems avoid flattening a work into a generic summary.

---

## 16. Meaning Boundary

The meaning boundary defines where interpretation should stop.

Suggested fields:

```yaml
meaning_boundary:
  allowed_interpretations:
    - "creator sovereignty"
    - "AI metadata control"
    - "meaning preservation"

  restricted_interpretations:
    - "private psychological diagnosis"
    - "inference of undisclosed personal experience"
    - "reconstruction of raw friction"

  ai_inference_allowed: false
```

### Principle

The boundary does not eliminate interpretation.

It prevents unauthorized reconstruction of the creator’s private origin.

---

## 17. Silence Node

A silence node represents intentional non-disclosure.

It is not missing data.

It is a declared boundary.

### Suggested Structure

```yaml
silence_node:
  present: true
  reason_type: creator_boundary
  ai_inference_allowed: false
  note: "A private origin exists but should not be inferred or reconstructed."
```

### Suggested Reason Types

```text
creator_boundary
privacy
unresolved_friction
ethical_risk
context_not_ready
future_revision
```

### Principle

Silence is part of the circle.

AI systems should not treat silence as an invitation to infer.

---

## 18. Circle Lifecycle

A circle may evolve through different lifecycle states.

Suggested values:

```text
draft
active
revised
superseded
withdrawn
archived
sealed
```

### Definitions

| State | Meaning |
| --- | --- |
| `draft` | The circle is being formed. |
| `active` | The circle is currently valid. |
| `revised` | The circle has been modified. |
| `superseded` | A newer circle has replaced it. |
| `withdrawn` | The creator has withdrawn the circle from active use. |
| `archived` | The circle is preserved for historical continuity. |
| `sealed` | The circle exists only as protected or private reference. |

### Example

```yaml
circle_lifecycle:
  state: active
  created_at: "2026-05-26T00:00:00Z"
  revised_at: null
  superseded_by: null
```

---

## 19. Temporal Relationship

A circle may refer to earlier or later circles.

### Suggested Structure

```yaml
temporal_relationship:
  parent_circle_id: "circle-2026-000"
  previous_version: "0.1"
  current_version: "0.2"
  evolution_type: revision
  continuity_note: "The core question remains, but visibility controls have been refined."
```

### Suggested Evolution Types

```text
origin
revision
expansion
correction
reflection
transformation
supersession
withdrawal
```

### Principle

The creator’s thought should be allowed to evolve without erasing earlier origins.

---

## 20. Suggested v0.2 Circle Structure

The following is a possible v0.2 structure.

```yaml
circle:
  circle_id: "circle-2026-001"
  circle_version: "0.2"

  circle_lifecycle:
    state: active
    created_at: "2026-05-26T00:00:00Z"

  initial_friction:
    primary_friction_type: ethical_conflict
    secondary_friction_types:
      - cognitive_dissonance
      - social_friction
    friction_intensity: 0.78
    friction_state: structured
    disclosure_level: abstract_public
    public_friction_label: "ethical discomfort regarding AI interpretation and creator sovereignty"

  core_question: "Who owns the question in the age of AI?"

  meaning_structure:
    central_claim: "Human-originated questions require creator-defined meaning sovereignty."
    key_concepts:
      - question_sovereignty
      - initial_friction
      - creator_defined_meaning
      - semantic_boundary
    intended_scope:
      - AI metadata design
      - creator sovereignty
      - RAG interpretation
    excluded_interpretations:
      - "This framework rejects AI."
      - "This framework requires disclosure of private friction."

  visibility_scope:
    circle: ai_read
    initial_friction: abstract_public
    raw_friction: private
    silence_node: silent

  circle_state:
    openness: semi_open
    interpretation_allowed: true
    derivation_allowed: false
    inference_boundary: no_private_inference

  sovereignty_control:
    access_layer: inner
    interpretation_allowed: true
    summarization_allowed: false
    derivation_restriction: strict
    inference_boundary: no_private_inference
    on_violation: halt_and_return_original_structure

  silence_node:
    present: true
    reason_type: creator_boundary
    ai_inference_allowed: false

  sub_circles:
    - circle_id: "circle-sub-001"
      core_question: "How can friction be preserved without exposing private details?"
      dependency_type: extends
      visibility_scope: abstract_public
```

---

## 21. Relationship to Friction Taxonomy

The Friction Taxonomy defines the types and states of initial friction.

The Circle Structure Model defines where friction belongs within the larger meaning structure.

```text
Friction Taxonomy
= what kind of origin pressure exists

Circle Structure Model
= how that origin pressure becomes part of a meaning circle
```

A friction record may exist at the core layer, inner layer, or outer layer depending on its disclosure level.

---

## 22. Relationship to Sovereignty Control

The Sovereignty Control Model defines how circle elements may be accessed, interpreted, summarized, or protected.

```text
Circle Structure Model
= structure of meaning

Sovereignty Control Model
= control of access and interpretation
```

The circle defines the boundary.

Sovereignty control defines the rules of interaction with that boundary.

---

## 23. Relationship to RAG Systems

RAG systems may use the circle structure to determine what can be indexed, retrieved, summarized, or excluded.

Suggested behavior:

| Circle Element | RAG Behavior |
| --- | --- |
| `outer_layer` | May be indexed if public. |
| `inner_layer` | May be read if permitted, but should preserve creator-defined meaning. |
| `core_layer` | Should not be indexed unless explicitly permitted. |
| `silence_node` | Should not be inferred from. |
| `visibility_scope` | Should guide ingestion and retrieval behavior. |
| `sovereignty_control` | Should guide summarization and generation behavior. |

### Principle

RAG systems should not treat all metadata as equally retrievable.

The circle defines retrieval boundaries.

---

## 24. Relationship to Trace and Royalty Systems

A Consciousness Circle may become a source structure for trace, attribution, dispute, or royalty systems.

If a circle is reused, summarized, cited, or transformed, trace systems may record that interaction.

If a circle contributes value to downstream outputs, future royalty or allocation systems may refer to its declared structure.

However, circle existence does not automatically imply royalty eligibility.

Additional review, trace validation, and allocation readiness may be required.

---

## 25. Design Risks

### 25.1 Over-Structuring

If the circle model becomes too complex, creators may avoid using it.

The structure should remain minimal at the point of entry.

### 25.2 False Control

Declaring a boundary does not guarantee enforcement.

Runtime systems, RAG filters, audit layers, and compliance mechanisms are required.

### 25.3 AI Over-Inference

AI systems may infer private meaning from partial structures.

This is why `silence_node`, `visibility_scope`, and `sovereignty_control` must work together.

### 25.4 Creator Burden

Creators should not be required to fully map every layer of a circle.

The system should support minimal declarations.

### 25.5 Rigid Identity Locking

A creator should not become trapped by an earlier circle.

Temporal revision and lifecycle states are essential.

---

## 26. Minimal Circle Profile

To reduce creator burden, a minimal profile should be supported.

```yaml
circle:
  circle_id: "circle-2026-001"
  core_question: "Who owns the question in the age of AI?"
  initial_friction:
    primary_friction_type: ethical_conflict
    disclosure_level: abstract_public
  visibility_scope:
    circle: ai_read
  sovereignty_control:
    inference_boundary: no_private_inference
```

This minimal profile allows participation without requiring full disclosure.

---

## 27. Extended Circle Profile

An extended profile may include full structure.

```yaml
circle:
  circle_id: "circle-2026-001"
  circle_version: "0.2"
  circle_lifecycle: {}
  initial_friction: {}
  core_question: ""
  meaning_structure: {}
  visibility_scope: {}
  circle_state: {}
  sovereignty_control: {}
  silence_node: {}
  temporal_relationship: {}
  sub_circles: []
```

This profile is suitable for advanced use, specification development, RAG policy testing, trace integration, or protocol-level review.

---

## 28. Future Extensions

Future versions may define:

- formal JSON Schema,
- YAML reference specification,
- recursive circle validation,
- sub-circle dependency validation,
- circle lifecycle validation,
- RAG ingestion profiles,
- AI compliance profiles,
- encrypted core layer references,
- circle visualization format,
- Graphviz diagrams,
- multi-wing review integration,
- trace and dispute registry integration.

Suggested future files:

```text
examples/minimal-circle.example.yaml
examples/extended-circle.example.yaml
examples/recursive-circle.example.yaml
examples/private-core-circle.example.yaml
examples/silence-node-circle.example.yaml
diagrams/circle-structure.dot
```

---

## 29. Summary

A Consciousness Circle is not a flat metadata object.

It is a living boundary structure.

It begins from friction.

It centers around a question.

It organizes meaning.

It defines visibility.

It protects silence.

It controls AI interpretation.

```text
Friction gives birth to the question.
The question forms the circle.
The circle defines the boundary.
The boundary allows meaning to live.
```

The purpose of the circle is not to imprison thought.

The purpose is to protect the origin of meaning while allowing controlled evolution.

A mature Question OS requires this circle structure.

Without it, metadata remains descriptive.

With it, metadata becomes a living architecture of human-originated meaning.
