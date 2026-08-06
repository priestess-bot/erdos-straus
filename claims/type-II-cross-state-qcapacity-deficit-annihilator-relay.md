---
kind: claim
claim_id: type-II-cross-state-qcapacity-deficit-annihilator-relay
title: Type II 跨状态 q 进缺口的 annihilator 子群—商递降桥
statement: 在同一固定参数纤维、同一 ell 初等源商中，若一个独立请求集 U 的逐层 q 进容量上界满足 C_q(U)<|U|，则其合法邻域必有 Rado/Hall 缺口，并存在阶 ell 对偶角色 lambda 湮灭所有邻域源列而分离至少一个请求方向。若 U 还是 SOURCE-DOMINATING-CUT，且全部真实源列已闭合到规范化源集 1 in R，则 lambda 湮灭整个源关系商。令 chi_lambda 为对应阶 ell 角色、K=ker(chi_lambda)：目标在 K 外时给出严格商 relay，目标在 K 内时给出严格子群 relay，K=1 的核外情形才是顶层 primary 终端；源列未被支配时输出 SOURCE_COLUMN_ESCAPE/算术障碍。只有 source-labelled SNF/CRT/range source-switch 与 E1--E5 解提升门全部通过，抽象 relay 才升级为整数递归边。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-layered-rado-qcapacity-cut
  - type-II-hall-deficit-linear-dual-bridge
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-cross-state-source-relation-role-capacity-dispatch
topics:
- type-II
- cross-state
- q-adic
- annihilator
- quotient-descent
- subgroup-descent
- Fourier
- Hall
- source-dominating-cut
- source-switch
- proof-program
sources:
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: q-layer-capacity-deficit
  - claim: type-II-hall-deficit-linear-dual-bridge
    role: Hall-to-dual-character
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: target-phase-two-sided-relay
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: quotient-descent-gate
visibility: public
last_checked: '2026-08-06'
---

# Type II 跨状态 q 进缺口的 annihilator 子群—商递降桥

## 1. q 进缺口产生对偶角色

固定一个已经通过来源标签、SNF、source-switch 和范围门的参数纤维。令 \(H\) 为
其有限阿贝尔目标商，\(V_\ell\) 为真实 \(\ell\)-初等源商，且
\(\mathcal R_\ell\) 是已去除线性依赖的角色请求集。对 \(U\subseteq\mathcal R_\ell\)
构造 q 层兼容图，记合法邻域为 \(N(U)\)，源列张成空间为
\[
W_U=\operatorname{span}_{\mathbb F_\ell}\{v_c:c\in N(U)\}.
\tag{1}
\]
若分层 q 进切割给出
\[
\mathsf C_q(U)<|U|,
\tag{2}
\]
则所有合法槽均包含在逐层上界内，因而
\[
|N(U)|\le\mathsf C_q(U)<|U|,
\qquad
\dim W_U\le |N(U)|<|U|.
\tag{3}
\]
把 \(D_U\subseteq V_\ell\) 记为 \(U\) 的需求方向空间。有限维对偶性给出
\[
\boxed{
\exists\lambda\in V_\ell^\*:
\lambda|_{W_U}=0,\qquad
\lambda|_{D_U}\ne0.
}
\tag{4}
\]
对应的阶 \(\ell\) 角色记为
\[
\chi_\lambda(x)
=\exp\!\left(\frac{2\pi i}{\ell}
\lambda(x\bmod \ell A_\ell)\right).
\tag{5}
\]
因此 q 进容量缺口不仅是槽数量不足，也产生一个可复核的
\(\mathrm{SOURCE\_RANK\_FOURIER\_SEPARATION}\)；它在所有邻域源列上平凡，并分离
至少一个未支付请求方向。

## 2. SOURCE-DOMINATING-CUT 与全源列闭包

称 \(U\) 满足 SOURCE-DOMINATING-CUT，若固定纤维的每个真实源生成元
\(g_i\in H\) 都有一个合法的同纤维邻接槽 \(c_i\in N(U)\)，且
\[
v_{c_i}=g_i\bmod \ell A_\ell.
\tag{6}
\]
这里的邻接槽必须保留真实 q 整除、来源标签和参数回译；跨纤维的同余相似列不能
冒充 (6)。

在 (6) 下，式 (4) 立即给出
\[
\lambda(g_i\bmod\ell A_\ell)=0
\quad\text{对所有 }i.
\tag{7}
\]
将源和集按一个实际基点的逆元规范化，并记
\[
1\in R\subset H,
\qquad
\tau\in H\setminus R.
\tag{8}
\]
若这些生成元在真实源关系商中生成全部已回译的源块成员，则
\(\chi_\lambda\) 在整个源集上平凡。令
\[
K=\ker(\chi_\lambda)\le H.
\tag{9}
\]
于是
\[
R\subseteq K.
\tag{10}
\]
这才是全源列闭包的 annihilator 条件；只在当前邻域槽上为零不足以推出 (10)。

若 SOURCE-DOMINATING-CUT 不成立，则输出
\[
\mathrm{SOURCE\_COLUMN\_ESCAPE}
\]
并把未被 \(N(U)\) 支配的生成元加入完整 Hall 菜单；若该列因 SNF、CRT 或范围门
无法加入，则保存
\(\mathrm{SOURCE\_COLUMN\_EDGE\_OBSTRUCTED}\)。不能在此分支直接声称商递降。

