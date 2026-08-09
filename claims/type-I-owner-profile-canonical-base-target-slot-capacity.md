---
kind: claim
claim_id: type-I-owner-profile-canonical-base-target-slot-capacity
title: owner 剖面的规范共同源基、指定目标准入与相位槽容量
statement: >-
  固定奇素数 q、层 J、核心素数 p 和已经通过整数对偶范围门的有限 owner 剖面。
  正整数标签 s 若写成规范 Type II 源行 s=Da、a|D、D/a 平方自由，则 D 唯一等于
  prod_l l^ceil(v_l(s)/2)。固定 D 的全部规范源标签恰为
  D^2/c（c|rad(D)）；加入 owner 前缀与范围后得到有限槽集 U_J(D;p)。因此同一个
  整数剖面的全部记录具有共同规范源基，且在指定 x 已通过 owner prefix/range 后支持
  该除子格目标，当且仅当剖面格命中
  某个 U_J(D;p)^X，且 D_x|D；这是同一个有限见证的必要充分条件，而非
  D|gcd(endpoints) 的算术必要筛选。按 owner 的下一层数字分割 U_J(D;p) 后，非零
  横向边构成完全 q-部图，其不交匹配容量为
  min(floor(N/2),N-max_r n_r)；deep--shallow 边构成完全二部图，容量为
  min(n_delta,N-n_delta)。再加入 deep 且实际 q 类可保留的目标槽，匿名局部三部
  算术容量为三类槽数的最小值。所有结论均在 prescribed label、全局 occurrence、
  既定角色 SNF、E4 与全局 E5 之前。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-source-lattice-owner-window-affine-profile-admission
  - type-I-linear-escape-canonical-d-lattice-source-menu
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
topics:
  - type-I
  - type-II
  - source-lattice
  - owner-profile
  - canonical-source-base
  - divisor-lattice
  - prescribed-target
  - q-adic-height
  - matching-capacity
  - strict-obstruction
  - capacity-map
  - proof-program
sources:
  - claim: type-I-source-lattice-owner-window-affine-profile-admission
    role: intrinsic-integer-dual-owner-profile-lattice
  - claim: type-I-linear-escape-canonical-d-lattice-source-menu
    role: fixed-D-canonical-source-and-target-universe
  - claim: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
    role: square-target-menu-and-exclusive-next-layer-physical-boundary
  - reproduction: reproductions/type_i_owner_profile_canonical_base_target_slot_capacity.py
    role: focused-inverse-dictionary-joint-profile-target-and-capacity-controls
visibility: public
last_checked: '2026-08-10'
---

# owner 剖面的规范共同源基、指定目标准入与相位槽容量

## 1. 共同算术行基不等于共同规范源基

固定奇素数 \(q\nmid p\)、\(J\ge1\)，记

\[
Q=q^J,
\qquad
B_p=\left\lfloor\frac{p-1}{4}\right\rfloor,
\qquad
0<\beta_J<Q,
\qquad
p+4\beta_J\equiv0\pmod Q.
\tag{1}
\]

若 \(B_p<\beta_J\)，owner 窗口为空。以下假设

\[
M_J=\left\lfloor\frac{B_p-\beta_J}{Q}\right\rfloor\ge0.
\tag{2}
\]

对正整数 \(s\)，定义其唯一平方自由分解

\[
\boxed{
A_s=\prod_\ell\ell^{\lfloor v_\ell(s)/2\rfloor},
\qquad
D_s=\prod_\ell\ell^{\lceil v_\ell(s)/2\rceil},
\qquad
C_s=D_s/A_s.}
\tag{3}
\]

于是 \(s=A_sD_s=A_s^2C_s\)，且 \(C_s\) 平方自由。

**规范源基逆引理。** 对正整数 \(D,a,s\)，下列条件等价：

\[
s=Da,
\qquad
a\mid D,
\qquad
D/a\text{ 平方自由};
\tag{4}
\]

\[
\boxed{(D,a)=(D_s,A_s).}
\tag{5}
\]

