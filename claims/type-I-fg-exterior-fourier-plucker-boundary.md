---
kind: claim
claim_id: type-I-fg-exterior-fourier-plucker-boundary
title: F/G top-exterior 的秩重述 no-go 与目标依赖 Plücker 分离边界
statement: >-
  对 m 维有限域空间 Q 及任一完成像 S<=Q，top exterior 消失
  wedge^m S=0 当且仅当 dim S<m；因此广义 Rado 亏损给出的全部 top minors
  为零只重述秩失败，不记录精确亏格，也不自动产生算术标量角色。m>=2 时
  determinant 对完成元组的加法群不是同态；任何额外提供的 homomorphic
  exterior realization 再与线性泛函复合，只会退化为已有普通 Fourier 角色。
  另一方面，若可达完成均给出固定 s 维子空间 S_omega，而一个有算术来源的目标
  s-plane D 的 Plucker line 不在全部可达 Plucker lines 的线性包中，则存在 exterior
  functional 同时湮灭全部可达完成且在 D 上非零；该条件也是线性 exterior
  separator 存在的充要条件。F_2^4 的两菜单例严格表明这种目标依赖分离可在没有
  共同标量 annihilator 时成立，但缺少目标平面 provenance 或高阶相位的算术实现时，
  它仍不是 Type I/II 终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-generalized-rado-fixed-quotient-defect
  - type-I-fg-dependent-role-evaluation-rado-tensor-selector
  - type-I-fg-exterior-grassmann-slice-successor-descent
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - exterior-power
  - determinant
  - Plucker
  - Fourier
  - target-separation
  - no-go
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-fg-generalized-rado-fixed-quotient-defect
    role: fixed-quotient-top-exterior-input
  - claim: type-I-fg-dependent-role-evaluation-rado-tensor-selector
    role: ordinary-role-and-tensor-Fourier-boundary
  - claim: type-I-fg-exterior-grassmann-slice-successor-descent
    role: positive-grassmann-and-matrix-Fourier-successor-route
  - reproduction: reproductions/type_i_fg_exterior_grassmann_slice_successor_descent.py
    role: determinant-nonadditivity-and-strict-plucker-separation-controls
visibility: public
last_checked: '2026-08-10'
---

# F/G top-exterior 的秩重述 no-go 与目标依赖 Plücker 分离边界

## 1. top exterior 精确等于秩失败

设 \(Q\) 是 \(m\) 维 \(\mathbb F_q\) 空间，具体完成 \(\omega\) 的像张成

\[
S_\omega\le Q.
\tag{1}
\]

则

\[
\boxed{
\bigwedge^m S_\omega=0
\quad\Longleftrightarrow\quad
\dim S_\omega<m.}
\tag{2}
\]

等价地，任取 \(Q\) 的基，完成矩阵的全部 \(m\) 阶 minors 为零。证明是 exterior
power 的维数公式：

\[
\dim\bigwedge^m S_\omega
=
{\dim S_\omega\choose m}.
\tag{3}
\]

所以固定亏损商 \(Q_U\) 中的

\[
\bigwedge^{m_U}S_\omega=0,
\qquad
\bigwedge^{m_U}Q_U\ne0
\tag{4}
\]

没有比
\(\dim S_\omega<m_U\) 多出新信息。特别地，亏格一、二或更大在 top exterior
层都只得到同一个零；精确 \(\delta(U)\) 仍来自 rank/nullity 或 Grassmann
annihilator 维数。

更一般地，任何 alternating \(m\)-linear invariant
\(A:Q^m\to Y\) 都唯一因子化为

\[
Q^m
\xrightarrow{\ \wedge\ }
\bigwedge^m Q
\xrightarrow{\ \widetilde A\ }
Y.
\tag{5}
\]

因此它在所有 \(\dim S_\omega<m\) 的完成上必为零，不能在这些完成之间选择一个
不同的算术分支。

## 2. determinant 不是普通 Fourier 角色

当 \(m\ge2\) 时，把 determinant 看成完成元组加法群 \(Q^m\) 上的函数。取

\[
x=(e_1,\ldots,e_{m-1},0),
\qquad
y=(0,\ldots,0,e_m).
\tag{6}
\]

则

\[
\det x=0,\qquad
\det y=0,\qquad
\det(x+y)=1.
\tag{7}
\]

故

\[
\boxed{
\det:Q^m\to\mathbb F_q
\text{ 不是加法群同态}.}
\tag{8}
\]

