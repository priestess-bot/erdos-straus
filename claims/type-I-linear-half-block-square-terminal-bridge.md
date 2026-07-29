---
kind: claim
claim_id: type-I-linear-half-block-square-terminal-bridge
title: 线性源半块平方给出的偶终端桥
statement: 设 p=a+s+asR 为线性源状态，p≡1 mod4、s 为奇数、R≡3 mod4，且 a 也为奇数且 a≠s。令 X=min((aR+1)/2,(sR+1)/2)、Y=max((aR+1)/2,(sR+1)/2)、K=XY。若同一 R 上存在目标 Type I 正规形，即存在 d|K^2、d≤K 且 d≡-K modR，则 E=4X^2 是该正规形的偶终端因子：E|4K^2、E≡1 modR、E≤4K-2R，且源 n=(4K-E)/R=2X|a-s| 为严格更小的偶数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- half-block
- terminal-bridge
- even-source
- square-factor
- mixed-selector
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 线性源半块平方给出的偶终端桥

## 设置

设

\[
p=a+s+asR,\qquad p\equiv1\pmod4,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4. \tag{1}
\]

再假定 \(a\) 为奇数且 \(a\ne s\)。定义两个半块

\[
G=\frac{aR+1}{2},\qquad H=\frac{sR+1}{2},
\qquad K=\frac{pR+1}{4}=GH. \tag{2}
\]

令

\[
X=\min(G,H),\qquad Y=\max(G,H). \tag{3}
\]

假设同一模数 \(R\) 上已经存在一个目标 Type I 正规形。按目标平方除子恢复判据，这等价于
存在某个 \(d\mid K^2\)、\(d\le K\) 且 \(d\equiv-K\pmod R\)；该假设只负责提供正规形，下面的终端因子
由线性源半块显式给出。

## 定理

若 \(G\ne H\)，则令

\[
E=4X^2. \tag{4}
\]

在该目标正规形上，\(E\) 满足

\[
E\mid4K^2,\qquad E\equiv1\pmod R,
\qquad E\le4K-2R,\qquad 2\mid E. \tag{5}
\]

因此

\[
n=\frac{4K-E}{R}=2X\lvert a-s\rvert \tag{6}
\]

是严格小于 \(p\) 的偶数，并给出保持该正规形前两项的反向终端桥。

## 证明

由 \(a,s\) 和 \(R\) 均为奇数，两个半块确实为整数。因

\[
4K=(aR+1)(sR+1),
\]

得到 \(K=GH=XY\)。又 \(2X=tR+1\) 对某个 \(t\in\{a,s\}\) 成立，故

\[
2X\equiv1\pmod R,
\qquad E=4X^2\equiv1\pmod R. \tag{7}
\]

显然 \(E\) 为偶数，且

\[
\frac{4K^2}{E}=\frac{4X^2Y^2}{4X^2}=Y^2\in\mathbb Z, \tag{8}
\]

所以 \(E\mid4K^2\)。由于 \(G\ne H\)，有 \(Y-X\ge1\)，并且

\[
\frac{4K-E}{R}
=\frac{4X(Y-X)}R
=2X|a-s|, \tag{9}
\]

因为 \(|a-s|R=2|H-G|\)。这说明 (6) 为正偶整数。更强地，
\(X\ge(R+1)/2\) 且两个奇数 \(a,s\) 不相等，所以 \(|a-s|\ge2\)，从而

\[
4K-E=nR\ge2R, \tag{10}
\]

即得到大小界。又 \(E>1\)，而 \(4K=pR+1\)，故

\[
n<p\quad\Longleftrightarrow\quad 4K-E<pR
\quad\Longleftrightarrow\quad E>1. \tag{11}
\]

最后，给定的 \(d\mid K^2\)、\(d\le K\)、\(d\equiv-K\pmod R\) 恢复同一 \(R\) 的 Type I 正规形；选择器
(5) 随即把 (4) 转成保持前两项的反向二尾分解。证毕。

## 例子

取

\[
p=73=3+7+3\cdot7\cdot3,
\qquad R=3,
\]

则 \(G=5\)、\(H=11\)、\(K=55\)，所以 \(X=5\)、\(E=100\)，并得到

\[
n=\frac{220-100}{3}=40=2\cdot5\cdot(7-3).
\]

在 \(R=3\) 的目标正规形 \((A,B,C,m)=(2,1,11,15)\) 上，这确实是一条偶源终端桥。

## 边界与意义

该定理不是全称选择器：它要求线性源与目标平方命中使用同一个 \(R\)，并排除了
\(a=s\) 的退化半块情形。它的贡献是消除这类状态中独立的“偶性/大小”障碍：一旦跨层目标
平方除子在该 \(R\) 命中，终端因子不必再从 \(K^2\) 中搜索，而由较小半块唯一给出。

因此，对混合终端选择猜想，含两个奇端点的线性状态可拆成：

\[
\text{同一 }R\text{ 的目标平方命中}
\Longrightarrow
\text{显式偶终端桥};
\]

剩余真正开放的是普通 Type II 遗漏素数是否必有这样的线性状态及同 \(R\) 的目标平方命中，
或是否转入另一 \(R\)/递降分支。该卡不把有限压力谱上的命中统计升级为全称证明。
