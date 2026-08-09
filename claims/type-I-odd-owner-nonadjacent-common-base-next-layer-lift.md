---
kind: claim
claim_id: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
title: 非相邻 owner 的共同基平方菜单、余因子碰撞与下一层物理 q-toggle
statement: >-
  固定奇素数 q、j>=1、核心素数 p 和一条非零 q^j-owner 边
  s_m=beta_j+mq^j、s_n=beta_j+nq^j。令 k=n-m。其最大共同算术行基为
  gcd(s_m,s_n)=gcd(s_m,k)，而固定共同基 D_0 的全部 Type II 除子格目标与
  x|D_0^2 一一对应；exact-q^j 目标菜单恰为 4x<p 且
  x=beta_j (mod q^j) 的这些除数。任意目标 D_*|D_0 都使 q^j-约化余因子在
  U(4D_*) 中完全碰撞，所以 endpoint-cofactor residue 不能承载非零横向源列。
  共同 q^j 前缀本身同样不能区分边；但若两端恰有一端进入 q^(j+1)，目标 x 也继承
  该端的 q^(j+1)，则相对公共前缀的独占下一层给出真实二点因子块 {1,q}。对已经
  provenance-qualified 且全局物理 occurrence 尚未收费的单边，这一块关闭 physical
  source-class E1；存在一个可自由选择且不杀掉实际 q 类的循环 q-primary 角色当且仅当
  q 整除 ord_{4D_*}(q)，既定 J/eta 仍需联合 SNF 门。仅有 q|phi(4D_*) 不充分。
  D_*<D_0 只产生局部 strict-relay candidate；在 D_0 不是已实现
  递归势或缺少 marked-solution lift 时不得登记 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-owner-fiber-incidence-lattice-source-map
  - type-I-odd-owner-incidence-edge-source-preserving-capacity
  - type-II-source-fiber-shared-q-ledger
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-owner-primary-mask-arithmetic-lift-criterion
topics:
  - type-I
  - type-II
  - odd-owner
  - nonadjacent-edge
  - fixed-source-base
  - source-CRT
  - q-adic-height
  - factor-toggle
  - source-rank
  - strict-obstruction
  - capacity-map
  - proof-program
sources:
  - claim: type-I-odd-owner-fiber-incidence-lattice-source-map
    role: owner-incidence-SNF-and-cofactor-realization
  - claim: type-I-odd-owner-incidence-edge-source-preserving-capacity
    role: provenance-qualified-edge-and-normalized-source-column
  - claim: type-II-source-fiber-shared-q-ledger
    role: shared-q-layer-deduplication
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: physical-q-direction-to-elementary-rank
  - claim: type-II-owner-primary-mask-arithmetic-lift-criterion
    role: E1-E5-boundary
  - reproduction: reproductions/type_i_odd_owner_nonadjacent_common_base_next_layer_lift.py
    role: exact-menu-universal-templates-arithmetic-gates-and-occurrence-assignment-controls
visibility: public
last_checked: '2026-08-10'
---

# 非相邻 owner 的共同基平方菜单、余因子碰撞与下一层物理 \(q\)-toggle

## 1. 非相邻边的最大共同基

固定奇素数 \(q\nmid p\)、\(j\ge1\)，记

\[
Q=q^j,
\qquad
s_r=\beta_j(p)+Qr,
\qquad
q^j\mid p+4s_r.
\tag{1}
\]

取 \(m<n\)，令 \(k=n-m\)，并假设该边横向非零：

\[
q\nmid k.
\tag{2}
\]

由 \(q\nmid s_m\)，有 \(\gcd(s_m,Q)=1\)，所以

\[
\boxed{
g:=\gcd(s_m,s_n)
=\gcd(s_m,Qk)
=\gcd(s_m,k).}
\tag{3}
\]

因此所有共同算术行基恰为 \(D_0\mid g\)。写

\[
s_m=D_0a,
\qquad
k=D_0t,
\tag{4}
\]

