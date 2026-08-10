---
kind: claim
claim_id: type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
title: 最小高支撑 C=2 边界的严格 carry no-go 与内部二进容量转导
statement: >-
  对每个核心素数 p=1 (mod 24)，大于 B_p=(p-1)^2/4 且满足 8A=1
  (mod p) 的最小支撑为 A_2=(p-1)(2p-1)/8；其 canonical 图表满足
  (R_2,K_2;A_2)=(2p-3,(p-1)(2p-1)/4;A_2) 且 K_2/A_2=2。
  在该图表的任意合法 bottom complete-excess 候选上，canonical target
  cofactor 都严格大于 2；故整个宏族没有下降或 stutter。其唯一满足
  A_2|M|K_2 的同图表 divisor upgrade A_2->K_2 需要乘子 2，却被 full-block
  complete-excess 语法严格排除。另一方面，K_2 内部存在统一短关系
  rho=2/(2p-1)=1 (mod R_2)，等价于 j=1 除子对 (a,b)=(4,2p-1)，并产生
  E=2(p-1)、偶前驱 n=p-1 及自然标记 alpha=A_2。该关系把缺失的内部容量
  精确转移到 dyadic/关系格侧；此卡证明其自然标记源非空当且仅当原图表已有
  中心 Type I 命中，因而关系本身不支付 E4。后续反足 Vieta 定理又证明该中心
  命中对所有核心素数都不可能，故自然标记最终应登记为空分支，而不是终端叶或
  verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-general-dyadic-terminal-transfer
  - type-I-generalized-dyadic-exact-relation-capacity
  - type-I-generalized-dyadic-natural-lift-equivalence
  - denominator-escape-state-contract
topics:
  - type-I
  - high-support
  - complete-excess
  - carry-capacity
  - generalized-dyadic
  - relation-lattice
  - even-predecessor
  - solution-lift
  - strict-no-go
  - capacity-transduction
sources:
  - reproduction: reproductions/type_i_high_support_c2_boundary_carry_dyadic_capacity_transduction.py
    role: focused-boundary-and-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# 最小高支撑 \(C=2\) 边界的严格 carry no-go 与内部二进容量转导

## 1. 最小边界的闭式

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

考虑 canonical 高支撑图表中余因子 \(C=2\) 的同余

\[
8A\equiv1\pmod p,
\qquad A>B_p.
\tag{2}
\]

### 定理 1（最小 \(C=2\) 高支撑边界）

满足 (2) 的最小正整数是

\[
\boxed{
A_2=B_p+\frac{p-1}{8}
=\frac{(p-1)(2p-1)}8.}
\tag{3}
\]

相应 canonical 图表为

\[
\boxed{
H_2(p)=(p,R_2,K_2;A_2),
\quad
R_2=2p-3,
\quad
K_2=2A_2=\frac{(p-1)(2p-1)}4.}
\tag{4}
\]

**证明。** 直接展开得

\[
8A_2=(p-1)(2p-1)=p(2p-3)+1,
\tag{5}
\]

故 (2) 成立且 \(R_2=(8A_2-1)/p=2p-3\)。同余 (2) 的全部解相差
\(p\)，而

\[
A_2-p<B_p<A_2.
\tag{6}
\]

所以 (3) 确为越过 \(B_p\) 的第一个解。式 (4) 随即成立。\(\square\)

若写 \(p=24h+1\)，同一边界也可写成

\[
A_2=3h(48h+1),
\qquad
K_2=6h(48h+1),
\qquad
R_2=48h-1.
\tag{7}
\]

本卡后续全称结论是对算术图表 \(H_2(p)\) 的条件性结论；它不声称每个
\(H_2(p)\) 都已有 source/path provenance，也不声称它必为 F 或 G。

## 2. complete-excess 候选全部严格上升

取 \(R_2\) 的任一正 bottom node \(x+y=R_2\)，并选定一个方向

\[
y=Q\beta.
\tag{8}
\]

这里 \(Q\) 按现有 complete-excess 语法由全部 offending full blocks 组成：若
\(q\mid Q\)，则

\[
v_q(Q)=v_q(y)>v_q(K_2).
\tag{9}
\]

一个合法候选还要求 \(x\beta\mid K_2\)、必要的互素条件以及

\[
M=\operatorname{lcm}(A_2,Q)=A_2L,
\qquad
L\ge2,
\qquad
p\nmid L.
\tag{10}
\]

置 \(g=(A_2,Q)\)，则

\[
L=\frac Qg,
\qquad
2\le L\le Q\le y<R_2=2p-3.
\tag{11}
\]

