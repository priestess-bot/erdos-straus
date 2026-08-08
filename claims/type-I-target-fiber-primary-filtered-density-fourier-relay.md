---
kind: claim
claim_id: type-I-target-fiber-primary-filtered-density-fourier-relay
title: 目标纤维 q-primary 过滤密度与稳定子商 Fourier 桥
statement: 设 X 是有限目标群 H 的角色子群、K=X^perp，m=|X|，并以目标陪集 y+K 的盒计数 C_{y,K} 代替精确纤维计数。若精确纤维超过 2^r 则已有近邻终端成立；否则，C_{y,K}>2^r 输出商饱和，C_{y,K}<=2^r 且盒体积 V>m*2^r 时必有 X 内非平凡角色的显式负实 Fourier 缺口，若 V<=m*2^r 则得到 X 过滤的低密度容量界。特别地，X 为 q-primary 子群时，商饱和与密度缺口都带 q-primary 过滤标签，且密度缺口的角色自动是 q-primary；X={1} 时退化为空过滤。该桥不自动完成整数 lift，但把固定层稳定子商、q 进角色和容量预算统一到同一正交恒等式。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-density-neighbor-fourier-trichotomy
  - type-I-target-fiber-fourier-overflow-generating-function
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-source-fiber-cyclic-primary-digit-terminal
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - target-fiber
  - q-primary
  - stabilizer
  - quotient
  - Fourier
  - density
  - capacity
  - relay
  - proof-program
sources:
  - claim: type-I-target-fiber-density-neighbor-fourier-trichotomy
    role: exact-fiber-density-branch
  - claim: type-I-target-fiber-fourier-overflow-generating-function
    role: box-Fourier-sum
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: annihilator-quotient-interface
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: q-primary-capacity-routing
  - reproduction: reproductions/type_i_target_fiber_primary_filtered_density_fourier_relay.py
    role: q-primary-filtered-four-branch-receipt
visibility: public
last_checked: '2026-08-09'
---

# 目标纤维 q-primary 过滤密度与稳定子商 Fourier 桥

## 设置

令 H 为有限阿贝尔群，g_1,...,g_r 为 H 中的生成元，令

    B_nu = product_i [-nu_i,nu_i] intersect Z^r,
    V = |B_nu| = product_i (2 nu_i + 1),
    phi(z) = product_i g_i^(z_i).

固定目标 y in H，并记精确目标纤维为

    N_y = #{z in B_nu : phi(z) = y},
    T_r = 2^r.

现在预先选择一个非平凡角色子群 X <= widehat(H)，令

    m = |X| > 1,
    K = X^perp = {h in H : chi(h) = 1 for every chi in X}.

目标陪集计数为

    C_(y,K) = #{z in B_nu : phi(z) in y + K}.

由于有限阿贝尔对偶性，|H/K|=|X|=m。对 chi in X 仍使用未归一化盒 Fourier 和

    Bhat(chi) = sum_(z in B_nu) chi(phi(z)).

称 X 是 q-primary 的，是指 X 中每个角色的阶都是 q 的幂。此时 K 是去掉
q-primary 角色所看见信息后的稳定子核，所有由 X 产生的缺口证书都自动带有
q-primary 标签。

## 过滤四分支引理

对固定的 H、生成元、盒、目标和 X，选择器按下列互斥顺序输出：

1. 若 N_y > T_r，输出 NEIGHBOR_TERMINAL。该分支先于任何过滤，因而保留已有
   目标精确纤维近邻和广义 2^j 偶终端。
2. 若 N_y <= T_r 但 C_(y,K) > T_r，输出
   PRIMARY_QUOTIENT_BOX_SATURATED（当 X 为 q-primary 时）或其无主层标签的
   QUOTIENT_BOX_SATURATED。这里饱和的是商 H/K 中的目标陪集，而不是
   精确目标 y；它是稳定子商已经聚集足够多盒点的回执，不能直接冒充 Type II
   整数命中。
3. 若 N_y <= T_r、C_(y,K) <= T_r 且 V > m T_r，则存在非平凡 chi in X，使

       -Re(conj(chi(y)) Bhat(chi))
       >= (V - m C_(y,K))/(m - 1) > 0.                 (1)

   按左端最大、角色阶最小、固定群坐标字典序选择 chi，得到规范的
   Q_PRIMARY_FILTERED_FOURIER_DEFICIT。若 X 是 q-primary 子群，chi 也必为
   q-primary。
4. 若 N_y <= T_r、C_(y,K) <= T_r 且 V <= m T_r，输出
   Q_PRIMARY_FILTERED_BOX_CAPACITY，并保留严格容量界

       V <= 2^r |X|.                                   (2)

   该界是过滤层的状态预算，不是空白或失败标记，可以与 q 进层、固定层稳定子
   或跨状态共享需求比较。