**证明。** 对每个素数 \(\ell\)，写

\[
e=v_\ell(s),\qquad d=v_\ell(D),\qquad \alpha=v_\ell(a).
\]

式 (4) 给出 \(e=d+\alpha\) 以及 \(d-\alpha\in\{0,1\}\)，故

\[
d=\left\lceil\frac e2\right\rceil,
\qquad
\alpha=\left\lfloor\frac e2\right\rfloor.
\tag{6}
\]

这逐素数强制 (5)。反向代回 (3) 即得 (4)。证毕。

所以两个标签 \(s_0,s_1\) 具有同一个**规范**源基，当且仅当

\[
\boxed{D_{s_0}=D_{s_1};}
\tag{7}
\]

通过时共同基唯一。条件 \(D\mid\gcd(s_0,s_1)\) 只说明 \(D\) 是共同算术行基，
不能替代 (7)。

## 2. 固定 \(D\) 的平方自由除数槽字典

固定 \(D\ge1\)。令 \(c=D/a\)。由 (4)，\(c\) 恰为 \(D\) 的平方自由除数，故

\[
\boxed{
\mathcal S(D)
=\left\{\frac{D^2}{c}:c\mid\operatorname{rad}(D)\right\}.}
\tag{8}
\]

映射 \(c\mapsto D^2/c\) 为双射，所以未加物理条件时

\[
|\mathcal S(D)|=2^{\omega(D)}.
\tag{9}
\]

把 (8) 与真实 owner 窗口相交，定义平方自由参数槽及 owner 指标槽

\[
\mathcal C_J(D;p)
=\left\{
c\mid\operatorname{rad}(D):
\frac{D^2}{c}\le B_p,
\quad
\frac{D^2}{c}\equiv\beta_J\pmod Q
\right\},
\tag{10}
\]

\[
\boxed{
\mathcal U_J(D;p)
=\left\{
u_c=\frac{D^2/c-\beta_J}{Q}:
c\in\mathcal C_J(D;p)
\right\}
\subseteq\{0,\ldots,M_J\}.}
\tag{11}
\]

因为非空 owner 标签不被 \(q\) 整除，若 (10) 非空，则 \(q\nmid D\)，从而

\[
\boxed{
c\in\mathcal C_J(D;p)
\iff
\begin{cases}
c\mid\operatorname{rad}(D),\\
c\equiv D^2\beta_J^{-1}\pmod Q,\\
D^2/c\le B_p.
\end{cases}}
\tag{12}
\]

这把规范 source slots 化成一个平方自由除数残类问题。又因
\(D^2/c\ge D\)，任何非空槽基都满足

\[
\boxed{1\le D\le B_p.}
\tag{13}
\]

因此全部候选 \(D\) 有限。由逆引理，不同 \(D\) 的槽集在 owner 标签意义下互不相交。

## 3. 仿射 owner 剖面与指定目标的联合准入定理

令 \(X\) 是非空有限带基点源记录集，
\(\mathcal P_{J,X}\subseteq\mathbb Z^X\) 是
`type-I-source-lattice-owner-window-affine-profile-admission`
给出的内禀整数剖面仿射格。对 \(u\in[0,M_J]^X\)，写

\[
s_z(u)=\beta_J+Qu_z\qquad(z\in X).
\tag{14}
\]

对正整数指定目标 \(x\)，令 \((D_x,A_x,C_x)\) 由 (3) 给出，并先检查

\[
0<4x<p,
\qquad
x\equiv\beta_J\pmod Q.
\tag{15}
\]

定义有限联合准入集

\[
\boxed{
\mathfrak A_{J,X}(x)
=\mathcal P_{J,X}\cap
\bigcup_{\substack{1\le D\le B_p\\D_x\mid D}}
\mathcal U_J(D;p)^X.}
\tag{16}
\]

若 \(X=\{z_0,z_1\}\) 是一条非零横向边，则把
\(\mathcal U_J(D;p)^X\) 换成有序互异对

