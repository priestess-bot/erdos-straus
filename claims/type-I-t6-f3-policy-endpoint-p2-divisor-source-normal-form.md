---
kind: claim
claim_id: type-I-t6-f3-policy-endpoint-p2-divisor-source-normal-form
title: T6-F3 p-free policy 终点的 p² divisor-source 正规形
statement: >-
  固定一个已绑定 persistent source/path 的 m=3 minimal-q=5 proper-root
  rank-stutter receipt，并执行既有确定 p-free raw policy omega_pf。若 terminal-first
  后的 primitive endpoint 为 u+v=R，按原 K 的唯一 complete-excess 分解定义
  u=E_u D_u、v=E_v D_v，则 D_u,D_v|K、D_uD_v|K，且 canonical joined
  multiplier 精确为 L_omega=E_uE_v。因而 L_omega=1 mod p^2 的正确 actual-source
  gate 是 E_uE_v=1+p^2 chi 连同两条 cross-divisor gate，而不是 first child
  L_1=(E/ell)F_y 所满足的旧 D_y 同余。full-capacity 分支进一步有 E_u=1；写
  v=(1+p^2 chi)d、R=1+p tau、c=(pu+1)/d、m=(d+u-1)/p、w=K/(ud)，则
  tau=m+p chi d、4uw=c+p+p^3 chi、p+c|mc^2-c+1，且该 residual 必有 u^2>=p。
  这些结论建立 source-bound normal form 与确定 tie-break，但不证明 residual 为空、
  terminal 或有 paid successor；short Q_pf 的真正 two-sided atomic residual、
  universal E1 path coverage、E3 serializer/owner 和 T5 strict ticket 仍开放。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
topics:
  - type-I
  - t6
  - proper-root
  - m-three
  - second-child
  - complete-excess
  - divisor-source
  - p-squared
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: first-child-rank-stutter-and-deterministic-p-free-policy
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: unique-complete-excess-blocks-canonical-target-and-conditional-E1-E4
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: one-sided-endpoint-divisor-pair-normal-form
  - claim: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
    role: p-squared-return-boundary-and-small-endpoint-exclusion
  - reproduction: reproductions/type_i_t6_f3_policy_endpoint_p2_gate.py
    role: focused-exact-controls-for-two-sided-and-one-sided-identities
visibility: public
last_checked: '2026-08-23'
---

# T6-F3 p-free policy 终点的 \(p^2\) divisor-source 正规形

## 1. 量词与对象分离

固定核心素数 \(p\equiv1\pmod {24}\)，以及一个已经入队、内容寻址的
`TYPEI/CHARGED` source

\[
S=(p,R,K;\mathcal A,\varsigma),
\qquad
K=\mathcal A(p-1),
\qquad
4K=pR+1,
\qquad
\mathcal A>B_p.
\tag{1}
\]

本卡只研究以下 **source-bound** 子域：source receipt 已保存从 \(S\) 到 \(m=3\)、
minimal-\(q=5\) proper-root endpoint 的实际 raw path \(\pi\)，第一次
excess-\(\ell\) child 落入 atomic rank-stutter，且从该 child 开始的所有
terminal/alternate priority prefix 均有 miss receipt。既有推导在该处写

\[
x=\frac E\ell D,
\qquad
y=F_yD_y,
\qquad
F_y\equiv\ell\pmod p,
\tag{2}
\]

并定义第一次 canonical checkpoint 的倍率

\[
\boxed{L_1=\frac E\ell F_y.}
\tag{3}
\]

旧的二阶 child 同余 `(20zz-factor-21/23)` 明确以

\[
L_1=1+p^2\chi_1
\tag{4}
\]

为前提，并约束 (2) 中的 \(D_y\)。它不是后述 \(L_\omega\) 的同余。

令

\[
\mathcal W_y=
\prod_{\nu_q(y)>\nu_q(K)}q^{\nu_q(y)-\nu_q(K)},
\qquad
J_y=(Q_y,p-1),
\qquad
F_y=\mathcal W_yJ_y.
\tag{5}
\]

既有确定 policy 为

