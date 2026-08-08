---
kind: claim
claim_id: type-I-qprimary-phase-affine-label-gcd-lift
title: q-primary Fourier 相位到仿射整数标签的 gcd—区间提升判据
statement: >-
  设 q^e 为过滤 Fourier 角色的 q-primary 阶，且独立 source-map 已把候选整数标签限制为 S={s0+h t | t∈Z}∩[L,U]，h>0。令 n=q^e、g=gcd(h,n)、Delta=gamma-s0 (mod n)。存在 phase lift 当且仅当 g|Delta 且同余解类在区间内非空；所有解、规范最小标签和精确槽数均有显式公式。对共享同一仿射标签进程的请求族，需求数超过重复度乘槽数时给出严格 PHASE_SLOT_HALL_DEFICIT。该判据只在 source-map 已声明为该仿射进程时成立，不把 Fourier 角色阶自动当作整数高度。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-primary-filtered-support-source-dichotomy
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
  - type-I
  - F-state
  - G-state
  - q-primary
  - Fourier
  - phase-lift
  - source-map
  - gcd
  - interval
  - Hall
  - capacity
  - proof-program
sources:
  - claim: type-I-target-fiber-primary-filtered-support-source-dichotomy
    role: source-difference-q-demand
  - claim: type-I-fourier-qprimary-phase-lift-capacity-dichotomy
    role: phase-tree-and-no-lift-boundary
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: shared-slot-capacity
  - reproduction: reproductions/type_i_qprimary_phase_affine_label_gcd_lift.py
    role: gcd-interval-and-slot-controls
visibility: public
last_checked: '2026-08-09'
---

# q-primary Fourier 相位到仿射整数标签的 gcd—区间提升判据

## 输入和 source-map 假设

固定一个 q-primary Fourier 相位

    gamma in Z/(q^e)Z,
    n = q^e.

这里的 gamma 可以来自目标纤维过滤缺口、固定层稳定子商或其它已经证明的
q-primary 角色投影。独立的整数 source-map 先声明候选标签为一条仿射进程

    S(s0,h;I) = {s=s0+h t : t in Z, L <= s <= U},
    I=[L,U] intersect Z,
    h>0.

相位 lift 的条件是

    s = gamma (mod n).                                  (1)

source-map 假设是本判据的输入；若真实标签不被这条进程穷尽，必须返回
PHASE_SOURCE_MAP_UNCLOSED，不能使用下面的空集结论。

## gcd—区间定理

令

    g = gcd(h,n),
    h1 = h/g,
    n1 = n/g,
    Delta = gamma-s0 (mod n).

取 Delta 的代表 0 <= Delta < n。则：

1. 若 Delta 不是 g 的倍数，(1) 无整数解，输出
   PHASE_GCD_OBSTRUCTED。
2. 若 g 整除 Delta，令

       t0 = (Delta/g) * h1^(-1) (mod n1),          (2)

   其中 n1=1 时 t0=0。所有整数解恰为

       t = t0 + n1 k,  k in Z.                    (3)

3. 令

       t_min = ceil((L-s0)/h),
       t_max = floor((U-s0)/h).

   若不存在 k 使 t_min <= t0+n1 k <= t_max，输出
   PHASE_INTERVAL_EMPTY。否则 phase-lift 集合恰为

       Lift(gamma;I)
       = {s0+h(t0+n1 k):
            ceil((t_min-t0)/n1) <= k <= floor((t_max-t0)/n1)}.   (4)

   其精确槽数是

       C_phase =
       max(0,
         floor((t_max-t0)/n1)
         - ceil((t_min-t0)/n1) + 1).                (5)

   规范标签取 (4) 中最小的 s；若需要全部候选，则 (4) 是无重复枚举。

因此在 source-map 已闭合时，局部 phase-lift 分派是互斥且穷尽的：

    PHASE_GCD_OBSTRUCTED
    PHASE_INTERVAL_EMPTY
    PHASE_LIFTED(C_phase, canonical_label).

## 证明

把 s=s0+h t 代入 (1)，得到一次线性同余

    h t = Delta (mod n).                              (6)

