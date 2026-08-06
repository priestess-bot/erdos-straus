---
kind: claim
claim_id: type-I-target-fiber-neighbor-dyadic-normalization
title: 目标纤维近邻对的规范二进归一化与关系格中性
statement: 对合法 Type I 图表 4K=pR+1，任何目标指数纤维中的近邻对都规范地产生一个广义 2^j 偶终端见证；该见证给出的 E 与 n 完全等于近邻终端的 E 与 n，其扩展素数坐标关系向量也恰为近邻差。因此近邻终端不是新的 Fourier q-primary demand；它只是一个短核关系的二进正规化。反向需要目标纤维在相应关系透镜中实际占据，不能由有界二进关系单独推出。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-neighbor-terminal
  - type-I-general-dyadic-terminal-transfer
  - type-I-short-relation-even-terminal
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
topics:
- type-I
- target-fiber
- near-pair
- generalized-dyadic
- relation-lattice
- Fourier
- terminal-normalization
- proof-program
sources:
  - claim: type-I-target-fiber-neighbor-terminal
    role: near-pair-terminal
  - claim: type-I-general-dyadic-terminal-transfer
    role: dyadic-terminal-criterion
  - claim: type-I-short-relation-even-terminal
    role: bounded-kernel-relation-terminal
visibility: public
last_checked: '2026-08-06'
---

# 目标纤维近邻对的规范二进归一化与关系格中性

## 1. 设置

设

\[
4K=pR+1,
\qquad
K=\prod_{i=1}^r q_i^{\nu_i},
\]

其中 \(R\) 为奇数。令 \(z,w\) 是目标指数纤维
\(\mathcal Z^-_{R,K}\) 中两个不同的近邻点，即

\[
|z_i-w_i|\le\nu_i\quad(1\le i\le r).
\tag{1}
\]

将两点互换后，令

\[
\delta=z-w,
\qquad
\rho=\prod_iq_i^{\delta_i}=\frac ab<1,
\tag{2}
\]

其中

\[
a=\prod_{\delta_i>0}q_i^{\delta_i},
\qquad
b=\prod_{\delta_i<0}q_i^{-\delta_i}.
\tag{3}
\]

由 (1)，\(a,b\mid K\) 且 \((a,b)=1\)。两点属于同一目标纤维还给出

\[
\rho\equiv1\pmod R,
\qquad a\equiv b\pmod R.
\tag{4}
\]

写 \(b=2^\beta b_0\)，其中 \(b_0\) 为奇数，并令 \(L=2K\)。

## 2. 规范二进见证

\[
\boxed{
\begin{array}{c|c|c|c}
\beta & A & B & j\\ \hline
0 & 2a & b & 1\\
>0 & a & b_0 & \beta
\end{array}}
\tag{5}
\]

在两种情形中，\(A,B\) 都是互素的 \(L\) 的除子，并且

\[
A\equiv2^jB\pmod R,
\qquad
A<2^jB.
\tag{6}
\]

此外，\(j\) 满足一般二进传输的精确二进预算。因此 (5) 是一个合法的广义
\(2^j\) 偶终端见证，且其终端数据恰为近邻对给出的数据：

\[
\boxed{
E_j=2^{1-j}L\frac AB=4K\frac ab=:E_{\rm near},
\qquad
n=\frac{2L-E_j}{R}=\frac{4K-E_{\rm near}}R.}
\tag{7}
\]

### 证明

若 \(\beta=0\)，则 \(b\) 为奇数。由 \(a\mid K\) 得 \(2a\mid L\)，并且
\((2a,b)=1\)。式 (4) 给出 \(2a\equiv2b\pmod R\)，而 \(a<b\) 给出
\(2a<2b\)。此时 \(j=1\) 自动满足二进预算，且

\[
E_1=L\frac{2a}{b}=4K\frac ab.
\tag{8}
\]

若 \(\beta>0\)，则 \(a\) 与 \(b_0\) 都是奇数，且
\(1\le\beta\le v_2(K)<v_2(L)\)。所以 \(A=a\)、\(B=b_0\) 是互素的
\(L\) 的除子，\(j=\beta\) 满足二进预算。由 (4)，

\[
a\equiv2^\beta b_0\pmod R,
\qquad
a<2^\beta b_0,
\]

并且

\[
E_\beta
=2^{1-\beta}L\frac a{b_0}
=4K\frac a{2^\beta b_0}.
\tag{9}
\]

两种情形均得到 (6)--(7)。一般二进传输定理于是给出同一个偶终端。证毕。

## 3. 关系格中性

在 \(\operatorname{Supp}(K)\cup\{2\}\) 的指数坐标中，令 \(v(x)\) 表示
正整数 \(x\) 的赋值向量，\(e_2\) 表示二的单位向量。由 (5) 逐项计算得到

\[
\boxed{v(A)-v(B)-j e_2=\delta=z-w.}
\tag{10}
\]

因此该二进见证的关系向量位于乘法核关系格：

\[
\prod_iq_i^{\delta_i}\equiv1\pmod R.
\tag{11}
\]

任意有限群 Fourier 角色在这个关系上取单位相位。故近邻对本身不能产生非平凡的
q-primary `SOURCE_RANK_DEMAND`；若一个独立的 source-map 使用它，只能把 (10)
作为标签相容性条件或 \(\mathrm{F\_SOURCE\_LABEL\_OBSTRUCTED}\) 的见证，不能把它
再次收费为 q-height 容量。

这也说明 (7) 只是在终端层面对短核关系的规范化，不提供有限指数 F 状态所缺少的
非自然标记提升。

## 4. 二进终端并不反推近邻

反向需要额外的仿射占据条件。一个没有外支撑的有界二进关系向量 \(\ell\) 只有在

\[
\mathcal Z^-_{R,K}\cap B_\nu\cap(B_\nu+\ell)\ne\varnothing
\tag{12}
\]

时才对应一个近邻对；其中 \(B_\nu=\{x:|x_i|\le\nu_i\}\)。广义二进见证只给出
关系 \(\ell\)，并不保证 (12) 中的目标纤维透镜被占据。因此不能用“存在有界二进
关系”替代近邻检测，也不能把一般二进终端反向解释为目标纤维的 Fourier 容量。

## 5. 一个 \(j=3\) 归一化例

取

\[
p=164150809,
\qquad R=23,
\qquad
K=2^4\cdot3^2\cdot61\cdot107453.
\]

目标纤维中的一对近邻差给出 \(\rho=1/24\)，故 \(a=1\)、\(b=24\)、
\(\beta=3\)、\(b_0=3\)。规范化 (5) 给出

\[
(A,B,j)=(1,3,3),
\qquad
1\equiv8\cdot3\pmod{23}.
\]

式 (7) 两侧均给出

\[
E=157311192,
\qquad n=157311192.
\]

这说明 \(j>1\) 的二进见证也可以恰好只是近邻短关系的规范表达，而不是新的
Fourier 或 q 进容量方向。

## 6. 研究边界

本引理只消除近邻终端与广义二进终端之间的重复搜索，并保留它们的几何 provenance。
它不证明每个目标纤维有近邻对，也不把广义二进偶前驱升级为可提升递降。推进全称
选择器仍需要一个不在乘法核中的、带来源标签的 source-image 相位 lift，或一个通过
E1--E5 的独立严格下降。
