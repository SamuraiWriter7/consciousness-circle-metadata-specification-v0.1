# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple versioning convention for early specification development:

```text
MAJOR.MINOR.PATCH
```

- `MAJOR` changes indicate incompatible structural changes.
- `MINOR` changes indicate new fields, documents, examples, or compatible extensions.
- `PATCH` changes indicate clarifications, documentation improvements, validation fixes, or minor editorial updates.

---

## [0.1.1] - 2026-05-25

### Added

- Added `docs/relationship-to-trace-protocol.md`.
- Added `docs/relationship-to-royalty-os.md`.
- Added `docs/rag-integration-notes.md`.

### Updated

- Updated `README.md` Repository Structure to include the new relationship and integration documents.
- Updated `README.md` Start Here section to include:
  - `docs/relationship-to-trace-protocol.md`
  - `docs/relationship-to-royalty-os.md`
  - `docs/rag-integration-notes.md`
- Updated `README.md` Future Extensions section to reflect new next-step candidates after the Trace / Royalty / RAG integration documents.

### Documentation

- Clarified the relationship between Consciousness Circle Metadata and Trace Protocol.
- Clarified that Consciousness Circle Metadata acts as a semantic pre-trace layer.
- Clarified that Trace Protocol records how content is referenced, reused, transformed, or connected.
- Clarified the relationship between Consciousness Circle Metadata and Royalty OS.
- Clarified that semantic depth is a signal, not automatic entitlement.
- Clarified that Royalty OS use must pass through trace review, dispute handling, and allocation-readiness review.
- Added RAG integration notes for meaning-aware retrieval.
- Added guidance for consent-aware retrieval, public output safety, metadata-aware ranking, and RAG trace logging.

### Core Concepts Added

- Semantic pre-trace layer
- Question trace
- Friction trace
- Context trace
- Structural trace
- Transformation trace
- Royalty-readiness signal layer
- Meaning-aware RAG
- Consent-aware retrieval
- RAG reference trace
- Safe-for-generation metadata handling

### Notes

This release extends the initial v0.1.0 specification by documenting how Consciousness Circle Metadata may connect to Trace Protocol, Royalty OS, and RAG systems.

No breaking schema changes were introduced in this release.

The core schema remains:

```text
schemas/consciousness-circle-metadata.schema.json
```

The main example remains:

```text
examples/note-article-consciousness-circle.sample.json
```

---

## [0.1.0] - 2026-05-25

### Added

- Initial release of the Consciousness Circle Metadata Specification.
- Added `schemas/consciousness-circle-metadata.schema.json`.
- Added `examples/note-article-consciousness-circle.sample.json`.
- Added `docs/field-definitions.md`.
- Added `docs/privacy-consent-and-human-review.md`.
- Added initial `README.md`.
- Added `LICENSE`.
- Added `CITATION.cff`.
- Added `CHANGELOG.md`.

### Core Concepts

- Defined the top-level metadata structure:

```text
schema_version
content_identity
consciousness_annotation
trace_governance
royalty_readiness
```

- Introduced the Consciousness Circle model:

```text
center
surface layer
deep layer
connections
rotation dynamics
```

- Defined `center` as the generative core of a content item, including:

```text
core_question
initial_friction
bodily_sensation
center_notes
```

- Defined `surface` as the fact-oriented layer for RAG-compatible retrieval.
- Defined `deep` as the contextual, interpretive, affective, and semantic layer.
- Defined `connections` to represent relationships between center, surface, and deep layers.
- Defined `rotation_dynamics` to describe semantic movement or transformation.

### Governance

- Added trace governance fields:

```text
annotation_method
review_status
consent_scope
human_final_edit
provenance_refs
dispute_ref
reviewer_notes
```

- Added privacy and consent principles for sensitive semantic metadata.
- Added human final edit principle.
- Added AI-inferred metadata handling rules.
- Added public exposure safeguards.
- Added RAG usage safeguards.
- Added royalty-readiness safeguards.
- Added anti-gaming flags.

### Royalty Readiness

- Added `royalty_readiness` as a signal layer only.
- Explicitly separated metadata annotation from automatic royalty allocation.
- Defined the correct flow:

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

### Notes

This release is a draft-level initial specification.

It does not claim to define consciousness itself.  
It defines a metadata layer for making the semantic structure behind content traceable, reviewable, and interoperable in AI-mediated knowledge ecosystems.

# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple versioning convention for early specification development:

```text
MAJOR.MINOR.PATCH
MAJOR changes indicate incompatible structural changes.
MINOR changes indicate new fields, documents, or compatible extensions.
PATCH changes indicate clarifications, examples, documentation improvements, or validation fixes.
[0.1.0] - 2026-05-25
Added
Initial release of the Consciousness Circle Metadata Specification.
Added schemas/consciousness-circle-metadata.schema.json.
Added examples/note-article-consciousness-circle.sample.json.
Added docs/field-definitions.md.
Added docs/privacy-consent-and-human-review.md.
Added initial README.md.
Added LICENSE.
Added CITATION.cff.
Added CHANGELOG.md.
Core Concepts
Defined the top-level metadata structure:
schema_version
content_identity
consciousness_annotation
trace_governance
royalty_readiness
Introduced the Consciousness Circle model:
center
surface layer
deep layer
connections
rotation dynamics
Defined center as the generative core of a content item, including:
core_question
initial_friction
bodily_sensation
center_notes
Defined surface as the fact-oriented layer for RAG-compatible retrieval.
Defined deep as the contextual, interpretive, affective, and semantic layer.
Defined connections to represent relationships between center, surface, and deep layers.
Defined rotation_dynamics to describe semantic movement or transformation.
Governance
Added trace governance fields:
annotation_method
review_status
consent_scope
human_final_edit
provenance_refs
dispute_ref
reviewer_notes
Added privacy and consent principles for sensitive semantic metadata.
Added human final edit principle.
Added AI-inferred metadata handling rules.
Added public exposure safeguards.
Added RAG usage safeguards.
Added royalty-readiness safeguards.
Added anti-gaming flags.
Royalty Readiness
Added royalty_readiness as a signal layer only.
Explicitly separated metadata annotation from automatic royalty allocation.
Defined the correct flow:
Consciousness Circle Metadata
↓
Trace review
↓
Allocation-readiness review
↓
Human or multi-wing judgment
↓
Possible royalty allocation
Notes

This release is a draft-level initial specification.

It does not claim to define consciousness itself.
It defines a metadata layer for making the semantic structure behind content traceable, reviewable, and interoperable in AI-mediated knowledge ecosystems.


