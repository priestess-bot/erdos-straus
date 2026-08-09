---
kind: claim
claim_id: type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
title: 奇素数 source 匹配的仿射载体、显式核 Fourier 与良基递降边界
statement: >-
  固定奇素数 q 和层 j>=1。存在一个只依赖 (q,j) 的有限、逐模板固定 target 且残数数目最优的
  canonical next-layer carrier 菜单；每张模板只有两个 source rows 和一个 target，且实际
  因子 q 通过显式 U(4D_*)->C_q 商承载一个非零 q-source rank。对任意具有 ambient
  指数格 pullback 的带名非零 C_q 源记录对，还可把其整数差向量的 content 吸收到
  共同基的平方部分，得到一个 content-adaptive 仿射模板；只要精确范围门通过，就同时关闭带名整数 provenance、
  独占 q^(j+1) 物理层和 freely selectable C_q role。固定 q=3 三模板并不具备这一
  全称 provenance：content=11 给出严格反例。另一方面，任意 proper cyclic prefix 的
  稳定子平凡；故单个 {1,q} 块不能吸收任何严格降模的非平凡同余核。失败分支可由
  physical-q-coordinate character twist 显式构造 kernel Fourier 角色；既定 target
  标签仍需联合 SNF，且该角色不能自动
  登记 E5。裸 D_*<D_0 只有在完整 target state、Sol(p) 恒等 mark 和不可重置 owner
  phase 中才给出良基下降；自然较小余因子 n=(p+4x)/q^(j+1) 也不保证非空、可递归
  闭合的 marked source，
  p=2113、x=14、n=241 的对应标记集严格为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
  - type-I-odd-owner-incidence-edge-source-preserving-capacity
  - type-II-cross-state-source-relation-role-capacity-dispatch
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-saturated-source-congruence-stabilizer-trichotomy
  - two-denominator-lift-d-only-marked-normal-form
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - odd-owner
  - source-rank
  - affine-provenance
  - cyclotomic
  - arithmetic-progression
  - q-adic
  - stabilizer
  - kernel-fourier
  - marked-solution
  - well-founded-descent
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
    role: exclusive-next-layer-physical-block
  - claim: type-I-odd-owner-incidence-edge-source-preserving-capacity
    role: named-integer-edge-and-rank-one-provenance-contract
  - claim: type-II-cross-state-source-relation-role-capacity-dispatch
    role: anchor-versus-source-rank-typed-input
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: exact-kernel-stabilizer-gate
  - claim: type-II-saturated-source-congruence-stabilizer-trichotomy
    role: kernel-fourier-or-lower-modulus-dispatch
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: marked-lift-nonemptiness-test
  - claim: denominator-escape-state-contract
    role: global-E1-E5-and-reset-policy
  - reproduction: reproductions/type_i_odd_owner_prime_matched_affine_carrier_fourier_boundary.py
    role: focused-carrier-affine-stabilizer-fourier-and-marked-no-go-controls
visibility: public
last_checked: '2026-08-10'
---

# 奇素数 source 匹配的仿射载体、显式核 Fourier 与良基递降边界

## 1. 只对真实 source demand 收费

先固定统一选择器已经产生的一条 typed 请求

\[
\operatorname{SOURCE\_RANK\_DEMAND}(q,1),
\tag{1}
\]

其中 \(q\) 是奇素数。要求该角色先拉回到完整指数格：存在 ambient 同态

\[
\widetilde\gamma:\mathbb Z^d\longrightarrow C_q
\]

使其在真实源差分群 \(\Delta\le\mathbb Z^d\) 上非平凡，并已降到非零商

\[
\gamma=\widetilde\gamma|_\Delta:\Delta\longrightarrow C_q.
\tag{2}
\]

若角色在 \(\Delta\) 上平凡而只分离 target anchor，则已有分派要求
\(d_q=0\)；这种 `ANCHOR_ONLY_FOURIER` 不进入本卡。F/G 是目标纤维分类，不能代替
式 (2) 的关系限制检验。若只有抽象子群角色而没有 ambient pullback，本卡的 content
构造不适用，必须先输出 `SOURCE_ROLE_AMBIENT_PULLBACK_UNPROVED`。

