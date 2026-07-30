---
kind: claim
claim_id: type-I-linear-private-carrier-isolation-criterion
title: 线性源私有 q 载体的唯一性判据与迁移边界
statement: 设正整数 t_0,u_0,R_0 给出 p=t_0+u_0+t_0u_0R_0，且 t_0R_0+1=qd_0，其中 q 为素数且 0<t_0,R_0<q，并令 n_0=(p-t_0)/q=u_0d_0。若 d_0+R_0>n_0-1，且 d_0 是 n_0 中满足 D>=d_0、D≡d_0 (mod t_0) 的唯一正因子，则在所有正整数线性源 p=t+u+tuR 中，q|tR+1 的有序载体唯一为 (t,u,R)=(t_0,u_0,R_0)。交换两个坐标后同一定理也覆盖每个源的第二块。对 (p,q)=(99151369,115561) 与 (487572409,6965317)，完整去重带标签块谱的 q 进总高度因而都恰为 1，真实 q 碰撞图没有边；候选标签差或模数差不能在这两个方向上解释为实际载体迁移收费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-block-label-collision
  - type-I-linear-block-divisor-q-adic-capacity
  - type-I-linear-support-window-qadic-locality-boundary
  - type-I-ordered-r-migration-min-cost-duality
topics:
  - type-I
  - linear-source
  - private-carrier
  - q-adic
  - uniqueness
  - collision-graph
  - migration-boundary
  - proof-program
sources:
  - claim: type-I-linear-block-label-collision
    role: necessary-collision-congruences
  - claim: type-I-linear-block-divisor-q-adic-capacity
    role: divisor-capacity-context
  - claim: type-I-ordered-r-migration-min-cost-duality
    role: migration-cost-interface
visibility: public
last_checked: '2026-07-30'
---

# 线性源私有 \(q\) 载体的唯一性判据与迁移边界

## 唯一性判据

设正整数 \(t_0,u_0,R_0\) 给出正整数 \(p\)，满足

\[
p=t_0+u_0+t_0u_0R_0,
\qquad
t_0R_0+1=qd_0,
\tag{1}
\]

其中 \(q\) 为素数、\(0<t_0,R_0<q\)，并记

\[
n_0=\frac{p-t_0}{q}=u_0d_0.
\tag{2}
\]

假设：

\[
d_0+R_0>n_0-1,
\tag{3}
\]

并且 \(d_0\) 是 \(n_0\) 的满足

\[
D\ge d_0,
\qquad
D\equiv d_0\pmod {t_0}
\tag{4}
\]

的唯一正因子。则对任意正整数线性源

\[
p=t+u+tuR,
\tag{5}
\]

若 \(q\mid tR+1\)，必有

\[
\boxed{(t,u,R)=(t_0,u_0,R_0).}
\tag{6}
\]

这里把 \((t,u)\) 看成有序坐标；因此结论断言的是带标签块
\(B(t,R)=tR+1\) 在完整有序源谱中的唯一性，而不只是某个固定标签或有限
\(R\)-窗口内的唯一性。一个无序源的两个块都在量词范围内：检查
\(uR+1\) 时只需把该源重写为有序三元组 \((u,t,R)\)。仓库的载体谱按
\((\text{label},R,B)\) 去重；交换列举顺序不会制造第二份独立容量。若一般源出现
\(t=u\) 的重复坐标，则其 occurrence 重数必须另行计入容量，本判据不把这种重数
解释成两个不同迁移顶点。下面两个实例都有 \(t_0\ne u_0\)，且另一坐标块不被 \(q\)
整除，所以不存在这一歧义。

## 证明

由 (5) 得

\[
p-t=u(tR+1).
\tag{7}
\]

若 \(q\mid tR+1\)，则 \(t\equiv p\pmod q\)。另一方面，(1) 给出
\(p\equiv t_0\pmod q\)。由 \(0<t_0<q\) 可写

\[
t=t_0+kq,
\qquad k\ge0.
\tag{8}
\]

又因 \(t_0R_0\equiv-1\pmod q\)，\(t_0\) 在模 \(q\) 下可逆；结合
\(tR\equiv-1\pmod q\) 与 \(t\equiv t_0\pmod q\)，得到

\[
R=R_0+\ell q,
\qquad \ell\ge0,
\tag{9}
\]

其中 \(0<R_0<q\) 保证 \(\ell\) 非负。将 (8)--(9) 代回载体块，得到

