# Friction Taxonomy

## Status

Draft: v0.1  
Document type: Design note  
Related specification: `consciousness-circle-metadata-specification v0.1`

---

## 1. Purpose

This document defines an initial taxonomy for `initial_friction` in the Consciousness Circle Metadata Specification.

`initial_friction` refers to the human collision with reality that gives birth to a question, idea, structure, or work.

The purpose of this taxonomy is to make initial friction more structured, without reducing it to a rigid psychological or emotional label.

The goal is not to classify the creator.

The goal is to classify the type of friction that contributed to the emergence of a question.

---

## 2. Why Friction Taxonomy Is Necessary

In v0.1, `initial_friction` is defined as a core concept.

However, without a taxonomy, it remains too abstract for practical use.

A creator may declare that a work emerged from friction, but AI systems, RAG systems, trace systems, or future review layers may not be able to understand what kind of friction is being referenced.

This creates several risks:

- `initial_friction` may become only poetic language.
- AI systems may over-infer private context.
- creators may feel pressured to reveal raw personal details.
- different types of friction may be treated as identical.
- unresolved or pre-verbal friction may be excluded.

A friction taxonomy provides a middle layer.

It allows creators to declare the structural type of friction without exposing the full private content of that friction.

---

## 3. Design Principles

The taxonomy follows five principles.

### 3.1 Creator-Controlled

The creator defines the friction type.

AI systems may suggest labels, but should not override the creator’s declaration.

### 3.2 Privacy-Preserving

The taxonomy should allow creators to signal the existence and type of friction without exposing raw private details.

### 3.3 Non-Diagnostic

This taxonomy is not a medical, psychological, or legal diagnostic framework.

It should not be used to classify the creator’s identity, health, personality, or status.

It classifies the origin pressure behind a question.

### 3.4 Revisable

A friction label may change over time.

A question may first appear as bodily discomfort, later become cognitive dissonance, and eventually be understood as ethical conflict.

### 3.5 Non-Exclusive

A single work may contain multiple friction types.

The taxonomy should support primary and secondary friction labels.

---

## 4. Core Friction Types

The initial taxonomy defines six major friction types.

