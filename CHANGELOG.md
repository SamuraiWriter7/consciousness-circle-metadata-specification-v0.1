# Changelog

All notable changes to this project will be documented in this file.

This project follows a documentation-first specification development process.  
Schema changes, example additions, and conceptual design notes are tracked separately when appropriate.

---

## [0.1.2] - 2026-05-26

### Added

- Added `docs/sovereignty-control-model.md`.
  - Defines the sovereignty control layer for creator-defined meaning boundaries.
  - Introduces multi-circle access control, temporal lineage control, friction encapsulation, and semantic brake concepts.
  - Clarifies that metadata-level control requires runtime enforcement, audit, and review layers for practical compliance.

- Added `docs/friction-taxonomy.md`.
  - Defines an initial taxonomy for `initial_friction`.
  - Introduces friction types such as:
    - `bodily_friction`
    - `daily_life_friction`
    - `social_friction`
    - `cognitive_dissonance`
    - `ethical_conflict`
    - `raw_unresolved_friction`
  - Adds design notes for friction intensity, friction state, friction timelines, disclosure levels, shadow friction, and silence nodes.

- Added `docs/circle-structure-model.md`.
  - Defines the Consciousness Circle as a layered and recursive meaning structure.
  - Introduces core, inner, and outer layers.
  - Defines circle depth, visibility scope, circle openness, recursive sub-circles, meaning boundaries, silence nodes, lifecycle states, and temporal relationships.
  - Provides a possible v0.2 circle structure.

- Added `docs/proto-friction-layer.md`.
  - Defines the pre-question layer before `initial_friction`.
  - Introduces proto-friction, shadow friction, vibration logs, silence nodes, and transition records from proto-friction to structured friction.
  - Clarifies that pre-verbal, incomplete, or private meaning pressure should not be erased or forcibly classified.

### Changed

- Updated `README.md` to reflect the expanded documentation structure.
- Added the v0.2 design direction to the README.
- Added the new documentation files to:
  - Repository Structure
  - Start Here
  - Key Documents
  - Future Extensions
  - Status
  - Summary

### Clarified

- Clarified that the current v0.1 series remains the minimum metadata layer.
- Clarified that the new documents represent the v0.2 design path, not a finalized v0.2 schema.
- Clarified the conceptual progression:

```text
v0.1
= minimum Consciousness Circle metadata

v0.2 design path
= structured Question OS layer

v0.3 and beyond
= runtime control, audit, RAG policy, trace integration, and review systems

Clarified that sovereignty control should not be treated as enforcement by metadata alone.
Clarified that creator-defined silence should be treated as a boundary, not missing data.
Clarified that proto-friction is optional and should remain private by default.
Clarified that friction taxonomy is intended to classify origin pressure, not the creator.
Notes

This release is documentation-only.

No schema-breaking changes were introduced.

The existing schema remains:

schemas/consciousness-circle-metadata.schema.json

The existing example remains:

examples/note-article-consciousness-circle.sample.json

Future versions may formalize the v0.2 design path into schema fields such as:

visibility_scope
sovereignty_control
proto_friction
shadow_friction
silence_node
circle_lifecycle
temporal_relationship
[0.1.1] - 2026-05-25
Added
Added docs/relationship-to-trace-protocol.md.
Explains how Consciousness Circle Metadata relates to semantic trace workflows.
Defines the metadata as a semantic pre-trace layer.
Added docs/relationship-to-royalty-os.md.
Explains how Consciousness Circle Metadata may support Royalty OS review.
Clarifies that metadata does not directly trigger royalty allocation.
Added docs/rag-integration-notes.md.
Explains how RAG systems may use the metadata for question-centered and meaning-aware retrieval.
Includes consent, visibility, and human-review considerations.
Changed
Updated README.md to include the new relationship and integration documents.
Updated the repository structure and recommended reading order.
Clarified
Clarified that Consciousness Circle Metadata is not an automatic allocation engine.
Clarified the separation between:
semantic annotation,
trace review,
allocation-readiness review,
possible royalty allocation.
[0.1.0] - 2026-05-25
Added
Initial release of the Consciousness Circle Metadata Specification.
Added schemas/consciousness-circle-metadata.schema.json.
Added examples/note-article-consciousness-circle.sample.json.
Added docs/field-definitions.md.
Added docs/privacy-consent-and-human-review.md.
Added README.md.
Added LICENSE.
Added CITATION.cff.
Added CHANGELOG.md.
Defined
Core metadata structure for annotating:
content identity,
core question,
initial friction,
surface facts,
deep context,
layer connections,
rotation dynamics,
trace governance,
royalty-readiness signals.
Established
Human review principle.
Creator-controlled deep metadata principle.
Privacy and consent safeguards.
Anti-gaming safeguards.
Allocation-readiness separation principle.
Initial Scope

The initial version focuses on defining a metadata layer for human-originated meaning structures in AI-mediated knowledge ecosystems.

It does not attempt to:

prove legal authorship,
diagnose creators,
infer hidden motives as facts,
automatically allocate royalties,
replace human review,
define consciousness scientifically or metaphysically,
define a complete RAG architecture,
define a complete Trace Protocol schema,
define a complete Royalty OS payment engine.


