---
kind: claim
claim_id: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
title: overflow 同图表支撑升级的无界精确秩与高支撑父端点边界
statement: >-
  设真实持久 overflow 状态满足 4K=pR+1、K=MC、R>p，并由绑定的
  determinant/source receipt 给出 A|M、M/A>=2。则无需 M<=B_p，保持同一
  (p,R,K) 图表并把 charged support 从 A 升为 M，恒以
  Lambda_p^sharp=(floor(B_p/A),K/A) 严格下降：第一坐标若不降，第二坐标仍从
  (M/A)C 严降到 C。该边保持 source scope 与 Sol(4,p)，因而在真实 source
  provenance 下给出完整 E1--E5。进一步，任一 A<=B_p 的 complete-excess bundle
  parent 可直接把 marked 或 overflow canonical target 都带支撑 M 入队，因为
  floor(B_p/M)<floor(B_p/A)；旧 M>B_p 例外被消除。但若 bundle overflow 只是
  A>B_p parent 的内部 receipt，真实 parent-to-target 的 E5 充要门是
  K_T/M<K_H/A，不能用 transient-to-target 的下降替代。p=73 的实际 F 路径从
  (R,K;A)=(3743,68310;1518) 到 bundle Q=1871，真实秩 (0,45)->(0,47)
  严格上升，而内部 receipt 的伪比较为 (0,87937)->(0,47)；故 persistence gate
  与低支撑假设均为 sharp。该反例只否定固定 sink-minimum candidate：对完整 sink
  SCC 做 rank-aware 选择后，一条额外 q=1871 raw 边给出 Q=1247 的真实宏边
  (0,45)->(0,44)，所以 p=73 高支撑状态已有严格出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-same-chart-support-promotion
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - complete-excess
  - same-chart
  - charged-support
  - residual-capacity
  - persistence-gate
  - well-founded-descent
  - F-state
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_overflow_unbounded_same_chart_promotion_persistence_boundary.py
    role: focused-unbounded-rank-low-support-composition-and-high-support-counterexample
visibility: public
last_checked: '2026-08-11'
---

# overflow 同图表支撑升级的无界精确秩与高支撑父端点边界

## 1. 无界同图表升级

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

设

\[
S=(p,R,K;A,\sigma)
\tag{2}
\]

是真实入队、内容寻址且带 scope \(\sigma\) 的 persistent overflow state。假设一个与
该 source state ID 绑定的 determinant/source receipt 重算出

\[
pn=4Md+1,
\qquad
R=4M-n>p,
\qquad
K=M(p-d)=MC,
\tag{3}
\]

其中

\[
C=p-d\in\{1,\ldots,p-1\},
\qquad
A\mid M,
\qquad
b:=\frac MA\ge2.
\tag{4}
\]

定义同图表 target

\[
T=(p,R,K;M,\sigma).
\tag{5}
\]

式 (3) 直接给出 \(M\mid K\)，所以 target support 合法。关键是 (5) 不需要旧条件
\(M\le B_p\)。采用已经建立的精确容量秩

\[
\Lambda_p^\sharp(p,R,K;D)
=\left(\left\lfloor\frac{B_p}{D}\right\rfloor,\frac KD\right),
\tag{6}
\]

有

\[
\left\lfloor\frac{B_p}{M}\right\rfloor
\le
\left\lfloor\frac{B_p}{A}\right\rfloor,
\qquad
\frac KM=C,
\qquad
\frac KA=bC>C.
\tag{7}
\]

若 (7) 的第一坐标严格下降，字典序下降已经成立；若第一坐标相等，第二坐标由
\(b\ge2\) 严格下降。因此无条件有

\[
\boxed{\Lambda_p^\sharp(T)<_{\rm lex}\Lambda_p^\sharp(S).}
\tag{8}
\]

这也覆盖 \(A>B_p\) 与 \(M>B_p\)：此时第一坐标可以同为零，但第二坐标仍支付 E5。

## 2. E1--E5 与 provenance 门

