---
kind: claim
claim_id: type-I-linear-two-block-kneser-f-obstruction
title: 线性两块除子积集的 Kneser F 型必要条件
statement: 设 gcd(K,R)=1 且 K=γL，令 X=A_R(γ)、Y=A_R(L)、H=H_R(K)、T=Stab_H(XY)。则 A_R(K)=XY。若状态为 F 型，即 -1∈H 但 -1∉C_R(K)，则 2|XY|≤|H|，并有 |XT|+|YT|-|T|≤|H|/2；特别地，T={1} 时 |X|+|Y|≤|H|/2+1。故若两块在稳定子群商中的投影违反该半密度上界，必命中一般 B 目标；对线性源状态，这一命中与源侧偶因子 E=sR+1 合并，给出混合终端选择器的一条充分分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- divisor-residues
- additive-combinatorics
- Kneser-theorem
- two-block
- terminal-bridge
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: Kneser-product-set-input
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 线性两块除子积集的 Kneser F 型必要条件

## 两块状态

设 (R) 为奇数，(gcd(K,R)=1)，并把一个线性源状态诱导的目标参数写成

$$
K=\gamma L. \tag{1}
$$

这里不要求 (gamma,L) 互素；在线性源的通常记号中，它们分别来自源块和仿射块的
二进制归一化。对任意正整数 (Nmid K)，置

$$
\mathcal A_R(N)=\{d\bmod R:d\mid N\},
\qquad
\mathcal H=\mathcal H_R(K)=\langle q\bmod R:q\mid K\rangle. \tag{2}
$$

记

$$
X=\mathcal A_R(\gamma),
\qquad
Y=\mathcal A_R(L),
\qquad
T=\operatorname{Stab}_{\mathcal H}(XY). \tag{3}
$$

其中 (T) 是乘法作用下的稳定子群：(hXY=XY) 的所有 (h\in\mathcal H) 构成 (T)。

## 两块分解与 F 型上界

有精确积集恒等式

$$
\boxed{\mathcal A_R(K)=XY.} \tag{4}
$$

若该状态属于 F 型，即

$$
-1\in\mathcal H,
\qquad
-1\notin\mathcal C_R(K),
\qquad
\mathcal C_R(K)=\mathcal A_R(K)\mathcal A_R(K)^{-1}, \tag{5}
$$

则

$$
XY\cap(-XY)=\varnothing,
\qquad
2|XY|\le|\mathcal H|. \tag{6}
$$

另一方面，Kneser 定理给出

$$
|XT|+|YT|-|T|\le|XY|. \tag{7}
$$

联立 (6)--(7)，得到 F 型状态的必要条件

$$
\boxed{
|XT|+|YT|-|T|\le\frac{|\mathcal H|}{2}.} \tag{8}
$$

若乘积集无周期，即 (T=\{1\})，则化为

$$
\boxed{
|X|+|Y|\le\frac{|\mathcal H|}{2}+1.} \tag{9}
$$

更一般地，把 (X,Y) 投影到商群 (mathcal H/T)，记像为

$$
\overline X=XT/T,
\qquad
\overline Y=YT/T.
$$

由于 (|XT|=|T||\overline X|)、(|YT|=|T||\overline Y|)，(8) 等价于

$$
\boxed{
|\overline X|+|\overline Y|-1
\le\frac{|\mathcal H/T|}{2}.} \tag{10}
$$

因此每一个 F 型两块状态都必须在稳定子群商中满足半密度缺口；若 (T) 非平凡，
缺口被解释为周期结构，若 (T) 平凡，缺口只能来自两个块本身的稀疏除子谱。

## 证明

逐素数写

$$
\gamma=\prod_q q^{r_q},
\qquad
L=\prod_q q^{s_q},
\qquad
K=\prod_q q^{r_q+s_q}.
$$

若 (d\mid K)，令 (e_q=v_q(d))。对每个 (q) 取

$$
u_q=\max(0,e_q-s_q),
\qquad
v_q=e_q-u_q.
$$

则 (0\le u_q\le r_q)、(0\le v_q\le s_q)，故 (d=d_\gamma d_L) 其中

$$
d_\gamma=\prod_q q^{u_q}\mid\gamma,
\qquad
d_L=\prod_q q^{v_q}\mid L.
$$

这证明 (mathcal A_R(K)\subseteq XY)；反向包含由 (d_\gamma d_L\mid K) 立即成立，
故得 (4)。

由 (5) 和中心化谱的反足点刻画，(-1\notin\mathcal C_R(K)) 等价于

$$
\mathcal A_R(K)\cap(-\mathcal A_R(K))=\varnothing.
$$

因 (-1\in\mathcal H)，两集合 (XY) 与 (-XY) 都是 (mathcal H) 的等势子集，
从而得到 (6)。

对有限阿贝尔群 (mathcal H) 中的两个非空子集 (X,Y)，以乘积集 (XY) 的稳定子群
(T) 应用 Kneser 定理，得到 (7)。将其与 (6) 联立即得 (8)；再除以 (|T|) 得 (10)。
证毕。

## 对混合终端选择器的含义

若 (K=\gamma L) 来自线性源

$$
p=a+s+asR,
\qquad s\text{ 为奇数},
\qquad R\equiv3\pmod4, \tag{11}
$$

并且 (8) 或 (9) 的反向严格不等式成立，则 (-1\in\mathcal C_R(K))。于是存在
(d\mid K^2)、(d\le K)、(d\equiv-K\pmod R)，可恢复一般 (B) 的 Type I 正规形。
同一线性源同时给出

$$
E_0=sR+1,
\qquad
E_0\mid4K,
\qquad
E_0\equiv1\pmod R,
\qquad
2\mid E_0,
\qquad
E_0\le4K-2R, \tag{12}
$$

所以该命中正好落入目标混合终端选择器的偶因子分支。

这提供了一个比“单状态反足点半密度”更细的局部目标：先识别乘积集稳定子群 (T)，
再在 (mathcal H/T) 中证明两块投影违反 (10)。若 (T) 平凡，只需控制两个块的
除子残数大小；若 (T) 非平凡，则必须解释该周期如何由跨模数标签块的共享因子产生。
这正是[带标签块碰撞刚性](type-I-linear-labeled-block-gcd-rigidity.md)可以提供的输入。

## 边界

该结论是 F 型状态的必要条件和局部充分判据，不是全称选择器。它不处理
(-1\notin\mathcal H) 的 G 型状态，也不保证不同 (R) 的单位群有公共坐标；跨状态证明仍
需要二次互反拉回、二残数注入或其它可比的算术结构。此外，(8) 中的稳定子群 (T) 依赖
当前乘积集，不能预先替换为任意固定子群。

因此下一步最小的可证明问题是：对一个完整线性谱，证明每个 F 型状态要么满足 (9) 的
稀疏性界，要么其非平凡 (T) 必含某个可由标签差/模数差控制的因子；若两者均不成立，
则该状态立即给出一般 (B) 命中和偶终端桥。
