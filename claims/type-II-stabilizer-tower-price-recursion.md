---
kind: claim
claim_id: type-II-stabilizer-tower-price-recursion
title: Type II 稳定子塔的非重复价格递归与有限终端
statement: 对同一已实现参数纤维中的有序源块序列，若目标仍缺失，则可按当前积集的稳定子递归投影：非平凡稳定子给出严格较小商，投影后成为单位块的来源永久从价格账本删除；稳定子平凡时，任何未被吸收的源块按其插入后稳定子收取一次 Kneser 价格。以群阶、当前稳定子商、剩余价格缺口和未处理块数构成良基势，递归必在 Type II 命中、保持来源标签的稳定子塔商、顶层 primary/Fourier 或明确的价格/整数提升障碍之一终止。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-surplus-kneser-price-injection
  - type-II-hall-surplus-stabilizer-absorption-quotient-relay
  - type-II-full-match-stabilizer-relay-certificate
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-II-stabilizer-tower-weighted-defect-conservation
topics:
- type-II
- stabilizer
- tower
- Kneser
- price-ledger
- quotient-descent
- Fourier
- source-switch
- well-founded-potential
- proof-program
sources:
  - claim: type-II-hall-surplus-kneser-price-injection
    role: active-surplus-price
  - claim: type-II-hall-surplus-stabilizer-absorption-quotient-relay
    role: one-step-absorbed-quotient
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: top-primary-terminal
visibility: public
last_checked: '2026-08-05'
---

# Type II 稳定子塔的非重复价格递归与有限终端

## 1. 递归状态

固定一个已经通过 FIBER_REALIZED、source-switch、SNF、shared-q 和范围门的
参数纤维。一个未闭合的层状态写成

\[
\mathfrak S=(H,A,t;\mathcal D,L),
\qquad
\mathcal D=(D_1,\ldots,D_m),
\tag{1}
\]

其中 \(H\) 是有限阿贝尔目标群，\(A\ne\varnothing\) 是已经处理的源块积集，
\(t\) 是目标，\(D_i=\{1,g_i,\ldots,g_i^{e_i}\}\) 是尚未处理的真实源块，
且 \(L\) 是当前层的价格下界。要求

\[
L\le |A|,
\qquad
t\notin A D_1\cdots D_m.
\tag{2}
\]

令

\[
T=\operatorname{Stab}_H(A),
\qquad
\delta(\mathfrak S)=|H|-|T|-L.
\tag{3}
\]

由于 \(AT=A\)，若目标在当前完整后继中仍缺失，则必有
\(L\le |A|\le |H|-|T|\)，所以未闭合状态的
\(\delta(\mathfrak S)\) 非负。价格下界只记录本层从一个精确基集开始之后的
增长；一旦进入商群，新的基集大小重新初始化，旧价格不在商中再次收费。

## 2. 一步转移和账本规则