则

\[
s_n=D_0(a+Qt),
\qquad
g=D_0\gcd(a,t).
\tag{5}
\]

特别地，\(D_0=g\) 当且仅当 \(\gcd(a,t)=1\)。又因 \(q\nmid s_m\)，有
\(q\nmid D_0\)；由 (2) 还得到 \(q\nmid t\)。相邻边是 \(k=1\) 的特例，因而
强制 \(D_0=1\)；一般非相邻边的新增自由度完全由 \(k\) 的非 \(q\) 因子提供。

## 2. 共同基目标的平方除子参数化

固定一个共同基 \(D_0\)。Type II 除子格目标满足

\[
D_*\mid D_0,
\qquad
A\mid D_*,
\qquad
D_*/A\text{ 平方自由},
\qquad
x=AD_*.
\tag{6}
\]

这些目标与 \(D_0^2\) 的正除数一一对应。若

\[
x=\prod_\ell \ell^{e_\ell},
\tag{7}
\]

唯一反解为

\[
\boxed{
A_x=\prod_\ell\ell^{\lfloor e_\ell/2\rfloor},
\qquad
D_x=\prod_\ell\ell^{\lceil e_\ell/2\rceil},
\qquad
C_x=D_x/A_x.}
\tag{8}
\]

确实，\(D_x/A_x\) 的每个素数指数为 \(0\) 或 \(1\)，且
\(D_x\mid D_0\) 等价于 \(x\mid D_0^2\)。反向由 \(x=AD_*\) 逐素数比较指数即回到
(8)。所以 exact-\(Q\) 共同基菜单不是开放搜索，而是有限集合

\[
\boxed{
\mathscr X_Q(D_0;p)
=\{x:x\mid D_0^2,\ 4x<p,\ x\equiv\beta_j(p)\pmod Q\}.}
\tag{9}
\]

对 \(x\in\mathscr X_Q\)，式 (8) 给出唯一 \((D_*,A,C)\)，而

\[
Q\mid p+4x
\tag{10}
\]

正是两个 source row 的 exact-\(Q\) E2 合同。若 (9) 为空，得到完整共同基菜单上的
`NONADJACENT_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED`。

因为 \(q\nmid D_*\)，目标单位群含抽象 \(q\)-primary 部分当且仅当

\[
\boxed{
q\mid\varphi(4D_*)
\iff
\exists\text{ prime }r\mid D_*:\ r\equiv1\pmod q.}
\tag{11}
\]

这样的 \(r\) 还满足 \(r\mid D_0\mid k\)。由于 \(q\) 为奇数，素数
\(r=1+cq\) 的 \(c\) 不能为奇数，故

\[
\boxed{k\ge r\ge2q+1.}
\tag{12}
\]

所以短于 \(2q+1\) 个横向步长的非相邻边仍不可能拥有这种目标奇阶环境。但 (11)
只说明环境里某处有 \(q\)-torsion；它尚未说明实际物理因子 \(q\) 落在该方向。

## 3. endpoint 余因子在每个共同基目标中严格碰撞

定义真实 \(Q\)-约化余因子

\[
N_r=\frac{p+4s_r}{Q}.
\tag{13}
\]

由 (1) 有

\[
N_n-N_m=4k.
\tag{14}
\]

式 (3) 给出 \(D_0\mid k\)，所以对任意 \(D_*\mid D_0\)，

\[
\boxed{N_n\equiv N_m\pmod {4D_*}.}
\tag{15}
\]

两个余因子实际都属于 \(U(4D_*)\)。它们是奇数；若素数
\(\ell\mid D_*\) 也整除 \(N_r\)，则由 \(\ell\mid s_r\)、\(\ell\nmid Q\) 和
\(QN_r=p+4s_r\) 得到 \(\ell\mid p\)。但 \(\ell\le D_*\le s_r<p/4\)，不可能
等于素数 \(p\)。因此

