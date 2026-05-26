# Proto-Friction Layer

## Status

Draft: v0.1  
Document type: Design note  
Related specification: `consciousness-circle-metadata-specification v0.1`

---

## 1. Purpose

This document defines the Proto-Friction Layer for the Consciousness Circle Metadata Specification.

The Proto-Friction Layer exists to record forms of human-originated friction that have not yet become clear questions, structured concepts, or formal meaning boundaries.

Not all meaningful human thought begins as language.

Before a question becomes a question, it may exist as:

- discomfort,
- hesitation,
- silence,
- repeated tension,
- vague resistance,
- intuition,
- bodily unease,
- ethical pressure,
- incomplete thought,
- unstructured emotional weight.

The purpose of this layer is to prevent the Question OS from excluding creators who cannot yet fully articulate their friction.

A mature system for human-originated meaning must be able to protect not only structured questions, but also the pre-verbal pressure that comes before them.

---

## 2. Why Proto-Friction Is Necessary

The Consciousness Circle model places `initial_friction` at the origin of meaning.

However, even `initial_friction` may already be too structured for some creators.

A creator may feel that something is wrong, but may not yet know:

- what the issue is,
- what category it belongs to,
- whether it is bodily, social, ethical, or cognitive,
- how to express it safely,
- whether it should be public,
- whether AI should be allowed to infer from it.

If the system only accepts clearly structured friction, then it creates a hidden exclusion:

```text
Only people who can already explain their friction can participate.
```

This would be a failure.

The Proto-Friction Layer exists to protect the stage before explanation.

It allows creators to declare:

```text
There is friction here.
It is not yet ready to become language.
Do not erase it.
Do not force it.
Do not infer beyond it.
```

---

## 3. Design Principles

The Proto-Friction Layer follows seven principles.

### 3.1 Pre-Verbal Inclusion

The system should accept friction before it becomes a clear sentence, argument, or question.

### 3.2 Creator-Controlled Ambiguity

Ambiguity should be controlled by the creator.

AI systems should not treat ambiguity as permission to invent missing meaning.

### 3.3 Non-Forcing

The system should not force creators to convert raw discomfort into structured explanation.

### 3.4 Privacy by Default

Proto-friction should be private or protected by default unless explicitly disclosed.

### 3.5 No Unauthorized Inference

AI systems should not infer private meaning from proto-friction signals unless explicitly permitted.

### 3.6 Evolvable Structure

Proto-friction may later become initial friction, a core question, a silence node, or be withdrawn.

### 3.7 Validity of Silence

Silence is not absence.

Silence may be an intentional boundary, an unresolved state, or a meaningful part of the circle.

---

## 4. Conceptual Position

The Proto-Friction Layer sits before `initial_friction`.

```text
proto_friction
↓
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

It is the earliest detectable layer of meaning origin.

It does not yet need to be classified as:

- bodily friction,
- daily-life friction,
- social friction,
- cognitive dissonance,
- ethical conflict,
- raw unresolved friction.

Instead, it may simply declare that a pre-question pressure exists.

---

## 5. Core Concepts

The Proto-Friction Layer includes four core concepts.

```text
proto_friction
shadow_friction
vibration_log
silence_node
```

Each concept represents a different form of pre-structured meaning.

---

## 6. Proto-Friction

### Definition

`proto_friction` refers to an early, unstable, or not-yet-verbalized pressure that may later become structured friction or a core question.

It is the earliest recordable form of meaning pressure.

### Examples

- “Something feels wrong, but I cannot explain it yet.”
- “There is repeated discomfort around this theme.”
- “This may become a question later.”
- “The issue is present, but not ready for public structure.”
- “A pressure exists, but its category is still unclear.”

### Suggested Structure

```yaml
proto_friction:
  present: true
  proto_state: emerging
  articulation_level: pre_verbal
  disclosure_level: private
  ai_inference_allowed: false
```

---

## 7. Proto-State

`proto_state` describes the current condition of proto-friction.

Suggested values:

```text
emerging
recurring
unstable
pressurized
partially_articulated
deferred
withdrawn
```

### Definitions

| Value | Meaning |
| --- | --- |
| `emerging` | The friction is beginning to appear. |
| `recurring` | The friction appears repeatedly over time. |
| `unstable` | The friction is present but unclear or changing. |
| `pressurized` | The friction has strong force but is not yet structured. |
| `partially_articulated` | The friction has some language but remains incomplete. |
| `deferred` | The creator intentionally delays articulation. |
| `withdrawn` | The creator no longer wishes to maintain this proto-friction record. |

---

## 8. Articulation Level

`articulation_level` defines how clearly the proto-friction has become language.

Suggested values:

```text
pre_verbal
image_based
gesture_based
fragmentary
partial_sentence
draft_question
structured_friction
```

### Definitions

| Value | Meaning |
| --- | --- |
| `pre_verbal` | Exists before language. |
| `image_based` | Exists as image, symbol, scene, or visual intuition. |
| `gesture_based` | Exists as bodily gesture, rhythm, movement, or posture. |
| `fragmentary` | Exists as fragments, words, or scattered notes. |
| `partial_sentence` | Exists as incomplete statements. |
| `draft_question` | Has begun to form as a question. |
| `structured_friction` | Ready to become `initial_friction`. |

---

## 9. Shadow Friction

### Definition

`shadow_friction` refers to friction that is known to exist but intentionally left undefined.

It may be too private, sensitive, early, unstable, or risky to describe.

Shadow friction is not missing data.

It is declared non-disclosure.

### Suggested Structure

```yaml
shadow_friction:
  present: true
  disclosure_level: private
  reason_type: creator_boundary
  ai_inference_allowed: false
  note: "Additional private friction exists but should not be inferred or reconstructed."
