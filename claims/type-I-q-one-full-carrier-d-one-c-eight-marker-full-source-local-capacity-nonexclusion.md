---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-marker-full-source-local-capacity-nonexclusion
title: q=1 容量八 marker 的全 source 局部容量非排除定理
statement: >-
  在真实 q_star=103 的 c=8 double-low marker
  (D,c,c_Sigma,epsilon,g_b)=(1,1,4,0,47) 中，s 为奇数，令
  T=M/47，且 q(rho)=32^{-1}(32p^2+32p-79-47p rho) (mod T)、
  A(rho)=1+p rho。则满足 (A(rho),T)=(q(rho),T)=1 的 rho (mod T)
  数目严格为一个显式正乘积：对每个 ell^e || T、ell not equal to 47，局部因子为
  ell^(e-1)(ell-1-1_{ell does not divide p^2+p-1})；若 47^e || T，局部因子为
  46*47^(e-1)。每一个这样的 rho 唯一决定 t (mod M)，使
  q(rho)(8+pt)=V (mod M)，且 n=(1+p rho)/32 在 T 上为单位。因此全部
  g_b=47 的 source gcd 分配、q/a 的 full-source 模投影，及 marker 的
  rho=-p^(-1) (mod 512)、rho=1 (mod 3)、t=7 (mod 16) 局部射线彼此兼容。
  所以任何只使用 M/47 上的逐素数 unit/gcd 分配、qa=V (mod M) 和有限
  2-adic carry 信息的排除，不能关闭 marker；必须加入整数等式 qa=V、素数/高度、
  跨 source 的不等式、terminal 或 typed/descent 信息。本结论不构造 actual marker
  endpoint，也不否定这些更强条件可能给出全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
  - type-I-q-one-full-carrier-d-one-c-eight-marker-affine-lift-source-allocation
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - q-star-103
  - marker
  - source-allocation
  - local-capacity
  - nonexclusion
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
    role: unique-zero-carry-marker
  - claim: type-I-q-one-full-carrier-d-one-c-eight-marker-affine-lift-source-allocation
    role: exact-rho-lift-and-source-gcd-allocation
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: c-eight-source-normal-form-and-D-one-unit-condition
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_marker_full_source_local_capacity_nonexclusion.py
    role: local-capacity-count-and-two-branch-formal-controls
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 marker 的全 source 局部容量非排除定理

## 1. 要排除的仅是 source-local 方案

保留唯一 zero-carry marker

\[
(D,c,C,\epsilon,g_b)=(1,1,4,0,47)
\tag{1}
\]

及容量八 source

\[
p=48s+1,
\qquad M=9sLE,
\qquad
L=176s+5,
\qquad E=3168s^2+24s-1.
\tag{2}
\]

前一条仿射 lift 已证明 actual marker 必有 \(s\) 奇、

\[
T:=\frac{M}{47}\ \text{为奇数},
\qquad
(V,M)=1,
\qquad
(p,T)=1,
\tag{3}
\]

最后一项也直接来自 \(pR+1=32M\)。

并且对某个整数 \(\rho\)，

\[
32n=1+p\rho,
\qquad
q=p^2+p-1-47n,
\qquad
(n,T)=1.
\tag{4}
\]

这里考察的不是 \(q\mid V\) 的完整整数条件，而是它在所有旧 source
素因子上的同时投影。由于 \((2,T)=1\)，定义

\[
\begin{aligned}
A(\rho)&:=1+p\rho,\\
Q(\rho)&:=32^{-1}\bigl(32p^2+32p-79-47p\rho\bigr)\pmod T.
\end{aligned}
\tag{5}
\]

若 (4) 成立，则 \(Q(\rho)\equiv q\pmod T\)。令

\[
\mathcal R_T=
\{\rho\pmod T:(A(\rho),T)=(Q(\rho),T)=1\}.
\tag{6}
\]

第一项正是 \((n,T)=1\) 的单位版本；第二项是 actual \(q\mid V\)、
\((V,M)=1\) 所必需的 \(q\)-unit 条件。

虽然 \(Q\) 只写在模 \(T\) 下，\(\rho\pmod T\) 仍唯一决定 \(q\) 的模 \(M\)
投影：令

\[
\widetilde Q(\rho):=
32^{-1}\bigl(32p^2+32p-79-47p\rho\bigr)\pmod M.
\tag{6a}
\]

把 \(\rho\) 替换为 \(\rho+T\) 时，分子只改变 \(-47pT=-pM\)，故 (6a) 的定义
确实不依赖代表元。它在模 \(T\) 下化为 \(Q\)。

## 2. 精确局部容量

设 \(\ell^e\Vert T\)。若 \(\ell\ne47\)，则 \(A\) 与 \(Q\) 都是
\(\rho\) 的非退化仿射式。它们的非单位根在模 \(\ell\) 下重合，当且仅当

\[
\ell\mid p^2+p-1.
\tag{7}
\]

事实上，将 \(A(\rho)=0\) 即 \(p\rho=-1\) 代入 (5)，得到

\[
Q(\rho)\equiv p^2+p-1\pmod\ell.
\tag{8}
\]

所以在模 \(\ell^e\) 下可选的 \(\rho\) 数恰为

\[
N_\ell=
\ell^{e-1}
\left(\ell-1-\mathbf 1_{\ell\nmid p^2+p-1}\right).
\tag{9}
\]

这始终为正，因为 \(T\) 为奇数。

剩下的 \(47\)-primary 也不产生空洞。已有 source 分解给出

\[
47\mid M
\Longleftrightarrow
s\equiv0\ \text{或}\ 20\pmod {47},
\tag{10}
\]

相应地 \(p\equiv1\) 或 \(21\pmod {47}\)。故