\[
\boxed{[N_m]=[N_n]\quad\text{in }U(4D_*).}
\tag{16}
\]

关联格中的整数差 \(N_n-N_m\) 模 \(q\) 可以非零，但它在所有共同基目标单位群中
都被 (16) 杀掉。于是任何只依赖 endpoint cofactor residue、其比值或其角色值的
直接 lift 均为零：

~~~text
NONADJACENT_COMMON_BASE_COFACTOR_RESIDUE_COLLISION
  incidence_source_column = nonzero in F_q
  endpoint_cofactor_ratio = 1 in U(4D_*)
~~~

这关闭了最自然的 cofactor lift；它不排除带不同物理 lineage 的因子层。

## 4. 公共前缀不能收费，独占下一层可以

对端点及目标定义下一层指标

\[
\epsilon_r=\mathbf 1_{q^{j+1}\mid p+4s_r},
\qquad
\epsilon_x=\mathbf 1_{q^{j+1}\mid p+4x}.
\tag{17}
\]

由 (2)，两个端点不可能同时深入。否则相减得到

\[
q^{j+1}\mid4Qk,
\]

从而 \(q\mid k\)，矛盾。因此

\[
\boxed{\epsilon_m+\epsilon_n\le1.}
\tag{18}
\]

exact-\(Q\) 只给两个端点和目标共同的前 \(j\) 个 \(q\) 层。这些层在 edge 上是常量，
不能区分两个记录；把规范 incidence 列事后配给其中一个公共层不构成 E1。

现在假设

\[
\boxed{
\epsilon_m+\epsilon_n=1,
\qquad
\epsilon_x=1.}
\tag{19}
\]

令 \(s_+\) 为唯一 deep endpoint。第二个条件等价于

\[
x\equiv s_+\pmod {q^{j+1}}.
\tag{20}
\]

在 source 端，shallow 与 deep 记录分别拥有合法因子 \(q^j\) 与 \(q^{j+1}\)；在
target 端这两个因子也都整除 \(p+4x\)。约去公共的 \(q^j\) 锚点，得到真实二点块

\[
\boxed{B_{\Pi,x}^{j+1}=\{1,q\}.}
\tag{21}
\]

选与不选独占层都回译为实际整数因子，且层 \(j+1\) 只由 deep endpoint 提供，不会
在 shared-\(q\) 账本中双计费。若原边 \(\Pi\) 已经通过带名记录和整数规则的
provenance 门，并且 source 与 target 上这一 \(j+1\) 层尚未被其它 token 收费，则
把唯一规范 edge token 送到两个**不含 \(\Pi\)** 的全局 occurrence key

\[
\begin{aligned}
\kappa_{\rm src}&=(\text{source-state-id},s_+,q,j+1),\\
\kappa_{\rm tgt}&=(\text{target-state-id},x,q,j+1),
\end{aligned}
\tag{22}
\]

并登记内容寻址的

~~~text
assignment_id = hash(Pi, kappa_src, kappa_tgt)
claimed_by = Pi
~~~

从而给出单射、前缀闭合且 source-preserving 的单请求 owner map。完全相同的
`assignment_id` 重放只返回旧回执，不新增容量；除此以外，只要任一 key 已占用，就必须
返回 `PHYSICAL_Q_LAYER_ASSIGNMENT_CAPACITY_OBSTRUCTED`。因此改变边名或让同一边改投
另一目标都不能重复收费。edge 的非零横向列与
\(\epsilon_+-\epsilon_-=1\) 之间只差一个非零 \(\mathbb F_q\) 标量，故可按既有规范化
同时化为列 \(1\)。这正是此前缺失的 physical source-class E1：

~~~text
NEXT_LAYER_EXCLUSIVE_Q_FACTOR_TOGGLE
  common_prefix_layers = 1..j (not charged as edge rank)
  exclusive_layer = j+1
  physical_block = {1,q}
  source_relation_scope = one qualified edge
  occurrence_key = (state-id, value, q, j+1)
  assignment_id = hash(Pi, source-key, target-key)
  claimed_by = Pi
  physical_slot_capacity = 1
