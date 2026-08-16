---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
title: q=1 容量八 V-side 一步 m=1 endpoint 的有限缺陷容量映射
statement: >-
  在合法 zero-k c=8 high-R target 的 primitive source S=(p,V,p-1) 上，取任一
  V-side strict raw prime q 且 q>2(p-1)，并写 a=V/q、h=gcd(a,M)，其中 K=8M。
  则该 raw edge 无 gcd reduction 地到达 m=1 的 bottom node (a,R-a)，有
  h divides 11*41*149，a-side complete-excess canonical multiplier 精确为 T=a/h，
  且其 canonical capacity c 满足 79c+32hq=0 (mod p)。所以 c<8 当且仅当 q 模 p
  落在由 h|67199 和 c=1,...,7 给出的至多 56 个显式剩余类之一。这个映射把 direct
  source-bypass 的潜在 E5 条件化为有限 residue gate；它不证明该 endpoint 已通过
  typed state、bundle、lift 或全局递降准入。p=157393 的实际 c=8 source 控制中，
  q=5963047 给出 h=1、c=11230，故不是降容量边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - raw-path
  - complete-excess
  - capacity-map
  - source-lineage
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: primitive-high-R-source-and-bounded-shared-support
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: complete-excess-lcm-semantics
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-capacity-comparison
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_v_side_direct_m_one_capacity_map.py
    role: exact-multiplier-and-capacity-control
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 \(V\)-side 一步 \(m=1\) endpoint 的有限缺陷容量映射

## 1. 直接进入 bottom layer 的 source 标签

沿用容量八 high-\(R\) normal form和 source-side 分离卡的记号：

\[
p=48s+1,
\qquad K=8M,
\qquad pR+1=4K=32M,
\tag{1}
\]

\[
V=R(p-1)-p,
\qquad (V,K)\mid67199=11\cdot41\cdot149.
\tag{2}
\]

取一个实际 \(V\)-side strict raw 标签 \(q\)，即

\[
q\mid V,
\qquad v_q(V)>v_q(K),
\tag{3}
\]

并额外假设

\[
q>2(p-1).
\tag{4}
\]

source-side 分离已经给出 \((q,pR(p-1))=1\)。所以该步的 shift 为

\[
t=q-(p-1),
\tag{5}
\]

并令

\[
a=\frac Vq.
\tag{6}
\]

由 \(q a=R(p-1)-p\)，原始迁移的另一坐标精确为

\[
\frac{p+Rt}{q}=R-a.
\tag{7}
\]

又 \((p-1+t)/q=1\)，故任何 gcd reduction 都必须整除 \(1\)。于是这不是
formal reverse parent，而是一条无约分的实际 raw receipt：

\[
\boxed{
(p,V,p-1)\xrightarrow{q}(a,R-a,1).}
\tag{8}
\]

条件 (4) 还给出

\[
0<a=\frac{R(p-1)-p}{q}<\frac R2,
\tag{9}
\]

所以 \(a\) 是这个 endpoint 的 bottom coordinate。

## 2. complete-excess multiplier 只有有限共同支撑缺陷

写

\[
h=(a,M).
\tag{10}
\]

因为 \(a\mid V\)，且 \(V\) 为奇数、\(K=8M\)，由 (2) 得

\[
\boxed{h\mid67199.}
\tag{11}
\]

对 \(a\) 侧取完整 complete-excess block \(Q_a\)，并令其相对于现有 support \(M\)
的 canonical multiplier 为

\[
T=\frac{\operatorname{lcm}(M,Q_a)}M.
\tag{12}
\]

逐个奇素数 \(\ell\) 比较 \(r=v_\ell(a)\) 与 \(u=v_\ell(M)=v_\ell(K)\)：若
\(r\le u\)，\(Q_a\) 不携带 \(\ell\)，而 \(T\) 的 \(\ell\)-估值为零；若
\(r>u\)，完整块携带 \(\ell^r\)，而 \(T\) 的估值为 \(r-u\)。两种情形共同给出

