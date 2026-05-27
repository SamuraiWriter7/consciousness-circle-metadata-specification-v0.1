# Changelog

All notable changes to this project will be documented in this file.

This project follows a documentation-first specification development process.  
Schema changes, example additions, validation workflows, and conceptual design notes are tracked separately when appropriate.

---

## [0.2.0] - 2026-05-27

### Added

- Added `schemas/consciousness-circle-metadata-v0.2.schema.json`.
  - Defines the v0.2 JSON Schema for the proposed Question OS object model.
  - Validates v0.2 metadata objects using JSON Schema Draft 2020-12.
  - Introduces schema-level support for:
    - `circle`
    - `proto_friction`
    - `initial_friction`
    - `meaning_structure`
    - `meaning_boundary`
    - `visibility_scope`
    - `circle_layers`
    - `sovereignty_control`
    - `temporal_relationship`
    - `sub_circles`
    - `silence_node`
    - `privacy_and_consent`
    - `rag_usage_policy`
    - `royalty_readiness`

- Added `scripts/validate-v0.2-examples.py`.
  - Validates the v0.2 JSON Schema itself.
  - Parses the v0.2 reference specification YAML.
  - Validates all current v0.2 YAML examples against the v0.2 schema.

- Added `.github/workflows/validate-v0.2-examples.yml`.
  - Runs v0.2 schema and example validation on GitHub Actions.
  - Triggers on changes to the v0.2 schema, v0.2 spec, v0.2 examples, validation script, or workflow file.
  - Supports manual execution through `workflow_dispatch`.

### Changed

- Updated `README.md` to reflect the validated v0.2 draft status.
- Updated the README `Current Status` section.
- Updated the README `Repository Structure` section to include:
  - `schemas/consciousness-circle-metadata-v0.2.schema.json`
  - `scripts/validate-v0.2-examples.py`
  - `.github/workflows/validate-v0.2-examples.yml`
- Updated the README `Key Files` and `Key Documents` sections.
- Updated the README `Schema` section to distinguish between:
  - the original v0.1-style schema,
  - the new v0.2 JSON Schema.
- Updated the README `Validation` section to include local validation and GitHub Actions validation.
- Updated the README `Status` section to clarify that v0.2 is now a validated draft specification.

### Fixed

- Fixed `spec/consciousness-circle-metadata-specification-v0.2.yaml` so it is parsed as a single YAML document.
  - Removed YAML document separators (`---`) that caused `yaml.safe_load()` to fail.
  - The v0.2 reference specification now parses correctly in the validation script.

- Fixed the v0.2 schema to allow `circle.silence_node`.
  - This aligns the schema with `examples/silence-node-v0.2.example.yaml`.
  - The silence node example now validates successfully.

### Validated

The following files now validate successfully through the v0.2 validation workflow:

