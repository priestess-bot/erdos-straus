---
kind: claim
claim_id: type-I-overflow-small-d-dual-saturation-composition
title: \(d^2<p\) 高载体容量层的 dual 饱和组合闭合
statement: >-
  设 p≡1 (mod 24) 的 verified overflow 满足 pn=4Md+1、B_p<M<2B_p、1≤d 且 d^2<p，
  并携带 A|M、1≤A≤B_p 及 source/path、Sol(p)、E1--E5 合同。令 r=M mod p、
  s=(4rd+1)/p、P=rd、c=(p−1)/4。则 1≤s≤4d−1 且 c≤P≤B_p。若 A<c，
  取 L=P 给出完整 fixed-s 严格外层秩递降；若 A≥c，则 d^2<p，直接接入既有
  small-d 容量层完整递降。因此整个 B_p<M<2B_p、d^2<p 容量层没有未分流 overflow。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-small-d-capacity-complete-reduction
topics:
  - type-I
  - overflow
  - high-carrier
  - small-d
  - capacity-window
  - fixed-s
  - dual-saturation
  - denominator-height
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s-E1-E5-contract
  - claim: type-I-overflow-small-d-capacity-complete-reduction
    role: A-at-least-c-composition
  - reproduction: reproductions/type_i_overflow_small_d_dual_saturation_composition.py
    role: d-squared-less-than-p-dual-and-composition-receipt
visibility: public
last_checked: '2026-08-09'
---

# \(d^2<p\) 高载体容量层的 dual 饱和组合闭合

## 定理

令 \(p\equiv1\pmod {24}\) 为核心素数，并设已有 source/path/node 回执的
verified overflow 满足

\[
pn=4Md+1,
\qquad B_p<M<2B_p,
\qquad 1\le d,\quad d^2<p,
\tag{1}
\]

其中

\[
B_p=\frac{(p-1)^2}{4},
\qquad c=\frac{p-1}{4}.
\tag{2}
\]

令 \(A\mid M\)、\(1\le A\le B_p\)，并取

\[
r=M\bmod p,\qquad
s=\frac{4rd+1}{p},\qquad
P=rd.
\tag{3}
\]

则 \(r\ne0\)，\(s\) 是正整数，并且

\[
1\le s\le4d-1,
\qquad
c\le P\le B_p.
\tag{4}
\]

于是按当前 absorbed support 的位置分流：

\[
\begin{array}{c|c|c}
\text{条件}&\text{后继}&\text{严格付款}\\ \hline
A<c&L=P\mid rd&\text{fixed-}s\text{，第一坐标严格下降}\\
A\ge c&\text{small-}d\text{ 的因子转移/交换/商折叠}&
\left(\left\lfloor B_p/A\right\rfloor,M\right)\text{ 字典序严格下降}.
\end{array}
\tag{5}
\]

两行互斥且穷尽；在既有图表无关的
\(W=\operatorname{Sol}(p)\) 恒等提升和 E1--E5 合同下，(1) 的整个
\(d^2<p\) 容量层没有未分流 overflow。

## 余数和容量界

由 \(pn=4Md+1\) 及 \(M=kp+r\)，有

\[
pn=4(kp+r)d+1
=p(4kd)+4rd+1.
\tag{6}
\]

因此 \(p\mid4rd+1\)，且 \(r\ne0\)，否则 (6) 模 \(p\) 给出矛盾。于是 (3) 的
\(s\) 是正整数，并满足

\[
4P+1=sp,\qquad
P=\frac{sp-1}{4}.
\tag{7}
\]

因为 \(1\le r<p\)，

\[
4rd+1\le4(p-1)d+1<4pd,
\tag{8}
\]

所以 \(s<4d\)，而 \(s\) 为整数，得到 \(s\le4d-1\)。

另一方面 \(s\ge1\)，故由 (7)

\[
P\ge\frac{p-1}{4}=c.
\tag{9}
\]

核心素数 \(p\equiv1\pmod {24}\) 必有 \(p\ge73\)。由 \(d^2<p\)，有
\(d<\sqrt p\)，而

