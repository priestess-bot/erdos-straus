---
kind: claim
claim_id: type-I-core-jacobi-ordered-capacity-strict-slack-terminal
title: 核心 Jacobi 符号盒的严格有序容量余量与等号终端
statement: >-
  设 p≡1 (mod 24)、4K=pR+1，并对 K 的全部素因子采用 N=1 的规范固定层分解。
  若 -1 位于这些素因子模 R 生成的群 H 中，则 Jacobi 角色 chi_R=(./R) 在 H 上
  非平凡。令 X={1,chi_R}、L=ker chi_R、I={i:chi_R(q_i)=-1}。若不存在同符号
  H-像碰撞，则 q-primary 有序权重计数满足
  C_{-1,X}<=Theta_ord(-1,X)-2^{r-|I|}<=2^{r-1}|H|-1。
  因而 C_{-1,X}>Theta_ord-2^{r-|I|} 已强制一个原指数盒内的非零核关系和偶终端；
  特别地，核心 N=1 分支中的 C>=Theta_ord 或 C>=[K_X:P]T_J 均已终端。
  该严格余量覆盖任意生成元数和非均匀预算。一般固定层 J 不能无条件继承：平衡
  u=v 时存在 C=Theta_ord 而无同符号 P-碰撞的抽象反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-ordered-weight-capacity-terminal
  - type-I-fixed-layer-stabilizer-collision-terminal
  - type-I-short-relation-even-terminal
topics:
  - type-I
  - core-prime
  - Jacobi-character
  - fixed-layer
  - ordered-weight-capacity
  - strict-slack
  - short-relation
  - even-terminal
  - selector
sources:
  - reproduction: reproductions/type_i_core_jacobi_ordered_capacity_strict_slack_terminal.py
    role: focused-core-slack-collision-and-balanced-layer-boundary
visibility: public
last_checked: '2026-08-09'
---

# 核心 Jacobi 符号盒的严格有序容量余量与等号终端

## 1. 规范无固定层分解

设

\[
p\equiv1\pmod {24},\qquad 4K=pR+1,\qquad R>1,
\tag{1}
\]

其中 \(p\) 为素数，并写

\[
K=\prod_{i=1}^r q_i^{\nu_i},\qquad
\nu_i\ge1,\qquad(q_i,R)=1.
\tag{2}
\]

对固定层稳定子选择器取总是合法的规范分解

\[
N=1,\qquad J=P=\{1\},\qquad
H=\langle q_1,\ldots,q_r\rangle\le U(R).
\tag{3}
\]

若 \(-1\notin H\)，已有 G 型支撑分离角色，以下只讨论 \(-1\in H\) 的分支。
令

\[
\chi_R(a)=\left(\frac aR\right),\qquad
X=\{1,\chi_R\},\qquad L=\ker(\chi_R|_H),
\tag{4}
\]

并记

\[
d=|L|=\frac{|H|}{2},\qquad
I=\{i:\chi_R(q_i)=-1\}.
\tag{5}
\]

这里不要求 \(R\) 为素数或平方自由数。对任意奇数
\(R=\prod_\ell\ell^{e_\ell}\)，Jacobi 符号是 \(U(R)\) 上的乘法角色；平方
因子只会使相应局部分量平凡。由 (1) 和 \(p\equiv1\pmod4\) 有

\[
R\equiv3\pmod4,
\qquad
\chi_R(-1)=(-1)^{(R-1)/2}=-1.
\tag{6}
\]

所以 \(\chi_R|_H\) 非平凡，(5) 成立且 \(I\ne\varnothing\)。另一方面，
\(4K\equiv1\pmod R\) 与 \(\chi_R(4)=1\) 给出

\[
1=\chi_R(K)=(-1)^{\sum_{i\in I}\nu_i}.
\tag{7}
\]

因此 \(I\) 中具有奇数预算 \(\nu_i\) 的坐标个数为偶数。这一核心奇偶约束正是
一般 centered 商群反例所缺少的严格余量来源。

## 2. 每个符号盒的精确字符和

把第 \(i\) 个指数区间分成

\[
I_{i,+}=[0,\nu_i]\cap\mathbb Z,
\qquad
I_{i,-}=[-\nu_i,-1]\cap\mathbb Z.
\tag{8}
\]

对 \(\sigma\in\{+,-\}^r\) 令