\[
\omega_{\rm pf}=
\begin{cases}
\omega_y,&\mathcal W_y\not\equiv\delta\pmod p,\\
Q_{\rm pf}\text{-word},&\mathcal W_y\equiv\delta\pmod p,
\end{cases}
\tag{6}
\]

其中第一行按非降素数顺序剥尽 \(y\)-side excess；第二行取最小 safe prime，若
safe set 为空则取前两个 bad occurrences。两行都非空，并确定一个新的 primitive、
\(p\)-free endpoint

\[
u+v=R,
\qquad
(u,v)=1,
\qquad
p\nmid uv.
\tag{7}
\]

第一行有 \(u=(y,K)=D_yJ_y\)；第二行有 \(u=y/Q_{\rm pf}\)。以下所有
complete-excess 数据都从 (7) **重新**计算。

## 2. 一般二侧 endpoint theorem

对 \(i\in\{u,v\}\)，相对同一个 \(K\) 唯一定义

\[
Q_i=Q_K(i)
=\prod_{\nu_q(i)>\nu_q(K)}q^{\nu_q(i)},
\qquad
\beta_i=\frac{i}{Q_i},
\tag{8}
\]

\[
g_i=(\mathcal A,Q_i),
\qquad
E_i=\frac{Q_i}{g_i},
\qquad
D_i=\beta_i g_i.
\tag{9}
\]

### 定理 1（policy endpoint divisor-source 正规形）

式 (7)--(9) 满足

\[
\boxed{u=E_uD_u,\qquad v=E_vD_v,}
\tag{10}
\]

\[
\boxed{
D_u,D_v\mid K,
\qquad
(D_u,D_v)=1,
\qquad
D_uD_v\mid K,}
\tag{11}
\]

以及两条 cross-divisor gate

\[
\boxed{
D_u\mid pE_vD_v+1,
\qquad
D_v\mid pE_uD_u+1.}
\tag{12}
\]

canonical joined support 与倍率精确为

\[
\boxed{
M_\omega=\operatorname{lcm}(\mathcal A,Q_u,Q_v)
=\mathcal A E_uE_v,
\qquad
L_\omega=E_uE_v.}
\tag{13}
\]

而且

\[
E_i=1\Longleftrightarrow Q_i=1\Longleftrightarrow i\mid K.
\tag{14}
\]

故 terminal-first 的 bottom Type I 条件恰为 \(E_u=E_v=1\)。在 terminal miss
下 \(L_\omega>1\)。

**证明。** 若 \(b=\nu_q(i)\le\nu_q(K)\)，则 \(q^b\) 全留在
\(\beta_i\)，其指数不超过 \(K\) 容量。若
\(b>\nu_q(K)\ge a:=\nu_q(\mathcal A)\)，则完整 \(q^b\) 块进入 \(Q_i\)，
而 \(g_i\) 与 \(E_i\) 的指数分别为 \(a\) 与 \(b-a\)。所以 (10) 成立，且
\(D_i\) 在每个素数上的指数不超过 \(K\) 的指数，得到 \(D_i\mid K\)。
由 \((u,v)=1\)，两侧 \(D_i\) 互素，故 (11) 成立。

将 \(4K=p(u+v)+1\) 分别模 \(D_u,D_v\) 化简即得 (12)。同一逐素数讨论还表明
\(\operatorname{lcm}(\mathcal A,Q_i)/\mathcal A\) 在 excess 素数上的指数恰为
\(b-a=\nu_q(E_i)\)。两侧互素，所以倍率为 \(E_uE_v\)，得到 (13)。若
\(Q_i>1\)，其某个指数严格超过 \(K\)，从而也严格超过 \(\mathcal A\)，故
\(E_i>1\)；这证明 (14)。\(\square\)

### 推论 1（正确的 \(p^2\) actual-source gate）

policy endpoint 重复进入 \(a=1\) 的二阶 hard branch 当且仅当

\[
\boxed{E_uE_v=1+p^2\chi,\qquad \chi\in\mathbb Z_{>0}.}
\tag{15}
\]

在此条件下还有精确恒等式

\[
\boxed{
E_uR-E_u^2D_u-D_v=p^2\chi D_v,}
\tag{16}
\]

因而

