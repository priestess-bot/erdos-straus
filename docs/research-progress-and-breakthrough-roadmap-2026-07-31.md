# Erdős–Straus 项目最新研究进展与突破路线评估

> 审计日期：2026-07-31  
> 仓库：`priestess-bot/erdos-straus`  
> 起始基线：`11ce2518b8c48fb9efd71ef7645b738082be0fae`  
> 审计 HEAD：`abcacc918b93af2af1a5f0074cdcea850f920ed7`  
> 提交范围：基线之后 13 次提交  
> 报告性质：研究进展、证明量词、有限证据和下一阶段优先级的综合评估；没有独立重跑全部新增复现程序，也不是对所有新增主张的外部同行评议。

## 一、结论先行

最近这一轮工作的价值明显高于继续扩大有限扫描。项目已经把上一阶段的“联合带符号分母缺陷”推进成一条更完整的结构链：

\[
\text{terminal-first}
\longrightarrow
\text{完整形式 Reach}
\longrightarrow
\text{Type I 汇点或 }m=1\text{ 周期}
\longrightarrow
\text{周期表示格 / 外部 slab}
\longrightarrow
\text{直接终端或合法标记状态}.
\]

这一链条中的多项接口已经成为不含素数扫描上界的一般命题：

1. 完整超高形式图的汇点精确等价于同状态 Type I 命中；中心 miss 时，任意持续轨道最终进入 \(m=1\) 周期；
2. 一个 \(m=1\) 周期生成的全部目标表示构成关系格中的二阶陪集，是否终端精确等价于该陪集是否与 \(K\) 指数容量盒相交；
3. 抽象通用周期何时能在无穷多个核心素数上实现为真实 \(K\)-支撑周期，已有完整 CRT/算术级数判据；
4. 外部单 \(q\)-slab 已有“两类直接碰撞或 small-slab 降 \(R\) 吸收”的无样本析取；
5. 所有保留两尾、替换一个分母的正提升，已经被压缩成 \(D\)-only 标记正规形，并带有精确的标记集非空判据和全域解提升公式。

同时，冻结有限证据也显著加强：完整 \(\Psi_0=1\) 谱由原来的 55 个状态扩展为 483 个状态，固定的内部缺口、双秩 Reach、跨图表中心谱和仿射边界菜单最终在这 483 个状态上全部产生独立验真的直接证书。

但是，当前仍不能合理声称猜想的完整证明已经迫近。真正未解决的不是“再找几个终端”，而是以下全称量词：

> 对任意 terminal-first 后仍未闭合的状态，为什么完整可达域必然产生直接 Type I/II、跨图表中心命中、可吸收 external slab，或一个标记集非空且满足完整解提升与良基下降的合法后继？

当前最窄的三个余项是：

- `large-slab`；
- 特殊外部载体（仓库前沿仍列有 \(q=p\)，但在原始线性图表的 \(m=1\) 层可能可以进一步排除）；
- \(D\)-only 后继标记集的递归非空性。

综合判断：

| 维度 | 当前状态 | 评价 |
|---|---|---|
| 形式搜索的结构归约 | 已有一般定理 | 强进展 |
| 周期障碍的规范化 | 已有关系格和容量盒判据 | 强进展 |
| 冻结 \(\Psi_0=1\) 状态 | 483/483 状态内候选闭合 | 很强有限证据 |
| 广义二进终端 | 内部选择器成熟，自然提升被关闭 | 路线澄清 |
| external slab | small-slab 已有合法吸收边 | 接近一般分支 |
| 标记递降 | \(D\)-only 正规形已完成，非空选择未完成 | 核心开放点 |
| 全称选择器 | 尚未闭合 | 决定性缺口仍在 |
| 独立复核 | 仍明显不足 | 可信度瓶颈 |

最可能较快取得的“实质性突破”，不是继续扩展 483 个冻结状态，而是证明下面两类无样本上界的定理之一：

\[
\boxed{
\text{\(m=1\) large-slab 的 }a=1,2,3	ext{ 三分逃逸定理}
}
\]

或

\[
\boxed{
\text{一个规范 \(D\)-only 后继族的标记集自动非空定理}.
}
\]

前者有机会闭合 external slab 分支；后者有机会产生第一族真正可用于归纳的标记解提升。

---

## 二、最近 13 次提交的研究主线

从 `11ce2518` 到 `abcacc918` 的提交大致分成五组：

1. **形式周期的结构与可实现性**  
   包括 cycle-or-hit、周期表示格、radical/multiplier bridge、核心可实现性、翻转分段和有限模数闭合。