在 (2)--(4) 的 persistent-source 假设下，(5) 是完整的
`overflow_unbounded_same_chart_support_promotion_v1`：

| 合同 | 支付内容 |
|---|---|
| E1 | 真实 queued source、原 determinant/source receipt 与 scope \(\sigma\) 的绑定 |
| E2 | 同一图表满足 \(4K=pR+1\)，且新 support 满足 \(M\mid K\) |
| E3 | source/target 分别重算 normal form、F/G/hit 与内容地址；不得继承 chart-local 类型字段 |
| E4 | 两端均取 \(\operatorname{Sol}(4,p)\)，使用恒等映射 |
| E5 | 式 (8) 的精确字典序下降 |

若 source 或 target 已由 terminal-first 分类为 `hit`，直接返回 Type I 终端，不把它
继续入队。否则图表不变不等于状态 ID 不变，因为 charged support 从 \(A\) 严格增到
\(M\)，且 (8) 排除了 bookkeeping stutter。

这里的 source receipt 是实质假设。若 (3) 只是某个 parent adapter 内部生成、从未
作为 (2) 入队的 transient arithmetic record，则 (8) 比较了错误端点，不能支付真实
parent edge 的 E5。

## 3. 低支撑 complete-excess overflow 不再是例外

现在从一个真实 parent

\[
H=(p,R_H,K_H;A,\sigma),
\qquad
1\le A\le B_p,
\tag{9}
\]

直接考虑 complete-excess bundle receipt。令

\[
M=\operatorname{lcm}(A,Q),
\qquad
\frac MA\ge2,
\tag{10}
\]

并令其 canonical chart 为

\[
1\le R_M<4M,
\qquad
pR_M\equiv-1\pmod {4M},
\qquad
K_M=\frac{pR_M+1}{4}.
\tag{11}
\]

不论 \(R_M<p\) 还是 \(R_M>p\)，都定义真实宏 target

\[
T=(p,R_M,K_M;M,\sigma).
\tag{12}
\]

已有 complete-excess receipt 支付 (12) 的 source/path、lcm cargo、target arithmetic
与 \(\operatorname{Sol}(4,p)\) 恒等提升。E5 不再需要 \(M\le B_p\)。令
\(u=\lfloor B_p/A\rfloor\ge1\)。由 \(M/A\ge2\) 得

\[
\left\lfloor\frac{B_p}{M}\right\rfloor
\le
\left\lfloor\frac{B_p}{2A}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{13}
\]

所以 (12) 的第一秩坐标严格下降。原来的

\[
R_M<p\;\text{才是 edge},
\qquad
R_M>p\;\text{只记 overflow receipt}
\]

应更新为 target state class 的二分，而不是递归资格的二分：低支撑 parent 的两类
target 都有完整 E1--E5。特别地，任意 marked chart 满足
\(R_H<p\Rightarrow K_H\le B_p\)，故 \(A\mid K_H\) 自动推出 (9)。结合 bottom
sink-SCC 定理，任意 terminal-free marked F state 都给出严格 bundle edge；target
可以继续是 F、G 或 overflow，类型必须独立重算。

## 4. 高支撑 parent 的精确门

若 parent 已满足 \(A>B_p\)，则 \(M>A\) 使两端第一坐标都为零。真实宏

\[
H=(p,R_H,K_H;A)
\longrightarrow
T=(p,R_M,K_M;M)
\tag{14}
\]

在同一个 \(\Lambda_p^\sharp\) 下严格，当且仅当

\[
\boxed{\frac{K_M}{M}<\frac{K_H}{A}.}
\tag{15}
\]

这是必要充分条件，不是只需补一个充分估计。内部 overflow receipt 若暂时仍带旧
support \(A\)，其容量为 \(K_M/A=(M/A)(K_M/M)\)，总会因 \(M/A\ge2\) 在随后
同图表升级时下降；但该中间点不持久时，这个下降与 (15) 无关。

## 5. 实际 F 路径上的 sharp 反例

