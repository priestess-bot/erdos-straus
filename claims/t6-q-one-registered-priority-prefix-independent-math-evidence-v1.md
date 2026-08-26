---
kind: claim
claim_id: t6-q-one-registered-priority-prefix-independent-math-evidence-v1
title: q=1 注册优先前缀 gaps 3/7/11 的独立数学证据层
statement: >-
  对每个通过 raw-integer domain replay 的 ordinary q=1 G 根输入，scheduler 对冻结前缀
  m=(3,7,11) 中每个 x_m=(p+m)/4 重新作完整素因子分解，按升序枚举全部
  d|x_m^2，并按 (gap,d,Type I before Type II) 的固定顺序重算全部 Bradford
  Type I/II 命中、分母和根方程。独立 coverage verifier 不导入 scheduler、旧 runtime
  或历史 reproduction，而是从同一 raw domain 独立重建因子、平方除子全集、全部证书、
  scan/outer digests 与 canonical wire。结果只证明注册前缀内的 ROOT_TERMINAL_HIT 或
  PREFIX_MISS_EVIDENCE_ONLY；global_exhaustion=false、next_unchecked_gap=15，terminal/role
  authority 均为 BLOCKED，issuance_allowed=false。它不产生 MISS_COMPLETE、角色授权、
  transition admission、全根终端穷尽、T6 闭合或 Erdos--Straus 猜想证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - terminal-first
  - registered-priority-prefix
  - short-certificate
  - independent-verification
  - proof-boundary
sources:
  - reproduction: scripts/t6_q_one_priority_prefix_scheduler_v1.py
    role: independent q1 G domain replay and exhaustive registered-prefix scheduler
  - reproduction: scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py
    role: separately implemented factor, divisor, certificate, equation and wire replay
  - reproduction: tests/test_t6_q_one_priority_prefix_independent_evidence_v1.py
    role: cross-module controls, global-boundary control and resealed mutation suite
  - claim: short-certificate-equivalence
    role: Type I/II algebra and natural-gap context, not global-prefix exhaustion
visibility: public
last_checked: '2026-08-26'
---

# q=1 注册优先前缀 gaps 3/7/11 的独立数学证据层

## 1. 精确而非循环的 domain

输入不是 owner 名称或 terminal MISS，而是 exact-field raw integer object。它必须独立满足

\[
p\text{ prime},\qquad p\equiv1\pmod {24},\qquad
q=1,\qquad X_3=\frac{p+3}{4},
\]

并携带 \(X_3\) 的完整严格有序素因子分解

\[
X_3=\prod_i \ell_i^{e_i},\qquad \ell_i\equiv1\pmod3.
\]

方程坐标必须是 \(4/p\)，mark 必须是 `ROOT_SOL(p)`，endpoint、phase、provenance 的整数码
必须分别表示 `G`、`TYPEII_G_HANDOFF` 与 `ORDINARY_ENDPOINT`。这重建 ordinary q=1 G 的
数学域，但不声称 actual admitted predecessor、common classifier owner 或 owner authority。

domain schema 没有 schedule outcome、local miss、complete miss 或 authority 字段。因此不能通过
把“已经 MISS”写回 domain 来循环定义 coverage。

## 2. 冻结候选全集

注册前缀固定为

\[
\mathcal M=(3,7,11).
\]

对每个 \(m\in\mathcal M\)，令

\[
x_m=\frac{p+m}{4}=\prod_j r_j^{a_j}.
\]

则全部正除数 \(d\mid x_m^2\) 恰为

\[
d=\prod_j r_j^{b_j},\qquad 0\le b_j\le2a_j.
\]

scheduler 生成这个集合、去重并按整数升序排序。对每个 \(d\) 依次检查

\[
\mathrm{I}:\quad m\mid px_m+d,
\]

\[
\mathrm{II}:\quad d\le x_m,\qquad m\mid x_m+d.
\]

候选总序为

```text
gap ascending, divisor ascending, Type I before Type II
```

即某个 divisor 的 Type I/II candidate index 分别为 \(2i\)、\(2i+1\)。即使已经发现早期
terminal，证据仍完整扫描三个 gap 并记录所有 matching certificates；`selected_terminal` 只取
全序中的第一项。

