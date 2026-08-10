---
kind: claim
claim_id: type-I-high-support-rank-aware-sink-bundle-selector
title: 高支撑 F/G 状态的 rank-aware sink-bundle 有限选择器与 p=73 严格出口
statement: >-
  设真实 persistent F/G overflow 状态 H=(p,R,K;A) 满足 A>B_p、A|K，且其
  source path 到达有限 bottom sink SCC。对 SCC 每个定向节点的完整超额分解
  y=Q beta、x beta|K，令 M=lcm(A,Q)，并以规范目标余因子
  c_Q=K_M/M=(4M)^(-1) mod p 标价。所有满足 c_Q<K/A 的候选都给出完整
  E1--E5 宏边；选择最短 source path、再取最小 c_Q，得到规范有限选择器。若该集合
  为空，穷尽的 c_Q 表就是 complete-excess 宏族的严格容量 no-go，而不是全局 no-go。
  对实际 p=73 状态 (R,K;A)=(3743,68310;1518)，sink-minimum 的 Q=1871 使
  45->47 失败，但再走一条 q=1871 raw 边到 (2,3741,1)，取
  3741=1247*3、2*3|K，即得 M=1892946 与严格秩 45->44。完整 SCC 有 33 个
  合法候选，其中 22 个下降，故该高支撑 F 状态已有真实可提升出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - F-state
  - G-state
  - overflow
  - high-support
  - sink-SCC
  - complete-excess
  - rank-aware-selector
  - residual-capacity
  - well-founded-descent
sources:
  - reproduction: reproductions/type_i_high_support_rank_aware_sink_bundle_selector.py
    role: focused-finite-candidate-map-and-p73-strict-edge
visibility: public
last_checked: '2026-08-11'
---

# 高支撑 F/G 状态的 rank-aware sink-bundle 有限选择器与 p=73 严格出口

## 1. 候选宇宙

固定

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4},
\tag{1}
\]

并设

\[
H=(p,R,K;A,\sigma),
\qquad
4K=pR+1,
\qquad
A\mid K,
\qquad
A>B_p
\tag{2}
\]

是真实入队、内容寻址的 persistent F/G overflow state。假设绑定于同一 source state
ID 的 raw path 已到达 bottom node \(v_0\)，并进入有限 sink SCC
\(\Sigma\)。这里的 source path、owner scope \(\sigma\) 与每条 raw edge 都是来源
回执的一部分；只知道抽象 SCC 存在并不足够。

对每个 \(v=\{x,y\}\in\Sigma\) 的两种定向，按完整素数幂块唯一分解

\[
y=Q\beta,
\tag{3}
\]

其中 \(Q\) 是所有满足 \(v_q(y)>v_q(K)\) 的完整 \(q^{v_q(y)}\) 块之积，
\(\beta\) 是其余块之积。只保留满足

\[
Q>1,
\qquad
x\beta\mid K,
\qquad
(Q,x\beta)=1,
\qquad
Q\nmid K
\tag{4}
\]

的定向。令

\[
M_Q=\operatorname{lcm}(A,Q).
\tag{5}
\]

若 \(p\mid M_Q\)，该行没有规范 target，直接从候选宇宙删除；否则定义唯一

\[
c_Q\in\{1,\ldots,p-1\},
\qquad
4M_Qc_Q\equiv1\pmod p,
\tag{6}
\]

以及

\[
K_Q=M_Qc_Q,
\qquad
R_Q=\frac{4K_Q-1}{p}.
\tag{7}
\]

由 (6) 可知 \(0<R_Q<4M_Q\) 且 \(R_Q\equiv3\pmod4\)，所以 (7) 正是 support
\(M_Q\) 的 canonical chart。又因 \(A\mid K\) 而 \(Q\nmid K\)，式 (5) 自动满足
\(M_Q>A\)。

## 2. rank-aware 有限二分

高支撑 parent 的精确秩为

\[
\Lambda_p^\sharp(H)
=\left(0,\frac KA\right).
\tag{8}
\]

对候选 (3)--(7)，定义改善集合

\[
\mathcal I_\Sigma(H)
=\left\{(v,x,y,Q):c_Q<\frac KA\right\}.
\tag{9}
\]

### 定理 1（rank-aware sink-bundle 选择器）

若 \(\mathcal I_\Sigma(H)\ne\varnothing\)，先最小化从 \(v_0\) 到 \(v\) 的 raw
路径长度，再依次最小化 \(c_Q,v,Q\)。所得 path-anchored complete-excess 宏

\[
H\longrightarrow T_Q=(p,R_Q,K_Q;M_Q,\sigma)
\tag{10}
\]

是完整 E1--E5 边。若改善集合为空，则所有候选的有限 \(c_Q\) 表构成当前
\(\Sigma\) 上 complete-excess 宏族的严格容量 no-go。

**证明。** Sink SCC 有限且强连通，所以每个候选节点都带一条从 \(v_0\) 出发的有限
raw path；最短路和上述字典序最小元均存在。式 (3)--(4) 正是已建立的
path-anchored complete-excess receipt，故它支付 source/path、完整 bundle、lcm cargo
与恒等解提升。由 \(M_Q>A>B_p\)，target 的第一秩坐标仍为零，而

\[
\Lambda_p^\sharp(T_Q)=(0,c_Q).
\tag{11}
\]

式 (9) 因而恰好是 E5 的必要充分门，不是一个松的充分估计。若 (9) 为空，(3) 对每个
定向的完整超额块是唯一的，遍历有限 \(\Sigma\) 就穷尽了该宏族；因此输出的是族内
no-go。它不排除 total/direct cofactor、dual、Type I/II terminal 或其它重图表边。
\(\square\)

