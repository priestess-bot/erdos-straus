---
kind: claim
claim_id: type-I-fixed-chart-determinant-factor-table
title: 固定 Type I 图表的完整因子对 determinant 表与 carry 边界
statement: 固定素数 p 与正规图表 pR+1=4K。所有满足 pn=4Md+1、0<d<p、n>0 且 4M-n=R 的 Type I determinant 行，恰与有限集合 W_det(p,R)={M|K: 1<=K/M<p,4M>R} 双射；对应式为 C=K/M、d=p-C、n=4M-R。故任何只列两个线性块 U°、V° 的模型都不是同图表全部 determinant 行的物理表。p=73,R=11,K=201 中 M=3 与 M=201 在 U(11) 的所有角色相位相同，但取 ledger A=3 后 E2 的带账本 carry/cofactor 前置门分别通过和失败，严格证明相位/两块不能替代实际 M carry。在线性式 p=a+s+asR 中恒有 R<p，故此完整表仅属 low rechart，不能直接成为 overflow source-lift 或 E1--E5 递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-two-block-source-map-completeness
  - type-I-overflow-cofactor-ledger-e2-gate
  - type-I-fg-physical-carry-arc-lift-interface
topics:
  - type-I
  - fixed-chart
  - determinant
  - factor-pair
  - linear-source
  - physical-carrier
  - E2
  - Fourier
  - proof-boundary
sources:
  - claim: type-I-linear-two-block-source-map-completeness
    role: two-block-subtable-and-boundary
  - claim: type-I-overflow-cofactor-ledger-e2-gate
    role: physical-carry-gate
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: row-level-carry-interface
visibility: public
last_checked: '2026-08-06'
---

# 固定 Type I 图表的完整因子对 determinant 表与 carry 边界

## 1. 同图表的有限完整算术表

固定素数 \(p\) 与一个正规 Type I 图表

\[
pR+1=4K.
\tag{1}
\]

定义

\[
\mathcal W^{\rm det}_{p,R}
=\left\{
M:M\mid K,\quad 1\le\frac KM<p,\quad4M>R
\right\}.
\tag{2}
\]

对每个 \(M\in\mathcal W^{\rm det}_{p,R}\)，置

\[
C=\frac KM,
\qquad
d=p-C,
\qquad
n=4M-R.
\tag{3}
\]

**定理。** (3) 给出且仅给出所有满足

\[
pn=4Md+1,
\qquad
0<d<p,
\qquad
n>0,
\qquad
4M-n=R
\tag{4}
\]

的实际同图表 determinant 行。特别地，

\[
K_M=M(p-d)=K,
\qquad
R_M=4M-n=R.
\tag{5}
\]

**证明。** 对 (3)，有

\[
\begin{aligned}
4Md+1
&=4M\left(p-\frac KM\right)+1\\
&=4pM-4K+1\\
&=p(4M-R)=pn,
\end{aligned}
\tag{6}
\]

其中最后一步使用 (1)。(2) 恰保证 \(0<d<p\) 与 \(n>0\)。

反过来，若 (4) 成立，令 \(C=p-d\)。由 \(n=4M-R\) 和行列式得到

\[
4M(p-d)=p(4M-R)+1=4K,
\tag{7}
\]

所以 \(MC=K\)，即 \(M\mid K\)、\(C=K/M\)，并恢复 (2)--(3)。证毕。

这是一张**固定 chart 的 determinant 表**：它对 (4) 完整，却不自动是实际 F/G
source-path、marked source table 或可提升递归边。

## 2. 两块模型并非该物理表

线性两块模型只给出

\[
U^\circ,\qquad V^\circ,\qquad U^\circ V^\circ=K,
\tag{8}
\]

两个确定的因子行。它在“两个声明块”范围内是完整的，但 (2) 往往还含其它因子对，故不能
被误读为同图表全部 physical determinant 行的 source-completeness。

最小核心例为

\[
(p,R,a_{\rm lin},s)=(73,11,6,1),
\qquad
(U^\circ,V^\circ,K)=(3,67,201).
\tag{9}
\]

这里

\[
\mathcal W^{\rm det}_{73,11}=\{3,67,201\}.
\tag{10}
\]

三行的算术数据分别是

\[
\begin{array}{c|c|c|c}
M&C&d&n\\ \hline
3&67&6&1\\
67&3&70&257\\
201&1&72&793
\end{array}
\tag{11}
\]

且每行都满足 \(73n=4Md+1\)、\(4M-n=11\)。因此 \(M=201\) 不是可省略的
“抽象组合”，而是同图表的一条真实 determinant 行。

## 3. 一个真实的 phase/carry 分离

在 (9) 中，

\[
3\equiv201\pmod {11},
\tag{12}
\]

所以 \(U(11)\) 的任意角色在 \(M=3\) 与 \(M=201\) 上的相位完全相同。取共同旧账本
\(A=3\)，两行都满足 \(A\mid M\)，但其 E2 带账本 carry/cofactor 前置门的参数不同于
线性参数 \(a_{\rm lin}=6\)：

\[
\begin{array}{c|c|c|c|c}
M&C& a_{\rm E2}=A/(A,C)&M\bmod73&\kappa_{a_{\rm E2}}(M)\\ \hline
3&67&3&3&0\\
201&1&3&55&2
\end{array}
\tag{13}
\]

故第一行通过该 carry/cofactor 前置门，而第二行失败。更等价地，

\[
u(3)=1,\qquad u(201)=67,\qquad
3u(3)<73<3u(201).
\tag{14}
\]

这是实际同图表 determinant 行的严格反例：仅依赖 \(U(11)\) Fourier/SNF 相位，或只保存
线性两块 \(U^\circ,V^\circ\)，都不足以判定 physical carry。若附加的 marked label
还编码其它整数数据，当然可区分它们；本反例只排除纯模 \(11\) 相位推断。

## 4. 为什么它尚不能推进 overflow 递降

线性参数式

\[
p=a_{\rm lin}+s+a_{\rm lin}sR
\tag{15}
\]

对正参数强制 \(R<p\)。所以 (2) 的所有行都是 low rechart，不能直接成为所需的
overflow source-lift。要将这张算术表接入主目标，还须分别证明：

1. 哪些 \(M\) 有实际 source/path provenance 与继承 ledger \(A\)；
2. marked F/G 标签如何从这些行完整导出；
3. 跨 \(d\) 的 row transition 是否满足 typed lift 与 E1--E5；
4. low chart 如何导向 terminal 或合法的高图表/跨状态分派。

本卡只给出一个有限、完全可枚举的物理 determinant 子宇宙和一条 phase/carry 边界；
它不把线性两块模型升级为全源闭合，也不产生新的短证书或严格递降。
