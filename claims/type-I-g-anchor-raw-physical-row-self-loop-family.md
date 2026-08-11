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

## 尾标记诱导的 AC 移位也不自动关闭

上述自环族有一个看似自然的 Type II 尝试。对 raw 边的起点 (e=Q/13)，令

\[
t=t_e=\frac{p-28}{3},
\qquad
s=t-7=\frac{p-49}{3}.
\tag{18}
\]

于是恒有

\[
p+4s=7t.
\tag{19}
\]

所以 (t) 和 (7t) 都是同一移位整数的因子。可是它们不因而成为 AC 射线的 target
因子。更一般地，设 (s=a^2c) 为**任意**正整数分解；不要求它是平方自由规范分解。

* 若 (t=s+7\equiv-1\pmod {4ac})，则 (4ac\mid s+8)。两边乘以 (4) 得

  \[
  4ac\mid4s+32=a(4ac)+32,
  \]

  故 (4ac\mid32)。于是 (ac\le8)，并且

  \[
  s=a(ac)\le(ac)^2\le64.\tag{20}
  \]

* 若 (7t=7s+49\equiv-1\pmod {4ac})，则 (4ac\mid7s+50)。同样乘以 (4) 得

  \[
  4ac\mid28s+200=7a(4ac)+200,
  \]

  故 (4ac\mid200)。于是 (ac\le50)，并且

  \[
  s=a(ac)\le(ac)^2\le2500.\tag{21}
  \]

因此对本族全部 (p\ge601)，(s>64)，裸因子 (t) 不可能满足任何 AC 射线的目标同余；
对 (p>7549)，又有 (s>2500)，裸因子 (7t) 也不可能满足该同余。由于 (1) 中有无穷多
素数，后一个双重排除也发生无穷多次。

这里仅排除了从 (19) 中直接取 (h=t) 或 (h=7t) 的做法；它不排除 (7t) 的其它因子、
其它移位、或一个完全不同的带标记 source-switch。

## 定向复核

```bash
PYTHONPATH=reproductions python3 reproductions/type_i_g_anchor_raw_physical_row_self_loop_family.py --verify
```
