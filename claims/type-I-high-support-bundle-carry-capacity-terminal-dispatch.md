---
kind: claim
claim_id: type-I-high-support-bundle-carry-capacity-terminal-dispatch
title: 高支撑 bundle 的精确 carry 容量门、空改善反例与终端分派
statement: >-
  设 canonical 高支撑状态 H=(p,R,AC;A) 满足 A>B_p、1<=C<p。任一合法
  complete-excess 候选 M=AL 的目标余因子唯一写成
  c=(C+p h_L)/L，其中 0<=h_L<L 且 C+p h_L≡0 (mod L)；因此 E5 等价于
  Delta_L(C)=p h_L-C(L-1)<0，等号恰当且仅当 L≡1 (mod p)。对固定
  L≠1 (mod p)，C=1,...,p-1 中恰有一半下降、一半上升，总漂移为零，故 sink
  强连通本身不能推出改善集合非空。事实上存在具完整 E1--E5 宏来源、但被
  terminal-first 抢占的 p=73 高支撑 F 状态 (R,K;A)=(143,2610;1305)、C=2；
  其唯一 24 节点 bottom sink 的 10 个
  合法候选全部满足 c>=6，故改善集严格为空。该素数已有直接 Type II 证书
  (20,219,4380)，所以统一选择器的完整输出是 CARRY_NO_GO 后由 terminal-first
  抢占，而不是递归失败。作为正控制，既有 C=44 F 状态沿七条显式 raw 边取
  Q=1521269，得到新的严格 44->2 E1--E5 边及独立 F 目标证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-rank-aware-sink-bundle-selector
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-unified-terminal-first-selector-contract
  - denominator-escape-state-contract
topics:
  - type-I
  - F-state
  - G-state
  - overflow
  - high-support
  - complete-excess
  - carry-capacity
  - strict-counterexample
  - terminal-first
  - well-founded-descent
sources:
  - reproduction: reproductions/type_i_high_support_bundle_carry_capacity_terminal_dispatch.py
    role: focused-carry-theorem-empty-capacity-counterexample-and-positive-edge
visibility: public
last_checked: '2026-08-11'
---

# 高支撑 bundle 的精确 carry 容量门、空改善反例与终端分派

## 1. 规范目标的精确 carry 公式

固定奇素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4},
\tag{1}
\]

并设

\[
H=(p,R,K;A),
\qquad
K=AC,
\qquad
A>B_p,
\qquad
1\le C<p
\tag{2}
\]

是 canonical 高支撑状态。由 \(4K=pR+1\) 有

\[
4AC\equiv1\pmod p.
\tag{3}
\]

取任一已经通过 source/path、完整超额分解和 residual divisibility 的合法
complete-excess 候选，并写

\[
M=\operatorname{lcm}(A,Q)=AL,
\qquad
L\ge2,
\qquad
p\nmid L.
\tag{4}
\]

其 canonical target 余因子 \(c\in\{1,\ldots,p-1\}\) 满足

\[
4ALc\equiv1\pmod p,
\qquad
c\equiv CL^{-1}\pmod p.
\tag{5}
\]

### 定理 1（canonical bundle carry gate）

令 \(h_L\in\{0,\ldots,L-1\}\) 是唯一满足

\[
C+ph_L\equiv0\pmod L
\tag{6}
\]

的整数，则

\[
\boxed{c=\frac{C+ph_L}{L}}
\tag{7}
\]

且与真实第二秩坐标差同号的精确缩放量为

\[
\boxed{
\Delta_L(C):=L(c-C)=ph_L-C(L-1).
}
\tag{8}
\]

因此

\[
c<C\iff \Delta_L(C)<0,
\qquad
c=C\iff L\equiv1\pmod p,
\qquad
c>C\iff \Delta_L(C)>0.
\tag{9}
\]

**证明。** 因 \((p,L)=1\)，式 (6) 有唯一标准解。又有

\[
0<C+ph_L<pL,
\]

所以式 (7) 是 \(1,\ldots,p-1\) 中的整数，并由 (3) 立即满足 (5)，故必为唯一
canonical target 余因子。展开 \(L(c-C)\) 即得 (8)。若 (8) 为零，则
\(p\mid C(L-1)\)；因 \(1\le C<p\)，这等价于 \(L\equiv1\pmod p\)。反向取
\(L=1+kp\) 时，\(h_L=Ck<L\)，代回即得等号。其余符号给出 (9)。\(\square\)

