---
kind: claim
claim_id: type-I-generalized-dyadic-natural-lift-equivalence
title: 广义二进偶前驱的自然标记提升等价与 F 态零分支
statement: 设 4K=pR+1、R>3 为奇数，且广义二进数据 E,n 满足 E|4K^2、E≡1 (mod R)、0<E<4K、n=(4K-E)/R>0。则 E|nK、E|n^2，且 alpha=nK/E 为整数；并有 4/n-1/alpha=R/K=4/p-1/(pK)，所以包含标记分母 alpha 的 n-解与包含标记分母 pK 的 p-解由替换 alpha↔pK 精确双射。该标记源非空当且仅当 R/K 可分成两个正单位分数，等价于当前图表存在中心 Type I 除子 D|K^2、D≡-K (mod R)。因此对 finite-exponent F 状态，任意这种广义二进偶前驱的自然标记源均为空；且 alpha 不等于平凡偶数解的 n/2 或 n。广义二进候选本身不是满足 E4 的终端或递降边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-general-dyadic-terminal-transfer
  - type-I-target-divisor-even-terminal-selector
  - two-denominator-lift-criterion
  - type-I-general-b-centered-square-spectrum
  - denominator-escape-state-contract
topics:
  - type-I
  - generalized-dyadic
  - even-predecessor
  - marked-solution
  - solution-lift
  - F-state
  - centered-spectrum
  - proof-boundary
sources:
  - claim: type-I-general-dyadic-terminal-transfer
    role: even-predecessor-arithmetic
  - claim: type-I-target-divisor-even-terminal-selector
    role: marked-source-and-target-interface
  - claim: type-I-general-b-centered-square-spectrum
    role: two-unit-fraction-factorization
  - claim: denominator-escape-state-contract
    role: E4-acceptance-criterion
visibility: public
last_checked: '2026-07-31'
---

# 广义二进偶前驱的自然标记提升等价与 F 态零分支

## 1. 设置

设

\[
4K=pR+1,
\qquad R>3\text{ 为奇数},
\tag{1}
\]

并设一个广义二进候选已经给出正整数 \(E,n\)，满足

\[
E\mid4K^2,
\qquad E\equiv1\pmod R,
\qquad 0<E<4K,
\qquad n=\frac{4K-E}{R}>0.
\tag{2}
\]

在一般二进传输中，\(E,n\) 还都是偶数。下面的提升等价只需要 (1)--(2)；偶性只负责
保证较小方程 \(4/n\) 有平凡解。

## 2. 标记分母自动为整数

定义

\[
\alpha=\frac{nK}{E}.
\tag{3}
\]

由 \(E\equiv1\pmod R\) 得 \((E,R)=1\)。另一方面，\(nR=4K-E\)，所以

\[
nRK=4K^2-EK\equiv0\pmod E.
\]

结合 \((E,R)=1\) 可约去 \(R\)，得到

\[
\boxed{E\mid nK,\qquad E\mid n^2,\qquad \alpha\in\mathbb N.}
\tag{4}
\]

这说明广义二进候选的最小问题不是 \(nK/E\) 的整除性，而是是否存在包含这个指定分母
的较小方程解。

这里 \(E\mid n^2\) 也自动成立：由 \(nR\equiv4K\pmod E\) 平方后得到
\(n^2R^2\equiv16K^2\equiv0\pmod E\)，再用 \((E,R)=1\) 约去 \(R^2\)。

## 3. 自然标记提升的精确双射

由 (1)--(4) 直接计算

\[
\frac4n-\frac1\alpha
=\frac{4K-E}{nK}
=\frac RK,
\tag{5}
\]

而

\[
\frac4p-\frac1{pK}
=\frac{4K-1}{pK}
=\frac RK.
\tag{6}
\]

因此对任意正整数 \(u,v\)，

\[
\frac4n=\frac1\alpha+\frac1u+\frac1v
\iff
\frac RK=\frac1u+\frac1v
\iff
\frac4p=\frac1{pK}+\frac1u+\frac1v.
\tag{7}
\]

所以替换

\[
\boxed{(\alpha,u,v)\longleftrightarrow(pK,u,v)}
\tag{8}
\]

给出自然标记源与目标标记解之间的精确双射。它确实是一个全域解提升，但前提是左端标记
解集非空；偶数 \(n\) 的未标记可解性不能替代这一点。

这也精确落入[两分母提升判据](two-denominator-lift-criterion.md)。以源标记坐标
\(a=\alpha\) 代入，其判别量为

\[
D=np-4(p-n)\alpha=\frac{n^2}{E}>0,
\tag{9}
\]

且恢复分母为

\[
a'=\frac{np\alpha}{D}=pK.
\tag{10}
\]

所以一旦标记源非空，(8) 不只是形式恒等式，而是现有提升接口中的合法边公式。

## 4. 非空性恰等价于当前中心 Type I 命中

两尾方程

\[
\frac RK=\frac1u+\frac1v
\tag{11}
\]

等价于

\[
(Ru-K)(Rv-K)=K^2.
\tag{12}
\]

若置 \(D=Ru-K\)，则

\[
D\mid K^2,
\qquad D\equiv-K\pmod R.
\tag{13}
\]

反过来，任意满足 (13) 的正除子 \(D\) 与配对除子 \(K^2/D\) 都恢复

\[
u=\frac{K+D}{R},
\qquad
v=\frac{K+K^2/D}{R}.
\tag{14}
\]

两配对除子不可能都等于 \(K\)：否则 \(R\mid2K\)，而 (1) 给出 \((R,K)=1\)，与
奇数 \(R>1\) 矛盾。因此可把 (13) 规范到 \(D<K\)，它正是当前 \((R,K)\) 图表的
中心 Type I 除子判据。于是

\[
\boxed{
W_{n,\alpha}\ne\varnothing
\iff
\frac RK\text{ 有两单位分数分解}
\iff
\text{当前图表为 Type I hit}.}
\tag{15}
\]

对 finite-exponent F 状态，定义上不存在 (13) 的除子，故每个广义二进 \(E\) 的自然标记
源都为空。注意这个结论与选中了哪一个 \(E\) 无关。

## 5. 平凡偶数解不能填补标记

若 \(n\) 为偶数，则总有未标记平凡解

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n.
\tag{16}
\]

但若 \(\alpha=n/2\)，则 (3) 给出 \(E=2K\)。结合 \(E\equiv1\pmod R\) 与
\(4K\equiv1\pmod R\) 得 \(2\equiv1\pmod R\)，不可能。若 \(\alpha=n\)，则
\(E=K\)，同理得到 \(4\equiv1\pmod R\)，只可能 \(R\mid3\)，与 \(R>3\) 矛盾。
所以

\[
\boxed{\alpha\notin\{n/2,n\}.}
\tag{17}
\]

平凡解的三个坐标均不能承担自然标记分母。

## 6. 对统一选择器的含义

旧文献和仓库早期主张中的“偶终端”只表示已经构造出较小偶数 \(n\)。按照当前
[状态合同](../concepts/denominator-escape-state-contract.md)，在 F 状态上它只能登记为
`unlifted_generalized_dyadic_candidate`：

1. 它不是原素数的直接 Type I/II 证书；
2. 自然标记源由 (15) 精确判为空；
3. 平凡偶数基例由 (17) 无法进入该标记源；
4. 若要成为真正递降，必须构造不同的标记集与全域 E4 提升，或采用另一种一/两分母提升。

因此，在已经分类为 F 后继续只寻找更多同类 \(E\) 不会推进证明；真正缺口是非自然解提升。