由 canonical carry 公式，目标余因子 \(c\in\{1,\ldots,p-1\}\) 满足

\[
c\equiv2L^{-1}\pmod p,
\qquad
\Delta_L(2)=L(c-2).
\tag{12}
\]

### 定理 2（最小 \(C=2\) 边界的严格 bundle no-go）

每个满足 (8)--(10) 的合法 complete-excess 候选都有

\[
\boxed{c>2,\qquad \Delta_L(2)>0.}
\tag{13}
\]

特别地，即使枚举整个 source path 或整个 bottom sink SCC，也不可能从该宏族取得
下降或 stutter。

**证明。** 先排除 \(c=1\)。由 (11)--(12)，这要求

\[
L\equiv2\pmod p,
\qquad
L\in\{2,p+2\}.
\tag{14}
\]

若 \(L=2\)，则 (9) 给出矛盾。确切地，对任一奇素数 \(q\mid Q\)，

\[
v_q(K_2)=v_q(A_2),
\qquad
v_q(L)=v_q(Q)-v_q(A_2)\ge1,
\tag{15}
\]

所以 \(L\) 含奇因子。若 \(Q\) 只有素因子 \(2\)，则

\[
v_2(K_2)=v_2(A_2)+1,
\qquad
v_2(Q)>v_2(K_2),
\qquad
v_2(L)\ge2,
\tag{16}
\]

故 \(4\mid L\)。两种情形都不允许 \(L=2\)。

若 \(L=p+2\)，由 \(Q=gL<R_2\) 得 \(g=1\)，再由
\(y=Q\beta<R_2\) 得 \(\beta=1\)。于是

\[
Q=p+2,
\qquad
x=R_2-Q=p-5,
\qquad
p-5\mid K_2.
\tag{17}
\]

令 \(t=(p-5)/4\)。因 \(p=24h+1\)，有 \(t=6h-1>1\) 且
\((t,9)=1\)。另一方面

\[
K_2=(t+1)(8t+9),
\tag{18}
\]

从而

\[
(t,K_2)=1.
\tag{19}
\]

这与 \(4t=p-5\mid K_2\) 矛盾，故 \(c\ne1\)。

再排除 \(c=2\)。式 (12) 此时要求 \(L\equiv1\pmod p\)；结合 (11) 只能有

\[
L=p+1.
\tag{20}
\]

同样由 \(Q=gL<R_2\) 和 \(Q\beta<R_2\) 得 \(g=\beta=1\)，所以

\[
Q=p+1,
\qquad
x=p-4,
\qquad
p-4\mid K_2.
\tag{21}
\]

但 \(p-4\mid K_2\) 会蕴含 \(p-4\mid4K_2\)，而

\[
4K_2=(p-1)(2p-1)\equiv3\cdot7=21\pmod {p-4}.
\tag{22}
\]

核心素数 \(p\ge73\)，故 \(p-4>21\)，矛盾。于是 \(c\notin\{1,2\}\)，
(13) 成立。\(\square\)

定理 2 不是一次有限搜索的结果。它只使用 full-block 定义、residual divisibility
和边界闭式，因而同时排除了路径上、sink 内以及其它已获 provenance 的全部同类候选。

## 3. 内部一比特容量不能由 complete-excess 取出

图表 (4) 内部若作 support-preserving divisor upgrade，必须满足

\[
A_2\mid M\mid K_2,
\qquad
M>A_2.
\tag{23}
\]

因为 \(K_2/A_2=2\)，唯一选择是

\[
\boxed{M=K_2,\qquad L=M/A_2=2.}
\tag{24}
\]

这本来会把 sharp rank 从

\[
(0,2)\longrightarrow(0,1)
\tag{25}
\]

严格降低。然而 (15)--(16) 已证明 complete-excess full-block 语法永远不能实现
\(L=2\)：当前 \(K_2\) 已比 \(A_2\) 多吸收一枚 \(2\)，而一个被判为 offending 的
二进 full block 必须越过 \(v_2(K_2)\)，其 lcm 增量至少为 \(4\)。

因此这里的障碍不是状态内部没有容量，而是当前物理语法只能读取 above-\(K_2\) 的
full blocks，不能读取 \(K_2/A_2\) 中已经存在的最后一枚二进支撑。这给出一个严格的
**内部一比特容量缺口**。

## 4. 两类二进关系：外部两比特赤字与内部短关系

令

\[
e=v_2(p-1)\ge3,
\qquad
L_0=2K_2.
\tag{26}
\]

则