## 3. 目标相位的双向 annihilator 分派

在 (8)--(10) 的全源列闭包下，计算 \(\chi_\lambda(\tau)\)：

1. 若 \(\chi_\lambda(\tau)\ne1\) 且 \(K\ne1\)，则
   \(\pi:H\to H/K\) 是严格较小的有限商，\(\pi(R)=\{1\}\) 而
   \(\pi(\tau)\ne1\)。因此商中目标仍缺失，输出
   \[
   \mathrm{GLOBAL\_ANNIHILATOR\_LOWER\_RELAY}
   =(H,R,\tau,\lambda,\pi).
   \tag{11}
   \]
   若该商存在保持来源标签的整数 source-switch、\(B'>A\) 和 E1--E5 解提升，
   (11) 才升级为严格可提升递降。
2. 若 \(\chi_\lambda(\tau)\ne1\) 且 \(K=1\)，则没有非平凡更小商，输出
   \[
   \mathrm{TOP\_PRIMARY\_ANNIHILATOR}(\ell,\lambda)
   \]
   并转入广义 \(2^j\)/primary 数字终端或其它 Type I/F/G 出口。
3. 若 \(\chi_\lambda(\tau)=1\)，则 \(\tau\in K\)。由 (10) 和
   \(\tau\notin R\)，同一个目标缺失保留在 \(K\) 中：
   \[
   \mathrm{ANNIHILATOR\_SUBGROUP\_LOWER\_RELAY}
   =(K,R,\tau,\chi_\lambda).
   \]
   因 \(1\in R\)，这里 \(K=1\) 不可能，故 \(|K|<|H|\) 给出严格真子群
   relay。若子群的 SNF/source-switch/标签/range 或 E1--E5 提升门失败，则同时记录
   \(\mathrm{ANNIHILATOR\_SUBGROUP\_LIFT\_OBSTRUCTED}\) 和
   \(\mathrm{RELATION\_FOURIER\_NO\_TARGET\_SEPARATION}\)；后者只是不收费的关系
   回执，不能抹掉已得到的抽象严格子群下降。

这三项都以 (7) 的真实源闭合为前提；若源列逃逸，先返回第 2 节的
SOURCE_COLUMN_ESCAPE。

## 4. 证明

由 (2) 和 (3)，邻域源列张成维数严格小于独立请求数。有限维双正交关系给出
\(\lambda\) 满足 (4)，而 (5) 是其阶 \(\ell\) 的角色实现。若割是
SOURCE-DOMINATING-CUT，则每个真实源生成元都有一个被 \(\lambda\) 湮灭的邻接列，
所以 (7) 成立；由生成性，整个源集落入 \(K\)。

当 \(\chi_\lambda(\tau)\ne1\) 时，源集在商 \(H/K\) 中只含单位元而目标非单位元，
故商目标缺失。若 \(K\ne1\)，商阶严格下降；若 \(K=1\)，只能进入顶层 primary
终端。若 \(\chi_\lambda(\tau)=1\)，则 \(\tau\in K\)，而 (10) 与
\(\tau\notin R\) 给出同一缺失在 \(K\) 内保留。规范化的 \(1\in R\) 排除
\(K=1\)，所以此时群阶也严格下降。源列逃逸时闭包假设不成立，必须补边或记录
障碍。整数提升门失败只阻止把 relay 升级为递归边，不否定上述有限群结论。证毕。

## 5. 边界例子

### 非平凡 annihilator 商

取 \(H=C_5\oplus C_5\)，源集
\[
R\subseteq K=\{0\}\oplus C_5,
\qquad
\tau=(1,0).
\]
投影角色 \(\chi(x,y)=\exp(2\pi i x/5)\) 湮灭所有源列而分离目标，故
\(K=\ker\chi\)、\(H/K\simeq C_5\)，得到严格的有限商目标缺失；整数递降仍需
source-switch 标签提升。

### 顶层 primary

取 \(H=C_5\)、\(R=\{0\}\)、\(\tau=1\)。同一角色的核为 \(K=1\)，目标相位非平凡，
没有更小 annihilator 商，回执是 TOP_PRIMARY_ANNIHILATOR 而不是伪造的下降边。

### 目标相位平凡的子群 relay

取 \(H=C_2\oplus C_2\)、\(R=\{(0,0)\}\)、\(\tau=(0,1)\)，并令
\(\chi(x,y)=(-1)^x\)。则
\[
K=\{(0,0),(0,1)\},
\qquad
R\subseteq K,
\qquad
\tau\in K\setminus R.
\]
所以 \(\chi(\tau)=1\) 仍给出严格子群 \((K,R,\tau)\)，而不是停在纯关系
Fourier。是否能回译为整数递降，仍由提升门决定。

## 研究边界

该桥把 q 进层容量缺口推进为“阶 \(\ell\) 对偶—全源列闭包—annihilator
子群/商”的构造性链条。全源闭合后的两种目标相位均有严格有限群 relay；只有
提升门失败时才留下不收费的关系 Fourier 障碍。仍未证明每个实际缺口都满足
SOURCE-DOMINATING-CUT，也未自动提供子群/商的整数 source-switch 和 E1--E5
提升；这些仍是全局选择器的决定性条件。
