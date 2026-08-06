---
kind: claim
claim_id: type-I-g-anchor-raw-fixed-chart-factor-projection
title: G-anchor Jacobi-odd raw 终点到固定图表因子表的投影、相位擦除与带标记嵌入
statement: 对核心素数 p，令 R=p-2、K=(p-1)^2/4、Q=(p-3)/2，并取 Jacobi-odd raw 标签 delta|Q。若 X_delta=2Q/delta、Y_delta=R-X_delta、c_delta=gcd(Y_delta,K)、M_delta=K/c_delta，则 M_delta 属于固定图表的完整 determinant 表 W_det(p,R)，并给出 pn_delta=4M_delta(p-c_delta)+1。写 Y_delta=c_delta t_delta 时，gcd(t_delta,M_delta)=1 且 chi_R(t_delta)=-1；只投影到 K-support 会擦除 raw 负相位。反之，保留精确 t_delta 或其 U(R) 剩余类，则 delta -> (M_delta,t_delta) 是 D_p^- 到一个显式有限带标记 determinant 行像的双射，并满足 M_delta t_delta^{-1}=K delta (mod R)。这只完整覆盖 raw 菜单，不覆盖整个 determinant 表、F/G source universe 或 E1--E5 转移。更强地，delta、Q、Q/delta、X_delta、Y_delta 与 X_delta Y_delta 都不能直接作为有效 M 列。full-Q 标签显式给 c_Q=3 或 9，故产生一个规范的真实 determinant 行。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-fixed-chart-determinant-factor-table
  - type-I-fg-physical-carry-arc-lift-interface
topics:
  - type-I
  - G-anchor
  - raw-path
  - Jacobi-symbol
  - fixed-chart
  - determinant
  - factor-projection
  - phase-erasure
  - marked-embedding
  - finite-abelian
  - Fourier
  - source-map
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: raw-Jacobi-odd-path-menu
  - claim: type-I-fixed-chart-determinant-factor-table
    role: complete-physical-determinant-table
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: physical-row-interface
visibility: public
last_checked: '2026-08-06'
---

# G-anchor Jacobi-odd raw 终点到固定图表因子表的投影、相位擦除与带标记嵌入

## 1. 输入与投影

固定核心素数 \(p\equiv1\pmod {24}\)，并写

\[
L=\frac{p-1}{2}=Q+1,
\qquad
R=p-2=2L-1,
\qquad
K=L^2.
\tag{1}
\]

取现有 G-anchor raw 菜单中的一个 Jacobi-odd 标签

\[
\delta\in\mathcal D_p^-,
\qquad
\delta\mid Q,
\qquad
\chi_R(\delta)=-1.
\tag{2}
\]

为避免与后面的 determinant 参数混淆，\(\delta\) 始终表示 raw 标签。令

\[
X_\delta=\frac{2Q}{\delta},
\qquad
Y_\delta=R-X_\delta,
\qquad
c_\delta=(Y_\delta,K),
\qquad
M_\delta=\frac K{c_\delta}.
\tag{3}
\]

原始 raw 路径给出

\[
0<Y_\delta<R,
\qquad
\chi_R(X_\delta)=1,
\qquad
\chi_R(Y_\delta)=-1.
\tag{4}
\]

**定理。** \(M_\delta\) 属于固定图表 \((p,R,K)\) 的完整 determinant 表。具体地，令

\[
C_{\rm det}=c_\delta,
\qquad
d_{\rm det}=p-c_\delta,
\qquad
n_\delta=4M_\delta-R,
\tag{5}
\]

则

\[
pn_\delta=4M_\delta d_{\rm det}+1.
\tag{6}
\]

**证明。** \(c_\delta\mid K\) 且 \(c_\delta\le Y_\delta<R<p\)。又令
\(Y_\delta=c_\delta t_\delta\)。由于 \(c_\delta\) 取尽 \(Y_\delta\) 与 \(K\) 的公共
素数赋值，有

\[
(t_\delta,M_\delta)=1.
\tag{7}
\]

所有 \(K\) 的素因子在 \(\chi_R\) 下都为 \(+1\)，所以

\[
\chi_R(c_\delta)=1,
\qquad
\chi_R(t_\delta)=-1.
\tag{8}
\]

\(Y_\delta,c_\delta,t_\delta\) 都是奇数；又 \(R\equiv11\pmod {12}\)，故
\(\chi_R(3)=1\)。于是 \(t_\delta\ne1,3\)，从而 \(t_\delta\ge5\)。因此

\[
c_\delta=\frac{Y_\delta}{t_\delta}<\frac R5,
\qquad
M_\delta>\frac{5K}{R}
=\frac54\left(p+\frac1{p-2}\right)>\frac{5p}{4}.
\tag{9}
\]

特别地 \(4M_\delta>R\)，故 \(M_\delta\in\mathcal W^{\rm det}_{p,R}\)。固定图表
因子表定理现在给出 (5)--(6)。证毕。

## 2. 相位擦除是严格的，而非缺少技巧