2. **\(\Psi_0=1\) 完整谱的选择器扩展**  
   包括内部缺口、双秩 Reach、一步 rejected 前瞻、跨图表中心谱和仿射边界菜单。

3. **二进终端与提升边界**  
   包括双向最大窗口选择器、自然标记提升等价、标准偶源和 E-split 的零边界。

4. **external slab 与合法重图表**  
   包括双碰撞、容量吸收图表、small-slab/large-slab 析取和完整换支撑 G 障碍。

5. **较小方程和标记递降**  
   包括双尾提升的 \(D\)-only 参数化、标记集非空的第二层因子同余，以及空标记状态的严格警示。

当前总览见[当前证明前沿与下一阶段发展目标](../concepts/current-frontier-2026-07-29.md)。

---

## 三、最近最重要的一般数学进展

### 3.1 完整超高图的 Type I 或一层周期归约

固定核心素数 \(p\)、合法模数 \(R\) 和

\[
4K=pR+1.
\]

形式节点为互素正整数对

\[
A+B=Rm.
\]

对每个满足

\[
v_q(AB)>v_q(K)
\]

的素数 \(q\)，都允许规范形式迁移。新结果证明：

- 固定起点的完整可达图有限；
- 每条 \(m>1\) 的边都严格降低 \(m\)；
- 节点无出边当且仅当
  \[
  AB\mid K;
  \]
- \(AB\mid K\) 会规范恢复同状态 Type I 证书；
- 因此，中心 Type I miss 时，任意持续轨道在有限步内必包含一个 \(m=1\) 周期。

即：

\[
\boxed{
\text{同状态 Type I 命中}
\quad\lor\quad
\text{\(m=1\) 有向周期}.
}
\]

这条归约见[完整超高形式图的 Type I 或一层周期归约](../claims/type-I-formal-full-excess-cycle-or-hit-reduction.md)。

它的意义是：未来不必继续分析任意深的形式树。所有真正的形式障碍最终都位于 \(m=1\) 层。

它的边界也必须保留：形式边仍是 `analysis_evidence`，没有自动给出新方程、标记解集和解提升；周期归约不是算术递降证明。

### 3.2 周期表示格、二阶目标类和容量盒

对一个 \(m=1\) 周期，将节点定向写为

\[
a_i+b_i=R,
\qquad(a_i,b_i)=1,
\]

并编码为素因子指数向量 \(z_i\)，使

\[
\prod_q q^{z_i(q)}\equiv-1\pmod R.
\]

定义周期表示格

\[
\Gamma_{\mathcal Z}=\langle z_0,\ldots,z_{\ell-1}\rangle_{\mathbb Z}
\]

以及关系格

\[
L_{\mathcal Z}
=
\left\langle z_i-z_0,\ 2z_0\right\rangle_{\mathbb Z}.
\]

新定理给出

\[
L_{\mathcal Z}
=\Gamma_{\mathcal Z}\cap\ker\varphi_R,
\qquad
[\Gamma_{\mathcal Z}:L_{\mathcal Z}]=2.
\]

所以周期生成的全部 \(-1\) 表示恰为

\[
\mathcal T_{\mathcal Z}=z_0+L_{\mathcal Z}.
\]

令 \(\mathcal B_K\) 为 \(K\) 的真实指数容量盒，则

\[
\boxed{
\mathcal T_{\mathcal Z}\cap\mathcal B_K\ne\varnothing
\iff
\text{周期节点的某个奇次乘法组合给出同状态 Type I}.
}
\]

详见[一层形式周期的表示格、二阶目标类与容量盒判据](../claims/type-I-formal-cycle-representation-lattice-capacity.md)。

这一步把“周期是否有用”变成了精确的整数格陪集与有限盒相交问题。Smith 正规形可以进一步输出：

- `HIT`；
- `MISS_EXTERNAL`：无法用奇数组合消掉外部素数坐标；
- `MISS_CAPACITY`：外部坐标可消，但内部指数必超出 \(K\) 盒。

这种分类比“发现一个周期”本身强得多，因为周期在很多模数中是普遍存在的，尤其是外部二进周期。

### 3.3 周期的核心可实现性

对 \(R\equiv7\pmod8\) 的通用一层周期，令 \(S\) 为全部周期坐标的素因子支撑。已有完整判据：

\[
\boxed{
\exists\text{ 无穷多个核心素数 }p,
\ S\subseteq\operatorname{Supp}\left(\frac{pR+1}{4}\right)
\iff
3\notin S\text{ 或 }R\equiv2\pmod3.
}
\]

