---
kind: claim
claim_id: type-I-general-bidirectional-dyadic-window-selector
title: 双向广义二进窗口的规范最大指数选择引理
statement: 设 R>1 为奇数，p,K 为正整数，L=2K 且 2L=4K=pR+1。若 A,B 是 L 的互素正除子，j0≥0 且 A≡2^j0 B (mod R)，令 J_+=v_2(L)+v_2(A)-v_2(B)、J_-=v_2(L)+v_2(B)-v_2(A)，并在 1≤j≤J_± 内分别取 j≡±j0 (mod ord_R(2)) 的窗口 W_±。每个非空窗口只需检查其最大指数 j_±^*：该固定有序因子对的双向广义二进终端存在，当且仅当 (W_+ 非空且 A<2^(j_+^*)B) 或 (W_- 非空且 B<2^(j_-^*)A)。若两个窗口都非空，则两条高度不等式不可能同时失败，故必有局部偶终端。特别地，ord_R(2)≤v_2(L)-|v_2(A)-v_2(B)| 是充分条件；奇除子情形退化为 ord_R(2)≤v_2(L)。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-general-dyadic-terminal-transfer
topics:
  - type-I
  - dyadic
  - bidirectional
  - canonical-selector
  - multiplicative-order
  - finite-exponent
  - even-terminal
  - proof-program
sources:
  - claim: type-I-general-dyadic-terminal-transfer
    role: exact-directional-budget-and-terminal-verifier
visibility: public
last_checked: '2026-07-31'
---

# 双向广义二进窗口的规范最大指数选择引理

## 设置与两个精确预算

设 \(R>1\) 为奇数，\(p,K\) 为正整数，且

\[
L=2K,
\qquad
2L=4K=pR+1.
\tag{1}
\]

特别地 \((L,R)=1\)。取互素正除子

\[
A,B\mid L,
\qquad
(A,B)=1,
\tag{2}
\]

并假设对某个整数 \(j_0\ge0\) 有

\[
A\equiv2^{j_0}B\pmod R.
\tag{3}
\]

记

\[
o=\operatorname{ord}_R(2),
\quad
\lambda=v_2(L),
\quad
\alpha=v_2(A),
\quad
\beta=v_2(B).
\tag{4}
\]

一般二进传输对两个方向给出的精确预算分别是

\[
J_+=\lambda+\alpha-\beta,
\qquad
J_-=\lambda+\beta-\alpha.
\tag{5}
\]

定义正、反两个有限窗口

\[
\begin{aligned}
W_+
&=\{j\in\mathbb Z:\ 1\le j\le J_+,\ j\equiv j_0\pmod o\},\\
W_-
&=\{j\in\mathbb Z:\ 1\le j\le J_-,\ j\equiv-j_0\pmod o\}.
\end{aligned}
\tag{6}
\]

若窗口非空，令

\[
j_+^*=\max W_+,
\qquad
j_-^*=\max W_-.
\tag{7}
\]

这里预算必须分方向。在式 (2) 的互素条件下，只有 \(A,B\) 都为奇数时，式 (5) 才共同退化为
\(J_+=J_-=v_2(L)\)。

## 最大指数给出精确规范选择

对任意 \(j\in W_+\)，式 (3) 和一般二进传输判据保证

\[
E_+(j)=2^{1-j}L\frac AB
\tag{8}
\]

是偶整数并整除 \(L^2\)，且 \(E_+(j)\equiv1\pmod R\)。这个方向剩下的唯一
高度条件是

\[
A<2^jB.
\tag{9}
\]

式 (9) 随 \(j\) 单调：若它对窗口中某个指数成立，就必对最大指数 \(j_+^*\)
成立。反过来，最大指数命中当然给出一个合法候选。因此

\[
\boxed{
\text{正向存在广义二进终端}
\Longleftrightarrow
W_+\ne\varnothing\ \text{且}\ A<2^{j_+^*}B.}
\tag{10}
\]

由 (3) 在单位群中取逆方向，得到

\[
B\equiv2^{-j_0}A\pmod R.
\]

同理有

\[
\boxed{
\text{反向存在广义二进终端}
\Longleftrightarrow
W_-\ne\varnothing\ \text{且}\ B<2^{j_-^*}A,}
\tag{11}
\]

对应因子为

\[
E_-(j)=2^{1-j}L\frac BA.
\tag{12}
\]

式 (10)--(11) 给出固定有序因子对内的方向规范选择器：每个方向至多检查一个最大
指数，不必遍历整个窗口。若两向都命中，本文和复现器约定正向优先，以得到唯一输出。

## 双窗口强制一个终端

若 \(W_+\) 与 \(W_-\) 都非空，而两个最大指数的高度条件同时失败，则

\[
A\ge2^{j_+^*}B,
\qquad
B\ge2^{j_-^*}A.
\tag{13}
\]

相乘并消去正数 \(AB\)，得到

\[
1\ge2^{j_+^*+j_-^*}>1,
\]

矛盾。因此