设 \(G\) 为有限阿贝尔群，\(u\in G\)。存在某个可自由选择的循环
\(\ell\)-primary 角色，使 \(u\) 的像恰有阶 \(\ell\)，当且仅当

\[
\boxed{\ell\mid\operatorname{ord}_G(u).}
\tag{3}
\]

必要性来自像的阶整除原像的阶。充分性可先在 \(\langle u\rangle\) 上把 \(u\)
送到一个本原 \(\ell\) 次单位根，再把有限阿贝尔群子群上的复角色延拓到 \(G\)，
最后取 \(\ell\)-primary 分量。若强制目标恰为 \(C_\ell\)，充要条件更强：

\[
\boxed{u\notin G^\ell.}
\tag{4}
\]

因此二点集合匹配、两个不同特征下数值都等于 1 的 Rado rank，以及非线性 lookup
token，都不能替代 (3) 或 (4)。例如旧 \(q=3\) 三模板的物理元素是 \([3]\)，而

\[
\operatorname{ord}_{56}(3)=6,
\qquad
\operatorname{ord}_{260}(3)=12.
\tag{5}
\]

所以它们对奇素数 source demand 只可能承载 \(q=3\)，不能承载任何
\(C_\ell\)、\(\ell\ne3\)。这不是 carrier 不足的全局 no-go；正确修复是令物理
factor 与 source prime 匹配。

## 2. cyclotomic 素数与直接 \(C_q\) 商

记

\[
\Phi=\Phi_q(q)=1+q+\cdots+q^{q-1}.
\tag{6}
\]

存在素数 \(r\mid\Phi\) 满足

\[
\boxed{
\operatorname{ord}_r(q)=q,
\qquad
v_q(r-1)=1.}
\tag{7}
\]

确实，\(\Phi\equiv1\pmod q\)，故 \(r\ne q\)。又有
\(r\mid q^q-1\)。若 \(r\mid q-1\)，则 \(q\equiv1\pmod r\) 会给出
\(\Phi\equiv q\equiv0\pmod r\)，从而 \(r=q\)，矛盾。因此
\(\operatorname{ord}_r(q)=q\)，特别地 \(q\mid r-1\)。另一方面

\[
\Phi\equiv1+q\pmod {q^2}.
\tag{8}
\]

若每个素因子都为 \(1\pmod {q^2}\)，则计入重数后的乘积也为
\(1\pmod {q^2}\)，与 (8) 矛盾。故可选出 (7) 的 \(r\)。下文一律取满足 (7) 的
**最小素因子**，从而 cyclotomic 坐标也成为菜单的确定字段，而不是隐藏选择。

令 \(M=(r-1)/q\)。式 (7) 给出 \(q\nmid M\)，且 \(M\) 为偶数。若
\(r\mid D\)，便有显式满射

\[
\eta_D:U(4D)\longrightarrow\mu_q(\mathbb F_r),
\qquad
\eta_D(z)=(z\bmod r)^M,
\tag{9}
\]

若再有 \(q\nmid D\)，实际单位类 \([q]\in U(4D)\) 才有定义，并满足

\[
\boxed{
\eta_D(q)\text{ 是生成元},
\qquad
\eta_D(-1)=1.}
\tag{10}
\]

这比仅有 \(q\mid\operatorname{ord}_{4D}(q)\) 更强：它给出一个直接、可复算的
\(C_q\) quotient。

## 3. 固定 \((q,j)\) 的残数最优有限菜单

固定 \(j\ge1\)，写

\[
Q=q^j,
\qquad
m=q^{j+1}.
\tag{11}
\]

用 Dirichlet 算术级数素数定理选择两两不同且避开 \(r\) 的素数

\[
u\equiv1+Q\pmod m,
\qquad
v\equiv1-Q\pmod m.
\tag{12}
\]

于是 \(uv\equiv1\pmod m\)。核心素数可能出现的 deep residue 集为

\[
\mathcal B_{q,j}=
\begin{cases}
\{b\in U(3^{j+1}):b\equiv2\pmod3\},&q=3,\\
U(q^{j+1}),&q\ge5.
\end{cases}
\tag{13}
\]