\[
\mathcal U_J(D;p)^{\underline 2}
=\{(u_0,u_1):u_i\in\mathcal U_J(D;p),\
u_0-u_1\not\equiv0\pmod q\}.
\tag{17}
\]

**联合准入定理。** 假设 (15) 成立。下列条件等价：

1. 存在同一个整数 \(q\)-height 对偶、同一个平移、一个正整数 \(D\) 以及
   \(a_z\mid D\)，使全部源记录同时满足
   
   \[
   s_z=Da_z,
   \qquad
   D/a_z\text{ 平方自由},
   \qquad
   0<4s_z<p,
   \qquad
   Q\mid p+4s_z,
   \tag{18}
   \]
   
   并且目标 \(x\) 属于这个 \(D\) 的 Type II 除子格菜单；
2. 存在 \(u\in\mathcal P_{J,X}\cap[0,M_J]^X\)，使所有
   \(D_{s_z(u)}\) 等于同一个 \(D\)，且 \(D_x\mid D\)；
3. 
   \[
   \boxed{\mathfrak A_{J,X}(x)\ne\varnothing.}
   \tag{19}
   \]

**证明。** owner 剖面定理把“同一个整数对偶与同一个平移”精确等价为
\(u\in\mathcal P_{J,X}\cap[0,M_J]^X\)。对每个坐标，逆引理把 (18) 的规范
源基唯一强制为 \(D_{s_z(u)}\)；所以全部记录共享规范源基恰为这些 \(D_{s_z(u)}\)
相等，也恰为 \(u\in\mathcal U_J(D;p)^X\)。

另一方面，固定共同源基 \(D\) 后，目标 \(x\) 的唯一规范参数满足

\[
\boxed{D_x\mid D\iff x\mid D^2.}
\tag{20}
\]

这正是固定 \(D\) 除子格目标菜单的充要条件。结合 (13) 即得 (16)--(19)。证毕。

没有指定目标时，删除 (16) 中的条件 \(D_x\mid D\)，便得到共同规范源基的精确
准入集。若 (15) 失败，先返回 `PRESCRIBED_TARGET_OWNER_PREFIX_OR_RANGE_OBSTRUCTED`。
若共同规范源基联合为空，返回
`CANONICAL_COMMON_SOURCE_BASE_PROFILE_EMPTY`；若共同基存在但 (16) 为空，返回
`PRESCRIBED_TARGET_CANONICAL_BASE_PROFILE_EMPTY`。

这是一个完全有限的严格判定：枚举 \(1\le D\le B_p\) 的槽元组，再用上一张卡的同一
Smith 系统检查元组是否属于 \(\mathcal P_{J,X}\)。空集时，对每个 \(D\) 保存槽字典
为空、target 整除失败或候选元组首个 Smith 失败行中的相应原因。该证书对声明的
profile--\(D\)-格 universe 是严格 iff，但候选数最坏不受统一常数控制，因而还不是
最终猜想所需的统一短证书。

## 4. 相位数字给出的闭式 source-slot 容量

固定 \(D\) 并简写

\[
\mathcal U=\mathcal U_J(D;p),
\qquad
\mathcal U_r=\{u\in\mathcal U:u\equiv r\pmod q\},
\qquad
n_r=|\mathcal U_r|,
\qquad
N=|\mathcal U|.
\tag{21}
\]

由 (11)，还可直接按平方自由除数计数：

\[
n_r=
\#\left\{
c\mid\operatorname{rad}(D):
D^2/c\le B_p,
\quad
D^2/c\equiv\beta_J+Qr\pmod{qQ}
\right\}.
\tag{22}
\]

两个槽给出非零横向 \(\mathbb F_q\) 数字，当且仅当它们属于不同的
\(\mathcal U_r\)。所以全部匿名非零 source pairs 构成完全 \(q\)-部图。单位
source-slot 容量下，其最大不交匹配数精确为