这把旧的“重算每个 canonical chart”压缩为一个精确的整数 carry gate。注意
\(h_L\) 不是路径长度，也不是 SCC 绕数；它只记录把 \(C\) 提升到首个可被 \(L\)
整除的 \(C+ph\) 所需的 carry。

## 2. 容量映射、对称性与三个充分条件

只看合法候选乘子在 \((\mathbb Z/p\mathbb Z)^\times\) 中的不同剩余类

\[
E_H=\{L\bmod p:\ L\text{ 来自合法 path-anchored bundle}\}.
\tag{10}
\]

目标余因子集合恰为

\[
\mathcal C_H=C E_H^{-1}
\subseteq(\mathbb Z/p\mathbb Z)^\times,
\tag{11}
\]

其中每个剩余类取 \(1,\ldots,p-1\) 的标准代表。候选重数仍用于 provenance 和
tie-break，但不增加 (11) 的代数容量。

### 定理 2（half-descent 对称性）

固定 \(L\not\equiv1\pmod p\)，令

\[
T_L(C)=\langle CL^{-1}\rangle_p.
\tag{12}
\]

则 \(T_L\) 没有不动点，并且

\[
T_L(p-C)=p-T_L(C).
\tag{13}
\]

所以 \(C=1,\ldots,p-1\) 中恰有 \((p-1)/2\) 个满足 \(T_L(C)<C\)，另有
\((p-1)/2\) 个满足 \(T_L(C)>C\)，且

\[
\sum_{C=1}^{p-1}(T_L(C)-C)=0.
\tag{14}
\]

**证明。** 不动点会给出 \(C(1-L)\equiv0\pmod p\)，与假设矛盾。式 (13) 由
乘法线性直接得到；每对 \(\{C,p-C\}\) 中一个下降、一个上升。最后 \(T_L\) 是非零
剩余类的置换，故两边总和相等。\(\square\)

这严格排除了“某个固定 bundle 乘子对所有余因子都有同向改善”。更重要的是，sink
强连通只控制模 \(R\) 的 raw 转移；它没有自动提供模 \(p\) 的 carry 符号。

式 (11) 仍给出三个可直接调用的充分条件：

1. **不同剩余类鸽巢门。** 若 \(|E_H|>p-C\)，则 \(\mathcal C_H\) 不可能全部落在
   \(\{C,C+1,\ldots,p-1\}\)，故必有 \(c<C\)。
2. **反足对门。** 若 \(E_H\) 同时含 \(L\) 与 \(-L\)，且
   \(C>(p-1)/2\)，则两个目标为 \(c,p-c\)，至少一个不超过
   \((p-1)/2<C\)。
3. **整除 carry 门。** 若某个合法整数乘子 \(L\mid C\)、\(L\ge2\)，则
   \(h_L=0\) 且 \(c=C/L<C\)。

这些都是真充分条件；下一节说明 sink 性并不强制其中任何一个成立。

## 3. 一个合同准入但终端抢占的空改善状态

先取低支撑 parent

\[
P=(p,R_0,K_0;A_0)=(73,1351,24656;1),
\tag{15}
\]

其中

\[
R_0=7\cdot193,
\qquad
K_0=2^4\cdot23\cdot67.
\tag{16}
\]

对 \(q=2,23,67\) 均有 Jacobi 符号 \((q/1351)=1\)，而
\((-1/1351)=-1\)，所以 \(P\) 是 G 状态。通用源和四条显式 raw 边为

\[
\begin{aligned}
(73,97199,72)
&\xrightarrow{73}(1,1350,1)
\xrightarrow{3}(450,901,1)\\
&\xrightarrow{53}(17,1334,1)
\xrightarrow{29}(46,1305,1).
\end{aligned}
\tag{17}
\]

末节点满足

\[
1305=3^2\cdot5\cdot29,
\qquad
Q=1305,
\qquad
\beta=1,
\qquad
46\mid K_0.
\tag{18}
\]

因此 \(M=1305\)，canonical target 为

\[
H=(73,143,2610;1305),
\qquad
K/M=2.
\tag{19}
\]

真实端点秩严格下降：

