---
kind: claim
claim_id: type-I-source-lattice-qheight-dual-valuation-shift-carrier
title: 源格角色的最小 q 层对偶与 content 估值移位载体
statement: >-
  设 L 是 Z^d 的源关系子格，gamma:L->F_q 是奇素数 q 上的非零角色。层 J 的整数
  q-height 对偶向量存在，当且仅当 gamma 在 L 与 q^(J+1)Z^d 的交上恒零；失败交点
  本身是严格阻碍见证。由此得到有限、可由 Smith 正规形计算的最小实现深度
  d_q(L,gamma)。对 rank-one named edge delta，d_q 恰为
  v_q(content(delta))；允许非零源列规范化时，指定 endpoints 在层 J 实现该角色的
  充要条件是 content(delta) 整除 endpoint 差且该差的 q 进赋值精确为 J。进一步对
  核心素数 p、q 不整除 p 且尚未绑定物理层的 rank-one 请求，在 J>=max(1,d_q) 时
  可用广义横向数字 alpha q^J 构造 source-prime matched canonical carrier；若精确
  范围门通过，它给出带名整数 provenance、角色精确匹配、独占下一层
  {1,q} 物理块和显式 C_q 商，而不要求原角色在第零层延拓到整个 ambient 格。任何
  两点 owner 边都必须满足 4q^J<p，因此最小深度超过窗口容量时得到全 owner 窗口的
  严格 no-go。层移位只支付 provenance 成本，不增加初等秩，也不自动构造 target
  state、E4 或 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-owner-incidence-edge-source-preserving-capacity
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
  - type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
  - type-II-cross-state-source-relation-role-capacity-dispatch
  - type-II-cross-state-layered-rado-qcapacity-cut
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - source-lattice
  - Smith-normal-form
  - q-adic
  - q-height
  - affine-provenance
  - matched-carrier
  - source-rank
  - strict-obstruction
  - capacity-map
  - well-founded-descent
  - proof-program
sources:
  - claim: type-I-odd-owner-incidence-edge-source-preserving-capacity
    role: one-named-edge-provenance-and-rank-one-capacity
  - claim: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
    role: exclusive-next-layer-physical-q-block
  - claim: type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
    role: cyclotomic-Cq-quotient-and-content-adaptive-carrier
  - claim: type-II-cross-state-source-relation-role-capacity-dispatch
    role: typed-primary-source-role-demand
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: fixed-layer-capacity-and-no-retagging-boundary
  - claim: denominator-escape-state-contract
    role: E1-E5-and-reset-boundary
  - reproduction: reproductions/type_i_source_lattice_qheight_dual_valuation_shift_carrier.py
    role: focused-dual-depth-carrier-window-and-scope-controls
visibility: public
last_checked: '2026-08-10'
---

# 源格角色的最小 \(q\) 层对偶与 content 估值移位载体

## 1. 从二元 ambient 门改为分层对偶门

固定奇素数 \(q\)、子格 \(L\le\mathbb Z^d\) 和非零角色

\[
\gamma:L\longrightarrow\mathbb F_q.
\tag{1}
\]

第零层问题是 \(\gamma\) 能否写成某个 ambient 线性式
\(\mathbf a\cdot\ell\bmod q\)。它并不是唯一有意义的实现问题。对每个 \(J\ge0\)，
定义整数对偶格

\[
\mathcal A_J(L)
=\{\mathbf a\in\mathbb Z^d:
  \mathbf a\cdot L\subseteq q^J\mathbb Z\}
\tag{2}
\]

以及归一化层角色

\[
\rho_J(\mathbf a)(\ell)
=\frac{\mathbf a\cdot\ell}{q^J}\pmod q
\qquad(\ell\in L).
\tag{3}
\]

式 (3) 是源子格上的角色；它不要求
\(\mathbf a\cdot z/q^J\) 对每个 \(z\in\mathbb Z^d\) 都为整数。后一个更强要求
等价于 \(\mathbf a\in q^J\mathbb Z^d\)，不能与 (2) 混用。

记

\[
F_J(L)=L\cap q^{J+1}\mathbb Z^d.
\tag{4}
\]

则层 \(J\) 的精确对偶像为