\[
tR+1
=q\bigl(d_0+kR_0+\ell t_0+k\ell q\bigr).
\tag{10}
\]

再把 (7) 除以 \(q\)，有

\[
n_0-k
=u\bigl(d_0+kR_0+\ell t_0+k\ell q\bigr).
\tag{11}
\]

若 \(k\ge1\)，右侧括号至少为 \(d_0+R_0\)，故由 (3)

\[
u\bigl(d_0+kR_0+\ell t_0+k\ell q\bigr)
\ge d_0+R_0
>n_0-1
\ge n_0-k,
\]

与 (11) 矛盾。因此 \(k=0\)。此时

\[
n_0=u(d_0+\ell t_0).
\tag{12}
\]

所以 \(D=d_0+\ell t_0\) 是 \(n_0\) 的正因子，并满足 (4)。因子唯一性迫使
\(D=d_0\)，从而 \(\ell=0\)，再由 (12) 得 \(u=u_0\)。式 (6) 得证。

## 两个完整源谱实例

### \(p=99151369\)

取

\[
(t_0,u_0,R_0,q,d_0,n_0)
=(31,39,82011,115561,22,858).
\]

直接有

\[
31\cdot82011+1=22\cdot115561,
\qquad
858=39\cdot22.
\]

并且 \(22+82011>857\)。在 \(858\) 的全部正因子中，唯一满足
\(D\ge22\) 且 \(D\equiv22\pmod {31}\) 的是 \(D=22\)。因此完整正整数
线性源谱中唯一的 \(115561\)-可除块为

\[
B(31,82011)=2542342=22\cdot115561.
\tag{13}
\]

交换坐标后的另一块为
\(B(39,82011)=3198430\)，不被 \(115561\) 整除。

### \(p=487572409\)

取

\[
(t_0,u_0,R_0,q,d_0,n_0)
=(219,7,318051,6965317,10,70).
\]

此时

\[
219\cdot318051+1=10\cdot6965317,
\qquad
70=7\cdot10,
\]

且 \(10+318051>69\)。由于 \(n_0=70<10+219\)，\(70\) 的正因子中
唯一满足 \(D\ge10\) 且 \(D\equiv10\pmod {219}\) 的是 \(D=10\)。因此唯一的
\(6965317\)-可除块为

\[
B(219,318051)=69653170=10\cdot6965317.
\tag{14}
\]

交换坐标后的另一块为
\(B(7,318051)=2226358<6965317\)，故同样不被 \(q\) 整除。

两式中的余因子 \(22,10\) 都小于对应的 \(q\)，所以两个唯一块的 \(q\)-进高度均
恰为 1。该证明遍历所有正整数源，甚至没有使用坐标奇性或
\(R\equiv3\pmod4\) 的限制；因此对仓库使用的完整线性源子谱当然也成立。

## 迁移收费边界

把真实 \(q\)-碰撞图的顶点定义为所有满足 \(q\mid B(t,R)\) 的不同带标签块
\((t,R,B(t,R))\)，并只在两个实际共享 \(q\) 的不同顶点之间连边；同一顶点的
occurrence 重数和 \(q\)-进高度属于容量权重，不产生自迁移边。上面的两个实例中，
唯一顶点都只出现一次且高度为 1，故图没有边、总高度也恰为 1。
因此：

1. 同标签模数差或异标签差的 \(q\)-进整除仍是实际碰撞的必要条件；
2. 反向推论不成立，单独的 \(q\mid(t-t')\) 或 \(q\mid(R-R')\) 只是候选菜单；
3. 有序 \(R\) 运输对偶在这两个重方向上没有可供收费的实际迁移边。

这不是容量路线的失败，而是把缺失引理定位得更准确。进一步的
[跨状态支撑退出与共享两尾等价](type-I-linear-private-carrier-support-exit-marked-equivalence.md)
已经证明：除原无序源状态外，其它线性源的 \(K\) 都不含该私有 \(q\)；而共享两尾的
marked lift 与同一 \(R\) 上的 Type I 命中是同一张证书，不能充当独立第三分支。
因此若目标纤维强制使用一个容量不足且完整谱私有的 \(q\) 坐标，统一选择器仍必须证明
它产生另一合法状态的 Type I 命中、独立 Type II 证书或改变标记/支撑且严格可提升的
递降。这里把该待证存在性接口称为**私有载体逃逸引理**；本卡不声称已经证明这个全称
逃逸结论。
