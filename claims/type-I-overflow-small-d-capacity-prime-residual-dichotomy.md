---
kind: claim
claim_id: type-I-overflow-small-d-capacity-prime-residual-dichotomy
title: 高载体小 d 容量层的素大余因子残余二分
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、B_p=(p-1)^2/4<M<2B_p、1<=d<p，且 charged support 满足 c=(p-1)/4<=A<=B_p、A|M、2d^2<=p-1。写 b=M/A。则 b<2(p-1)；若 b 合数，余因子因子转移给出完整 E1--E5；若 b 是小于 p 的素数，则 b<=d 时因子转移、b>d 时余因子交换均给出完整 E1--E5；若 b 是大于 p 的素数且 4b>n，则 L=b 给出支付 support reset 的 fixed-n 完整 E1--E5。故唯一未由这三类规则闭合的三规则残余必满足 b 为素数、p<b<2(p-1) 且 4b<=n。该残余实际非空于算术层面：p=73,d=4,n=329,M=1501,A=19,b=79；完整的固定-n 商模 p 折叠随后闭合全部这类素大余因子行，因此该卡是通向小-d 容量层完整闭合的中间二分，不是猜想反例，也不带额外可达性断言。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
  - type-I-overflow-fixed-n-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - high-carrier
  - small-d
  - capacity-window
  - cofactor
  - prime-residual
  - support-reset
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: factor-transfer-and-exchange-edges
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: prime-large-reset-edge-contract
  - reproduction: reproductions/type_i_overflow_small_d_capacity_prime_residual_dichotomy.py
    role: focused-five-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体小 \(d\) 容量层的素大余因子残余二分

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，并令

\[
B_p=\frac{(p-1)^2}{4},
\qquad c=\frac{p-1}{4}.
\tag{1}
\]

设一个已有 source/path/node 回执的 verified overflow 满足

\[
pn=4Md+1,
\qquad B_p<M<2B_p,
\qquad 1\le d<p,
\tag{2}
\]

并携带 \(A\mid M\) 和

\[
c\le A\le B_p,
\qquad 2d^2\le p-1.
\tag{3}
\]

写 \(b=M/A\)。则 \(b>1\)，并且精确有以下二分：

\[
\boxed{
\begin{array}{ll}
\text{存在完整 E1--E5 递降},&\text{或}\\[2mm]
b\text{ 为素数，}\quad p<b<2(p-1),\quad4b\le n.&
\end{array}}
\tag{4}
\]

前一行可以按下表规范构造：

\[
\begin{array}{c|c|c}
\text{余因子条件}&\text{构造}&\text{合同}\\ \hline
b\text{ 合数}&g\mid b,\ dg<p\text{ 的因子转移}&\text{保留 }A\\
b<p\text{ 素数},\ b\le d&g=b\text{ 的因子转移}&\text{保留 }A\\
b<p\text{ 素数},\ b>d&(M,d)\mapsto(Ad,b)&\text{保留 }A\\
b>p\text{ 素数},\ 4b>n&L=b&\text{fixed-}n\text{，支付 support reset}
\end{array}
\tag{5}
\]

因子转移和交换都以

\[
\Lambda_p(M,d;A)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,M\right)
\tag{6}
\]

的字典序严格下降；最后一行由 fixed-\(n\) 合同严格降低第一坐标。

## 余因子上界与复合分流

由 (2)--(3)，

\[
b=\frac MA\le\frac Mc<\frac{2B_p}{c}=2(p-1).
\tag{7}
\]

又 \(M>B_p\ge A\) 给出 \(b>1\)。若 \(b\) 合数，令
\(q=\operatorname{spf}(b)\)。那么

\[
q\le\sqrt b<\sqrt{2(p-1)}.
\tag{8}
\]

由 (3) 有

\[
d^2q^2<2d^2(p-1)\le(p-1)^2<p^2,
\]

