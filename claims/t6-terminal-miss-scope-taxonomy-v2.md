---
kind: claim
claim_id: t6-terminal-miss-scope-taxonomy-v2
title: T6 注册优先前缀 miss 与全终端宇宙 miss 的不可混淆类型边界 v2
statement: >-
  RegisteredPriorityPrefixMissReceiptV2 and TerminalUniverseMissReceiptV2 are
  disjoint, exactly shaped, canonically sealed evidence types. The prefix type
  has outcome MISS_REGISTERED_PRIORITY_COMPLETE, coverage semantics
  REGISTERED_PRIORITY_ONLY and global_exhaustion=false; it binds an exact HEAD,
  coordinator registry v2, source/domain/schedule, a contiguous ordered natural
  gap prefix, one declared family and local miss digest per gap, the next unchecked
  gap and coverage artifact declarations. The universe type has outcome
  TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY and global_exhaustion=true; its shape names
  the complete natural range 3,7,...,p-2, primality, factorization/divisor-lattice
  and reverse-equivalence artifacts, but the parser does not execute or trust any
  of them. Neither type carries E1 or queue authority. A prefix receipt may be
  consumed by E1 only after a future HEAD-bound coordinator registry v2 and an
  independent semantic verifier authorize that exact schedule. A universe shape
  may report a counterexample only after full semantic verification and can never
  continue to a producer.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - terminal-first
  - proof-receipt
  - scope-taxonomy
  - proof-boundary
sources:
  - reproduction: scripts/t6_terminal_miss_scope_taxonomy_v2.py
    role: exact evidence types, shape parsers, canonical seal check and continuation firewall
  - reproduction: tests/test_t6_terminal_miss_scope_taxonomy_v2.py
    role: scope-confusion, authority-spoof and p1201 boundary controls
  - source: schemas/t6-terminal-miss-scope-taxonomy-v2.schema.json
    role: machine-readable exact field and constant contracts
visibility: public
last_checked: '2026-08-26'
---

# T6 terminal miss scope taxonomy v2

## 1. 为什么必须拆成两个结果

一个有限 terminal schedule 可以完整重放自己登记的优先族，而不枚举所有可能的根证书。
这时正确结论只是

```text
MISS_REGISTERED_PRIORITY_COMPLETE
coverage_semantics = REGISTERED_PRIORITY_ONLY
global_exhaustion = false
```

它不能被转述成 `all_root_terminals_miss`。相反，若对核心素数 (p) 枚举全部

\[
m=3,7,\ldots,p-2,\qquad x_m=\frac{p+m}{4},\qquad d\mid x_m^2,
\]

并以已独立证明的反向 Type I/II 等价确认没有命中，则结论为

```text
TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY
global_exhaustion = true
```

这个字段组合只声明“提交者声称已覆盖全域”，并不证明根方程没有解。只有 coordinator
固定全部 artifact 后，由独立 semantic verifier 重放素性、范围、分解、除子全集、反向
等价和零命中，才能另行报告根反例。无论是否完成这项未来验证，universe miss 永远没有
producer continuation。

## 2. 注册优先前缀的推荐冻结

q=1 G root source 的首个实用候选可以使用下列建议 ID：

```text
registry_id = t6_coordinator_role_registry_v2
schedule_id = q1_g_root_full_divisor_gap3_7_11_priority_prefix_v2
owner_domain_id = owner-domain:q1-g-root-source:v2
ordered_gaps = [3, 7, 11]
ordered_family_ids = [
  bradford_full_divisor_gap3_v2,
  bradford_full_divisor_gap7_v2,
  bradford_full_divisor_gap11_v2
]
next_unchecked_gap = 15
```

未来 semantic verifier 对这里每个 family 必须枚举对应 (x_m^2) 的全部正除子并同时
检查 Type I、Type II；本卡 parser 只把 family ID、definition digest 和 local miss digest
当作 opaque declarations，不读取其内容。schedule、owner-domain 和 coverage theorem、
reproduction、verifier、replay 字段也都是 opaque declarations。gap 7 的三个固定同余
公式只能作为 evaluator 的快速命中路径，不能替代完整 gap-7 divisor family。schedule
digest 应声明绑定上述次序和 artifacts；parser 不重算这种绑定是否真实成立。

## 3. p=1201 的严格负控

(p=1201) 是 ordinary q=1 G root：(x_3=301=7\cdot43)，两个素因子都为
(1\pmod3)。完整 divisor screen 在 (m=3,7,11) 全部 miss，因此它可以形成上述
prefix evidence；但 (m=23)、(x=306)、Type I (d=34) 给出

\[
(x,y,z)=(306,15980,172727820),
\qquad
\frac4{1201}=\frac1x+\frac1y+\frac1z.
\]

所以 prefix receipt 必须记录 `next_unchecked_gap=15` 和 `global_exhaustion=false`。测试还
故意构造一个声称 `hit_count=0` 的 p=1201 universe mapping；它可以通过 shape parser，
恰好证明 canonical seal 和字段自洽不构成数学验证。把 prefix 字段改成 universe 常量后
重新计算 digest，也只是在攻击者可见字段上重封装；parser 对其拒绝只是类型/字段常量
边界，不应被描述成对 terminal completeness 的验证。

## 4. 两类精确绑定

prefix receipt 绑定：

```text
HEAD and evidence-only coordinator registry v2
subject and scheduler-input digests
owner-domain membership replay artifact/result
schedule ID/digest
contiguous ordered gaps and family-definition digests
one local miss digest per registered family
next unchecked natural gap
coverage theorem/reproduction/independent verifier/replay
```

universe receipt 另行绑定：

```text
root prime p congruent to 1 modulo 24
root primality verifier ID, artifact digest and claimed replay digest
natural range start=3, stop=p-2, step=4, count=(p-1)/4
checked gap/divisor counts and zero hits
claimed complete factorization and divisor-lattice manifest digests
scan algorithm/transcript
range definition
reverse-equivalence claim, proof, independent verifier and claimed replay
```

类型字段、JSON field set、数组类型和 canonical digest 均作 shape-only 检查。所有 object
key、text、digest、HEAD 和 integer 必须是 exact builtin type；Python `bool` 或 `int`
子类不得替代整数，`str` 子类不得替代 key/text/digest/HEAD。dataclass 子类、v1/local
receipt、额外 `queue_gate` 或跨类型字段集合均被拒绝。parser 不读取 artifact，不运行
primality、factorization、family、schedule、coverage 或 reverse-equivalence verifier，
也不证明任何 digest 声称确实来自对应程序。

## 5. 当前权限边界

本模块不提供 production issuer，不读取 caller-supplied registry，不接入 runtime，也不
生成 E1 或 queue token。两种 receipt 均固定携带：

```text
evidence_class = EVIDENCE_ONLY_NO_E1_OR_QUEUE_AUTHORITY
e1_authority = false
queue_authority = false
```

prefix receipt 将来只有在 coordinator role registry v2 对同一 HEAD、schedule、domain、
family order 和 coverage artifacts 给出明确 grant，并由独立 semantic verifier 实际重放
后，才能由新的 production verifier 重新签发或包装为 E1 可消费证明。universe receipt
只有在独立 semantic verifier 完成素性、完整自然范围、全部分解/除子和反向等价重放后，
才可另行报告根反例；即使如此也不能获得 producer 或 queue 权限。本卡因此不关闭 Gate
2、Gate 4、F1 或 T6。
