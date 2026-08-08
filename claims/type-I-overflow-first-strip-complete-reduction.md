---
kind: claim
claim_id: type-I-overflow-first-strip-complete-reduction
title: 高载体首带的余因子完整递降分流
statement: 设核心素数 p=1 (mod 24) 的已有来源回执 overflow 满足 pn=4M+1、M>B_p=(p-1)^2/4、p<=n<=2p-5，并携带 A|M、1<=A<=B_p 及图表无关标记集 Sol(p)。令 c=(p-1)/4、b=M/A。则必有一条严格可提升递降：A<c 时 L=c 给出 fixed-s 边；A>=c、b 合数时 L=M/spf(b) 给出保留 A 的 fixed-n 边；A>=c、b 为素数且 b<p 时，(M,d=1;A) 重图表为 (A,d=b;A)，并以 (floor(B_p/A),M) 的字典序严格下降；A>=c、b 为素数且 b>p 时 L=b 给出支付 support reset 的 fixed-n 边。b=p 不可能。故首高载体带在既有 source/solution-lift 合同下不留未分流的 overflow。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-height-staircase
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
topics:
  - type-I
  - overflow
  - high-carrier
  - first-strip
  - cofactor-primality
  - denominator-transfer
  - support-reset
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-high-carrier-height-staircase
    role: first-strip-d-one-and-cofactor-boundary
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: complete-fixed-n-edge-contract
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: complete-fixed-s-edge-contract
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: unified-carrier-rank-for-prime-cofactor-transfer
  - reproduction: reproductions/type_i_overflow_first_strip_complete_reduction.py
    role: focused-four-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体首带的余因子完整递降分流

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，且已有 source/path/node 回执的 overflow 满足

\[
pn=4M+1,
\qquad M>B_p:=\frac{(p-1)^2}{4},
\qquad p\le n\le2p-5.
\tag{1}
\]

令 \(A\mid M\) 为当前 absorbed support，\(1\le A\le B_p\)，并假设该 overflow
使用图表无关的标记集 \(W=\operatorname{Sol}(p)\)，正如既有 fixed-\(n\)/fixed-\(s\)
合同所要求。写

\[
c=\frac{p-1}{4},
\qquad b=\frac MA.
\tag{2}
\]

则此状态必有一条带恒等解提升的严格递降，按下列互斥分流构造：

\[
\begin{array}{c|c|c}
\text{条件}&\text{后继构造}&\text{严格付款}\\ \hline
A<c&L=c\mid rd&\text{既有 fixed-}s\\
A\ge c,\ b\text{ 合数}&L=M/\operatorname{spf}(b)&\text{fixed-}n\text{，保留 }A\\
A\ge c,\ b\text{ 素数},\ 1<b<p&(M,d)\mapsto(A,b)&\text{载体 }M\text{ 严格下降}\\
A\ge c,\ b\text{ 素数},\ b>p&L=b&\text{fixed-}n\text{，支付 support reset}
\end{array}
\tag{3}
\]

特别地，首高载体带不再保留一个需要 alternate/capacity 才能处理的 overflow 子族。
这不是对猜想的全称证明：首带之外的 \(n\ge2p-1\) 仍然需要独立处理，且本定理仍以
输入已有的来源与全域解提升回执为前提。

## 公共预备结论

由高载体首带的高度阶梯，(1) 已强制 \(d=1\)。因此

\[
M=\frac{pn-1}{4},
\qquad r=c,
\qquad s=1,
\qquad rd=c.
\tag{4}
\]

又 \(M>B_p\ge A\)，故 \(b>1\)。首带上界给出

\[
4M=pn-1\le2p^2-5p-1<8B_p,
\qquad M<2B_p,
\tag{5}
\]

并且当 \(A\ge c\) 时

\[
b\le\frac Mc<\frac{2B_p}{c}=2(p-1).
\tag{6}
\]

最后，\(p\nmid M\)，否则 (1) 模 \(p\) 给出 \(0\equiv1\pmod p\)。所以当 \(b\) 是
素数时，\(b\ne p\)，恰有 \(b<p\) 或 \(b>p\) 两种可能。

