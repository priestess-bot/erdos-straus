---
kind: claim
claim_id: type-I-formal-cycle-representation-lattice-capacity
title: 一层形式周期的表示格、二阶目标类与容量盒判据
statement: 对任意 m=1 形式周期，把第 i 个互素节点 a_i+b_i=R 编码为素因子指数向量 z_i，使其模 R 像为 a_i/b_i=-1。周期表示格 Gamma=<z_i> 的关系子格 L=<z_i-z_0,2z_0> 精确等于 Gamma 中模 R 像为 1 的核，故 Gamma/L 为二阶群，全部周期生成的 -1 表示恰为陪集 z_0+L。该陪集与 K 的内禀指数盒相交，当且仅当周期节点的奇次乘法组合可消去所有外部素数并落入 K 容量；任一交点都规范恢复同状态直接 Type I 证书。先对外部行作 Smith 消元、再对内部仿射格作商签名盒搜索，可有限且精确地输出 hit 见证或外部/容量 miss 证书，但不保证每个周期都有交点。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-general-b-centered-square-spectrum
  - type-I-core-formal-cycle-radical-cube-boundary
topics:
  - type-I
  - formal-target-pair
  - cycle
  - representation-lattice
  - quotient-certificate
  - Fourier
  - capacity-box
  - external-support
  - centered-spectrum
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: m-one-cycle-input
  - claim: type-I-general-b-centered-square-spectrum
    role: intrinsic-capacity-box
  - claim: type-I-core-formal-cycle-radical-cube-boundary
    role: independent-radical-sufficient-condition
visibility: public
last_checked: '2026-07-31'
---

# 一层形式周期的表示格、二阶目标类与容量盒判据

## 1. 周期节点是多组 \(-1\) 表示

固定 \(R\ge3\) 和一个 \(m=1\) 形式周期。把它的不同节点定向写成

\[
(a_i,b_i),
\qquad a_i+b_i=R,
\qquad (a_i,b_i)=1,
\qquad 0\le i<\ell.
\tag{1}
\]

令 \(P\) 为周期全部坐标与 \(K\) 的素因子并集。任何 \(q\in P\) 都与 \(R\) 互素；
周期坐标部分由 (1) 的互素性得到，\(K\) 部分由 \(4K=pR+1\) 得到。定义

\[
z_i(q)=v_q(a_i)-v_q(b_i)
\qquad(q\in P),
\tag{2}
\]

并令负指数在模 \(R\) 下解释为逆元：

\[
\varphi_R:\mathbb Z^P\longrightarrow(\mathbb Z/R\mathbb Z)^\times,
\qquad
\varphi_R(z)=\prod_{q\in P}q^{z(q)}\pmod R.
\tag{3}
\]

由 (1) 立刻有

\[
\boxed{\varphi_R(z_i)=a_i b_i^{-1}\equiv-1\pmod R.}
\tag{4}
\]

所以一个形式周期不只是一组迁移边，也是一组共享同一目标 \(-1\) 的整数表示。

## 2. 规范关系格与二阶目标类

在 \(\mathbb Z^P\) 中定义周期表示格和关系格

\[
\Gamma_{\mathcal Z}=\langle z_0,\ldots,z_{\ell-1}\rangle_{\mathbb Z},
\tag{5}
\]

\[
L_{\mathcal Z}
=
\left\langle
z_i-z_0\ (1\le i<\ell),\ 2z_0
\right\rangle_{\mathbb Z}.
\tag{6}
\]

由 (4)，(6) 的每个生成元都映到 \(1\)，故
\(L_{\mathcal Z}\subseteq\ker(\varphi_R|_{\Gamma_{\mathcal Z}})\)。反过来，任取

\[
w=\sum_{i=0}^{\ell-1}c_i z_i\in\Gamma_{\mathcal Z},
\tag{7}
\]

则

\[
\varphi_R(w)=(-1)^{\sum_i c_i}.
\tag{8}
\]

因为 \(R>2\)，\(-1\ne1\pmod R\)，所以同一 \(w\) 的不同生成表示具有相同的系数和
奇偶性。若 (8) 等于 1，则 \(s=\sum_i c_i\) 为偶数，而且

\[
w=
\sum_{i=1}^{\ell-1}c_i(z_i-z_0)+s z_0
\in L_{\mathcal Z}.
\tag{9}
\]

因此得到精确等式

\[
\boxed{
L_{\mathcal Z}
=\Gamma_{\mathcal Z}\cap\ker\varphi_R,
\qquad
[\Gamma_{\mathcal Z}:L_{\mathcal Z}]=2.}
\tag{10}
\]

全部由周期节点乘法生成的 \(-1\) 表示恰为

\[
\boxed{
\mathcal T_{\mathcal Z}=z_0+L_{\mathcal Z}
=
\left\{
\sum_i c_i z_i:\sum_i c_i\equiv1\pmod2
\right\}.}
\tag{11}
\]

这一定义不依赖基节点 \(z_0\) 或节点定向：反转某个 \((a_i,b_i)\) 只把 \(z_i\) 换为
\(-z_i\)，仍属于同一个奇陪集。

