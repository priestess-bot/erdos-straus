---
kind: claim
claim_id: type-I-root-capacity-stutter-finite-curve-constraint
title: 根容量 stutter 的三参数整数曲线约束
statement: >-
  对核心素数 p≡1 mod24 的 proper-root 实际 maximal receipt，设
  h=3u、h|(p^2+p+1)、R-h=ED、D|K、gcd(h,D)=1，并且非终端 canonical carry
  发生 stutter，即 D≡1-h (mod p)。定义
  m=(D+h-1)/p、e=(ph+1)/D、a=em-h。则 m,e,a 都是正整数，并满足
  D=mp+1-h、p a=e(h-1)+1、D a=m+h(h-1)，以及精确恒等式
  m e^2-e+1=a(p+e)。进一步令
  F(e,m)=e^2m^2-e^2m+e^2+em-2e+1
  =(em-e+1)^2+em(e-1)，则 h|F(e,m)。因此 actual stutter
  receipt 必须落在一条显式整数曲线及其整除交集中；这些条件是必要筛选，
  不是 actual receipt 的充分条件，也不产生 Type I/II 证书或自动递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - integer-curve
  - divisor-filter
  - complete-excess
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-root-receipt-and-divisor-gate
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-receipt-factor-boundary
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: stutter-parameterization-and-relay-boundary
  - reproduction: reproductions/type_i_root_capacity_stutter_finite_curve.py
    role: fixed-arithmetic-controls-and-negative-perturbation
visibility: public
last_checked: '2026-08-14'
---

# 根容量 stutter 的三参数整数曲线约束

## 1. 假设与参数

固定一个核心素数 \(p\equiv1\pmod {24}\) 的 \(a=1,d=1\) 根接口。取一个
proper-root、非 bottom-terminal 的真实 maximal complete-excess 回执

\[
R-h=ED,\qquad D\mid K,\qquad (h,D)=1,\qquad h=3u,\qquad h\mid p^2+p+1.
\tag{1}
\]

沿用根容量端点的 canonical map。假设该回执落在唯一的非严格门

\[
D\equiv1-h\pmod p,\qquad D\mid ph+1.
\tag{2}
\]

这里 \(D\) 必须是实际 maximal receipt 的除数；(2) 不能用任意抽象的
\(ph+1\) 除数替代。

## 2. 三参数恒等式

由 (2) 唯一写成

\[
m=\frac{D+h-1}{p}\in\mathbb Z_{>0},\qquad
D=mp+1-h,
\tag{3}
\]

并置

\[
e=\frac{ph+1}{D}\in\mathbb Z_{>0},\qquad
a=em-h.
\tag{4}
\]

将 \(eD=ph+1\) 和 (3) 相乘展开，得到

\[
\boxed{pa=e(h-1)+1.}
\tag{5}
\]

右端为正，所以 \(a>0\)。再用 (3)、(5) 消去 \(pa\)，有

\[
\boxed{Da=m+h(h-1).}
\tag{6}
\]

另有

\[
D(p+e)=mp^2+p+1,
\tag{7}
\]

而由 \(a=em-h\) 与 (5)，有

\[
me^2-e+1=e(em-h)+e(h-1)+1=a(p+e).
\tag{8}
\]

特别地 \(p+e\mid me^2-e+1\)，但这里的整除只是上述精确商的推论，不能在引入
\(a\) 后再当作独立筛选条件。式 (5)--(8) 是 stutter 的精确整数必要条件，不涉及
近似或范围搜索。

## 3. Cyclotomic 曲线约束

记

\[
F(e,m)=e^2m^2-e^2m+e^2+em-2e+1.
\tag{9}
\]

由 (5) 令 \(X=e(h-1)+1=pa\)。因为 \(h\mid p^2+p+1\)，有

\[
X^2+Xa+a^2=a^2(p^2+p+1)\equiv0\pmod h.
\tag{10}
\]

而模 \(h\) 时 \(a\equiv em\)、\(X\equiv1-e\)，所以 (10) 化为

\[
\boxed{h\mid F(e,m).}
\tag{11}
\]

同时

\[
F(e,m)=(em-e+1)^2+em(e-1),
\tag{12}
\]

给出一个不含 \(p\) 的正整数曲线表达。由 \(F\equiv1\pmod e\) 还得到
\(\gcd(e,h)=1\)（这也可直接由 \(eD=ph+1\) 看出）；由
\(F\equiv(e-1)^2\pmod m\) 得

\[
\gcd(h,m)\mid(e-1)^2.
\tag{13}
\]

这些余数条件可与 actual receipt 的
\(\gcd(D,M_0)=1\)、\(D_C\mid h^2-1\)、\(D_T\mid h^2-h-2r\)
联立，作为下一步排除门；目前尚未得到核心素数上的空性证明。

## 4. 边界与用途

三参数曲线只压缩算术候选，不携带源路径、标记解集或跨分母提升数据。因此：

* 满足 (5)--(13) 的抽象整数元组不一定来自真实 root receipt；
* 即使来自真实 receipt，也不自动给出 \(4/p\) 的 Type I/II 证书或更小分母；
* 任何将该约束升级为全局出口的证明仍须补齐 state contract 的 source、target
  fiber、identity lift 和严格良基势。

一个核心同余但非素数的控制为
\(p=361,h=1029,m=3,e=6754,D=55\)，它满足全部曲线整除式；这说明曲线本身
不能替代核心素数与 actual-receipt 条件。另有非核心素数控制
\(p=67,h=93,m=13,e=8,D=779\)，同样满足算术式，进一步表明不能脱离
\(p\equiv1\pmod {24}\) 与 receipt provenance 宣称门为空。

## 聚焦复现

    python3 reproductions/type_i_root_capacity_stutter_finite_curve.py --verify

脚本只检查两个固定抽象控制、恒等式和一次扰动失败，不执行范围扫描。