\[
\Lambda_{73}^{\sharp}(P)=(1296,24656)
\longrightarrow
\Lambda_{73}^{\sharp}(H)=(0,2).
\tag{20}
\]

两端独立重分类：\(P\) 由上述 Jacobi 角色为 G；\(H\) 的

\[
K=2\cdot3^2\cdot5\cdot29
\]

centered box 有 86 个不同剩余类且不含 \(-1\)，而指数次序
\((2,3,5,29)\) 下

\[
z=(-3,0,-3,0)
\tag{21}
\]

满足 \(2^{-3}5^{-3}\equiv-1\pmod {143}\)，故 \(H\) 是 F。宏边保持同一个
\(\operatorname{Sol}(4,73)\)，解提升为恒等映射。因此 (17)--(21) 支付完整
E1--E5；这里证明的是状态合同准入，而不是越过 terminal-first 强行选择该边。

## 4. 完整 sink 容量 no-go

见证 (21) 对应整数源 \((1,1000,7)\)，并有

\[
(1,1000,7)
\xrightarrow{2}(18,125,1)
\xrightarrow{5}(25,118,1)
\xrightarrow{59}(2,141,1).
\tag{22}
\]

模 \(R=143\) 的完整 bottom graph 有唯一 sink SCC，含 24 个节点、43 条边，且
(22) 的终点在其中。枚举 SCC 每个节点的两个定向后，合法 complete-excess 候选
恰为下表十行：

