---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
title: q=1 容量八 target 的 source-side 支撑分离与非 p raw 出边
statement: >-
  设 ordinary q=1 full-carrier 的 zero-k 容量八 normal form 已给出
  p=48s+1、K=8M、pR+1=4K，其中 M=9s(176s+5)(3168s^2+24s-1)，且 s>=86。
  则高 R 形式源 S=(p,V,p-1)，V=R(p-1)-p，是 primitive actual raw source；其
  V-side 共享容量满足 gcd(V,K) divides 11*41*149，故 V 不整除 K，并存在一个
  q!=p 使 v_q(V)>v_q(K)。这个 q 给出一条实际 non-p raw edge。若再处于真实
  q_star=103 rough 域，则 103 divides K 而 103 does not divide V，且
  gcd(V,6s-1) divides 5*503；因此 macro carrier 103 不能被误作 V-side source
  标签。已知 p=157393 的 c=8 arithmetic macro control 有 q=5963047 的一步
  non-p edge 直接到 m=1。结论只提供 source/path 和支撑分离；不构造 Type I/II
  terminal、解提升或 E5 strict edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
  - type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
  - type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-I-ordered-raw-lineage-normalized-phase-rigidity
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - full-carrier
  - c-eight
  - universal-source
  - raw-path
  - source-support
  - q-star
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
    role: c-eight-high-R-target-normal-form
  - claim: type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
    role: exact-q-star-103-domain
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: high-R-source-path-contract
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation.py
    role: exact-support-identities-and-one-step-raw-control
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 target 的 source-side 支撑分离与非 \(p\) raw 出边

## 1. 高 \(R\) target 和它的形式源

固定 zero-\(k\) 容量八 normal form

\[
p=48s+1,
\qquad
L=176s+5,
\qquad
E=3168s^2+24s-1,
\tag{1}
\]

\[
M=9sLE,
\qquad
K=8M=72sLE,
\qquad
pR+1=4K,
\tag{2}
\]

其中

\[
R=3345408s^3+50688s^2-1392s-1.
\tag{3}
\]

这里的 \(R\) 通常大于 \(p\)，所以不能把它和低 \(R\) anchor 的静态
因子菜单混同。设

\[
\begin{aligned}
V&=R(p-1)-p\\
 &=160579584s^4+2433024s^3-66816s^2-96s-1,
\end{aligned}
\tag{4}
\]

并考虑有序三元组

\[
\mathsf S=(p,V,p-1).
\tag{5}
\]

它满足 \(p+V=R(p-1)\)。此外有精确恒等式

\[
4R-79=p(278784s^2-1584s-83).
\tag{6}
\]

对于核心 \(p=48s+1\ge4129\)，(6) 给出 \((p,R)=1\)。再由

\[
(V,p)=(R,p)=1,
\qquad
(V,R)=(p,R)=1,
\qquad
(V,p-1)=1
\tag{7}
\]

可知 (5) 是 primitive formal raw source。其 \(p\)-edge 的 shift 为 \(1\)，且

\[
(p,V,p-1)\xrightarrow{p}(1,R-1,1).
\tag{8}
\]

式 (8) 只是既有 high-\(R\) source/path 合同的 canonical branch；本卡研究同一
source 的另一坐标，而不把它预设为 anchor 后路径。

## 2. \(V\) 与当前容量的精确共同支撑

首先 \(V\) 是奇数且 \(V\equiv2\pmod3\)，并且 \(V\equiv-1\pmod s\)。所以
\((V,72s)=1\)。余下两个载体有 Bezout 恒等式

\[
-44V+3(528s-7)(25344s^2-1)L=149,
\tag{9}
\]

\[
-(5280s+139)V
+24(11151360s^3+378048s^2+464s-13)E=451=11\cdot41.
\tag{10}
\]

结合 (2) 得到

\[
\boxed{D:=(V,K)\mid 11\cdot41\cdot149=67199.}
\tag{11}
\]

这不是只给上界的模糊说法。逐个约化 (4)、(1)--(2) 给出共同支撑的精确出现表：

\[
\begin{array}{c|c}
q&q\mid D\ \Longleftrightarrow\ s\pmod q\\ \hline
11&6\\
41&30\\
149&55
\end{array}
\tag{12}
\]

在 \(s\ge1\) 时，(4) 还满足

\[
V>160512768s^2-1>67199.
\tag{13}
\]

因此 \(D<V\)。若每个 \(V\) 的素数估值都不超过 \(K\) 中的估值，则会有
\(V\mid K\)，从而 \(D=V\)，与 (11)--(13) 矛盾。故存在素数 \(q\) 使

