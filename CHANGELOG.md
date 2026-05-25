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


