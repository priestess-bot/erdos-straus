---
kind: claim
claim_id: type-I-high-support-c4-first-bundle-dual-r7-boundary
title: C=4 第一 bundle 双对偶的 R=7 边界与 p=1801 压力点
statement: 对每个核心素数 p=25 (mod 48)，C=4 最小高支撑正分支的第一 canonical complete-excess target 满足 M=A(2p+1)、R_M=R(2p+1)+2、K_M=4M。令 d=p-4、r=M mod p、s=(4rd+1)/p，则 r=(7p+1)/16、s=(7p-27)/4，d 对偶的 R_d=(9p-37)/4>p，r 对偶固定为 R_r=7、K_r=(7p+1)/4。因 M>K_r，r 对偶不能保留第一 target 的 charged support。p=1801 上 H0、H1 与 R=7 对偶均为 Jacobi G，且 x_7=(p+7)/4 的所有素因子都是模 7 二次剩余，因此该 C=4 第一 bundle 路径不能由这两个 determinant 对偶加 gap-7 factor-pair 分支关闭。这是受限选择器的严格压力边界，不是 Erdos--Straus 反例，也不声称 p=1801 没有其它 gap 或外层出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-c4-canonical-stutter-boundary
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-support-preserving-dual-criterion
  - type-II-factor-pair-carrier-strict-descent
  - denominator-escape-state-contract
topics:
  - type-I
  - high-support
  - c4-boundary
  - overflow
  - determinant-dual
  - r7
  - Jacobi-G
  - type-II-gap-seven
  - pressure-point
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_support_c4_first_bundle_dual_r7_boundary.py
    role: closed-form-duals-and-p1801-pressure-receipt
  - claim: type-I-high-support-c4-canonical-stutter-boundary
    role: first-C4-bundle-chart
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: determinant-dual-normal-form
  - claim: type-II-factor-pair-carrier-strict-descent
    role: gap-seven-factor-pair-criterion
visibility: public
last_checked: '2026-08-12'
---

# C=4 第一 bundle 双对偶的 \(R=7\) 边界与 \(p=1801\) 压力点

## 1. 问题范围

已有 C=4 正分支从

\[
R=4p+3,\qquad
A=\frac{pR+1}{16},\qquad
K=4A
\]

开始。令

\[
Q=2p+1,\qquad
M=AQ,\qquad
R_M=RQ+2,\qquad
K_M=4M.
\tag{1}
\]

这正是第一张 canonical complete-excess target chart。这里研究的是该 target
overflow 的 determinant 双对偶；结论只约束这条可复核的局部选择器路径。

## 2. 双对偶闭式

令

\[
d=p-4,\qquad r=M\bmod p,\qquad
s=\frac{4rd+1}{p}.
\tag{2}
\]

由

\[
A=\frac{4p^2+3p+1}{16}
\]

及 \(p\equiv9\pmod {16}\)，有

\[
M=A(2p+1)\equiv 16^{-1}
\equiv \frac{7p+1}{16}\pmod p.
\]

取 \(1\le r<p\)，得到

\[
\boxed{r=\frac{7p+1}{16}}.
\tag{3}
\]

于是

\[
4rd+1
=4\frac{7p+1}{16}(p-4)+1
=p\frac{7p-27}{4},
\]

所以

\[
\boxed{s=\frac{7p-27}{4}}.
\tag{4}
\]

两个 determinant 对偶图表分别为

\[
R_d=4d-s
=\boxed{\frac{9p-37}{4}},
\qquad
R_r=4r-s
=\boxed{7},
\tag{5}
\]

\[
K_d=d(p-r),
\qquad
K_r=r(p-d)=4r
=\boxed{\frac{7p+1}{4}}.
\tag{6}
\]

对 \(p\ge73\)，

\[
R_d-p=\frac{5p-37}{4}>0,
\]

故 d 对偶不是更小图表；唯一的小对偶固定为 \(R=7\)。同时

\[
M-K_r
=A(2p+1)-4r>0,
\]

所以 \(R=7\) 图表的支撑 \(K_r\) 小于第一 target 的 charged support \(M\)，不能作为
保持旧支撑的 E1--E5 边。特别地，这不是“找到一个小图表”就已经完成递降：
支撑承诺丢失必须由显式 outer-rank reset、alternate 或其它证书支付。

## 3. \(p=1801\) 严格压力点

复现脚本给出

\[
\begin{array}{c|c|c}
\text{chart}&R&K\\ \hline
H_0&7207&3244952\\
H_1&25966823&11691562056\\
R=7\text{ dual}&7&3152
\end{array}
\]

其中

\[
H_0:\ K=2^3\cdot43\cdot9433,
\]

\[
H_1:\ K=2^3\cdot3\cdot43\cdot1201\cdot9433,
\]

\[
R=7:\ K=2^4\cdot197.
\]

对三个图表的每一个 \(K\)-素因子，Jacobi 符号均为 \(+1\)，而
\(\left(\frac{-1}{R}\right)=-1\)。因此三个图表都是 G；特别是 \(R=7\) 的有限
Type I 盒只产生 \(\{1,2,4\}\)，不含 \(-1\equiv6\pmod7\)。

同一个 \(p\) 的 gap-7 因子对载体为

\[
x_7=\frac{p+7}{4}=452=2^2\cdot113.
\]

其素因子模 7 分别为 \(2,1\)，全是二次剩余。由于
\(\operatorname{QR}_7=\{1,2,4\}\)，现有 gap-7 factor-pair 判据不能产生
Type II 终端或相应的严格两尾递降。

因此，\(p=1801\) 明确排除了以下局部闭合假设：

1. C=4 第一 bundle 的 overflow 总能由 d/r 双对偶之一保留旧支撑并下降；
2. 若双对偶落到 \(R=7\)，gap 7 factor-pair 总能接管。

这仍然不是猜想反例：其它 gap、非 determinant carrier、Type I alternate、外层
reset 或已有终端菜单均未在本卡中穷举。它真正证明的是，下一步必须构造一个支付
支撑丢失的全局 selector，或找到不依赖 \(R=7\) 的新证书。

## 4. 复现

~~~bash
python3 reproductions/type_i_high_support_c4_first_bundle_dual_r7_boundary.py --verify
~~~

输出：

~~~text
verified C=4 first-bundle dual R=7 boundary and p=1801 pressure point
~~~