于是 \(\psi(\det(\cdot))\) 是高阶多线性相位，不是现有 source group 上的普通
Fourier character。不能仅凭“determinant 是一个标量”就把 (4) 接到
annihilator relay。

若另外构造了一个真实群同态

\[
\Phi:H\longrightarrow\bigwedge^sQ
\tag{9}
\]

及线性泛函
\(\Lambda\in(\bigwedge^sQ)^*\)，那么

\[
\Lambda\circ\Phi:H\longrightarrow\mathbb F_q
\tag{10}
\]

恰是一个普通标量角色。它必须重新通过 source closure、target phase 和整数提升
门；不会绕过饱和分支共同标量 annihilator 为零的既有 no-go。由此得到严格二分：

\[
\boxed{
\begin{array}{ll}
\text{有 homomorphic exterior realization}
&\Longrightarrow\text{退回普通角色接口};\\
\text{没有该 realization}
&\Longrightarrow\text{只能记为高阶相位，不能调用普通 Fourier relay}.
\end{array}}
\tag{11}
\]

当 \(m=1\) 时 top exterior 本来就是 \(Q\)，同样只给普通线性角色，并无新的
determinantal 层。

## 3. “规范标量”不能修复同态缺口

\(\bigwedge^mQ\) 是一维空间，但一般没有从数据 \(Q\) 自身得到的规范
\(\bigwedge^mQ\simeq\mathbb F_q\) 平凡化。对 \(q>2\)，
\(\operatorname{diag}(a,1,\ldots,1)\in\operatorname{GL}(Q)\) 在 top exterior
上乘以任意 \(a\in\mathbb F_q^\times\)，所以不存在非零
\(\operatorname{GL}(Q)\)-不变向量或泛函。

在 \(q=2\) 时，一维空间确有唯一非零元素，因而这项坐标歧义消失；但 (7)--(8)
仍成立，而且所有亏损完成仍统一映到零。故二元域也没有因此获得 source-group
同态或目标相位。

## 4. 最小 quotient 反例

取

\[
Q=\mathbb F_2^2,
\qquad
B=\{e_1,e_2\},
\tag{12}
\]

并让一个补集请求从 \(B\) 中选一条列。每个完成的 span 都是一维，故其
top exterior 恒为零：

\[
\bigwedge^2\langle e_i\rangle=0.
\tag{13}
\]

但全部候选生成 \(Q\)，所以共同标量 annihilator 为

\[
\langle e_1,e_2\rangle^\perp=0.
\tag{14}
\]

这严格否定

\[
\text{“所有完成 top wedge 为零”}
\Longrightarrow
\text{“存在统一非零标量角色”}.
\tag{15}
\]

该例只在 quotient 层说明逻辑边界；带 \(n\ge k\)、全非零列与 source saturation
的 lifted 严格例见 fixed-quotient claim 的 \(\mathbb F_2^3\) 三请求系统。

## 5. 固定秩 Plücker 目标分离定理

top exterior 无效并不排除低阶、目标依赖的 exterior 证书。设所有可达完成
\(\omega\in\Omega\) 都给出固定 \(s\) 维子空间

\[
S_\omega\in\operatorname{Gr}_s(Q).
\tag{16}
\]

令其 reachable Plücker span 为

\[
\mathcal P_\Omega
=
\operatorname{span}
\{\bigwedge^sS_\omega:\omega\in\Omega\}
\le\bigwedge^sQ.
\tag{17}
\]

这里 \(\bigwedge^sS_\omega\) 是 \(\bigwedge^sQ\) 中的一维 Plücker line。
若算术目标给出另一个 \(s\) 维子空间 \(D\le Q\)，则下列条件等价：

\[
\boxed{
\begin{aligned}
&\bigwedge^sD\not\subseteq\mathcal P_\Omega;\\
&\exists\Lambda\in(\bigwedge^sQ)^*:
\ \Lambda(\bigwedge^sS_\omega)=0\ (\forall\omega),
\quad
\Lambda(\bigwedge^sD)\ne0.
\end{aligned}}
\tag{18}
\]

证明是有限维线性分离。若目标 Plücker line 不在
\(\mathcal P_\Omega\) 中，对 quotient
\(\bigwedge^sQ/\mathcal P_\Omega\) 中的非零目标像取非零线性泛函并拉回；
反向蕴含由线性性立即得到。

