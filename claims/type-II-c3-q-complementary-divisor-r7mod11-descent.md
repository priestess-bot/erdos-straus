---
kind: claim
claim_id: type-II-c3-q-complementary-divisor-r7mod11-descent
title: c=3 中 q=(p+11)/12 的 7 mod 11 互补因子 Type II 递降
statement: 令 p=24h+1 为核心素数、q=2h+1=(p+11)/12。若 q 有因子 r=7 (mod 11)，令 d=q/r、c=(3r+1)/11、x=3q，则 m=11 满足 m|(x+d)，并显式给出 4/p=1/(3q)+1/(pcd)+1/(3pcq)。同一数据给出严格 two-tail descent 4/q=1/(3q)+1/(cd)+1/(3cq)，其中 q<p。该选择律包含原 h=3+42u 分支的 r=7 证书，也给出避开固定小扇的新 r=29 ray。任意有限个固定 r 候选都不能覆盖全部 c=3 核心素数；本卡只处理 r=7 (mod 11) 子扇，完整 gap-11 因子对选择器及其互补残余见 type-II-factor-pair-carrier-strict-descent。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-p-plus-12-36-divisor-terminal-fan
  - type-II-affine-uniform-divisor-rigidity
  - denominator-escape-state-contract
topics:
  - type-II
  - c3
  - terminal-first
  - short-certificate
  - strict-descent
  - complementary-divisor
  - adaptive-factor
  - proof-boundary
sources:
  - claim: type-II-p-plus-12-36-divisor-terminal-fan
    role: type-II-parameterization-and-terminal-semantics
  - claim: type-II-affine-uniform-divisor-rigidity
    role: uniform-affine-boundary
  - concept: denominator-escape-state-contract
    role: terminal-first-and-lift-contract
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 中 \(q=(p+11)/12\) 的 \(7\pmod{11}\) 互补因子递降

## 1. 选择律与直接证书

令

\[
p=24h+1,
\qquad
q=2h+1=\frac{p+11}{12},
\qquad
p=12q-11.
\tag{1}
\]

假设存在正因子

\[
r\mid q,
\qquad
r\equiv7\pmod{11}.
\tag{2}
\]

定义

\[
d=\frac qr,
\qquad
c=\frac{3r+1}{11},
\qquad
x=3q.
\tag{3}
\]

**定理（互补因子 Type II 终端）。** 数据 (1)--(3) 给出一个实际的 Type II
三分分解

\[
\boxed{
\frac4p
=\frac1{3q}
+\frac1{pcd}
+\frac1{3pcq}.}
\tag{4}
\]

**证明。** 由 (1) 有

\[
x=\frac{p+11}{4}.
\tag{5}
\]

而 (2)--(3) 给出

\[
x+d=3q+\frac qr=d(3r+1)=11cd.
\tag{6}
\]

因此 \(11\mid x+d\)，且 \(d\mid q\mid x^2\)。Type II 参数化于是给出

\[
y=\frac{p(x+d)}{11}=pcd,
\qquad
z=\frac{px(x+d)}{11d}=3pcq,
\tag{7}
\]

即 (4)。证毕。

## 2. 严格 two-tail descent

同一组 \((q,r,d,c)\) 还满足

\[
\boxed{
\frac4q
=\frac1{3q}
+\frac1{cd}
+\frac1{3cq}.}
\tag{8}
\]

事实上，把 (3) 代入，右端乘以 \(3cq\) 后的分子为

\[
c+3r+1=12c.
\tag{9}
\]

这正等于 \(4/q\) 所需的分子。由于

\[
q=\frac{p+11}{12}<p,
\tag{10}
\]

\((8)\) 是严格的较小实例；\((4)\) 通过保留第一分母 \(3q\)、并将后两尾乘以 \(p\)
把它提升回 \(p\)。因此选择律 \((2)\) 同时提供短证书和可提升严格递降。

## 3. 原 \(h=3+42u\) 分支被 terminal-first 抢占