## 3. 与 \(K\) 容量盒相交当且仅当周期可终端化

令 \(\nu_q=v_q(K)\)，并在同一环境坐标 \(P\) 中定义内禀容量盒

\[
\mathcal B_K=
\left\{
z\in\mathbb Z^P:
z(q)=0\ (q\nmid K),\quad
-\nu_q\le z(q)\le\nu_q\ (q\mid K)
\right\}.
\tag{12}
\]

则有精确的周期终端判据

\[
\boxed{
\mathcal T_{\mathcal Z}\cap\mathcal B_K\ne\varnothing
\quad\Longleftrightarrow\quad
\text{周期节点的一个奇次乘法组合消去全部外部指数并落入 }K\text{ 盒}.}
\tag{13}
\]

右侧的“奇次”是所有整数系数之和为奇数，允许负系数。它不是启发式条件，而正是
(11)--(12) 的整数形式。

任取交点 \(w\)。把正负指数分别相乘为

\[
a=\prod_{w(q)>0}q^{w(q)},
\qquad
b=\prod_{w(q)<0}q^{-w(q)}.
\tag{14}
\]

则

\[
(a,b)=1,
\qquad ab\mid K,
\qquad a+b\equiv0\pmod R.
\tag{15}
\]

其中最后一个合同来自 \(\varphi_R(w)=-1\)。盒与目标陪集都关于 \(w\mapsto-w\) 对称：
对陪集而言，\(-w=w-2w\)，而 \(2w\in L_{\mathcal Z}\)。所以可交换后设 \(a<b\)。令

\[
C=\frac K{ab},
\qquad A=\frac{a+b}{R},
\qquad B=a,
\qquad H=b.
\tag{16}
\]

则中心除子与自然缺口为

\[
D=B^2C<K,
\qquad
h=\frac{4B^2C+1}{R},
\tag{17}
\]

而且

\[
K=BCH,
\qquad
p=4ABC-h,
\qquad
(A,B)=1,
\qquad
Bp+A=Hh.
\tag{18}
\]

所以 \((A,B,C)\) 是同一 \((p,R,K)\) 的 Type I 互素正规形。故 (13) 的每个交点都
给出原素数的独立可验直接终端；它不需要把形式周期边升级成合法解提升。

## 4. 商格是精确的对偶证书

令

\[
\Pi:\mathbb Z^P\longrightarrow
Q_{\mathcal Z}=\mathbb Z^P/L_{\mathcal Z},
\qquad
\tau_{\mathcal Z}=\Pi(z_0).
\tag{19}
\]

由 (6)，所有 \(z_i\) 在商中都等于 \(\tau_{\mathcal Z}\)，且

\[
2\tau_{\mathcal Z}=0.
\tag{20}
\]

式 (13) 等价于

\[
\boxed{
\tau_{\mathcal Z}\in\Pi(\mathcal B_K).}
\tag{21}
\]

所以 Smith 正规形把周期终端问题精确分成：商格自由部分上的整数等式、扭结部分上的
有限同余，以及 (12) 的逐坐标容量界。若 \(Q_{\mathcal Z}\) 有限，交点数还有标准 Fourier
公式

\[
\left|\mathcal T_{\mathcal Z}\cap\mathcal B_K\right|
=\frac1{|Q_{\mathcal Z}|}
\sum_{\chi\in\widehat Q_{\mathcal Z}}
\overline{\chi(\tau_{\mathcal Z})}
\prod_{q\mid K}
\left(
\sum_{e=-\nu_q}^{\nu_q}\chi(\Pi(e\mathbf e_q))
\right).
\tag{22}
\]

这给出一个规范的“表示—对偶—容量”接口：\(z_i\) 是表示，\(Q_{\mathcal Z}\) 与角色是
对偶，\(\mathcal B_K\) 是有限容量。式 (21) miss，或有限商情形下式 (22) 为零，是
固定周期的精确格障碍，不是原猜想的全局反例。

## 5. 两个边界实例

### 5.1 五周期的格交点

对 \(p=6{,}415{,}417\)、\(R=47\) 的五周期，取节点
\((16,31),(8,39),(4,43)\) 的向量，有

\[
w=z_{(16,31)}-z_{(8,39)}-z_{(4,43)},
\tag{23}
\]

其系数和为 \(-1\)，且

\[
\varphi_{47}(w)
=\frac{16}{31}\frac{39}{8}\frac{43}{4}
=\frac{1677}{62}
\equiv-1\pmod {47}.
\tag{24}
\]

取对称交点 \(-w\) 后，\((a,b)=(62,1677)\)、\(a+b=47\cdot37\)。又

\[
K=75{,}381{,}150,
\qquad
C=\frac K{ab}=725.
\tag{25}
\]

式 (16)--(17) 恢复

\[
(A,B,C,H,h)=(37,62,725,1677,237183),
\tag{26}
\]

给出该周期自身生成的一张同状态 Type I 终端。它与先前从完整中心盒取得的规范首证书
可以不同。

