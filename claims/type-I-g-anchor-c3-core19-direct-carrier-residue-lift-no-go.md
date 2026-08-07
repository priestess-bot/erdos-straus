---
kind: claim
claim_id: type-I-g-anchor-c3-core19-direct-carrier-residue-lift-no-go
title: c=3 core-19 的直接载体余数 Type II q=19 提升障碍
statement: 在 c=3 high-R chart 中令 h=8+19u、p=24h+1、M0=26h+1、K=M0(p-3)、M1=K/19。若一个 Type II q=19 来源标签必须方向保持地满足 b=M_i (mod p) 及 0<b<p/4，则 i=0 时唯一可能 b=r0=(p-1)/12，但 p+4r0=10 (mod 19)；i=1 时唯一正标准余数 r1=(63p+1)/76 已满足 r1>p/4。故两行都不能提供同时具有范围和正 q=19 高度的直接载体余数标签。该结论只否定 b=M_i (mod p) 的直接 lift，不否定 signed、仿射或其它 nonnative source map。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-c19-atomic-reset
  - type-II-source-fiber-qheight-kneser-bridge
topics:
  - type-I
  - type-II
  - c3
  - core19
  - source-map
  - carrier-remainder
  - q-adic-height
  - range-gate
  - no-go
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_core19_direct_carrier_residue_lift_no_go.py
    role: symbolic core-19 carrier-remainder and q-height verifier
visibility: public
last_checked: '2026-08-07'
---

# c=3 core-19 的直接载体余数 Type II \(q=19\) 提升障碍

这张卡只审计一类自然但过强的整数 lift：把 raw leaf 的载体直接取为 Type II
来源标签的模 \(p\) 余数。它给出严格 no-go，同时明确保留非原生映射的空间。

## 1. 两条 core-19 载体行

令

\[
h=8+19u,\qquad
p=24h+1,\qquad
R=104h-9,
\tag{1}
\]

并写

\[
M_0=26h+1,\qquad
C_0=p-3,\qquad
K=M_0C_0,\qquad
M_1=\frac K{19}.
\tag{2}
\]

因为 \(h\equiv8\pmod {19}\)，有 \(19\mid M_0\)，所以 \(M_1\) 是整数。两行分别
对应 \(C_0=p-3\) 与 \(C_1=19\) 的 carrier。设

\[
r_i\in\{1,\ldots,p-1\},\qquad r_i\equiv M_i\pmod p.
\tag{3}
\]

这里考虑的 direct lift contract 是

\[
\boxed{
b\equiv M_i\pmod p,\qquad
0<b<\frac p4,\qquad
19\mid p+4b.}
\tag{4}
\]

最后一个条件正是 Type II 来源纤维中 \(q=19\) 的正高度门。

## 2. 两个标准余数

由

\[
M_0=\frac{13p-1}{12}
=p+\frac{p-1}{12},
\tag{5}
\]

得到

\[
r_0=\frac{p-1}{12}=2h.
\tag{6}
\]

因此 \(0<4r_0<p\)，但

\[
p+4r_0=32h+1\equiv10\pmod {19}.
\tag{7}
\]

另一方面 \(p\equiv41\pmod {76}\)，而

\[
4\cdot19M_1=pR+1\equiv1\pmod p.
\tag{8}
\]

所以

\[
r_1=\frac{63p+1}{76},
\tag{9}
\]

确为 \(M_1\) 的标准余数。它满足

\[
0<r_1<p,\qquad
4r_1-p=\frac{44p+1}{19}>0.
\tag{10}
\]

## 3. 直接余数 no-go

**定理。** 对 (1)--(2) 的每个 \(u\ge0\)，(4) 对 \(i=0,1\) 都不可能成立。

**证明。** 因 \(0<b<p/4<p\)，任何满足 \(b\equiv M_i\pmod p\) 的正标签只能是
标准余数 \(r_i\)。对 \(i=0\)，式 (6) 是唯一范围内候选，但式 (7) 排除
\(19\mid p+4r_0\)。对 \(i=1\)，式 (10) 直接排除范围门。证毕。

特别地，\(r_1\) 正是固定 \(C=19\) RESET 中的
\((63p+1)/76\)：它天然有 \(19\)-方向的同余，却总在 Type II 小标签范围之外；
\(r_0\) 则恰好相反。

## 4. 控制与边界

复现器以 \(p=193\)、\(p=6121\) 和既有 v=5 点
\(p=1202376916441\) 检查同一组仿射恒等式。后者给

\[
(r_0,r_1)=(100198076370,996707180734).
\]

本定理没有宣称任意可行 source-map 都保留 \(b\equiv M_i\pmod p\)。带方向的 mark、
额外仿射平移、新的 \(D_*\) 或非 carrier 标签都在范围之外；它们必须各自提供完整的
整数来源、范围、q-height 和 physical-slot 回执。