取

\[
p=73,
\qquad
(R_H,K_H;A)=(3743,68310;1518),
\qquad
B_{73}=1296.
\tag{16}
\]

有

\[
4K_H=73R_H+1,
\qquad
K_H/A=45,
\qquad
\Lambda_{73}^\sharp(H)=(0,45).
\tag{17}
\]

该图表是严格 F state。按素因子顺序

\[
(2,3,5,11,23),
\qquad
v(K_H)=(1,3,1,1,1),
\]

盒内不命中 \(-1\)，但无界见证

\[
z=(2,-1,-3,0,-2)
\tag{18}
\]

给出

\[
\frac{4}{198375}\equiv-1\pmod {3743},
\qquad
4+198375=53\cdot3743.
\]

完整 raw 迁移中有实际路径

\[
(4,198375,53)
\xrightarrow{2}
(2,101059,27)
\xrightarrow{7}
(535,14437,4)
\xrightarrow{14437}
(1,3742,1).
\tag{19}
\]

最后节点的 complete-excess 分解为

\[
3742=1871\cdot2,
\qquad
Q=1871,
\qquad
\beta=2,
\qquad
2\mid K_H.
\tag{20}
\]

于是

\[
M=\operatorname{lcm}(1518,1871)=2840178.
\tag{21}
\]

其 canonical target 为

\[
K_M=133488366=47M,
\qquad
R_M=7314431,
\tag{22}
\]

所以真实 parent 比较是

\[
\boxed{(0,45)\longrightarrow(0,47),}
\tag{23}
\]

严格上升。相反，若错误地把内部 receipt 当 source，就会得到

\[
\frac{K_M}{1518}=87937
\longrightarrow
\frac{K_M}{2840178}=47,
\tag{24}
\]

即一个巨大的伪下降。

式 (16) 不是孤立的不可达算术行：它正是已知
`lcm_cycle_step_0` overflow chart 在本定理无界升级后从 support \(66\) 升到
\(1518\) 的 target。因而 (23) 是新合法边之后会遇到的真实高支撑边界，而不是为了
否定过强命题临时拼出的无来源四元组。

## 6. 对统一选择器的推进

本定理删除了两个旧余项：

1. persistent overflow 的 `M>B_p` 同图表升级不再被拒绝；
2. 所有 \(A\le B_p\) complete-excess parent 的 overflow target 都可直接成为严格边。

新的精确余项是：已经进入 \(A>B_p\) 的 high-support overflow state 再产生 bundle
时，每个实际 candidate 都必须通过 (15)，或改走 total-cofactor、direct-cofactor、
dual、Type I/II terminal 或其它严格容量出口。式 (23) 证明不能把低支撑结论无条件
外推，也证明固定选择 sink 最小节点不是合法的全称策略。

后续 rank-aware sink-bundle 定理已经修复本卡的具体 \(p=73\) 状态：从
\((1,3742,1)\) 再走一条 \(q=1871\) raw 边到 \((2,3741,1)\)，其完整超额分解
\(3741=1247\cdot3\) 满足 \(2\cdot3\mid K_H\)，并产生

\[
(R_T,K_T;A_T)=(4563815,83289624;1892946),
\qquad
\Lambda_{73}^\sharp(T)=(0,44).
\]

完整 sink SCC 的 33 个合法候选中有 22 个满足 (15)。因此 (23) 仍是 persistence
gate 的 sharp 反例，却不再是该状态的递归阻塞。一般 high-support F/G overflow 的
剩余命题已收紧为 rank-aware 改善集合的非空性，或其有限 no-go 到其它出口的完备
分派；这仍不构成 Erdős--Straus 猜想的全称证明。详见
[高支撑 rank-aware sink-bundle 有限选择器](type-I-high-support-rank-aware-sink-bundle-selector.md)。

聚焦验证：

```bash
python3 reproductions/type_i_overflow_unbounded_same_chart_promotion_persistence_boundary.py --verify
```