\[
\boxed{
\operatorname{im}\rho_J
=\{\theta\in\operatorname{Hom}(L,\mathbb F_q):
  \theta|_{F_J(L)}=0\}.}
\tag{5}
\]

因此存在 \(\mathbf a\in\mathcal A_J(L)\) 满足
\(\rho_J(\mathbf a)=\gamma\)，当且仅当

\[
\boxed{\gamma(F_J(L))=0.}
\tag{6}
\]

若 (6) 失败，任取

\[
\ell_J\in F_J(L),
\qquad
\gamma(\ell_J)\ne0
\tag{7}
\]

就是严格阻碍：对所有 \(\mathbf a\in\mathbb Z^d\)，

\[
\frac{\mathbf a\cdot\ell_J}{q^J}
\equiv0\pmod q.
\tag{8}
\]

这把 `AMBIENT_PULLBACK_UNPROVED` 改成了一个有正、负证书的有限层判定，而不是
把所有第零层失败都永久拒绝。

## 2. Smith 正规形证明与最小实现深度

取 \(L\) 的一组 Smith 基。在相应的 ambient 整数坐标中可写成

\[
L=\bigoplus_{i=1}^r d_i\mathbb Z e_i,
\qquad
d_i\mid d_{i+1},
\qquad
t_i=v_q(d_i),
\tag{9}
\]

并记

\[
h_i=\gamma(d_i e_i)\in\mathbb F_q.
\tag{10}
\]

对角坐标 \(a_i\) 必须解同余

\[
a_i d_i\equiv q^J h_i\pmod {q^{J+1}}.
\tag{11}
\]

若 \(t_i\le J\)，写 \(d_i=q^{t_i}u_i\)、\(q\nmid u_i\)，可取

\[
a_i\equiv
q^{J-t_i}u_i^{-1}h_i
\pmod {q^{J+1-t_i}}.
\tag{12}
\]

若 \(t_i\ge J+1\)，式 (11) 可解当且仅当 \(h_i=0\)，此时取 \(a_i=0\)。另一方面，
\(F_J(L)\) 在第 \(i\) 个方向由

\[
q^{\max(0,J+1-t_i)}d_i e_i
\tag{13}
\]

生成；式 (10) 在该生成元上非零，恰当且仅当 \(t_i\ge J+1\) 且 \(h_i\ne0\)。
这同时证明 (5)--(6) 及构造式 (12)。

定义角色的最小 \(q\)-层深度

\[
\boxed{
d_q(L,\gamma)
=\min\{J\ge0:\gamma(F_J(L))=0\}
=\max_{h_i\ne0}t_i.}
\tag{14}
\]

由于 \(L\) 有限生成，(14) 总是有限。固定一个确定性 Smith 算法，并在
\([0,q^{J+1})^d\) 中取字典序最小解，便得到规范对偶向量

\[
\mathbf a^{\rm can}_{J}(L,\gamma).
\tag{15}
\]

对 \(J<d_q\)，同一 Smith 顺序中第一个满足
\(t_i\ge J+1,h_i\ne0\) 的方向给出规范阻碍 (7)。所以每一层都有且只有以下二类输出：

~~~text
SOURCE_LATTICE_QHEIGHT_DUAL_READY
  or SOURCE_LATTICE_QHEIGHT_DUAL_OBSTRUCTED
~~~

特别地，第零层 ambient pullback 存在，当且仅当

\[
d_q(L,\gamma)=0.
\tag{16}
\]

第零层失败并不意味着所有正层失败；它精确测量的是必须支付多少层 source-lattice
divisibility，才能使角色成为整数归一化对偶。

## 3. rank-one named edge 的精确充要条件

令带名有向边的完整整数记录差为

\[
\delta=z_1-z_0\ne0,
\qquad
g=\operatorname{content}(\delta)=q^t g_0,
\qquad q\nmid g_0,
\tag{17}
\]

并在边格 \(L_\delta=\mathbb Z\delta\) 上固定

\[
\gamma(n\delta)=nc,
\qquad c\in\mathbb F_q^\times.
\tag{18}
\]

rank-one Smith 不变量就是 \(g\)，故 (14) 立即给出

\[
\boxed{d_q(L_\delta,\gamma)=t.}
\tag{19}
\]

