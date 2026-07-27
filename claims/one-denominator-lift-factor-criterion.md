---
kind: claim
claim_id: one-denominator-lift-factor-criterion
title: 保留一个源分母的两项替换提升判据
statement: 对 p,n>=2 和 4/n 的任意解中出现的分母 c，存在正整数 u,v 使 4/p=1/u+1/v+1/c，当且仅当令 R=4c-p、S=pc 后，R>0 且存在 e|S^2 使 R|(S+e) 及 R|(S+S^2/e)；此时 u=(S+e)/R、v=(S+S^2/e)/R。若 gcd(R,S)=1，则第二个同余由第一个自动推出；按 u<=v 排序时可额外取 e<=S。
claim_status: established
topics:
- descent
- egyptian-fractions
- divisors
- solution-lift
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 保留一个源分母的两项替换提升判据

## 定理

设

\[
\frac4n=\frac1a+\frac1b+\frac1c
\]

是一个源实例的解，且 \(p\ge2\)。令

\[
R=4c-p,\qquad S=pc.
\]

存在正整数 \(u,v\)，使

\[
\frac4p=\frac1u+\frac1v+\frac1c, \tag{1}
\]

当且仅当 \(R>0\)，且存在正除子 \(e\mid S^2\)，满足

\[
R\mid S+e,\qquad R\mid S+\frac{S^2}{e}. \tag{2}
\]

在此情形可取

\[
u=\frac{S+e}{R},\qquad
v=\frac{S+S^2/e}{R}. \tag{3}
\]

因此，对所有含同一坐标 \(c\) 的源解，(3) 给出一个真正的部分提升：它保留一个
源分母、同时重组其余两个。

## 证明

从 (1) 减去 \(1/c\)，得到

\[
\frac1u+\frac1v=\frac4p-\frac1c=\frac{4c-p}{pc}=\frac RS.
\]

清分母并配方给出标准二项单位分数因子式

\[
(Ru-S)(Rv-S)=S^2. \tag{4}
\]

若有 \(u,v\)，令 \(e=Ru-S\)，则另一个因子为 \(S^2/e\)；两者为正，故
\(e\mid S^2\)，并且 (3) 的两个分子均被 \(R\) 整除，即 (2)。

反过来，若 (2) 成立，按 (3) 定义正整数 \(u,v\)。直接代入得

\[
Ru-S=e,\qquad Rv-S=\frac{S^2}{e},
\]

故 (4) 成立，从而 \(1/u+1/v=R/S\)，再加 \(1/c\) 即得 (1)。

## 互素情形的单同余化简

若额外有

\[
\gcd(R,S)=1, \tag{5}
\]

则对任意 \(e\mid S^2\)，也有 \(\gcd(R,e)=1\)。因此只要

\[
R\mid S+e, \tag{6}
\]

令 \(f=S^2/e\)，便有 \(e\equiv-S\pmod R\) 及 \(ef=S^2\)。在模 \(R\)
下消去可逆的 \(e\)，得到

\[
f\equiv-S\pmod R. \tag{7}
\]

这正是原来第二个整除条件。反向显然，故在 (5) 下，(2) 等价于单个条件 (6)。
若把 \(u,v\) 排成 \(u\le v\)，则由 \(Ru-S=e\)、\(Rv-S=f\) 可取 \(e\le f\)，
亦即 \(e\le S\)。

当 \(p\) 为奇素数且 \(p\nmid c\) 时，只要 \(R>0\)，(5) 自动成立：由
\(\gcd(4c-p,p)=\gcd(4c,p)=1\)，以及
\(\gcd(4c-p,c)=\gcd(p,c)=1\)，即可同时与 \(p\) 和 \(c\) 互素。
因此所有保留分母 \(c<p\) 的标准源分支都可用这一单同余判据。

## 示例与边界

对 \(n=25\) 有

\[
\frac4{25}=\frac1{10}+\frac1{17}+\frac1{850}.
\]

取 \(p=97\)、\(c=850\)、\(e=125\)，(3) 给出

\[
\frac4{97}=\frac1{25}+\frac1{16490}+\frac1{850}.
\]

这与 `gap-three-two-denominator-lift-obstruction` 不矛盾：后者保留**两个**源分母，
而这里仅保留一个。要把本判据升级为严格递降，仍必须证明：对每个未获短证书的
\(p\)，所选较小实例 \(n<p\) 至少有一个可得源解含有满足 (2) 的分母 \(c\)。
这可表为 marked-solution-descent-closure 中的标记源解集非空；不必要求所有源解
都含有可用 \(c\)。目前没有这种全覆盖定理；该判据提供的是可验证的部分提升机制，
而非目标引理本身。

## 首分母范围的循环性

若保留的 \(c\) 位于 \(p/4<c<p/2\)，则目标等式中其余两个分母必严格大于 \(c\)。
因此这个 \(c\) 已经是 \(4/p\) 的首分母，令 \(m=4c-p\) 后，一分母提升存在当且仅当
缺口 \(m\) 的 Type I/II 证书存在，见 middle-coordinate-lift-certificate-equivalence。
这里源解只证明某个 \(c\) 可被保留；它不能帮助构造 (2) 中所需的因子 \(e\)。

特别地，偶数 \(2c<p\) 的无条件标准源解
\(4/(2c)=1/c+1/(2c)+1/(2c)\) 不会提供新的递降：从它保留 \(c\) 的成功提升已经
等价于直接解决目标 \(p\) 的相应缺口。

它甚至不是自然 \(m=3\) 源的普遍规则。对 \(p=73\)、\(n=(p+3)/4=19\)，完整枚举
\(4/19\) 的 11 个按升序规范化的分母三元组得到 21 个不同的源分母；逐个应用 (2) 后均失败。
这是该提升模板的有限反例，不是 Erdős--Straus 猜想的反例：\(p=73\) 本身有
`p-plus-four-sqrt-certificate` 的直接证书。
