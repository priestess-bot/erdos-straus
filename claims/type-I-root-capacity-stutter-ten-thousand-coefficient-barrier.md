---
kind: claim
claim_id: type-I-root-capacity-stutter-ten-thousand-coefficient-barrier
title: 根容量实际 stutter 的 10000 系数排除带
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，
  令 h=3u、m=(D+h-1)/p、eD=ph+1、a=em-h。则 a(m-1)≥10000，因而
  h^2>10000p。该结论以 root-divisor gate 的精确有限枚举证明：在
  a(m-1)<10000 的全部 8549 个同余允许参数对中，只有 60 个 (m,a,u) 通过
  gate 整性；其中 17 个满足 p≡1 mod24，且均非素数。因此没有实际核心素数
  root-stutter 可位于该系数带。它只排除 arithmetic stutter，不构造 Type I/II
  证书、解提升、E1--E5 递归边或全局势。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-actual-small-root-exclusion
  - type-I-root-capacity-stutter-pair-root-divisor-gate
  - type-I-root-capacity-stutter-positive-definite-norm-bound
topics:
  - type-I
  - root-capacity
  - stutter
  - hard-root
  - coefficient-barrier
  - height-bound
  - finite-menu
  - computer-assisted-proof
  - strict-carry
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-m-a-congruence-and-height-identities
  - claim: type-I-root-capacity-stutter-pair-root-divisor-gate
    role: finite-u-divisor-gate-and-p-reconstruction
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-m-less-than-h
  - reproduction: reproductions/type_i_root_capacity_stutter_ten_thousand_coefficient_barrier.py
    role: deterministic-exhaustive-coefficient-gate-verifier
visibility: public
last_checked: '2026-08-14'
---

# 根容量实际 stutter 的 \(10000\) 系数排除带

## 1. 结论

固定核心素数

\[
p\equiv1\pmod {24}.
\]

terminal-first 后，设一个 actual proper-root maximal complete-excess receipt 仍落在
stutter 门中。沿用

\[
h=3u,\qquad
D=mp+1-h,\qquad
eD=ph+1,\qquad
a=em-h.
\tag{1}
\]

则有

\[
\boxed{a(m-1)\ge10000.}
\tag{2}
\]

结合已有的

\[
h^2-h+m=aD,\qquad
D\ge(m-1)p+2,\qquad
m<1+\sqrt h<h,
\tag{3}
\]

立即得到

\[
\boxed{h^2>10000p.}
\tag{4}
\]

因此任何满足 \(h^2\le10000p\) 的 actual proper-root receipt，在 terminal-first
之后都不可能停在 canonical stutter；其 cofactor 必已算术严格。

这是一个有限、确定性的系数门排除，不是对 \(p\)、分母或历史 selector 的范围扫描。

## 2. 实际 stutter 的有限必要门

已有 actual-root 条件给出

\[
m\ge3,\qquad
m\not\equiv2\pmod3,\qquad
a\equiv1\pmod2,
\tag{5}
\]

\[
m\equiv0\pmod3\Longrightarrow a\equiv0\pmod3,
\qquad
m\equiv1\pmod3\Longrightarrow a\equiv2\pmod3.
\tag{6}
\]

令

\[
L=am,\qquad s=m-a,\qquad
\mathcal B=L^2+Ls+s^2.
\tag{7}
\]

parameter-pair root-divisor gate 对 actual stutter 强制

\[
(u,6)=1,\qquad
u\mid\mathcal B,\qquad
m\mid a+3u,
\tag{8}
\]

\[
L\mid 9u^2+3(a-1)u+s,
\qquad
p=\frac{9u^2+3(a-1)u+s}{L}.
\tag{9}
\]

任一 actual stutter 都必须出现在 (5)--(9) 生成的有限表中；(8) 允许逐一枚举
\(\mathcal B\) 的全部正除子，而不必枚举 \(p\) 或 \(r\)。

## 3. \(10000\) 以下的精确穷尽

反设

\[
a(m-1)<10000.
\tag{10}
\]

于是

\[
3\le m\le10000,\qquad
1\le a\le\left\lfloor\frac{9999}{m-1}\right\rfloor.
\tag{11}
\]

复现器按 (5)--(6) 先生成全部 \(8549\) 个 \((m,a)\) 对。对每一对，它对
\(\mathcal B(m,a)\) 的每个正除子 \(u\) 测试 (8)--(9)，并重建

\[
e=\frac{a+3u}{m},\qquad
D=mp+1-3u.
\tag{12}
\]

它额外直接核对 \(eD=3pu+1\) 与 \(a=em-3u\)，避免把一个只通过除法的
实现错误登记为 stutter 参数。

结果如下：

| 筛选层 | 精确数量 |
| --- | ---: |
| 满足 (5)--(6) 且 (10) 的 \((m,a)\) | 8549 |
| 通过 (8)--(9) 的 \((m,a,u)\) | 60 |
| 其中 \(p\equiv1\pmod {24}\) | 17 |
| 其中 \(p\) 为素数 | 0 |

为使最后一步可独立复核，17 个核心同余的 \(p\) 值只包含

\[
1\ (\text{出现 12 次}),\quad25,\quad54481,\quad709801,\quad
23170945,\quad145035865.
\tag{13}
\]

后四个非平凡值分别有分解

\[
\begin{aligned}
54481&=7\cdot43\cdot181,\\
709801&=17\cdot43\cdot971,\\
23170945&=5\cdot7\cdot41\cdot67\cdot241,\\
145035865&=5\cdot13\cdot59^2\cdot641.
\end{aligned}
\tag{14}
\]

所以 (10) 与核心素数条件矛盾，证得 (2)。这里甚至尚未需要将通过门的合数候选提升为
完整 root receipt；因为 actual receipt 必先满足核心素数门，故该必要门已经足够排除
整个低系数区域。

## 4. 高度推论与边界

由 (2)--(3)，

\[
h^2-h+m=aD
\ge a(m-1)p+2a
\ge10000p+2a.
\tag{15}
\]

又 \(m<h\)，左端严格小于 \(h^2\)，从而得到 (4)。

这个常数带与既有 \(p^{2/3}\) 高度墙相容，并实质收缩了可发生 stutter 的 root
区域；但它并不产生 Type I/II 证书、较小分母 \(n<p\) 的解、全域 identity lift、
target contract 或严格全局势。带外 hard-root 仍须由 canonical \(D,E\) provenance
或新的 terminal/descent adapter 关闭。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_ten_thousand_coefficient_barrier.py --verify
~~~

该程序只对 \(a(m-1)<10000\) 的数学必要门作精确有限穷尽，使用标准库整数分解和
确定性素性试除；它不扫描素数区间、分母、selector history 或已有测试集。
