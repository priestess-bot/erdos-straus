---
kind: claim
claim_id: t6-q-one-root-initializer-envelope-v2-contract
title: q=1 G evidence-only V2 root initializer 的无环 source envelope
statement: >-
  对每个通过 exact raw-integer replay 的核心素数 ordinary q=1 G 输入，V2 factories 按唯一
  拓扑序构造 CanonicalQOneGSourceBodyV2、无 state_id 的 RootInitializerAnchorV2，最后构造
  只以两字段 RootOriginAnchorRefV2 保存 origin metadata 的 RawRootSourceStateV2。body 独立重算
  p 的素性、p=1 mod24、4/p、ROOT_SOL(p)、q=1 G 与 X=(p+3)/4 的完整素因子分解；anchor
  的 domain replay pin 由 body 引用和固定合同唯一计算，不能由 caller 注入。三个 content ID
  均不消费 terminal、schedule、result、owner、potential、E1--E5、transition、admission sidecar
  或 queue token。所有 factory、serializer 和 parser 对 exact class、全部 typed invariants、seal
  及显式 upstream dependency fail closed。输出固定为 EVIDENCE_ONLY_ROOT_SOURCE，initializer、
  admission、queue authority 均为 false；它不建立 exact-HEAD actualness、common owner、persistent
  admission、terminal issuer、E1 或 queue authority。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - root-initializer
  - source-state
  - acyclic-content-addressing
  - evidence-only
  - proof-boundary
sources:
  - reproduction: scripts/t6_q_one_root_initializer_envelope_v2.py
    role: independent q1 G replay, sealed factories and explicit-upstream parsers
  - reproduction: tests/test_t6_q_one_root_initializer_envelope_v2.py
    role: positive controls, ID-independence and forged-object negative controls
  - source: schemas/t6-q-one-root-initializer-envelope-v2.schema.json
    role: exact reserved-field interoperability shapes
visibility: public
last_checked: '2026-08-26'
---

# q=1 G evidence-only V2 root initializer envelope

## 1. 要解决的内容寻址问题

V1 q=1 initializer 把 terminal-first receipt 放进 raw state，再对除 `state_id` 外的整个 state
取哈希。若 production terminal receipt 又必须绑定 source state ID/digest，就会产生

```text
state_id -> terminal result -> state_id
```

的循环。另一方面，successor-only `RawTargetStateV2` 必须依赖一张已有 edge anchor，不能表示
没有 parent transition 的根 source。

本合同只补这一个结构缺口。固定依赖序为

```text
raw q=1 G integers
  -> CanonicalQOneGSourceBodyV2
  -> RootInitializerAnchorV2
  -> RawRootSourceStateV2
```

任何反向引用都不属于 schema。

## 2. canonical q=1 G body

raw input 是 exact-field JSON object，且所有数学标量必须是 exact integer。factory 独立验证

\[
p\text{ prime},\qquad p\equiv1\pmod {24},\qquad
\frac4p,\qquad q=1,
\]

以及 mark、phase、endpoint、provenance 分别对应
`ROOT_SOL(p)`、`TYPEII_G_HANDOFF`、`G`、`ORDINARY_ENDPOINT`。令

\[
X=\frac{p+3}{4}.
\]

输入分解必须是严格递增素数和正指数，乘积恰为 X，并满足

\[
X=\prod_i\ell_i^{e_i},\qquad \ell_i\equiv1\pmod3.
\]

所以单独伪造 G code、提供不完整分解、合数 p、布尔整数或 legacy V1 state 均不能创建 body。

body 的固定非数学字段为

```text
source_tree_scope    = type_ii_endpoint_only
evidence_class       = EVIDENCE_ONLY_ROOT_SOURCE
initializer_authority = false
admission_authority   = false
queue_authority       = false
```

`body_id=q1-source-body:<digest>`，其中 digest 覆盖 artifact type、schema version、全部重算后的
语义字段和上述零权限边界。

## 3. state 之前的 root anchor