```text
F1: bodily_friction
F2: daily_life_friction
F3: social_friction
F4: cognitive_dissonance
F5: ethical_conflict
F6: raw_unresolved_friction

5. F1: Bodily Friction
Definition

Bodily friction refers to friction that begins from physical sensation, fatigue, discomfort, rhythm, illness, tension, posture, breath, sleep, movement, or embodied perception.

It is the friction of having a body in the world.

Examples
fatigue caused by overwork,
discomfort from long-term screen use,
changes in sleep or rhythm,
bodily tension that leads to reflection,
physical practice that changes perception,
breath, posture, or movement revealing a new question.
Suggested Metadata Value
friction_type: bodily_friction
Notes

Bodily friction should not require disclosure of medical details.

A creator may simply declare that the origin was embodied or physical.

6. F2: Daily-Life Friction
Definition

Daily-life friction refers to friction that emerges from ordinary life, work, routine, family, money, tools, habits, schedules, or repeated practical inconvenience.

It is the friction of everyday reality.

Examples
repeated inconvenience in a workflow,
mismatch between daily rhythm and creative work,
practical difficulty in publishing,
financial pressure,
small frustrations that accumulate over time,
ordinary life producing a structural question.
Suggested Metadata Value
friction_type: daily_life_friction
Notes

Daily-life friction is important because many deep questions do not begin as abstract philosophy.

They begin from repeated ordinary resistance.

7. F3: Social Friction
Definition

Social friction refers to friction caused by social systems, institutions, platforms, communities, norms, hierarchy, visibility, exclusion, communication, or collective behavior.

It is the friction between the creator and the surrounding social field.

Examples
discomfort with platform behavior,
mismatch between creator values and market logic,
social pressure to conform,
exclusion from existing categories,
frustration with shallow public discourse,
tension between individual meaning and institutional systems.
Suggested Metadata Value
friction_type: social_friction
Notes

Social friction does not require the creator to identify a specific person, group, or institution.

It may be declared at an abstract level.

8. F4: Cognitive Dissonance
Definition

Cognitive dissonance refers to friction caused by contradiction, inconsistency, unresolved logic, conceptual mismatch, or the failure of existing explanations.

It is the friction of thought encountering a structural gap.

Examples
two ideas that should connect but do not,
an explanation that feels incomplete,
contradiction between theory and reality,
mismatch between technical progress and social understanding,
inability of existing language to describe a phenomenon,
repeated observation that does not fit existing categories.
Suggested Metadata Value
friction_type: cognitive_dissonance
Notes

Cognitive dissonance is often the origin of new conceptual frameworks.

It may be the most common friction type in structural philosophy, technical design, and research-oriented writing.

9. F5: Ethical Conflict
Definition

Ethical conflict refers to friction caused by moral tension, responsibility, fairness, harm, misuse, accountability, rights, consent, attribution, or value circulation.

It is the friction of “something should not remain unresolved.”

Examples
concern over AI using creator work without return,
discomfort with invisible extraction,
questions about attribution,
platform power imbalance,
unclear consent,
tension between innovation and responsibility,
concern that human origin may be erased.
Suggested Metadata Value
friction_type: ethical_conflict
Notes

Ethical conflict often becomes the basis for governance, protocol design, audit systems, dispute systems, or royalty models.

10. F6: Raw / Unresolved Friction
Definition

Raw or unresolved friction refers to friction that has not yet been fully verbalized, classified, or structurally understood.

It may exist as discomfort, silence, hesitation, intuition, pressure, image, sound, gesture, or vague resistance.

It is the friction before language.

Examples
a vague but persistent discomfort,
a feeling that something is wrong,
silence around a theme,
an intuition not yet expressible,
a recurring image or sensation,
a question that has not yet become a question.
Suggested Metadata Value
friction_type: raw_unresolved_friction
Notes

This category is essential.

Without it, the system would only recognize creators who can already verbalize their friction.

A mature Question OS must allow participation before full articulation.

11. Multiple Friction Types

A single Consciousness Circle may contain multiple friction types.

Suggested structure:

initial_friction:
  primary_friction_type: ethical_conflict
  secondary_friction_types:
    - cognitive_dissonance
    - social_friction
Principle

The primary friction type identifies the dominant origin pressure.

Secondary friction types identify supporting pressures.

12. Friction Intensity

Friction intensity is an optional scalar value from 0.0 to 1.0.

It represents the creator-declared strength of the friction.

It should not be treated as an objective measurement.

It is a self-declared structural signal.

Suggested Scale
Value Range	Meaning
0.0 - 0.2	weak or background friction
0.3 - 0.5	noticeable friction that shaped the work
0.6 - 0.8	strong friction that significantly influenced the work
0.9 - 1.0	defining friction that strongly shaped the creator’s question
Example
initial_friction:
  primary_friction_type: ethical_conflict
  friction_intensity: 0.78
Caution

Friction intensity should not be used to rank creators.

It is not a competition score.

It is a contextual signal for meaning origin.

13. Friction State

Friction may exist in different states.

Suggested values:

emerging
active
structured
resolved
unresolved
transformed
withdrawn
Definitions
State	Meaning
emerging	The friction is beginning to appear but is not yet clearly understood.
active	The friction is currently shaping the creator’s question.
structured	The friction has been converted into a clear conceptual structure.
resolved	The friction has been sufficiently addressed or integrated.
unresolved	The friction remains open or incomplete.
transformed	The friction has changed into a new form.
withdrawn	The creator no longer wishes to expose or use this friction record.
Example
initial_friction:
  primary_friction_type: cognitive_dissonance
  friction_state: structured
14. Friction Timeline

A friction source may evolve over time.

A timeline can record major stages.

Suggested Structure
friction_timeline:
  - event_type: emergence
    date: "2026-05-01"
    note: "Initial discomfort appeared."
  - event_type: articulation
    date: "2026-05-12"
    note: "The discomfort became a clear question."
  - event_type: structuring
    date: "2026-05-26"
    note: "The question was formalized into a metadata structure."
Suggested Event Types
emergence
recurrence
articulation
structuring
revision
resolution
transformation
withdrawal
Principle

The timeline should preserve the evolution of friction without forcing creators to expose unnecessary private detail.

15. Privacy and Disclosure Levels

Friction records should support disclosure control.

Suggested values:

public
abstract_public
ai_read
ai_summary_only
private
encrypted
Definitions
Value	Meaning
public	The friction description may be publicly visible.
abstract_public	Only an abstract label or summary may be public.
ai_read	AI may read the declared structure but should not expose it directly.
ai_summary_only	AI may use only a creator-approved summary.
private	The friction is not available to AI or public systems.
encrypted	The friction is referenced only through encrypted or hashed form.
Example
initial_friction:
  primary_friction_type: social_friction
  disclosure_level: abstract_public
  public_friction_label: "platform-level discomfort around AI interpretation"
16. Raw Friction and Unresolved Friction

The taxonomy should allow friction that is not yet cleanly structured.

Suggested fields:

initial_friction:
  primary_friction_type: raw_unresolved_friction
  friction_raw: "A recurring discomfort that has not yet become a clear question."
  friction_unresolved: true
  disclosure_level: private
Principle

The system should not punish creators for being unfinished.

Unfinished friction is not noise.

It may be the earliest form of a future question.

17. Shadow Friction

Shadow friction refers to friction that is present but intentionally left undefined.

It may be too private, too early, too sensitive, or too unstable to describe.

Suggested Structure
shadow_friction:
  present: true
  disclosure_level: private
  ai_inference_allowed: false
  note: "Creator has declared that additional private friction exists but should not be inferred."
Principle

Shadow friction tells AI systems:

There is something here.
Do not try to reconstruct it.

This is important for preventing AI from over-interpreting silence.

18. Silence Node

A silence node records intentional non-disclosure.

It treats silence not as missing data, but as part of the structure.

Suggested Structure
silence_node:
  present: true
  reason_type: creator_boundary
  ai_inference_allowed: false
Suggested Reason Types
creator_boundary
privacy
unresolved_friction
ethical_risk
context_not_ready
future_revision
Principle

Silence should not be treated as absence.

Silence may be a creator-defined boundary.

19. Suggested v0.2 Metadata Structure

The following is a possible structure for v0.2.

initial_friction:
  primary_friction_type: ethical_conflict

  secondary_friction_types:
    - cognitive_dissonance
    - social_friction

  friction_intensity: 0.78
  friction_state: structured

  disclosure_level: abstract_public

  public_friction_label: "ethical discomfort regarding AI interpretation and creator sovereignty"

  friction_unresolved: true

  friction_timeline:
    - event_type: emergence
      date: "2026-05-01"
    - event_type: articulation
      date: "2026-05-12"
    - event_type: structuring
      date: "2026-05-26"

  shadow_friction:
    present: true
    ai_inference_allowed: false

  silence_node:
    present: true
    reason_type: creator_boundary
    ai_inference_allowed: false
20. Relationship to Sovereignty Control

Friction Taxonomy defines what kind of friction exists.

Sovereignty Control defines how that friction may be accessed, interpreted, protected, or withheld.

The two documents should be read together.

Friction Taxonomy
= classification of origin pressure

Sovereignty Control Model
= access and interpretation control for that origin pressure

A friction record may be classified as ethical_conflict, but its raw content may still be private.

A friction record may be declared as raw_unresolved_friction, and AI may be explicitly forbidden from inferring its content.

21. Relationship to Consciousness Circle Structure

The friction taxonomy is one part of the larger Consciousness Circle.

Suggested conceptual flow:

initial_friction
↓
core_question
↓
meaning_structure
↓
visibility_scope
↓
sovereignty_control

Friction is not the final meaning.

It is the origin pressure that gives birth to a question.

22. Design Risks
22.1 Over-Classification

Too many categories may make the system rigid.

The taxonomy should remain minimal and extensible.

22.2 False Objectivity

Friction intensity and friction type are creator-declared signals.

They should not be treated as objective truth.

22.3 Privacy Leakage

Even abstract friction labels may reveal sensitive context.

Creators should be able to use private, encrypted, or shadow friction fields.

22.4 AI Over-Inference

AI systems may infer private meaning from partial signals.

This is why ai_inference_allowed and sovereignty control fields are necessary.

22.5 Exclusion of the Unarticulated

If the system only accepts fully structured friction, it excludes creators who are still in the pre-verbal stage.

The category raw_unresolved_friction exists to prevent this failure.

23. Future Extensions

Future versions may define:

formal JSON Schema definitions,
controlled vocabulary files,
friction intensity calibration notes,
examples for each friction type,
private friction hash references,
encrypted friction capsules,
relationship to temporal lineage,
relationship to dispute review,
multi-wing review examples,
AI compliance profile for friction handling.

Suggested future files:

examples/friction-bodily.example.yaml
examples/friction-ethical-conflict.example.yaml
examples/friction-raw-unresolved.example.yaml
examples/shadow-friction.example.yaml
examples/silence-node.example.yaml
24. Summary

Initial friction is the human pressure that gives birth to a question.

The Friction Taxonomy provides a minimal structure for describing that pressure without forcing creators to over-disclose private experience.

The purpose is not to classify the person.

The purpose is to preserve the origin of meaning.

The answer may be generated.
The question may be declared.
But the friction must be protected.

A mature Question OS must be able to record not only what has already become language, but also what still exists as discomfort, silence, shadow, and unresolved pressure.

That is where human-originated meaning begins.
