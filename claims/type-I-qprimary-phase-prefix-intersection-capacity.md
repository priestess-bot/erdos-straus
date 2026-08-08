---
kind: claim
claim_id: type-I-qprimary-phase-prefix-intersection-capacity
title: q-primary Fourier 相位与真实 q-prefix 的交集容量
statement: 设 q^e 为 Fourier 相位阶，source-map 标签为 s=s0+h t，且真实 q-prefix 由 q^j | p+4s 给出。两者的交集在同一 q-primary 模数上是一个精确的线性同余：它为空当且仅当 Fourier 相位与 prefix 中心在 q^min(e,j) 层不相容，非空时可用前一 gcd—区间公式计算全部标签和槽数。对共享该仿射进程的请求族，逐层需求超过重复度乘交集槽数时给出 PHASE_PREFIX_LAYER_DEFICIT；该缺口是实际 q 进容量切割输入。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-qprimary-phase-affine-label-gcd-lift
  - type-I-target-fiber-primary-filtered-support-source-dichotomy
  - type-II-cross-state-layered-rado-qcapacity-cut
topics:
  - type-I
  - type-II
  - q-primary
  - Fourier
  - q-prefix
  - phase-lift
  - affine-source-map
  - layered-capacity
  - Hall
  - proof-program
sources:
  - claim: type-I-qprimary-phase-affine-label-gcd-lift
    role: affine-label-gcd-intersection
  - claim: type-I-target-fiber-primary-filtered-support-source-dichotomy
    role: filtered-source-demand
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: layered-q-capacity-dispatch
  - reproduction: reproductions/type_i_qprimary_phase_prefix_intersection_capacity.py
    role: exact-prefix-intersection-controls
visibility: public
last_checked: '2026-08-09'
---

# q-primary Fourier 相位与真实 q-prefix 的交集容量

## 设置

固定一个 q-primary Fourier 相位

    gamma = s (mod q^e)

和一个已经声明闭合的仿射 source-map

    s = s0 + h t,
    t in Z,
    L <= s <= U,
    h>0.

对奇素数 q 和真实核心参数 p，q-prefix 层 j 的整数条件为

    q^j | p + 4s.

由于 q 不整除 4，该条件等价于

    s = beta_j (mod q^j),
    beta_j = -p * 4^(-1) (mod q^j).                 (1)

令 n_j=q^j，e_j=max(e,j)，以及

    delta_j = min(e,j).

## 相位—prefix 交集定理

Fourier 相位和 q-prefix 层 j 相容，当且仅当

    gamma = beta_j (mod q^delta_j).                  (2)

若 (2) 不成立，输出

    PHASE_PREFIX_CONFLICT(q,e,j,gamma,beta_j).

若 (2) 成立，令合并剩余类 c_j (mod q^e_j) 为

    c_j = gamma  (mod q^e)       when e >= j,
    c_j = beta_j (mod q^j)       when j > e.

则所有同时满足 Fourier 相位和 q-prefix 的标签恰为

    s = c_j (mod q^e_j),
    s = s0 + h t,
    L <= s <= U.                                  (3)

令

    g_j = gcd(h,q^e_j),
    Delta_j = c_j-s0 (mod q^e_j).

若 g_j 不整除 Delta_j，输出

    PHASE_PREFIX_GCD_OBSTRUCTED(q,e,j,g_j,Delta_j).