\[
p-4\sqrt p-1>0
\qquad(p\ge73).
\tag{10}
\]

因此 \(p>4d+1\)，并由 (7) 得

\[
4P=sp-1\le(4d-1)p-1<(p-1)^2=4B_p.
\tag{11}
\]

所以 \(P\le B_p\)。这证明 (4) 的完整容量范围；它不需要枚举 \(d\) 的模 \(4d\)
逆元，也不依赖 \(p\bmod16\) 的分支。

## \(A<c\) 的统一 fixed-\(s\) 边

若 \(A<c\)，由 (4) 有

\[
A<P\le B_p,\qquad P\mid rd.
\tag{12}
\]

又由 (7)

\[
4P-s=s(p-1)-1>0,
\tag{13}
\]

并且

\[
\frac{B_p}{P}\le\frac{B_p}{c}=p-1,
\qquad
\frac{B_p}{A}>\frac{B_p}{c}=p-1.
\tag{14}
\]

故

\[
\left\lfloor\frac{B_p}{P}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{15}
\]

将 \(L=P\) 代入既有 fixed-\(s\) 有界除子合同，得到

\[
R_P=4P-s,\qquad K_P=P\left(p-\frac{rd}{P}\right)=P(p-1).
\tag{16}
\]

直接计算给出

\[
pR_P+1=4K_P,\qquad
R_P\equiv3\pmod4,\qquad
0<R_P<4P,\qquad K_P>0.
\tag{17}
\]

所以这是完整 E1--E5 的 fixed-\(s\) 严格外层秩边。若 \(A\nmid P\)，则由 (15)
明确支付 support reset；不把这条边误标为 support-preserving。

## \(A\ge c\) 的组合闭合

若 \(A\ge c\)，输入已经给出 \(B_p<M<2B_p\)、\(A\mid M\)、
\(1\le A\le B_p\) 以及 \(d^2<p\)，所以既有
“高载体小 \(d\) 容量层的完整余因子递降”定理逐项适用。它按
\(b=M/A\) 穷尽三类后继：

1. \(b\le d\) 时的最小素因子转移；
2. \(b<p\) 且 \(b>d\) 时的余因子交换；
3. \(b>p\) 时的固定-\(n\) 商模 \(p\) 折叠。

这些后继都保持或显式重置 support，并严格降低

\[
\Lambda_p(M,d;A)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,M\right).
\tag{19}
\]

因此 \(A\ge c\) 分支不再需要按 d 逐层重做余因子证明。

## 穷尽性与边界

因为 \(A<c\) 或 \(A\ge c\) 必有其一，(12)--(17) 和 (18)--(19) 合起来给出整个
\(d^2<p\)、\(B_p<M<2B_p\) 层的严格可提升选择器入口。该结论仍不覆盖
\(M\ge2B_p\)、\(d^2\ge p\) 或 source/path 可达性本身未给回执的状态；这些边界仍需
generalized \(2^j\)、q-adic capacity 或其它 Type I/II 短证书。

## 控制实例与复现

本卡用 \(p=73\) 的 \(d=1,\ldots,8\) 各一条 \(A<c\) dual 控制，并用
\(p=97,d=9\) 的额外控制确认泛化边界；同时用 \(d=5,6,7,8\) 的
factor/exchange/fold 控制验证组合接口：

\[
\begin{array}{c|r|r|r|r|r}
d&n&M&A&r&s\\ \hline
1&73&1332&1&18&1\\
2&145&1323&1&9&1\\
3&217&1320&1&6&1\\
4&297&1355&1&41&9\\
5&357&1303&1&62&17\\
6&433&1317&1&3&1\\
7&509&1327&1&13&5\\
8&569&1298&1&57&25
\end{array}
\]

额外控制为
\[
(p,n,M,d,A,r,s)=(97,877,2363,9,1,35,13).
\]

精确复现命令：

    python3 reproductions/type_i_overflow_small_d_dual_saturation_composition.py --verify