若

\[
h=3+42u,
\qquad
p=1008u+73,
\tag{11}
\]

则

\[
q=7(12u+1).
\tag{12}
\]

在定理中取 \(r=7\)，便有 \(c=2\)、\(d=12u+1\)，从而

\[
\frac4{1008u+73}
=\frac1{21(12u+1)}
+\frac1{2(12u+1)(1008u+73)}
+\frac1{42(12u+1)(1008u+73)}.
\tag{13}
\]

对应的严格来源是

\[
\frac4{84u+7}
=\frac1{21(12u+1)}
+\frac1{2(12u+1)}
+\frac1{42(12u+1)}.
\tag{14}
\]

所以原 \((a,b)=(7,2)\) raw-word 族的一切实例都应在 terminal-first 阶段由
(13) 停止；无论中间标签是素数还是复合数，都不增加该族的未解决覆盖。

## 4. 一个不属于固定小扇的新 ray

取

\[
h=6699w+217,
\qquad
p=160776w+5209,
\qquad
q=29(462w+15).
\tag{15}
\]

这里取 \(r=29\equiv7\pmod{11}\)，于是 \(c=8\)、\(d=462w+15\)，故 (4)
对每个使 \(p\) 为素数的 \(w\) 成立。又

\[
(5209,160776)=1,
\tag{16}
\]

所以 Dirichlet 定理给出无穷多个这样的核心素数。基点 \(w=0\) 给出

\[
\frac4{5209}
=\frac1{1305}
+\frac1{625080}
+\frac1{54381960},
\tag{17}
\]

并严格递降到

\[
\frac4{435}
=\frac1{1305}
+\frac1{120}
+\frac1{10440}.
\tag{18}
\]

这一 ray 恒有 \(p\equiv1\pmod7\) 与 \(p\equiv6\pmod{11}\)，所以它避开了依赖
固定小除子的既有 \(m=7\) 与 \(m=11\) 同余扇。这里的有效性来自 \(q\) 的互补因子，
而非另加一个固定常数模板。

## 5. 有限固定 \(r\)-扇的不完备性

**定理（有限扇 no-go）。** 令 \(\mathcal R\) 是任意有限个满足
\(r\equiv7\pmod{11}\) 的正整数候选，令

\[
L=\operatorname{lcm}_{r\in\mathcal R}r.
\tag{19}
\]

则存在无穷多个 \(c=3\) 核心素数 \(p\)，使得没有任何 \(r\in\mathcal R\) 整除
对应的 \(q=(p+11)/12\)。

**证明。** 令

\[
h=3Lw,
\qquad
p=72Lw+1,
\qquad
q=6Lw+1.
\tag{20}
\]

Dirichlet 定理给出无穷多个素数 \(p\equiv1\pmod{72L}\)。这些 \(h\) 都满足
\(h\equiv0\pmod3\)，故位于 \(c=3\) 分支；且对每个 \(r\in\mathcal R\)，有

\[
q\equiv1\pmod r,
\tag{21}
\]

从而 \(r\nmid q\)。证毕。

因此下一步不是添加更多固定 \(r\)。固定 \(r\) 的 no-go 只针对本卡的
\(r\equiv7\pmod{11}\) 子扇；完整 gap \(11\) Type II 层应改用互素因子对及
signed-ratio box 选择，见 type-II-factor-pair-carrier-strict-descent。

## 6. 合同边界

\((4)\) 是直接 terminal，\((8)\) 是严格且可提升的较小实例；两者都在任何 raw root-entry
之前执行。它们不依赖形式 \(p\)-parent，也不把未命中 \((2)\) 的 \(p\) 解释成反例或
递归状态。有限扇 no-go 只排除有限候选集，既不排除自适应因子选择，也不排除 Type I、
非线性除子或其他 Type II 分支。尤其是，它不排除同一 gap 的 \(r\equiv8,10\) 低尺度
分支或 \(A>3\) 的完整因子对分支。