\[
\boxed{E_u^2D_u+D_v\equiv E_uR\pmod {p^2}.}
\tag{17}
\]

式 (16) 只需把 \(R=E_uD_u+E_vD_v\) 乘以 \(E_u\)，再使用
\(E_uE_v=1+p^2\chi\)。这才是一般 \(L_\omega\) 的 source gate。

## 3. Full-capacity 的单侧特化

现在取 (6) 第一行。置

\[
u=Y_K=(y,K)=D_yJ_y.
\tag{18}
\]

已有 rank-stutter 尺寸门给 \(D_y\ge5\)，所以 \(u\ge5\)。因为 \(u\mid K\)，
定理 1 给出

\[
E_u=1,
\qquad
D_u=u.
\tag{19}
\]

若 companion \(v=R-u\) 也整除 \(K\)，立即 terminal。以下固定 terminal miss，并写

\[
v=(1+p^2\chi)d,
\qquad
d=D_v,
\qquad
\chi\ge1.
\tag{20}
\]

由 (11)--(12)，

\[
\boxed{
d\mid\gcd(K/u,pu+1),
\qquad
(u,d)=1,
\qquad
ud\mid K.}
\tag{21}
\]

当前 \(m=3,a_0=1\) root 精确满足

\[
R=1+p\tau,
\qquad
\tau=3+\sigma D_{\rm root}>0.
\tag{22}
\]

定义

\[
m=\frac{d+u-1}{p},
\qquad
c=\frac{pu+1}{d},
\qquad
w=\frac K{ud}.
\tag{23}
\]

这些量均为正整数：\(d\equiv v\equiv1-u\pmod p\) 给出 \(m\in\mathbb N\)；
(21) 给出 \(c,w\in\mathbb N\)。

### 定理 2（单侧 \(p^2\) factor-pair gate）

式 (20)--(23) 满足

\[
\boxed{\tau=m+p\chi d,}
\tag{24}
\]

\[
\boxed{4uw=c+p+p^3\chi.}
\tag{25}
\]

特别地，

\[
\boxed{
4u\mid c+p+p^3\chi,
\qquad
\frac K{ud}=\frac{c+p+p^3\chi}{4u}.}
\tag{26}
\]

此外

\[
\boxed{
d=\frac{mp^2+p+1}{p+c},
\qquad
u=\frac{mpc+c-1}{p+c},}
\tag{27}
\]

所以

\[
\boxed{p+c\mid mc^2-c+1.}
\tag{28}
\]

并有范围门

\[
\boxed{
d\le\frac{\tau-1}{p},
\qquad
u^2\ge p.}
\tag{29}
\]

**证明。** 由 \(d=mp+1-u\)、\(R-u=(1+p^2\chi)d\) 与
\(R=1+p\tau\) 比较，约去 \(p\) 即得 (24)。又
\(cd=pu+1\)、\(v=(1+p^2\chi)d\) 及 \(4K=p(u+v)+1\) 给出

\[
4udw=d\bigl(c+p(1+p^2\chi)\bigr),
\]

约去 \(d\) 得 (25)--(26)。联立 \(d=mp+1-u\) 与 \(cd=pu+1\)，直接解出
(27)；把第一式分子模 \(p+c\) 化简即得 (28)。式 (24) 与
\(m,\chi,d\ge1\) 给第一条范围。若 \(u^2<p\)，则既有 small-endpoint theorem
已证明 \(u\)-endpoint 必 terminal 或 canonical cofactor 严格小于 \(p-1\)，与
(20) 的 stutter 矛盾，故 \(u^2\ge p\)。\(\square\)

反向满足这些整数式仍不自动证明 \(d\) 是 canonical \(D_v\)：必须重算
(8)--(9)、actual path、terminal prefix 和 target typing。

## 4. Short \(Q_{\rm pf}\) 分支

在 (6) 第二行，置 \(P=Q_{\rm pf}\)，则

\[
u=\frac yP,
\qquad
v=x+(P-1)u.
\tag{30}
\]

这个节点仍是确定、primitive 且 \(p\)-free。若

\[
b_q=\nu_q(y),
\quad
k_q=\nu_q(K),
\quad
a_q=\nu_q(\mathcal A),
\quad
t_q=\nu_q(P),
\]