\[
B_\sigma=\prod_i I_{i,\sigma_i},\qquad
b_\sigma=|B_\sigma|,
\qquad
\Phi(z)=\prod_iq_i^{z_i}\pmod R,
\tag{9}
\]

以及

\[
D_\sigma=\sum_{z\in B_\sigma}\chi_R(\Phi(z)).
\tag{10}
\]

若 \(i\notin I\)，对应的一维和为

\[
S_{i,+}=\nu_i+1,\qquad S_{i,-}=\nu_i.
\tag{11}
\]

若 \(i\in I\)，则

\[
S_{i,+}=
\begin{cases}1,&2\mid\nu_i,\\0,&2\nmid\nu_i,
\end{cases}
\qquad
S_{i,-}=
\begin{cases}0,&2\mid\nu_i,\\-1,&2\nmid\nu_i.
\end{cases}
\tag{12}
\]

并且 \(D_\sigma=\prod_iS_{i,\sigma_i}\)。所以 \(D_\sigma\ne0\) 当且仅当每个
active-even 坐标取正盒、每个 active-odd 坐标取负盒；inactive 坐标任取。这样的
special boxes 恰有

\[
\boxed{2^{r-|I|}}
\tag{13}
\]

个。由 (7)，每个 special box 中来自 active-odd 坐标的 \(-1\) 因子个数为偶数，
故

\[
\boxed{D_\sigma>0\quad\text{对每个 special box}.}
\tag{14}
\]

其余盒精确满足 \(D_\sigma=0\)。

## 3. 严格有序容量余量

取目标 \(y=-1\)。过滤条件

\[
\Phi(z)\in yL=-L
\tag{15}
\]

等价于 \(\chi_R(\Phi(z))=-1\)。所以第 \(\sigma\) 个盒的过滤计数为

\[
\boxed{c_\sigma=\frac{b_\sigma-D_\sigma}{2},}
\qquad
C_{-1,X}=\sum_\sigma c_\sigma.
\tag{16}
\]

在 \(J=P=\{1\}\) 时，有序权重

\[
w_{-1}(a)=\mathbf1_{a\in-L}
\tag{17}
\]

在 \(H\) 上恰有 \(d\) 个 \(1\) 和 \(d\) 个 \(0\)。若某个
\(b_\sigma>|H|=2d\)，则 \(B_\sigma\to H\) 已由鸽巢原理产生同符号碰撞，直接得到
偶终端。以下设所有 \(b_\sigma\le2d\)，则该盒的有序容量为

\[
\Theta_\sigma=\min(b_\sigma,d),
\qquad
\Theta_{\rm ord}(-1,X)=\sum_\sigma\Theta_\sigma.
\tag{18}
\]

再假设没有同符号 \(H\)-像碰撞。对 non-special box，(16) 给出

\[
c_\sigma=b_\sigma/2\le\min(b_\sigma,d)=\Theta_\sigma.
\tag{19}
\]

对 special box，若 \(b_\sigma\le d\)，则由 \(D_\sigma>0\) 得
\(c_\sigma<b_\sigma=\Theta_\sigma\)；若
\(d<b_\sigma\le2d\)，则

\[
c_\sigma<b_\sigma/2\le d=\Theta_\sigma.
\tag{20}
\]

两边都是整数，故每个 special box 至少亏一个单位。结合 (13)，得到

\[
\boxed{
C_{-1,X}
\le
\Theta_{\rm ord}(-1,X)-2^{r-|I|}
\le d2^r-1.}
\tag{21}
\]

这给出比旧严格门更强的可构造终端条件：

\[
\boxed{
C_{-1,X}>\Theta_{\rm ord}(-1,X)-2^{r-|I|}
\Longrightarrow
\text{同符号核关系偶终端}.}
\tag{22}
\]

特别地，\(C_{-1,X}\ge\Theta_{\rm ord}\) 已终端。又因
\([K_X:P]T_J=d2^r\)，条件

\[
C_{-1,X}\ge [K_X:P]T_J
\tag{23}
\]

也已足够，不再需要一般模型中的严格大于号。碰撞向量之差满足原坐标预算，且其像为
\(1=P\)；短关系偶终端引理遂构造 \(E\mid4K^2\) 和较小偶数 \(n<p\)。

## 4. 全盒计数的第二种精确证明

令

