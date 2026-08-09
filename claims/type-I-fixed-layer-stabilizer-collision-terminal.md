---
kind: claim
claim_id: type-I-fixed-layer-stabilizer-collision-terminal
title: 固定层稳定子商碰撞与 q-primary 饱和的短关系偶终端
statement: >-
  对合法 Type I 状态 4K=pR+1，写 K=N product_i q_i^{nu_i}，其中 q_i 为两两不同的
  残余素数且与固定素支撑互素，J=C_R(N)，P=Stab_H(J)。同一符号盒内两个残余指数向量在 H/P 中碰撞时，
  P 的固定层吸收把其差提升为完整 K 指数盒的非零核关系，故产生偶终端。因而
  product_i(2nu_i+1)>2^r |<pi(q_i)>| 是直接终端的充分条件。更一般地，对
  q-primary X<=P^perp、K_X=X^perp，C_{y,X}>|K_X:P| |J| 2^r 强制同一终端；
  C_{y,X}>|J|2^r 则至少给出一个有界 q-primary 商关系，不能自动冒充终端。
  对精确目标纤维，centered 固定层把阈值从 |J|2^r 收紧为 |J/P|2^r。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-short-relation-even-terminal
topics:
  - type-I
  - fixed-layer
  - stabilizer
  - quotient
  - collision
  - short-relation
  - even-terminal
  - q-primary
  - target-fiber
  - representation
  - finite-abelian-groups
  - proof-program
sources:
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: P-periodic-centered-fixed-layer
  - claim: type-I-short-relation-even-terminal
    role: full-box-kernel-relation-terminal
  - reproduction: reproductions/type_i_fixed_layer_stabilizer_collision_terminal.py
    role: focused-positive-and-boundary-receipts
visibility: public
last_checked: '2026-08-09'
---

# 固定层稳定子商碰撞与 q-primary 饱和的短关系偶终端

## 设置

设

\[
4K=pR+1,\qquad
K=NQ,\qquad
Q=\prod_{i=1}^{r}q_i^{\nu_i},
\qquad
\gcd(N,Q)=1,
\tag{1}
\]

其中 \(R\) 为正奇数，\(q_i\) 是两两不同的素数，且固定与残余素支撑不相交。令

\[
H=\left\langle \ell\bmod R:\ell\mid K\right\rangle,\qquad
J=\mathcal C_R(N),\qquad
P=\operatorname{Stab}_H(J),\qquad
\pi:H\longrightarrow H/P.
\tag{2}
\]

由固定层稳定子约化，\(P\subseteq J\)，而中心化层 \(J\) 对取逆封闭。对残余
指数盒和残余乘积写