\[
v_2(K_2)=e-2,
\qquad
v_2(L_0)=e-1.
\tag{27}
\]

### 引理 3（自然 \(R_2+1\) 仿射族恰差两位预算）

对 \(1\le s\le e\)，取

\[
a_s=1,
\qquad
b_s=\frac{p-1}{2^s},
\qquad
j_s=s+1.
\tag{28}
\]

则 \(a_s,b_s\mid L_0\)、\((a_s,b_s)=1\)，且

\[
2^{j_s}b_s=2(p-1)=R_2+1,
\qquad
a_s\equiv2^{j_s}b_s\pmod {R_2}.
\tag{29}
\]

但是广义二进预算上界恰为

\[
J_s=v_2(L_0)+v_2(a_s)-v_2(b_s)=s-1,
\tag{30}
\]

所以

\[
\boxed{j_s-J_s=2.}
\tag{31}
\]

相应形式量

\[
2^{1-j_s}L_0\frac{a_s}{b_s}=\frac{2p-1}{2}
\tag{32}
\]

确为半整数。故整个最自然的 \(R_2+1\) 仿射族都不是合法 dyadic 候选；不能只看
模同余而忽略二进预算。

### 定理 4（内部 cofactor 的统一关系格转导）

与引理 3 不同，取

\[
\boxed{(a,b,j)=(4,2p-1,1).}
\tag{33}
\]

则这是对每个核心素数都合法的 \(j=1\) 自由除子对，并唯一产生

\[
\boxed{
E=2(p-1)=R_2+1,
\qquad
n=p-1.}
\tag{34}
\]

其关系格形式为

\[
\boxed{
\rho=\frac{E}{4K_2}=\frac2{2p-1}\equiv1\pmod {R_2}.}
\tag{35}
\]

该关系向量位于 \(K_2\) 的对称指数盒内：二进坐标为 \(+1\)，而
\(2p-1\) 的每个奇素因子坐标恰位于其负边界。

**证明。** 因 \(p\equiv1\pmod {24}\)，式 (27) 给出 \(4\mid L_0\)；又有

\[
L_0=\frac{(p-1)(2p-1)}2,
\tag{36}
\]

所以 \(2p-1\mid L_0\)，并且 \((4,2p-1)=1\)。由于

\[
2(2p-1)=2R_2+4,
\tag{37}
\]

有 \(4\equiv2(2p-1)\pmod {R_2}\)，且 \(4<2(2p-1)\)。预算为

\[
1\le v_2(L_0)+v_2(4)-v_2(2p-1)=e+1.
\tag{38}
\]

故 (33) 合法。直接计算

\[
E=L_0\frac4{2p-1}=2(p-1),
\tag{39}
\]

以及

\[
n=\frac{2L_0-E}{R_2}
=\frac{(p-1)(2p-3)}{2p-3}=p-1.
\tag{40}
\]

式 (35) 由 \(2p-1=R_2+2\) 立即得到。最后
\((p-1,2p-1)=1\)，所以 \(2p-1\) 的奇素因子在 \(K_2\) 中恰以原指数出现；
二进坐标 \(+1\le v_2(K_2)\) 由 \(e\ge3\) 保证。\(\square\)

这不是“多找到了一个 \(E\)”而已。定理 2--4 给出了一个明确容量映射：

\[
\boxed{
\text{complete-excess 无法读取的内部 }K_2/A_2=2
\quad\longmapsto\quad
\rho=2/(2p-1)\text{ 的短核关系}.}
\tag{41}
\]

## 5. 自然标记恰回到 \(A_2\)，F/G 上仍不可提升

对 (34) 的自然标记分母

\[
\alpha=\frac{nK_2}{E}
\tag{42}
\]

有一个精确闭式：

\[
\boxed{\alpha=A_2.}
\tag{43}
\]

事实上

\[
\frac4{p-1}-\frac1{A_2}
=\frac{R_2}{K_2}
=\frac4p-\frac1{pK_2}.
\tag{44}
\]

所以包含标记 \(A_2\) 的源解与包含标记 \(pK_2\) 的目标解由替换

\[
(A_2,u,v)\longleftrightarrow(pK_2,u,v)
\tag{45}
\]

精确对应；但这个标记源非空当且仅当

\[
\frac{R_2}{K_2}=\frac1u+\frac1v
\tag{46}
\]

可解，也等价于原图表已有中心 Type I 除子

\[
D\mid K_2^2,
\qquad
D\equiv-K_2\pmod {R_2}.
\tag{47}
\]