而且可以同时强制

\[
v_q(K)=1\qquad(q\in S).
\]

证明使用 CRT 控制每个素数的一阶赋值，再用算术级数中的素数得到无穷多个 \(p\)。详见[通用一层周期的核心可实现性与十万模数闭合](../claims/type-I-core-universal-cycle-realizability-and-100k-closure.md)。

这说明，很多通用周期不是与原猜想无关的图论伪影，而能够在无穷多个核心素数上成为真实的超高周期。

同一工作还对

\[
R<100000,\qquad R\equiv7\pmod8
\]

的通用周期进行了完整扫描。唯一 direct radical miss 为 \(R=30031\) 的五周期，但它不满足核心可实现条件。于是得到有限模数、无穷 \(p\) 的结果：

\[
\boxed{
R<100000
\Longrightarrow
\text{每个真实核心 \(K\)-支撑周期都产生同状态 Type I 终端}.
}
\]

这不是任意大 \(R\) 的定理，但已经比有限素数验证更接近结构性成果。

### 3.4 三目标乘子桥

直接要求周期支撑的 signed cube 命中 \(-1\) 是错误的。正确的充分条件要同时检查

\[
-1,\qquad -4B,\qquad -(4B)^{-1},
\]

其中

\[
B=\prod_{q\in S}q.
\]

只要三个目标之一命中，就能构造

\[
D\mid B^2
\]

满足

\[
D\equiv-B\pmod R
\quad\text{或}\quad
4D\equiv-1\pmod R,
\]

进而嵌入完整 \(K\) 盒并恢复同状态 Type I。详见[周期平方自由支撑的三目标乘子桥](../claims/type-I-formal-cycle-radical-multiplier-bridge.md)。

\(R=30031\) 的首个 direct radical 反例仍被另外两个乘子目标修复。对 \(R<100000\) 的完整扫描，三目标 miss 为零。

正确的开放命题不再是“每个周期都直接命中 \(-1\)”，而是：

\[
\boxed{
\exists D\mid B^2:
D\equiv-B\pmod R
\quad\lor\quad
4D\equiv-1\pmod R.
}
\]

### 3.5 补数翻转和两翻转周期正规形

通用一层周期中，取补数恰好翻转所选坐标的奇偶。因此：

- 翻转次数为正偶数；
- 周期边标号乘积满足
  \[
  \prod_iq_i\equiv1\pmod R;
  \]
- 周期长度至少为 3。

将周期按翻转分段，若一段起点为 \(A_j\)、标号积为 \(Q_j\)，则

\[
A_j=Q_j(R-A_{j+1}),
\qquad
\operatorname{rad}(Q_j)\mid R-A_{j+1}.
\]

恰有两次翻转时，可写成闭式

\[
A=rac{Q(T-1)}h,
\qquad
R-A=rac{Q-1}h,
\]

\[
B=rac{T(Q-1)}h,
\qquad
R-B=rac{T-1}h,
\]

其中

\[
h=rac{QT-1}{R},
\qquad(Q,T)=1,
\]

并有交叉 radical 整除。详见[通用一层周期的偶补数分段与两翻转正规形](../claims/type-I-universal-cycle-complement-flip-segment-normal-form.md)。

这使两翻转周期成为一个很有希望首先证明全称三目标命中的子类。

---

## 四、完整 \(\Psi_0=1\) 谱的有限推进

### 4.1 从 55 态扩展到 483 态

冻结的 200 个压力素数共有 2752 个 finite-exponent F 状态。完整枚举

\[
13{,}533{,}050
\]

个正向一层面点后，得到

\[
\boxed{
483	ext{ 个 }\Psi_0=1	ext{ 状态},
\qquad1615	ext{ 条正向见证}.
}
\]

此前的 55 个状态只是其真子集。详见[完整 F 谱中四百八十三个缺陷一状态的终端与提升边界](../claims/type-I-psi-one-full-spectrum-terminal-descent-boundary.md)。

### 4.2 状态内直接证书覆盖

累计通道包括：

1. 所有合法内部缺口 \(M\mid K\) 的 Type I/II 完整谱；
2. 形式对的 \((m,\min(A,B))\) accepted 闭包与一步 rejected 前瞻；
3. 对称的 \((m,\max(A,B))\) 分支；
4. 把外部候选 \(Q\) 作为新模数，检查 \(K_Q^2\) 中心谱；
5. 对最终四个状态的完整 Reach，检查
   \[
   A,\ B,\ m,\ |A-R|,\ |B-R|
   \]
   的合法因子。