\[
\boxed{
\nu_{\rm tr}(D)
=\min\left\{\left\lfloor\frac N2\right\rfloor,
N-\max_r n_r\right\}.}
\tag{23}
\]

证明只需注意两个上界：每条边使用两个槽，且每条边至少使用一个最大部之外的槽。
若最大部大小至少 \(N/2\)，把每个外部槽配给不同的最大部槽，达到 \(N-\max n_r\)；
否则反复配对当前两个最大非空部，直到只剩至多一个槽，达到
\(\lfloor N/2\rfloor\)。

令

\[
0<\beta_{J+1}<qQ,
\qquad
\delta_J=\frac{\beta_{J+1}-\beta_J}{Q}
\in\{0,\ldots,q-1\}.
\tag{24}
\]

槽 \(u\) 深入 \(J+1\) 层当且仅当 \(u\equiv\delta_J\pmod q\)。因此

\[
n_{\rm deep}=n_{\delta_J},
\qquad
n_{\rm shallow}=N-n_{\delta_J},
\tag{25}
\]

而 exclusive-next-layer source-pair 图严格为
\(K_{n_{\rm deep},n_{\rm shallow}}\)。故候选边数与不交匹配容量分别为

\[
\boxed{
E_{\rm ex}(D)=n_{\rm deep}n_{\rm shallow},
\qquad
\nu_{\rm ex}(D)=\min(n_{\rm deep},n_{\rm shallow}).}
\tag{26}
\]