所以 (18) 是 linear exterior separator 存在的**充要条件**，而不是只给必要
rank test。本卡使用的是“每个 \(S_\omega\) 的 top Plücker line”版本，因此可达
空间维数变化时须先按秩分层。另一种合法推广是预先固定 exterior degree \(j\)，
把各 \(\bigwedge^jS_\omega\le\bigwedge^jQ\) 作为可能高维的子空间统一处理；
那是不同于本卡 (18) 的命题。

## 6. 没有共同标量角色但有 Plücker separator 的严格例

取

\[
Q=\mathbb F_2^4
=\langle e_1,e_2,e_3,e_4\rangle,
\tag{19}
\]

两个菜单

\[
B_1=\{e_1\},
\qquad
B_2=\{e_2,e_3,e_4\}.
\tag{20}
\]

可达平面为

\[
S_i=\langle e_1,e_i\rangle
\qquad(i=2,3,4),
\tag{21}
\]

而全部菜单候选生成 \(Q\)，故共同标量 annihilator 为零。它们的 Plücker span
却只有

\[
\mathcal P_\Omega
=
\langle
e_1\wedge e_2,\,
e_1\wedge e_3,\,
e_1\wedge e_4
\rangle.
\tag{22}
\]

取目标平面

\[
D=\langle e_3,e_4\rangle.
\tag{23}
\]

则
\(e_3\wedge e_4\notin\mathcal P_\Omega\)，且

\[
\Lambda=e_3^*\wedge e_4^*
\tag{24}
\]

在 (22) 上全为零、在目标上为一。这严格证明低阶 target-dependent Plücker
分离可以强于共同标量 annihilator。

## 7. 算术准入门

式 (18) 仍只是一张有限线性证书。要成为 Type I/II 终端，至少还须证明：

1. \(D\) 由真实 prescribed target fiber、目标近邻或广义 \(2^j\) 正规形规范产生，
   不是事后挑选的任意平面；
2. 每个 \(S_\omega\) 来自通过物理耦合与 source provenance 的实际完成；
3. \(\Lambda\) 要么通过类似 (9) 的 source homomorphism 实现并回到普通角色门，
   要么进入一个已证明可消费高阶相位的 Type I/II determinantal identity；
4. 后续仍保存 source labels、SNF/CRT、范围、\(B'>A\)、marked E4 和不可重置 E5。

缺少第 1 项时，输出 `PLUCKER_TARGET_PROVENANCE_UNPROVED`；缺少第 3 项时，
输出 `HIGHER_ORDER_PHASE_NOT_FOURIER_ROLE`，不能把 linear separator
写成算术终端。

## 8. 统一分派与研究边界

~~~text
GENERALIZED_RADO_FIXED_QUOTIENT_DEFECT
  bare top wedge only:
    EXTERIOR_RANK_RESTATEMENT_NO_ARITHMETIC_GAIN
  fixed-rank reachable subspaces + prescribed target plane:
    target Plucker line in reachable span:
      PLUCKER_TARGET_NOT_SEPARATED
    target Plucker line outside reachable span:
      PLUCKER_TARGET_SEPARATION
      arithmetic target provenance absent:
        PLUCKER_TARGET_PROVENANCE_UNPROVED
      source homomorphic realization present:
        reduce to ordinary Fourier role gates
      proven higher-order Type I/II identity present:
        DETERMINANTAL_ARITHMETIC_TERMINAL
      neither present:
        HIGHER_ORDER_PHASE_NOT_FOURIER_ROLE
  selected-source overhead h < delta:
    use GRASSMANN_SLICE_CAPACITY_CERT
~~~

本卡关闭了“直接消费 \(\bigwedge^{m_U}Q_U\) 就能得到算术终端”的裸路线：
top wedge 只重述 rank deficit。保留下来的 exterior 方向必须同时带有低阶固定秩、
specified target 与 arithmetic provenance。与之互补的正向路线是 Grassmann
kernel slice：它不把 determinant 冒充 source character，而是直接选择一个实际
角色子空间，并以 \(\delta-\dim X\) 支付后继收缩。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_exterior_grassmann_slice_successor_descent.py --verify
~~~

其中 exterior 子检查验证 determinant 非加性、\(\mathbb F_2^4\) reachable
Plücker span 的秩三以及加入目标 \(e_3\wedge e_4\) 后秩严格增至四；不运行
历史测试。