最终在 483 个冻结状态上得到状态内候选生成的

\[
\boxed{483/483}.
\]

最后四个状态的仿射边界闭合见[完整 Reach 的仿射边界终端菜单](../claims/type-I-psi-one-affine-boundary-terminal-profile.md)。

这是一项很强的有限正信号，因为最后两个原本需要状态外固定 gap 回退的状态，现在也能从同一状态的完整 Reach 和固定五项边界菜单产生原素数证书。

但它仍然没有证明全称命题

\[
\forall S\ \exists v\in\operatorname{Reach}(S)
\ \exists X\in\{A_v,B_v,m_v,|A_v-R|,|B_v-R|\}
\ \exists h\mid X:
\operatorname{Term}_p(h).
\]

后续不能在遇到新反例时继续向菜单中追加临时表达式；必须证明固定菜单的存在性，或者及时接受它被反例否定。

### 4.3 内部缺口的 \(R\)-坐标拉回

若

\[
M\mid K,\qquad M\equiv3\pmod4,
\]

令

\[
x=rac{p+M}{4}.
\]

则对任意 \(d\)：

\[
M\mid px+d
\iff
4dR^2\equiv-1\pmod M,
\]

\[
M\mid x+d
\iff
4dR\equiv1\pmod M.
\]

补上 \(d\mid x^2\) 后，这两条分别是 Type I 和 Type II 的精确终端判据。详见[K 内部缺口的 R 坐标残数拉回](../claims/internal-support-gap-residue-pullback.md)。

在旧 55 态上，完整内部菜单只闭合 37 态；所以 \(\Psi_0=1\) 的缺陷坐标只提供候选，不保证内部终端。

---

## 五、广义二进路线的推进与关闭

### 5.1 双向最大窗口选择器

对互素除子 \(A,B\mid L=2K\)，若

\[
A\equiv2^{j_0}B\pmod R,
\]

两个方向的二进预算为

\[
J_+=v_2(L)+v_2(A)-v_2(B),
\]

\[
J_-=v_2(L)+v_2(B)-v_2(A).
\]

每个非空窗口只需检查其中最大的合法指数。若正反窗口都非空，则两个大小条件不可能同时失败，所以至少一个方向产生合法偶终端。

一个一般充分条件是

\[
\operatorname{ord}_R(2)
\le
v_2(L)-|v_2(A)-v_2(B)|.
\]

详见[双向广义二进窗口的规范最大指数选择引理](../claims/type-I-general-bidirectional-dyadic-window-selector.md)。

### 5.2 自然标记提升在 F 状态中为空

对广义二进候选 \(E,n\)，定义自然标记分母

\[
\alpha=rac{nK}{E}.
\]

已有精确恒等式

\[
\frac4n-\frac1\alpha
=rac RK
=rac4p-rac1{pK}.
\]

因此包含 \(\alpha\) 的较小方程标记解，与包含 \(pK\) 的目标标记解精确双射。

但该标记源非空，当且仅当

\[
rac RK
\]

本身能分成两个单位分数，也就是当前图表已经存在中心 Type I 除子。于是对 finite-exponent F 状态：

\[
\boxed{
\text{每个广义二进偶前驱的自然标记源均为空}.
}
\]

详见[广义二进偶前驱的自然标记提升等价与 F 态零分支](../claims/type-I-generalized-dyadic-natural-lift-equivalence.md)。

这意味着，继续扩大同类 \(E,n\) 枚举基本不会推进证明。二进路线只应继续研究：

- 不同于 \(\alpha=nK/E\) 的标记分母；
- 改变一条或两条尾；
- 将终端失败证书映到 external slab、D-only 或跨图表终端。

---

## 六、external slab 的新接口

### 6.1 单外部 \(q\)-slab

设形式表示只留下一个 \(K\) 外素数幂

\[
Q=q^e,
\]

并写为

\[
X=Qa,\qquad Y=b,\qquad (X,Y)=1,\qquad ab\mid K,\qquad X+Y=Rm.
\]

记

\[
L=XY.
\]

对任意 \(T\mid X+Y\)，已有两类直接碰撞：

- 若
  \[
  4L\mid p+T,
  \]
  则得到 gap \(T\) 的 Type II 证书；

- 若
  \[
  4L\mid pT+1,
  \]
  则以 \(T\) 为新模数得到中心 Type I 命中，并恢复原素数的自然 Type I gap。

详见[单新支撑 q-slab 的双碰撞终端与容量吸收图表族](../claims/type-I-formal-external-slab-collision-absorption-rechart.md)。

