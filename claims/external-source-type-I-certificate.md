---
kind: claim
claim_id: external-source-type-I-certificate
title: 外部源条件给出精确的 Type I 证书
statement: 固定核心素数 p 与合法缺口 m，令 x=(p+m)/4。存在外部源 i 使 m|(p+i)、4i|(p+m)，当且仅当存在一个 Type I 证书除子 d|x^2 满足 x|d；对应关系为 d=ix。
claim_status: established
topics:
- certificate
- type-I
- continued-fractions
- divisor-parametrization
- proof-program
sources:
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-formulation
- paper: bello2026
  locator: "Proposition 17"
  role: independent-parametrization-check
- paper: bradford2024
  locator: "Proposition 1"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 外部源条件给出精确的 Type I 证书

## 精确表征

令 \(p\equiv1\pmod{24}\) 是素数，\(m\equiv3\pmod4\)、
\(3\le m\le p-2\)，并设 \(x=(p+m)/4\)。则下列两项等价：

1. 存在 \(i\ge1\) 使
   \[
   m\mid p+i,\qquad 4i\mid p+m;
   \]
2. 存在 Type I 证书除子 \(d\mid x^2\)，满足
   \[
   x\mid d,\qquad m\mid px+d.
   \]

对应由 \(d=ix\) 给出。换言之，外部源机制恰好是 Type I 除子格中
\(x\cdot\operatorname{Div}(x)\) 这一条“射线”的完整描述，而不是全部 Type I
证书的描述。

## 前向构造

令 \(p\equiv1\pmod{24}\) 是素数。设 \(i\ge1\) 和 \(m\) 满足

\[
m\equiv3\pmod4,\qquad 3\le m\le p-2,
\qquad m\mid p+i,\qquad 4i\mid p+m.
\]

令

\[
x=\frac{p+m}{4},\qquad d=ix.
\]

则 \((m,d)\) 是 Type I 除子证书。相应的分母是

\[
x,\qquad \frac{x(p+i)}m,\qquad \frac{px(p+i)}{im}.
\]

这正是 Ventas 的 *external source* 条件在 Bradford 缺口变量中的写法；
Bello--Hernandez--Benito--Fernandez 的 Proposition 17 也将其识别为
`fab(p,i,1)` 的可采纳除子。

## 证明

由 \(4i\mid p+m=4x\)，可写 \(x=it\)。于是

\[
d=ix=i^2t\mid i^2t^2=x^2.
\]

又 \(m\mid p+i\)，故

\[
m\mid x(p+i)=px+ix=px+d.
\]

这正是 `short-certificate-equivalence` 的 Type I 条件。Bradford 的恢复公式给出

\[
\frac{px+d}{m}=\frac{x(p+i)}m,
\]

以及

\[
\frac{p(x+px^2/d)}m=\frac{px(p+i)}{im}.
\]

所有量为正整数，且 \(m\) 已被假设在自然缺口范围内，结论成立。

反向地，设 \(d=ix\) 是第二项中的证书。由 \(d\mid x^2\) 得 \(i\mid x\)，
所以 \(4i\mid4x=p+m\)。又 \(m\mid px+d=x(p+i)\)。而
\(\gcd(x,m)=1\)：任一公因子同时整除 \(x\) 和 \(m=4x-p\)，从而整除素数
\(p\)，但 \(0<x<p\)。故可从最后一个整除式消去 \(x\)，得到 \(m\mid p+i\)。
这就恢复外部源条件。

## 与已有分支的关系及限制

取 \(i=1\) 恢复来自 \(p+1\) 的 Type I 分支。它也能生成并非最小缺口的额外
证书：例如 \(p=193\)、\((i,m)=(2,39)\) 给出 \((x,d)=(58,116)\)。

该定理把寻找这个 Type I 子类的证书转化为寻找某个外部数 \(p+i\) 的合适
\(3\pmod4\) 因子，但没有证明对每个 \(p\) 都存在这样的 \(i,m\)。一般 Type I
除子无需满足 \(x\mid d\)，所以该子类也不等于整个 Type I 空间；例如短证书搜索中
可以出现这条整除性不成立的最小缺口。它同样没有给出 \(p\) 到更小分母实例的解提升映射，
因此不是所需递降。