给定整数 endpoints \(s_0,s_1\)，写 \(\Delta_s=s_1-s_0\)。存在整数仿射函数

\[
\mathcal L(z)=s_0+\mathbf A\cdot(z-z_0),
\qquad
\mathcal L(z_i)=s_i
\tag{20}
\]

当且仅当

\[
\boxed{g\mid\Delta_s.}
\tag{21}
\]

取固定顺序的 Bezout 向量
\(\mathbf r\cdot(\delta/g)=1\)，便可令

\[
\mathbf A=\frac{\Delta_s}{g}\mathbf r.
\tag{22}
\]

而且所有整数插值在整条 source line 上都有同一个值：

\[
\mathcal L(z_0+n\delta)-s_0=n\Delta_s.
\tag{23}
\]

因此层 \(J\) 的边数字

\[
T_{\mathcal L,J}(n\delta)
=\frac{\mathcal L(z_0+n\delta)-s_0}{q^J}pmod q
\tag{24}
\]

在 \(L_\delta\) 上有定义，当且仅当 \(q^J\mid\Delta_s\)；它在生成元上的值为

\[
T_{\mathcal L,J}(\delta)
=\frac{\Delta_s}{q^J}pmod q.
\tag{25}
\]

所以不允许重标度时，(20) 精确实现 (18) 当且仅当

\[
g\mid\Delta_s,
\qquad
q^J\mid\Delta_s,
\qquad
\Delta_s/q^J\equiv c\pmod q.
\tag{26}
\]

若像现有 incidence 合同一样允许一个非零 \(\mathbb F_q\) 源列规范化，则精确条件缩为

\[
\boxed{
g\mid\Delta_s,
\qquad
v_q(\Delta_s)=J.}
\tag{27}
\]

式 (27) 自动强制 \(J\ge t\)。当 \(t>0\) 时，任何 ambient 第零层线性角色都在
\(\delta\) 上为零；若还要求 (24) 对全部 \(z\in\mathbb Z^d\) 有定义，则
\(\mathbf A\in q^J\mathbb Z^d\)，从而

\[
v_q(\mathbf A\cdot\delta)\ge J+t>J,
\tag{28}
\]

又与 (27) 矛盾。这证明 source-line provenance 与 whole-ambient same-prefix map 是
两个不同合同。

最小反例已经说明这种区分不能删除：取

\[
q=3,
\quad L=3\mathbb Z,
\quad\gamma(3n)=n,
\quad J=1,
\quad\mathcal L(z)=z.
\tag{29}
\]

则 \(T_{\mathcal L,1}(3n)=n\)，但任何
\(\mathbb Z\to\mathbb F_3\) 的 ambient 线性式都把 \(3\) 送到零；而
\(\mathcal L(1)/3\) 也不是整数。它是合法 source-line 正例，不是 ambient 正例。

## 4. 最小层的 valuation-shift matched carrier

现在固定核心素数 \(p\)、奇素数 \(q\nmid p\) 和式 (17)--(18) 的 named edge。
取任意

\[
J\ge J_0:=\max(1,t),
\qquad
Q=q^J,
\qquad
m=q^{J+1},
\tag{30}
\]

并令

\[
b=\beta_{J+1}(p)=-p\,4^{-1}\pmod m,
\qquad
\bar b=b\pmod q,
\qquad
\alpha=c\bar b^{-1}\in\mathbb F_q^\times.
\tag{31}
\]

取 cyclotomic 构造中满足

\[
r\mid\Phi_q(q),
\qquad
\operatorname{ord}_r(q)=q,
\qquad
v_q(r-1)=1
\tag{32}
\]

的最小素因子。依次取满足避让条件的最小素数

\[
u\equiv1+\alpha Q\pmod m,
\qquad
u\nmid g_0r,
\tag{33}
\]

定义

\[
H=\operatorname{lcm}(g_0,r,u),
\qquad
A_0=H/\operatorname{rad}(H),
\tag{34}
\]

再取

\[
v\equiv1\pmod m,
\quad v\nmid H,
\qquad
\lambda\equiv b(A_0H)^{-1}\pmod m,
\quad\lambda\nmid Hv.
\tag{35}
\]

这些剩余类都与 \(m\) 互素，故 Dirichlet 定理保证选择存在。令