否则设

    h_j = h/g_j,
    n_j' = q^e_j/g_j,
    t_j = (Delta_j/g_j) h_j^(-1) (mod n_j').       (4)

把 (4) 代入区间 [L,U] 后，得到精确交集槽表

    S_j =
    {s0+h(t_j+n_j' k):
      ceil((t_min-t_j)/n_j') <= k
      <= floor((t_max-t_j)/n_j')}.                (5)

其大小 C_j=|S_j|；若 C_j=0，输出 PHASE_PREFIX_INTERVAL_EMPTY，
否则输出 PHASE_PREFIX_LIFTED(C_j, min S_j, S_j)。

## 逐层容量切割

令 R_j 是共享该仿射 source-map 的独立请求中要求至少 q^j 层的数量，令 mu
是一个具体标签最多承接的请求重复度。任何保持标签的逐层实现都必须满足

    R_j <= mu C_j.                                  (6)

若

    R_j > mu C_j,

则输出严格的

    PHASE_PREFIX_LAYER_DEFICIT
    (q,j,R_j,mu,C_j,R_j-mu*C_j).                    (7)

该缺口可直接作为分层 Rado—q 进容量切割的一个邻域上界；它先于普通 Hall
匹配和 Kneser surplus。若各请求有不同 source-map，应分别构造 S_j，再在带来源
标签的兼容图中取邻域，不能把不同进程的 C_j 相加。

## 证明

由 q 不整除 4，4 在 Z/q^j Z 中可逆，故 q^j | p+4s 当且仅当 (1)。两个同
q 的同余类存在共同解，当且仅当它们在较小模数 q^min(e,j) 上相等，得到 (2)。
同余模数嵌套时，较高阶的剩余类唯一决定合并类 c_j，得到 (3)。

把 s=s0+h t 代入 (3)，得到

    h t = Delta_j (mod q^e_j).

线性同余的 gcd 判据给出 (4) 的可解性和全部参数解；再与
t_min <= t <= t_max 相交，得到 (5) 和精确槽数 C_j。每个标签最多被 mu 个
独立请求使用，因此逐层需求至多为 mu C_j，得到 (6)；反向不等式即 (7)。
证毕。

## 精确控制

取 p=23、q=5、s0=3、h=10、I=[0,220]、gamma=13 (mod 25)。此时

    beta_1 = 3 (mod 5),
    beta_2 = 13 (mod 25),
    beta_3 = 88 (mod 125).

Fourier 相位与 j=1、2 均相容，而 j=3 也相容，因为 88=13 (mod 25)。
交集槽分别为

    S_1=S_2={13,63,113,163,213},
    S_3={213}.

| 控制 | 层 j | 交集槽 | 输出 |
|---|---:|---|---|
| 相位—prefix 一层 | 1 | 五个标签 | PHASE_PREFIX_LIFTED |
| 相位—prefix 二层 | 2 | 五个标签 | PHASE_PREFIX_LIFTED |
| 高层稀疏 | 3 | 仅 213 | PHASE_PREFIX_LIFTED，C_3=1 |
| 高层双请求 | 3 | 2 个请求、1 个槽、mu=1 | PHASE_PREFIX_LAYER_DEFICIT |

另取同一 p、q、e、gamma，但把 j=2 的 prefix 中心改成 beta=3 (mod 25)。
此时 3 不等于 13 (mod 5)，直接输出 PHASE_PREFIX_CONFLICT；即使 Fourier
phase-lift 本身有五个标签，也不能把它们算成真实 q^2 槽。

## 与统一选择器的接线

对过滤 Fourier 缺口先执行：

    SOURCE_DIFFERENCE_Q_DEMAND
      -> affine phase gcd gate
      -> phase/prefix intersection
      -> layered Rado/Hall
      -> FIBER_REALIZED Kneser or annihilator/descent.

第一层和第二层交集相容只说明存在整数标签；高层槽数可能骤减，如控制中的
C_3=1。故不能从角色阶 e=2 直接收取两个独立 q 层，必须逐层使用 (5)--(7)。

## 研究边界

本引理完成了 Fourier 相位、整数 source-map 和真实 q-prefix 的精确交集容量
公式，但仍以仿射 source-map 已闭合为前提。它不证明所有状态都有这种 source-map，
也不保证 PHASE_PREFIX_LAYER_DEFICIT 已自动具有整数递降；后续仍需调用
source-column closure、SNF/CRT 和 Type I/II/稳定子 relay。

## 聚焦复现

~~~bash
python3 reproductions/type_i_qprimary_phase_prefix_intersection_capacity.py --verify
~~~

复现只检查相位—prefix 嵌套同余、精确逐层标签、冲突分支和高层容量缺口。