对当前第一个非恒等块 \(D=\{1,g,\ldots,g^e\}\) 令
\(P=AD\)、\(T'=\operatorname{Stab}_H(P)\)。若 \(D\) 是恒等块，直接删除它；
此操作既不改变 \(A\)，也不改变价格账本。对非恒等块有互斥的两项记录：

### 2.1 活跃价格

若

\[
g\notin T',
\tag{4}
\]

则在当前层登记

\[
\operatorname{ACTIVE\_PRICE}(D)=|T'|,
\qquad
L' = L+|T'|.
\tag{5}
\]

Kneser 不等式给出

\[
|P|\ge |A T'|+|D T'|-|T'|
       \ge |A|+|T'|,
\tag{6}
\]

因此 \(L'\le |P|\)。把 \(A\leftarrow P\)、\(L\leftarrow L'\) 后继续检查。
若 (4) 还通过一个商角色
\(\chi\in\widehat{H/T'}\) 且
\(\chi(gT')\ne1\)，则该角色是这一笔价格的规范 Fourier 见证；角色只证明
非吸收，不额外增加价格单位。

### 2.2 吸收记录

若

\[
g\in T',
\tag{7}
\]

则登记
\(\operatorname{ABSORBED\_PRICE}(D,T')\)，不增加 \(L\)，但仍令
\(A\leftarrow P\)。若 \(T'>1\)，下一步优先进入第 3 节的商转移；若
\(T'=1\)，则 (7) 只可能是一个已经在当前平凡稳定子中不起作用的块，实际有
\(P=A\)，可直接删除。这样，块即使后来出现在最终稳定子中，也不会从最终状态
倒推一个历史价格；反之，已在 (4) 中收费的块保留其插入时价格。

### 2.3 加权价格的精确化

上面的单价规则是“每个非吸收块收费一次”的安全下界。若一个块在当前稳定子商
中跨越多个但少于全部的独立陪集，应改用
\[
\kappa(D,T')=|DT'/T'|-1,\qquad
\rho(D,T')=\kappa(D,T')|T'|.
\]
逐层 Kneser 增长和缺陷望远镜恒等式见
[Type II 稳定子塔的加权价格与逐层缺陷守恒](type-II-stabilizer-tower-weighted-defect-conservation.md)。
在 q 前缀、有限阶折叠或多点幂块中，后者是账本的规范价格；本节的单价规则
可作为其 \(\kappa\ge1\) 时的粗粒度特例，不能再与加权价格重复相加。

## 3. 稳定子塔商转移

若当前 \(T=\operatorname{Stab}_H(A)\) 满足

\[
1<|T|<|H|,
\tag{8}
\]

令

\[
\pi:H\to H_+=H/T,
\qquad
A_+=\pi(A),
\qquad
t_+=\pi(t),
\tag{9}
\]

并把尚未处理的块投影为
\(\mathcal D_+=(\pi(D_1),\ldots,\pi(D_m))\)。满足
\(\pi(D_i)=\{1\}\) 的块标记为
\(\operatorname{ABSORBED\_UNIT}\) 并永久删除；它们不是商层的价格来源。
新状态设为

\[
\mathfrak S_+=(H_+,A_+,t_+;\mathcal D_+,|A_+|).
\tag{10}
\]

这是一个严格稳定子塔边：

\[
|H_+|=|H|/|T|<|H|.
\tag{11}
\]

并且 \(A\) 是 \(T\)-饱和集，故对任意未来块列 \(\mathcal E\) 都有
\[
A\mathcal E=\pi^{-1}(\pi(A\mathcal E)).
\tag{12}
\]
因此

\[
t\notin A\mathcal D
\Longleftrightarrow
t_+\notin A_+\mathcal D_+.
\tag{13}
\]

式 (13) 是递归合法性的关键：商中命中会真实提升为原层命中，商中缺失才进入
下一层。旧层的 \(L\) 不被带入 \(H_+\)；它已经被精确基集 \(A_+\) 吸收，避免
把同一稳定子块重新计入容量。

边界 \(T=H\) 时 \(A=H\)，与目标缺失矛盾；边界 \(T=1\) 时没有可用的稳定子商，
递归转入当前层的剩余块或第 5 节顶层终端。

## 4. 良基价格势与递归终止

令 \(m(\mathfrak S)\) 为删除恒等块后的剩余块数，并定义

\[
\Theta(\mathfrak S)=
\bigl(|H|,\ |H/T|,\ \delta(\mathfrak S),\ m(\mathfrak S)\bigr)
\tag{14}
\]

按字典序取值于非负整数。每一步均有明确下降：

1. 商转移 (8)--(10) 使第一坐标严格下降；
2. 活跃价格 (4)--(6) 在稳定子不变时使第三坐标至少下降 \(|T'|\ge1\)；
3. 吸收块、恒等块或没有新增长的块使第四坐标下降；若稳定子增长，则第二坐标
   也下降，因为 \(T<T'\) 时 \(|H/T'|<|H/T|\)。

如果价格缺口达到

\[
L>|H|-|T|,
\tag{15}
\]

则 \(A\) 不可能仍遗漏一个 \(T\)-陪集，直接输出
\(\operatorname{PRICE\_HIT}\) 和 Type II 源块积。若 (15) 不成立且 \(m=0\)，
则目标缺失位于稳定子平凡的有限阿贝尔层；按固定合成列输出严格较小商或顶层
素数核 Fourier/数字缺口。由于 (14) 良基，不能无限重复处理已吸收块。

## 5. 终端和障碍菜单

对每一个未闭合状态，递归输出以下互斥分支之一：

* **PRICE_HIT**：式 (15) 或显式成员检查给出 \(t\in A\)，源块回译为 Type II；
* **STABILIZER_TOWER_SOURCE_SWITCH**：某层 (13) 中目标仍缺失，且
  KERNEL_STABILIZER、统一来源 CRT、SNF、范围和 (B'>A) 门通过，得到保持标签的
  严格较小商后继；
* **STABILIZER_TOWER_LIFT_OBSTRUCTED**：商群缺失成立，但核包含、单位群映射或
  来源合同失败，保存对应的 KERNEL_SOURCE_ANNIHILATOR、KERNEL_BOX_FOURIER、
  G1/G2/G3 或 G4 最小失败行；
* **TOP_PRIMARY_FOURIER / PRIMARY_DIGIT_DEFICIT**：当前稳定子为平凡群且没有
  剩余非恒等块，调用有限阿贝尔合成列的顶层非空真截面或循环/多 primary 数字终端；
* **HALL_SURPLUS_UNPRICED**：某个声称的 surplus 块未通过同纤维、shared-q、
  source-switch 或非吸收门。此时不得把该块放入 (L)，而应转入源列逃逸、关系
  Fourier 或算术障碍分支。

其中前两项是可直接用于统一选择器的命中或严格递降；后三项是明确的有限障碍/终端，
不把抽象商或 Fourier 非零系数自动当成原整数猜想的证明。

## 6. 证明

若 \(T'=\operatorname{Stab}(AD)\) 且 \(g\notin T'\)，则
\(DT'/T'\) 至少含两个陪集。Kneser 给出 (6)，故一次 active price 不会使价格
下界超过实际积集大小；若 \(g\in T'\)，该块在该层没有可验证的非吸收价格，
只保留精确积集并等待稳定子商。稳定子定义和阿贝尔性给出 \(AT=A\) 以及
\((A\mathcal E)T=A\mathcal E\)，从而得到 (12)--(13)。非平凡 \(T\) 使 (11)
严格成立；投影为单位的块在商中确实消失，不能再次计费。

在没有商转移时，若 active price 使 (15) 成立，则目标陪集与 (A) 的 Kneser
下界不相容，得到命中；否则每次 active price 减少非负的价格缺口，吸收或恒等块
至少减少剩余块数。于是 (14) 良基，递归只可能到达第 5 节列出的有限终端。顶层
终端由有限阿贝尔合成列命题给出；整数提升则由相应的 source-switch/SNF 菜单决定。
证毕。

## 7. 小型有限群检查

### 7.1 中途吸收不能回溯收费

在加法群 \(H=C_8\) 中取 \(A=\{0\}\)，先加入
\(D_1=\{0,4\}\)。此时

\[
P=\{0,4\},\qquad T'=\{0,4\}.
\]

块 \(D_1\) 走 ABSORBED_PRICE，随后商为 \(C_4\)，其投影块为单位；即便后续块
使原群最终稳定子更大，也不能把 \(D_1\) 当作商层新的 active price。

### 7.2 先收费再吸收的合法记录

仍取 \(H=C_8\)，先用 \(D_1=\{0,1\}\)，得到
\(P=\{0,1\}\)、\(T'=\{0\}\)，故登记一次价格 \(1\)。再加入
\(D_2=\{0,2\}\)，得到
\(P=\{0,1,2,3\}\)，其稳定子仍为平凡群；继续加入
\(D_3=\{0,4\}\) 后得到 \(P=H\)，此时 \(T'=H\)，\(D_3\) 走吸收分支而目标已经
命中。前两步的价格仍按插入时账本保留，但 \(D_3\) 不追溯扣除或重复收取。

### 7.3 商缺失的单步回执

取 \(H=C_4\)、\(A=\{0,2\}\)、\(t=1\)。有
\(T=\{0,2\}\)、\(A/T=\{T\}\)，目标投影仍缺失于
\(H/T\simeq C_2\)。若统一来源合同通过，该层是严格较小商；否则保存
KERNEL/CRT 提升障碍，而不是把 \(C_2\) 抽象缺失直接称为整数递降。

## 研究边界

该递归把一次稳定子吸收 relay 扩展成一个不会重复收费的有限稳定子塔，并为每层
给出统一的价格、商降阶和顶层 Fourier 回执。它仍是状态级闭包：尚未证明所有真实
q 进 surplus 都通过同纤维 PRICE-INJECTION，也未证明每个
STABILIZER_TOWER_LIFT_OBSTRUCTED 都能转成 Type I/F/G、广义 \(2^j\) 终端或
另一条保持标签的严格下降。因此全局猜想的最后缺口仍是“所有实际最小割均满足
价格注入或可提升障碍闭包”，而不是稳定子塔本身的有限性。