式 (8) 表明 raw 终点的 Jacobi 负相位完全留在被投影掉的尾因子
\(t_\delta=Y_\delta/c_\delta\) 中；而 \(M_\delta\mid K\) 的所有素因子都带正相位。
因此 (3) 是一个真实的 integer projection，却不是保留 raw 标记的 source-lift。

更直接地，有

\[
(\delta,K)=\left(Q,K\right)=\left(\frac Q\delta,K\right)=1,
\qquad
(X_\delta,K)=2.
\tag{10}
\]

所以 \(\delta,Q,Q/\delta\) 都不能直接作为非平凡 \(M\mid K\)。唯一的平凡商
\(Q/\delta=1\) 出现在 \(\delta=Q\)，但核心域 \(p\ge73\) 时仍有
\(4(Q/\delta)=4<R\)，故它也不是有效表行。若 \(X_\delta\mid K\)，则 (10) 强制
\(\delta=Q\)、\(X_\delta=2\)，但 \(4X_\delta=8<R\)，仍不是有效表行。另一方面，\(Y_\delta\) 及
\(X_\delta Y_\delta\) 的 Jacobi 值都为 \(-1\)，而 \(K\) 的任何因子都带 \(+1\)，
故它们也不能直接作为 \(M\)-列。

本卡展示的 raw 路径到物理 determinant 表的 adapter 包含 \(K\)-support 投影；若要在未来
恢复 marked lift，必须至少说明如何把 \(t_\delta\) 或等价的负相位数据作为额外行标签保存，
并另行证明 transition 与解提升。

## 3. full-\(Q\) 的规范行

取 \(\delta=Q\)，则

\[
X_Q=2,
\qquad
Y_Q=p-4.
\tag{11}
\]

若 \(p=24h+1\)，则

\[
c_Q=(p-4,K)
=3(8h-1,48h^2)
=3(8h-1,48)
=\begin{cases}
3,&h\not\equiv2\pmod3,\\
9,&h\equiv2\pmod3,
\end{cases}
\tag{12}
\]

从而 (3) 给出规范物理行

\[
(M_Q,C_{\rm det})=
\begin{cases}
(48h^2,3),&h\not\equiv2\pmod3,\\
(16h^2,9),&h\equiv2\pmod3.
\end{cases}
\tag{13}
\]

例如 \(p=73\) 时 \(h=3,Q=35\)，有

\[
Y_Q=69=3\cdot23,
\qquad
(M_Q,C_{\rm det})=(432,3).
\tag{14}
\]

而 \(p=193\) 时 \(h=8,Q=95\)，有

\[
Y_Q=189=9\cdot21,
\qquad
(M_Q,C_{\rm det})=(1024,9).
\tag{15}
\]

同一 \(p=73\) 中，\(\delta=7\) 与 \(\delta=35\) 都是 Jacobi-odd 标签，却分别得到
\(c_\delta=1,3\)。所以单一 Fourier/Jacobi 符号也不能恢复这张物理表。

## 4. 保留单位尾的无损带标记编码

上节的相位擦除只发生在忘掉 \(t_\delta\) 时。实际上，保留这个**精确整数尾**，可对
原始有限菜单给出一个无损的、但严格受限的带标记编码。

定义

\[
\widetilde{\mathcal W}_p^-=
\left\{
(M,t):
\begin{array}{l}
M\in\mathcal W^{\rm det}_{p,R},\quad c=K/M,\quad 0<ct<R,\quad(t,M)=1,\\
R-ct=2a,\quad a\mid Q,\quad\chi_R(Q/a)=-1
\end{array}
\right\}.
\tag{16}
\]

这里所有变量均取正整数；此定义不把 \(\mathcal D_p^-\) 作为像集的循环定义。令

\[
\iota_p:\mathcal D_p^-\longrightarrow\widetilde{\mathcal W}_p^-,
\qquad
\delta\longmapsto(M_\delta,t_\delta),
\qquad
t_\delta=\frac{Y_\delta}{c_\delta}.
\tag{17}
\]

**定理（lossless marked-row embedding）。** 映射 \(\iota_p\) 是双射。并且对每个
\(\delta\in\mathcal D_p^-\)，\(\delta,c_\delta,t_\delta,M_\delta\) 都是
\(U(R)\) 的单位，且

\[
\boxed{
M_\delta t_\delta^{-1}\equiv K\delta\pmod R.
}
\tag{18}
\]

因此，若只记录 \(M_\delta\bmod R\) 和
\(t_\delta\bmod R\)，原始标签仍由

\[
\delta\equiv K^{-1}M_\delta t_\delta^{-1}\pmod R,
\qquad 1\le\delta\le Q<R
\tag{19}
\]

唯一恢复。仅记录固定的 Jacobi 符号 \(\chi_R(t_\delta)=-1\) 显然不足；若以较粗的
Fourier 标签取代 \(t_\delta\bmod R\)，则必须另行证明该标签与 \(M_\delta\bmod R\)
在这个像上仍是单射，才可用于反演。

