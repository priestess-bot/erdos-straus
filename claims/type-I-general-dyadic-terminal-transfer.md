---
kind: claim
claim_id: type-I-general-dyadic-terminal-transfer
title: 一般二进传输的偶终端判据
statement: 设 L=2K、gcd(L,R)=1，且互素除子 a,b|L 满足 a=2^j b mod R。对 j>=1 定义 E_j=2^(1-j)L a/b。令 lambda=v_2(L)、alpha=v_2(a)、beta=v_2(b)。则 E_j 为整数、偶数且 E_j|L^2 当且仅当 1<=j<=lambda+alpha-beta；若再有 a<2^j b，则 E_j=1 mod R 且 n=(2L-E_j)/R 为满足 0<n<p 的偶数终端（当 4K=pR+1）。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- dyadic
- even-terminal
- finite-exponent
- divisor-ratio
- selector
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 一般二进传输的偶终端判据

## 设置

设 $L=2K$、$\gcd(L,R)=1$，并取互素正除子 $a,b\mid L$。令 $j\ge1$，假设

\[
a\equiv2^j b\pmod R.
\]

定义有理式

\[
E_j=2^{1-j}L\frac ab.
\]

若 $4K=pR+1$，则 $2L=4K\equiv1\pmod R$。

## 精确的二进判据

置

\[
\lambda=v_2(L),\qquad \alpha=v_2(a),\qquad \beta=v_2(b).
\]

则

\[
\boxed{
E_j\text{ 为整数、偶数且 }E_j\mid L^2
\Longleftrightarrow
1\le j\le\lambda+\alpha-\beta.}
\]

这里右端必须至少为 $1$；特别地，$j=1$ 可能因 $b$ 吸收了全部二进预算而不给出偶数
终端，$j>1$ 只能在剩余二进预算允许时使用。

### 证明

对每个奇素数 $q\mid L$，$E_j$ 中的指数为
\[
v_q(L)+v_q(a)-v_q(b)\in[0,2v_q(L)],
\]
所以奇部自动是 $L^2$ 的除子。二进指数为
\[
e_2=\lambda+\alpha-\beta+1-j.
\]

由于 $j\ge1$、$\alpha\le\lambda$ 且 $\beta\ge0$，有
$e_2\le2\lambda$。因此 $E_j$ 整数且偶数、并且二进部分整除 $L^2$，恰好等价于
$e_2\ge1$，即所述区间。证毕。

## 同余和终端范围

在上述二进条件下，$E_j$ 是整数。由于 $2b$ 与 $R$ 互素，可在单位群中把
$a\equiv2^jb\pmod R$ 乘以 $2^{1-j}L/b$，得到

\[
E_j\equiv2L\equiv1\pmod R.
\]

若再满足方向条件

\[
a<2^j b,
\]

则 $0<E_j<2L$。定义

\[
n=\frac{2L-E_j}{R}=\frac{4K-E_j}{R}.
\]

因为 $E_j$ 与 $2L$ 都是偶数，且 $R\mid(2L-E_j)$，所以 $n$ 是正偶数；正性还给出
$E_j\le2L-2R$。进一步
\[
n<\frac{2L}{R}=p+\frac1R,
\]
故整数 $n\le p$。若 $n=p$，则
$2L-E_j=pR=4K-1$ 为奇数，而左边为偶数，矛盾。因此 $0<n<p$。

综上，$E_j$ 满足

\[
E_j\mid L^2,\qquad E_j\text{ 偶数},\qquad E_j\equiv1\pmod R,\qquad
E_j\le4K-2R,
\]

并给出合法偶终端 $n=(4K-E_j)/R$。

## 与统一选择器的关系

当 $j=1$ 时这是普通比值二传输；$j>1$ 只改变二进指数预算，不自动产生同余碰撞。
故广义二进路线的实际增量必须在“存在 $a\equiv2^jb$”这一有限群命中问题上衡量，
而不能把形式上的 $E_j$ 定义误报为新的全称证书。该卡也不证明目标纤维存在或跨状态
递降；它只闭合统一选择器的终端接口。