~~~

若 (18) 两端均为零，输出 `EDGE_NEXT_LAYER_SOURCE_CLASS_UNSEPARATED`；若有 deep
endpoint 但 \(\epsilon_x=0\)，输出
`EDGE_NEXT_LAYER_TARGET_QJ1_CRT_OBSTRUCTED`。这两个回执只否定当前直接下一层
factor-toggle，不否定更深层、其它素数或异质 source-map。

## 5. 实际因子方向的精确 Fourier/rank 门

令

\[
G_*=U(4D_*),
\qquad
u=[q]\in G_*,
\qquad
H_q=\langle u\rangle.
\tag{23}
\]

物理块 (21) 在 \(q\)-初等商中的列为

\[
uH_q^q\in H_q/H_q^q.
\tag{24}
\]

因为 \(H_q\) 是阶 \(o=\operatorname{ord}_{4D_*}(q)\) 的循环群，

\[
\boxed{
H_q/H_q^q\simeq C_q
\iff q\mid o.}
\tag{25}
\]

这也是存在某个循环 \(q\)-primary 角色环境 \(J\) 及同态
\(\eta:G_*\twoheadrightarrow J\)，使 \(\eta(q)\) 恰有阶 \(q\) 的充要条件。正向证明是：
先在 \(H_q\) 上定义 \(u\mapsto\zeta_q\)；有限阿贝尔群子群上的复角色可延拓到
\(G_*\)，再取延拓角色的 \(q\)-primary 部分。反向由元素阶整除像前元素阶立即得到。

因此 (19) 与 (25) 合并给出

\[
\boxed{
\text{qualified incidence }C_q
\longrightarrow
\text{physical next-layer factor block}
\longrightarrow
\text{nonzero target }q\text{-source rank in some selectable role}.}
\tag{26}
\]

仅有 (11) 不够：目标群可能含一个与整数 \(q\) 类无关的抽象 \(q\)-方向。若
\(q\nmid\operatorname{ord}_{4D_*}(q)\)，输出
`TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO`。

还有一个不可混淆的边界。若强制 \(J=C_q\)，存在
\(G_*\to C_q\) 且不杀掉 \(u\) 的充要条件是

\[
u\notin G_*^q.
\tag{27}
\]

它比 (25) 强；当 \(u\in G_*^q\) 时，更高阶循环 \(q\)-primary 角色仍可能把
\(u\) 映到阶 \(q\) 元素。若选择器已经固定了特定 \(J\)、锚点和其它因子标签，仍须
运行完整 SNF/\(\eta\) 门，不能用存在性的 (25) 覆盖既定标签。
例如在 (U(584)) 中，

\[
\operatorname{ord}_{584}(3)=12,
\qquad
67^3\equiv3\pmod {584}.
\tag{27a}
\]

所以 (25) 通过而 (3\in U(584)^3\)，直接 (C_3) 商必须杀掉类 (3)；只有选择
更高阶 3-primary 角色环境时，才可能保留其阶 3 像。

## 6. 三个聚焦控制

### 6.1 \(p=2113\)：独占第二层给出物理 rank-one 准备正控制

取 \(q=3,j=1\)。因 \(p\equiv1\pmod{24}\)，有 \(\beta_1=2\)。令

\[
(s_m,s_n)=(140,350),
\qquad
(m,n)=(46,116),
\qquad
D_0=70.
\tag{28}
\]

两行分别是 \(A=2,5\)，且

\[
70/2=35,
\qquad
70/5=14
\]

均平方自由，所以它们是同一 \(D_0\) 下的 canonical source rows。取

\[
(D_*,A,C,x)=(14,1,14,14).
\tag{29}
\]

有