\[
\boxed{
W_+\ne\varnothing\ \text{且}\ W_-\ne\varnothing
\Longrightarrow
\text{至少一个方向产生合法偶终端}.}
\tag{14}
\]

命中方向取相应的 \(E=E_\pm(j_\pm^*)\)。一般二进传输给出

\[
n=\frac{4K-E}{R},
\qquad
0<n<p,
\qquad
n\equiv0\pmod2.
\tag{15}
\]

所以 (14) 强制的是满足一般二进传输全部算术条件的局部偶终端，不只是一个
模 \(R\) 的形式碰撞。

## 正代表、充分条件与精确失败三分

用

\[
\langle t\rangle_o=1+((t-1)\bmod o)
\tag{16}
\]

表示模 \(o\) 的正代表，并令

\[
u=\langle j_0\rangle_o,
\qquad
v=\langle-j_0\rangle_o.
\]

当 \(o\mid j_0\) 时二者都等于 \(o\)，不能取成 0。两个窗口非空的条件分别为

\[
W_+\ne\varnothing\Longleftrightarrow u\le J_+,
\qquad
W_-\ne\varnothing\Longleftrightarrow v\le J_-.
\tag{17}
\]

在对应窗口非空时，最大指数有闭式

\[
j_+^*=u+o\left\lfloor\frac{J_+-u}{o}\right\rfloor,
\qquad
j_-^*=v+o\left\lfloor\frac{J_--v}{o}\right\rfloor.
\tag{18}
\]

由于

\[
\min(J_+,J_-)=\lambda-|\alpha-\beta|,
\]

得到一个不依赖 \(j_0\) 的充分条件：

\[
\boxed{
o\le\lambda-|\alpha-\beta|
\Longrightarrow
\text{至少一个方向产生合法偶终端}.}
\tag{19}
\]

特别地，若 \(A,B\) 都为奇数，则 \(\alpha=\beta=0\)，故

\[
o\le v_2(L)
\Longrightarrow
\text{至少一个方向命中}.
\tag{20}
\]

这正是现有线性块阶—预算二分的全称部分。更精确地，固定有序因子对的二进窗口族
未决只能属于以下三类之一：

1. \(W_+=W_-=\varnothing\)；
2. 只有 \(W_+\) 非空，且 \(A\ge2^{j_+^*}B\)；
3. 只有 \(W_-\) 非空，且 \(B\ge2^{j_-^*}A\)。

“两个窗口都非空但仍未决”由 (14) 无条件排除。

## 偶除子边界

不能把奇除子推论 (20) 原样用于任意除子。取核心素数 \(p=313\equiv1\pmod {24}\)，并令

\[
R=7,
\quad K=548,
\quad L=1096=2^3\cdot137,
\quad A=1,
\quad B=1096.
\tag{21}
\]

这里 \(4K=2192=313\cdot7+1\)，所以仍处在本引理的终端正规化范围内。

则 \(A\equiv2B\pmod7\)，且

\[
\operatorname{ord}_7(2)=3=v_2(L).
\]

但方向预算为

\[
J_+=0,
\qquad
J_-=6.
\]

所以正向窗口为空；反向窗口只有 \(2,5\)，而
\(1096<2^2\) 与 \(1096<2^5\) 都失败。这个固定因子对在两个方向都没有终端；它不与
(14) 矛盾，因为只有一个窗口非空，也不排除同一 \((p,R,K)\) 的其它因子对产生终端。
这个例子说明式 (5) 中的方向赋值不能被共同的 \(v_2(L)\) 取代。

## 冻结线性谱的实现回归

线性块不平衡归一化产生互素奇数 \(A,B\)，因此两个预算都等于
\(J_{\max}=v_2(2K)\)。对现有 15,356 个有向二进状态应用最大窗口选择器，得到：

\[
\begin{array}{c|r|r|r}
\text{窗口类型}&\text{状态数}&\text{终端}&\text{未决}\\ \hline
\text{none}&7433&0&7433\\
\text{forward only}&6460&2274&4186\\
\text{reverse only}&232&178&54\\
\text{both}&1231&1231&0.
\end{array}
\tag{22}
\]

按“正向优先，否则反向”的规范规则，3,683 个命中状态分成

\[
2776\text{ 个正向选择},
\qquad
907\text{ 个反向选择}.
\tag{23}
\]

冻结分类与最大窗口选择器逐状态完全一致，且所有 1,231 个双窗口状态均命中。复现入口为
`reproductions/type_i_general_bidirectional_dyadic_window_selector.py`，冻结结果为
`reproductions/type-i-general-bidirectional-dyadic-window-selector-results.json`。

## 逻辑边界

本引理完成的是广义 \(2^j\) 家族内部的规范有限选择：它把每个方向的指数搜索压成一个
最大窗口端点，并严格排除双窗口未决。它没有证明至少一个窗口总是非空，也没有把偶终端
自动升级为原目标的 Type I/II 证书。把 (15) 登记为递降边仍需给出源解、显式解提升和
严格下降的合法状态合同；否则它只能作为终端接口或下一层候选生成器。
