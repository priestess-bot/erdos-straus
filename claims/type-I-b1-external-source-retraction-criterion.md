---
kind: claim
claim_id: type-I-b1-external-source-retraction-criterion
title: B等于一正规形回缩到完整平方因子外部源的判据
statement: 对核心素数的任一B=1 Type I正规形，令R=4k-1且K满足4K=pR+1。该正规形以同一(R,K,C)回缩为完整平方因子外部源，当且仅当k|K（等价于k|((p-1)/4)）。此时典范外源为N=K/k=(Rp+1)/(R+1)，并取外源平方因子e=C；其重建的Type I证书与原正规形完全相同。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- external-source
- factorization
- descent
- b1
- terminal-bridge
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-28'
---

# \(B=1\) 正规形回缩到完整平方因子外部源的判据

设 \(p\equiv1\pmod {24}\) 是素数，已有一张 \(B=1\) 的 Type I 正规形。写成

\[
mR=4C+1,\qquad H=AR-1,\qquad K=CH,
\tag{1}
\]

其中 \(m\equiv3\pmod4\)、\(R\equiv3\pmod4\)。于是

\[
p=4AC-m,\qquad 4K=pR+1.
\tag{2}
\]

令

\[
k=\frac{R+1}{4},\qquad B_p=\frac{p-1}{4}.
\tag{3}
\]

## 定理

以下条件等价：

\[
\begin{aligned}
&k\mid B_p;\\
&k\mid K;\\
&N:=\frac{Rp+1}{R+1}\text{ 是整数，且 }K=kN;\\
&\text{完整平方因子外部源可取 }(q,M,e)=(R,K,C).
\end{aligned}
\tag{4}
\]

在这些条件下，外源构造的二项尾为

\[
u=\frac{K+C}{R}=AC,\qquad v=\frac{Ku}{C}=ACH,
\tag{5}
\]

所以它恢复的目标 Type I 证书恰是原来的 \((m,A,1,C)\)，不是仅仅另一张
同一素数的证书。其典范外源是 \(N\)，对应的正规形桥因子为 \(E_0=N\)。

特别地，若 \(N\) 为偶数，则这是一条偶源终端桥；若 \(N\) 为奇数，则它仍是一条
严格外源递降，但不能未经标记地作为偶基底终止。

## 证明

由 \(R=4k-1\) 和 (2)，

\[
K=kp-B_p.
\tag{6}
\]

故 \(k\mid K\) 当且仅当 \(k\mid B_p\)。而在此情形

\[
N=\frac{Rp+1}{R+1}=\frac{4K}{4k}=\frac Kk,
\tag{7}
\]

这也证明前三项等价。

现在 \(C\mid K\)，所以 \(C\le K\) 且 \(C\mid K^2\)。又 (1) 和 (2) 分别给出

\[
4C\equiv-1\pmod R,\qquad 4K\equiv1\pmod R,
\]

从而 \(C\equiv-K\pmod R\)。这正是
[完整平方因子外部源](quadratic-factor-external-source-descent.md) 对
\((q,M,e)=(R,K,C)\) 的全部因子条件；反向则其定义要求 \(k\mid B_p\)。
式 (5) 由 \(K=CH\) 和 \(H+1=AR\) 直接得到。最后

\[
4K=(R+1)N
\]

说明外源的正规形桥因子为 \(N\)，与
[外部源到正规形桥](type-I-even-external-source-normal-bridge.md) 一致。

## 与源优先坐标的区别

源优先式可以从同一张正规形选择多个桥因子 \(E\)，因而它选择的源
\(n=(4K-E)/R\) 不必等于典范外源 \(N\)。所以

\[
E\ne n
\]

不能推出该 Type I 证书不属于外源走廊。只有 \(E=n\) 时才有 \(K=kn\)，即当前选择的
源本身就是典范外源；这是本判据的充分特例，不是必要条件。

例如 \(p=85369\) 的选定上半区 \(B=1\) 证书为

\[
(m,A,C,R,K,E,n)=(15,821,26,7,149396,8,85368).
\]

这里选定桥满足 \(E\ne n\)，但 \(k=2\mid K\)，故同一证书回缩到外源

\[
N=K/k=74698
\]

并以 \(E_0=N\) 给出偶源终端桥。

## 有限剖面

在五亿普通双尾遗漏的 1,717 张按当前目标级规则选定的上半区 \(B=1\) 证书中，
1,132 张满足 \(k\mid K\)，故已经有这种精确外源回缩；其中 636 张的典范源 \(N\)
为偶数，496 张为奇数。其余 585 张的**所选正规形**满足 \(k\nmid K\)。这只是对当前
选择的有限证书的分类，不排除同一目标另有可回缩的 \(B=1\) 正规形。

重建与计数由

~~~bash
python3 -m unittest tests/test_type_i_tail_upper_b1_completion_profile_500m.py -q
~~~

精确核验。

## 范围

该判据分类的是既有 \(B=1\) 正规形是否可回缩到**同一** \((R,K,C)\) 的完整平方因子
外源。它不构造每个核心素数的 \(B=1\) 正规形，也不证明每个未回缩的正规形不存在其他
外源、Type II 或非 \(B=1\) 证书。