若一组带名请求只固定定向数字
\(c_i=u_{\rm shallow}-u_{\rm deep}\in\mathbb F_q^\times\)，而没有其它耦合标签，令
\(R_c=\#\{i:c_i=c\}\)。存在 source-slot 不相交分配当且仅当

\[
\boxed{
\sum_{c\ne0}R_c\le n_{\delta_J},
\qquad
R_c\le n_{\delta_J+c}\quad(c\ne0).}
\tag{27}
\]

式 (27) 的下标按模 \(q\) 解释。必要性显然；充分性分别在每个 shallow 数字部内
注入，再把全部请求注入 deep 部。
若 profile、prescribed label 或 target 条件把某些 deep--shallow 组合耦合删除，
(27) 不再是充分条件，必须在实际有限边图或三部超图上运行匹配；不能只检查两个投影
Hall 条件。

## 5. deep target 槽与局部三部算术容量

对固定 \(D\)，定义可自由选择角色的 deep target 槽

\[
\boxed{
\mathcal T_{J+1}^{\rm sel}(D;p)
=\left\{
x:x\mid D^2,
\ 0<4x<p,
\ x\equiv\beta_{J+1}\pmod{qQ},
\ q\nmid D_x,
\ q\mid\operatorname{ord}_{4D_x}(q)
\right\}.}
\tag{28}
\]

若 \(\mathcal U\ne\varnothing\)，则 \(q\nmid D\)，故 (28) 中的乘法阶都有定义。
任取

\[
u_d\in\mathcal U_{\delta_J},
\qquad
u_s\in\mathcal U\setminus\mathcal U_{\delta_J},
\qquad
x\in\mathcal T_{J+1}^{\rm sel}(D;p).
\tag{29}
\]

对应的两个 source labels 是同一规范 \(D\) 下的一深一浅 source row；目标满足
\(D_x\mid D\)，继承第 \(J+1\) 层，且实际整数类 \(q\) 在某个可自由选择的
\(q\)-primary 角色中非零。因此 (29) 是现有 next-layer 定理的完整**局部算术候选**。
没有额外带名约束时，候选三元组形成完全三部三一致超图。

写 \(t_D=|\mathcal T_{J+1}^{\rm sel}(D;p)|\)。把 source-deep、source-shallow 和
target 看成三个带类型、单位容量的局部槽，则

\[
\boxed{
E_{\rm arith}(D)=n_{\rm deep}n_{\rm shallow}t_D,
\qquad
\nu_{\rm arith}(D)
=\min(n_{\rm deep},n_{\rm shallow},t_D).}
\tag{30}
\]

式 (30) 是算术供给容量，不是全局 physical assignment 容量。对一个固定 prescribed
target \(x\)，即使有 \(n_{\rm deep}n_{\rm shallow}\) 条候选 source edge，同一个
target occurrence key 仍只能收费一次。实际 F/G 请求还必须命中 (16) 的 profile
边、通过 prescribed-role SNF，并检查 source/target state-id 的全局 occurrence；
这些删除可把 (30) 降低。

## 6. 三个严格控制

### 6.1 \(p=97\)：共同 gcd 基的严格假阳性

取 \(q=3,J=1,L=\mathbb Z,\gamma(1)=1,X=\{0,4\}\)。这里

\[
\beta_1=2,
\qquad
M_1=7,
\qquad
\mathcal Y_1=1+3\mathbb Z.
\tag{31}
\]

窗口内全部剖面恰为

\[
(0,4),(1,5),(2,6),(3,7),
\tag{32}
\]

对应标签对

\[
(2,14),(5,17),(8,20),(11,23).
\tag{33}
\]

每一对的两个规范基都不同，所以共同规范源基联合为空。特别地，第三对满足

\[
\gcd(8,20)=\gcd(8,6-2)=4,
\tag{34}
\]

故 \(D_0=4\) 是非平凡共同算术行基；但

\[
D_8=4,
\qquad
D_{20}=10.
\tag{35}
\]

在 \(D_0=4\) 下，第二行会要求 \(a=5\nmid4\)。因此该完整 profile 输出
`CANONICAL_COMMON_SOURCE_BASE_PROFILE_EMPTY`，严格反驳
“取 \(D_0\mid\gcd(endpoints)\) 就已经得到共同 canonical source state”。

### 6.2 \(p=2113\)：profile、共同基与指定 target 的唯一联合正例

取 \(q=3,J=1,L=\mathbb Z,\gamma(1)=1,X=\{0,70\}\)。此时

\[
\beta_1=2,
\qquad
M_1=175,
\qquad
\delta_1=1.
\tag{36}
\]

所有范围可行剖面中，只有以下两个剖面具有共同规范源基：

\[
\begin{array}{c|c|c|c}
D&u&(s_0,s_1)&(u_0,u_1)\bmod3\\ \hline
35&(11,81)&(35,245)&(2,0)\\
70&(46,116)&(140,350)&(1,2).
\end{array}
\tag{37}
\]

指定 \(x=14\) 时 \(D_x=14\)，所以 \(14\nmid35\) 而 \(14\mid70\)。于是 (16)
只剩

\[
\boxed{D=70,\qquad u=(46,116),\qquad(s_0,s_1)=(140,350).}
\tag{38}
\]

其中第一槽 deep、第二槽 shallow；目标 \(14\equiv5\pmod9\)，且

\[
\operatorname{ord}_{56}(3)=6.
\tag{39}
\]

因此它通过联合 profile--canonical-base--prescribed-target 的局部算术门。
若改指定 \(x=65\)，则 \(D_x=65\) 不整除 35 或 70，联合为空，严格输出
`PRESCRIBED_TARGET_CANONICAL_BASE_PROFILE_EMPTY`。

### 6.3 \(D=70\) 的局部容量

同一 \(p,q,J,D\) 下，固定基槽只有

\[
\mathcal U_1(70;2113)=\{46,116\},
\qquad
(n_0,n_1,n_2)=(0,1,1).
\tag{40}
\]

所以

\[
\nu_{\rm tr}=1,
\qquad
\nu_{\rm ex}=1.
\tag{41}
\]

满足 (28) 的 deep selectable targets 恰为

\[
\mathcal T_2^{\rm sel}(70;2113)=\{14,140\},
\tag{42}
\]

其乘法阶分别为 6 和 12。故 \(t_{70}=2\)，候选算术三元组数为 2，而 typed
不交局部容量仍为

\[
\nu_{\rm arith}=\min(1,1,2)=1.
\tag{43}
\]

这区分了“菜单里有两个 target”与“同一对 source slots 能支付两个独立请求”。

## 7. 统一选择器分派

对已经通过 owner profile 范围门的有限源请求，新增精确分派：

~~~text
OWNER_WINDOW_AFFINE_DUAL_PROFILE_READY(P_J,X)
  prescribed target x exists and fails owner prefix/range:
    PRESCRIBED_TARGET_OWNER_PREFIX_OR_RANGE_OBSTRUCTED
  otherwise:
    enumerate canonical slot dictionaries U_J(D;p), 1 <= D <= B_p
    P_J,X misses every U_J(D;p)^X:
      CANONICAL_COMMON_SOURCE_BASE_PROFILE_EMPTY
    otherwise:
      CANONICAL_COMMON_SOURCE_BASE_PROFILE_READY(u,D)
      no prescribed target:
        emit exact phase counts n_r and transverse/deep-shallow capacities
      prescribed target passes prefix/range but D_x divides no surviving D:
        PRESCRIBED_TARGET_CANONICAL_BASE_PROFILE_EMPTY
      otherwise:
        CANONICAL_PROFILE_PRESCRIBED_TARGET_READY(u,D,x)
        no selected named two-point edge:
          emit the joint tuple and build the finite coupled edge graph
        selected named edge e=(z0,z1) with nonzero phase:
          source pair has no deep-shallow split:
            CANONICAL_NEXT_LAYER_SOURCE_SLOT_DEFICIT
          target not deep:
            EDGE_NEXT_LAYER_TARGET_QJ1_CRT_OBSTRUCTED
          q does not divide ord_{4D_x}(q):
            TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO
          otherwise:
            CANONICAL_PROFILE_NEXT_LAYER_ARITHMETIC_READY
            intersect prescribed role/label and global occurrence keys
            run the actual finite matching or Rado gate
            E4 and full marked E5 remain separate
~~~

现有 fixed-endpoint 非相邻定理仍保留“共同算术行基 \(D\mid\gcd\)”的广义分支；
本卡只在调用者声称 endpoints 属于同一 canonical Type II source fiber 时强制更严格的
(16)。两种 `D` 语义不得混名。

## 8. 研究边界

本卡把 profile 范围、共同 canonical source base、指定 target 与匿名相位槽容量合成了
同一个有限见证，并消除了 gcd-base 假阳性。它仍没有证明每个真实 F/G profile 都命中
某个 \(D\)，也没有把联合空集自动转成另一个 Type I/II 终端或良基下降。

下一决定性缺口现在更窄：对真实带名请求，把 (16) 的 surviving tuples 与 prescribed
角色、全局 occurrence 和 source-switch state 同时相交；若实际耦合超图没有匹配，
必须从该严格缺口构造完整 kernel source box、直接 Type I/II 证书或不可重置的 marked
良基下降，而不能再用匿名容量 (23)、(26) 或 (30) 代替。

当 target state-id 与整数目标均已由请求固定时，先在 source/target 共享 occurrence
ledger 上预收费 target；同一 edge 的 \(d=t(r)\) 映为私有零增量 atom，其它 deep
使用残余容量。source 侧仍保留 incremental-deep--shallow--independent-column 耦合。
只有请求角色方向本身独立且该耦合严格矩形化时，才进一步收缩为两组 capacitated
Hall 加一组 Rado；相关角色带不同物理义务、target 或 source 组合随候选变化时保留
一般耦合超图。详见
[指定 target occurrence 的先验割、矩形 Hall--Rado 收缩与耦合反例](type-I-prescribed-target-occurrence-rado-contraction.md)。

## 聚焦验证

~~~bash
python3 \
  reproductions/type_i_owner_profile_canonical_base_target_slot_capacity.py \
  --verify
~~~

验证器只重算规范逆字典、两个有限 profile 联合、\(D=70\) 的相位/target 槽和闭式
容量；不运行历史扫描。
