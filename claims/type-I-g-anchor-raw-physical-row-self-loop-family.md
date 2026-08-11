---
kind: claim
claim_id: type-I-g-anchor-raw-physical-row-self-loop-family
title: G-anchor 原始边在未标记物理 determinant 行上的无穷自环族
statement: 对每个素数 p=601 (mod 936)，令 R=p-2、K=(p-1)^2/4、Q=(p-3)/2、e=Q/13。则 e 和 Q 都属于 G-anchor 的 Jacobi-negative raw 菜单，并有一条实际 raw 边 e -> Q。两端的完整物理 determinant 行完全相同：c_e=c_Q=3、M_e=M_Q=K/3、d_e=d_Q=p-3、n_e=n_Q=4K/3-R；但精确尾标记分别为 t_e=(p-28)/3 和 t_Q=(p-4)/3，彼此不同。Dirichlet 定理保证这给出无穷多个核心素数。因此，任何把 G-anchor raw 状态压缩为 (p,R,K,M,c,d,n) 的适配器都含非平凡自环；仅依赖这些未标记物理字段的势不可能沿全部实际 raw 边严格下降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-raw-fixed-chart-factor-projection
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-fixed-chart-determinant-factor-table
topics:
  - type-I
  - G-state
  - G-anchor
  - raw-path
  - determinant
  - marked-state
  - self-loop
  - no-go
  - well-founded-potential
  - proof-program
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: universal-Jacobi-negative-raw-menu
  - claim: type-I-g-anchor-raw-fixed-chart-factor-projection
    role: marked-raw-to-determinant-row-map
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: actual-raw-edge-and-marked-tail-interface
  - reproduction: reproductions/type_i_g_anchor_raw_physical_row_self_loop_family.py
    role: exact-family-identity-check
visibility: public
last_checked: '2026-08-12'
---

# G-anchor 原始边在未标记物理 determinant 行上的无穷自环族

## 定理

设

\[
p\equiv601\pmod {936}
\tag{1}
\]

为素数。这个同余类与 \(936\) 互素，故由 Dirichlet 定理含无穷多个素数。它们全都满足
\(p\equiv1\pmod {24}\)，因而属于核心域。

令

\[
R=p-2,\qquad K=\frac{(p-1)^2}{4},\qquad Q=\frac{p-3}{2},
\qquad e=\frac Q{13}.
\tag{2}
\]

则 \(e,Q\) 都在 G-anchor 的 Jacobi-negative raw 菜单中，且存在实际 raw 边

\[
e\xrightarrow{\ 13\ }Q.\tag{3}
\]

把 raw 标签 \(\delta\) 投影为

\[
X_\delta=\frac{2Q}{\delta},\qquad
Y_\delta=R-X_\delta,\qquad
c_\delta=(Y_\delta,K),\qquad
M_\delta=\frac K{c_\delta},\qquad
t_\delta=\frac{Y_\delta}{c_\delta}.
\tag{4}
\]

则 (3) 的两端满足

\[
\begin{array}{c|ccccc}
\delta&Y_\delta&c_\delta&M_\delta&t_\delta&\text{raw label}\\ \hline
e&(p-28)&3&K/3&(p-28)/3&Q/13\\
Q&(p-4)&3&K/3&(p-4)/3&Q
\end{array}
\tag{5}
\]

所以它们的完整固定图表 determinant 行也完全一致：

\[
(M,c,d,n)=
\left(\frac K3,3,p-3,\frac{4K}{3}-R\right),
\qquad pn=4M d+1.
\tag{6}
\]

然而 \(t_Q-t_e=8\)，且 (e\ne Q)。故这是实际 raw 图中的非平凡边，而不是同一标记的重复编码。

## 证明

将 (p=24h+1)。由 (1) 得

\[
h\equiv25\pmod {39},
\tag{7}
\]

特别地 (3\nmid h)。又 (p\equiv3\pmod {13})，故 (13\mid Q)。

G-anchor 的一般 Jacobi 恒等式给出

\[
\chi_R(Q)=-1.
\tag{8}
\]

另一方面 (R=p-2\equiv1\pmod {13})，且 (13\equiv1\pmod4)。Jacobi 二次互反律因而给出

\[
\chi_R(13)=\left(\frac{13}{R}\right)
=\left(\frac R{13}\right)=1.
\tag{9}
\]

于是

\[
\chi_R(e)=\chi_R(Q)\chi_R(13)^{-1}=-1.
\tag{10}
\]

所以 (e,Q\in\mathcal D_p^-\)。按 G-anchor raw-peeling 的实际边规则，因 (Q=13e)
且 (13) 是正 Jacobi 相位的素因子，得到 (3)。

现在 (K=(12h)^2)，并且

\[
Y_Q=R-2=p-4=24h-3,
\qquad
Y_e=R-26=p-28=24h-27.
\tag{11}
\]

先看 (Y_Q)。有

\[
(24h-3,12h)=3.
\tag{12}
\]

且 (3\nmid h) 时 (v_3(24h-3)=1)。任何与 \(K=(12h)^2) 的公素因子也已整除
\(12h)，故

\[
c_Q=(Y_Q,K)=3.
\tag{13}
\]

同理

\[
(24h-27,12h)=(27,12h)=3,
\tag{14}
\]

并且 (v_3(24h-27)=1)，故

\[
c_e=(Y_e,K)=3.
\tag{15}
\]

将 (11)、(13)、(15) 代入 (4)，即得 (5)。固定图表 determinant 投影以

\[
d=p-c,\qquad n=4M-R
\tag{16}
\]

定义其物理行，故 (6) 成立。最后 (t_Q-t_e=8)，所以这一边在保留精确尾时仍非平凡。
证毕。

## 对全局出口的约束

这不是 Erdős--Straus 猜想的反例，也不排除利用带标记 raw 状态、AC/Type II 证书、
跨图表重图表或较小分母递降来关闭该族。它只证明一个必要的状态设计条件：

\[
\boxed{
\text{若 G 的 raw 边仍属于递降主链，状态必须保留 }t
\text{ 或等价的可区分标签；}
}
\]

\[
\boxed{
\text{任何只以 }(p,R,K,M,c,d,n)\text{ 为状态的 raw 递降势都不可能全局严格。}
}
\tag{17}
\]

因此，下一条正向 G/Type I 出口不能把 raw 图先压成未标记 determinant 行再寻求势下降；
它必须在标记层构造 terminal、可提升 source-switch，或将精确尾映射到一个独立的短证书/严格分母下降。

## 定向复核

```bash
PYTHONPATH=reproductions python3 reproductions/type_i_g_anchor_raw_physical_row_self_loop_family.py --verify
```