线性同余的标准判据给出可解当且仅当 gcd(h,n)=g 整除 Delta。可解时除以 g，
得到

    h1 t = Delta/g (mod n1),

且 h1 与 n1 互素，所以 h1 有逆元，得到 (2)--(3)。区间条件等价于
t_min <= t <= t_max；把 t=t0+n1 k 代入后得到 (4)，计数直接为整数区间
中 k 的个数，得到 (5)。证毕。

## 对跨状态容量的直接推论

若一个已通过 source-map 的状态族共享同一仿射进程和相位槽，允许每个实际标签
最多承接 mu 个独立请求，则它们在该局部进程上的可用容量至多为

    mu C_phase.                                      (7)

因此请求数 R 满足：

* R <= mu C_phase 时，(4) 可直接生成一个显式局部 phase-lift 槽表，再交给
  source-switch、SNF、范围和 Rado/Hall 门；
* R > mu C_phase 时，输出
  PHASE_SLOT_HALL_DEFICIT
  = (R,mu,C_phase,R-mu*C_phase)。

后一个缺口是实际标签进程内的严格容量阻碍，不是抽象 Fourier 幅度不足；它可以
作为跨状态 q 进容量切割的一个邻域上界。若不同状态有不同进程，应先分别求
候选槽，再用已有的带来源 Hall 图，不能把各进程的槽数相加。

## 与过滤源差分请求的接线

在 q-primary 过滤 Fourier 缺口的 SOURCE_DIFFERENCE_Q_DEMAND 分支中，先从角色
得到 gamma，再由独立 source-map 识别 s0、h 和区间 I。于是本判据把抽象请求
细分为：

1. PHASE_GCD_OBSTRUCTED：相位与 source-map 的步长模 q^e 不相容；
2. PHASE_INTERVAL_EMPTY：同余相容，但允许标签区间没有代表；
3. PHASE_LIFTED：存在具体整数标签，才允许支付 q-height、进入相位树或
   Hall/Rado 容量；
4. 多状态槽不足时的 PHASE_SLOT_HALL_DEFICIT。

这四类结果都保留 q、e、gamma、s0、h、I 和完整的最小整数见证。它们不自动
给出 Type I/II 证书：前两类需要另一个 source-map、支撑对偶出口或良基下降，
第三类还要通过整数 E1--E5，第四类还要转成可提升的 Type I/II/商 relay。

## 精确控制

| 控制 | (q,e) | (s0,h) | 区间 I | gamma | 输出 |
|---|---:|---:|---:|---:|---|
| gcd 可解且有标签 | (5,2) | (3,10) | [0,40] | 13 | PHASE_LIFTED，标签 13 |
| gcd 不相容 | (5,2) | (3,10) | [0,40] | 14 | PHASE_GCD_OBSTRUCTED |
| 同余可解但区间为空 | (7,2) | (4,14) | [0,10] | 18 | PHASE_INTERVAL_EMPTY |
| 共享槽严格缺口 | (5,2) | (3,10) | [0,40] | 13 | 2 请求、mu=1、槽数 1 |

第一个控制中 g=5、n1=5，解为 t=1 (mod 5)，区间内唯一标签是 13。第二个
控制的 Delta=11 不被 g=5 整除。第三个控制满足 g=7、t=1 (mod 7)，最小
标签 18 已超出上界 10。第四个控制与第一个控制共享同一槽，但两个独立请求
只能占用一个标签，缺口为 1。

## 研究边界

本引理首次把过滤 Fourier 角色到整数标签的局部提升写成精确的 gcd 和区间公式，
并给出可进入跨状态 Hall 图的槽容量。它仍要求 source-map 预先证明为该仿射进程；
没有证明所有 F/G 状态都满足该形式，也没有把局部缺口自动升级为原猜想的严格
递降。下一步是对实际 Type I/II source-map 建立这种仿射表示，或证明其失败时
能落入支撑对偶、SNF 障碍或已有稳定子商 relay。

## 聚焦复现

~~~bash
python3 reproductions/type_i_qprimary_phase_affine_label_gcd_lift.py --verify
~~~

复现只检查 gcd 可解性、规范标签、区间空集和共享槽容量，不做历史扫描。
