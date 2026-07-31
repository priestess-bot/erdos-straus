---
kind: claim
claim_id: type-I-universal-cycle-complement-flip-segment-normal-form
title: 通用一层周期的偶补数分段与两翻转正规形
statement: 对奇数 R 的通用图 U_R 有向周期，逐边 q_i^2 整除所选坐标使取补数恰等价于所选坐标奇偶翻转。因此补数翻转数为正偶数、prod q_i=1(mod R)，且周期长度至少为 3。按翻转分段后，每段起点 A_j、标号积 Q_j 与下一段起点 A_(j+1) 满足 A_j=Q_j(R-A_(j+1)) 及 rad(Q_j)|(R-A_(j+1))。恰有两次翻转时存在 h=(QT-1)/R，使两个段首及其补数具有显式闭式，并有 rad(Q)|(T-1)/h、rad(T)|(Q-1)/h、gcd(Q,T)=1。该结构把三目标乘子桥化为完整同余关系格三个陪集的 l_infinity 短代表问题，并给出周期生成子格内的充分条件，但本身不保证命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-core-formal-cycle-radical-cube-boundary
  - type-I-formal-external-cycle-product-law-boundary
  - type-I-formal-cycle-radical-multiplier-bridge
topics:
  - type-I
  - universal-cycle
  - complement-flip
  - segment-normal-form
  - cycle-product
  - representation-lattice
  - multiplier-bridge
  - capacity-box
sources:
  - claim: type-I-core-formal-cycle-radical-cube-boundary
    role: universal-q-square-cycle-graph
  - claim: type-I-formal-external-cycle-product-law-boundary
    role: general-signed-cycle-product-law
  - claim: type-I-formal-cycle-radical-multiplier-bridge
    role: three-target-capacity-objective
visibility: public
last_checked: '2026-07-31'
---

# 通用一层周期的偶补数分段与两翻转正规形

## 1. 设置

设 \(R\ge3\) 为奇数，\(\mathcal Z\) 是通用一层图 \(U_R\) 的一个有向周期。对第
\(i\) 条边，记当前选中坐标、边素数和下一条边的选中坐标为

\[
c_i,
\qquad q_i,
\qquad c_{i+1},
\tag{1}
\]

其中循环下标满足 \(c_\ell=c_0\)，并且

\[
q_i^2\mid c_i,
\qquad
c_{i+1}=\frac{c_i}{q_i}
\quad\text{或}\quad
c_{i+1}=R-\frac{c_i}{q_i}.
\tag{2}
\]

第二种情形称为一次**补数翻转**，并继续用

\[
\varepsilon_i=
\begin{cases}
+1,&c_{i+1}=c_i/q_i,\\
-1,&c_{i+1}=R-c_i/q_i
\end{cases}
\tag{3}
\]

记录方向。

## 2. 翻转数必为正偶数

若 \(q_i\) 为奇数，除以 \(q_i\) 保持奇偶。若 \(q_i=2\)，条件 \(4\mid c_i\) 保证
\(c_i/2\) 仍为偶数。因此在两种情形中，不取补数都保持奇偶；因 \(R\) 为奇数，取补数
则恰好翻转奇偶。闭环回到同一个 \(c_0\)，所以补数翻转次数为偶数，并且

\[
\boxed{\prod_{i=0}^{\ell-1}\varepsilon_i=1.}
\tag{4}
\]

另一方面，若没有补数翻转，则每一步都有 \(c_{i+1}=c_i/q_i<c_i\)，不可能闭环。因此
翻转次数是**正偶数**。与一般带符号乘积律结合，得到加强式

\[
\boxed{\prod_{i=0}^{\ell-1}q_i\equiv1\pmod R.}
\tag{5}
\]

这一步真正使用了 \(q_i^2\mid c_i\)。只要求 \(q_i\mid c_i\) 的完整外部图允许
\(q_i=2\) 把偶数变成奇数，因而不能把 (4)--(5) 原样外推过去。

周期长度还满足

\[
\boxed{\ell\ge3.}
\tag{6}
\]

长度 1 已被“正偶数次翻转”排除。若长度为 2，则两条边都必须翻转；第 4 节的正规形
此时令 \(Q=q_0,T=q_1\) 为素数，会同时给出 \(q_0<q_1\) 与 \(q_1<q_0\)，矛盾。

## 3. 补数分段恒等式

从一次翻转后的坐标开始，沿若干条不翻转边下降，直到包含下一次翻转边。把第 \(j\) 段
的起点、边标号乘积和下一段起点分别记为

\[
A_j,
\qquad
Q_j=\prod_{i\in I_j}q_i,
\qquad
A_{j+1}.
\tag{7}
\]

段内连续相除，最后一条边取补，立即得到

\[
\boxed{A_j=Q_j(R-A_{j+1}).}
\tag{8}
\]

真实平方边还给出比 (8) 更强的支撑信息：

\[
\boxed{\operatorname{rad}(Q_j)\mid R-A_{j+1}.}
\tag{9}
\]

证明 (9) 时，固定任意 \(q\mid Q_j\)，并取它在该段的最后一次出现。边条件使相除前
至少还有两层 \(q\)，所以相除后仍留一层；后续只除其它素数，故最终商
\(R-A_{j+1}=A_j/Q_j\) 仍被 \(q\) 整除。

式 (8)--(9) 是一般整圈乘积同余看不到的真实邻接几何。

## 4. 恰有两次翻转时的闭式正规形

若周期恰有两次补数翻转，记两个下降段的起点与标号积为

\[
(A,Q),
\qquad(B,T).
\tag{10}
\]

式 (8) 变为

\[
A=Q(R-B),
\qquad
B=T(R-A).
\tag{11}
\]

由 (5)，正整数

\[
h=\frac{QT-1}{R}
\tag{12}
\]

