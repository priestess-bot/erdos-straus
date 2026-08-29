---
kind: claim
claim_id: sp21-sp22-q1-g-scoped-prototype-reproduction-v1
title: SP-21/SP-22 q=1,G scoped selector prototype reproduction
statement: >-
  提交的 SP-21/SP-22 concrete closure v1 package 在其声明的 e6e9e4a 基线工作树中可重放：
  25 项 manifest、constructor、independent replayer 与 37 个 focused controls 均通过，
  并给出 M23-priority q=1,G selector prototype 和 p=21169 正向 trace。该结论仅是
  computationally reproduced 的独立 slice 证据；其内嵌 RSA key 未提供外部 authority
  provenance，base_head_sha 亦未在运行时与当前 Git HEAD 比较，且 pilot runtime 未接入
  现有 persistent selector。因此它不关闭 active SP-21、SP-22、SP-03、F1/F2/F3、T6 或猜想。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
  - SP-21
  - SP-22
  - q=1
  - terminal-first
  - prototype
  - reproducibility
  - proof-boundary
  - T6
sources:
  - document: docs/standalone-proof-propositions-2026-08-28/SP-21-SP-22-concrete-closure-v1-review-2026-08-29.md
    role: independent review and status boundary
  - document: docs/archive/proof-submissions/2026-08-29/SP-21-SP-22-concrete-closure-v1-ARCHIVAL-NOTE.md
    role: submitted package provenance
  - document: docs/archive/proof-submissions/2026-08-29/sp21-sp22-concrete-closure-v1/VALIDATION.md
    role: supplied validation record
visibility: public
last_checked: '2026-08-29'
---

# Scoped Prototype Reproduction

The reviewed package supplies a useful implementation experiment: a finite
M23-priority terminal policy followed by a phase-root producer, with gap 31
explicitly later. Its two programs reproduce the supplied \(p=21169\) trace and
the package's focused controls in the declared base worktree.

The claim deliberately stops there. A signature whose public key and trust
anchor are both introduced by the submitted bytes cannot independently establish
external coordinator authority. Nor can a declared base commit be used as an
actual-source fact when the verifier never compares it with the running Git
checkout. The package is consequently retained as a reproducible prototype and
as a concrete design reference for the next SP-21/SP-22 revision.