`RootInitializerAnchorV2` 绑定 body ID/digest、固定 initializer contract、
`PARENTLESS_ROOT` origin kind 和 raw-integer domain replay。domain replay ID 是固定常量，其 digest
由 body ID/digest、固定结果标签和三项 false authority 唯一重算；factory 不接受 caller 提供的
replay ID 或 digest。

特别地，anchor reserved fields 中没有 `state_id`。因此

\[
\operatorname{anchor\_id}
=H(\text{body ref},\text{fixed root contract},\text{fixed domain replay})
\]

在 source state 出现前已经闭合，并且不依赖任何 terminal 或 schedule 决策。

`contract_digest` 只是本模块固定结构合同的摘要，不是 Git provenance、HEAD binding、initializer
grant 或 role authority。

## 4. root source state

`RawRootSourceStateV2` 逐字段重复 canonical body 语义并绑定 body ID/digest。它唯一的 origin
metadata 是

```text
root_origin = {
  root_initializer_anchor_id,
  digest
}
```

随后才计算

\[
\operatorname{state\_id}
=\texttt{state:}H(\text{body semantics},\text{body ref},\text{root-origin ref},
\text{evidence-only boundary}).
\]

state 没有 terminal receipt、schedule/result、owner cache、potential、E1--E5、transition bundle、
admission sidecar 或 queue token。因而任意后置 terminal/schedule sidecar 的内容变化都不改变
body ID、anchor ID 或 state ID。

这个对象可作为未来 terminal issuer 的稳定 `SOURCE_STATE` 内容依赖，但当前仍只是 source
shape evidence。它不是 actual admitted state，也不能直接进入 persistent queue。

## 5. factory 与 parser 边界

所有 artifact dataclass 都是 `frozen=True, slots=True, init=False`，只能由 factory 正常创建。
这本身不是安全证明；真正边界是每次序列化或下游消费前都会：

1. 要求 exact class，拒绝 subclass；
2. 逐字段要求 exact built-in string、integer、boolean、tuple 和 digest；
3. 重新验证 p、q=1 G、mark、方程及完整因子分解；
4. 重算 authority 常量、domain replay、content digest 和 ID；
5. downstream factory 完整重验 upstream artifact；
6. parser 要求显式 raw/body/anchor upstream，并从 upstream 重建 expected artifact 后逐字比较。

因此，经 `object.__new__` / `object.__setattr__` 绕过 frozen、再重算 seal 的 authority flip、
语义变化和 body/anchor swap 仍不能通过相应信任边界。一个局部自洽但属于另一 body 的 anchor
只有与它自己的 upstream 一起才有意义，不能在显式 parser 中替换当前 root origin。

JSON Schema 只描述 reserved wire fields，不能验证素性、完整因子分解、content seal 或 upstream
preimage；这些义务由 Python factories/parsers 承担。Schema 的 JSON `integer` 语义也不等同于
Python 的 exact `int`，不作二者完全等价的声称。

## 6. 聚焦控制与非结果

正控制覆盖 \(p=73,X=19\) 以及

\[
p=76129,\qquad X=19033=7\cdot2719.
\]

负控制覆盖：合数 core、伪 G、错误分解、caller authority、legacy terminal/state fields、
bool/`str`/`int`/key subclass、artifact subclass、authority/semantic 重封、cross-body anchor、
cross-anchor origin 和 schema field injection。

```bash
python3 -m unittest tests.test_t6_q_one_root_initializer_envelope_v2 -v
ruff check scripts/t6_q_one_root_initializer_envelope_v2.py \
  tests/test_t6_q_one_root_initializer_envelope_v2.py
python3 -m py_compile scripts/t6_q_one_root_initializer_envelope_v2.py \
  tests/test_t6_q_one_root_initializer_envelope_v2.py
```

本合同不建立 exact-HEAD binding、initializer occurrence、common owner classification、registered
prefix schedule authority、terminal decision、E1、admission 或 queue mutation。未来 production issuer
仍须以独立 HEAD-bound receipt 同时绑定本 state ID/digest、initializer actualness、owner-domain replay、
scheduler evidence 和 independent coverage replay。