## 3. p=73：最小节点失败，但 rank-aware 选择成功

取已经由无界同图表支撑升级真实入队的状态

\[
p=73,
\qquad
(R,K;A)=(3743,68310;1518),
\qquad
B_{73}=1296.
\tag{12}
\]

它满足

\[
\Lambda_{73}^\sharp(H)=(0,45).
\tag{13}
\]

该状态的 F receipt 由素数次序 \((2,3,5,11,23)\) 下的

\[
z=(2,-1,-3,0,-2)
\tag{14}
\]

以及 raw path

\[
(4,198375,53)
\xrightarrow{2}(2,101059,27)
\xrightarrow{7}(535,14437,4)
\xrightarrow{14437}(1,3742,1)
\tag{15}
\]

给出。Bottom graph 有唯一 sink SCC，含 324 个节点。若机械选择 (15) 的最小节点，
则

\[
3742=1871\cdot2,
\qquad
Q=1871,
\qquad
c_Q=47,
\tag{16}
\]

于是得到已经验证的失败比较 \(45\to47\)。这只否定 sink-minimum-first，并不否定
整个 SCC。

在 (15) 后再走一条合法 raw edge：

\[
(1,3742,1)
\xrightarrow{1871}
(2,3741,1).
\tag{17}
\]

这里 shift 为 1870，且无 gcd reduction。新节点满足

\[
3741=3\cdot29\cdot43=3\cdot1247,
\qquad
Q=1247,
\qquad
\beta=3,
\qquad
2\beta=6\mid68310.
\tag{18}
\]

因此

\[
M_Q=\operatorname{lcm}(1518,1247)=1892946.
\tag{19}
\]

其 canonical target 为

\[
(R_Q,K_Q;M_Q)
=(4563815,83289624;1892946),
\qquad
K_Q=44M_Q.
\tag{20}
\]

真实 parent-to-target 比较现在是

\[
\boxed{(0,45)\longrightarrow(0,44),}
\tag{21}
\]

所以 (17)--(20) 修复了 minimum-node policy 的 persistence failure。

## 4. 完整容量图与选择规范

对 324 个 sink 节点的两个定向逐一应用 (3)--(7)，共有 33 个合法候选；其
target cofactor 多重集为

\[
\begin{aligned}
\{&6,8,9,11,14,15^{[2]},18^{[3]},20,23,26,30,32,34,35,\\
  &39^{[2]},41,44^{[2]},47,48,49,50,55,59,60^{[2]},61,68,71\}.
\end{aligned}
\tag{22}
\]

上标 \([m]\) 表示重数，不是幂。恰有 22 个候选满足 \(c_Q<45\)。按定理 1 的
“最短路径优先”规范，(17) 是唯一距离 1 的改善候选，因此选择 \(c_Q=44\)。若改用
“余因子最小优先”，唯一全局最小值是

\[
v=(297,3446),
\qquad
Q=1723,
\qquad
c_Q=6,
\tag{23}
\]

但从 (15) 的 anchor 最短需 13 条 raw edge。式 (22) 因而同时说明：证书长度与下降
幅度是可明确选择的成本函数，而不是继续固定在 sink 最小坐标。

## 5. E1--E5 与目标重分类

最短选择 (17)--(20) 的完整合同为：

| 合同 | 回执 |
|---|---|
| E1 | 已入队 source state ID、(14)--(15) 的 F/source path，以及同一 scope 下的 (17) |
| E2 | (18) 的完整超额分解、残余整除、(19) 的 lcm cargo 与 (20) 的 canonical chart |
| E3 | source 与 target 独立重算 normal form、内容地址及 F/G/hit；不继承旧类型 |
| E4 | 两端都表示 \(\operatorname{Sol}(4,73)\)，提升为恒等映射 |
| E5 | 式 (21) 的真实 persistent parent-to-target 严格下降 |

Target (20) 仍是 F，而不是从 source 继承 F 标签。事实上

\[
K_Q=2^3\cdot3\cdot11^2\cdot23\cdot29\cdot43,
\tag{24}
\]

其 centered box 有 2739 个不同剩余类且不含 \(-1\)。按素数次序

\[
(2,3,11,23,29,43)
\tag{25}
\]

的无界见证

\[
(-1,6,4,-7,-1,-8)
\tag{26}
\]

模 \(4563815\) 的值为 \(-1\)，故重新分类确为 F。

## 6. 推进与剩余边界

本结果把 (12) 从“高支撑 persistence sharp 反例”推进成一个实际严格出口，并证明
bottom selector 不能固定选择 sink 最小节点。对一般高支撑 F/G state，新的决定性
命题是改善集合 (9) 的非空性；若某状态的集合为空，有限 no-go 回执应立即转交
total/direct cofactor、dual、terminal 或其它良基分支，而不是继续重复最小节点扫描。

素数 \(p=73\) 本身已有 terminal-first 优先的直接 Type II 证书
\((20,219,4380)\)，所以 (21) 推进的是高支撑递归机制与良基边界，不是新增一个此前
未覆盖的素数。它的作用是严格否定“minimum-node failure 等于整个 sink failure”，
并给下一步全称非空性命题提供首个真实路径正控制。

本定理尚未证明每个高支撑 F/G sink 都有 \(c_Q<K/A\)，因此不是 Erdős--Straus 猜想的
全称证明。

聚焦验证：

```bash
python3 reproductions/type_i_high_support_rank_aware_sink_bundle_selector.py --verify
```