\[
v_q(V)>v_q(K).
\tag{14}
\]

由 (7)，这个 \(q\) 与 \(pR(p-1)\) 互素，特别地 \(q\ne p\)。令

\[
t_q\in\{1,\ldots,q-1\},
\qquad t_q\equiv-(p-1)\pmod q.
\tag{15}
\]

则 (14) 和 raw unit 条件给出一条实际 non-\(p\) 边

\[
\boxed{
(p,V,p-1)
\xrightarrow{q}
\operatorname{prim}\left(
\frac Vq,
\frac{p+Rt_q}{q},
\frac{p-1+t_q}{q}
\right).}
\tag{16}
\]

其中 \(\operatorname{prim}\) 只做该步真实出现的 gcd reduction；本结论没有暗中
假设 reduction 为 \(1\)。所以容量八 target 不存在“source 只有 canonical
\(p\)-edge”这一缺口，但 (16) 尚未指定它应落入哪一种 typed state。

## 3. 真正 \(q_\star=103\) 域与 source 标签分离

令

\[
N=6s-1.
\tag{17}
\]

由 (4) 有

\[
V=N(26763264s^3+4866048s^2+799872s+133296)+133295,
\tag{18}
\]

且

\[
133295=5\cdot53\cdot503.
\tag{19}
\]

现在额外假设真实 macro selection 满足 \(q_\star=103\)。既有 rough 判据给出
\(103\mid N\)、\(25\nmid N\)，以及 \(7\) 至 \(101\) 的每个素数均不整除
\(N\)。因此 (18)--(19) 强化为

\[
\boxed{(V,N)\mid5\cdot503.}
\tag{20}
\]

特别地 \(V\equiv133295\equiv13\pmod{103}\)，故 \(103\nmid V\)。另一方面
\(s\equiv86\pmod{103}\)，所以

\[
L=176s+5\equiv176\cdot86+5\equiv0\pmod{103},
\tag{21}
\]

并由 (2) 得 \(103\mid K\)。综上，

\[
\boxed{103\mid K,\qquad103\nmid V.}
\tag{22}
\]

因此 second-anchor macro 的 carrier \(q_\star=103\) 不是 (16) 中可重用的
\(V\)-side label。任何利用 (16) 的 source-aware bypass 都必须携带一个真实的
\(V\) 因子及其 shift/gcd transcript；不能把 rough phase 本身冒充为 raw word。

## 4. 一步 \(m=1\) 的实际控制

已有容量八 arithmetic macro 控制为

\[
s=3279,
\qquad p=157393,
\qquad q_\star=103.
\tag{23}
\]

它本身会被 terminal-first 抢占，只用于复核这里的 raw 算术。此时

\[
V=11\cdot241\cdot5963047\cdot1174302652267,
\qquad (V,K)=1.
\tag{24}
\]

取 \(q=5963047\)，有 \(q>p-1\)，故

\[
t_q=q-(p-1)=5805655.
\tag{25}
\]

式 (16) 的 gcd reduction 等于 \(1\)，并给出

\[
\begin{aligned}
(157393,V,157392)
\xrightarrow{5963047}
(&3113076331159817,\\
 &114830786617996134,1).
\end{aligned}
\tag{26}
\]

这是一条与 canonical \(p\)-edge 不同、从同一 source 直接重入 \(m=1\) 的实际
raw receipt。它说明后续 source-aware 分支不是纯形式的 reverse parent；但 (26) 的
原素数已有 terminal，因而不能作为 persistent 反例或递归边。

## 5. 精确边界

本卡支付的是 source/path 层的一个缺口：所有容量八 normal-form target 都至少有一条
non-\(p\) raw 出边，并且真实 103 macro carrier 与该 source-side 载体分离。它**没有**
支付下列任一项：

- 从 (16) 的 endpoint 到可接纳 Type I state 的 typed reclassification；
- 对任意 \(q\) 的有界、无需因子信息的选择规则；
- 全域解提升、terminal 证书，或 E5 严格势下降。

因而下一条决定性工作是为 (16) 构造 source-lineage endpoint interface，或证明所有这类
endpoint 的合法 complete-excess continuation 必定增容；不能再次把 static formal
\(m=1\) node 当作 source/path 回执。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation.py --verify
~~~

复现器只重放 (6)、(9)--(12)、(18)--(22) 以及 (26) 的单个 raw receipt；不扫描参数、
素数或 target 因数分解。
