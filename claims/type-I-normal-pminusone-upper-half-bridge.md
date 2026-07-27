---
kind: claim
claim_id: type-I-normal-pminusone-upper-half-bridge
title: Type I 正规形的 p减一桥判据与上半区性质
statement: 设核心素数p的Type I正规形满足4K=pR+1，并写R=4r-1、t=(p-1)/4。保持前两项并取源n=p-1的最大尾反向桥存在，当且仅当r|t^2；此时桥因子唯一为E=R+1=4r，且E<2K。因此每个正常形p减一桥自动对应小侧普通除子对，并有上半区偶源n=p-1≥(p+1)/2。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- p-minus-one
- terminal-bridge
- upper-half-source
- square-divisibility
- divisor-pairs
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-divisor-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# Type I 正规形的 p 减一桥判据与上半区性质

设核心素数 \(p\equiv1\pmod {24}\) 已有一张 Type I 正规形，其最大尾尺度满足

\[
4K=pR+1,
\qquad R=4r-1,
\qquad t=\frac{p-1}{4}. \tag{1}
\]

这里不假定此正规形对任意 \(p\) 都存在；结论只刻画**固定正规形**能否以 \(p-1\) 为源。

## 定理

保持前两项、把最大尾反向提升到

\[
n=p-1
\tag{2}
\]

的偶终端桥存在，当且仅当

\[
r\mid t^2. \tag{3}
\]

命中时桥因子被唯一强制为

\[
E=4K-(p-1)R=R+1=4r. \tag{4}
\]

它总是小侧：若 \(L=2K\)，则

\[
E<L. \tag{5}
\]

所以它对应[小侧普通除子对](type-I-normal-even-source-small-side-simplification.md)中的
\(a<b\)，并且源满足

\[
n=p-1\ge\frac{p+1}{2}. \tag{6}
\]

## 证明

由 (1)，

\[
4K=p(4r-1)+1=4pr-(p-1)=4(pr-t),
\]

因而

\[
K=pr-t\equiv-t\pmod r. \tag{7}
\]

若源为 (2)，反向桥公式唯一给出 (4)。该 \(E\) 是 \(4\) 的倍数，满足
\(E\equiv1\pmod R\)，而 \(n\) 为偶数。桥的唯一非自动整除条件为

\[
E\mid4K^2
\quad\Longleftrightarrow\quad
4r\mid4K^2
\quad\Longleftrightarrow\quad
r\mid K^2
\quad\Longleftrightarrow\quad
r\mid t^2,
\]

最后一步使用 (7)。桥的自然范围也自动成立，因为

\[
E=R+1\le4K-2R
\quad\Longleftrightarrow\quad
R\le(p-2)R,
\]

对核心素数 \(p>2\) 成立。这证明 (3)--(4)。

又由 (1)，

\[
2K=\frac{pR+1}{2}>R+1=E,
\]

因为 \((p-2)R>1\)。故 (5) 成立；再由小侧--上半区等价得到 (6)。

## 与已有 B等于1 判据的关系

当 \(B=1\) 时，写 \(m=4q-1\)、\(R=4r-1\)、\(C=mr-q\)。此时

\[
t=AC-q\equiv-q(A+1)\pmod r,
\]

所以 (3) 正好化为

\[
r\mid q^2(A+1)^2,
\]

即 [B等于1的精确二分](type-I-b1-pminusone-same-gap-dichotomy.md)中的 p 减一桥条件。
本卡说明该平方条件并非 \(B=1\) 特有：其坐标无关的本质是 (3)。

## 范围

本定理不选择 \(R\)、\(K\) 或 Type I 正规形，故不证明上半区混合终端选择猜想。
它的作用是把其中最自然的 \(p-1\) 子分支化为一条精确、自动小侧的平方整除判据；
跨正规形选择仍是全称缺口。