四分支覆盖所有情况。若 K={1}，则 X 是整个对偶群，C_(y,K)=N_y，第二分支
自动消失，恢复整个目标群上的目标纤维近邻—密度—Fourier 三分。若 X={1}，
m=1，不使用第三分支并退化为单个过滤容量条件。

## 证明

角色子群 X 的正交关系是

       sum_(chi in X) chi(h) = m  if h in K,
                              0  otherwise.             (3)

因此

       sum_(chi in X) conj(chi(y)) Bhat(chi)
       = sum_(z in B_nu) sum_(chi in X) chi(phi(z)-y)
       = m C_(y,K).                                      (4)

平凡角色项等于 V，故

       sum_(chi in X, chi != 1)
         Re(conj(chi(y)) Bhat(chi))
       = m C_(y,K) - V.                                  (5)

在第三分支中 C_(y,K) <= T_r 且 V > m T_r，所以右端严格为负。X 中有
m-1 个非平凡角色，其中至少一个的实部不大于平均值

       -(V - m C_(y,K))/(m - 1),

得到 (1)。第四分支正是第三分支的密度条件不成立时的互补不等式，给出 (2)。
第一、二分支是计数阈值的优先级判断，所以与后两支互斥。证毕。

## 稳定子商与 q-primary 路由

令 pi:H -> H/K 为商映射。C_(y,K) 正是盒点在商目标 pi(y) 的纤维计数，
而 H/K 的阶等于 m。因此本引理把固定层稳定子约化的商目标直接变成过滤盒
计数：商纤维饱和时保留稳定子商回执，商纤维不饱和但体积过大时把缺口限制在
预选的角色子群 X 内。

若 X 是 q-primary 子群，第三分支产生的角色可以直接送入已有的 q-primary
相位、源关系格或 q-height 容量接口；不需要先从整个对偶群的任意角色中猜测
其主分量。第四分支则给出同一 X 过滤下的精确容量预算，可作为跨 F/G 状态
共享 q 需求的一个输入。这个桥仍不提供从有限角色到整数除子参数的自动提升：
来源标签、CRT/SNF 可实现性、范围条件和 E1--E5 仍需单独证明。

## 精确控制

下表中的循环群控制以 C_6 的奇偶商实现 q=2 的角色过滤：

| 控制 | H、生成元 | 盒预算 | y | X 阶 | 计数 (N_y,C_(y,K)) | 输出 |
|---|---|---:|---:|---:|---:|---|
| q-primary 缺口 | C_6, g_1=1 | (2) | 1 | 2 | (1,2) | Q_PRIMARY_FILTERED_FOURIER_DEFICIT |
| 商陪集饱和 | C_6, g_1=1 | (3) | 1 | 2 | (1,4) | PRIMARY_QUOTIENT_BOX_SATURATED |
| q-primary 容量 | C_6, g_1=1 | (1) | 1 | 2 | (1,2) | Q_PRIMARY_FILTERED_BOX_CAPACITY |
| 精确近邻优先 | C_3, (g_1,g_2)=(1,1) | (2,2) | 0 | 3 | (9,9) | NEIGHBOR_TERMINAL |

在第一个控制中 V=5、m=2、C_(y,K)=2，故 (1) 的下界为
(5 - 2*2)/(2 - 1)=1。唯一非平凡 q-primary 角色为 chi(x)=(-1)^x，
并且

       -Re(conj(chi(1)) Bhat(chi)) = 1,

恰好达到该下界。第二个控制的商陪集有四个点而 T_r=2，故即使精确目标
纤维只有一个点，也必须先输出商饱和。第三个控制满足 V=3 <= 2*2，命中
过滤容量。第四个控制满足 N_y=9>2^2，近邻终端优先于过滤。

## 研究边界

这条引理新增了一个严格的 q-primary 过滤选择器，但仍不是 Erdős--Straus
猜想的全称证明。它把下一个决定性缺口压缩为两个可检验方向：

* 证明第三分支的过滤 Fourier 角色带有可提升的来源标签，或由 q-primary
  相位直接构造 Type I/II 短证书；
* 证明第四分支的过滤容量在跨 F/G 状态共享需求下必然超载，或者沿稳定子商
  产生严格良基下降。

若某个 q-primary 过滤的商陪集饱和却不能提升，必须保留
PRIMARY_QUOTIENT_BOX_SATURATED 作为独立的中间状态，不能把它误写成原模数
命中或完整递降。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_fiber_primary_filtered_density_fourier_relay.py --verify
~~~

复现脚本只检查四个控制的精确计数、近邻优先级、q-primary Fourier 下界和
过滤容量不等式，不执行历史范围扫描。