\[
\begin{aligned}
D_*&=H\lambda,& A_*&=A_0,&
C_*&=\operatorname{rad}(H)\lambda,\\
x&=A_0H\lambda,&D_0&=D_*v,\\
a_0&=A_0,&a_1&=A_0u,\\
s_0&=xv,&s_1&=xuv.
\end{aligned}
\tag{36}
\]

和 ambient content-adaptive 构造一样，有

\[
\begin{aligned}
&A_*\mid D_* &&\text{且 }D_*/A_*=\operatorname{rad}(H)\lambda\text{ 平方自由},\\
&a_i\mid D_0 &&\text{且 }D_0/a_0=\operatorname{rad}(H)\lambda v\text{ 平方自由},\\
&&&D_0/a_1=(\operatorname{rad}(H)/u)\lambda v\text{ 平方自由}.
\end{aligned}
\tag{37}
\]

所以 target 与两个 source rows 都 canonical，且 \(D_*<D_0\)、\(q\nmid D_*D_0\)。
若精确范围门

\[
\boxed{p>4xuv}
\tag{38}
\]

通过，则三个算术点都在窗口内。由构造有

\[
x\equiv s_0\equiv b,
\qquad
s_1\equiv b(1+\alpha Q)\pmod m,
\tag{39}
\]

从而

\[
\boxed{
v_q(p+4x)\ge J+1,
\quad
v_q(p+4s_0)\ge J+1,
\quad
v_q(p+4s_1)=J.}
\tag{40}
\]

横向数字还**精确**匹配输入角色：

\[
\tau_J(s_1)-\tau_J(s_0)
=\frac{s_1-s_0}{Q}
\equiv xv\alpha
\equiv\bar b\alpha
=c\pmod q.
\tag{41}
\]

另一方面，\(g_0\mid x\) 且 \(q^t\mid u-1\)，所以

\[
g\mid s_1-s_0=xv(u-1),
\qquad
v_q(s_1-s_0)=J.
\tag{42}
\]

式 (21)--(27) 给出整数仿射规则

\[
\boxed{
\mathcal L(z)
=s_0+\frac{s_1-s_0}{g}\,
\mathbf r\cdot(z-z_0),
\qquad
\mathbf r\cdot(\delta/g)=1,}
\tag{43}
\]

它在整条 named source line 上实现 (18)。式 (40) 又满足 next-layer 定理：\(s_0\)
是唯一 deep endpoint，target \(x\) 继承独占层 \(J+1\)，所以得到真实
\(\{1,q\}\) physical block。由于 \(r\mid D_*\) 且 \(q\nmid D_*\)，幂角色

\[
\eta(z)=(z\bmod r)^{(r-1)/q}
\tag{44}
\]

给出 \(U(4D_*)\twoheadrightarrow C_q\)，并把实际 \([q]\) 送到生成元。

因此在 occurrence 与 prescribed-label 门也通过时，可输出

~~~text
VALUATION_SHIFTED_SOURCE_LINE_CARRIER_READY
  qheight_dual_depth = t
  physical_layer = J
  affine_rule = AFFINE_QHEIGHT_CONTENT_EDGE_LIFT_V3
  source_relation_scope = one_named_edge_source_line
  owner_digit_difference = gamma(z1-z0) = c
  physical_block = {1,q}
  source_rank_capacity = 1
  whole_ambient_same_prefix = false when t > 0
  recursive_edge_eligible = false
~~~

对固定 \((q,J,g_0,c)\)，可对有限个允许的 \(b\) 分别冻结 (33)--(35)，因而存在有限
阈值 \(B(q,J,g_0,c)\)，使所有 \(p>B\) 的兼容核心素数通过 (38)。但在真实选择器中
\(g_0,t\) 可以随 \(p\) 和 source state 增长，所以这里没有全局统一阈值。

## 5. 窗口容量、固定层与递降边界

任意两个不同的层 \(J\) owner endpoints 都满足

\[
s_1-s_0\in q^J\mathbb Z\setminus\{0\},
\qquad
0<s_i<p/4.
\tag{45}
\]

所以必有

\[
q^J\le|s_1-s_0|<p/4,
\qquad
\boxed{4q^J<p.}
\tag{46}
\]

