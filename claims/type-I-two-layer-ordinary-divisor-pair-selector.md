---
kind: claim
claim_id: type-I-two-layer-ordinary-divisor-pair-selector
title: Type I 偶终端桥的二层普通除子对选择器
statement: 对核心素数 p 和合法缺口 m，令 x=(p+m)/4。存在一张 Type I 正规形及其最大尾偶终端桥，当且仅当存在两对互素普通除子 (A,B) 与 (u,v)：AB|x、m|Bp+A；令 C=x/(AB)、R=(4B^2C+1)/m、H=AR-B、K=BCH、L=2K，则 u,v|L、u=2v modR，且 E=Lu/v 为偶数并满足 E<=2L-2R。此时 E 是桥因子，源为 n=(2L-E)/R。故目标和终端的两个平方除子选择同时等价于两个普通除子对的残数命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- terminal-bridge
- divisor-pairs
- normal-form
- factorization
- even-source
- selector
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# Type I 偶终端桥的二层普通除子对选择器

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，\(m\equiv3\pmod4\)、
\(3\le m\le p-2\)，并令

\[
x=\frac{p+m}{4}.
\]

则存在一张 Type I 正规形及其保持前两项的最大尾偶终端桥，当且仅当存在正整数

\[
A,B,u,v
\]

满足

\[
(A,B)=1,\quad\quad AB\mid x,\quad\quad m\mid Bp+A. \tag{1}
\]

写

\[
C=\frac{x}{AB},\quad\quad
R=\frac{4B^2C+1}{m},\quad\quad
H=AR-B,\quad\quad K=BCH,\quad\quad L=2K, \tag{2}
\]

并要求第二对满足

\[
(u,v)=1,\quad\quad u\mid L,\quad\quad v\mid L,\quad\quad
u\equiv2v\pmod R, \tag{3}
\]

以及由它重构的

\[
E=\frac{Lu}{v} \tag{4}
\]

满足

\[
2\mid E,\quad\quad E\le2L-2R. \tag{5}
\]

此时

\[
4K=pR+1,\quad\quad E\mid4K^2,\quad\quad E\equiv1\pmod R,
\]

且

\[
n=\frac{2L-E}{R}
\]

是 \(2\le n<p\) 的偶数。相应的目标和源解为

\[
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK},
\quad\quad
\frac4n=\frac1{nK/E}+\frac1{ABC}+\frac1{ACH}. \tag{6}
\]

## 证明

先设 (1) 成立。因 \((x,m)=1\)，也有 \((A,m)=1\)。又

\[
Bp+A=A(4B^2C+1)-Bm,
\]

故 \(R\) 是正整数，并且

\[
H=AR-B=\frac{Bp+A}{m}>0.
\]

代入 \(x=ABC\) 得

\[
4K=4BC(AR-B)=(p+m)R-(mR-1)=pR+1. \tag{7}
\]

这正是 Type I 互素因子正规形。其目标平方除子为

\[
e=B^2C,\quad\quad e\mid x^2,\quad\quad 4e+1=mR. \tag{8}
\]

现在由 (3) 和 \(L=2K\) 可知 \(v\) 在模 \(R\) 下可逆；事实上 \((L,R)=1\) 由
(7) 给出。因此

\[
E=\frac{Lu}{v}\equiv2L=4K\equiv1\pmod R. \tag{9}
\]

又 (u,v\mid L) 且互素，所以

\[
\frac{L^2}{E}=\frac{Lv}{u}\in\mathbb N,
\]

即 \(E\mid L^2=4K^2\)。式 (5) 正是偶源的奇偶性和自然范围；(9) 则给出
\(n=(4K-E)/R=(2L-E)/R\)。最大尾偶源选择器于是给出 (6)。

反向地，给定一张 Type I 正规形及偶终端桥，互素因子正规形给出唯一的
\((A,B,C)\)，因此 (1)--(2) 成立。令

\[
L=2K,\quad\quad g=(E,L),\quad\quad u=\frac Eg,\quad\quad v=\frac Lg.
\]

由 \(E\mid L^2\) 知 \(u,v\mid L\)，且定义给出 \((u,v)=1\)。桥同余
\(E\equiv4K=2L\pmod R\) 推出 \(u\equiv2v\pmod R\)，而桥的偶性与范围正是
(5)。故两类数据完全等价。

## 含义与边界

第一层 \((A,B)\) 是 Type I 目标除子的普通因子坐标，第二层 \((u,v)\) 是终端桥
因子 \(E/L\) 的既约普通因子坐标。因而目标 \(e\mid x^2\) 与桥 \(E\mid4K^2\)
都不再是需要独立处理的“平方除子黑箱”：它们是两个相互耦合的普通除子对残数问题。

这仍未强制任意 \(p\) 存在 (1)--(5) 的一组数据，故不证明混合终端选择引理。它提供的是
适合跨缺口碰撞/私有因子分析的精确状态：以后任何正向机制必须实际产生这两对因子，或证明
其失败触发 Type II 双尾证书。

五亿至六亿连续审计的全部 247 条 Type I 偶终端桥均由脚本从其原始正规形和桥因子还原为
这两对普通除子，并重新核对两条单位分数恒等式。

~~~bash
python3 -m unittest tests/test_type_i_two_layer_divisor_pair_selector.py -q
~~~