## 3. 命中声性与前缀覆盖

Type I 命中时重建

\[
y=\frac{px_m+d}{m},\qquad
z=\frac{p(x_m+px_m^2/d)}m;
\]

Type II 命中时重建

\[
y=\frac{p(x_m+d)}m,\qquad
z=\frac{p(x_m+x_m^2/d)}m.
\]

两套实现都重新检查正性、整性和

\[
4x_myz=p(x_my+x_mz+yz).
\]

因此 `ROOT_TERMINAL_HIT` 包含一张可直接检查的根方程证书。但这个字符串仍只是数学 evidence
status；本层没有 terminal authority，不能自行结束 production proof run。

若三个 scan 的 matching list 都为空，则由于每个 \(x_m^2\) 的全部正除数和两个类型都已逐项
检查，严格得到

\[
\forall m\in\{3,7,11\},\quad
\nexists d\mid x_m^2\text{ satisfying Type I or Type II}.
\]

这正是 `PREFIX_MISS_EVIDENCE_ONLY` 的完整量词。它没有量化 \(m\ge15\)，所以不是
`MISS_COMPLETE` 或 \(\operatorname{Sol}(p)=\varnothing\) 的证明。

## 4. 独立 coverage replay

coverage verifier 与 scheduler 位于不同模块，且不导入 scheduler、旧 q=1 runtime、state
contract 或任何 reproduction。它使用单独编写的素性、奇数试除、平方除子生成和 Type I/II
恢复逻辑，从 raw domain 重建完整 expected wire。验证必须同时满足：

1. 三个 gap 的 factorization 和 divisor universe 完全相同；
2. matching certificates、candidate indices、首选 terminal 和 HIT/MISS 状态完全相同；
3. 每个 scan digest 与 outer digest 分别重算；
4. 最终 canonical JSON wire 逐字一致；
5. scope 固定为 `REGISTERED_PRIORITY_PREFIX_GAPS_3_7_11`；
6. `global_exhaustion=false`、`next_unchecked_gap=15`；
7. terminal/role authority 为 `BLOCKED`，issuance 为 false。

coverage verifier 返回的 DTO 同样只是 evidence-only 结果。未来若要成为 production receipt，仍需
HEAD-bound registry、独立 role grant、subject/admitted-predecessor binding 和 consumer-side authority
合同；对象存在或 digest 正确都不授予这些权限。

## 5. 控制与严格边界

- \(p=73\)：gap 3 MISS，gap 7 的 Type II \(d=1\) 是全序第一命中；
- \(p=241441\)：gap 3/7 MISS，gap 11 的全序第一命中是 Type II \(d=27\)；完整 matching
  集同时包含历史 Type II 控制 \(d=1083\)；
- \(p=1201\)：三个注册 gap 全 MISS，但未注册的 gap 23、Type I \(d=34\) 给出
  \((x,y,z)=(306,15980,172727820)\)；
- \(p=2521\)：三个注册 gap 全 MISS。

\(p=1201\) 是故意保留的反全球穷尽控制：它证明 prefix MISS 可以与更晚 root terminal 同时成立。
因此不得把 coverage scope 改为 `TERMINAL_UNIVERSE_COMPLETE`，也不得把
`global_exhaustion` 改为 true。

聚焦 mutation suite 在重算受影响的 scan/outer digest 后，仍拒绝 gap、gap order、candidate
order、divisor、factorization、domain、selected terminal、scope 和 global flag 交换；它还拒绝
在 raw domain 注入 schedule MISS。

```bash
python3 -m unittest tests.test_t6_q_one_priority_prefix_independent_evidence_v1 -v
ruff check scripts/t6_q_one_priority_prefix_scheduler_v1.py \
  scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py \
  tests/test_t6_q_one_priority_prefix_independent_evidence_v1.py
python3 -m py_compile scripts/t6_q_one_priority_prefix_scheduler_v1.py \
  scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py \
  tests/test_t6_q_one_priority_prefix_independent_evidence_v1.py
```