有定义。联立 (11) 后得到完整闭式

\[
\boxed{
\begin{aligned}
A&=\frac{Q(T-1)}h,
&R-A&=\frac{Q-1}h,\\
B&=\frac{T(Q-1)}h,
&R-B&=\frac{T-1}h.
\end{aligned}}
\tag{13}
\]

特别地，\(h\mid Q-1\) 且 \(h\mid T-1\)。把 (9) 应用于两个段，还得到交叉整除

\[
\boxed{
\operatorname{rad}(Q)\mid\frac{T-1}h,
\qquad
\operatorname{rad}(T)\mid\frac{Q-1}h.}
\tag{14}
\]

若某个素数同时整除 \(Q,T\)，第一条整除会迫使它同时整除 \(T\) 与 \(T-1\)，故

\[
\boxed{(Q,T)=1.}
\tag{15}
\]

式 (13)--(15) 是两翻转周期的必要正规形；它们不单独编码段内素数的排列，也不声称
任意满足这些式子的 \((Q,T,h)\) 都能反向生成 \(U_R\) 周期。

## 5. 三目标桥的规范短代表形式

令 \(S\) 为周期**全部坐标**的素因子支撑，并定义

\[
\phi:\mathbb Z^S\longrightarrow(\mathbb Z/R\mathbb Z)^\times,
\qquad
\phi(z)=\prod_{q\in S}q^{z(q)}\pmod R.
\tag{16}
\]

按每条出边的选中坐标定向节点，并令

\[
z_i(q)=v_q(c_i)-v_q(R-c_i).
\tag{17}
\]

则 \(\phi(z_i)=-1\)。令 \(t\) 为边标号乘积的指数向量；由 (5)，
\(t\in\ker\phi\)，而且 \(z_i-z_0\in\ker\phi\)。因此定向周期生成一个关系子格

\[
\mathcal L_{\mathcal Z}
=\left\langle t,\ z_i-z_0:1\le i<\ell\right\rangle_{\mathbb Z}
\subseteq\ker\phi.
\tag{18}
\]

令

\[
B_S=\prod_{q\in S}q
\tag{19}
\]

并令 \(b\in\mathbb Z^S\) 为 \(4B_S\) 的指数向量。因为 \(2\in S\)，所以
\(b(2)=3\)，其余坐标为 1。三目标乘子桥的完整命中条件精确等价于

\[
\boxed{
\bigl([-1,1]\cap\mathbb Z\bigr)^S\cap
\left[
(z_0+\ker\phi)
\cup(z_0+b+\ker\phi)
\cup(z_0-b+\ker\phi)
\right]\ne\varnothing.}
\tag{20}
\]

三个陪集分别映到 \(-1,-4B_S,-(4B_S)^{-1}\)。所以一个直接可验的周期内充分条件是：
把 (20) 中的 \(\ker\phi\) 换成较小的 \(\mathcal L_{\mathcal Z}\) 后仍有交点。
这个充分条件不要求周期关系生成完整核。事实上当周期长度小于支撑维数时，
\(\mathcal L_{\mathcal Z}\) 的秩可能不足，等式
\(\mathcal L_{\mathcal Z}=\ker\phi\) 根本不可能。正确的剩余问题是：段正规形和互补坐标
是否直接迫使三个 \(\mathcal L_{\mathcal Z}\) 陪集之一进入单位盒；若不能，还须控制完整
核相对周期子格的额外关系并在 (20) 中寻找短代表。式 (5) 只提供核中的一条向量，不能
替代这项容量论证。

## 6. 为什么必须使用互补坐标

取 \(R=55\) 的真实通用周期

\[
\{6,49\}\to\{7,48\}\to\{24,31\}\to\{12,43\}\to\{6,49\},
\tag{21}
\]

依次选中 \(49,48,24,12\)，边标号为 \((7,2,2,2)\)，符号为
\((-1,+1,+1,-1)\)。于是 \(7\cdot2^3=56\equiv1\pmod{55}\)，而两翻转正规形为

\[
(Q,T,h,A,B)=(7,8,1,49,48).
\tag{22}
\]

若只取边标号，甚至取全部**选中坐标**的支撑

\[
S_{\rm sel}=\{2,3,7\},
\qquad B_{\rm sel}=42,
\tag{23}
\]

其 signed cube 的 24 个残数对

\[
-1,
\qquad-4B_{\rm sel},
\qquad-(4B_{\rm sel})^{-1}\pmod{55}
\tag{24}
\]

全部 miss。加入未选互补坐标产生的 \(31,43\) 后，完整支撑则有

\[
\frac3{7\cdot31}\equiv-1\pmod{55}.
\tag{25}
\]

所以任何三目标证明都必须实质使用中间互补坐标的新素因子；边标号乘积、平方整除和
所选坐标支撑三者合在一起仍然不够。

另一个两翻转例是首个 direct radical miss：\(R=30031\) 时

\[
(Q,T,h,A,B)=(125,961,4,30000,29791).
\tag{26}
\]

复现程序逐边核对 (4)--(15)、(21)--(26) 以及选中支撑的三目标 miss。入口和结果为
`reproductions/type_i_universal_cycle_flip_segments.py` 与
`reproductions/type-i-universal-cycle-flip-segment-results.json`。

## 7. 证明边界

本卡强化了周期几何并把开放问题压成 (18)--(20) 的有限盒短代表问题，但没有证明每个
两翻转周期或一般周期必命中。下一步应优先检验：两翻转正规形 (13)--(15) 加上所有
中间互补坐标，是否迫使 \(\mathcal L_{\mathcal Z}\) 的三个目标陪集之一进入单位盒；若
否，应保存首个**核心可实现**反例，而不是退回只含整圈乘积的较弱命题。
