---
kind: claim
claim_id: type-I-g-anchor-marked-raw-peeling-calculus
title: G-anchor 带精确尾标记的 raw-peeling calculus 与物理行边界
statement: 对 G-anchor 的带标记嵌入 delta -> (M_delta,t_delta)，若 delta=q e，则反向去皮 delta->e 在 (M,t) 上有显式公式，并使 Fourier 坐标 M t^{-1} 乘以 q^{-1}。相邻行的精确 gcd/lcm 恒等式为 gcd(c_delta,c_e)=gcd(c_delta,q-1) 及 lcm(M_delta,M_e)=K/gcd(c_delta,q-1)，后者仍是一条固定图表 determinant 行。可是 M-only 乃至 (M,q) 不能决定去皮后继，且存在真实 nontrivial raw 边使整个 physical determinant 行不变，故未标记物理表不能携带 raw 动作或严格 E5。扩展到全部 primitive m=1 raw bottom node 后，(M,t) 与该 raw 图严格双射并共轭其全部 m=1 边；这仍是 raw action，不是 certificate-fiber lift 或 E1--E5 转移。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-raw-fixed-chart-factor-projection
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-fixed-chart-determinant-factor-table
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - raw-path
  - raw-peeling
  - marked-embedding
  - determinant
  - lcm
  - Fourier
  - E5
  - no-go
  - proof-boundary
sources:
  - claim: type-I-g-anchor-raw-fixed-chart-factor-projection
    role: lossless-marked-row-embedding
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: actual-raw-peeling-menu
  - claim: type-I-fixed-chart-determinant-factor-table
    role: physical-determinant-row-table
  - concept: denominator-escape-state-contract
    role: action-versus-E1-E5-boundary
visibility: public
last_checked: '2026-08-06'
---

# G-anchor 带精确尾标记的 raw-peeling calculus 与物理行边界

## 1. 反向去皮的精确作用

固定

\[
p\equiv1\pmod {24},
\qquad
R=p-2,
\qquad
K=\frac{(p-1)^2}{4},
\qquad
Q=\frac{p-3}{2}.
\tag{1}
\]

对 \(\delta\in\mathcal D_p^-\)，沿用带标记行

\[
X_\delta=\frac{2Q}{\delta},
\qquad
Y_\delta=R-X_\delta=c_\delta t_\delta,
\qquad
c_\delta=(Y_\delta,K),
\qquad
M_\delta=K/c_\delta.
\tag{2}
\]

设 \(\delta=qe\)，其中 \(q\) 为素数。把标签从 \(\delta\) 去回 \(e=\delta/q\)
（这与实际 raw 边方向相反）时，有

\[
X_e=qX_\delta,
\qquad
Y_e=qY_\delta-(q-1)R,
\tag{3}
\]

从而

\[
c_e=(qc_\delta t_\delta-(q-1)R,K),
\qquad
M_e=K/c_e,
\qquad
t_e=Y_e/c_e.
\tag{4}
\]

所以 \((M,t)\) 上存在一个完全显式的部分动作，而不只是“存在某个标记”。由
\(M_\delta t_\delta^{-1}\equiv K\delta\pmod R\)，有

\[
M_et_e^{-1}\equiv q^{-1}M_\delta t_\delta^{-1}\pmod R.
\tag{5}
\]

因而每个 \(\psi\in\widehat{U(R)}\) 满足

\[
\psi(M_e)\psi(t_e)^{-1}
=\psi(q)^{-1}\psi(M_\delta)\psi(t_\delta)^{-1}.
\tag{6}
\]

若还要求 \(e\in\mathcal D_p^-\)，则由
\(\chi_R(\delta)=\chi_R(q)\chi_R(e)=-1\) 得到精确条件

\[
e\in\mathcal D_p^-
\Longleftrightarrow
\chi_R(q)=1.
\tag{7}
\]

实际 raw 边方向是 \(e\to\delta=qe\)。所以 \(\delta\to\delta/q\) 的下降只是一条
反向标签秩，不能直接作为递归合同的 E5 势。

## 2. 相邻行的因子 join 恒等式

**定理。** 在 (3)--(4) 的条件下，

\[
\boxed{
(c_\delta,c_e)=(c_\delta,q-1)
}
\tag{8}
\]