```text
schemas/consciousness-circle-metadata-v0.2.schema.json
spec/consciousness-circle-metadata-specification-v0.2.yaml
examples/minimal-circle-v0.2.example.yaml
examples/extended-circle-v0.2.example.yaml
examples/proto-friction-v0.2.example.yaml
examples/silence-node-v0.2.example.yaml

Successful validation output includes:

OK: Schema is valid JSON Schema Draft 2020-12: schemas/consciousness-circle-metadata-v0.2.schema.json
OK: Spec YAML parsed: spec/consciousness-circle-metadata-specification-v0.2.yaml
OK: Example validates: examples/minimal-circle-v0.2.example.yaml
OK: Example validates: examples/extended-circle-v0.2.example.yaml
OK: Example validates: examples/proto-friction-v0.2.example.yaml
OK: Example validates: examples/silence-node-v0.2.example.yaml

All v0.2 examples validated successfully.
Clarified
Clarified that v0.2 is a validated draft specification.
Clarified that v0.2 now includes:
reference specification,
JSON Schema,
validated YAML examples,
CI-based validation.
Clarified that v0.2 remains a draft and does not yet define runtime enforcement.
Clarified that metadata-level sovereignty controls require downstream runtime, audit, and review systems for practical compliance.
Clarified that silence_node is a valid circle-level boundary structure.
Clarified that creator-defined silence should not be treated as missing data or permission for AI inference.
Clarified the current project progression:
v0.1.x
= initial metadata schema and documentation

v0.2.0 draft
= reference specification + JSON Schema + validated examples

future v0.3
= runtime control, audit, semantic brake enforcement, and integration profiles
Notes

This release marks the transition of v0.2 from a reference-only draft into a validated draft specification.

It does not claim that runtime enforcement is complete.

The v0.2 schema validates structure.
It does not enforce AI behavior by itself.

The core principle remains:

Metadata defines the structure.
Runtime systems enforce behavior.
Audit systems provide accountability.
Review systems handle disputes.
[0.1.3] - 2026-05-26
Added
Added spec/consciousness-circle-metadata-specification-v0.2.yaml.
Introduces the v0.2 draft reference specification.
Defines the proposed object model for the structured Question OS layer.
Adds proposed top-level sections including:
schema_version
content_identity
circle
trace_governance
privacy_and_consent
rag_usage_policy
royalty_readiness
Introduces controlled vocabularies for friction types, visibility scope, circle lifecycle, proto-friction states, sovereignty controls, inference boundaries, and violation behavior.
Defines minimal, standard, and extended conformance profiles.
Added examples/minimal-circle-v0.2.example.yaml.
Demonstrates a minimal v0.2-compatible circle profile.
Includes core question, initial friction, meaning structure, visibility scope, sovereignty control, trace governance, privacy controls, RAG usage policy, and royalty-readiness safeguards.
Added examples/extended-circle-v0.2.example.yaml.
Demonstrates an extended v0.2 circle profile.
Includes proto-friction, vibration logs, shadow friction, silence nodes, circle layers, meaning boundaries, temporal relationships, recursive sub-circles, sovereignty control, and royalty-readiness notes.
Added examples/proto-friction-v0.2.example.yaml.
Demonstrates how pre-question pressure may be represented.
Includes proto-friction, vibration logs, shadow friction, silence nodes, protected ambiguity, and strict AI inference boundaries.
Added examples/silence-node-v0.2.example.yaml.
Demonstrates how creator-defined silence may be declared as a boundary.
Clarifies that silence should not be treated as missing data or permission for AI inference.
Changed
Updated README.md to reflect the new v0.2 draft reference materials.
Added spec/ to the repository structure.
Added v0.2 example files to the repository structure.
Updated the README reading order to include:
spec/consciousness-circle-metadata-specification-v0.2.yaml
examples/minimal-circle-v0.2.example.yaml
examples/extended-circle-v0.2.example.yaml
examples/proto-friction-v0.2.example.yaml
examples/silence-node-v0.2.example.yaml
Updated the README Key Documents, v0.2 Reference Specification, v0.2 Examples, Validation, Status, and Future Extensions sections.
Clarified
Clarified that v0.2 is currently a draft reference specification, not yet a finalized JSON Schema.
Clarified that the current machine-readable schema remains the v0.1-style schema located at:
schemas/consciousness-circle-metadata.schema.json
Clarified that the v0.2 YAML examples are reference examples and are not yet backed by a complete v0.2 JSON Schema.
Clarified the current project status:
v0.1.x
= initial metadata schema and documentation

v0.2 draft
= reference specification plus examples

future v0.2 schema
= formal machine-validation layer for the v0.2 object model
Clarified that metadata existence does not equal permission for AI systems to summarize, infer, transform, or expose private creator-defined structures.
Clarified that proto-friction, shadow friction, and silence nodes should remain private or protected by default.
Clarified that sovereignty control declarations require runtime enforcement, audit, and review layers for practical compliance.
Notes

This release adds the v0.2 draft reference specification and example set.

No finalized v0.2 JSON Schema is included in this release.

No breaking validation changes are introduced to the existing v0.1-style schema.

The existing schema remains:

schemas/consciousness-circle-metadata.schema.json

The new draft reference specification is:

spec/consciousness-circle-metadata-specification-v0.2.yaml

The new v0.2 reference examples are:

examples/minimal-circle-v0.2.example.yaml
examples/extended-circle-v0.2.example.yaml
examples/proto-friction-v0.2.example.yaml
examples/silence-node-v0.2.example.yaml

Future work may formalize the v0.2 object model into:

schemas/consciousness-circle-metadata-v0.2.schema.json
[0.1.2] - 2026-05-26
Added
Added docs/sovereignty-control-model.md.
Defines the sovereignty control layer for creator-defined meaning boundaries.
Introduces multi-circle access control, temporal lineage control, friction encapsulation, and semantic brake concepts.
Clarifies that metadata-level control requires runtime enforcement, audit, and review layers for practical compliance.
Added docs/friction-taxonomy.md.
Defines an initial taxonomy for initial_friction.
Introduces friction types such as:
bodily_friction
daily_life_friction
social_friction
cognitive_dissonance
ethical_conflict
raw_unresolved_friction
Adds design notes for friction intensity, friction state, friction timelines, disclosure levels, shadow friction, and silence nodes.
Added docs/circle-structure-model.md.
Defines the Consciousness Circle as a layered and recursive meaning structure.
Introduces core, inner, and outer layers.
Defines circle depth, visibility scope, circle openness, recursive sub-circles, meaning boundaries, silence nodes, lifecycle states, and temporal relationships.
Provides a possible v0.2 circle structure.
Added docs/proto-friction-layer.md.
Defines the pre-question layer before initial_friction.
Introduces proto-friction, shadow friction, vibration logs, silence nodes, and transition records from proto-friction to structured friction.
Clarifies that pre-verbal, incomplete, or private meaning pressure should not be erased or forcibly classified.
Changed
Updated README.md to reflect the expanded documentation structure.
Added the v0.2 design direction to the README.
Added the new documentation files to:
Repository Structure
Start Here
Key Documents
Future Extensions
Status
Summary
Clarified
Clarified that the current v0.1 series remains the minimum metadata layer.
Clarified that the new documents represent the v0.2 design path, not a finalized v0.2 schema.
Clarified the conceptual progression:
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