定义两点 owner 窗口的最大层容量

\[
H^{\rm edge}_{p,q}
=\left\lfloor\log_q\frac{p-1}{4}\right\rfloor.
\tag{47}
\]

若请求未预先固定层，则 rank-one edge 的最小代数成本是
\(J_0=\max(1,t)\)。若

\[
\boxed{J_0>H^{\rm edge}_{p,q},}
\tag{48}
\]

任何标准 owner 窗口中的整数仿射 two-point 实现都不可能存在，输出

~~~text
EDGE_SOURCE_ROLE_QHEIGHT_WINDOW_OBSTRUCTED
  required_layer = J0
  available_edge_height = H_edge(p,q)
~~~

例如

\[
p=97,
\quad q=3,
\quad L=27\mathbb Z,
\quad\gamma(27n)=n
\tag{49}
\]

有 \(t=3\)，而 \((p-1)/4=24\) 给出
\(H^{\rm edge}_{97,3}=2\)。任意 \(J\ge3\) 都要求两个窗口点至少相差 27，但窗口宽度
小于 24，故 (48) 是严格 no-go，不是构造搜索失败。

若原请求已经绑定层 \(J_{\rm req}\)，则只能在该层应用 (5)--(6)：

* \(J_{\rm req}<d_q(L,\gamma)\) 时输出带 (7) 的严格 dual obstruction；
* \(J_{\rm req}\ge d_q(L,\gamma)\) 时构造该层对偶，但仍须另过物理范围与来源门。

把失败请求改标为更深层并不支付原 occurrence key。确实，若
\(v_q(s_1-s_0)=J>J_{\rm req}\)，则

\[
\frac{s_1-s_0}{q^{J_{\rm req}}}\equiv0\pmod q,
\tag{50}
\]

原层源列为零。只有另有经过证明的 layer-relay/retyping 合同，才能产生新的层请求。

content 深度 \(t\) 也不是新增容量。式 (40) 仍只产生一个 exclusive
\(\{1,q\}\) block，初等源秩精确为 1；公共的前 \(J\) 层不能重复收费，单块稳定子
仍然平凡，不能吸收非平凡降模核。

固定 \(p,q\) 后，若额外定义一个封闭状态类型，使 \(J\) 是权威 cursor、每条非终端边
都严格增加 \(J\) 或先降低一个永不回升的外层秩，并禁止退出后重置 \(J\)，则

\[
\Psi_{p,q}(J)=H^{\rm edge}_{p,q}-J
\tag{51}
\]

是该封闭子系统的良基局部势。但当前 carrier 是一次算术构造，不是这种状态转移；它
没有完整 target state、全域 marked map 或 reset policy。因此 (51) 不能把本卡升级为
E4/E5，更不能把“选择了较深层”误写成下降。

## 6. 两个正控制

### 6.1 非饱和源格的层深对偶

在 \(\mathbb Z^2\) 中取

\[
L=3\mathbb Z e_1\oplus\mathbb Z e_2,
\qquad q=3.
\tag{52}
\]

若 \(\gamma(3e_1)=1,\gamma(e_2)=2\)，则第零层由
\(3e_1\in L\cap3\mathbb Z^2\) 严格阻塞，而第 1 层可取

\[
\mathbf a=(1,6),
\qquad
\frac{\mathbf a\cdot3e_1}{3}=1,
\qquad
\frac{\mathbf a\cdot e_2}{3}=2.
\tag{53}
\]

所以 \(d_3(L,\gamma)=1\)。若改为
\(\gamma(3e_1)=0,\gamma(e_2)=2\)，则
\(\mathbf a=(0,2)\) 已在第零层实现角色，说明最小深度依赖角色的 active Smith
方向，而不是只取 \(L\) 的最大 Smith 赋值。

### 6.2 \(p=97561\) 的 non-ambient physical carrier

取

\[
p=97561,
\quad q=3,
\quad\delta=3,
\quad\gamma(3n)=n,
\quad J=t=1.
\tag{54}
\]

这里 \(p\equiv1\pmod {24}\) 为素数，且

\[
b=2,
\quad\alpha=2,
\quad r=13,
\quad u=7,
\quad H=91,
\quad A_0=1,
\quad v=19,
\quad\lambda=2.
\tag{55}
\]

