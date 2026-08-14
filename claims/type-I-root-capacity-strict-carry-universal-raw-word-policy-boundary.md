---
kind: claim
claim_id: type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
title: 严格 root carry 的规范 universal raw word 与 E1 root-policy 边界
statement: >-
  对任一核心 a=1,d=1 根图表，universal_p_source_v1 的 p 边后，依次按
  (R-1)/(p+1) 与 (R-p-1)/(3u) 的规范素因子 word 做实际容量剥离，必从
  (1,R-1) 到达根锚 (p+1,R-p-1)，再到达 actual proper-root endpoint
  (3u,R-3u)。因此 strict root carry 的完整 raw word 可由 (p,r) 及两个有限
  素因子分解回放；p=73,r=3 与 p=313,r=271 给出固定 strict controls。然而该 source
  和两个 word 都由目标 root chart 反向确定，故仅说明 actual raw reachability；按
  universal p-parent root-policy no-go，它不能单独支付 E1、创建 fresh/charged state，
  或把 support-rebase 登记为 verified_edge。真正剩余的 E1 输入仍是 target-independent
  persistent charged origin、scope 与 terminal-first miss；E3 仍须独立 typed
  reclassification。既有 strict support-rebase 的 E2、图表无关恒等 E4 和严格 E5
  不受此边界影响。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-strict-carry-support-rebase
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - root-capacity
  - strict-carry
  - raw-path
  - universal-source
  - capacity-peeling
  - source-provenance
  - root-policy
  - E1
  - support-rebase
  - proof-boundary
sources:
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: universal-p-source-and-actual-capacity-peeling
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: root-endpoint-capacity-gcd
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: strict-receipt-and-support-rank
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: target-derived-raw-parent-is-not-E1
  - reproduction: reproductions/type_i_root_capacity_strict_carry_universal_raw_word.py
    role: fixed-canonical-raw-word-replays
visibility: public
last_checked: '2026-08-15'
---

# 严格 root carry 的规范 universal raw word 与 E1 root-policy 边界

## 1. 为什么需要区分 raw word 与 E1

固定核心素数

\[
p\equiv1\pmod {24},
\]

并取一个 \(a=1,d=1\) 根接口参数 \(r\ge1\)。沿用

\[
g=\frac{p+1}{2},\qquad T=p^2r-g,\qquad A=gT,
\]

\[
K=A(p-1),\qquad
R=2p^3r-p^2-2pr-p+1,
\tag{1}
\]

以及

\[
M=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M),\qquad h=3u.
\tag{2}
\]

已有根容量定理给出

\[
4K=pR+1,\qquad
(R-p-1,K)=h,\qquad (h,R-h)=1.
\tag{3}
\]

严格 carry 的 support-rebase 卡此前正确地把缺口写成 root raw path、persistent
source、terminal-first priority 与 typed serializer。这里先解决其中最容易被混淆的
部分：root endpoint 的 raw **可达性**确实有一个完全显式的 word；但这个 word 由当前
chart 本身反向计算，所以不构成独立 E1 来源。

## 2. 从 universal source 到根锚的精确 word

令

\[
b=2r(p-1)-1.
\tag{4}
\]

直接由 (1) 得

\[
R-1=p(p+1)b,
\qquad
K=(p+1)\frac{p-1}{2}T.
\tag{5}
\]

而且

\[
(pb,\tfrac{p-1}{2}T)=1.
\tag{6}
\]

的确，\(p\nmid T\)、\(b\equiv-1\pmod{(p-1)/2}\)，并且

\[
2(p-1)T
=p^2\bigl(2r(p-1)\bigr)-(p^2-1)
\equiv1\pmod b.
\tag{7}
\]

所以

\[
\boxed{(R-1,K)=p+1.}
\tag{8}
\]

定义两个正整数

\[
L_0=\frac{R-1}{p+1}=pb,
\qquad
L_1=\frac{R-p-1}{h}.
\tag{9}
\]

把每一个写成按非降素数顺序排列、重复保留幂次的 word

\[
L_i=q_{i,1}\cdots q_{i,\ell_i}.
\tag{10}
\]

`universal_p_source_v1` 对这里的高 \(R\) 仍是一个实际 formal raw source：

\[
\bigl(p,\ R(p-1)-p,\ p-1\bigr)
\xrightarrow[q=p]{\mathrm{shift}=1}
(1,R-1,1).
\tag{11}
\]

这里 \(R\equiv1\pmod p\)，故 source primitive，且 \(p\nmid K\) 来自

\(4K\equiv1\pmod p\)。式 (11) 的 raw 条件不使用 \(R<p\)。

在 \(m=1\) node \((x,R-x)\) 上，若 \(q\mid x\) 且