\[
Q(\rho)\equiv p^2+p-1\equiv1\ \text{或}\ 38\pmod {47},
\tag{11}
\]

与 \(\rho\) 无关且为单位。若 \(47^e\Vert T\)，唯一要排除的仍是
\(A(\rho)\equiv0\pmod {47}\)，于是

\[
N_{47}=46\cdot47^{e-1}.
\tag{12}
\]

中国剩余定理现在给出精确的全 source 容量：

\[
\boxed{
|\mathcal R_T|
=
\prod_{\substack{\ell^e\Vert T\\\ell\ne47}}
\ell^{e-1}
\left(\ell-1-\mathbf 1_{\ell\nmid p^2+p-1}\right)
\cdot
\prod_{47^e\Vert T}46\cdot47^{e-1}>0.}
\tag{13}
\]

第二个乘积在 \(47\nmid T\) 时按 \(1\) 解释。这个公式同时覆盖 \(s\)、\(L\)
和 \(E\) 的所有素因子，而不是逐个 source factor 的启发式检查。

## 3. q/a 投影与 marker 的二进射线可同时实现

取任意 \(\rho\in\mathcal R_T\)。由 (11)，\(\widetilde Q(\rho)\) 在模 \(47\)
下为单位；它又在模 \(T\) 下为单位。因此 \(\widetilde Q(\rho)\) 是模 \(M\) 的
单位。因为 \((V,M)=1\)，定义

\[
a_\rho\equiv V\widetilde Q(\rho)^{-1}\pmod M,
\qquad
t_\rho\equiv p^{-1}(a_\rho-8)\pmod M.
\tag{14}
\]

它们唯一，并满足

\[
\widetilde Q(\rho)(8+pt_\rho)\equiv V\pmod M,
\qquad
(8+pt_\rho,M)=1.
\tag{15}
\]

它在模 \(T\) 下正是原来的 \(Q(\rho)(8+pt_\rho)\equiv V\pmod T\)。
在 distinguished \(47\) 上，它还强制

\[
a_\rho\equiv R\pmod {47},
\qquad b=R-a_\rho\equiv0\pmod {47}.
\tag{15a}
\]

确切地说，\(pR+1\equiv0\pmod {47}\) 及
\(\widetilde Q\equiv p^2+p-1\pmod {47}\) 给出

\[
\widetilde Q R-V
\equiv R(p^2+p-1)-\bigl(R(p-1)-p\bigr)
=p(pR+1)\equiv0\pmod {47}.
\tag{15b}
\]

而 \(\widetilde Q\) 为单位，故 (15a) 随之成立。这正是不能从 \(M/47\) 投影中
省去、但也不减少 \(\rho\) 容量的一条线性条件。
因此每个 \(\rho\) 同时实现 \(q\)、\(a\)、\(n\) 的全部 source-unit 条件和完整
source 同余。
特别地，若把 \(\rho\) 提升为

\[
p\rho\equiv-1\pmod {512},
\tag{16}
\]

则 (4) 中的 \(n,q\) 都是整数，且

\[
q\equiv1\pmod {16}.
\tag{17}
\]

这里不会同 \(T\) 的 \(3\)-primary 条件冲突。因为 \(p\equiv1\pmod3\)，
模 \(3\) 时 (6) 唯一保留

\[
\rho\equiv1,
\qquad Q(\rho)\equiv2,
\qquad a_\rho\equiv1,
\qquad t_\rho\equiv2\pmod3.
\tag{18}
\]

而 \((512,T)=1\)，故 (16) 与任意 \(\rho\in\mathcal R_T\) 可由 CRT 合并；
再将 (14) 的 \(t_\rho\) 与

\[
t\equiv7\pmod {16}
\tag{19}
\]

合并，便得到 marker 已知的

\[
\rho\equiv1\pmod3,
\qquad t\equiv23\pmod {48},
\qquad a=8+pt\equiv15\pmod {16}.
\tag{20}
\]

此外，(16) 的整数 lift 满足

\[
p^2+p-1-q=47n,
\qquad (n,T)=1,
\tag{21}
\]

从而确实有

\[
\gcd(M,p^2+p-1-q)=47.
\tag{22}
\]

所以已有的 \((S_{\rm odd},1+\rho)=1\)、
\((L_0,4\rho-11)=1\)、\((E,A)=1\) 不是额外的 local 排除：它们已被 (6)
的 full-source 单位条件同时容纳。

## 4. 路线边界

(13)--(22) 只构造 marker 的完整 **source-local projection**。它不声称

\[
q(8+pt)=V
\tag{23}
\]

作为整数等式，也不声称 \(q\) 是正的 high raw prime，或 \(a,b=R-a\) 为合法
endpoint。因此它绝不构造 actual marker。

它排除的是更窄但此前仍未切断的设想：把 \(q\mid V\) 降为整个 \(M\) 上的同余后，
再与 \(g_b=47\)、三类 source gcd 分配和有限二进 carry 条件联用，不可能导出矛盾。
该局部系统对每个允许 source 都有显式正容量。

故 marker 研究在这里必须停止继续做 source-local 素数分配。下一条可产生全称出口的
路线必须至少使用以下一项尚未投影的信息：

- (23) 的精确整数整除及其高度/不等式后果；
- \(q\) 的素性和 \(q>2(p-1)\) 的全局因子结构；
- 跨 source factor 的非局部耦合，且不能仅化为单位条件；
- terminal-first、typed admission 或已有 parent macro 的可提升 strict descent。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_marker_full_source_local_capacity_nonexclusion.py --verify
~~~

复现器只检查局部容量公式、CRT 合并和 \(47\mid s\)、\(47\mid L\) 的两个明确标为
formal 的控制；不搜索 source、素数、\(V\) 因子或 terminal。