\[
\mathcal B_\nu=\prod_i[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad
\Phi(z)=\prod_iq_i^{z_i}.
\tag{3}
\]

每个坐标区间按 \([0,\nu_i]\) 与 \([-\nu_i,-1]\) 分成两个符号盒。记

\[
\bar G_Q=\langle\pi(q_1),\ldots,\pi(q_r)\rangle\le H/P.
\tag{4}
\]

## 稳定子商碰撞终端

若存在不同 \(z,w\in\mathcal B_\nu\)，位于同一符号盒，且

\[
\pi(\Phi(z))=\pi(\Phi(w)),
\tag{5}
\]

则存在合法偶终端。

事实上，令 \(\delta=z-w\)。同一符号盒给出

\[
|\delta_i|\le\nu_i,
\tag{6}
\]

而 (5) 给出 \(h:=\Phi(\delta)\in P\)。因为 \(h^{-1}\in P\subseteq J\)，存在
固定层向量 \(\alpha\)，满足固定素数的指数预算以及

\[
\prod_{\ell\mid N}\ell^{\alpha_\ell}\equiv h^{-1}\pmod R.
\tag{7}
\]

把 \(\alpha\) 与 \(\delta\) 按不相交的素支撑拼接，得到完整 \(K\) 的非零指数盒向量
\(\lambda\)，并有

\[
\prod_{\ell\mid K}\ell^{\lambda_\ell}\equiv1\pmod R.
\tag{8}
\]

短关系偶终端引理遂适用：定向 \(\lambda\) 后，

\[
\rho=\prod_{\ell\mid K}\ell^{\lambda_\ell}<1,\qquad
U=K\rho,\qquad E=4U,\qquad n=\frac{4K-E}{R}
\tag{9}
\]

满足 \(E\mid4K^2\)、\(E\equiv1\pmod R\)、\(4\mid n\) 与 \(0<n<p\)。

对 \((\operatorname{sgn}z,\pi(\Phi(z)))\) 装箱，立即得到充分条件

\[
\boxed{
\prod_i(2\nu_i+1)>2^r|\bar G_Q|
\quad\Longrightarrow\quad
\text{存在偶终端}.
}
\tag{10}
\]

由于 \(|\bar G_Q|\le|H/P|\)，右边也可用较粗的 \(2^r|H/P|\) 替代。

## q-primary 饱和的精确升级

令 \(X\le P^\perp\) 为非平凡 q-primary 角色子群，记

\[
K_X=X^\perp,\qquad
T_J=|J|2^r,\qquad
s=[K_X:P].
\tag{11}
\]

对 \(y\in H\)，定义

\[
N_y=\#\{(j,z)\in J\times\mathcal B_\nu:j\Phi(z)=y\},
\tag{12}
\]

\[
C_{y,X}=
\#\{(j,z)\in J\times\mathcal B_\nu:j\Phi(z)\in yK_X\}.
\tag{13}
\]

### 弱饱和只给商关系

若 \(C_{y,X}>T_J\)，按 \((j,\operatorname{sgn}z)\) 分入至多 \(T_J\) 个桶。
每个碰撞给出不同 \(z,w\) 与

\[
\delta=z-w\ne0,\qquad
|\delta_i|\le\nu_i,\qquad
\Phi(\delta)\in K_X.
\tag{14}
\]

实际上至少有 \(C_{y,X}-T_J\) 个这种碰撞对。若

\[
\Lambda_X=\{\delta\in\mathbb Z^r:\Phi(\delta)\in K_X\},
\tag{15}
\]

则

\[
\mathbb Z^r/\Lambda_X\simeq\operatorname{im}(\Phi\bmod K_X)
\tag{16}
\]

是阶整除 \(|X|\) 的有限 q-群。因此普通
q-primary quotient saturation 是一个规范的短商关系格证书；它并不蕴含
\(\Phi(\delta)\in P\)，所以不能直接写成偶终端。

### 稳定子阈值强制终端

因为 \(P\subseteq K_X\) 且 \(J\) 是 \(P\)-周期集，(13) 的记录在 \(P\) 作用下
按大小 \(|P|\) 的轨道分解。故

\[
\bar C_{y,X}=\frac{C_{y,X}}{|P|},
\qquad
|\bar J|=\frac{|J|}{|P|}.
\tag{17}
\]

在 \(H/P\) 中，目标集合 \(yK_X/P\) 有 \(s\) 个元素。按

\[
(\text{目标 }P\text{-陪集},\ jP,\ \operatorname{sgn}z)
\tag{18}
\]

装箱，桶数至多 \(s|\bar J|2^r\)。因此

\[
\boxed{
C_{y,X}>sT_J
\quad\Longrightarrow\quad
\Phi(z-w)\in P
\quad\Longrightarrow\quad
\text{偶终端}.
}
\tag{19}
\]

特别地，若 \(K_X=P\)，原有 \(C_{y,X}>T_J\) 饱和分支必然终端。这里的
稳定子吸收计数本身只需要 \(X\le P^\perp\)；q-primary 假设只使商关系和
Fourier 标签带有一个指定的 primary 类型。只有当 \(H/P\) 是 q-primary 时，
这个 \(X=P^\perp\) 特例才属于 q-primary 选择器。

### 精确目标的稳定子缩放

精确目标记录无需先共享同一个 \(j\)。若

\[
\boxed{N_y>|J/P|2^r,}
\tag{20}
\]

则两个记录共享 \(jP\) 与符号盒。精确等式 \(j\Phi(z)=j'\Phi(w)=y\) 与
\(jP=j'P\) 给出 \(\Phi(z-w)\in P\)，再由第一节得到偶终端。这比抽象固定层的
\(N_y>T_J\) 阈值严格更强；它依赖 \(J=\mathcal C_R(N)\) 的中心化固定层吸收。

## 聚焦正控制

取

\[
p=433,\qquad R=15,\qquad K=1624=2^3\cdot7\cdot29,
\qquad N=29.
\tag{21}
\]

此时 \(J=P=\{1,14\}\)、\(H=U(15)\)、\(|H/P|=4\)。取
\(X=P^\perp\)，它是 2-primary，且 \(K_X=P\)。对目标 \(y=-1=14\)，有

\[
N_y=5,\qquad C_{y,X}=10,\qquad
|J/P|2^r=4,\qquad T_J=8.
\tag{22}
\]

所以 (19) 和 (20) 都适用。显式的同符号精确碰撞是

\[
1\cdot2^1 7^1\equiv14\equiv14\cdot2^0 7^0\pmod {15}.
\tag{23}
\]

取关系

\[
2\cdot7\cdot29^{-1}\equiv1\pmod {15},
\tag{24}
\]

则

\[
U=1624\frac{14}{29}=784,\qquad
E=3136,\qquad n=224<433.
\tag{25}
\]

另一个非退化的稳定子商碰撞控制为
\((p,R,K,N,Q)=(73,23,420,12,35)\)：\(P=\mathcal C_{23}(12)\) 的阶为 \(11\)，
残余盒体积 \(9\) 超过 \(2^2|H/P|=8\)，而
\(5\cdot7^{-1}=4\in P\) 与 \(2\cdot3=4^{-1}\) 给出 \(U=98,E=392,n=56\)。

## 弱阈值边界

取

\[
p=97,\qquad R=67,\qquad K=1625=5^3\cdot13,\qquad N=13.
\tag{26}
\]

这里 \(J=\{1,13,31\}\)、\(P=\{1\}\)。取二次 \(X\)，则 \(K_X\) 是 33 阶平方
子群。对 \(y=-1\)，有

\[
N_y=0,\qquad C_{y,X}=10>6=T_J,
\qquad [K_X:P]T_J=198.
\tag{27}
\]

因此普通饱和发生而强阈值失败。以 \(2\) 为 \(U(67)\) 的生成元，
\(\log_2 5=15\)、\(\log_2 13=19\)。完整短关系必须满足

\[
15a+19b\equiv0\pmod {66},
\qquad |a|\le3,\quad |b|\le1.
\tag{28}
\]

模 \(3\) 先强制 \(b=0\)，随后 \(22\mid a\)，所以盒内只有零关系。这严格表明
\(C_{y,X}>T_J\) 只能输出 q-primary 商关系，不能自动升级为固定层吸收或终端。

## 聚焦复现

    python3 reproductions/type_i_fixed_layer_stabilizer_collision_terminal.py --verify

复现器核验两个实际正控制、p=433 的精确计数与 q-primary 阈值，以及 p=97 的弱饱和
反例；不做历史范围扫描。