## 三类已有边

若 \(A<c\)，取 \(L=c\)。式 (4) 给出 \(L\mid rd\)、\(4L>s\)，且

\[
\left\lfloor\frac{B_p}{L}\right\rfloor=4c
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

既有 fixed-\(s\) 合同给出完整 E1--E5。

现在设 \(A\ge c\)。若 \(b\) 合数，令 \(q=\operatorname{spf}(b)\)。由
\(q\le b/2<p\)，有

\[
L=\frac Mq=A\frac bq,
\qquad A\mid L,
\qquad 2A\le L\le\frac M2<B_p.
\tag{7}
\]

又 \(4L=(pn-1)/q>n\)，且 \(L\mid M\)。于是

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
\le\left\lfloor\frac{B_p}{2A}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor,
\]

故既有 fixed-\(n\) 合同给出保留 \(A\) 的完整 E1--E5。

若 \(b>p\) 为素数，令 \(L=b\)。由 (1) 与 \(b>p\)，

\[
4A=\frac{pn-1}{b}<n,
\qquad 2A<\frac n2<p<b.
\tag{8}
\]

再由 (6) 和 \(p\ge73\)，\(b<2(p-1)<B_p\)。于是 \(L=b\mid M\)、
\(2A<L\le B_p\)、\(4L>n\)，且同一个 floor 势严格下降。这里 \(A\nmid L\)，
所以 fixed-\(n\) 合同明确把它登记为支付 support reset 的完整 E1--E5 边，而不伪称
旧支撑被保留。

## 素余因子的小于 \(p\) 分母转移

剩下 \(b<p\) 的素余因子情形。定义确定的后继 determinant 坐标

\[
M_T=A,
\qquad d_T=b,
\qquad R_T=4A-n,
\qquad K_T=A(p-b).
\tag{9}
\]

因为

\[
4A=\frac{pn-1}{b}>n
\]

（等价于 \(n(p-b)>1\)），有 \(0<R_T<4A\)，且

\[
pn=4M_Td_T+1,
\qquad pR_T+1=4K_T,
\qquad A\mid K_T,
\qquad 1<d_T<p.
\tag{10}
\]

所以 (9) 是一个合法的 fixed-\(n\) canonical chart；它可以是 marked absorb，也可以
仍是 overflow。它严格降低 canonical \(R\)：

\[
R_M-R_T=4A(b-1)>0.
\tag{11}
\]

这里不再把较小 \(R\) 或一次性相位标志误当作全局势。源状态有 \(M=Ab\)，而 (9)
的目标载体为 \(M_T=A<M\)。在本分流与既有 fixed-\(n\)/fixed-\(s\) 外层秩边的
并集中，使用

\[
\Lambda_p(M,d;A)=
\left(
\left\lfloor\frac{B_p}{A}\right\rfloor,
M
\right)
\tag{12}
\]

的字典序。普通 fixed-\(n\)/fixed-\(s\) 边把后继 support 设为 \(L\)，已经严格降低
第一坐标；(9) 保持 \(A\) 而严格降低第二坐标。故这是一条状态内禀的良基递降；更一般
的因子转移与余因子交换由[余因子因子转移与交换的载体秩递降](type-I-overflow-cofactor-factor-exchange-carrier-descent.md)
统一给出。

E1 继承原 overflow 的 source/path/node 回执；E2--E3 是 (9)--(10) 的整数恒等式；
E4 取 \(W_T=W_S=\operatorname{Sol}(p)\) 与恒等映射；E5 是 (12)。故这是一条
`first_strip_prime_cofactor_transfer_v1` verified edge，而不是只降低局部载体的 RESET
候选。

这完成 (3) 的全部分支。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_first_strip_complete_reduction.py --verify
```

四条精确回执分别覆盖 \(A<c\)、合数 \(b\)、素数 \(b<p\) 的分母转移，以及素数
\(b>p\) 的 support reset；不做历史范围扫描。