则 selected side 的 canonical 因子由

\[
\nu_q(E_u)=
\begin{cases}
b_q-t_q-a_q,&b_q-t_q>k_q,\\
0,&b_q-t_q\le k_q,
\end{cases}
\tag{31}
\]

\[
\nu_q(D_u)=
\begin{cases}
a_q,&b_q-t_q>k_q,\\
b_q-t_q,&b_q-t_q\le k_q
\end{cases}
\tag{32}
\]

唯一确定。但 companion \(v\) 必须从 (30) 重新计算 \(Q_v,E_v,D_v\)：旧
\(x\)-side block 可以退出，\(v\) 也可以引入新 block。因此

\[
\frac{L_1}{P}
\]

只是 formal multiplier，不是 \(L_\omega\)。若 \(E_u=1\) 或 \(E_v=1\)，交换方向后
回到第 3 节的单侧系统。真正尚未闭合的 short-word residual 是

\[
\boxed{
E_u,E_v>1,
\quad
E_uE_v=1+p^2\chi,
\quad
\text{并满足 (10)--(17) 与完整 canonical receipt}.}
\tag{33}
\]

## 5. 确定性、非重复与 E1--E5 边界

1. **Tie-break。** \(\ell\)、\(q_\star\)、最小 safe prime、两个 bad occurrences
   和非降 capacity word 均是 source 整数的确定函数；complete-excess block 由 gcd/modular
   power 公式确定，不需要目标解或搜索上界。
2. **Raw non-repetition。** 两行 policy 都以 \(P>1\) 把 selected coordinate 从
   \(y\) 严格降为 \(u=y/P\)。若最终无序节点只是 \(\{x,y\}\) 的交换，则必须
   \(u=x\mid y\)，而 \((x,y)=1\) 与 \(x>1\) 矛盾。非终止 target 又有
   \(M_\omega>\mathcal A\)，所以也不是同一个 typed chart。
3. **E1。** 在 source 已保存 \(\pi\) 且每个 priority prefix 有 miss receipt 时，
   (6) 是同一 source 的 forward suffix。尚未证明每个 actual proper-root state 都保存
   这样的 \(\pi\)。
4. **E2。** (8)--(13) 及 canonical \(R_M,K_M\) 是唯一整数 target。
5. **E3。** 仍须实际 serializer、owner tuple、scope、normalizer、state IDs 与
   target classifier 全部接受；现有 atomic theorem 只是条件表示定理。
6. **E4。** target 被接受后，两端标记集同为 \(\operatorname{Sol}(p)\)，恒等映射给
   全称 lift。
7. **E5。** \(L_\omega\not\equiv1\pmod p\) 时 high-support cofactor 严格小于
   \(p-1\)。若 (15) 成立，两端 local rank 均为 \((0,p-1)\)，没有 standalone T5
   ticket；checkpoint 只能留在一次最终严格的 macro 内，不能入 persistent queue。

## 6. 最小开放量词

令 \(\mathcal R_{\omega,p^2}^{\rm bind}\) 为满足第 1 节全部 source/path/priority
前提、terminal-first miss、(8)--(15) 和 canonical maximality 的 receipts。B5 的正确
验收式是

\[
\boxed{
\forall\rho\in\mathcal R_{\omega,p^2}^{\rm bind},
\quad
\operatorname{TerminalLift}(\rho)
\ \lor\
\exists T\,[E1\land E2\land E3\land E4
\land\Pi_{T5}(T)<\Pi_{T5}(S)].}
\tag{34}
\]

本卡只建立 \(\mathcal R_{\omega,p^2}^{\rm bind}\) 的 source normal form。它没有证明
该集合为空，也没有证明 (34)。因此状态必须保持

\[
\boxed{
\texttt{NORMAL\_FORM = ESTABLISHED},
\qquad
\texttt{B5 = OPEN\_MINIMAL\_RESIDUAL},
\qquad
\texttt{F3 = OPEN}.}
\tag{35}
\]

此外，pure-dyadic multiplier、source-path 全覆盖、其余 \(m,q\) slices、E3/F1 grammar
和所有 channel target 的 recursive closure 均不在本卡量词内。