```

### Suggested Reason Types

```text
creator_boundary
privacy
ethical_risk
emotional_risk
context_not_ready
unresolved_pressure
future_revision
```

### Principle

Shadow friction tells AI systems:

```text
There is something here.
Do not try to reconstruct it.
```

---

## 10. Vibration Log

### Definition

`vibration_log` records repeated signals, tensions, or subtle disturbances before they become structured friction.

It is a low-resolution log of early meaning pressure.

It may be useful when a creator does not yet know what the friction is, but notices that a theme keeps returning.

### Suggested Structure

```yaml
vibration_log:
  - vibration_id: "vibration-001"
    date: "2026-05-20"
    signal_type: recurring_discomfort
    articulation_level: fragmentary
    note: "Repeated discomfort around AI interpretation."
    ai_inference_allowed: false
```

### Suggested Signal Types

```text
recurring_discomfort
bodily_signal
ethical_pressure
conceptual_gap
social_resistance
creative_pull
silence_pressure
unclassified_signal
```

### Principle

The vibration log should preserve early signals without forcing premature explanation.

---

## 11. Silence Node

### Definition

A `silence_node` records intentional silence as part of the structure.

It prevents AI systems from treating silence as missing data or as an invitation to infer.

### Suggested Structure

```yaml
silence_node:
  present: true
  reason_type: creator_boundary
  ai_inference_allowed: false
  note: "The creator intentionally withholds this part of the origin structure."
```

### Suggested Reason Types

```text
creator_boundary
privacy
unresolved_friction
ethical_risk
context_not_ready
future_revision
sealed_origin
```

### Principle

Silence should be treated as a boundary, not an absence.

---

## 12. Disclosure Levels

Proto-friction should support careful disclosure control.

Suggested values:

```text
private
encrypted
abstract_public
ai_read
silent
```

### Definitions

| Value | Meaning |
| --- | --- |
| `private` | Not available to AI or public systems. |
| `encrypted` | Exists only as encrypted or hashed reference. |
| `abstract_public` | Only a vague abstract signal may be public. |
| `ai_read` | AI may read declared structure under restriction. |
| `silent` | Existence may be declared, but content should not be inferred. |

### Default Recommendation

The default disclosure level for proto-friction should be:

```text
private
```

Proto-friction should not become public by accident.

---

## 13. AI Inference Boundary

Proto-friction requires a strong inference boundary.

Suggested field:

```yaml
ai_inference_allowed: false
```

When this value is false, AI systems should not:

- infer private meaning,
- reconstruct hidden friction,
- diagnose the creator,
- generate speculative origin stories,
- summarize withheld context,
- transform silence into content.

### Suggested Boundary Object

```yaml
proto_friction_control:
  ai_inference_allowed: false
  summarization_allowed: false
  transformation_allowed: false
  reconstruction_allowed: false
  on_violation: halt_and_return_declared_boundary
```

---

## 14. Transition to Initial Friction

Proto-friction may later evolve into `initial_friction`.

Suggested transition structure:

```yaml
proto_friction_transition:
  from_proto_friction_id: "proto-001"
  to_initial_friction_id: "friction-001"
  transition_type: articulation
  transitioned_at: "2026-05-26T00:00:00Z"
  creator_confirmed: true
```

### Suggested Transition Types

```text
articulation
classification
structuring
integration
withdrawal
sealing
```

### Principle

Only the creator should confirm when proto-friction has become structured friction.

AI may suggest.

The creator decides.

---

## 15. Relationship to Initial Friction

Proto-friction is not a replacement for `initial_friction`.

It is the layer before it.

```text
Proto-Friction Layer
= pre-question pressure

Initial Friction
= structured origin pressure
```

A creator may skip proto-friction and declare initial friction directly.

However, if the origin pressure is unclear, private, or unresolved, proto-friction provides a safer entry point.

---

## 16. Relationship to Friction Taxonomy

The Friction Taxonomy classifies structured friction.

The Proto-Friction Layer handles friction before classification.

```text
Proto-Friction Layer
= not yet classified