故 \(dq<p\)。因此 \(q\) 属于余因子因子转移引理的可移集合；取其规范最大可移
因子即可得到完整 E1--E5，并保持 \(A\)，同时严格降低 (6) 的第二坐标。

## 小素余因子

注意 \(p\nmid M\)，否则 (2) 模 \(p\) 给出 \(0\equiv1\pmod p\)。所以素数
\(b\) 不会等于 \(p\)。设先有 \(b<p\)。若 \(b\le d\)，则

\[
db\le d^2\le\frac{p-1}{2}<p,
\]

所以 \(g=b\) 本身可作因子转移。若 \(b>d\)，余因子交换

\[
(M,d;A)=(Ab,d;A)\longmapsto(Ad,b;A)
\tag{9}
\]

满足交换引理的全部条件。两种情形都由 (6) 严格递降。

## 素大余因子与 reset 门

最后设 \(b>p\) 为素数。由 (2)，

\[
4Ad=\frac{pn-1}{b}<n.
\tag{10}
\]

同时 \(M<2B_p\) 给出

\[
pn<8B_pd+1=2d(p-1)^2+1<2dp^2,
\qquad n<2dp.
\tag{11}
\]

于是

\[
A<\frac n{4d}<\frac p2<b,
\qquad b>2A.
\tag{12}
\]

再由 (7) 和 \(p\ge73\)，\(b<2(p-1)<B_p\)。如果 \(4b>n\)，取 \(L=b\mid M\mid Md\)。
它满足 \(A<L\le B_p\) 和

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
\le\left\lfloor\frac{B_p}{2A}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{13}
\]

所以既有 fixed-\(n\) 有界除子合同给出支付 support reset 的完整 E1--E5。若
\(4b\le n\)，这个 \(L=b\) 门恰好不正；结合前面的穷尽，仅剩 (4) 的素大余因子残余。

## 三规则残余与后续重入收缩

三类旧规则的残余不是形式上的空集合。精确算术行

\[
(p,d,n,M,A,b)=(73,4,329,1501,19,79)
\tag{14}
\]

满足

\[
B_{73}=1296<M<2B_{73},
\qquad 2d^2=32\le72,
\qquad 4b=316\le329.
\]

其中 \(b=79>p\) 为素数；因子转移、\(b<p\) 的交换以及 \(L=b\) reset 都不适用。
这只证明当前三类规则在该算术状态没有自动出口，不声称该行有 source 可达性，也绝不
构成 Erdos--Straus 猜想的反例。

但这不是最终余项。该行有 \(Ad=76<2p\)，所以
\(D=Ad-p=3<p\)。[负固定-\(n\) 重入的支持重置递降](type-I-overflow-negative-fixed-n-reentry-reset.md)
把它重图表为 \((M,d,n;A)=(79,3,13;79)\) 并支付严格 outer-rank reset。更一般地，
[固定-\(n\) 商模 \(p\) 折叠的完整外层秩递降](type-I-overflow-fixed-n-quotient-fold-descent.md)
把任意正 \(D\) 折叠为非零的 \(D\bmod p\)，所以连 \(Ad\ge2p\) 的长余量也会闭合。
由此得到[高载体小 \(d\) 容量层的完整余因子递降](type-I-overflow-small-d-capacity-complete-reduction.md)；
本卡保留为三规则菜单如何精确暴露素大余因子分支的中间二分。

作为一致性检查，\(d=1\) 或 \(d=2\) 时 (2) 分别强制 \(n<2p\) 或 \(n<4p\)，
而素大余因子总有 \(b>p\)，故 \(4b>n\)。所以 (4) 的残余只能从 \(d\ge3\) 开始，
与此前首带和 \(d=2\) 容量窗的完整闭合相容。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_small_d_capacity_prime_residual_dichotomy.py --verify
```

五条精确回执覆盖复合因子转移、小素数因子转移、小素数交换、素大余因子的
support reset，以及 (14) 的严格残余；不做历史范围扫描。