\[
\boxed{T=\frac a{(a,M)}=\frac ah.}
\tag{13}
\]

因此所有来自 current support 的不确定性都被压到 (11) 的八个可能缺陷：

\[
\mathcal H=
\{1,11,41,149,451,1639,6109,67199\}.
\tag{14}
\]

这里 (12)--(13) 是 complete-excess 的算术正规化；它本身尚不是已经支付 E1--E5 的
bundle edge。若 \(T=1\)，则 \(Q_a=1\)，没有非平凡 bundle，且下面的 canonical
capacity 恰回到 \(8\)；因此真正的 direct carry 候选还须满足 \(T>1\)。

## 3. 线性容量同余

令 \(c\in\{1,\ldots,p-1\}\) 是 support \(MT\) 的 canonical capacity，即

\[
4MTc\equiv1\pmod p.
\tag{15}
\]

由 (1) 有 \(8\cdot4M\equiv1\pmod p\)，故

\[
Tc\equiv8pmod p.
\tag{16}
\]

另一方面，source 坐标满足

\[
qa=V\equiv-Rpmod p.
\tag{17}
\]

source-side 正规形还有 \(4R\equiv79\pmod p\)。把 (13)、(16)--(17) 合并，得到

\[
\boxed{79c+32hq\equiv0\pmod p.}
\tag{18}
\]

这条式子不含大端点 \(a\)、\(R-a\) 或完整块的因子分解。

## 4. 潜在 E5 的有限 residue gate

在当前容量为 \(8\) 的比较中，direct endpoint 的 canonical capacity 严格更小当且仅当
\(c\in\{1,\ldots,7\}\)。由 (18)，对每个已知缺陷 \(h\in\mathcal H\)，定义

\[
\mathcal C_p(h)=
\left\{
-79r(32h)^{-1}\pmod p:1\le r\le7
\right\}.
\tag{19}
\]

于是有精确等价

\[
\boxed{
c<8
\Longleftrightarrow
q\bmod p\in\mathcal C_p(h),
\qquad h=(V/q,M).}
\tag{20}
\]

所以一次 direct \(m=1\) source bypass 能否给出低于 \(8\) 的容量，并非需要扫描
endpoint 的开放问题：它至多落在 \(8\times7=56\) 条明确的 \(q\)-residue gate 上。
这为后续寻找 actual source-aware E5 edge 提供了有限、可验证的输入接口；但 (20) 不会
把一个命中的 capacity residue 自动升级为 E1--E5。

## 5. 实际控制

在既有 terminal-preempted 的容量八 macro 控制

\[
s=3279,
\qquad p=157393,
\tag{21}
\]

取 source 因子 \(q=5963047\)。它满足 (3)--(4)，且

\[
a=3113076331159817,
\qquad h=(a,M)=1,
\qquad T=a.
\tag{22}
\]

由 (18) 或直接的 canonical rechart 得

\[
c=11230,
\qquad79\cdot11230+32\cdot5963047\equiv0pmod{157393}.
\tag{23}
\]

所以这个真实 non-\(p\) \(m=1\) bypass 不给出降容量。该控制只检验映射和
source transcript；原素数已有 terminal，不能用于声称 persistent selector 失败。

## 6. 作用域

本卡把一个 source-aware 直接分支压缩成有限 residue 条件，严格排除了两种错误推理：

- 不能仅凭 (8) 就宣称 source endpoint 已有 Type I state 或全域 lift；
- 不能仅凭当前 \(c=8\) 就推断 direct complete-excess continuation 增容或降容，必须
  检查 (18)。

尚未闭合的是：对 (19) 命中的真实 \(q\) 因子构造 typed E1--E5 边，或证明这些
有限 gate 在真实 rough \(q_\star=103\) 域中全空。后者是此接口的下一条决定性数学缺口。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_v_side_direct_m_one_capacity_map.py --verify
~~~

复现器只重放 (8)、(13)、(18)--(23) 的一个实际 source 控制；不扫描素数、因子或
历史 target。