Friction Taxonomy
= classified origin pressure
```

A proto-friction record may later become:

- `bodily_friction`,
- `daily_life_friction`,
- `social_friction`,
- `cognitive_dissonance`,
- `ethical_conflict`,
- `raw_unresolved_friction`.

But it does not need to be classified immediately.

---

## 17. Relationship to Circle Structure

The Proto-Friction Layer may exist at the deepest part of the circle.

Suggested conceptual position:

```text
depth_3_silent
↓
depth_2_private
↓
depth_1_structural
↓
depth_0_public
```

Proto-friction often belongs to:

- `depth_3_silent`,
- `depth_2_private`.

It should not be automatically exposed to the outer layer.

---

## 18. Relationship to Sovereignty Control

The Sovereignty Control Model defines how proto-friction may be protected.

Proto-friction should usually include strong controls:

```yaml
sovereignty_control:
  access_layer: core
  interpretation_allowed: false
  summarization_allowed: false
  derivation_restriction: strict
  inference_boundary: no_inference
  on_violation: halt_and_return_original_structure
```

### Principle

The more incomplete the friction, the stronger the boundary should be.

---

## 19. Minimal Proto-Friction Profile

A minimal proto-friction record may be very simple.

```yaml
proto_friction:
  present: true
  proto_state: emerging
  articulation_level: pre_verbal
  disclosure_level: private
  ai_inference_allowed: false
```

This allows a creator to declare early friction without explaining it.

---

## 20. Extended Proto-Friction Profile

An extended profile may include logs and transitions.

```yaml
proto_friction:
  proto_friction_id: "proto-2026-001"
  present: true
  proto_state: recurring
  articulation_level: fragmentary
  disclosure_level: private
  ai_inference_allowed: false

  vibration_log:
    - vibration_id: "vibration-001"
      date: "2026-05-20"
      signal_type: recurring_discomfort
      note: "Repeated discomfort around AI summarization."
      ai_inference_allowed: false

  shadow_friction:
    present: true
    disclosure_level: private
    reason_type: creator_boundary
    ai_inference_allowed: false

  silence_node:
    present: true
    reason_type: context_not_ready
    ai_inference_allowed: false

  proto_friction_control:
    summarization_allowed: false
    transformation_allowed: false
    reconstruction_allowed: false
    on_violation: halt_and_return_declared_boundary
```

---

## 21. Suggested v0.2 Integration

The Proto-Friction Layer may be integrated into v0.2 as an optional structure.

```yaml
circle:
  circle_id: "circle-2026-001"

  proto_friction:
    present: true
    proto_state: emerging
    articulation_level: pre_verbal
    disclosure_level: private
    ai_inference_allowed: false

  initial_friction:
    primary_friction_type: raw_unresolved_friction
    disclosure_level: abstract_public

  core_question: "Who owns the question in the age of AI?"
```

### Principle

Proto-friction should remain optional.

A circle may begin directly from `initial_friction`.

But if a creator needs to preserve pre-question pressure, the layer should be available.

---

## 22. Design Risks

### 22.1 Over-Structuring the Unstructured

The biggest risk is forcing proto-friction to become too formal.

This layer should remain lightweight.

### 22.2 AI Over-Inference

AI systems may treat vague signals as clues and infer private meaning.

This must be explicitly prohibited by default.

### 22.3 Creator Burden

Creators should not be required to log every feeling, discomfort, or hesitation.

Proto-friction should be used only when it helps preserve meaning origin.

### 22.4 False Depth

Not every vague feeling is structurally important.

The system should avoid turning all ambiguity into significance.

### 22.5 Privacy Leakage

Even declaring that proto-friction exists may reveal something.

Creators should be able to use silent, private, encrypted, or abstract forms.

---

## 23. Implementation Notes

A compliant system should:

- allow proto-friction to remain private,
- avoid requiring detailed explanation,
- prohibit AI inference by default,
- support later transition into structured friction,
- preserve creator confirmation,
- support silence nodes,
- avoid diagnostic interpretation,
- distinguish between absence and intentional non-disclosure.

A system should not:

- force classification,
- infer hidden meaning,
- diagnose the creator,
- expose private proto-friction,
- treat silence as missing data,
- convert ambiguity into content without permission.

---

## 24. Future Extensions

Future versions may define:

- formal JSON Schema,
- proto-friction examples,
- vibration log examples,
- encrypted proto-friction references,
- transition records from proto-friction to initial friction,
- AI compliance profile,
- RAG exclusion profile,
- audit trace integration,
- multi-wing review handling,
- dispute handling for inferred private meaning.

Suggested future files:

```text
examples/minimal-proto-friction.example.yaml
examples/vibration-log.example.yaml
examples/shadow-friction.example.yaml
examples/silence-node.example.yaml
examples/proto-to-friction-transition.example.yaml
```

---

## 25. Summary

The Proto-Friction Layer exists to protect meaning before it becomes language.

It allows creators to declare early pressure without being forced to explain, classify, or expose it.

```text
Before friction becomes structured,
there may be vibration.

Before a question appears,
there may be silence.

Before meaning becomes public,
there may be a protected origin.
```

A mature Question OS must not only protect clear questions.

It must also protect the fragile, incomplete, and pre-verbal conditions from which questions are born.

The Proto-Friction Layer is that protection.