因此若 \(H_2(p)\) 已分类为 F 或 G miss，则 (43) 的标记源严格为空。后续的
[反足 Vieta 全称 no-go](type-I-high-support-c2-centered-vieta-antipodal-no-go.md)
进一步证明 \(R_2/K_2\) 对每个核心素数都没有二单位分数分解，所以自然标记源其实
无条件为空。偶数 \(p-1\) 的平凡解

\[
\left(\frac{p-1}{2},p-1,p-1\right)
\tag{48}
\]

也不含 \(A_2\)，不能承担 (45)。正确 typed 状态只能写成

~~~text
bundle_capacity_status = CARRY_NO_GO
existing_candidate_deltas = ALL_EXISTING_DELTAS_POSITIVE
dyadic_status = SHORT_RELATION_EVEN_PREDECESSOR
predecessor_n = p - 1
natural_marker = A_2
marked_source_status = EMPTY_BY_ANTIPODAL_VIETA_NO_GO
edge_status = REJECTED_EMPTY_MARKED_SOURCE
~~~

若 (47) 命中，则原图表本来已经有直接 Type I 终端；若 (47) 未命中，则这个自然
dyadic lift 不能成为 E4。定理 4 因而闭合了算术容量，却没有偷换成猜想证明。

## 6. 两个精确控制

| \(p\) | \(H_2(p)=(R_2,K_2;A_2)\) | 边界分类与 bundle | 直接分派 |
|---:|---|---|---|
| 73 | \((143,2610;1305)\) | 已有真实 source；F；唯一 sink 的 10 个合法候选全严格上升 | Type II \((20,219,4380)\) |
| 193 | \((383,18480;9240)\) | 算术控制；F；唯一 sink 的 6 个合法候选全严格上升 | \(p+4\) 的 \(d=1\) 子菜单 miss，但 gap-7 Type I \((50,1380,1331700)\) |

\(p=193\) 的 bounded centered box 有 319 个不同剩余类且不含 \(-1\)，而

\[
5^{191}\equiv-1\pmod {383}
\tag{49}
\]

给出 unbounded F 见证。其 \(p+4=197\) 没有 \(3\pmod4\) 的除子，所以只能推出
该 \(d=1\) 子菜单 no_output，不能称为 terminal-free。另一方面，取

\[
m=7,
\qquad
x=50,
\qquad
d=10,
\tag{50}
\]

有 \(d\mid x^2\)、\(7\mid193x+d\)，并得到

\[
\frac4{193}=\frac1{50}+\frac1{1380}+\frac1{1331700}.
\tag{51}
\]

两个控制说明 carry no-go、有限直接子菜单 miss 和完整直接终端是三个不同谓词。

## 7. 对统一选择器的推进

此前只知道 \(p=73\) 的一个 \(C=2\) sink 容量反例。现在得到的是全称结构定理：

1. 最小 \(C=2\) 高支撑边界上的 complete-excess 分支不仅不下降，而且每个合法候选
   都严格上升；继续扩张或重复扫描 sink 不会产生出口。
2. 状态内部唯一可降的支撑位是 \(A_2\to K_2\)，但 full-block 语法无法读取它。
3. 同一位容量自动变成短关系 (35)，统一产生 \(p-1\) 偶前驱；后续 Vieta
   递降又证明其自然标记源对每个核心素数都为空。
4. 后续的 rank-one 穷尽定理已经关闭双尾保持 \(D\)-only 子路：全部
   source-supported 候选只是其它 \(p-1\) 图表的自然标记，非空时立即给出
   centered Type I；全部 non-source-supported 候选的标记纤维恒空。
5. 固定 gap-\(7\) 的单分母源切片虽然总非空，但其目标提升恰等价于原
   gap-\(7\) Type I/II 菜单命中，同样不能独立支付 E4；标准 terminal-first
   次序仍须先检查更小的 gap-\(3\) 等直接菜单。

因此下一步不应再试图证明这个边界的 bundle 改善集非空，也不应只重复寻找别的
dyadic \(E\) 或 \(D\)-only 标记。真正的新对象必须改变保留尾/坐标语法、使用随
source 变化的单坐标映射、完全重组三个坐标，或给出边界前的跨正规形抢占。双尾菜单
的精确重索引、容量公式和空纤维定理见
[C=2 偶前驱的 rank-one 保留坐标穷尽](type-I-high-support-c2-rank-one-retention-exhaustion.md)。

聚焦验证：

~~~bash
python3 reproductions/type_i_high_support_c2_boundary_carry_dyadic_capacity_transduction.py --verify
~~~
