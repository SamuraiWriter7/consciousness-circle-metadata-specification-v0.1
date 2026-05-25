# Privacy, Consent, and Human Review

This document defines privacy, consent, and human review principles for the Consciousness Circle Metadata Specification v0.1.0.

The Consciousness Circle Metadata Specification may describe sensitive interpretive fields such as bodily sensation, emotional context, deep-layer meaning, friction, and creator intent.

For this reason, metadata must not be treated as neutral technical data only.  
It must be handled as human-centered semantic metadata that requires consent, visibility control, review, and the creator’s final editorial authority.

---

## 1. Core Principle

The core principle of this specification is:

```text
Do not extract inner meaning without consent.
Do not expose deep metadata without visibility control.
Do not convert semantic depth into automatic entitlement.
Do not override the creator’s final interpretation.

The metadata may support AI retrieval, trace governance, and allocation-readiness review, but it must not be used to define, judge, or profile the creator without human control.

This specification annotates the structure behind content.
It does not claim to capture the creator’s actual consciousness.

2. Sensitive Fields

The following fields may contain sensitive or semi-sensitive information:

consciousness_annotation.center.bodily_sensation
consciousness_annotation.center.initial_friction
consciousness_annotation.layers.deep.context
consciousness_annotation.layers.deep.affective_tags
consciousness_annotation.layers.deep.interpretive_summary
consciousness_annotation.layers.deep.personal_resolution
consciousness_annotation.rotation_dynamics.resonance_points
trace_governance.reviewer_notes
royalty_readiness.allocation_notes

These fields should be handled with additional care because they may describe:

embodied signals
emotional states
unresolved tensions
personal interpretation
philosophical commitments
creator intent
sensitive context
allocation-related judgment

Even when these fields are useful for RAG or trace review, they must not be exposed automatically.

3. Visibility Levels

The schema defines the following visibility levels:

private
restricted
platform
public
private

The field may be accessed only by the creator or a local/private system.

Recommended for:

bodily sensations
private emotional context
unpublished interpretive notes
early drafts
sensitive personal reflections
restricted

The field may be used in limited review workflows, controlled metadata processing, or trusted system-level analysis.

Recommended for:

human review
multi-wing review
allocation-readiness preparation
restricted RAG testing
privacy-preserving semantic analysis
platform

The field may be used internally by a platform, subject to platform policy and user consent.

Recommended for:

internal recommendation systems
platform-level semantic indexing
creator dashboards
controlled RAG enhancement
public

The field may be exposed publicly.

Recommended only for:

creator-approved summaries
public metadata
non-sensitive interpretive descriptions
documentation examples
intentionally published semantic annotations
4. Consent Scope

The trace_governance.consent_scope field defines how the metadata may be used.

Allowed values:

private
platform_internal
research
rag_reference
royalty_reference
public
Recommended Interpretation
Consent Scope	Meaning
private	Metadata may only be used by the creator or local/private tools.
platform_internal	Metadata may be used internally by the hosting platform.
research	Metadata may be used for research, analysis, or system evaluation.
rag_reference	Metadata may be used for AI retrieval, reference, or semantic indexing.
royalty_reference	Metadata may be considered in allocation-readiness review.
public	Metadata may be publicly exposed or indexed.

Consent scope should be explicit.
Systems must not infer broad consent from content publication alone.

Publishing an article does not automatically mean the creator has consented to expose deep-layer metadata.

5. Human Final Edit

The trace_governance.human_final_edit field is a core safeguard.

"human_final_edit": true

When human_final_edit is true, the creator or authorized human reviewer has final editorial authority over the metadata.

When human_final_edit is false, systems should treat the metadata as provisional.

Recommended Rule

If human_final_edit is false, the following fields should not be used for sensitive decisions:

bodily_sensation
deep.context
deep.affective_tags
deep.interpretive_summary
deep.personal_resolution
depth_signal_score
allocation_notes

AI-generated or automated metadata may be useful for drafting, but it must not override human interpretation.

6. AI-Inferred Metadata

AI may assist in generating metadata, but AI-inferred metadata must be clearly marked.

Relevant fields include:

trace_governance.annotation_method
consciousness_annotation.center.bodily_sensation.annotation_origin
royalty_readiness.scoring_method

Possible values include:

ai_assisted
automated
ai_inferred
ai_estimated
hybrid
Required Handling

AI-inferred metadata should be treated as provisional.

Systems should avoid language such as:

The creator felt...
The creator intended...
The creator's true emotion was...

Preferred language:

The metadata suggests...
The annotation indicates...
The system estimates...
The creator-approved metadata states...

AI must not claim authority over the creator’s inner state.

7. Bodily Sensation Handling

The bodily_sensation field is optional and should be opt-in.

"bodily_sensation": {
  "label": "胸の奥に残る圧迫感",
  "visibility": "restricted",
  "confidence": 0.82,
  "annotation_origin": "creator_provided"
}
Rules
Bodily sensation should not be required.
Creator-provided entries should be preferred over AI-inferred entries.
AI-inferred bodily sensation should not be public by default.
The field should not be used for psychological diagnosis.
The creator should be able to remove or revise it.
Public RAG systems should not expose it unless visibility is explicitly public.

This field exists to preserve the embodied origin of thought, not to profile the creator.

8. Deep Layer Handling

The deep layer may contain context, affective tags, interpretive summary, and personal resolution.

deep.context
deep.affective_tags
deep.interpretive_summary
deep.intensity
deep.visibility
deep.personal_resolution
Rules
Deep-layer metadata should be opt-in or creator-reviewable.
Deep-layer visibility should default to restricted or private.
Deep-layer metadata should not be publicly exposed by default.
AI-inferred deep-layer metadata should require human review before allocation use.
Deep-layer metadata should not be used for manipulation, persuasion targeting, or emotional exploitation.
Deep-layer metadata should not be treated as a psychological diagnosis.

The deep layer is designed to support meaningful retrieval and traceability, not behavioral control.

9. RAG Usage Safeguards

When used in RAG systems, this metadata can improve retrieval quality by enabling search through:

core questions
semantic depth
surface/deep relationships
resonance points
interpretive context
traceable knowledge structures

However, RAG systems must respect visibility and consent scope.

Recommended RAG Filter

RAG systems should check:

consent_scope = rag_reference OR consent_scope = public
review_status = reviewed
human_final_edit = true
field.visibility = public OR field.visibility = platform

For restricted or private fields, RAG systems should avoid direct exposure.

Safe RAG Output

Acceptable:

This article addresses the question of whether AI-referenced knowledge should remain uncompensated.

Risky:

The creator felt pressure in the chest and quiet anger when writing this article.

The first summarizes public semantic structure.
The second exposes sensitive deep-layer metadata.

10. Royalty Readiness Safeguards

The royalty_readiness object may support allocation-readiness review, but it must not trigger automatic royalty allocation.

Correct flow:

metadata annotation
↓
trace review
↓
allocation-readiness review
↓
human or multi-wing judgment
↓
possible royalty allocation

Incorrect flow:

high depth_signal_score
↓
automatic royalty increase
Required Safeguards

Before metadata influences allocation review, systems should verify:

human_final_edit = true
review_status = reviewed
requires_human_review = true
consent_scope = royalty_reference
anti_gaming_flags are reviewed

The metadata provides signals.
It does not create entitlement by itself.

11. Anti-Gaming Considerations

Semantic metadata can be gamed.

Possible risks include:

score_inflation
low_confidence_high_depth
missing_sources
unreviewed_ai_inference
privacy_sensitive_claim
contradictory_metadata
other
Examples
Risk	Description
score_inflation	Metadata assigns artificially high depth, intensity, or resonance scores.
low_confidence_high_depth	A high depth score is paired with low confidence.
missing_sources	Surface facts lack adequate references.
unreviewed_ai_inference	AI-inferred metadata has not been reviewed.
privacy_sensitive_claim	Metadata includes sensitive inner-state claims.
contradictory_metadata	Fields conflict with each other.

Anti-gaming flags should not automatically invalidate metadata.
They should trigger review.

12. Review Status

The trace_governance.review_status field defines the current review state.

Allowed values:

draft
reviewed
disputed
deprecated
superseded
Recommended Usage
Status	Meaning
draft	Metadata is not finalized.
reviewed	Metadata has been reviewed and may be used within its consent scope.
disputed	Metadata is challenged or under review.
deprecated	Metadata should no longer be used.
superseded	Metadata has been replaced by a newer record.
Rule

Only reviewed metadata should be used for royalty-readiness workflows.

draft, disputed, deprecated, or superseded metadata should not influence allocation decisions without additional review.

13. Dispute Handling

Metadata may be disputed when:

the creator disagrees with AI-inferred interpretation
a reviewer finds the metadata misleading
deep-layer fields expose sensitive information
scores appear inflated or inconsistent
provenance references are insufficient
allocation-related use is contested

When disputed, the metadata should be marked:

"review_status": "disputed"

If available, an external dispute registry may be referenced:

"dispute_ref": "dispute:example:metadata_001"
Recommended Dispute Flow
metadata challenged
↓
review_status = disputed
↓
sensitive use paused
↓
creator or authorized reviewer examines fields
↓
metadata revised, deprecated, or reaffirmed

Dispute handling should preserve creator agency while allowing systems to maintain auditability.

14. Creator Rights

Creators should retain the ability to:

View generated metadata.
Edit metadata.
Remove sensitive fields.
Change visibility levels.
Restrict consent scope.
Mark metadata as disputed.
Replace metadata with a newer version.
Opt out of royalty-reference use.
Request deletion or deprecation where applicable.
Prevent AI-inferred inner-state claims from being presented as facts.

These rights are especially important for bodily sensation and deep-layer fields.

15. Public Exposure Rules

Public exposure should follow the minimum necessary principle.

Before exposing metadata publicly, systems should check:

field.visibility = public
consent_scope = public
human_final_edit = true
review_status = reviewed

If these conditions are not met, systems should expose only a reduced public summary.

Example Public Summary
This content explores the question of how AI-referenced knowledge should be traced and reviewed for possible value return.
Fields Generally Unsafe for Public Exposure by Default
bodily_sensation
deep.personal_resolution
reviewer_notes
allocation_notes
anti_gaming_flags
private provenance details
16. Platform Responsibilities

Platforms that adopt this specification should provide:

Clear metadata visibility controls.
Creator review interface.
Consent scope settings.
AI-generated field labeling.
Ability to edit or remove deep metadata.
Dispute status workflow.
Provenance and audit references.
Restricted access controls for sensitive fields.
Clear separation between RAG usage and royalty-readiness usage.
Documentation explaining how metadata is used.

Platforms should not bury consent inside vague terms of service.

Deep semantic metadata requires clear and specific user control.

17. Multi-Wing Review

For high-impact use cases, metadata may be reviewed through multi-wing review.

Multi-wing review may include:

creator self-review
AI-assisted review
human reviewer
domain expert
trace reviewer
allocation-readiness reviewer
multiple model perspectives

The purpose of multi-wing review is not to create automatic truth.
It is to reduce unilateral interpretation and improve review quality.

Recommended Use Cases

Multi-wing review is recommended when metadata is used for:

royalty_reference
public exposure
dispute handling
high-depth scoring
allocation-readiness review
cross-platform trace mapping
18. Minimal Safe Implementation

A minimal safe implementation should include:

visibility controls
consent_scope
human_final_edit
review_status
annotation_method
provenance_refs
anti_gaming_flags

A platform or repository should not adopt deep-layer metadata without these safeguards.

Minimal Safe Metadata Example
{
  "trace_governance": {
    "annotation_method": "ai_assisted",
    "review_status": "draft",
    "consent_scope": "private",
    "human_final_edit": true,
    "provenance_refs": [
      "trace:example_content_001"
    ]
  },
  "royalty_readiness": {
    "eligible_for_allocation_review": false,
    "depth_signal_score": 0.0,
    "requires_human_review": true,
    "anti_gaming_flags": [
      "unreviewed_ai_inference"
    ]
  }
}
19. Recommended Defaults

For newly generated metadata, recommended defaults are:

review_status = draft
consent_scope = private
human_final_edit = true
deep.visibility = restricted
bodily_sensation.visibility = private
eligible_for_allocation_review = false
requires_human_review = true

These defaults prioritize creator control and reduce accidental exposure.

The creator or authorized reviewer may later expand consent scope.

20. Non-Goals

This specification is not intended to:

diagnose the creator
profile the creator psychologically
infer hidden motives as facts
manipulate readers
optimize emotional targeting
automatically allocate royalties
prove legal authorship
replace human review
expose private interpretive metadata by default

The specification is designed to make meaning more traceable, not to make human interiority extractable.

21. Summary

Privacy, consent, and human review are not optional additions to the Consciousness Circle Metadata Specification.

They are part of the core architecture.

This metadata can help AI systems understand content more deeply, but deep understanding without consent becomes extraction.

The correct goal is:

richer retrieval
traceable meaning
creator agency
reviewable allocation signals
privacy-preserving semantic metadata

The incorrect goal is:

automatic inner-state extraction
uncontrolled emotional metadata
score-based entitlement
public exposure without consent
platform capture of deep creator context

The Consciousness Circle Metadata Specification should therefore be implemented as a human-centered metadata layer, not as an automated consciousness-mining system.