\[
\begin{aligned}
p+4s_m&=2673=3^5\cdot11,\\
p+4s_n&=3513=3\cdot1171,\\
p+4x&=2169=3^2\cdot241.
\end{aligned}
\tag{30}
\]

所以 \(s_m\) 是唯一 deep endpoint，且目标继承第二层。另一方面

\[
\operatorname{ord}_{56}(3)=6,
\tag{31}
\]

故存在一个可自由选择的 3-primary 角色，使 (25) 的 3-rank 为 1。显式
\(\eta:U(56)\to C_3\) 可先约化到
\(U(7)\)，再把 \(3^e\) 送到 \(e\bmod3\)；它满足 \(\eta(3)=1\)、
\(\eta(-1)=0\)。

余因子路线仍严格碰撞：

\[
891\equiv1171\equiv723\equiv51\pmod {56}.
\tag{32}
\]

同时 \(p+4=2117=29\cdot73\) 的 \(D=1\) 单因子菜单为空，\(2169\) 的全部除数也
没有 \(-1\pmod {56}\)；所以该局部控制不是被同一块的 E4 命中伪装出来的。对任何
已经通过 provenance 且 source/target occurrence 均未收费的这条边，它建立 E1--E3
的 physical rank-one bridge；纯算术控制本身只标为
`ARITHMETIC_NEXT_LAYER_LIFT_READY`。虽然 \(14<70\)，没有外层权威状态和 marked lift 时仍只标为
`OWNER_MASK_STRICT_SOURCE_SWITCH_CANDIDATE`。

### 6.2 \(p=1489\)：目标未继承独占层

使用同一 \((s_m,s_n,D_0,D_*,A,x)=(140,350,70,14,1,14)\)。此时

\[
2049=3\cdot683,
\qquad
2889=3^3\cdot107,
\qquad
1545=3\cdot5\cdot103.
\tag{33}
\]

deep endpoint 是 \(350\)，但目标 \(x=14\) 只有第一层。虽然
\(\operatorname{ord}_{56}(3)=6\)，仍必须在 group-map 之前返回
`EDGE_NEXT_LAYER_TARGET_QJ1_CRT_OBSTRUCTED`。公共第一层不能替代独占下一层来源。

### 6.3 \(p=2113\)：ambient torsion 不等于物理 \(q\) 方向

另取

\[
(s_m,s_n)=(122,488),
\qquad
D_0=D_*=122,
\qquad
A=1,
\qquad
x=122.
\tag{34}
\]

这里 target/左端具有第二个 3 层，右端只有第一层，故 physical block (21) 存在。
目标群阶为

\[
\varphi(488)=240,
\qquad
3\mid240,
\tag{35}
\]

但实际整数类满足

\[
\operatorname{ord}_{488}(3)=10.
\tag{36}
\]

所以所有 3-primary 角色都杀掉物理 factor \(3\)，输出
`TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO`。这严格反驳了
“\(q\mid\varphi(4D_*)\) 加 extra layer 就足以支付 source rank”。

## 7. 所有充分大核心素数上的固定算术载体模板

上述正控制不是孤立数值。对任意核心素数 \(p\equiv1\pmod {24}\)、\(p>2600\)，
按 \(p\pmod9\) 选择：

\[
\begin{array}{c|c|c|c|c|c}
p\bmod9&D_0&(a_0,a_1)&(s_0,s_1)&(D_*,A,x)&
\operatorname{ord}_{4D_*}(3)\\ \hline
7&70&(2,5)&(140,350)&(14,1,14)&6\\
4&70&(2,5)&(140,350)&(14,7,98)&6\\
1&130&(2,5)&(260,650)&(65,1,65)&12
\end{array}
\tag{37}
\]

每行都有：

1. 两个 source rows 满足 \(a_i\mid D_0\)、\(D_0/a_i\) 平方自由；
2. \(s_i\equiv x\equiv2\pmod3\)，且范围由 \(4\cdot650<p\) 保证；
3. 表中与 \(x\) 同余模 9 的 endpoint 唯一进入第二个 3 层，另一个 endpoint
   精确只有第一层，target 也进入第二层；
