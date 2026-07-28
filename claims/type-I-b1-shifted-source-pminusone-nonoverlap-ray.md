---
kind: claim
claim_id: type-I-b1-shifted-source-pminusone-nonoverlap-ray
title: B等于一移位源避开同正规形p减一桥与同缺口Type II的无穷射线
statement: 进程p=1363440u+905353中的每个核心素数项都有一个固定的B=1、源p-3、R=63、E=190的Type I终端桥；同一正规形的p减一桥条件失败，且同一缺口不存在普通Type II双尾证书。故固定正规形层面的终端选择不能收缩为p减一源或同缺口Type II。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- type-II
- b1
- shifted-source
- p-minus-one
- terminal-bridge
- same-gap
- dirichlet
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# \(B=1\) 移位源避开同正规形 \(p-1\) 桥与同缺口 Type II 的无穷射线

对每个非负整数 \(u\)，令

\[
\begin{aligned}
q&=5,&m&=19,\\
r&=16,&R&=63,\\
C&=mr-q=299,&A&=1140u+757,\\
p&=4AC-m=1363440u+905353.
\end{aligned}
\tag{1}
\]

再取

\[
s=3,\qquad E=sR+1=190.
\tag{2}
\]

## 定理

进程 (1) 是原始且恒为 \(1\pmod {24}\) 的等差进程，故有无穷多个素数项。对每个这样的
素数 \(p\)，(1) 给出一张 \(B=1\) Type I 正规形，并满足：

\[
\begin{aligned}
&\text{桥因子 }E=190\text{ 将最大尾反向提升到偶源 }n=p-3;\\
&\text{同一正规形没有以 }p-1\text{ 为源的终端桥；}\\
&\text{同一缺口 }m=19\text{ 没有普通 Type II 双尾证书。}
\end{aligned}
\tag{3}
\]

因此，固定正规形内的终端选择不能缩减成“\(p-1\) Type I 桥或同缺口普通 Type II”。

## 证明

令

\[
H=AR-1,\qquad K=CH.
\tag{4}
\]

因为

\[
mR=19\cdot63=4\cdot299+1,
\tag{5}
\]

所以 \((A,1,C)\) 是自然 Type I 正规形，且 \(4K=pR+1\)。又

\[
A=1140u+757\equiv-3\pmod {190},
\]

从而

\[
H=63A-1\equiv0\pmod {190},\qquad E=190\mid K.
\tag{6}
\]

故 \(E\mid4K^2\)，并且 \(E\equiv1\pmod R\)。由

\[
4K-E=pR+1-(3R+1)=(p-3)R
\tag{7}
\]

得到源 \(n=p-3\)，它是严格上半区偶数。由于 \(E\mid K\)，源首分母
\(nK/E\) 为整数；于是这正是 Type I 最大尾的有效偶终端桥。

同一正规形的 \(p-1\) 桥须满足

\[
r\mid q^2(A+1)^2.
\tag{8}
\]

但

\[
A+1=1140u+758=2(570u+379),
\tag{9}
\]

右侧括号恒奇，故 \(v_2(A+1)=1\)。而 \(r=16\)，所以 (8) 失败。
另一方面

\[
Ar=16(1140u+757)\equiv2\pmod5,
\tag{10}
\]

故 \(q=5\nmid Ar\)，由
[B等于一同缺口二分](type-I-b1-pminusone-same-gap-dichotomy.md)，同缺口普通 Type II
双尾也不存在。

最后，令 \(P=1363440\)、\(p_0=905353\)。直接有

\[
p_0\equiv1\pmod {24},\qquad \gcd(P,p_0)=1.
\tag{11}
\]

例如，\(P=2^4\cdot3\cdot5\cdot13\cdot19\cdot23\)；其中 \(p_0\) 与 \(2,3,5\)
互素，而 \(p_0\equiv-19\pmod {299}\) 且 \(p_0\equiv3\pmod {19}\)。Dirichlet 定理
给出无穷多个素数项，完成证明。

## 样本

\[
u=1,\qquad p=2268793
\]

是一个素数项，并完整满足 (3)。该样本只用于回归；无穷性来自 (11)。

## 范围

本定理不排除同一素数在其他正规形上有 \(p-1\) 桥或 Type II 证书，也不是原混合终端
选择引理的反例。它只排除固定正规形内把移位源分支删去的归约。