\[
V=\prod_i(2\nu_i+1),
\qquad
A_0=\prod_{i\notin I}(2\nu_i+1).
\tag{24}
\]

全对称盒上的字符和为 \(A_0>0\)，所以

\[
\boxed{C_{-1,X}=\frac{V-A_0}{2}.}
\tag{25}
\]

无同符号碰撞时，每个符号盒至多含 \(|H|\) 个点，故
\(V\le2^r|H|\)。于是

\[
\boxed{
d2^r-C_{-1,X}
=\frac{2^r|H|-V+A_0}{2}\ge1.}
\tag{26}
\]

式 (26) 独立确认强阈值等号在核心域不可能保持无碰撞；式 (21) 还定位了更细的
逐盒余量。

## 5. 聚焦控制与固定层边界

真实核心控制

\[
p=97,\qquad R=67,\qquad K=5^3\cdot13
\tag{27}
\]

具有 \(I=\{5,13\}\)。四个符号盒的 \((b_\sigma,c_\sigma)\) 为

\[
(8,4),\quad(4,2),\quad(6,3),\quad(3,1).
\tag{28}
\]

每个盒的 \(H\)-像均单射，且

\[
C_{-1,X}=10,\qquad
\Theta_{\rm ord}=21,\qquad
d2^r=132.
\tag{29}
\]

这验证了定理确实覆盖多生成元和非均匀预算，但也说明它尚未关闭
\(C<\Theta_{\rm ord}\) 的内部低密度区。另一方面，
\((p,R,K)=(433,15,1624)\) 的正控制已有符号盒大于 \(|H|\)，直接产生短关系
\(2\cdot7\cdot29^{-1}\equiv1\pmod {15}\) 和偶终端 \((E,n)=(3136,224)\)。
非平方自由模数控制
\((p,R,K)=(73,27,493=17\cdot29)\) 也满足
\(|H|=18\)、\(C=4\)、\(\Theta_{\rm ord}=9\)，确认这里使用的是真正 Jacobi
角色而不是只适用于素模数的 Euler criterion。

不能把 (21) 无条件搬到任意固定层。以加法记号取

\[
H=C_6,\qquad J=\{0,1\},\qquad P=\{0\},\qquad
\chi(x)=(-1)^x,\qquad y=3,
\tag{30}
\]

残余生成元为 \((1,2)\)、预算为 \((1,1)\)。四个符号盒大小为
\(4,2,2,1\)，且各自到 \(C_6\) 的像均单射。因为 \(J\) 在 \(\ker\chi\) 与其
非平凡陪集中各有一个元素，每个残余点恰有一个 eligible fixed-layer 元素，从而

\[
C_{y,X}=\Theta_{\rm ord}=9
\tag{31}
\]

而没有同符号 \(P\)-碰撞。一般 fixed layer 的两侧权重平衡 \(u=v\) 会完全抹去
Jacobi 严格余量；因此主定理只使用对每个图表都可选的 \(N=1\) 规范分支。

## 6. 对统一选择器的推进

旧有序容量定理只能在 \(C>\Theta_{\rm ord}\) 时终端，并由非核心一生成元族证明一般
抽象模型的严格号不可删除。本定理说明该边界不是核心算术的真实边界：关系
\(4K\equiv1\pmod R\) 强制 special boxes 的 Jacobi 字符和同向为正，从而对任意
生成元数和非均匀预算产生显式余量。

它尚未证明低密度分支 \(C\le\Theta_{\rm ord}-2^{r-|I|}\) 必有跨状态递降，也不把
G 型支撑分离角色直接变成终端；但它已经排除了核心域中全部“有序容量等号而无短关系”
的 \(N=1\) 边界。

该内部低密度区现已进一步分解。精确目标缺失会从 Jacobi-negative 陪集中删去一个
目标像，使每个符号盒至多占 \(d-1\) 个像；与 special-box 余量及全局偶性合并后得到
更强容量门。余下 F 状态在 Jacobi 核上必有规范成对 Fourier 负对比，并按奇 Hall /
二进 Sylow 分派为奇素数源秩旗标或纯二进缩放关系。真实 \(p=97\) 控制由此得到一个
全局 11 阶核角色和局部 11 阶源秩旗标，但仍没有物理 11-owner。详见
[核心 Jacobi 饱和陪集的删点容量、成对 Fourier 与主分派选择器](type-I-core-jacobi-punctured-kernel-primary-selector.md)。