4. \(D_*<D_0\)，且存在一个可自由选择的目标 3-primary 角色，使实际 factor
   \(3\) 的像秩为 1。

所以全部充分大核心素数都有一个**常数大小、canonical、严格降参数的
next-layer physical carrier skeleton**。这不是猜想的全称闭合：该模板尚未证明任意
terminal-first 未决 F/G 请求都能以带名整数来源映到这两个固定 source rows，也没有
给出跨状态 marked-solution lift。它把决定性缺口从“是否存在算术 q-carrier”收紧为
“如何把实际 F/G source relation source-preserving 地准入该固定 carrier，并把局部
\(D_*<D_0\) 升级为全局良基 E5”。

## 8. 选择器分派

对来源合格的非相邻 edge，新增分派为

~~~text
terminal-first precheck
  -> common source base D0 | gcd(endpoints)
  -> exact target menu X_Q(D0;p)
       -> empty: NONADJACENT_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED
       -> candidate x=(D_*,A):
            endpoint cofactor residues collide in U(4D_*)
            -> no unique deep endpoint:
                 EDGE_NEXT_LAYER_SOURCE_CLASS_UNSEPARATED
            -> unique deep endpoint, target not deep:
                 EDGE_NEXT_LAYER_TARGET_QJ1_CRT_OBSTRUCTED
            -> target inherits exclusive layer:
                 ARITHMETIC_NEXT_LAYER_LIFT_READY: physical {1,q}
                 -> edge provenance absent:
                      INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED
                 -> source/target occurrence already claimed:
                      PHYSICAL_Q_LAYER_ASSIGNMENT_CAPACITY_OBSTRUCTED
                 -> qualified edge and both occurrence keys free:
                      NEXT_LAYER_PHYSICAL_SOURCE_CLASS_LIFT_VERIFIED
                      edge/source/slot rank = 1
                      -> q does not divide ord_{4D_*}(q):
                           TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO
                      -> q divides ord_{4D_*}(q):
                           FREELY_SELECTABLE_Q_PRIMARY_ROLE_EXISTS
                           prescribed J/anchor/labels -> joint SNF/eta gate
                      E4 target test remains separate
                      D_* < D0: STRICT_SOURCE_SWITCH_CANDIDATE
                      verified E5 only after realized-state and marked-lift gates
~~~

该定理首次为一类非相邻 odd-owner 边给出 arithmetic-ready 块，并在 provenance 与
全局 occurrence 分配门通过时构造实际 physical source-class token，同时严格
说明公共前缀、cofactor residue、ambient torsion 和全局 E5 各自不足在哪里。它没有
提高横向载体的总秩：同一 \((p,q,j)\) 仍只有一个独立方向，不能把多个 exclusive
edge 重复收费。

后续[奇素数 source 匹配的仿射载体、显式核 Fourier 与良基递降边界](type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary.md)
已把本节的固定 \(q=3\) skeleton 推广到任意奇 source prime，并给出 fixed-row affine
content 的充要门与 content-adaptive 修复。它同时证明单个 \(\{1,q\}\) 块的稳定子
平凡，故这里的 \(D_*<D_0\) 不能直接走 kernel-saturated 降模；未固定额外标签时，
失败后可构造显式 kernel Fourier 角色，预设标签则仍需联合 SNF。全局剩余已经收紧为
自适应范围/target-state 出口或完整核来源盒，
而不是继续增加固定数值模板。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_odd_owner_nonadjacent_common_base_next_layer_lift.py --verify
~~~

验证器只重算平方除子菜单、三个固定载体模板、\(p=2113/1489\) 的 next-layer 分派、
cofactor 碰撞、实际 factor-order 门和跨边 occurrence 冲突；它不伪造 F/G provenance，
也不运行历史扫描。