并且

\[
\boxed{
\operatorname{lcm}(M_\delta,M_e)
=\frac K{(c_\delta,q-1)}.
}
\tag{9}
\]

右端仍属于 \(\mathcal W^{\rm det}_{p,R}\)，故是一条同固定图表的真实 determinant 行。

**证明。** 因 \(c_\delta\mid K\)，有

\[
(c_\delta,c_e)=(c_\delta,Y_e)
=(c_\delta,-(q-1)R)=(c_\delta,q-1),
\tag{10}
\]

其中最后一步使用 \((K,R)=1\)。对 \(K\) 的两个除子 \(K/c_\delta,K/c_e\)，
取 lcm 即得 (9)。又它至少不小于 \(M_\delta>5p/4\)，其余因子
\((c_\delta,q-1)\le c_\delta<R<p\)，故固定图表因子表条件成立。证毕。

式 (9) 是一个精确的 raw-adjacent capacity 上包络；但它没有保留哪一个标签、
更没有给出解纤维 lift 或合法转移。

## 3. 未标记 physical row 不足以确定 raw 动作

首先，\(M\) 甚至连同剥离素数 \(q\) 也不足以决定后继。对

\[
p=5281,
\qquad q=29,
\qquad
\delta=203,2639,
\tag{11}
\]

两个带标记行都有

\[
(c_\delta,M_\delta)=(3,2323200).
\tag{12}
\]

但反向去皮分别到 \(e=7,91\)，并给出

\[
(c_7,M_7)=(25,278784),
\qquad
(c_{91},M_{91})=(1,6969600).
\tag{13}
\]

故精确尾 \(t\) 是必要标签，不能把 (3) 降为未标记 determinant-row 规则。

更强地，非平凡 raw 边也可能完全不改变 physical determinant 行。取

\[
p=601,
\qquad R=599,
\qquad Q=299=13\cdot23,
\qquad K=90000.
\tag{14}
\]

这里 \(\chi_{599}(13)=1\)、\(\chi_{599}(23)=-1\)，所以实际 raw 边

\[
23\xrightarrow{\ q=13\ }299
\tag{15}
\]

在带标记表中是

\[
(M,t):(30000,191)\longmapsto(30000,199).
\tag{16}
\]

两端的未标记 physical determinant 行完全相同：

\[
(M,c,d,n)=(30000,3,598,119401),
\qquad
601\cdot119401=4\cdot30000\cdot598+1.
\tag{17}
\]

因此任何只依赖 \((p,R,K,M,c,d,n)\) 的严格势，在这条真实 raw 边上必为自环。

## 4. 完整 \(m=1\) raw 表的无损 adapter

原始 \(\mathcal D_p^-\) 只是一张特定负相位子菜单，不对所有 raw 出边封闭。可以把
所有 primitive \(m=1\) bottom node 一并编码：将唯一偶坐标记为 \(x\)，另一个坐标为
\(y=R-x\)，并置

\[
c=(y,K),
\qquad M=K/c,
\qquad t=y/c.
\tag{18}
\]

这给出与下列显式集合的双射：

\[
\left\{(M,t)\in\mathbb N^2:
\begin{array}{l}
M\mid K,\quad c=K/M,\quad 0<ct<R,\quad ct\text{ 为奇数},\\
(t,M)=1,\quad(R-ct,R)=1
\end{array}
\right\}.
\tag{19}
\]

逆映射为 \(x=R-(K/M)t\)。因为 \(ct<R\)，有
\(M=K/c>K/R>p/4\)，所以每个像均属于
\(\mathcal W^{\rm det}_{p,R}\)。在这张扩展的带标记表上，所有 \(m=1\) raw 边
（每步后重新选择偶侧）都只是 (18) 下的精确共轭。

这仍只是完整 raw 图的 action；它没有制造 certificate fiber、全域解提升或 E1--E5。
例如 (14) 中从 \(\delta=23\) 的另一侧还可剥离 \(191\)，到达 \(\{3,596\}\) 并编码为
\((M,t)=(30000,1)\)。这个行不来自任何 \(\delta\mid Q\) 的负菜单，明确说明
\(\mathcal D_p^-\) 像本身不对完整 raw 动作闭合。
