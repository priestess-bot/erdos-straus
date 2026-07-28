---
kind: claim
claim_id: ghermoul-2025-p2-linear-terminal-factor-pair-equivalence
title: Ghermoul 第二族固定正规形的线性终端桥因子对等价
statement: 设 Ghermoul 第二族坐标 x,y,z 给出核心素数 p，令 R=4y-1、C=4xy-x-y、H=zR-1、K=CH。保持这张 B=1 正规形的线性 Type I 偶终端桥与 4CH 的有向因子对 EQ=4CH 一一对应，其中 E、Q 都至少为 R+1，E 为偶数，且 E=Q=1 模 R。对应关系为 s=(E-1)/R、a=(Q-1)/R、n=aE；于是 p=a+s+asR，E=sR+1 整除 n。该等价把第二族表示提升为线性终端桥仍所需的明确因子对选择条件，但不证明这种因子对对每个第二族表示或核心素数存在。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- literature-audit
- polynomial-family
- type-I
- b1
- linear-source
- terminal-bridge
- factorization
- shifted-source
sources:
- paper: ghermoul2025
  locator: Equations (5), (19), (26)--(29)
  role: second-family-coordinate-context
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# Ghermoul 第二族固定正规形的线性终端桥因子对等价

令 Ghermoul 的第二族坐标为

\[
q=x(4yz-z-1)-yz,
\qquad p=4q+1, \tag{1}
\]

并假定 \(p\) 是核心素数。按[第二族与 \(B=1\) 正规形的等价](ghermoul-2025-p2-b1-normal-form-equivalence.md)，置

\[
R=4y-1,
\qquad C=4xy-x-y,
\qquad H=zR-1,
\qquad K=CH. \tag{2}
\]

则

\[
4K=4CH=pR+1. \tag{3}
\]

以下结论固定这张 \(B=1\) 正规形；它不对同一 \(p\) 的其它正规形作量化。

## 定理

下列两类对象一一对应：

1. 保持 (2) 的目标前三项不变的线性 Type I 偶终端桥，即正整数 \(a,s\) 满足

   \[
   s\equiv1\pmod2,
   \qquad p=a+s+asR, \tag{4}
   \]

   并以

   \[
   E=sR+1,
   \qquad n=p-s=aE \tag{5}
   \]

   作为桥因子和偶源；
2. \(4CH\) 的有向因子对

   \[
   EQ=4CH, \tag{6}
   \]

   满足

   \[
   E\equiv Q\equiv1\pmod R,
   \qquad E,Q\ge R+1,
   \qquad 2\mid E. \tag{7}
   \]

对应显式为

\[
\boxed{
E=sR+1,
\quad Q=aR+1,
\quad
s=\frac{E-1}{R},
\quad a=\frac{Q-1}{R},
\quad n=aE.} \tag{8}
\]

特别地，一张第二族表示本身只给出目标正规形；它给出**线性**终端桥当且仅当 (6)--(7) 的因子对存在。

## 证明

若有 (4)，则 (5) 给出

\[
(sR+1)(aR+1)
=1+(a+s+asR)R
=pR+1
=4CH. \tag{9}
\]

令 \(Q=aR+1\) 即得 (6)。由于 \(a,s\ge1\)，有 \(E,Q\ge R+1\)；又 \(R\) 为奇数而 \(s\) 为奇数，故 \(E=sR+1\) 为偶数。其余同余见 (8)。

反之，给定 (6)--(7)，按 (8) 定义 \(a,s\)。它们是正整数；\(E\) 偶而 \(R\) 奇，所以 \(s\) 为奇数。由 (3)、(6) 得

\[
1+pR=EQ=(1+sR)(1+aR)
=1+(a+s+asR)R,
\]

从而得到 (4)。再由 (8) 有 \(n=aE=p-s\) 和 \(E\mid n\)。同时

\[
E\mid4K,
\qquad E\equiv1\pmod R,
\qquad
\frac{4K-E}{R}=aE=n. \tag{10}
\]

因此 \(E\mid4K^2\)，且 \(n\ge2\) 自动等价于

\[
E\le4K-2R. \tag{11}
\]

这正是[线性上半区一般 \(B\) 终端桥](type-I-linear-source-general-b-terminal-selector-conjecture.md)在已给定 \(B=1\) 目标正规形上的偶终端条件。源解的第一分母为

\[
\frac{nK}{E}=aK,
\]

故这确实恢复保持该目标前两项的线性 Type I 偶终端桥。两个构造在 (8) 下显然互逆。

## 两个正对照与一个边界对照

1. \(p=73\) 可取 \((x,y,z)=(4,1,2)\)，故 \((R,C,H)=(3,11,5)\)。因子对

   \[
   (E,Q)=(4,55)
   \]

   给出 \((s,a,n)=(1,18,72)\)。
2. \(p=297049\) 的移位 \(B=1\) 证书对应

   \[
   (x,y,z)=(4,5,1046),
   \qquad (R,C,H)=(19,71,19873).
   \]

   因子对

   \[
   (E,Q)=(476,11857)
   \]

   恢复 \((s,a,n)=(25,624,297024)\)。
3. \(p=878089\) 已知的一张非线性 \(B=1\) 正规形有

   \[
   (x,y,z)=(36,21,74),
   \qquad (R,C,H)=(83,2967,6141).
   \]

   穷尽 \(4CH\) 的因子后，(6)--(7) 没有解。这与该形式的桥源满足
   \(\beta=9>1\) 一致；它不是“每张 \(p_2\) 形式都线性闭合”的证据。

这张卡既不证明 Ghermoul 第二族在核心残余上的覆盖，也不把 \(B=1\) 的因子对条件推广到一般 \(B\)。它的作用是将文献参数化与当前线性终端选择器之间的额外、不可省略的因子选择量词明确分开。

~~~bash
python3 -m unittest tests.test_ghermoul_p2_linear_terminal_factor_pair_equivalence -v
~~~