这是因为 \(p\equiv1\pmod {24}\)；当 \(q=3\) 时兼容性强制
\(b=-p4^{-1}\equiv2\pmod3\)，而 \(q\ge5\) 时 CRT 模数互素。

对每个 \(b\in\mathcal B_{q,j}\)，再选一个素数

\[
\lambda_b\equiv br^{-1}\pmod m
\tag{14}
\]

且所有 \(\lambda_b\) 两两不同并避开 \(r,u,v\)。为使菜单真正 canonical，固定如下
确定化约定：按 \(b\) 的最小正代表递增处理，每次都取满足当前同余和避让条件的最小
素数；\(u,v\) 也依次取满足条件的最小素数。Dirichlet 定理保证这一递归选择总能完成。
定义

\[
\begin{aligned}
D_{*,b}&=x_b=r\lambda_b,\\
D_{0,b}&=x_buv,\\
(a_0,a_1)&=(1,u),\\
(s_0,s_1)&=(D_{0,b},D_{0,b}u).
\end{aligned}
\tag{15}
\]

四个素因子互异，所以两个 source rows 与 target \((D_*,A)=(D_{*,b},1)\)
都 canonical，并且

\[
\gcd(s_0,s_1)=D_{0,b},
\qquad
D_{*,b}<D_{0,b}.
\tag{16}
\]

若 \(b=\beta_{j+1}(p)\) 且

\[
p>B(q,j):=4ru^2v\max_b\lambda_b,
\tag{17}
\]

则 \(4s_i<p\)，并且

\[
s_0\equiv x_b\equiv b,
\qquad
s_1\equiv b(1+Q)\pmod m.
\tag{18}
\]

因此 \(s_0\) 与 target 至少有 \(j+1\) 个 \(q\)-层，而
\(s_1\) 的高度精确为 \(j\)。横向步长满足

\[
\frac{s_1-s_0}{Q}
=D_{0,b}\frac{u-1}{Q}\not\equiv0\pmod q.
\tag{19}
\]

结合前卡的 next-layer 定理，(18)--(19) 给出真实 exclusive block
\(\{1,q\}\)；(9)--(10) 又把它送入一个非零 \(C_q\) role。

每个固定 target \(x\) 只能覆盖唯一剩余类

\[
p\equiv-4x\pmod m.
\tag{20}
\]

反之，CRT 与 Dirichlet 定理保证 (13) 中每个允许类都含无穷多个核心素数。因此任意
覆盖全部充分大核心素数的 fixed-target 菜单至少需要

\[
\boxed{
|\mathcal B_{q,j}|=
\begin{cases}
3^j,&q=3,\\
q^j(q-1),&q\ge5.
\end{cases}}
\tag{21}
\]

张模板。(15) 恰好达到下界。这里“有界”是对固定 \((q,j)\) 而言；不存在对全部
\(q\) 都保持绝对常数模板数的 fixed-target 推广。

## 4. 固定 rows 的仿射 provenance 充要门

令两条带名源记录的完整整数指数向量为 \(z_0,z_1\in\mathbb Z^d\)，并记

\[
\delta=z_1-z_0,
\qquad
g=\operatorname{content}(\delta)
=\gcd_i|\delta_i|.
\tag{22}
\]

给定两个整数 endpoint \(t_0,t_1\)，存在整数仿射函数

\[
L(z)=c+\mathbf a\cdot z,
\qquad
L(z_i)=t_i\quad(i=0,1),
\tag{23}
\]

当且仅当

\[
\boxed{g\mid t_1-t_0.}
\tag{24}
\]

因为所有整数点积 \(\mathbf a\cdot\delta\) 组成的理想恰为 \(g\mathbb Z\)。通过固定
坐标顺序的扩展 gcd/HNF，规范取 \(\mathbf r\cdot\delta=g\)，再令

\[
\mathbf a=\frac{t_1-t_0}{g}\mathbf r,
\qquad
c=t_0-\mathbf a\cdot z_0
\tag{25}
\]

即可构造 (23)。对 source-role 兼容性还需使用第 1 节的 ambient pullback。写