构造给出

\[
(D_*,A_*,C_*,x)=(182,1,182,182),
\qquad
D_0=3458,
\tag{56}
\]

\[
(a_0,a_1)=(1,7),
\qquad
(s_0,s_1)=(3458,24206).
\tag{57}
\]

范围与层高逐项为

\[
4s_1=96824<p,
\tag{58}
\]

\[
\begin{aligned}
p+4x&=98289=3^2\cdot10921,\\
p+4s_0&=111393=3^2\cdot12377,\\
p+4s_1&=194385=3\cdot64795.
\end{aligned}
\tag{59}
\]

而

\[
\frac{s_1-s_0}{3}=6916\equiv1\pmod3.
\tag{60}
\]

取 \(z_0=0,z_1=3\)，式 (43) 成为

\[
\mathcal L(z)=3458+6916z,
\tag{61}
\]

故 \(\mathcal L(0)=s_0,\mathcal L(3)=s_1\)，并在 \(3\mathbb Z\) 上精确实现
\(\gamma\)。但 \(\mathcal L(1)-s_0=6916\) 不被 3 整除，所以该控制严格是
source-line carrier；它不伪装成 whole-ambient same-prefix map。

## 7. 统一分派与剩余缺口

本卡把 source role 的准入改写为：

~~~text
SOURCE_RANK_DEMAND(q, gamma on L)
  -> requested physical layer J already fixed:
       gamma(L intersect q^(J+1) Z^d) != 0:
         SOURCE_LATTICE_QHEIGHT_DUAL_OBSTRUCTED(witness)
       otherwise:
         SOURCE_LATTICE_QHEIGHT_DUAL_READY
         physical source/range/label gates remain
  -> unlayered rank-one named edge:
       t = v_q(content(delta)); J0 = max(1,t)
       J0 > H_edge(p,q):
         EDGE_SOURCE_ROLE_QHEIGHT_WINDOW_OBSTRUCTED
       otherwise:
         valuation-shift matched carrier
           range pass + occurrence/label pass:
             VALUATION_SHIFTED_SOURCE_LINE_CARRIER_READY
           range fail:
             VALUATION_SHIFTED_CARRIER_RANGE_UNCLOSED
  -> two or more independent roles:
       one carrier still has source_rank_capacity = 1
       form W <= Hom(L,F_q) and the obstruction filtration O_J
       fixed-layer request:
         check W intersect V_J_req at the original singleton layer
         never retag through a deeper tail
       unlayered basis-flexible contract:
         run the exact role-subspace tail-capacity criterion
       unlayered named/immutable contract:
         run the exact minimum-depth tail-Hall criterion
       then run physical layered Rado/Hall and distinct occurrence ledger
~~~

这关闭了一个真实缺口：rank-one named edge 不再需要先有第零层 ambient pullback；
非饱和 content 的 \(q\)-部分被精确转成最小层成本，并在超出 owner 窗口时给出全窗口
no-go。它没有证明每个实际 F/G 状态都通过 (38)，也没有把一般源子格的对偶向量自动
变成全部记录都 canonical、范围合格的物理 rows。下一决定性缺口因此收紧为：

1. 对 range-pass 的 receipt 构造完整 target state、occurrence assignment 与既定标签
   联合 SNF；
2. 对 range-fail 或 (48) 的状态，构造另一 Type I/II terminal、完整 kernel source
   box，或已封闭的良基下降；
3. 对 \(\dim\langle\gamma\rangle>1\) 的需求，先用
   [源格障碍过滤的短正合列与上尾 Hall 容量](type-I-source-lattice-filtered-dual-tail-hall-capacity.md)
   对 fixed-layer 请求计算原层障碍秩，对 unlayered 请求计算基不变的上尾代数缺口；
   再为通过者证明真实 carrier 的范围、标签与 occurrence
   Hall/Rado 条件，不能复制本卡的一维块。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_source_lattice_qheight_dual_valuation_shift_carrier.py \
  --verify
~~~

验证器只重算 (52)--(53) 的层深二分、(54)--(61) 的 non-ambient carrier、固定层
退化和 (48)--(49) 的窗口 no-go；不运行历史扫描。