### 5.2 外部二进自环的商障碍

对 \((p,R,K)=(1009,3,757)\) 的自环 \(\{1,2\}\)，唯一周期向量在外部素数 2
坐标上为 \(-1\)。其关系格是偶数倍子格，目标类是奇类；但 \(\mathcal B_K\) 强制外部
2 坐标为 0。因此 (20) miss，精确解释了为什么这个周期不能在原 \(K\) 容量内消去其
外部素数。

## 6. 与 radical cube 的关系

radical-cube 判据允许从周期坐标的全部素因子中任取指数
\(\{-1,0,1\}\)，但不要求所得向量属于 \(\Gamma_{\mathcal Z}\)。本卡则只允许周期节点的
整数乘法组合，却可在 \(K\) 的真实指数预算内使用绝对值大于 1 的指数。因此一般情形下
两者互不蕴含：若 \(K\) 在相关支撑上平方自由，本卡命中必是 radical-cube 命中，反向仍
不自动成立；若 \(K\) 含高次幂，本卡还可能使用 radical cube 看不到的高指数。一个
radical witness 若同时属于 \(\Gamma_{\mathcal Z}\) 且不含外部素数，就是 (13) 的交点。

## 7. 精确有限判定算法

式 (13) 不需要枚举无限多个周期系数组合。把 (6) 的生成元写成列矩阵

\[
M=\left[z_1-z_0\mid\cdots\mid z_{\ell-1}-z_0\mid2z_0\right]
\in\mathbb Z^{P\times\ell},
\qquad
\mathcal T_{\mathcal Z}=z_0+M\mathbb Z^\ell.
\tag{27}
\]

按是否整除 \(K\) 把行坐标分成

\[
I=\{q\in P:q\mid K\},
\qquad
E=P\setminus I.
\tag{28}
\]

第一步只消去外部坐标。对整数方程

\[
M_Et=-z_{0,E}
\tag{29}
\]

作带左右幺模变换的 Smith 分解。若相应对角元整除条件失败，则 (13) 必定 miss，并且
这些失败的整除条件就是规范的 `MISS_EXTERNAL` 证书。若方程可解，则 Smith 数据给出一个
特解 \(t_0\) 和整数核基 \(N\)，全部外部坐标为零的候选可唯一归约为内部仿射格

\[
t=t_0+Nu,
\qquad
x_I=c+Au,
\qquad
c=z_{0,I}+M_It_0,
\qquad
A=M_IN.
\tag{30}
\]

再取 \(A\) 的 Smith 分解

\[
UAV=\operatorname{diag}(s_1,\ldots,s_\rho,0,\ldots,0),
\qquad s_j>0,
\tag{31}
\]

并定义商格签名

\[
\sigma_A(x)=
\left(
(Ux)_1\bmod s_1,\ldots,(Ux)_\rho\bmod s_\rho,
(Ux)_{\rho+1},\ldots,(Ux)_{|I|}
\right).
\tag{32}
\]

于是

\[
x-c\in A\mathbb Z^{\operatorname{rank}N}
\quad\Longleftrightarrow\quad
\sigma_A(x)=\sigma_A(c).
\tag{33}
\]

算法只需在有限盒 \(-\nu_q\le x(q)\le\nu_q\) 中检查 (33)。周期中没有出现的
\(K\)-素数行在 \(z_0,M\) 中恒为零，必须固定为零，可在搜索前删去。记剩余活跃盒大小为

\[
B_{\rm eff}=\prod_{q\in I_{\rm active}}(2\nu_q+1).
\tag{34}
\]

直接枚举需要 \(O(|I|B_{\rm eff})\) 次整数运算；把坐标按盒大小平衡分成两半，并利用
签名的可加性做 meet-in-the-middle，时间和内存降为
\(O(|I|\sqrt{B_{\rm eff}})\) 量级。所有比较都是精确整数等式或同余，不使用浮点近似。

命中时，由 (31) 恢复 \(u\)，再由 (30) 恢复 \(t\)。若

\[
t=(t_1,\ldots,t_{\ell-1},t_*),
\tag{35}
\]

则原节点的整数系数为

\[
c_0=1-\sum_{i=1}^{\ell-1}t_i+2t_*,
\qquad
c_i=t_i\quad(1\le i<\ell).
\tag{36}
\]

其系数和恒为 \(1+2t_*\)，所以恢复的是奇陪集中的真实表示；随后按 (14)--(18) 输出并
精确核验 Type I 证书。若有限盒全部 miss，则 Smith 数据、目标签名和完整盒签名缺失共同
构成固定周期的 `MISS_CAPACITY` 证书。该两阶段算法因此同时给出规范 hit 见证和规范 miss
障碍，而不是只报告启发式搜索失败。

## 8. 证明边界

本卡证明的是固定周期的完整判据和有限判定算法，不是“每个周期必命中”。当 (20) miss
时，仍必须使用周期外信息：全局 Type I/II 终端、跨模数中心谱、源可达性，或具有
E1--E5 与全域解提升的合法 support switch。