### 6.2 部分容量吸收

若 \(q
e p\)，对任意

\[
Q\mid M\mid L
\]

定义唯一代表

\[
1\le R_M<4M,
\qquad pR_M\equiv-1\pmod{4M},
\]

以及

\[
K_M=rac{pR_M+1}{4}.
\]

则

\[
M\mid K_M.
\]

在隔离的 `external_capacity_absorption` 阶段中，若

\[
R_M<R,
\]

则以同一个目标解集

\[
W=\operatorname{Sol}(p)
\]

作为两端标记，恒等映射给出全域解提升，而势函数 \(R\) 严格下降。这是一条真正满足局部 E1--E5 的合法重图表边。

特别取 \(M=Q\)，因为 \(R_Q
e R\)，得到

\[
\boxed{
Q\lerac R4
\Longrightarrow
R_Q<R.
}
\]

因此 external slab 已被压成：

\[
\boxed{
\text{直接碰撞}
\quad\lor\quad
\text{small-slab 吸收}
\quad\lor\quad
Q>rac R4.
}
\]

真正未决的是 large-slab 以及不能使用同 \(p\) 图表吸收的特殊外部坐标。

### 6.3 完全换支撑不是自动成功

仓库还构造了一个适用于每个核心素数的规范完全换支撑重图表：从

\[
\left(\frac{p-1}{4},1,3\right)
\]

转到

\[
(1,1,p-2).
\]

它具有恒等解提升和严格降低的图表势，而且新旧 \(K\) 支撑完全不交；但规范终点对所有 \(p\) 都是 G 状态。详见[规范完全换支撑重图表及其普适 G 态终点](../claims/type-I-canonical-complete-support-rechart-g-obstruction.md)。

这条结果说明：

> 合法换支撑和良基下降本身仍不够；下降终点必须有直接终端，或能继续进入一个真正闭合的标记递归。

---

## 七、D-only 双尾标记正规形

设

\[
2\le n<p,
\qquad r=p-n,
\qquad N=np,
\qquad C=4r.
\]

所有可能保留两个尾分母、只替换一个正坐标的提升，恰由满足

\[
D\mid N^2,
\qquad0<D<n^2,
\]

\[
D\equiv N\pmod C,
\qquad
N^2/D\equiv N\pmod C
\]

的因子 \(D\) 参数化。定义

\[
a_D=rac{N-D}{C},
\qquad
 a_D'=rac{N^2/D-N}{C}.
\]

则对所有正整数 \(b,c\)：