\[
v_q(x)>v_q(K),
\tag{12}
\]

则实际 raw move 是

\[
(x,R-x)
\longmapsto
\left(\frac{x}{q},\ R-\frac{x}{q}\right).
\tag{13}
\]

每次无需 gcd reduction；因为 node primitive，\(q\nmid R\)，而 (13) 仍是一对
primitive 正整数。按 (8) 对 (R-1) 的全部 excess 层施用 (13)，正好按 word
(L_0) 抵达

\[
\boxed{(1,R-1)\leadsto(p+1,R-p-1).}
\tag{14}
\]

同理，(3) 的第二个 gcd 意味着把 (R-p-1) 的每个超过 (K) 容量的素数层剥尽，
其规范 word 恰是 (L_1)，于是

\[
\boxed{(p+1,R-p-1)\leadsto(h,R-h).}
\tag{15}
\]

因此 (11)、(14)、(15) 是从一个明确 raw triple 到 actual root endpoint 的有限、
可重放 transcript。各 prime word 的排列只影响中间 node；固定非降顺序后，word 和
physical occurrence 都成为确定对象。它不依赖对端点因子作静态替换。

## 3. strict receipt 的连接

现取 proper-root \(u<M\)，并把 endpoint 对侧作 maximal complete-excess 分解

\[
z=R-h=Q\beta,\qquad
g_A=(A,Q),\qquad E=Q/g_A,\qquad D=\beta g_A.
\tag{16}
\]

由 (15)，这里的 \((h,z)\) 是 actual raw occurrence；由 maximality 和 (3)，

\[
Q>1,\qquad (Q,\beta)=1,\qquad h\beta\mid K.
\tag{17}
\]

strict 条件

\[
c=\langle-E^{-1}\rangle_p\le p-2
\tag{18}
\]

仍给出既有的

\[
M_{\rm ex}=\operatorname{lcm}(A,Q)=AE,
\qquad
\Lambda_p^\sharp:(0,p-1)\longmapsto(0,c).
\tag{19}
\]

所以 root raw occurrence 不再是未解释的存在性断言：若另有一个独立已入队的 source
state，它可以把 (11)--(15) 作为其 endpoint path segment 的可验证 payload。

## 4. 为什么这仍不能支付 E1

式 (1)、(2)、(9) 表明 universal source、两条 prime word 及其每个中间 node 都由
当前目标 chart \((p,r)\) 算出。特别是，先指定一个希望获得的 endpoint，再反向写出
(11)--(15) 总是可能的。它没有提供 target-independent 的 root family，也没有说明
当前 charged support \(A\) 是怎样在同一 `source_tree_scope` 下获得的。

这正落在 universal \(p\)-parent 的 root-policy 边界内：actual p-raw parent 或有限
actual raw word 的存在可以对任意 primitive node 成立，不能单独区分可进入递归树的
source。因此本卡的 transcript 必须满足

```text
selector_status = analysis_evidence
recursive_edge_eligible = false
```

除非另一张回执独立提供：

1. target-independent、已声明的 persistent charged origin；
2. 不可伪造的 `source_tree_scope` 连续性；
3. terminal-first prefix 全部 miss；
4. source/target 的 F/G/hit 重分类、normal form 与内容寻址 verifier。

前三项才是 strict support-rebase 的剩余 E1；第 4 项是 E3。它们不能由 (11)--(15)
反向补造。另一方面，本卡不影响既有 E2 的 canonical support construction、
图表无关 \(\operatorname{Sol}(4,p)\) 恒等 E4，或 (19) 的严格 E5。

## 5. 固定 strict controls

两个 fixed controls 的完整 word 为

\[
\begin{array}{c|c|c|c|c}
(p,r)&L_0&L_1&h&c\\ \hline
(73,3)&73\cdot431&73\cdot10631&3&37\\
(313,271)&11\cdot313\cdot15373&313\cdot97787&543&298
\end{array}
\tag{20}
\]

前者重放到 ((3,2328260))，后者重放到
((543,16619780504))。它们分别给出 (16) 的

\[
(Q,\beta,E,D)=(10583,220,10583,220),
\]

及

\[
(Q,\beta,E,D)=(2077472563,8,2077472563,8).
\]

两例都验证 (19)，但故意只保存为 `analysis_evidence`：fixed raw transcript 不是
已登记 charged state 的 parent receipt，也没有执行 terminal-first 或 typed target
reclassification。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_strict_carry_universal_raw_word.py --verify
```

该脚本只重放 (20) 的两条 target-derived raw word、逐步容量和 unit 条件、maximal
receipt 及 strict support rank。它显式拒绝篡改的 prime word，不扫描素数、参数、
分母、selector history 或历史测试。
