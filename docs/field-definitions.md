# Field Definitions

This document defines the fields used in the Consciousness Circle Metadata Specification v0.1.0.

The purpose of this specification is to describe the question, friction, surface facts, deep context, relational dynamics, trace governance, and allocation-readiness of a content item.

This metadata does not claim to store consciousness itself.  
It annotates the structure behind a piece of content: the question that generated it, the friction that shaped it, the surface facts it refers to, and the deeper interpretive context that gives it meaning.

---

## 1. Top-Level Structure

```json
{
  "schema_version": "0.1.0",
  "content_identity": {},
  "consciousness_annotation": {},
  "trace_governance": {},
  "royalty_readiness": {}
}

The metadata object is divided into four major sections.

Field	Required	Description
schema_version	Yes	Version of this metadata schema.
content_identity	Yes	Identifies the content item being annotated.
consciousness_annotation	Yes	Describes the question, friction, surface/deep layers, and circular dynamics of the content.
trace_governance	Yes	Defines annotation method, consent scope, review status, and provenance references.
royalty_readiness	Yes	Indicates whether this metadata may be considered for allocation-readiness review.
2. schema_version
"schema_version": "0.1.0"

The version of the Consciousness Circle Metadata Schema.

For this release, the value must be:

"0.1.0"

This field allows future versions of the specification to evolve without breaking earlier metadata records.

3. content_identity

The content_identity object identifies the content item being annotated.

"content_identity": {
  "content_id": "note_article_2026_001",
  "content_type": "article",
  "platform": "note",
  "version": "1.0",
  "timestamp": "2026-05-25T10:00:00+09:00",
  "creator_id": "did:example:creator:shidenkai-alpha",
  "language": "ja-JP",
  "canonical_url": "https://example.com/note/articles/note_article_2026_001"
}
Fields
Field	Required	Description
content_id	Yes	Unique identifier of the content item on the source platform.
content_type	Yes	Type of the content item.
platform	Yes	Source platform or publication environment.
version	Yes	Version of the content item or annotation target.
timestamp	Yes	Creation or update timestamp of this metadata record.
creator_id	Yes	Creator identifier, such as a hash, DID, platform ID, or pseudonymous ID.
language	No	Language code of the content item.
canonical_url	No	Canonical URL of the content item.
content_type

Allowed values:

article
essay
note
book_section
social_post
repository_document
dataset_entry
other

Use article for general long-form articles.
Use note only when the platform-specific nature of the content is important.

4. consciousness_annotation

The consciousness_annotation object is the core of this specification.

It describes the circular structure behind the content:

center
↓
surface layer
↓
deep layer
↓
connections
↓
rotation dynamics

This structure allows AI-mediated retrieval systems to understand not only what a content item says, but also what question, friction, and interpretive movement generated it.

"consciousness_annotation": {
  "center": {},
  "layers": {},
  "connections": [],
  "rotation_dynamics": {}
}
5. center

The center object defines the generative core of the content.

It is the “epicenter” of the article, essay, post, or document.

"center": {
  "core_question": "AIに読まれる知識は、無料素材のままでよいのか？",
  "initial_friction": "AIが人間の記事や思想を参照して価値を生成しているにもかかわらず、その痕跡や還元構造が十分に整備されていないことへの違和感。",
  "bodily_sensation": {},
  "center_notes": "この記事の震源は、AI時代における知識参照・痕跡・価値還元の非対称性にある。"
}
Fields
Field	Required	Description
core_question	Yes	Central question or generative inquiry behind the content.
initial_friction	Yes	Initial friction, discrepancy, discomfort, or unresolved tension that triggered the content.
bodily_sensation	No	Optional bodily or affective signal associated with the content.
center_notes	No	Optional notes about the center of the consciousness circle.
core_question

The core_question should be written as a clear question whenever possible.

Good examples:

AIに読まれる知識は、無料素材のままでよいのか？
AI時代に、創作者の痕跡はどのように記録されるべきか？
なぜ単体AIではなく、群知能が重要になるのか？

Avoid vague labels such as:

AIについて
印税OS
最近考えたこと

The field should capture the generative question, not merely the topic.

initial_friction

The initial_friction field describes the first tension that led to the content.

It may include:

a contradiction
a discomfort
a structural gap
a social imbalance
a technical limitation
an unresolved question

This field replaces stronger terms such as violation in order to avoid implying legal or moral accusation by default.

6. bodily_sensation

The bodily_sensation object describes an optional embodied signal associated with the content.

This field is sensitive and should remain optional.

"bodily_sensation": {
  "label": "胸の奥に残る圧迫感と、構造がまだ閉じていない感覚",
  "visibility": "restricted",
  "confidence": 0.82,
  "annotation_origin": "creator_provided"
}
Fields
Field	Required	Description
label	Yes	Human-readable label of the bodily sensation.
visibility	Yes	Visibility scope of this field.
confidence	Yes	Confidence level of the annotation.
annotation_origin	No	Origin of the annotation.
visibility

Allowed values:

private
restricted
platform
public

Recommended usage:

Value	Meaning
private	Only the creator or local system may access it.
restricted	May be used for limited review or controlled metadata processing.
platform	May be used internally by the platform.
public	May be exposed publicly.
annotation_origin

Allowed values:

creator_provided
ai_assisted
ai_inferred
reviewer_added

Important rule:

If this field is inferred by AI, systems should avoid presenting it as a confirmed inner state of the creator.

AI may assist with annotation, but it must not claim authority over the creator’s internal experience.

7. layers

The layers object contains two primary layers:

"layers": {
  "surface": {},
  "deep": {}
}
Layer	Description
surface	Fact-oriented, externally checkable, or source-based layer.
deep	Contextual, interpretive, affective, or philosophical layer.

This distinction allows RAG systems to retrieve content not only by factual similarity, but also by depth, context, and question structure.

8. surface

The surface layer describes facts, references, observations, and externally checkable statements.

"surface": {
  "facts": [],
  "certainty_level": 0.84,
  "surface_summary": "AI時代には、知識が読まれるだけでなく、AIによって参照・再構成・再配布される。"
}
Fields
Field	Required	Description
facts	Yes	List of fact-oriented statements.
certainty_level	Yes	Overall certainty level of the surface layer.
surface_summary	No	Optional summary of the surface-level factual layer.
certainty_level

A normalized score from 0.0 to 1.0.

Range	Meaning
0.0 - 0.3	Low certainty
0.3 - 0.7	Moderate certainty
0.7 - 1.0	High certainty

This score should reflect the reliability of the surface layer, not the emotional strength of the content.

9. fact_item

Each item in surface.facts describes one factual or externally checkable statement.

{
  "statement": "AI検索やRAGシステムは、Web上の記事、論文、ニュース、投稿などを参照して回答を生成する。",
  "source_ref": "internal_trace:rag_observation_001",
  "certainty_level": 0.9,
  "source_type": "internal_trace"
}
Fields
Field	Required	Description
statement	Yes	Factual or externally checkable statement.
source_ref	No	Source reference, URL, citation key, platform reference, or internal trace ID.
certainty_level	Yes	Confidence in the factual statement.
source_type	No	Type of the source reference.
source_type

Allowed values:

url
citation
platform_reference
internal_trace
self_report
unknown

Use internal_trace when the source is an internal log, trace object, repository artifact, or previously defined evidence object.

Use self_report when the statement is based on the creator’s own observation or account.

10. deep

The deep layer describes the interpretive and contextual depth of the content.

"deep": {
  "context": "この記事は、AI検索・RAG・note記事・印税OS・痕跡管理の交差点にある。",
  "affective_tags": [
    "違和感",
    "構造的緊張",
    "知的フェアトレード"
  ],
  "interpretive_summary": "このコンテンツの深層には、創作者の問い・震源・構造的貢献が不可視化されることへの抵抗がある。",
  "intensity": 0.88,
  "visibility": "restricted",
  "personal_resolution": "AIによる参照を拒絶するのではなく、痕跡と還元の仕組みを整える。"
}
Fields
Field	Required	Description
context	Yes	Contextual, historical, philosophical, personal, or interpretive background.
affective_tags	Yes	Emotional, semantic, or affective tags associated with the deep layer.
interpretive_summary	Yes	Summary of the deeper meaning formation behind the content.
intensity	Yes	Strength of the deep-layer signal.
visibility	Yes	Visibility scope of the deep layer.
personal_resolution	No	Optional statement of how the creator reframes or resolves the tension.
affective_tags

These tags should not be used as psychological diagnosis.

They are semantic-affective annotations, not medical or personality labels.

Good examples:

違和感
構造的緊張
共鳴
問いの保護
制度化への意志
静かな怒り

Avoid:

病名
断定的な人格評価
攻撃的なレッテル
intensity

A normalized score from 0.0 to 1.0.

This score represents the strength of the deep-layer signal.

It should not be used as a direct measure of truth, quality, or royalty entitlement.

11. connections

The connections array describes relationships between the center, surface layer, and deep layer.

"connections": [
  {
    "from": "surface",
    "to": "deep",
    "relation_type": "transformation",
    "strength": 0.84,
    "confidence": 0.79,
    "description": "技術的な参照問題が、創作者の問いや思想の不可視化という深層問題へ変換されている。"
  }
]
Fields
Field	Required	Description
from	Yes	Source node of the connection.
to	Yes	Target node of the connection.
relation_type	Yes	Type of relationship between the nodes.
strength	Yes	Strength of the relationship.
confidence	Yes	Confidence in the relationship annotation.
description	No	Human-readable explanation of the connection.
Nodes

Allowed values:

center
surface
deep
relation_type

Allowed values:

tension
resonance
transformation
contradiction
clarification
amplification
suppression
contextualization

Recommended interpretation:

Type	Meaning
tension	Two nodes are in unresolved tension.
resonance	Two nodes reinforce or echo each other.
transformation	One node is transformed into another level of meaning.
contradiction	Two nodes conflict or negate each other.
clarification	One node clarifies another.
amplification	One node strengthens another.
suppression	One node suppresses, hides, or weakens another.
contextualization	One node provides context for another.
12. rotation_dynamics

The rotation_dynamics object describes the dynamic movement of the consciousness circle.

"rotation_dynamics": {
  "dominant_axis": "question",
  "resonance_points": [
    "AI検索",
    "RAG",
    "Trace",
    "Royalty OS"
  ],
  "openness_score": 0.74,
  "rotation_notes": "この意識構造丸は、批判から制度設計へ、違和感から仕様化へと回転している。"
}
Fields
Field	Required	Description
dominant_axis	Yes	Primary axis driving the content’s movement.
resonance_points	Yes	Keywords, concepts, or semantic nodes that act as resonance points.
openness_score	Yes	Degree to which the content remains open to external input or reinterpretation.
rotation_notes	No	Optional notes about dynamic movement or transformation.
dominant_axis

Allowed values:

question
bodily
friction
fact
context
relation
unknown
openness_score

A normalized score from 0.0 to 1.0.

Range	Meaning
0.0 - 0.3	Closed or highly fixed interpretation
0.3 - 0.7	Moderately open
0.7 - 1.0	Highly open to external resonance, reinterpretation, or extension

This score should not be interpreted as quality.
A closed structure may be appropriate for formal definitions, while an open structure may be appropriate for exploratory essays.

13. trace_governance

The trace_governance object defines how the metadata was created, reviewed, consented to, and linked to provenance records.

"trace_governance": {
  "annotation_method": "ai_assisted",
  "review_status": "draft",
  "consent_scope": "royalty_reference",
  "human_final_edit": true,
  "provenance_refs": [
    "trace:note_article_2026_001"
  ],
  "reviewer_notes": "Deep-layer fields should remain opt-in and editable by the creator."
}
Fields
Field	Required	Description
annotation_method	Yes	Method used to create or update the metadata.
review_status	Yes	Current review status of the metadata.
consent_scope	Yes	Scope of permitted use.
human_final_edit	Yes	Whether a human has final editorial control.
provenance_refs	Yes	References to provenance records, trace IDs, hashes, or audit logs.
dispute_ref	No	Optional reference to an external dispute registry entry.
reviewer_notes	No	Optional notes from a human or multi-wing reviewer.
annotation_method

Allowed values:

human
ai_assisted
automated
multi_wing_review

Recommended usage:

Value	Meaning
human	Created directly by a human.
ai_assisted	AI assisted but a human may review or edit.
automated	Generated automatically without human editing.
multi_wing_review	Reviewed by multiple models, agents, reviewers, or perspectives.
review_status

Allowed values:

draft
reviewed
disputed
deprecated
superseded
Value	Meaning
draft	Not finalized.
reviewed	Reviewed and accepted for current use.
disputed	Under dispute or challenge.
deprecated	No longer recommended for use.
superseded	Replaced by a newer metadata record.
consent_scope

Allowed values:

private
platform_internal
research
rag_reference
royalty_reference
public

Recommended interpretation:

Value	Meaning
private	Only the creator or local environment may use it.
platform_internal	Platform may use it internally.
research	May be used for research or analysis.
rag_reference	May be used for AI retrieval and reference.
royalty_reference	May be considered in allocation-readiness review.
public	May be publicly exposed.
human_final_edit

This field must be treated as a core governance safeguard.

If human_final_edit is false, systems should not use deep-layer or bodily-sensation fields for sensitive decisions.

14. royalty_readiness

The royalty_readiness object indicates whether this metadata may be considered for allocation-readiness review.

It does not trigger automatic royalty allocation.

"royalty_readiness": {
  "eligible_for_allocation_review": true,
  "depth_signal_score": 0.83,
  "requires_human_review": true,
  "scoring_method": "hybrid",
  "allocation_notes": "This metadata may support allocation-readiness review, but must not trigger automatic royalty allocation.",
  "anti_gaming_flags": [
    "unreviewed_ai_inference"
  ]
}
Fields
Field	Required	Description
eligible_for_allocation_review	Yes	Whether the metadata may be considered for allocation-readiness review.
depth_signal_score	Yes	Signal score indicating semantic or interpretive depth.
requires_human_review	Yes	Whether human or multi-wing review is required before allocation use.
scoring_method	No	Method used to assign the depth signal score.
allocation_notes	No	Notes about possible allocation-readiness use.
anti_gaming_flags	No	Flags for possible gaming, inflation, inconsistency, or suspicious scoring patterns.
Important Principle

This section must not be used as an automatic payment trigger.

The correct flow is:

metadata annotation
↓
trace review
↓
allocation-readiness review
↓
human or multi-wing judgment
↓
possible royalty allocation

The metadata provides signals.
It does not produce entitlement by itself.

15. depth_signal_score

The depth_signal_score field is a normalized score from 0.0 to 1.0.

It may reflect:

semantic depth
originality of question structure
traceable relation between surface and deep layers
strength of interpretive transformation
resonance between center and deep layer

It must not be treated as:

proof of authorship
proof of originality
proof of legal entitlement
automatic royalty multiplier
psychological evaluation

Recommended interpretation:

Range	Meaning
0.0 - 0.3	Low depth signal
0.3 - 0.7	Moderate depth signal
0.7 - 1.0	Strong depth signal
16. scoring_method

Allowed values:

creator_self_report
ai_estimated
human_reviewed
multi_wing_reviewed
hybrid

Recommended usage:

Value	Meaning
creator_self_report	Score provided by the creator.
ai_estimated	Score estimated by AI.
human_reviewed	Score reviewed by a human.
multi_wing_reviewed	Score reviewed through multiple perspectives or models.
hybrid	Combination of creator, AI, and/or reviewer input.

Scores generated by AI should be treated as provisional unless reviewed.

17. anti_gaming_flags

The anti_gaming_flags array records possible risks in the metadata.

Allowed values:

score_inflation
low_confidence_high_depth
missing_sources
unreviewed_ai_inference
privacy_sensitive_claim
contradictory_metadata
other

Recommended interpretation:

Flag	Meaning
score_inflation	Scores appear artificially high.
low_confidence_high_depth	High depth score but low confidence.
missing_sources	Surface claims lack sufficient source references.
unreviewed_ai_inference	AI-generated fields have not been reviewed.
privacy_sensitive_claim	Metadata includes sensitive or personal claims.
contradictory_metadata	Metadata contains unresolved contradiction.
other	Other risk not covered by existing flags.

These flags do not necessarily invalidate the metadata.
They indicate that additional review may be needed.

18. Score Fields

Several fields use normalized scores from 0.0 to 1.0.

Examples:

certainty_level
confidence
intensity
strength
openness_score
depth_signal_score

General interpretation:

Score Range	Meaning
0.0 - 0.3	Low
0.3 - 0.7	Medium
0.7 - 1.0	High

Scores should be interpreted according to their specific field context.

A high intensity does not mean a high factual certainty.
A high depth_signal_score does not mean automatic royalty entitlement.
A high confidence does not mean legal proof.

19. Privacy and Consent Principles

This metadata may include sensitive interpretive fields.

The following fields require particular care:

bodily_sensation
deep.context
deep.affective_tags
deep.interpretive_summary
deep.personal_resolution

Recommended principles:

Deep-layer metadata should be opt-in.
AI-inferred inner states should be clearly marked.
Human final edit should be preserved whenever possible.
Private or restricted fields should not be exposed in public RAG outputs.
Allocation-related use should require review.
The creator should retain the ability to revise, hide, or remove sensitive annotations.
20. RAG Usage Notes

In RAG systems, this metadata can support retrieval beyond simple keyword or vector similarity.

Example filters:

depth_signal_score > 0.7
relation_type = "resonance"
connection.strength > 0.6
consent_scope = "rag_reference"
review_status = "reviewed"

Possible use cases:

retrieving content by core question
retrieving content by semantic depth
mapping resonance between articles
identifying high-context knowledge sources
supporting trace review
preparing allocation-readiness assessment

However, RAG systems should not expose private or restricted fields without permission.

21. Royalty OS Usage Notes

This specification may support Royalty OS workflows, but it does not perform royalty allocation by itself.

Correct usage:

Consciousness Circle Metadata
↓
Trace Protocol
↓
Review / Dispute / Governance
↓
Allocation Readiness
↓
Royalty OS

The metadata may provide signals for:

semantic depth
question originality
traceable influence
center-deep resonance
interpretive transformation

But allocation must remain separate from annotation.

This prevents gaming, score inflation, and premature automation.

22. Design Philosophy

This specification is designed around one core principle:

Do not reduce living thought to dead tags.
Annotate the structure of thought while preserving human agency, consent, and interpretive depth.

The Consciousness Circle is not a psychological profile.
It is not a claim of literal consciousness.
It is not an automatic royalty engine.

It is a metadata layer for making the structure behind a content item traceable, reviewable, and interoperable in AI-mediated knowledge ecosystems.

23. Summary

The Consciousness Circle Metadata Specification v0.1.0 provides a structured way to describe:

what question generated a content item
what friction triggered it
what surface facts support it
what deep context gives it meaning
how its layers relate to each other
how it may be used in RAG and trace systems
whether it may enter allocation-readiness review

Its purpose is to help AI systems read knowledge with more context, while preserving creator agency and preventing automatic exploitation of deep semantic metadata.