**证明。** 由 \(\delta X_\delta=2Q=R-1\) 和
\(Y_\delta=c_\delta t_\delta=R-X_\delta\)，有精确恒等式

\[
\delta(R-c_\delta t_\delta)=R-1,
\qquad
\delta c_\delta t_\delta=1+R(\delta-1).
\tag{20}
\]

故 \(\delta,c_\delta,t_\delta\in U(R)\)。又
\((K,R)=(L^2,2L-1)=1\)，所以 \(M_\delta=K/c_\delta\in U(R)\)。
从 (20) 得 \(t_\delta^{-1}\equiv\delta c_\delta\pmod R\)，乘以
\(M_\delta=K/c_\delta\) 即得 (18)。又
\(R-c_\delta t_\delta=X_\delta=2(Q/\delta)\)，故令
\(a=Q/\delta\) 即验证 (16) 的其余条件；所以
\(\iota_p(\delta)\) 确实落在 (16)。

反过来，取 \((M,t)\in\widetilde{\mathcal W}_p^-\)，令

\[
\delta=\frac Qa=\frac{2Q}{R-ct}.
\tag{21}
\]

则 \(\delta\mid Q\) 且 \(\chi_R(\delta)=-1\)，故 \(\delta\in\mathcal D_p^-\)。此外

\[
(ct,K)=(ct,cM)=c(t,M)=c,
\tag{22}
\]

所以从此 \(\delta\) 重建的 \(Y_\delta=ct\) 满足
\(c_\delta=(Y_\delta,K)=c\)，从而恢复同一 \(M,t\)。故 (17) 为双射。
最后 (19) 来自 (18)；其唯一性使用 \(1\le\delta\le Q<R\)。证毕。

对任意 \(\psi\in\widehat{U(R)}\)，(18) 还给出规范的有限 Abelian/Fourier 关系

\[
\psi(M_\delta)\psi(t_\delta)^{-1}
=\psi(K)\psi(\delta).
\tag{23}
\]

因此 \(\widetilde{\mathcal W}_p^-\) 是与 raw 菜单等势的带标记有限表，且
\(|\widetilde{\mathcal W}_p^-|=\tau(Q)/2\)。例如在 \(p=73\) 的 G-anchor 图表中，
\(R=71,K=1296,Q=35\)，有

\[
\delta=7\longmapsto(1296,61),
\qquad
\delta=35\longmapsto(432,23).
\tag{24}
\]

这并不是整个 determinant 表：同一图表中 \(M=144,c=9,n=505\) 也是一条合法行，
却不在 (24) 的像中。

## 5. 固定 \(p-2\) 缺口的 Type I/II 双重空性

这个固定图表的自然缺口是

\[
m=R=p-2,
\qquad
x=\frac{p+m}{4}=\frac{p-1}{2}=L,
\qquad
x^2=K.
\tag{25}
\]

**命题。** 在缺口 \(m=p-2\) 上不存在 Type I 或 Type II 除子证书。

**证明。** Type I 除子证书须有 \(e\mid x^2=K\) 及
\(e\equiv-px\pmod R\)。但

\[
px=(R+2)\frac{R+1}{2}\equiv1\pmod R,
\tag{26}
\]

故它要求 \(e\equiv-1\pmod R\)。Type II 证书则须有 \(e\mid K\)、
\(e\le x\) 及 \(e\equiv-x\pmod R\)，即

\[
e\equiv-\frac{R+1}{2}=Q\pmod R.
\tag{27}
\]

然而每个 \(e\mid K\) 都满足 \(\chi_R(e)=1\)，而
\(\chi_R(-1)=\chi_R(Q)=-1\)。两种同余皆不可能。证毕。

这比“中心 Type I 纤维为空”更具体：本卡构造的 \(M_\delta,c_\delta\) 都虽为
\(K\) 的因子，却不能是这一固定缺口的 Type I/II 证书除子；负相位尾
\(t_\delta\) 则不在 \(K\)-support 内。又由 (9)，其 determinant 行满足

\[
n_\delta=4M_\delta-R>4p+2,
\qquad n_\delta\ge4p+3.
\tag{28}
\]

所以它也不是要求 \(0<n<p\) 的小实例桥。

## 6. 边界

本卡没有构造 raw path 到 determinant 行的物理 action-preserving map，更没有证明
F/G source completeness、E1--E5、terminal 或严格递降。第 4 节的双射至多允许把
raw peeling 的组合关系**形式共轭**到带标记像上；这仍只是标签重命名，并未给出
determinant 行之间的实际 transition、certificate fiber 的 lift 或任何可支付容量。

因此，本卡给出的是一个可复算的算术投影及其 raw-menu 范围内的无损标记恢复：若只保留
\(M_\delta/K\)-support 数据而不携带精确负尾 \(t_\delta\)，原始 Jacobi 标签必被擦除；
若保留该尾，则可恢复标签，但该标签本身不会自动成为 \(K\)-support、Type I/II 短证书
或严格递降资源。