\[
\boxed{
(a_D,b,c)\in\operatorname{Sol}(n)
\iff
(a_D',b,c)\in\operatorname{Sol}(p).
}
\]

标记集

\[
W(p,n,D)
=\{(a_D,b,c)\in\operatorname{Sol}(n)\}
\]

的非空性又精确等价于

\[
\exists z>0,\qquad z\mid\sigma^2,\qquad z\equiv-\sigma\pmod\mu,
\]

其中 \(\mu,\sigma\) 由 \(p,n,D\) 显式计算。详见[双尾提升的 D-only 标记正规形与 p 载体刚性](../claims/two-denominator-lift-d-only-marked-normal-form.md)。

若只给 \(D\)，得到的是一条局部验证、仍待递归闭合的条件边；若同时给出 \(z\)，则已经显式恢复 \(b,c\)，进而得到目标解，应直接登记为终端。

关键边界是：合法 \(D\) 可能对应空标记集。普通归纳假设

\[
\operatorname{Sol}(n)\ne\varnothing
\]

不能推出指定坐标切片 \(W(p,n,D)\) 非空。因此，D-only 路线真正的任务是规范选择一个可递归证明非空的 \(D\)，而不是仅证明 \(D\) 的两个同余有解。

---

## 八、当前证明前沿应如何重新表述

目前最准确的旗舰目标是：

\[
\boxed{
\begin{array}{c}
\text{任意 terminal-first 后仍未闭合的 }\Psi_0=1\text{ 状态}\[1mm]
\Downarrow\[1mm]
\text{完整 Reach 中存在直接终端、跨图表中心命中、}\
\text{可吸收 external slab，或非空且可提升的 D-only 后继。}
\end{array}
}
\]

量词必须使用完整可达域：

\[
\forall S\quad
\exists v\in\operatorname{Reach}(S):
\operatorname{Exit}(v).
\]

不能错误替换为：

- 每个起始见证都有出口；
- 每个汇 SCC 都含终端；
- 某个统一 gap 对所有状态有效；
- 某个较小偶数 \(n\) 自动可提升；
- 某个合法 \(D\) 自动对应非空标记集。

瞬态 Reach 节点可以独占产生直接证书，因此在完整 Reach 已经 terminal-free 之前，不能只分析汇 SCC。

---

## 九、最可能较快取得突破的研究方向

### 9.1 第一优先级：\(m=1\) large-slab 的 \(a=1,2,3\) 压缩

在最终 \(m=1\) 周期层，单外部 slab 满足

\[
Qa+b=R,
\qquad Q>rac R4.
\]

因为 \(Qa<R\)，立即得到

\[
\boxed{a<4,\qquad a\in\{1,2,3\}.}
\]

这意味着 large-slab 不是无界参数问题，而只有三类内部系数。

#### \(a=1\)

此时

\[
Q+b=R,
\qquad Q=|b-R|.
\]

所以外部 \(Q\) 已经直接出现在当前仿射边界菜单

\[
|A-R|,\ |B-R|
\]

中。下一步不是再发现这个候选，而是证明：其因子或跨图表中心谱为什么必有一个命中；若不命中，应该如何构造 D-only 后继。

#### \(a=2\)

因为 \(2\mid K\)，而核心素数满足 \(p\equiv1\pmod8\)，由

\[
4K=pR+1
\]

得到

\[
R\equiv7\pmod8.
\]

同时

\[
rac R4<Q<rac R2.
\]

这个分支应与 \(R\equiv7\pmod8\) 的周期翻转正规形、radical/multiplier bridge 和二进窗口一起分析，而不是当作一般 slab。

#### \(a=3\)

因为 \(3\mid K\) 且 \(p\equiv1\pmod3\)，有

\[
R\equiv2\pmod3,
\qquad
rac R4<Q<rac R3.
\]

这与周期核心可实现性的模 3 条件高度一致，可能允许用 CRT、Jacobi 或 Type II 射线作进一步分流。

建议建立明确候选命题：

> 对 \(m=1\) 单外部 large-slab，若 \(Qa+b=R\)、\(Q>R/4\)、\(ab\mid K\)，则在 \(a=1,2,3\) 三类中至少发生：直接 Type I/II、跨图表中心命中，或一个显式非空的 D-only 标记状态。

这是目前最有可能把有限正信号升级成一般分支的方向。

### 9.2 一个可能快速删去的分支：原始线性图表中的 \(q=p\)

对于原始线性源状态

\[
p=a+s+asR,
\]

恒有

\[
R<p.
\]

若最终 \(m=1\) slab 的外部素数满足 \(q=p\)，则

\[
Q=p^e,\qquad Qa\ge p>R,
\]

与

\[
Qa+b=R
\]

矛盾。

因此，在**原始线性图表的最终 \(m=1\) 周期层**，\(q=p\) 应当结构性为空。它只可能在：

- \(m>1\) 的瞬态节点；
- 后续非线性重图表；
- 不再满足原始线性 \(R<p\) 的扩展状态

中出现。

建议将其写成独立引理并核对所有状态合同。如果成立，可把当前前沿列出的

\[
	ext{large-slab},\quad q=p,\quad	ext{标记集非空}
\]

进一步收缩为

\[
	ext{large-slab},\quad	ext{标记集非空}
\]

至少在原始线性分支上成立。

### 9.3 第二优先级：D-only 标记集的低复杂度非空充分条件

D-only 非空判据是

\[
z\mid\sigma^2,
\qquad
z\equiv-\sigma\pmod\mu,
\qquad(\mu,\sigma)=1.
\]

以下充分条件是立即可用的：

1. \(\mu=1\)：取 \(z=1\)；
2. \(\mu=2\)：\(\sigma\) 为奇数，取 \(z=\sigma\)；
3. \(\mu\mid\sigma+1\)：取 \(z=1\)。

因此下一步不应无目标地枚举所有 \(D\)，而应尝试从 large-slab 或 Reach 节点规范构造 \(n,D\)，使

\[
\mu\in\{1,2\}
\quad\text{或}\quad
\mu\mid\sigma+1.
\]

若能对一个无限子族证明这一点，就能直接写出 \(z,b,c\) 和目标解，得到真正的终端定理，而不是空标记风险尚存的条件边。

更长远的目标是证明一个选择定理：

\[
\forall(p,S)	ext{ 未闭合状态}
\quad
\exists n<p,\ D\in\mathcal D(p,n):
W(p,n,D)
e\varnothing.
\]

### 9.4 第三优先级：核心可实现的两翻转周期

两翻转周期已有闭式 \((Q,T,h)\) 正规形和强交叉整除。可优先尝试证明：

> 每个满足核心可实现条件的两翻转通用周期，都由 direct radical 或 multiplier bridge 终端化。

这相当于证明三个目标陪集中的至少一个具有单位盒短代表。

建议搜索空间只保留：

- 满足核心可实现条件的周期；
- 两翻转正规形；
- 所有中间互补坐标的完整支撑；
- 直接三目标 miss。

若发现首个核心可实现反例，应冻结完整 Smith/关系格证书；若长期无反例，则应尝试由交叉 radical 整除直接构造短代表，而不是继续单纯扩大 \(R\) 上界。

### 9.5 第四优先级：固定仿射边界菜单的全称化或尽快证伪

当前五项菜单

\[
\{A,B,m,|A-R|,|B-R|\}
\]

在四个最终余项上全部命中，并把 483 态闭合。但其来源仍是有限正信号。

应立即做两件事：

1. 对更广的核心可实现 \(\Psi_0=1\) 状态作**反例导向**搜索，而不是继续统计覆盖率；
2. 尝试从迁移公式
   \[
   A_0=A/q,\qquad B_0=(B+Rt)/q,\qquad m_0=(m+t)/q
   \]
   证明为什么端点 \(t=0,-1\) 必产生某个合法缺口因子。

一旦找到完整 Reach 五项全 miss 的核心状态，这条路线应立即降级，不再追加第六项菜单。

### 9.6 暂停继续扩大普通广义二进终端

完整 483 态已经在未标记层面全部有较小偶前驱，但自然标记提升在 F 状态中严格为空。继续增加 \(j\)、枚举更多 \(E\) 或扩展同类偶源，只会重复这一逻辑障碍。

二进方向只保留：

- 非自然标记；
- 改变尾项；
- 将失败合同映入 external slab 或 D-only；
- 直接 Type I/II 交叉图表桥。

---

## 十、建议的统一证明骨架

### Phase A：terminal-first

对每个状态先完整检查：

- 内部 \(M\mid K\) 缺口；
- 已建立的 Type I/II 射线；
- 中心平方除子谱；
- 规范双向二进窗口；
- 已知跨图表中心谱。

命中即返回直接证书，不制造虚假后继。

### Phase B：完整形式 Reach

若仍未闭合：

- 构造完整超高图；
- 汇点直接 Type I；
- 无汇点时归约到 \(m=1\) 周期。

### Phase C：周期格三分

对周期关系格执行：

\[
	ext{HIT}\quad\lor\quad	exttt{MISS\_EXTERNAL}\quad\lor\quad	exttt{MISS\_CAPACITY}.
\]

- HIT：直接 Type I；
- `MISS_EXTERNAL`：提取最小外部 Smith circuit 或单 external slab；
- `MISS_CAPACITY`：提取最小内部超限向量和带符号缺陷。

### Phase D：external slab

应用：

\[
	ext{双碰撞}
\quad\lor\quad
Q\le R/4	ext{ 的吸收重图表}
\quad\lor\quad
m=1,\ a\in\{1,2,3\}	ext{ 的 large-slab}.
\]

### Phase E：真正递归

只有下列对象可以进入递归证明图：

- 已证明标记集非空的 D-only 状态；
- 满足完整 E1--E5 的 support switch；
- 新 equation target 上的合法标记状态，带全域解提升和预定义良基势严格下降。

任何只降低形式参数、只改变图表、只解出同余或只产生较小偶数的对象，都保持为 `analysis_evidence` 或 `candidate_transition`。

---

## 十一、怎样衡量“实质性突破”

下一阶段不应再以新增主张数、冻结命中数或素数扫描上界作为主要指标。建议采用以下标准。

### 一级突破

证明一个不含有限扫描上界的非平凡分支，例如：

- large-slab \(a=1,2,3\) 全部分流；
- 核心可实现两翻转周期全部三目标命中；
- 一个无限 D-only 子族标记集自动非空。

### 二级突破

构造第一族真正满足以下全部条件的递降边：

1. 合法后继状态；
2. 后继标记集非空或有完整递归闭合；
3. 全域解提升；
4. 预定义良基势严格下降；
5. 不依赖先知道目标证书。

### 三级突破

把当前三个余项压成一个，或者证明其中一个分支结构性为空。

### 不再计为突破

- 继续扩大同一冻结谱；
- 继续增加仿射菜单项；
- 继续枚举自然广义二进终端；
- 只证明新同余有整数解；
- 只发现合法重图表但终点仍为空/G；
- 对有限图事后赋拓扑序；
- 只给 D 而不处理标记集非空。

---

## 十二、建议的六周集中计划

### 第 1 周：冻结主干与补独立验证

- 固定 cycle-or-hit、周期格、核心可实现性、三目标桥、external slab 和 D-only 六条核心主张；
- 为它们建立独立 verifier；
- 不再扩大 483 状态菜单；
- 将 \(m=1\) 原始线性图表中的 \(q=p\) 排除写成正式候选引理并做反例审计。

### 第 2 周：large-slab 三类完全分类

对 \(a=1,2,3\) 分别推导：

- 可用模类；
- \(Q\) 的大小区间；
- 两碰撞的因子条件；
- \(R_Q\) 和其它 \(R_M\) 的方向；
- 与五项仿射边界菜单的重合；
- 可构造的 \(n,D,\mu,\sigma\)。

输出必须是定理候选或明确反例，不是覆盖率表。

### 第 3 周：D-only 低复杂度非空子族

系统搜索和证明：

\[
\mu=1,\quad\mu=2,\quad\mu\mid\sigma+1
\]

是否能由 large-slab 三类中的某一类强制。若不能，保存最小核心可实现反例，并寻找下一个规范条件，而不是任意扩大 \(D\) 菜单。

### 第 4 周：两翻转周期三目标短代表

- 仅枚举核心可实现两翻转正规形；
- 检查周期子格三个目标陪集与单位盒；
- 提取最小 miss 的完整 Smith 数据；
- 若无 miss，尝试从交叉 radical 整除直接证明短代表。

### 第 5 周：统一状态机

把 terminal-first、Reach、周期格、slab、D-only 写入同一 typed selector：

- 每个输出标明 `terminal`、`candidate_transition` 或 `verified_edge`；
- 只有 verified edge 承担递归；
- 明确每条边的势函数阶段，避免允许反向图表边形成二环。

### 第 6 周：外部审阅与论文级整理

- 邀请至少一名数论研究者审阅六条核心主张；
- 将周期结构、external slab 和 D-only 拆成可独立阅读的三个章节；
- 用第二实现复核所有代表性整数例和有限扫描摘要；
- 决定哪一个方向进入下一轮主攻，另外两条降为辅助接口。

---

## 十三、证据治理风险

当前主张账本共有 695 条主张，其中：

- `established`：297；
- `computationally_reproduced`：360；
- `independent_review`：18；
- `internal_review`：250；
- 证明来源 `unspecified`：427；
- 审阅状态 `unspecified`：427。

见[主张证据账本](../index/theorem-ledger.md)。

因此，当前研究速度已经远高于独立复核速度。最近的一般定理越来越接近证明主干，一处共同建模错误的影响也随之增大。

建议：

1. 暂停继续生产大量微型主张卡；
2. 将核心证明依赖压缩为 10–15 条主张；
3. 对核心六条一般定理进行第二实现和人工逐式复核；
4. 为 `established` 的核心仓库推导要求至少 `independent_review`；
5. 将大规模结果文件的生成器和验证器分离；
6. 将最近新增复现程序纳入 CI，而不是只保存脚本和哈希。

---

## 十四、最终评价

最近进展具有实质性，原因不是冻结覆盖率提高，而是证明对象发生了正确的结构收缩：

- 任意形式树被压到 Type I 或 \(m=1\) 周期；
- 周期被压到二阶目标陪集和容量盒；
- 抽象周期是否与核心素数相容已有无穷素数判据；
- 周期的直接 radical 错误命题被三目标乘子桥修正；
- external slab 首次接上直接终端和合法降 \(R\) 重图表；
- 双尾提升首次具有完整的 \(D\)-only 状态参数化和全域解提升。

项目已经从“证书搜索实验室”进入“少数结构引理决定成败”的阶段。

最值得主攻的不是再次扩大样本，而是：

\[
\boxed{
\text{large-slab 的 }a=1,2,3	ext{ 三分}
}
\]

和

\[
\boxed{
\text{D-only 标记集的规范非空选择}
}
\]

其中任意一条获得无样本上界的定理，都可以称为真正的近期突破。若两者能够连接——large-slab 规范地产生一个低复杂度且非空的 D-only 后继——就可能形成项目第一条真正可重复递归的证明分支。

完整猜想是否能很快解决，目前仍高度不确定；但在未来数周内取得一个可发表的无限分支定理、合法递降子族或周期全称子类闭合，是现实目标。研究资源应集中在这些严格定义的节点上，而不再分散到新的有限菜单和同类终端枚举中。
