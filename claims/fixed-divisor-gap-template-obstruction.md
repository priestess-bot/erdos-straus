---
kind: claim
claim_id: fixed-divisor-gap-template-obstruction
title: 有限个基本固定缺口固定除子证书族可被 Dirichlet 素数列同时避开
statement: 对固定缺口 m=4j-1，令 g=gcd(6,j)。对核心素数 p=24t+1、x=6t+j，基本的 d=s（s|g^2）Type II 构造和 d=sx（s|g）Type I 构造都可由 x 的固定公共因子得到。任取有限多个缺口，这两类构造都被无穷多个 p=1 mod L 的核心素数同时避开，其中 L=24*lcm(m)。故有限叠加此类无分解模证书不能完成 Erdős--Straus 猜想。
claim_status: established
topics:
- certificate
- congruences
- obstruction
- dirichlet
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: certificate-reconstruction
- paper: elsholtz_tao2013
  locator: "Section 2, fixed residue-class limitations"
  role: parametrization-context
visibility: public
last_checked: '2026-07-23'
---

# 有限个基本固定缺口固定除子证书族可被 Dirichlet 素数列同时避开

## 两类固定除子生成器

设固定缺口 \(m=4j-1\)，并令 \(p=24t+1\)、

\[
x=\frac{p+m}{4}=6t+j,
\qquad g=\gcd(6,j).
\]

于是 \(g\mid x\)。因此有两类完全不分解 \(x\) 的候选：

\[
\begin{array}{c|c|c}
\text{类型} & \text{固定除子} & \text{成立条件}\\
\hline
\mathrm{II} & d=s,\ s\mid g^2,\ s\le x & p\equiv-4s\pmod m\\
\mathrm{I} & d=sx,\ s\mid g & p\equiv-s\pmod m
\end{array} \tag{1}
\]

第一行中 \(s\mid x^2\)，而 \(m\mid x+s\) 等价于
\(m\mid4(x+s)=p+m+4s\)。第二行中 \(sx\mid x^2\)，且
\(m\mid px+sx=x(p+s)\)；这里 \(\gcd(x,m)=1\)，故可消去 \(x\)。
所以 (1) 给出两类最直接的、由 \(x=6t+j\) 的固定公共因子得到的 Type I/II 切片。

例如 \(m=7\) 时 \(j=g=2\)，Type II 的 \(s=1,2,4\) 给出
\(p\equiv3,6,5\pmod7\)，即 `gap-seven-congruence-certificates` 的三个类。\(m=11\)
时 \(j=g=3\)，Type II 的 \(s=1,3,9\) 给出
\(p\equiv7,10,8\pmod{11}\)。

## 有限避免定理

给定有限个缺口 \(m_1,\ldots,m_r\)，令

\[
L=\operatorname{lcm}(24,m_1,\ldots,m_r).
\]

则每个素数

\[
p\equiv1\pmod L \tag{2}
\]

都不满足这些缺口的任一 (1) 中的两类固定除子条件。因 \(\gcd(1,L)=1\)，Dirichlet
定理给出无穷多个这样的素数；故任何有限个上述固定缺口族都不能覆盖全部核心素数。

### 证明

对 Type I，若 (2) 满足 \(p\equiv-s\pmod m\)，则 \(m\mid s+1\)。
因为 \(g\mid6\)，可能的 \(s\mid g\) 只在 \(\{1,2,3,6\}\) 中。\(m\equiv3\pmod4\)
且 \(m\mid s+1\) 只可能要求 \((m,s)=(3,2)\) 或 \((7,6)\)；但前者的
\(j=1,g=1\)，后者的 \(j=2,g=2\)，均与 \(s\mid g\) 矛盾。

对 Type II，(2) 和 (1) 会给出 \(m\mid4s+1\)。可能的
\(s\mid g^2\) 属于

\[
\{1,2,3,4,6,9,12,18,36\}.
\]

其中 \(4s+1\) 的 \(3\pmod4\) 因子只可能产生 \((m,s)=(3,2)\) 或
\((7,12)\)；如上，分别与 \(g=1\) 和 \(g=2\) 不相容。故两类条件均不能成立。

## 对证明计划的含义

该定理不否定其他固定缺口除子形式、因子依赖的除子、可变缺口、Type II 射线或真正的
递降；它只严格排除 (1) 的有限叠加。若要闭合全称目标，至少必须超越这两类基本模板，
并让除子或递降状态真正读取 \(p\) 的非平凡因子结构。