| node | \(Q\) | \(\beta\) | \(x\beta\) | \(L=M/A\) | \(h_L\) | \(c\) | \(\Delta_L(2)\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \((1,142)\) | 71 | 2 | 2 | 71 | 70 | 72 | 4970 |
| \((2,141)\) | 47 | 3 | 6 | 47 | 18 | 28 | 1222 |
| \((3,140)\) | 28 | 5 | 15 | 28 | 18 | 47 | 1260 |
| \((5,138)\) | 23 | 6 | 30 | 23 | 11 | 35 | 759 |
| \((6,137)\) | 137 | 1 | 6 | 137 | 30 | 16 | 1918 |
| \((9,134)\) | 67 | 2 | 18 | 67 | 22 | 24 | 1474 |
| \((10,133)\) | 133 | 1 | 10 | 133 | 102 | 56 | 7182 |
| \((15,128)\) | 128 | 1 | 15 | 128 | 14 | 8 | 768 |
| \((45,98)\) | 49 | 2 | 90 | 49 | 4 | 6 | 196 |
| \((58,85)\) | 17 | 5 | 290 | 17 | 3 | 13 | 187 |

每行 \(\Delta_L(2)>0\)，最小目标余因子仍为 6。因此

\[
\boxed{\mathcal I_\Sigma(H)=\varnothing.}
\tag{23}
\]

这是对“仅由真实 source、完整 E1--E5 宏来源和 sink/complete-excess 结构即可推出
rank-aware 改善非空”的严格反例，不是有限搜索未找到。它不否定附加
`terminal-first 已失败` 前提后可能成立的更窄命题。候选乘子还满足

\[
\prod_{L\in E_H}L\equiv25\not\equiv1\pmod {73},
\tag{24}
\]

所以不能把模 \(R\) 的 SCC 循环关系未经新证明便搬成模 \(p\) 的乘子积约束。

## 5. terminal-first 完整分派

同一个根素数有直接 Type II 证书

\[
\boxed{
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.
}
\tag{25}
\]

因此统一选择器在进入 (15) 或 (19) 的递归分支之前已经终止。若为了检验局部机制仍
重放 (19)，完整 typed 输出应写成

```text
bundle_capacity_status = CARRY_NO_GO
improving_candidate_count = 0
fallback_status = TERMINAL_PREEMPTION
terminal_kind = direct_Type_II
recursive_edge_selected = false
```

这同时说明两件事：式 (23) 不是 Erdős--Straus 猜想的反例；但任何全称选择器证明都
必须真正证明 `terminal / alternate / dual / total-cofactor / paid reset` 中至少一个
后备分支，而不能继续把 sink 强连通当作改善非空性的替代品。

## 6. 正控制：新的 \(44\to2\) 严格边

取此前已经持久化并独立重分类为 F 的状态

\[
H_{44}=(73,4563815,83289624;1892946),
\qquad
\Lambda_{73}^{\sharp}(H_{44})=(0,44).
\tag{26}
\]

从绑定于该状态的 universal source 出发，有七条显式 raw 边：

\[
\begin{aligned}
(73,328594607,72)
&\xrightarrow{73}(1,4563814,1)
\xrightarrow{73}(62518,4501297,1)\\
&\xrightarrow{31259}(2,4563813,1)
\xrightarrow{1933}(2361,4561454,1)\\
&\xrightarrow{6353}(718,4563097,1)
\xrightarrow{7}(651871,3911944,1)\\
&\xrightarrow{488993}(8,4563807,1).
\end{aligned}
\tag{27}
\]

最后节点满足

\[
4563807=3\cdot1521269,
\qquad
Q=1521269,
\qquad
\beta=3,
\qquad
8\beta=24\mid83289624.
\tag{28}
\]

于是

\[
L=\frac{\operatorname{lcm}(1892946,Q)}{1892946}=1521269,
\qquad
h_L=41678,
\tag{29}
\]

而 carry 公式直接给出

\[
c=\frac{44+73\cdot41678}{1521269}=2,
\qquad
\Delta_L(44)=-63893298.
\tag{30}
\]

新 target 为

\[
T_2=(73,315581377367,5759360136948;2879680068474),
\tag{31}
\]

所以得到新的严格边

\[
\boxed{(0,44)\longrightarrow(0,2).}
\tag{32}
\]

目标类型没有继承。\(R_T=315581377367\) 是素数；其 centered exponent box 共
3645 项，合并后有 3581 个不同剩余类，仍不含 \(-1\)。另一方面

\[
\left(\frac{11}{R_T}\right)=-1,
\qquad
11^{(R_T-1)/2}\equiv-1\pmod {R_T},
\tag{33}
\]

而该指数超过 \(v_{11}(K_T)=1\)，故 (33) 是一个紧凑的无界 F 见证。于是 (27)--(33)
支付 source/path、bundle、目标重分类、恒等解提升和真实端点严格下降，构成完整
E1--E5。

这个正控制和 (23) 放在一起还给出一个新的结构结论：即使 \(p\) 与当前余因子
\(C\) 相同，改善容量仍取决于当前图表产生的合法乘子集合 \(E_H\)，不能只由 \(C\)
或抽象 residue permutation 决定。

## 7. 推进后的决定性缺口

本卡关闭了“不利用 terminal-free 或其它跨模条件、只从高支撑 sink 证明改善集非空”
这条路线。可继续追求的全称对象必须是以下带证明责任的析取：

\[
\boxed{
\text{carry decrease}\ \lor
\text{direct terminal}\ \lor
\text{support-preserving alternate/dual/total-cofactor}\ \lor
\text{paid well-founded reset}.
}
\tag{34}
\]

式 (10)--(11) 提供了一个有限、可组合的容量接口：先用三个充分条件尝试直接证明
非空；失败时输出完整 signed carry vector，而不是再次扫描同一个 SCC。下一项真正的
数学任务，是从该 no-go vector 中抽取能强制 (34) 其余分支之一的跨模耦合量。

该任务在最小 \(C=2\) 高支撑边界上已有全称推进。对每个核心素数，越过 \(B_p\) 的
首个 \(C=2\) 图表都是

\[
(R,K;A)=\left(2p-3,\frac{(p-1)(2p-1)}4;
\frac{(p-1)(2p-1)}8\right).
\]

其任意合法 complete-excess 候选都满足 \(c>2\)，所以该分支全域严格上升；唯一满足
\(A\mid M\mid K\) 的同图表 divisor upgrade \(A\to K\) 需要 \(L=2\)，却被
full-block 语法排除。与此同时，内部短关系
\(2/(2p-1)\equiv1\pmod{2p-3}\) 统一产生 \(E=2(p-1)\)、偶前驱 \(n=p-1\) 和
自然标记 \(\alpha=A\)。因此这个 no-go 已被转成精确 dyadic 容量，但 F/G miss 上的
自然标记源仍为空；真正余项是构造非自然 E4 或由其它分支抢占。见
[最小高支撑 \(C=2\) 边界的 carry--dyadic 容量转导](type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction.md)。

聚焦验证：

```bash
python3 reproductions/type_i_high_support_bundle_carry_capacity_terminal_dispatch.py --verify
```
