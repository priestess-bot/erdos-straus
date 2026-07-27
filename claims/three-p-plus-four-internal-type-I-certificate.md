---
kind: claim
claim_id: three-p-plus-four-internal-type-I-certificate
title: 来自 3p+4 的内部 (A,B)=(4,3) Type I 证书
statement: 对核心素数 p=1 mod24，若 m|3p+4 且 m=-p mod48，则 x=(p+m)/4、d=(p+m)/3 是自然缺口范围内的 Type I 除子证书；其互素正规形恰为 (A,B,C)=(4,3,(p+m)/48)。每个这样的 m 均满足 m<=(3p+4)/41。
claim_status: established
topics:
- certificate
- type-I
- internal-parameter
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-equivalence
- paper: elsholtz_tao2013
  locator: "Section 2, Proposition 2.3"
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-23'
---

# 来自 \(3p+4\) 的内部 \((A,B)=(4,3)\) Type I 证书

## 定理

令 \(p\equiv1\pmod{24}\) 为素数。若 \(m\) 是 \(3p+4\) 的正因子并且

\[
m\equiv-p\pmod{48},
\]

则

\[
x=\frac{p+m}{4},\qquad d=\frac{p+m}{3}
\]

是缺口 \(m\) 的 Type I 除子证书。更精确地，写

\[
C=\frac{p+m}{48},
\]

则

\[
x=4\cdot3\cdot C,\qquad d=4^2C,
\]

所以 `type-I-coprime-factor-normal-form` 中的参数恰为

\[
(A,B,C)=(4,3,C).
\]

特别地，\(m\) 自动处于自然缺口范围，并满足

\[
23\le m\le\frac{3p+4}{41}\le p-2. \tag{1}
\]

## 证明

条件 \(m\equiv-p\pmod{48}\) 使 \(C\) 为正整数。于是

\[
x=12C,\qquad d=16C,
\]

从而 \(d\mid x^2\)，因为 \(x^2/d=9C\)。又

\[
px+d=12Cp+16C=4C(3p+4),
\]

而 \(m\mid3p+4\)，故 \(m\mid px+d\)。这正是 Type I 条件。也可直接由
正规形验证：\((4,3)=1\)、\(x=ABC\)，且

\[
m\mid3p+4=Bp+A.
\]

剩下只需验证范围。核心素数模 \(48\) 只能为 \(1\) 或 \(25\)。相应地

\[
\begin{array}{c|c|c|c}
p\pmod{48}&3p+4\pmod{48}&m\pmod{48}&(3p+4)/m\pmod{48}\\
\hline
1&7&47&41\\
25&31&23&41
\end{array}
\]

表中最后一列由 \(47^{-1}\equiv47\) 和 \(23^{-1}\equiv23\pmod{48}\)
得到。令 \(h=(3p+4)/m\)。因 \(h>0\) 且 \(h\equiv41\pmod{48}\)，有
\(h\ge41\)，于是 \(m\le(3p+4)/41\)。同时 \(m\equiv23\) 或
\(47\pmod{48}\)，所以 \(m\ge23\)；而 \((3p+4)/41\le p-2\) 对
\(p\ge3\) 成立。这证明 (1)。

## 因子判据与组合见证

按 \(p\) 的模 \(48\) 类，这个分支是以下显式因子判据：

\[
\begin{array}{c|c|c}
p\pmod{48}&3p+4&\text{可取的因子 }m\\
\hline
1&7\pmod{48}&47\pmod{48}\\
25&31\pmod{48}&23\pmod{48}
\end{array}
\]

因此，若 \(3p+4\) 含表中指定残数的**素因子**，它本身已经给出证书；不过完整
判据必须允许组合因子。例如

\[
3\cdot1297+4=3895=5\cdot19\cdot41,
\]

三个素因子都不是 \(47\pmod{48}\)，但 \(m=5\cdot19=95\equiv47\pmod{48}\)
给出

\[
(m,x,d)=(95,348,464),\qquad(A,B,C)=(4,3,29).
\]

同样，曾作为五分支共同残余示例的 \(p=2521\) 满足

\[
3p+4=7567=23\cdot329,
\]

故取 \(m=23\) 得到内部 Type I 证书

\[
(m,x,d)=(23,636,848),\qquad(A,B,C)=(4,3,53).
\]

## 边界

这是一条围绕目标 \(p\) 对移位整数 \(3p+4\) 分解的直接证书分支，不是从某个
\(n<p\) 的已知解提升而来的递降边。它也刻意说明了为何只搜索 Type I 的两个边界面
不够：这里 \(A>1\)、\(B>1\)，既不属于外部源的 \(B=1\) 面，也不属于
`geometric-lcm-boundary-type-I-equivalence` 的 \(A=1\) 面。