\[
\widetilde\gamma(z)=\mathbf h\cdot z\pmod q
\]

并假设 \(\widetilde\gamma(\delta)\ne0\)。此时若 \(q\mid g\)，则
\(\delta\equiv0\pmod q\)，与非零性矛盾；故 \(q\nmid g\)。令

\[
\delta'=\delta/g,
\qquad
\lambda=(\mathbf h\cdot\delta')^{-1}\in\mathbb F_q^\times.
\tag{25a}
\]

固定 \(\lambda\) 的最小非负代表。因为
\(1-\lambda\mathbf h\cdot\delta'\) 被 \(q\) 整除，而 primitive 向量
\(\delta'\) 的整数点积覆盖 \(\mathbb Z\)，可规范求出 \(\mathbf k\in\mathbb Z^d\)
使

\[
\mathbf k\cdot\delta'
=\frac{1-\lambda\mathbf h\cdot\delta'}q.
\]

于是

\[
\boxed{
\mathbf r=\lambda\mathbf h+q\mathbf k,
\qquad
\mathbf r\cdot\delta'=1,
\qquad
\mathbf r\equiv\lambda\mathbf h\pmod q.}
\tag{25b}
\]

这比任意 Bezout 向量更强：它同时实现 content 插值，并保证最终横向线性函数在整个
ambient 指数格上与 \(\widetilde\gamma\) 只差一个非零标量。若没有 ambient
pullback，则“\(\gamma(\delta)\ne0\Rightarrow q\nmid g\)”一般为假；例如在子格
\(3\mathbb Z\) 上可定义 \(\gamma(3n)=n\bmod3\)。

这给出旧固定三模板的严格边界。其 endpoint 差只有

\[
350-140=210,
\qquad
650-260=390.
\tag{26}
\]

取一维源记录 \(z_0=0,z_1=11\) 和 \(\gamma(z)=z\bmod3\)。这是非零
\(C_3\) source relation，但 \(11\nmid210,390\)。因此任何整数仿射规则都不可能把
这对记录送到旧固定 rows。`source rank = 1`、二点 set token 与 prime matching
都不能删除 (24)。

## 5. content-adaptive 带名 matched carrier

式 (24) 的障碍可以通过一个自适应、仍为常数 row 数的算术构造消除。固定
\((q,j)\) 和一条满足 \(\gamma(\delta)\ne0\) 的带名记录对。先取第 2 节的 \(r\)，
再选素数

\[
u\equiv1+Q\pmod m,
\qquad u\ne r.
\tag{27}
\]

定义

\[
H=\operatorname{lcm}(g,r,u),
\qquad
A_0=H/\operatorname{rad}(H).
\tag{28}
\]

因为 \(q\nmid g\)，有 \((A_0H,m)=1\)。选择素数

\[
v\equiv1\pmod m,
\qquad v\nmid H,
\tag{29}
\]

并对每个 \(b\in\mathcal B_{q,j}\) 选择素数

\[
\lambda_b\equiv b(A_0H)^{-1}\pmod m,
\qquad
\lambda_b\nmid Hv,
\tag{30}
\]

所有选择仍由 Dirichlet 定理保证。令

\[
\begin{aligned}
D_{*,b}&=H\lambda_b,& A_*&=A_0,&
C_*&=\operatorname{rad}(H)\lambda_b,\\
x_b&=A_0H\lambda_b,& D_{0,b}&=D_{*,b}v,\\
a_0&=A_0,& a_1&=A_0u,\\
s_0&=D_{0,b}a_0=x_bv,&
s_1&=D_{0,b}a_1=x_buv.
\end{aligned}
\tag{31}
\]

这些参数逐项满足

\[
\begin{aligned}
&A_*\mid D_{*,b},
&&D_{*,b}/A_*=\operatorname{rad}(H)\lambda_b\text{ 平方自由},\\
&a_i\mid D_{0,b},
&&D_{0,b}/a_0=\operatorname{rad}(H)\lambda_bv\text{ 平方自由},\\
&&&D_{0,b}/a_1=(\operatorname{rad}(H)/u)\lambda_bv\text{ 平方自由}.
\end{aligned}
\tag{32}
\]

这里 \(u\mid\operatorname{rad}(H)\)，故最后一式为整数。又有

\[
D_{*,b}<D_{0,b},
\qquad
s_0\equiv x_b\equiv b,
\qquad
s_1\equiv b(1+Q)\pmod m.
\tag{33}
\]

若

\[
\boxed{p>4x_buv,}
\tag{34}
\]

则两个 endpoint 都在 owner 窗口中，并像 (18)--(19) 一样给出唯一 deep endpoint、
deep target 和非零横向列。由于 \(r\mid D_*\) 且 \(q\nmid D_*\)，式 (9)--(10)
仍给出直接 \(C_q\) 商，并把实际单位类 \([q]\) 送到生成元。

最后，\(g\mid H\mid x_b\)，所以

\[
g\mid s_1-s_0=x_bv(u-1).
\tag{35}
\]

取 (25b) 的 source-compatible \(\mathbf r\)，并令

\[
L(z)=s_0+\frac{s_1-s_0}{g}\,
\mathbf r\cdot(z-z_0).
\tag{35a}
\]

则 \(L(z_i)=s_i\)。而 \((s_1-s_0)/g\) 被 \(Q\) 整除，所以所有 \(L(z)\) 保持
同一个 \(q^j\)-owner prefix，并且

\[
\frac{L(z)-s_0}{Q}
\equiv
\frac{s_1-s_0}{gQ}\lambda\,
\mathbf h\cdot(z-z_0)
\pmod q.
\tag{35b}
\]

前面的标量非零，因为 \(v_q(s_1-s_0)=j\) 且 \(q\nmid g\)。因此 (35a) 不只插值
一个 pair；其完整 ambient 横向函数与 \(\widetilde\gamma\) 相差可逆标量。不过
canonical/range 的物理 rows 仍只对选中的带名 pair 验证，所以可收费容量仍是一个
named edge，而不是把全部记录各自变成独立 occurrence。在 occurrence ledger 尚未收费
且既定额外标签通过联合 SNF 时，输出

~~~text
CONTENT_ADAPTIVE_AFFINE_MATCHED_CARRIER_READY
  source_prime = physical_factor = q
  source_rows = (D0,A0), (D0,A0*u)
  target = (D_*,A_*,C_*,x)
  affine_rule = AFFINE_CONTENT_EDGE_LIFT_V2
  source_relation_scope = one_named_edge_with_ambient_Cq_functional
  physical_block = {1,q}
  exact_Cq_quotient = eta_D_star
  source_rank_capacity = 1
~~~

该构造把任意 rank-one 非零 \(C_q\) pair 的**代数 provenance**缺口压缩成精确范围门
(34)。因为 \(g\)、最小可选 \(v,\lambda_b\) 可能随当前状态增长，(34) 尚未对每个
未决核心素数自动成立；因此这里不能声称全称选择器已经闭合。两个独立请求仍超过这张
二 row 模板的一维 source rank。

## 6. proper prefix 的稳定子 no-go 与容量下界

令 \(G\) 为有限群，\(u\in G\) 的阶为 \(n\)，并定义循环前缀

\[
P_d=\{1,u,\ldots,u^d\}.
\tag{36}
\]

若 \(0\le d<n-1\)，则

\[
\boxed{\operatorname{Stab}_G(P_d)=\{1\}.}
\tag{37}
\]

任一稳定元 \(h\) 因 \(h\cdot1\in P_d\) 必属于 \(\langle u\rangle\)。在
\(\mathbb Z/n\mathbb Z\) 中，真循环区间 \(\{0,\ldots,d\}\) 只有 \(0\) 的前驱
不在区间内；保持该区间的平移必须固定这个唯一边界点，故只能是零平移。若
\(d\ge n-1\)，则 \(P_d=\langle u\rangle\)，其稳定子恰为 \(\langle u\rangle\)。

即使额外授予或已经验证这张跨 row toggle 在固定 \(D_0,A_0\) source fiber 中
`FIBER_REALIZED`，它在第 5 节 source group 中的抽象积集仍只有

\[
G_0=U(4D_0),
\qquad
P=\{1,q\},
\tag{38}
\]

模 \(r\) 投影保证 \(q\mid\operatorname{ord}_{G_0}(q)\)，所以该阶大于 2，(37)
给出 \(\operatorname{Stab}(P)=1\)。另一方面 \(D_0=D_*v\) 且
\((v,4D_*)=1\)，故严格降模核

\[
K=\ker\bigl(U(4D_0)\to U(4D_*)\bigr)
\simeq U(v),
\qquad
|K|=v-1>1.
\tag{39}
\]

因此

\[
\boxed{K\nleq\operatorname{Stab}_{G_0}(\{1,q\}).}
\tag{40}
\]

单个 arithmetic-ready block 绝不可能直接成为现有
`STABILIZER_CONGRUENCE_LOWER_EDGE` 的核饱和源积集。

更一般地，若非空集合 \(P\) 在 \(K\) 下稳定，则 \(P\) 是若干个完整 \(K\)-陪集，
所以

\[
|K|\mid|P|,
\qquad
|P|\ge|K|.
\tag{41}
\]

若 \(P\) 由 \(R\) 个 binary physical occurrence 的乘积产生，则
\(|P|\le2^R\)，必要条件为

\[
\boxed{R\ge\lceil\log_2|K|\rceil.}
\tag{42}
\]

只增加同一 \(q\)-column 的深度也不总能修复：任何该列前缀都包含于
\(\langle q\rangle\)，故非平凡 \(K\)-稳定至少要求

\[
K\le\langle q\rangle,
\tag{43}
\]

且 proper prefix 仍由 (37) 排除；只有覆盖完整循环后才可能吸收 (43) 中的核。

旧三模板给出两个严格控制：

\[
\begin{array}{c|c|c|c}
D_0\to D_*&K&K\cap\langle3\rangle&K\le\langle3\rangle\\ \hline
70\to14&\{1,57,113,169\}\subset U(280)&\{1,169\}&\text{否}\\
130\to65&\{1,261\}\subset U(520)&\{1\}&\text{否}.
\end{array}
\tag{44}
\]

所以这两个固定模板即使无限增加 3-depth，也不能独自完成对应 kernel；必须加入至少
一个独立的非 3 方向。对第一行，单按大小总计至少需要两个 binary bits，即现有
\(\{1,3\}\) 之外至少再加一个。若 `FIBER_REALIZED` 本身未通过，则在稳定子门之前即已
阻塞，不能把本节的抽象 no-go 误写成完整 source-fiber 回译。

## 7. 未固定额外标签时的显式 kernel Fourier 角色

式 (40) 不只给出否定回执。第 2 节的角色可在 source group 上用同一模 \(r\) 公式
定义为

\[
\eta_0:G_0\to C_q.
\tag{45}
\]

因为每个 \(k\in K\) 都约化为 \(1\pmod {4D_*}\)，有

\[
\eta_0|_K=1,
\qquad
\eta_0(q)\text{ 为生成元}.
\tag{46}
\]

选择一个 \(c\in K\setminus\{1\}\) 及分离角色
\(\psi\in\widehat{G_0}\) 使 \(\psi(c)\ne1\)。这可确定化：先按最小正整数代表选择
\(c\)，再把单位按代表排序、把单位根按“阶、标准指数”排序，并在有限角色值表中取
字典序最小的分离角色。令 \(\eta_0(q)\) 对应标准 \(e^{2\pi i/q}\)。对
\(t\in\mathbb F_q\) 定义

\[
\chi_t=\psi\eta_0^t.
\tag{47}
\]

则每个 \(t\) 都有 \(\chi_t(c)=\psi(c)\ne1\)，而

\[
\widehat{1_P}(\chi_t)
=1+\overline{\chi_t(q)}.
\tag{48}
\]

随着 \(t\) 变化，\(\chi_t(q)\) 取 \(q\) 个不同值；至多一个等于 \(-1\)。因为
\(q\ge3\)，按固定顺序取第一个不等于 \(-1\) 的 \(t\)，便得到

\[
\boxed{
\chi_t(c)\ne1,
\qquad
\widehat{1_P}(\chi_t)\ne0.}
\tag{49}
\]

这是未固定其它标签时的显式、可确定化 `CONGRUENCE_KERNEL_FOURIER`。其中
\(\eta_0\) 来自 target 的物理 \(C_q\) 坐标，但 twist **不自动保持**已经指定的
anchor、target phase 或其它 source labels。若这些标签把允许 twist 限制为
\(T_{\rm lab}\subseteq\mathbb F_q\)，必须在 \(T_{\rm lab}\) 内重新检查 (48)；集合为空，
或唯一允许值恰使 \(\chi_t(q)=-1\) 时，输出
`KERNEL_FOURIER_TARGET_LABEL_OBSTRUCTED`。

这一限制是真实的。取加法群 \(G=C_6\oplus C_2\)、\(q=3\)，令

\[
u=(1,0),\quad c=(0,1),\quad
\eta_0(a,b)=e^{2\pi ia/3},\quad
\psi(a,b)=(-1)^{a+b}.
\]

若 anchor \(\alpha=(4,0)\) 被要求满足 \(\chi_t(\alpha)=1\)，则只能取 \(t=0\)；但
\(\chi_0(u)=-1\)，所以 (48) 为零。\(t=1,2\) 虽使 Fourier 非零，却破坏 anchor
标签。因此“物理 target coordinate 可 twist”严格弱于“prescribed target-compatible”。

无标签 witness 把“单块不能降模”变成对偶证书；有标签时还需联合 SNF。两者之后尚缺
把角色送入来源保持、范围合格的 F/G capacity 或完整 kernel source box，不能把 Fourier
非零本身记为递降。

## 8. marked lift 与全局 E5 的精确边界

### 8.1 条件性 identity-mark state completion

局部 \(D_*<D_0\) 并非本质上缺少 E4。设选择器正式定义
`owner_base_descent_v1` 状态，并满足：

1. `equation_target=4/p`，且每个状态都取
   \(W_S=\operatorname{Sol}(p)\)；
2. `owner_base_cursor=D` 是 `state_id` 的权威字段，target 的 F/G、纤维、Fourier、
   provenance 与 occurrence ledger 全部确定性重建；
3. \(\omega,\varphi\in\mathbb N\) 是预先定义、方向固定的 outer/phase ranks；
4. 从该 state type 可达的每条非终端边，要么保持 \((\omega,\varphi)\) 并满足
   \(D_T<D_S\)，要么严格降低字典序前缀 \((\omega,\varphi)\)；更早分量以后永不回升；
5. 除 terminal 与第 4 条列出的边外没有其它允许出口，特别是禁止无成本退出后以更大的
   \(D\) 重入。

则

\[
\Phi_{T\to S}(w)=w
\tag{50}
\]

是全域 E4，且预先定义的字典序势

\[
\Pi(S)=(\omega(S),\varphi(S),D(S),\ldots)
\tag{51}
\]

对每条可达非终端边都严格下降。因此这是一个**封闭 owner 子系统内**的合法 E5；只有
统一选择器的全部入边、出边也满足第 4--5 条时，才能称全局 E5。

当前 arithmetic carrier receipt 尚不满足这些前提。它只给出
\((D_*,A,x,\{1,q\})\)，没有完整 target state，也没有证明旧 F/G 数据与 ledger 的
继承或重建。更直接地，同一 \(p=2113\) 同时存在共同基 \(70\) 和 \(122\) 的不同
owner 边；若下一步可重新选边，路径可在 \(70\to14\) 后把 cursor 重置到 \(122\)。
所以裸 \(D\) 不是全局势。identity rechart 只有在 target 继续具有完整出口时才有用；
它本身不构造 \(\operatorname{Sol}(p)\) 的元素。

### 8.2 自然较小余因子的严格空 marked fiber

对已有正控制

\[
p=2113,
\quad q=3,
\quad j=1,
\quad x=14,
\tag{52}
\]

最自然的真分母候选为

\[
n=\frac{p+4x}{q^{j+1}}=241<p.
\tag{53}
\]

考虑保留两尾的一坐标 marked lift。对
\((a,b,c)\in\operatorname{Sol}(241)\)，其判据为

\[
\Delta=241\cdot2113-4(2113-241)a
=509233-7488a>0,
\qquad
\Delta\mid241\cdot2113\,a.
\tag{54}
\]

正性与 \(a>241/4\) 强制 \(61\le a\le68\)。尾方程的精确因子化是

\[
\bigl((4a-241)b-241a\bigr)
\bigl((4a-241)c-241a\bigr)
=(241a)^2.
\tag{55}
\]

穷尽 (55) 的正因子，只在下列三个 \(a\) 上有解：

\[
\begin{array}{c|c|c|c}
a&(b,c)&\Delta&(241\cdot2113\,a)\bmod\Delta\\ \hline
62&(2139,1030998),(2169,134478)&44977&43569\\
63&(1386,334026),(1446,30366)&37489&28584\\
66&(693,334026),(723,15906)&15025&13478.
\end{array}
\tag{56}
\]

三行余数都非零，其余五个 \(a\) 没有正整数尾。因此

\[
\boxed{W_{2113,241}^{(1)}=\varnothing.}
\tag{57}
\]

这严格证明“next-layer target cofactor 更小”不推出非空、可递归闭合的自然 marked
source。two-denominator 公式在空域上仍可形式地作为 E4 映射，但该分支已知没有任何
source 解，必须标记为 `rejected_branch`；普通 \(\operatorname{Sol}(241)\) 的非空性
不能闭合它。后续不应继续把 (53) 当作默认可用 marked lift。

## 9. 统一分派与剩余缺口

本卡把奇阶 source 请求细化为：

~~~text
typed compatible role
  -> anchor-only on true source differences:
       ANCHOR_ONLY_FOURIER (no source charge)
  -> SOURCE_RANK_DEMAND(ell,1):
       -> no ambient exponent-lattice pullback:
            SOURCE_ROLE_AMBIENT_PULLBACK_UNPROVED
       choose physical prime q=ell
       -> fixed residue-optimal carrier menu
       -> fixed-row affine content gate
            pass: NAMED_EDGE_AFFINE_LIFT_READY
            fail: FIXED_TEMPLATE_AFFINE_CONTENT_OBSTRUCTED
                  -> content-adaptive carrier
                       range pass:
                         CONTENT_ADAPTIVE_AFFINE_MATCHED_CARRIER_READY
                       range fail:
                         ADAPTIVE_CARRIER_RANGE_UNCLOSED
       -> occurrence / prescribed-label joint-SNF gates
       -> one request: owner-local physical rank-one gates ready
            (global E2 still requires complete target state)
       -> at least two independent requests: SOURCE_RANK_DEFICIT
       -> strict D reduction attempt
            single {1,q} block: KERNEL_STABILIZER_OBSTRUCTED
            output explicit unconstrained CONGRUENCE_KERNEL_FOURIER
            prescribed labels -> joint-SNF / TARGET_LABEL_OBSTRUCTED
            full kernel source box: enter sealed lower-modulus phase
       -> global edge only after complete target state, identity mark,
          immutable phase or outer-rank reset payment
~~~

因此已经排除三个伪缺口：任意奇素 source prime 并不缺匹配算术 carrier；固定三模板的
content 阻碍不是绝对障碍；单块的局部 \(D\) drop 不能冒充稳定子 E5。尚未闭合的决定性
命题缩为：对每个实际未决 F/G 状态，要么构造 ambient pullback，并证明某个
content-adaptive 模板在当前 \(p\)-范围内通过且完成 occurrence/target-state 出口，
要么让 (49) 的显式角色通过
既定标签门并扩成
足以覆盖完整同余核的来源盒或送入另一个已有良基 phase。只有该二分具有全称性，才会
推进到目标中的“每个核心素数必有短证书或严格可提升递降”。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_odd_owner_prime_matched_affine_carrier_fourier_boundary.py \
  --verify
~~~

验证器只重算 \(q=3,5\) 的残数数目与固定模板控制、content=11 的固定模板 no-go、
平方 content=4 的自适应载体、ambient/角色相容 Bezout 边界、两个旧 kernel 控制、
binary stabilizer、无约束 twist 与预设标签阻碍，以及 (52)--(57) 的空 marked fiber；
不运行历史扫描。
