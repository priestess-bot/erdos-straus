# Erdős–Straus 项目最新研究进展与突破路线评估

> 审计日期：2026-07-31  
> 仓库：`priestess-bot/erdos-straus`  
> 起始基线：`11ce2518b8c48fb9efd71ef7645b738082be0fae`  
> 审计 HEAD：`abcacc918b93af2af1a5f0074cdcea850f920ed7`  
> 提交范围：基线之后 13 次提交  
> 报告性质：研究进展、证明量词、有限证据和下一阶段优先级的综合评估；没有独立重跑全部新增复现程序，也不是对所有新增主张的外部同行评议。

## 2026-08-01 吸纳更新

本报告已从远程仓库拉取并逐节用于下一轮研究。以下更新晚于原审计 HEAD，并覆盖本文
后文关于“两个主余项”的旧表述；原文其余部分保留为 2026-07-31 的路线基线。

报告提出的两个最高优先级方向都已产生一般结果：

1. **裸 G source 已解决。** 对每个合法核心图表 \(4K=pR+1\)，

   \[
   (U,V,m)=\bigl(p,R(p-1)-p,p-1\bigr)
   \]

   是显式实际形式源。因为 \(p\nmid K\)，唯一 \(q=p,t=1\) 边无 gcd 约分地一步到达
   \((1,R-1,1)\)。因此完整 raw 合同下，G 不再缺 source；anchor 直接进入 Type I、
   bundle marked absorb 或 bundle overflow。

2. **初始 overflow 已解决一步出口。** 对 verified overflow

   \[
   R_M>p,
   \qquad
   pn=4Md+1,
   \]

   固定 \(n\) 的每个因子

   \[
   L\mid Md,
   \qquad
   n<4L<p+n
   \]

   都给出合法小图表

   \[
   R_L=4L-n,
   \qquad
   K_L=L\left(p-\frac{Md}{L}\right).
   \]

   若 \(A\mid L\)、\(L>A\)，这是保持 \(\operatorname{Sol}(p)\)、恒等提升且严格降低
   absorbed-support 势的 `overflow_determinant` 边。若额外有 \(A=1,\ M<p\)，则
   \(d\ge2\) 且 \(L=d\) 总合法，所以小载体子族有 verified 后继；一般 \(A=1\) 不能
   删除 \(M<p\) 假设，负边界见[A=1 overflow 的小载体假设边界](../claims/type-I-overflow-a-one-generic-determinant-boundary.md)；
   但该负边界仍由对偶 \(d/r\) 外层 RESET 处理，见[A=1 overflow 的对偶外层秩 RESET](../claims/type-I-overflow-a-one-dual-outer-rank-reset.md)。

此外，任意 overflow 写 \(M=kp+r\) 后都有载体 \(d,r\) 的两个对称图表，至少一个满足
\(R_t<p\)，并且该小图表的载体严格满足 \(t<M\)。这给出一个可定义外层
`overflow_carrier_reset` 秩的候选，但没有自动保留累积 support，也没有自动保证
reset 后的 phase 不重新回到较大的 carrier。

这一 phase 风险已有精确回执：\(p=73\) 上的 \(M=38\) overflow 取 \(t=12\)，其
\(R_t=23,K_t=420\) 的 anchor bundle 为 \(Q=11\)。若把 \(t\) 作为新的 charged
support，普通 `lcm` 重入给出 \(38\to132\to330\to132\)，其中 \(M=132\) 的 reset
载体为 \(30\)，而 \(M=330\) 的 reset 载体回到 \(12\)。因此 \(t<M\) 只证明局部
算术下降，不能证明全局良基；RESET 必须封闭在不可重入 phase，或由独立外层秩支付。

新的精确瓶颈是：

\[
\boxed{
\text{递归可达的 }A>1\text{ overflow 是否必有保持旧 }A\text{ 的 alternate/终端，}
\text{或能否由独立外层秩支付 support reset。}
}
\]

这不是措辞上的保守。根 Jacobi-G 状态 \((73,39,712;1)\) 经通用 anchor 合法进入
\((73,51,931;19)\)；从该 anchor 出发的完整 16 节点 bottom Reach 无 raw terminal，
全部合法 bundle 只有 \(Q\in\{2,32,44,50\}\)。四者全部 overflow，其对称双图表
没有一个既保留 \(A=19\) 又严格增加 support，且 fixed-\(n\) 支撑保持窗口也全部为空。
该例反驳当前菜单的全称闭合，不是 Erdős--Straus 反例，也不排除别的 source、marked
state 或直接短证书。

   **2026-08-02 账本细化。** 对称双载体的支撑失败现已进一步消元。若
   \(M=kp+r\)，则 d 通道的旧 support 整除等价于
   \(A/\gcd(A,d)\mid k+1\)，r 通道等价于
   \(A/\gcd(A,r)\mid dn-1\)。对每个 \(q^a\parallel A\)，这两个条件又精确分解为
   载体支付和余数支付：

   \[
   P_d(q)=\min\{a,v_q(d)+v_q(k+1)\},
   \qquad
   P_r(q)=\min\{a,v_q(r)+v_q(dn-1)\}.
   \]

   相应未支付高度是正部差值；若 \(q\mid d\)，则 \(dn-1\) 是 q-进单位，若
   \(q\mid r\)，则 \(k+1\) 是 q-进单位。因此阻碍带有方向性，不能无符号合并两个
   通道的余数层。聚焦的 12 个 overflow、24 个双通道和 30 个素数幂账本行全部通过
   截断赋值、方向性单位和阻碍乘积核验。它仍不产生跨状态容量或递归边，详见
   [overflow 双对偶支撑阻碍的逐素数幂支付分解](../claims/type-I-overflow-qadic-obstruction-transfer.md)。

   **缺陷单位相位边界。** 对每个非零未支付高度 \(h\)，把通道标签 \(\ell\) 去掉其
   \(q\)-进赋值 \(b\)，得到 \(\eta=(\ell/q^b)\pmod {q^h}\)。只有额外证明不同状态
   的 \(\eta\) 满足嵌套同余，才能把它们送入 phase-tree capacity。17 条阻碍幂记录
   形成 5 个 q 分组和 13 个条件性相位胞，5 对兼容记录、0 个容量超载胞；因此
   原始 obstruction 不自动形成共享相位资源。下一步必须寻找真实 alternate 的同余
   映射，或把缺陷单位直接转成 Type I/II/合法下降。见
   [overflow 缺陷单位的条件性相位胞与容量边界](../claims/type-I-overflow-defect-unit-phase-capacity.md)。

3. **固定层稳定子—Fourier 接口已精确化。** 对固定层稳定子
   \(P=\operatorname{Stab}_H(J)\)，固定目标的表示数满足
   \(N_J(t)=\bar N(\pi(t))\)；只有在目标陪集 \(tP\) 上求和时才出现 \(|P|\) 因子。
   Fourier 系数则恰在 \(P^\perp\) 上按 \(|P|\) 放大、其外消失，所以 F 缺失可以
   规范限制到商群角色，阈值分母由 \(|H|-1\) 改为 \(|H/P|-1\)。真实 F 核心
   \((193,63,3040)\) 的现有聚焦回执是 \(J=\mathcal A_{63}(608)\) 的一侧
   固定层切片，给出 \(|P|=6\)、\(|H/P|=6\) 与商谱最大幅度 \(2\sqrt3\)，并核验
   了每个切片目标的计数恒等式；它不是中心化 \(\mathcal C_R(N)\) 分解的数值回执。
   另一个中心化控制给出商向量 \((3,2,1,0,1,2)\) 与 target-odd 能量 \(33\)。
   这些都是状态内精确约化，不是
   跨状态容量定理；下一步要把商角色阶、幅度和相位分子转成 overflow 的带符号载体
   需求。

   该回执已按统一状态合同登记为
   `certificate_type=fixed_layer_quotient_fourier`、`selector_status=analysis_evidence`、
   `recursive_edge_eligible=false`；一侧切片幅度以精确平方范数 `12` 保存，而不是用
   浮点值承担证据。这样可以把表示、对偶和容量字段放进同一状态记录，同时保留“对偶证书不是
   递归边”的类型边界。新增的有限角色阶债务在该回执中为 `1/36`，但
   `carrier_mapping_status=unproved`；它只是连接 Fourier 与容量的中间字段，不能
   被解释为已经得到跨状态 \(q\)-进容量矛盾。

**2026-08-02 状态级分派收口。** 以上三类证据现已由
`reproductions/type_i_representation_dual_capacity_selector.py` 装配为统一的
内容寻址状态回执，并把 overflow q 进支付/缺陷单位审计作为独立的容量回执附加。分派
顺序固定为 `direct -> near -> dyadic -> quotient-Fourier -> overflow-fixed-n -> overflow-fixed-n-outer-rank-reset -> overflow-fixed-n-bounded-divisor-outer-rank -> overflow-same-chart-support-promotion -> overflow-fixed-s-outer-rank-reset -> overflow-outer-rank-reset -> overflow-capacity`；
每条回执均保存 `state_id`、根方程、目标纤维、标记集、带符号缺陷、证书上下文和势记录。
当前三条状态回执与一条容量回执仍严格保持 `analysis_evidence`，且
`recursive_edge_eligible=false`；但固定-\(n\) 行列式图谱中的正例
\((p,M,A)=(409,250,5)\to L=125\) 已重算出 \(R_L=11,K_L=1125\)，恒等解提升和
\(8323\to332\) 的支撑势下降均成立，故可标记 `verified_edge`。只有 E1--E5、解提升
和严格势下降齐备时才允许该升级，因此实现仍是类型安全的证据编排，不是全称选择器证明。
聚焦命令为：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

新增合同见[表示—对偶—容量统一选择器的状态级 typed 分派合同](../claims/type-I-representation-dual-capacity-selector-contract.md)。

**2026-08-03 RESET 外层秩更新。** 为处理上一节的载体重入风险，RESET 现要求先把
旧支撑与对偶载体合并为 \(A'=\operatorname{lcm}(A,t)\)，再检查 \(A'\mid K_t\) 和
\(\Pi_A(A')<\Pi_A(A)\)。统一回执在 12 个 overflow、24 个双通道上得到 8 条完整
`verified_edge`：3 条到达 \(R_t<p\) 的吸收态，5 条仍是 overflow 但支撑秩严格下降；
16 条不能支付旧支撑或 E5，继续保留为分析证据。该更新把“carrier-size 局部下降”与
“不可重置的全局支撑秩”分开，但尚未证明任意递归可达 \(A>1\) overflow 都能进入这
一分支。详见[overflow RESET 的 joined-support 外层秩递降](../claims/type-I-overflow-outer-rank-reset.md)。

同一批回执还修正了固定-\(n\) 空窗口的解释：对 d 通道
\(L=\operatorname{lcm}(A,d)\) 总有 \(L\mid Md\)，若 \(R_L>p\) 仍可生成 overflow
后继，并由 \(\Pi_A(L)<\Pi_A(A)\) 支付 E5。12 个 fixture 中 9 条通过该固定-\(n\)
窗口扩展，6 条是此前未登记的 overflow 递降，3 条落入 \(R_L<p\) 吸收态；只有 3 条
因 \(d=1\) 或 \(R_L\le0\) 失败。该结果把“窗口空”从无后继误读改为“没有窗口内
吸收态”，不关闭 r 通道或全称 \(A>1\) 存在性。详见
[固定 \(n\) 窗口上方的 overflow 支撑秩递降](../claims/type-I-overflow-fixed-n-overflow-rank-descent.md)。

**2026-08-03 对偶固定-\(s\) 更新。** 对 \(M=kp+r\) 的同一 overflow，恒有
\(ps=4rd+1\)。若 \(L=\operatorname{lcm}(A,r)\mid rd\)，则固定-\(s\) 图谱
\(R_L^{(s)}=4L-s\)、\(K_L^{(s)}=L(p-rd/L)\) 同样给出 canonical chart、恒等
提升和外层势下降。12 个 fixture 中该分支得到 7 条 E1--E5 边，5 条与 d 侧重叠，
2 条补上此前拒绝的 fixture；与固定-\(n\) 分支合计覆盖 11/12。剩余 d=1 边界仍不满足
\(L\mid rd\)，因此这一步收缩但没有消除 r 通道的全称整除缺口。详见
[overflow 对偶固定 \(s\) 图谱与 \(r\) 侧外层秩递降](../claims/type-I-overflow-fixed-s-dual-outer-rank-descent.md)。

**2026-08-03 同图表支撑升级。** 对来源可达的 complete-excess bundle overflow，若
\(A\mid M\)、\(M/A\ge2\) 且 \(M\le B_p=(p-1)^2/4\)，则可以保持同一个
canonical chart \((p,R_M,K_M)\)，把 absorbed support 从 \(A\) 升到 \(M\)。因为
\(K_M=MC\)，该升级支付 E2；\(\operatorname{Sol}(p)\) 对图表独立，恒等映射支付
E4；而 \(\lfloor B_p/M\rfloor<\lfloor B_p/A\rfloor\) 支付 E5。因此这是完整的
overflow 同图表 verified edge，但目标仍是 overflow。12 个聚焦来源行中有 11 条满足
该条件，唯一拒绝项是 \(p=73,M=1518>B_{73}=1296\) 的高载体行。对任意这样的高载体
行，令 \(S=Md=(pn-1)/4\)，则 \(M>B_p\) 排除 \(n\le p-4\)，而 \(n=p\) 仍是允许的
精确边界；结合 \(n\equiv1\pmod4\)，高载体残差满足 \(n=p\) 或 \(n\ge p+4\)。因此残差落在
大载体和大补余区域。当前余项可收缩为这一高载体区域，以及需要 alternate、直接
Type I/II 或其它外层秩的分支；11/12 只是有限回放，不是全称覆盖。详见
[overflow 同图表支撑升级](../claims/type-I-overflow-same-chart-support-promotion.md)。

同一高载体残差现在有一个更窄的固定-\(n\) 出口：若有界除子选择器找到
\(L\mid Md\) 且 \(L\le B_p<M\)，则
\[
R_L=4L-n<R_M=4M-n.
\]
因此该边在 absorbed-support 势之外还携带严格的 canonical-\(R\) 次级下降；选择器以
`high_carrier_R_descent` 字段逐项重算这一事实。当前 12 条有界固定-\(n\) 回执中仅
`lcm_cycle_step_0` 适用，\(3743\to2823\)，回放为 1/1。该结论仍是“候选存在时的
秩下降”，不证明高载体残差必有这样的除子，也不替代 alternate、终端或全局相位秩。
详见[高载体 overflow 固定 \(n\) 有界除子的 \(R\) 严格递降](../claims/type-I-overflow-high-carrier-fixed-n-R-descent.md)。

同一选择器现在把已建立的 \(p+4\) Type II 证书放在 overflow 递降之前：冻结的 12 个
fixture 全部重建为 `terminal_leaf`，其中 d=1 边界由 \(q=7\) 的证书直接
闭合。该有限覆盖不能外推为所有核心素数，因为一般 \(p+4\) 可能没有 \(3\bmod4\)
素因子。

   近邻偶前驱、广义 \(2^j\) 偶前驱和该商 Fourier 回执现已统一到终端优先协议；协议
   明确保存标准偶解但将 `lift_status` 保持为 `unproved`，因此这些回执仍不能替代
   F/G 状态的全域解提升或 overflow 的良基递降。见[Type I 终端优先统一选择器合同](../claims/type-I-unified-terminal-first-selector-contract.md)。

   随后的相位阶—载体高度聚焦复现进一步收紧了这条桥梁。冻结的 45 个双方向 F 状态共
   90 个活跃方向，其中 78 个非空相位投影方向的角色阶全为 2；其余 12 个高阶方向
   全部属于 6 个空投影状态。81 个同色实际载体组均满足模数差整除与 \(q\)-进容量上界，
   没有出现跨状态超载。因此角色阶债务目前只能作为状态内空投影证书，不能与实际块
   高度直接相加或互换；这一步仍没有得到一般的 `carrier_mapping`。详见[冻结 F 状态的
   相位阶—载体高度二分与容量边界](../claims/type-I-f-phase-order-carrier-capacity-dichotomy.md)。

   进一步把规范有界 Fourier 选择本身投影到线性源的实际块，而不预先固定最小活跃素数
   或第一个颜色：冻结 45 个状态共得到 141 个方向。113 个同色组和 100 个混色组的
   标签/模数整除链均通过，128 次两两检查和两类混合容量界均无超载；排除单例后最大
   容量比仍分别为 (12835/186111) 与 (38505/4787548)。因此这条更直接的
   Fourier--载体接口也只给出有限负边界：角色阶和相位预算尚未转成额外高度，不能据此
   关闭 bundle overflow 或生成递归边。详见[冻结 F 状态规范 Fourier 载体容量边界](../claims/type-I-f-bounded-fourier-carrier-capacity-boundary.md)。

   清分分支随后补上了一个严格的条件性容量接口。对固定 \(B\) 的盒外高度
   \(e=v_q(B)-v_q(K)>0\)，清分移位必须命中
   \(\gamma=-AR^{-1}\pmod{q^e}\)。若跨状态相位中心在每个最低共同层兼容，则任何
   命中相位的有界标签自动满足嵌套 \(q\)-进容量前提；标签重复度必须显式计入。新增
   合同只证明这条算术桥，不证明有界标签的全称存在或 marked lift，见[清分相位胞与
   跨状态容量合同](../claims/type-I-phase-clearing-cell-capacity-contract.md)。
   相位兼容现在还有等价的表示坐标判据：
   \(q^{\min(e_i,e_j)}\mid(A_iR_j-A_jR_i)\)。因此
   \(v_q(A_iR_j-A_jR_i)\) 可作为两状态的相位分离层数；该行列式为零时共同层完全
   兼容。这使相位胞划分可以从整数表示坐标直接重算。

   进一步，交叉行列式判据定义的兼容关系是等价关系；每个胞的模 \(q\) 首层相位为
   非零残基，但不同胞可以共享同一首层残基，因此胞数不自动受 \(q-1\) 控制。相位
   不兼容的状态可以先按等价类分胞，再逐胞应用容量界：在胞标签宽度为 \(M_c\)、
   重复度上界为 \(\mu\) 时，条件性地有
   \(\sum_i e_i\le\mu\sum_c(M_c/(q-1)+H_c)\)。只有额外证明首层残基单射时，才可
   把胞数压到 \(q-1\) 并进一步合并全局 \(M\) 项。这只补齐容量账本的分区方式，仍
   不证明有界标签、合法 marked lift 或 E1--E5 递归边。

   为处理首层碰撞而不丢弃高层信息，新增相位树容量字段。对高度层 \(k\) 令
   \(D_k=\#\{\gamma_i\bmod q^k:e_i\ge k\}\)，则统一标签区间宽度 \(M\) 和重复度
   \(\mu\) 给出
   \(\sum_i e_i\le\mu\sum_k D_k(\lfloor M/q^k\rfloor+1)\)。其中
   \(D_k-1\) 的加权和是显式的相位多样性税；兼容单胞的所有 \(D_k=1\)，同首层
   碰撞只在更高层增加税。这是一般的条件性账本，不是标签存在或递归边证明。

因此原六周计划应立即调整：

- 原第 3 周“寻找裸 G source”已完成，转为研究可达 \(A>1\) 的 alternate-source 完备性；
- 原第 2 周的 determinant 推导已完成到 fixed-\(n\) divisor atlas，下一步证明该窗口在
  哪些历史可达不变量下必非空；
- 同步研究允许丢弃旧 \(A\) 的 phase transition，但必须先给出跨 phase 的全局良基序；
- 两翻转周期三目标路线保留为独立辅助方向，不与当前支撑冲突菜单混写；
- 继续遵守只验证本轮新增公式、不重跑历史测试的证据策略。

新增严格主张见
[通用 \(p\) 源与容量锚点轨道](../claims/type-I-universal-p-source-capacity-anchor-orbit.md)及
[overflow 固定 \(n\) 对偶图谱](../claims/type-I-overflow-determinant-fixed-n-dual-support-conflict.md)，
相位阶—载体高度的冻结边界见[相位阶—载体高度二分](../claims/type-I-f-phase-order-carrier-capacity-dichotomy.md)。

> **口径修正（2026-08-03）。** 本报告后文若仍把“裸 G source”列为独立开放方向，均
> 属于 2026-07-31 审计基线的历史措辞；2026-08-01 更新中的显式
> \((p,R(p-1)-p,p-1)\) source 已关闭该接口。当前全称余项应只记为递归可达
> \(A>1\) bundle overflow 的 alternate/终端/良基 support reset；裸 G source 可作为
> 已解决前置引理，不再重复计入决定性缺口。

**2026-08-04 Type II 侧吸纳更新。** 共享 Type II 选择器的生成子群阈值又得到一个
p-primary 收紧。若合法缺口 \(m\) 的单位素因子残数生成子群满足
\[
H\simeq\bigoplus_i C_{\ell^{a_i}},
\]
则精确 Davenport 阈值
\[
D(H)=1+\sum_i(\ell^{a_i}-1)
\]
替代旧的 \(t\ge |H|\) 前缀碰撞阈值。达到该阈值即构造非空子序列积
\(D\equiv1\pmod m\)，与已有 Type II 证书组合成共享除子和 scaled-first marked
witness。10M、\(m\le239\) 回放在 84 个非 \(k=1\) 压力点中识别 51 个 p-primary
缺口，28 个达到阈值并构造新见证；阈值分布为 \(D=5\) 的 28 个缺口和 \(D=17\) 的
23 个缺口，仍有 56 个压力点未覆盖。完整证明、构造器和结果文件见
[p 群 Davenport 阈值](../claims/type-II-shared-p-group-davenport-threshold.md)。

这条结果是 Type II 共享选择器的局部结构推进，不改变旗舰问题的全称余项：它没有
处理非 p-primary 子群、低于 Davenport 阈值的短零积或跨缺口共同避靶，也不能把
marked Type II 表示升级为无标记递降。后文关于“两个主余项”的历史文字按上述
2026-08-03 口径解释。

**2026-08-04 秩至多二扩展。** 为处理上述非 p-primary 低秩缺口，现按单位残数生成子群
的完整 primary 分量恢复不变因子。对循环群 \(C_n\) 使用 \(D(C_n)=n\)，对
\(C_{n_1}\oplus C_{n_2}\)、\(n_1\mid n_2\)，使用
\(D(H)=n_1+n_2-1\)。10M、\(m\le239\) 回放在同一 84 个压力点中找到 933 个秩至多二
缺口（496 个循环、437 个秩二），29 个达到阈值并重建共享 marked witness；这 29 个
包含原 p-primary 分支的 28 个见证，并新增
\(p=1497049,m=39,H=C_2\oplus C_{12},t=13,D(H)=13,D_I=44032\)。
profile 仍有 55/84 个压力点未覆盖，且秩至少三、阈值以下短零积、跨缺口共同避靶和
marked 到无标记递降均未解决。详见[共享 Type II 秩至多二 Davenport 阈值](../claims/type-II-shared-rank-two-davenport-threshold.md)。

**2026-08-04 秩至少三序列级 profile。** 沿着上述未覆盖边界，新增回放只对秩至少三
的生成子群运行 0/1 动态程序，寻找给定 p+m 素因子多重序列的最短非空零积。10M、
m<=239 的 84 个压力点中只有 19 个秩三缺口：17 个结构为 C2 + C2 + C30，2 个
结构为 C2 + C4 + C12；动态序列搜索命中 4/84，80/84 未命中。4 个 marked
见证为 p=2669209、2852809、6254329、7504249，其中 3 个相对秩二 profile 是
新压力点，最短子积长度为 8、3、7、7。

这一步把下一阶段的可证方向收缩为秩三低于阈值的逆零和结构、因子顺序/分组不变量和
跨缺口联合避靶；它不声称一般秩三 Davenport 公式，也不把有限序列 miss 当作无共享
除子证明。主张卡见[共享 Type II 秩至少三序列短 profile](../claims/type-II-shared-higher-rank-sequence-short-profile.md)，
结果见[10M 秩至少三回执](../reproductions/type-ii-automatic-residual-higher-rank-short-profile-10m-results.json)。

**2026-08-04 秩三精确阈值补充。** Girard--Schmid 的 Theorem 2.7 给出
\[
D(C_2\oplus C_{2a}\oplus C_{2ab})=2a+2ab.
\]
当前 19 个秩三缺口分别落在
\(C_2\oplus C_2\oplus C_{30}\)（17 个，\(D=32\)）和
\(C_2\oplus C_4\oplus C_{12}\)（2 个，\(D=16\)）。19 个单位素因子序列均低于对应
阈值，因此 Davenport 分支命中为 0；这严格关闭的是“阈值强制共享除子”这一充分条件，
不是共享除子不存在。低于阈值的动态短零积 4 个命中仍独立保留。详见
[共享 Type II 秩三精确 Davenport 阈值](../claims/type-II-shared-rank-three-exact-davenport-threshold.md)
和[秩三精确 Davenport profile](../reproductions/type-ii-automatic-residual-rank-three-exact-davenport-profile-10m-results.json)。

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
\text{直接终端、bundle marked edge 或 bundle overflow}.
\]

这一链条中的多项接口已经成为不含素数扫描上界的一般命题：

1. 完整超高形式图的汇点精确等价于同状态 Type I 命中；中心 miss 时，任意持续轨道最终进入 \(m=1\) 周期；
2. 一个 \(m=1\) 周期生成的全部目标表示构成关系格中的二阶陪集，是否终端精确等价于该陪集是否与 \(K\) 指数容量盒相交；
3. 抽象通用周期何时能在无穷多个核心素数上实现为真实 \(K\)-支撑周期，已有完整 CRT/算术级数判据；
4. 外部单 \(q\)-slab 已有“两类直接碰撞或 small-slab 降 \(R\) 吸收”的无样本析取；
5. bottom sink-SCC 的全部 competing excess 已规范打包为 composite complete-excess
   bundle，并以 lcm 容量账本给出 marked edge 或显式 overflow；
6. 所有保留两尾、替换一个分母的正提升，已经被压缩成 \(D\)-only 标记正规形；同
   \(1\pmod4\) 的 non-source 标记纤维又已由 Vieta 下降全部排空。

同时，冻结有限证据也显著加强：完整 \(\Psi_0=1\) 谱由原来的 55 个状态扩展为 483 个状态，固定的内部缺口、双秩 Reach、跨图表中心谱和仿射边界菜单最终在这 483 个状态上全部产生独立验真的直接证书。

但是，当前仍不能合理声称猜想的完整证明已经迫近。真正未解决的不是“再找几个终端”，而是以下全称量词：

> 对任意 terminal-first 后仍未闭合的状态，为什么完整可达域必然产生直接 Type I/II、跨图表中心命中、可吸收 external slab，或一个标记集非空且满足完整解提升与良基下降的合法后继？

当前最窄的决定性余项是：

- \(R_M>p\) 的 complete-excess bundle overflow，其中
  \(M=\operatorname{lcm}(A,Q)\)，需要换载体、终端或全局良基 support reset。

独立的 Type II 共享选择器仍有 84 个有限压力点，其中秩至多二 Davenport 分支覆盖
29 个（p-primary 子分支覆盖 28 个）；它是辅助短证书路线，不是 overflow 余项的替代名称。

此前列出的 competing-excess sink-SCC 已由最小坐标 complete-excess bundle 定理
关闭为 marked absorb 或 bundle overflow，不再是独立余项。

综合判断：

| 维度 | 当前状态 | 评价 |
|---|---|---|
| 形式搜索的结构归约 | 已有一般定理 | 强进展 |
| 周期障碍的规范化 | 已有关系格和容量盒判据 | 强进展 |
| 冻结 \(\Psi_0=1\) 状态 | 483/483 状态内候选闭合 | 很强有限证据 |
| 广义二进终端 | 内部选择器成熟，自然提升被关闭 | 路线澄清 |
| external slab | clean \(AQ\) 与一般 bundle \(\operatorname{lcm}(A,Q)\) 均有良基边 | 余项只剩 bundle overflow |
| 标记递降 | \(n=p-1\) 层及同 \(1\bmod4\) 的 non-source D-only 均已证明全空；Type II 秩至多二 Davenport 分支新增 29 个有限命中 | overflow 必须换尾或换载体，全称 Type II 仍开放 |
| 全称选择器 | 尚未闭合 | 决定性缺口仍在 |
| 独立复核 | 仍明显不足 | 可信度瓶颈 |

最可能较快取得的“实质性突破”，不是继续扩展 483 个冻结状态，而是证明下面两类无样本上界的定理之一：

\[
\boxed{
\text{overflow determinant 的换载体、终端或合法后继定理}
}
\]

或

\[
\boxed{
\text{裸 G 的实际 source，或非保尾 marked 状态的全称构造定理}.
}
\]

前者有机会闭合 clean external slab 分支。过去设想的 overflow D-only 平方超额后继
现已被同余类 Vieta no-go 全部排除，不能再作为第二条突破路线。

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
A=\frac{Q(T-1)}h,
\qquad
R-A=\frac{Q-1}h,
\]

\[
B=\frac{T(Q-1)}h,
\qquad
R-B=\frac{T-1}h,
\]

其中

\[
h=\frac{QT-1}{R},
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
483\text{ 个 }\Psi_0=1\text{ 状态},
\qquad1615\text{ 条正向见证}.
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
x=\frac{p+M}{4}.
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
\alpha=\frac{nK}{E}.
\]

已有精确恒等式

\[
\frac4n-\frac1\alpha
=\frac RK
=\frac4p-\frac1{pK}.
\]

因此包含 \(\alpha\) 的较小方程标记解，与包含 \(pK\) 的目标标记解精确双射。

但该标记源非空，当且仅当

\[
\frac RK
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

若 \(q\ne p\)，对任意

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
K_M=\frac{pR_M+1}{4}.
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

特别取 \(M=Q\)，因为 \(R_Q\ne R\)，得到

\[
\boxed{
Q\le\frac R4
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
Q>\frac R4.
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
a_D=\frac{N-D}{C},
\qquad
 a_D'=\frac{N^2/D-N}{C}.
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
\text{任意 terminal-first 后仍未闭合的 }\Psi_0=1\text{ 状态}\\[1mm]
\Downarrow\\[1mm]
\text{完整 Reach 中存在直接终端、跨图表中心命中、}\\
\text{bundle marked edge，或其它非空且可提升的合法后继。}
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

> **当前重分类：** 三系数压缩仍是正确参数化，但不再是当前开放量词。
> absorbed-support 定理已经统一处理所有 \(R_{AQ}<p\) 的 clean slab，包括
> \(R_{AQ}>R\) 的上升图表。以下 \(a=1,2,3\) 分析保留为 overflow 的输入；
> 当前第一优先级是 \(R_{AQ}>p\) 的 determinant 分支，而不是重新证明三类局部菜单。

在最终 \(m=1\) 周期层，单外部 slab 满足

\[
Qa+b=R,
\qquad Q>\frac R4.
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
\frac R4<Q<\frac R2.
\]

这个分支应与 \(R\equiv7\pmod8\) 的周期翻转正规形、radical/multiplier bridge 和二进窗口一起分析，而不是当作一般 slab。

#### \(a=3\)

因为 \(3\mid K\) 且 \(p\equiv1\pmod3\)，有

\[
R\equiv2\pmod3,
\qquad
\frac R4<Q<\frac R3.
\]

这与周期核心可实现性的模 3 条件高度一致，可能允许用 CRT、Jacobi 或 Type II 射线作进一步分流。

该局部命题现在已由 absorbed-support/bundle 二分取代。真正候选命题应直接针对
\(R_M>p\)：

> 对每个 source/path/node 锚定的 large-slab 或 complete-excess bundle overflow，
> 至少发生直接 Type I/II、另一个 \(R_{M'}<p\) 的 anchored carrier，或一个改变尾数据
> 且满足完整 E1--E5 的非空 marked 状态。

这避免把已经全空的 same-class D-only 补秩重新放回菜单。

> **2026-08-01 因子对与载体更新。** large-slab 的三分现已进一步精确参数化。写
> \(Q=q^e,K=\alpha\beta c\)，则
> \[
> \beta(4\alpha c-p)=\alpha p q^e+1.
> \]
> 反向加入一个模 \(4\alpha\) 条件、\(q\nmid c\) 和
> \(\beta<(4-\alpha)q^e\)，便与算术 large-slab 双射。不同层还满足
> \[
> \gcd(N_{\alpha,e},N_{\alpha',f})
> =\gcd(N_{\alpha,e},\alpha'q^{f-e}-\alpha),
> \qquad N_{\alpha,e}=\alpha p q^e+1,
> \]
> 因此尾素数跨指数层的复用受乘法阶容量控制，同一指数的所有 admissible \(\alpha\) 分支不共享
> 奇尾素数。
>
> 来源路径字中的 slab 素数也有了精确判据。若
> \(a=v_q(\Theta),b=v_q(V),s=v_q(x_R)\)，终点两坐标的指数为
> \(e_U,e_V\)，则
> \[
> v_qC(L_U)=(a+e_V-s)_+,
> \qquad
> v_qC(L_V)=(|b-a-e_U|-s)_+.
> \]
> 这同时否定了“slab \(q\) 无条件属于共同过载 union”：
> \((p,R,q)=(10170169,127,101)\) 是来源锚定反例，但它已有锚点 Type I 和
> \(R_q<R\)。所以本节的主攻命题应收紧成以下三分，而不是继续证明错误的无条件载体：
> \[
> \boxed{
> \text{共同过载}
> \quad\lor\quad
> x_R\text{-覆盖出生并进入碰撞/ABSORB}
> \quad\lor\quad
> \text{首边继承 carrier-swap 的有界终端或合法 E4}.
> }
> \]
> 详见[large-slab 的受限因子对正规形与跨指数层支撑容量](../claims/type-I-large-slab-factor-pair-layer-capacity.md)。

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
\text{large-slab},\quad q=p,\quad\text{标记集非空}
\]

进一步收缩为

\[
\text{large-slab},\quad\text{标记集非空}
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

> **2026-07-31 后续校正。** 对合法核心 \(D\)-only 状态做完全消元后，两支都满足
> \(\mu\equiv3\pmod4\)，所以 \(\mu=1,2\) 实际上不会出现；
> \(\mu\mid\sigma+1\) 也在核心类中不可能。非 source-supported 分支的正确正规形为
> \[
> \mu=4\lambda-1,\qquad
> \sigma=p\lambda,\qquad
> H=p+(4\lambda-1)(p-n)\mid4\lambda^2,
> \]
> 其非空性等价于 \(\lambda^2\) 的因子命中三个模 \(\mu\) 目标之一。因此本节列出的
> 三个 shortcut 应关闭，替代任务是把 large-slab 或来源路径字映到上述 \(H\)-整除条件，
> 再证明三目标命中或构造合法 E4。详见
> [核心 D-only 的支撑二分与三目标谱](../claims/two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum.md)。

> **2026-08-01 路径字接口更新。** 来源路径字现可按祖先坐标写成
> \[
> \Theta X=U+Ru,
> \qquad
> \Theta Y=V+Rv,
> \qquad
> u,v\ge0,
> \qquad
> u+v=\Theta-m_1.
> \]
> 交叉约分 \((U,\Theta Y)\)、\((V,\Theta X)\) 产生两个规范相位 \(-1\)
> 表示；其乘积整除 \(K\) 即为直接 Type I，整除
> \(x_R=(p+R)/4\) 即为 gap \(R\) 的 Type II。双 miss 时得到可记录的
> \(q\)-进容量缺陷，但还没有跨状态超载。另一方面，把模 \(R\) 路径字送入同模
> 非自然 D-only 必须满足 \(\mu\mid R\) 且
> \[
> \mu>2\sqrt p-1.
> \]
> 因此小底层差值不能普遍承担该 E4；下一步应改为寻找大尺度路径量或新的跨模数
> 恒等式。详见
> [来源路径的底层投影、双节点相位差与双容量接口](../claims/type-I-source-word-bottom-projection-dual-capacity.md)。

> **2026-08-01 联合容量更新。** 对任一来源交叉乘积 \(L\)，令
>
> \[
> e_K=\frac{L}{(L,K)},
> \qquad
> e_x=\frac{L}{(L,x_R)},
> \qquad
> g=(K,x_R).
> \]
>
> 现已证明
>
> \[
> (e_K,e_x)=\frac{L}{(L,\operatorname{lcm}(K,x_R))},
> \qquad
> \operatorname{lcm}(e_K,e_x)=\frac{L}{(L,g)}.
> \]
>
> 因而双容量 miss 精确二分为“同一 \(q\) 同时过载”与“两个互素缺陷分别由
> \(x_R/g,K/g\) 的独占容量承担”。split 支还满足
>
> \[
> R e_K a-e_x b=\frac{R^2-1}{4g},
> \qquad
> a=\frac{x_R}{ge_K},
> \quad
> b=\frac{K}{ge_x}.
> \]
>
> 这条交换恒等式本身不是终端：\(p=122014489,R=471\) 给出来源锚定、内部终端为空的
> 单边 split，尽管同一路径另一交叉表示仍有共同过载，且完整 Reach 在 external gap
> \(35\) 有 Type I。更强地，\((p,R)=(2017,207)\) 是 F 且 internal-free，来源交叉
> 乘积严格 split，但其完整 post-first formal Reach 只有 5 个节点、5 条边，全部
> external gap 候选 \(103,139\) 都完整 miss。因此“split 强制任意有界深度的同图表
> external 终端”，甚至“split 的完整 formal Reach 必有 external 终端”都为假。
> 这里不能删除 external：该素数已有 ordinary gap \(15\)，且路径前缀还有
> \(R_{103}=115\) 的合法 absorption。一般底层边还会保持一个交叉表示完全不变，只
> 仿射更新另一个，所以 split 本身不是下降量。
>
> 两个共同过载表示也不必共享同一 \(q\)。另一方面，70 条现有
> formal-descendant residual 的探索性重建中，140 个交叉乘积全部仍有共同过载，且
> external slab 素数是唯一逐记录稳定的载体字段。由此下一步不再笼统寻找“某个缺陷
> 素数”，而应把 slab/suffix 载体组成跨状态可比较的向量容量；split 支必须把两个交叉
> 表示与 bottom SCC 一起纳入状态，再证明新容量下降或真正 E4，不再增加 depth 菜单。详见
> [来源交叉表示的联合容量共同过载—分裂交换二分](../claims/type-I-source-word-joint-capacity-common-split-dichotomy.md)。

> **2026-08-01 表示--对偶--容量与 bottom-SCC 更新。** 上述“向量容量”现已完成两层
> 一般化，但也出现了一个必须接受的反例边界。
>
> 第一层是精确三盒字典。对固定状态级有限素数支撑和互素相位 \(-1\) 表示 \((P,Q)\)，令
>
> \[
> z_\ell=v_\ell(P)-v_\ell(Q),
> \quad
> \nu_\ell=v_\ell(K),
> \quad
> \sigma_\ell=v_\ell(x_R),
> \quad
> \mu_\ell=\max(\nu_\ell,\sigma_\ell).
> \]
>
> 则
>
> \[
> e_K=\prod_\ell\ell^{(|z_\ell|-\nu_\ell)_+},
> \quad
> e_x=\prod_\ell\ell^{(|z_\ell|-\sigma_\ell)_+},
> \quad
> C=\prod_\ell\ell^{(|z_\ell|-\mu_\ell)_+}.
> \]
>
> strict split 因而恰是 \(B_\mu\setminus(B_\nu\cup B_\sigma)\)，共同过载恰是
> \(B_\mu\) 外部。给定见证 \(z\) 后，正负溢出指出载体位于 \(P\) 或 \(Q\)；但原来的
> 无符号 Fourier/Pareto 单项式不能恢复方向，跨状态证明若需要颜色必须使用
> \(T_\ell^+,T_\ell^-\) 双变量。联合盒内的目标表示数超过
>
> \[
> \prod_\ell\left\lceil
> \frac{2\mu_\ell+1}{\nu_\ell+1}
> \right\rceil
> \]
>
> 时，外盒近邻引理仍强制一个偶终端。这里的“选择不变”只相对于预先固定的支撑成立，
> 不能让每条路径自行改变生成元集合。
>
> 第二层是 bottom-word 正规形。底层定向路径字在缩放 ancestry 坐标上唯一写成
>
> \[
> M(Q,A,B)=
> \begin{pmatrix}A+1&A\\B&B+1\end{pmatrix},
> \qquad A+B=Q-1,
> \]
>
> 满足 \(QX'=X+AR\)、\(QY'=Y+BR\) 及
> \(\operatorname{SNF}(M)=\operatorname{diag}(1,Q)\)。同向周期重复 \(n\) 次后的四通道
> 赋值都是
>
> \[
> |d_{i,\ell}-n v_\ell(Q)|,
> \]
>
> 所以无限周期可由 CYCLE_RAY_HIT、MISS_STATIC 或 MISS_INTERVAL 有限判定。更一般地，
> 对 \(N\) 个 ancestry-lifted 顶点，固定首后继和定向终点后的每个 Pareto 极小签名及
> 任一容量命中，都有长度小于
>
> \[
> B=N\prod_{\ell\in\mathcal P_{\rm move}}
> \bigl(\max(0,a_\ell,b_\ell)+1\bigr)
> \]
>
> 的见证。因此无需再把任意图最短路径当成容量最优路径。
>
> 反例边界是
>
> \[
> (p,R,K,x_R)=(57073,23,328170,14274).
> \]
>
> 它有线性源、中心 F 状态和真实首边
> \((20,3,1)\to(10,13,1)\)；首后继就是 strong slab
> \((Q,\alpha,\beta)=(13,1,10)\)，但唯一最短空后缀满足
>
> \[
> L_U=L_V=130,
> \qquad
> C(L_U)=C(L_V)=1.
> \]
>
> 所以“strong miss 必有最短来源字使 slab \(q\) 进入共同过载”即使在 linear-source
> 下也为假。该例已有内部 gap \(15\) 和 Reach gap \(7\) 的 Type I，只是否定旧载体规则。
> 另一个 \((p,R)=(2017,207)\) 的 internal-free 例在底部二循环上由静态素数 \(103\)
> 分离四个容量通道，说明指定 cycle ray 可以严格输出 miss；它不说明整个状态没有
> terminal 或 descent。
>
> 短词可继续生成直接终端，但语义必须分开：\((5596369,35)\) 的路径积 \(38\) 选择出
> 中心命中的 \(R_{38}=23\)，却不是现有 E4；\((212973049,215)\) 到达
> \(\{3,212\}\) 后暴露的 single-slab \(Q=53\) 才满足已有 absorption 合同，并在
> \(R_{53}=171\) 中心命中。下一步主命题因此改为：对每个 terminal-first unresolved
> sink-SCC，把规范 Pareto/周期 miss 证书强制转成直接 Type I/II、改变根尾数据的非空
> D-only 状态，或完整 E1--E5 合法递降。SCC 凝聚序只是分析调度，不是猜想下降。详见
> [目标纤维溢出与联合容量的带符号载体字典](../claims/type-I-target-fiber-joint-capacity-signed-carrier-dictionary.md)和
> [底层路径字的格正规形、有限 Pareto 前沿与周期容量选择器](../claims/type-I-bottom-word-lattice-pareto-cycle-capacity-selector.md)。

> **2026-08-01 静态载体来源、完整纤维与 D-only 尺寸更新。** 对上述 \(p=2017\)
> 的语义已作事实更正。它不只是“可能另有出口”：路径前缀中
>
> \[
> (1,206)=(1,103\cdot2)
> \]
>
> 是 clean single-external slab，且
>
> \[
> R_{103}=115<207,\qquad K_{103}=103\cdot563,
> \]
>
> 所以现有合同已给出 E1--E5 verified absorption。循环节点的 \(101\)-slab 还有
> \(R_{101}=135\) 的中心 Type I gap \(3\)；原素数本身则同时有 gap \(15\) 的 Type I
> 和 Type II 证书。因此该例只反驳 cycle-ray 容量修复和同图表 external 终端，不能
> 再称 terminal-first 或 terminal-or-descent 反例。
>
> 这一更正可以提升为无样本来源三分。对任意 bottom 节点
> \(X=q^e a,Y\)、外部 \(q\nmid K\)，有
>
> \[
> \boxed{
> aY\mid K
> \Longrightarrow
> \text{ABSORB}(q^e)\ \lor\
> \text{LARGE}(q^e,a),\ a\in\{1,2,3\};
> }
> \]
>
> 若 \(aY\nmid K\)，则同一节点必有 \(r\ne q\) 满足
> \(v_r(aY)>v_r(K)\)，从而产生竞争 raw 边。于是 path-carried
> \(\texttt{MISS\_STATIC}(q)\) 可回溯为
>
> \[
> \boxed{
> \texttt{VERIFIED\_ABSORB}
> \ \lor\
> \texttt{LARGE\_SLAB}
> \ \lor\
> \texttt{COMPETING\_EXCESS}.
> }
> \]
>
> 三分不能再加强成“同一静态 \(q\) 必给出口”。精确边界
>
> \[
> (p,R)=(107722177,207)
> \]
>
> 保留同一个 \(103\)-static 二循环，但 \(R_{103}=375>207\)，gap \(103\)、两类
> collision、节点/锚点菜单和新图表中心谱全部 miss，所以它是旧的固定 \(R\) 菜单
> 边界；然而 \(R_{103}=375<p\)，在携带 absorbed support 后已经是势严格下降的
> marked edge。该状态也不是全局 unresolved：循环的 \(q=41\) 给
> \(R_{41}=35<207\) 并立即中心命中，\(q=101\) 的新图表也中心命中。详见
> [底层外部静态载体的来源三分与吸收边界](../claims/type-I-bottom-external-static-carrier-support-fork.md)。
>
> 完整目标纤维还排除了另一条过强容量路线。若基础支撑已经能表示 \(-1\)，扩张到 SCC
> 新标签并放宽预算时，旧坐标 forced height 只能下降，每个新坐标都可取指数 \(0\)，
> 因而 forced height 恒为零。\(p=2017,R=207\) 的完整联合支撑逐坐标全为零，尽管受限
> path language 有 \(\texttt{MISS\_STATIC}(103)\)。所以跨状态证明不能寻找“加入 SCC
> 后自动出现的强制单 \(q\)”；应保留完整多坐标 Pareto 或层化价格，并先证明 overflow
> 到实际有限载体容量的注入。
>
> D-only 方向也获得两个一般尺寸障碍。令
> \(\kappa\in\{1,2,3,4\}\) 由 \(n+\kappa\equiv0\pmod4\) 确定，则每个合法参数满足
>
> \[
> D\le n(n+\kappa)-\kappa p.
> \]
>
> 因而 \(\kappa p\ge n(n+\kappa)\) 时整个参数集为空；特别地，
> \(n\equiv3\pmod4,\ p\ge n(n+1)\) 时没有任何 D-only 后继。non-source-supported
> 分支还强制
>
> \[
> n>\sqrt p,\qquad
> \lambda>\max\left(p-n,\frac{\sqrt p}{2}\right).
> \]
>
> 这结构性关闭了把小 endpoint gap、短路径标签或小 rechart 模数直接当作 equation rank
> 的方案。当前优先级因此进一步收紧为：先在所有路径前缀和 SCC 节点扫描 direct
> terminal 与 clean-slab marked absorption；剩余只主攻 \(R_{AQ}>p\) 的 overflow、
> multi-excess SCC 的 clean-slab 强制，以及多坐标层价格的真实算术容量映射。

> **2026-08-01 累积支撑下降与 overflow 重分类。** 上一段的 “large-slab”
> 余项现在可以再严格缩小。在线性图表状态中增加 absorbed support
> \(A\mid K\)。clean external slab 给出 \(Q=q^e,\ q\nmid K\) 后，令
>
> \[
> M=AQ,\qquad
> pR_M\equiv-1\pmod {4M},\qquad
> 1\le R_M<4M.
> \]
>
> 若 \(R_M<p\)，则后继 \((p,R_M,K_M;M)\) 保持同一个 equation target \(4/p\)
> 和同一个标记集 \(\operatorname{Sol}(p)\)，解提升为恒等映射，而且
>
> \[
> \left\lfloor\frac{(p-1)^2}{4AQ}\right\rfloor
> <
> \left\lfloor\frac{(p-1)^2}{4A}\right\rfloor.
> \]
>
> 因此不再要求 \(R_M<R\)。已吸收素数永久保留在 \(A\mid K\) 中，不能重新作为
> external \(q\) 收费；每条边至少把 \(A\) 翻倍。过去列作 local strong miss 的
> \((107722177,207,Q=103)\)、\((21169,23,Q=7)\) 等例，由于 \(R_Q<p\)，现已是
> verified marked edge，而不是 residual。
>
> 真正 clean residual 是
>
> \[
> R_M>p.
> \]
>
> 此时 \(M>p/4\)。写 \(K_M=MC\)，并令
>
> \[
> n=4M-R_M,\qquad d=p-C,
> \]
>
> 得到精确 overflow determinant
>
> \[
> \boxed{pn=4Md+1,\qquad(M,pn)=1.}
> \]
>
> 它尚不是后继。初始 \(A=1,\alpha=2,3\) 时 \(h=4Q-p\) 是合法 gap，但完整
> \(p^iq^j\) 三目标谱已有 \(9,9,75\) 个候选全 miss 的三个精确边界，所以 overflow
> 后不能依赖 generalized prime-power terminal 自动闭合。
>
> 三个内部系数还给出不同接口：\(\alpha=1\) 有“gap 3 Type II 或规范
> \(\ell\equiv2\pmod3\) 容量超额”二分；\(\alpha=2\) 的固定载体补量严格下降
> \(d\mapsto d-4\tau\)，但换载体会重置；\(\alpha=3\) 产生
> \(n_*Q-p\beta'=1\)、\(0<n_*<p\) 的 Farey 邻接候选，但尚无全域解提升。
> 一个无穷 \(\alpha=1\) 算术族还给出 \(E=196,n=p-5\) 的广义 \(2^2\) 数据；
> 自然标记在中心 miss 时为空，所以它只能登记为
> unlifted_generalized_dyadic_candidate。
>
> 同图表的两个 clean slabs 还给出真实中心谱 cocycle
>
> \[
> \beta_j\beta_i^{-1}
> \equiv
> \frac{\alpha_j}{\alpha_i}q^{e_j-e_i}\pmod R,
> \]
>
> 且固定 \((p,R,K,q)\) 最多只有三条 slab。这为稳定子/Kneser 容量提供了常数大小的
> 真实输入，但中心谱本身不是群，尚不能直接推出饱和。
>
> \(D\)-only 方向也有新的全域 no-go：对每个 \(p\equiv1\pmod4\)，
> \(n=p-1\) 的 non-source-supported 标记纤维恒空；source-supported 分支只等价已有
> 中心 Type I。证明通过 \(s=a^2c,\lambda=abc\) 参数化和 Vieta 下降完成。因此后续
> D-only 只研究 \(p-n\ge2\) 的大尺度路径量。
>
> 这轮工作的净结论不是 large-slab 已闭合，而是优先级被改写为：
>
> 1. overflow determinant 的换载体/终端/合法标记状态三分；
> 2. 至多三个 \(\beta\)-ratio cocycle 的固定层稳定子容量；
> 3. \(\alpha=1\) 的 gap 3 容量超额及 \(\alpha=3\) determinant pair 的合法标记提升；
> 4. competing-excess SCC 到 clean slab 或直接终端的强制；
> 5. \(r\ge2\) 的大尺度 D-only 三目标，不再测试 \(r=1\)。
>
> 详见
> [累积支撑重图表与 overflow 边界](../claims/type-I-marked-support-accumulation-rechart-saturation.md)、
> [large-slab 因子层与 cocycle 容量](../claims/type-I-large-slab-factor-pair-layer-capacity.md)、
> [large-slab 三系数算术边界](../claims/type-I-large-slab-three-alpha-arithmetic-boundaries.md)和
> [p 减一秩 D-only no-go](../claims/two-denominator-lift-core-rank-one-no-go.md)。

> **2026-08-01 overflow-to-D-only 平方超额更新。** 对严格补秩
> \(u=4AQ-R_{AQ}<p\)，现已证明 \(u\equiv1\pmod4\)、\(p-u\in4\mathbb N\)，且每个
> D-only 参数都与累积支撑 \(AQ\)、determinant 互补量 \(d\) 和 rank gap \(p-u\)
> 互素。non-source 参数唯一写成 \(D=p\delta,\delta\mid u^2\)；若
> \(\delta\mid u\)，三个标记目标全部为空。因此真正可能的新后继必须具有
>
> \[
> \delta=cw^2,\qquad
> u=acw,\qquad
> \lambda=abc,\qquad
> a=w+4(p-u)b,\qquad
> w\ge3,
> \]
>
> 并满足
>
> \[
> \delta\ge9,\qquad
> 13u\ge12p+9,\qquad
> u(u+3)>12p.
> \]
>
> 这把 overflow-to-D-only 从任意因子搜索压成近 \(p\) 的平方超额问题。真实 clean
> overflow \((p,R,Q,R_Q,u)=(1129,1023,1021,2959,1125)\) 同时含
> \(\delta=5\mid u\) 的全域 no-go 和 \(\delta=405\nmid u\) 的 square-excess
> miss，说明平方超额仍只是必要条件。下一步只应证明真实载体为何强制这种超额并命中
> 三目标，或把其缺失转成换载体/competing-excess E4。详见
> [overflow D-only 平方超额边界](../claims/type-I-overflow-d-only-square-excess-no-go.md)。

> **2026-08-01 同 \(1\bmod4\) 的 D-only 全域闭合更新。** 上一更新中的
> square-excess 余项现已完全关闭。更一般地，设 \(p\) 是
> \(1\pmod4\) 的奇素数，\(2\le n<p\) 且 \(n\equiv1\pmod4\)。每个 non-source
> D-only 参数都可统一写成
>
> \[
> H=a^2c,\qquad
> \lambda=abc,\qquad
> n=acw,\qquad
> \delta=cw^2,\qquad
> a=w+4(p-n)b.
> \]
>
> 规范 \(e=1,e=2\) 目标由大小直接排除；假设 \(e=0\) 命中，则因子互补与消元给出
>
> \[
> 2XY=\frac{X^2}{L}+\frac{Y^2}{m}+\frac1c,
> \qquad X\text{ 奇},\quad Y\text{ 偶},\quad L>1.
> \]
>
> 奇偶保持的 Vieta 极小下降证明该方程没有正整数解。因此
>
> \[
> D\nmid n^2\Longrightarrow W(p,n,D)=\varnothing.
> \]
>
> overflow 的严格补秩 \(u\) 自动满足 \(p\equiv u\equiv1\pmod4\)。source-supported
> 分支只复述中心 Type I，non-source 分支由上式全空，所以 overflow-to-D-only 应从
> 选择器菜单整体删除；\(u<p\) 不能把空 marked state 变成合法递降。真正余项是从
> source/path/node 锚定的其它载体构造直接终端或 MARKED_ABSORB，或证明
> competing-excess SCC 必到达其中之一。详见
> [同 1 mod 4 秩的 D-only 全域 no-go](../claims/two-denominator-lift-same-one-mod-four-no-go.md)。

> **2026-08-01 complete-excess bundle 更新。** 上一段最后保留的 competing-excess
> SCC 量词现已闭合，但结论不是“必出现单素数 clean slab”。对任一来源可达完整
> bottom raw 图的 sink-SCC，取小坐标最小节点 \(\{x,y\}\)。若 \(x\) 仍有超出
> \(K\) 容量的素数 \(q\)，完整 raw 边会到达更小坐标 \(x/q\) 的同一 SCC，矛盾；
> 因而 \(x\mid K\)。若 \(xy\nmid K\)，令
>
> \[
> Q=\prod_{v_q(y)>v_q(K)}q^{v_q(y)},
> \qquad
> \beta=y/Q.
> \]
>
> 则
>
> \[
> Q>1,\qquad x\beta\mid K,\qquad
> (Q,x\beta)=1,\qquad Q\nmid K.
> \]
>
> 对 absorbed support \(A\mid K\)，规范容量并必须取
>
> \[
> \boxed{M=\operatorname{lcm}(A,Q),}
> \]
>
> 而不是一般的 \(AQ\)。它满足 \(M/A\ge2\)。若 \(R_M<p\)，两端均以
> \(\operatorname{Sol}(p)\) 为标记集、恒等映射为提升，并由
> \(\lfloor (p-1)^2/(4M)\rfloor<\lfloor (p-1)^2/(4A)\rfloor\) 得到完整
> E1--E5 边；若 \(R_M>p\)，则仍有
>
> \[
> pn=4Md+1,\qquad(M,pn)=1.
> \]
>
> 因此完整 Reach 已严格压成
>
> \[
> \boxed{
> \text{DIRECT TYPE I}
> \ \lor\
> \text{BUNDLE MARKED ABSORB}
> \ \lor\
> \text{BUNDLE OVERFLOW}.}
> \]
>
> 每个 F 状态自身给出 \(K\)-支撑的无界形式源，故 F 无条件进入后两支。精确例
> \((p,R,K)=(21169,19,193\cdot521)\) 的九节点 sink-SCC 没有任何 clean
> single-prime-power slab，却在最小点 \(\{1,18\}\) 给出复合 \(Q=18\) 和
> \(R_{18}=71<p\)。这既否定旧的单素数强化，也说明 competing-excess 已被正确吸收为
> composite bundle。初始线性 F overflow 还被压到 \(\alpha=1,\ as\in\{2,3\}\)；
> \(as=1\) 整族由 Jacobi 角色严格属于 G。详见
> [底层汇 SCC 的完整超额 bundle 选择器](../claims/type-I-bottom-sink-scc-complete-excess-bundle-selector.md)。

> 对更窄的 source-anchored clean single-external \(\alpha=1\) overflow，还能继续
> 无样本收缩。因 \(Q=q^e,\ q\nmid K\)，合法 \(q\)-peeling 会到达
> \(\{1,R-1\}\)。令 \(S=(R-1)/2\)：\(as=3\) 时 anchor 的新 bundle 是
> \((S,2)\) 且 \(R_S<p\)，故整支吸收；\(as=2\) 时，\(K\) 偶支同样吸收，\(K\)
> 奇支经规范余数分类只在 \(p\equiv73,169\pmod{240}\) overflow。前一类有统一
> gap \(7\) Type I 证书
>
> \[
> x=\frac{p+7}{4},\qquad d=\frac{x^2}{5},
> \]
>
> 所以该 clean 子类只剩必要类 \(p\equiv169\pmod{240}\)。此处必须保留范围：
> general complete-excess bundle 可以含 \(q\mid K\)，不能保证 peeling 到 \(1\)；
> 因而该模 \(240\) 结论不能推广到全部 bundle overflow。

更长远的目标应改写为不预设 D-only 的选择定理：

\[
\forall(p,S)\text{ 未闭合状态}
\quad
\exists\text{ 直接 Type I/II、MARKED\_ABSORB，或其它满足 E1--E5 的非空后继}.
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
\text{HIT}\quad\lor\quad\texttt{MISS\_EXTERNAL}\quad\lor\quad\texttt{MISS\_CAPACITY}.
\]

- HIT：直接 Type I；
- `MISS_EXTERNAL` 或 `MISS_CAPACITY`：保存规范格/Pareto miss receipt，并进入完整
  bottom sink-SCC；不再要求先提取单 external prime。

### Phase D：external slab

应用：

\[
\text{直接 Type I}
\quad\lor\quad
R_{\operatorname{lcm}(A,Q)}<p\text{ 的 bundle marked edge}
\quad\lor\quad
R_{\operatorname{lcm}(A,Q)}>p\text{ 的 bundle overflow}.
\]

这里 \(Q\) 由 sink 最小节点的全部超容量完整素数幂块唯一确定。单素数 clean slab 的
双碰撞仍可在此前作为快捷终端，但 competing excess 不再保留为独立 Phase D 输出。

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

- overflow determinant 的换载体/终端/合法后继全部分流；
- 核心可实现两翻转周期全部三目标命中；
- 裸 G 状态的规范实际 source 或非保尾 marked 状态构造。

### 二级突破

构造第一族真正满足以下全部条件的递降边：

1. 合法后继状态；
2. 后继标记集非空或有完整递归闭合；
3. 全域解提升；
4. 预定义良基势严格下降；
5. 不依赖先知道目标证书。

### 三级突破

把当前两个余项压成一个，或者证明其中一个分支结构性为空。

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

### 第 1 周：冻结主干与定向复核

- 固定 cycle-or-hit、周期格、external slab、complete-excess bundle 和同余类 D-only
  no-go 五条核心主张；
- 只对本轮新增或实质修改的证明做定向复核，不重跑已通过的历史测试；
- 不再扩大 483 状态菜单；
- 固化 bundle 的 lcm 容量合同和代表性 receipt。

### 第 2 周：overflow 与换载体分类

对 \(R_M>p\)、\(M=\operatorname{lcm}(A,Q)\) 的 bundle overflow 分别推导：

- determinant \(pn=4Md+1\) 的互补坐标；
- source/path/node 锚定的 alternate carrier 是否必存在；
- 素数幂 gap 三目标 miss 的 Fourier 分离角色；
- \(\beta\)-ratio cocycle 的稳定子闭包；
- 初始线性源的一般 \(\alpha=1,\ as\in\{2,3\}\) bundle，以及 clean 子类剩余的
  \(as=2,\ p\equiv169\pmod{240}\) 必要类；
- 一般 \(A>1\) bundle overflow 与初始 clean overflow 的边界差异。

输出必须是定理候选或明确反例，不是覆盖率表。

### 第 3 周：裸 G source 与非保尾接口

- 为 G 状态寻找不只使用 \(K\) 支撑的 source/path/node 形式源；
- 从 bundle overflow 构造改变一条或两条尾的 marked 状态；
- 每个候选必须同时给出标记集非空、全域提升和预定义势下降；
- 不再把同 \(1\pmod4\) 的 D-only 补秩放回 overflow 菜单。

### 第 4 周：两翻转周期三目标短代表

- 仅枚举核心可实现两翻转正规形；
- 检查周期子格三个目标陪集与单位盒；
- 提取最小 miss 的完整 Smith 数据；
- 若无 miss，尝试从交叉 radical 整除直接证明短代表。

### 第 5 周：统一状态机

把 terminal-first、Reach、周期格、complete-excess bundle 和 marked edge 写入同一
typed selector：

- 每个输出标明 `terminal`、`candidate_transition` 或 `verified_edge`；
- 只有 verified edge 承担递归；
- 明确每条边的势函数阶段，避免允许反向图表边形成二环。

### 第 6 周：外部审阅与论文级整理

- 邀请至少一名数论研究者审阅压缩后的核心证明链；
- 将周期结构、bundle overflow 和 G/marked source 拆成可独立阅读的章节；
- 只为新结论保留聚焦复现；已通过且未重大修改的历史代码不重复审计；
- 决定哪一个方向进入下一轮主攻，另外两条降为辅助接口。

---

## 十三、证据治理风险

原审计 HEAD 的主张账本快照共有 695 条主张，其中：

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
- absorbed support 使所有 \(R_{AQ}<p\) 的 clean slab 都成为良基边，不再要求降 \(R\)；
- sink 最小坐标把所有 competing excess 规范化为 composite complete-excess bundle；
- \(M=\operatorname{lcm}(A,Q)\) 把一般 bundle 压成 marked edge 或带
  \(pn=4Md+1\) 的 overflow；
- 同 \(1\pmod4\) 的 non-source D-only 标记纤维已全部证明为空。

项目已经从“证书搜索实验室”进入“少数结构引理决定成败”的阶段。

最值得主攻的不是再次扩大样本，而是：

\[
\boxed{
\text{overflow determinant 的换载体、终端或合法后继三分}
}
\]

和

\[
\boxed{
\text{裸 G 的实际 source 或非保尾 marked 状态构造}
}
\]

其中任意一条获得无样本上界的定理，都可以称为真正的近期突破。若两者能够连接，即
overflow 的 alternate carrier 同时为 G 状态提供实际 source，就可能把当前已经良基的
bundle 子程序接到统一递归分支。

完整猜想是否能很快解决，目前仍高度不确定；但在未来数周内取得一个可发表的无限分支定理、合法递降子族或周期全称子类闭合，是现实目标。研究资源应集中在这些严格定义的节点上，而不再分散到新的有限菜单和同类终端枚举中。

## 2026-08-04 高载体 overflow 的 p+4 互补分流补充

本轮把报告中“同图表支撑升级留下的高载体残差”接入统一选择器，得到一个明确的
量词分类。设 verified overflow 满足

\[
pn=4Md+1,
\qquad R_M=4M-n>p,
\qquad B_p=\frac{(p-1)^2}{4}.
\]

若 \(M>B_p\)，则 \(Md=(pn-1)/4>B_p\)。同时 \(n\equiv1\pmod4\)；若
\(n\le p-4\)，则 \(Md<B_p\)，而 \(n=p\) 时

\[
Md=\frac{p^2-1}{4}=B_p+\frac{p-1}{2}>B_p.
\]

故有无条件边界

\[
\boxed{M>B_p\Longrightarrow n=p\ \text{或}\ n\ge p+4.}
\]

这不是新的猜想证明，但把高载体余项压到 \(n=p\) 或 \(p+4\) 以上的互补区域。

进一步，若 \(p+4\) 含素因子 \(q\equiv3\pmod4\)，取

\[
m=q,
\qquad x=\frac{p+m}{4},
\qquad y=\frac{p(x+1)}m,
\qquad z=\frac{px(x+1)}m,
\]

则 \(m\mid p+4\)、\(m\mid x+1\)，并直接得到

\[
\frac1x+\frac1y+\frac1z=\frac4p.
\]

统一选择器新增分支
`overflow_high_carrier_p_plus_four_complement`，优先于其它 overflow 递降。冻结的
12 条来源回执中，1 条属于高载体且由 \(p+4=77=7\cdot11\) 直接终端化：

\[
(p,M,d,n)=(73,1518,28,2329),
\qquad (x,y,z)=(20,219,4380).
\]

若 \(p+4\) 没有 \(3\pmod4\) 素因子，分支明确保留为
`analysis_evidence`/factor-filter hard core，不生成递归边。合成算术边界

\[
(p,M,d,n)=(97,2449,1,101),
\qquad p+4=101
\]

验证了该负分支不会因当前冻结样本缺失而消失；\((97,2352,1,97)\) 同时展示了允许的
精确边界 \(n=p\)。这些行没有 raw Reach/source provenance，也不是猜想反例。该分流
只关闭高载体的 \(p+4\) 因子子族，不能替代一般 \(A>1\) bundle overflow 的
alternate/容量/良基后继定理。

主张卡：[高载体 overflow 的 p+4 互补分流](../claims/type-I-overflow-high-carrier-p-plus-four-complement.md)。
回执位于
`reproductions/type-i-representation-dual-capacity-selector-results.json`，验证命令：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

## 当前新增接口：中心化盒的对合瓶颈

单活跃 Type I 退出后，目标指数不再适合按单向幂段计费。新增
[中心化指数盒的 Kneser 对合瓶颈](../claims/type-I-symmetric-box-kneser-involution-bottleneck.md)：
若

\[
P=A_0\prod_i\{g_i^z:-e_i\le z\le e_i\},\qquad
T=\operatorname{Stab}(P),
\]

并令 \(o_i\) 为 \(g_iT\) 在 \(H/T\) 中的阶，则
\(\lambda_i=\min(2e_i,o_i-1)\) 满足

\[
|P|\ge |A_0T|+|T|\sum_i\lambda_i.
\]

目标缺失时，所有方向的总 \(\lambda\)-预算受
\(\lfloor(|H|-1-|A_0T|)/|T|\rfloor\) 控制；稳定子吸收、二阶商和非对合商分别收费
0、1、至少 2。对 Type I 中心化私有盒，这化为

\[
\sum_i\min(2b_i,o_i-1)\le |Q/T|-2.
\]

并且，若所有未被 \(T\) 吸收的方向在 \(Q/T\) 中都为二阶元，则中心化盒像就是
\(Q/T\) 本身；当 \(-1\in H\) 时该分支必命中，目标不在 \(H\) 时则已经是 G 型
支撑逃逸。因此 F 型未命中不能停留在“纯 dyadic”状态，必须含有阶至少 3 的
非对合方向。

这一步把多活跃缺口从一般 Kneser 容量细分为 dyadic/吸收两类结构，下一阶段不应再把
二阶方向与奇素数方向混合计费。仍未闭合的关键是：把真实 Fourier/Pareto 或 Type II
移位缺陷证明性地注入 \(\lambda_i\)，或者在二阶/吸收商中给出保持标记解集的严格下降。

## Type II q 高度的单状态精确注入

新增[Type II 单状态 q 进高度到 Kneser 幂块的精确桥](../claims/type-II-qadic-height-kneser-block-bridge.md)。
在 \(N=p+4A^2C\) 中若 \(q^e\mid N\)，其因子幂块
\(B_q=\{1,q,\ldots,q^e\}\) 在最终稳定子商中的活跃容量不是未知量，而是

\[
\kappa_q=\min\{e,\operatorname{ord}_{H/T}(qT)-1\}.
\]

故 q 高度分成两个精确分支：低于商阶时逐层支付 Kneser 容量，达到商阶后多余高度
转化为 \(q^{o_q}\in T\) 的有限阶关系。结合移位差容量后，跨状态 relay 只可使用
完全支付部分；折叠部分必须进入商群或二幂分支，不能继续按原始高度重复计费。

这一步尚未识别不同移位的 \(H_s/T_s\)，也没有把有限阶关系自动提升为更小核心素数。
下一阶段的决定性问题是建立共同商群中的载体同态，或证明折叠关系导致严格可提升下降。

## 同模数跨状态池化的负边界

已构造[Type II 同模数跨状态积集池化的严格反例](../claims/type-II-cross-state-same-modulus-pooling-counterexample.md)：
\(p=97,M=24\) 的 \(s=6\) 与 \(s=18\) 两条射线分别只有
\(\{1,11\}\) 和 \(\{1,13\}\) 两个除子残数，均遗漏 \(23=-1\pmod{24}\)，但
\(11\cdot13=23\pmod{24}\)。

这排除了“同一模数的不同状态可以直接合并 Kneser 积集”的捷径。跨状态容量若要成立，
必须证明混合因子具有共同整数来源、可逆 source-switch/alternate，或有标记解集提升；
否则混合命中只是伪证书。当前研究重点因此从“识别共同商群”改为“证明共同载体同态
且保持单状态因子来源”。

同一反例还给出可正向使用的带来源 CRT 判据：固定 \(M=4D\)、\(N_a=p+aM\)，若
来源块 \(h_i\mid N_{a_i}\) 两两互素，则
\[
h=\prod_i h_i\mid N_a
\iff
a\equiv a_i\pmod{h_i}\quad\forall i.
\]
若同时 \(h\equiv-1\pmod M\)，且 CRT 解满足 \(a\mid D\)、\(D/a\) 平方自由，
则可构造 Type II 因子生成器。这个判据把“跨状态容量”改造成真正的
source-switch 选择器；缺少 admissible CRT 解时，混合残数只能算伪命中。
详见[Type II 同模数 source-switch 的带来源 CRT 判据](../claims/type-II-same-modulus-source-switch-crt-criterion.md)。

该判据现在还给出一个有限的除子格分支。对混合因子
\(h\mid p+4Da_0\)，定义
\[
\mathscr C_D(h,a_0;p)=
\{(D',A):D'\mid D,\ A\mid D',\ D'/A\ {\rm squarefree},\
4AD'<p,\ AD'\equiv Da_0\pmod h\}.
\]
它非空当且仅当 \(h\) 能沿 \(M'=4D'\) 产生一个 Type II source-switch 候选；
为空是该分支的有限负证书。若 \(h>D^2\)，候选至多一个，最小剩余
\(r=Da_0\bmod h\) 直接决定是否存在 \(r=A^2c\)、\(Ac\mid D\) 的候选。

这一区分已经有正、负两个边界：\(p=5113,D=6\) 的来源块
\(17\mid N_3\)、\(7\mid N_6\) 合成 \(h=119\)，可严格降到 \(M'=4\) 并得到
\(m=43,d=1\)；而 \(p=97,D=6,h=143\) 的 CRT 剩余为 \(r=83>D^2\)，
\(h\) 的同模数和除子格 source-switch 均被排除。该分支仍不保证全局下降，空候选时
必须转入容量/字符障碍或另一条带标记提升的递降边。

空候选还可转成加法群 \(\mathbb Z/h\mathbb Z\) 上的有限 Fourier 对偶。令
\(\mathcal X_D=\{AD'\bmod h:(D',A)\in\mathscr L_D(p)\}\)、
\(r=Da_0\bmod h\)，则 \(r\notin\mathcal X_D\) 时
\[
\widehat g(t)=
\sum_{x\in\mathcal X_D}e^{2\pi i tx/h}-e^{2\pi i tr/h}
\]
满足
\(\sum_t|\widehat g(t)|^2=h(|\mathcal X_D|+1)\)，故有一个频率的模至少为
\(\sqrt{|\mathcal X_D|+1}\)。这是 source-switch 的严格残数分离证书，不是乘法
单位群角色；只有建立带来源同态后，才能把它注入 Kneser/Fourier 容量。

同态桥受到一个硬的阶障碍：若
\(\Phi:\mathbb Z/h\mathbb Z\to U(M')\) 和乘法角色保留频率
\(e^{2\pi i tx/h}\)，则 \(h/\gcd(h,t)\mid\lambda(M')\)。当
\(\gcd(h,\lambda(M'))=1\) 时所有提升都是平凡的。\(p=97,M=24,h=143\) 的
\(\lambda(24)=2\)，因此该负例的加法 Fourier 证书不能直接变成 \(U(24)\) 的非平凡
角色。下一阶段若要继续容量路线，必须寻找共享阶的因子商/标记同态；否则应把这类
空候选状态送入严格下降分支。阶条件对无标签单频率是充分的群论筛选，但对带来源
标签仍只是必要条件，关系格判据才决定能否真正提升。

有来源标签时，精确门槛是关系格相容性。若加法标签为 \(x_i\)、目标单位为
\(u_i\)，则必须同时有
\[
\prod_i u_i^{n_i}=1\quad
(\sum_i n_i x_i=0\pmod h),\qquad
\sum_i n_i t x_i=0\pmod h\quad
(\prod_i u_i^{n_i}=1).
\]
这两个关系格可由 Smith 正规形有限计算；任一失败都标记为 LIFT_OBSTRUCTED，
不能继续把该频率计入容量。\(p=97,M=24,h=143\) 例因
\(\lambda(24)=2\) 与 \(h\) 互素，直接落在该不可提升分支。

还有一个更强的结构边界：\(h\equiv-1\pmod{4D'}\) 使 \(h\) 为奇数，
\(\mathbb Z/h\mathbb Z\) 的同态像必为奇阶，不能包含目标二阶元 \(-1\)。
因此 CRT 参数 Fourier 不能直接充当 Type II 的目标角色。正确载体应改为源块计数格
\(\rho:\mathbb Z^r\to U(4D')\)、\(\rho(e_i)=h_i\)，并与 admissible 参数纤维
\[
\mathcal F(\mathbf n)=
\{(D'',A)\in\mathscr L_D(p):
AD''\equiv Da_0\pmod{h_i}\text{ 对所有 }n_i=1\}
\]
做拉回。只有 \(\rho(\mathbf1)=-1\) 且 \(\mathcal F(\mathbf1)\ne\varnothing\) 时，
乘法目标命中才可回译为 Type II 证书；\(p=97\) 的 \(11\cdot13=-1\pmod{24}\)
正是 \(\mathcal F(\mathbf1)=\varnothing\) 的伪命中。后续容量必须先保留源块计数，
再施加参数纤维。

这一步已整理为[Type II 源块计数格与参数纤维的 Kneser 选择器](../claims/type-II-source-lattice-fibered-kneser-selector.md)。
固定候选 \(D_*\mid D\) 与参数 \(A\) 后，只允许兼容集合
\[
I_{D_*}(A)=\{i:AD_*\equiv Da_i\pmod{h_i}\}
\]
进入积集 \(P_A=\prod_{i\in I_{D_*}(A)}\{1,h_i\bmod4D_*\}\)。这是精确的
“纤维先过滤、容量后计算”顺序：\(-1\in P_A\) 当且仅当该纤维产生 Type II
source-switch。若 \(T_A=\operatorname{Stab}(P_A)\)，则
\[
|P_A|\ge |T_A|(1+\sum_i\kappa_{A,i}),\qquad
\sum_i\kappa_{A,i}\le|G_*/T_A|-2
\]
在目标缺失时逐纤维成立；达到 \(|G_*/T_A|-1\) 则直接命中。不同 \(A\) 的稳定子和
参数纤维不能相加。\(p=97\) 的 pooled pseudo-hit 被三个单独纤维全部排除，
而 \(p=5113\) 的 \(D_*=1\) 纤维给出真实 \(M=24\to4\) 降模证书。

在互异源素数模型中，q 进 relay 也已变成精确恒等式。若
\(q_i^{e_i}\mid p+4Da_i\)，定义
\[
d_i(A)=\max\{d\le e_i:q_i^d\mid AD_*-Da_i\}.
\]
则 \(q_i^{d_i(A)}\mid p+4AD_*\)，并在同一纤维中使用
\(B_{i,A}=\{1,q_i,\ldots,q_i^{d_i(A)}\}\)。其 Kneser 活跃容量
\[
\kappa_{i,A}=\min(d_i(A),\operatorname{ord}_{G_*/T_A}(q_iT_A)-1)
\]
是逐层精确的；目标缺失强制
\(\sum_i\kappa_{i,A}\le|G_*/T_A|-2\)。因此这里不再假设整数 q 高度能注入
容量，注入由同余恒等式直接证明。相同 q 的多来源仍需先合并共同高度，详见
[Type II 源参数纤维的 q 进高度—Kneser 幂块精确桥](../claims/type-II-source-fiber-qheight-kneser-bridge.md)。

重复 q 的合并也已形式化：对来源 \(b_i=Da_i\) 定义
\[
\ell_i(s)=\min(e_i,v_q(s-b_i)),\qquad
d_q(s)=\min\left(v_q(p+4s),\sum_i\ell_i(s)\right).
\]
在保留逐层来源标签时，候选纤维可用的 q 幂恰为 \(q^{d_q(s)}\)，对应 Kneser
幂块只出现一次。\(p=241,D=6,q=5\) 的两个来源都含一个 5，但候选
\(p+24=265\) 的实际高度只有 1，严格排除把 \(5^2\) 当成两个独立容量单位。
见[Type II 源参数纤维的重复 q 共同账本](../claims/type-II-source-fiber-shared-q-ledger.md)。

稳定子约化现在也接上了低模数递降：若
\(K=\ker[U(4D_*)\to U(4D')]\subseteq\operatorname{Stab}(P)\)，则
\(P\) 是商积集的完整原像，原群与商群的 \(-1\) 命中完全等价；双重缺失时商群阶
下降。若核不包含稳定子，才可能出现只在低模数商命中的伪分支，此时必须检查
低模数参数纤维。\(p=97\) 的 \(P=\{1,11\}\subset U(24)\) 虽在模 \(4\) 投影中
命中，但同余核不包含稳定子，正是这种伪分支。完整三分见
[Type II 稳定子包含同余核时的低模数商—递降三分](../claims/type-II-stabilizer-kernel-quotient-descent-trichotomy.md)。

核不饱和的伪分支现在也有规范对偶出口。对目标陪集截面
\(S_t=\{k\in K:tk\in P\}\)，若 \(0<|S_t|<|K|\)，则
\[
\sum_{\chi\ne1}\left|\sum_{k\in S_t}\overline{\chi(k)}\right|^2
=|S_t|(|K|-|S_t|),
\]
从而存在非平凡核字符。若 \(K\) 是 2-群，该字符阶为 \(2^j\)，直接进入广义
二幂对偶分支；否则保留为一般有限 Fourier 证书。\(p=97\) 的
\(S_{-1}=\{13\}\subset\{1,5,13,17\}\) 给出显式系数 \(-1\)。见
[Type II 同余核分裂的有限 Fourier 证书](../claims/type-II-congruence-kernel-split-fourier-certificate.md)。

## 2026-08-04 Type II 二幂深度回执与高阶字符分支

规范扇的支撑外失败现在不再只记录“二次可分/不可分”。对
\(M=4AC\) 和支撑子群 \(K\)，选择器精确计算

\[
\nu=\max\{d\ge0:-1\in K\,U(M)^{2^d}\}.
\]

回执同时保存
\(K\,U(M)^{2^\nu}\) 中的有限群见证和下一层
\(-1\notin K\,U(M)^{2^{\nu+1}}\) 的集合排除。由二幂字符深度引理，所需字符像阶为
\(2^{\nu+1}\)：\(\nu=0\) 是二次分离，\(\nu\ge1\) 进入高阶字符分支。

三条精确 raw-\((A,C)\) 边界为：

| \(p\) | \(A\) | \(C\) | \(\nu\) | 最小字符像阶 |
| ---: | ---: | ---: | ---: | ---: |
| 97 | 4 | 1 | 1 | 4 |
| 3457 | 4 | 4 | 2 | 8 |
| 14593 | 4 | 4 | 3 | 16 |

这一步证明平方饱和核确实有非二次层，不再允许把所有支撑外失败统一标为二次
分离；有限回执已经构造生成元级高阶字符证书，但跨状态角色坐标、
容量注入、目标纤维提升和 E1--E5 仍未建立。选择器继续保持
analysis_evidence 与 recursive_edge_eligible=false。

三条高阶角色拉回共同模数
\(\operatorname{lcm}(24,16,64,64)=192\) 后，核心残余类联合核仍有代表
\(1\pmod {192}\)，联合核指数为 \(8\)。因此这组字符条件是有限兼容而非容量矛盾；
后续必须把移位数的逐素因子分布或真实载体相位加入容量映射。

为验证逐素因子接口，\(p=433\) 的两条深度一射线
\((A,C)=(4,1),(5,4)\) 共享素因子 \(7\)，对应
\(v_7(497)=1\)、\(v_7(833)=2\)，高度差为 \(1\)，私有余因子为
\(71,17\)。两条角色在 \(7\) 上的相位均为零，联合模 \(240\) 的核心核仍有
4 个残余类。因此目前得到的是 local valuation ledger，而不是 q 进容量边；
回执还核验了逐素因子差值界
\(\min(v_7(497),v_7(833))=1\le v_7(4(100-16))=1\)，这是一个达到等号的
局部容量上界。下一步仍要证明私有避靶条件如何支付该高度差，或把它转成可下降载体；
局部上界本身不等于跨状态容量边。
该逐对约束已登记为
[Type II 共享素因子幂的移位差 q 进上界](../claims/type-II-shared-factor-q-adic-difference-bound.md)，
后续可直接作为跨移位状态转移的局部预算接口。回执还按 \(q^e\) 层保存活动移位同余
类，形成 exact_local_collision_tree；这仍不是容量注入。

本轮把它提升为有限移位集容量不等式：若
\(C_r(S,q)=\max_{a\bmod q^r}\#\{s\in S:s\equiv a\pmod{q^r}\}\)，则
\[
\sum_{s\in S}\min(v_q(p+4s),E)\le\sum_{r=1}^{E}C_r(S,q).
\]
对 \(p=433,S=\{16,100\},q=7,E=2\)，左、右两侧都为 \(3\)，形成一个紧的跨状态
q 进容量证书。它仍未控制目标残数 \(-1\pmod{4AC}\)，所以全局选择器仍需证明严格
容量缺口，或把等号分支转为 Type II 命中/严格递降。

容量引理还给出刚性二分：等号当且仅当每一层的目标残类都是最大移位残类；
否则至少支付一个单位的 q 进缺口。该二分已写入
[Type II 共享素因子幂的移位差 q 进上界](../claims/type-II-shared-factor-q-adic-difference-bound.md)，
下一步可分别处理“最大残类链”与“严格缺口”两种状态。
该容量还可按 relay 来源标签计数：对 \(p=433,q=7\)，双来源同时携带 \(7^2\)
需要 4 个单位而容量仅 3，因而被严格排除；实际 \(7^1,7^2\) 标签恰好饱和。
但等号链并非障碍：同一 \(p=433\) 在 \(s=1\) 有
\(437=19\cdot23\)、\(19\equiv-1\pmod4\)，取 \((A,C,K)=(1,1,5)\) 即得
Type II 短证书。等号分支必须转入目标纤维，而不能停在 q 进核。

本轮又得到一个有限目标纤维终端：对碰撞/私有分解
\(x=ER\)，Kneser 分别作用于 \(C\Pi(R)^2\)、\(D^+\Pi(R)\) 和
\(D\Pi(R)^+\)。任一乘积的下界达到 \(|H|\) 即构造相应 Type II/共享命中；
否则联合失败显式支付三个稳定子容量缺口。\(p=33011449,m=63\) 的联合失败行给出
缺口 \(6,12,20\)，见
[Type II 共享选择器的 Kneser 目标纤维容量终端](../claims/type-II-shared-selector-kneser-target-fiber-terminal.md)。

私有因子现在也有了逐因子接口：把私有残数按 \(g\) 加入目标积集时，若
\(g\notin\operatorname{Stab}(P)\)，Kneser 给出至少一个稳定子块的增长；若
\(g\in\operatorname{Stab}(P)\)，则该方向被吸收并投影到更小的商群。因而后续证明只需在
“积集增长达到全群”与“稳定子商严格缩小”两条分支中继续闭合，而不再把私有残数当作
未区分的容量项。具体桥接见
[Type II 私有因子的 Kneser 增长—稳定子吸收二分](../claims/type-II-private-factor-kneser-growth-stabilizer-bridge.md)。

进一步把逐因子接口合并为多块预算：对
\(P=A_0\prod_i B_i\)、\(T=\operatorname{Stab}(P)\)，定义
\(\kappa_i=|B_iT/T|-1\)，则
\[
|P|\ge |A_0T|+|T|\sum_i\kappa_i.
\]
目标缺失时，活跃容量总和不超过
\(\lfloor(|H|-1-|A_0T|)/|T|\rfloor\)；所有
\(g_i\in T\) 的私有块在 \(H/T\) 中消失。对
\(p=33011449,j=16\)，两个私有块均有 \(\kappa_i=0\)，商群缺口完全来自固定碰撞层。
这给出了 q 进 relay 需求的定量入口，但只有在证明真实坐标到
\(\kappa_i\) 的注入后，超载才可升级为命中。见
[Type II 多私有块的活跃容量—稳定子二分](../claims/type-II-multiblock-kneser-active-capacity-dichotomy.md)。

Type I 单活跃循环商也已封闭为同样的出口三分：实际载荷总和若不超过
\[
\frac{M_tM_R}{q^2-1}+\frac{M_t+M_R}{q-1}+H_q,
\]
则状态仍可保持单活跃 F；若超载，至少一个状态要么有限盒命中，要么转为 G，
要么退出单活跃循环商而进入多活跃/固定层目标纤维。该结论把单活跃分支从
“容量输入”提升为真正的选择器出口，但第三分支仍未给出算术递降。见
[单活跃 Fourier—载体容量的跨状态退出三分](../claims/type-I-single-active-cross-state-exit-trichotomy.md)。

下一步应把这些高阶角色的层数与相邻移位的共同素因子/相位条件结合，尝试构造跨状态
\(q\)-进容量或良基下降映射；单独叠加字符核仍可能被同一条
\(p\equiv1\) 算术级数同时满足，不能直接产生矛盾。

## 2026-08-04 Type II 规范扇的支撑--目标纤维三分

统一选择器现在接入规范 Type II 扇的逐点三分。若
`4H < p` 且 `4*product(primes <= H) > p-1`，前 `H` 条规范射线不能全部是
一孔支撑临界失败：要么已有直接 Type II 命中，要么某条失败射线满足
`-1 not in K_s` 并产生二次角色分离子，要么 `-1 in K_s` 但目标纤维缺陷
`K_s minus Pi_s` 至少有两个元素。

七个聚焦核心素数的精确回放中，`H` 取 5、7、11 或 13；所有样本的非临界射线数均为
`H`。其中 `p=193` 的前 7 条射线全部没有直接命中，但 6 条是支撑外二次分离、1 条是
支撑内多孔失败。这把 Type II 失败明确接入表示--对偶--容量选择器：二次可分的支撑外行进入
角色/对偶接口，二次不可分的支撑外行保留为平方饱和核，支撑内多孔行进入目标纤维缺陷接口；两者仍保持
`analysis_evidence`，不自动产生解提升或递归边。
边界回放 `(p,s)=(97,16)` 确认二次不可分支撑外类确实出现，因此后续容量桥必须处理平方
饱和核，不能只统计二次角色数量。

主张卡：[规范 Type II 扇不能长期全为一孔临界失败](../claims/type-II-canonical-critical-fan-escape-trichotomy.md)。
结果：[Type II 扇逃逸三分结果](../reproductions/type-ii-canonical-fan-escape-trichotomy-results.json)。

## 2026-08-04 高载体 n=p 的精确正规形补充

高载体边界中的 n=p 分支还可以完全算术化。由

    M*d=(p^2-1)/4

以及 (p^2-1)/4 < 2*((p-1)^2/4)，结合 M>B_p，得到 d=1、M=(p^2-1)/4。
令 r=(p-1)/4，则对偶图表唯一固定为

    (R_r,K_r)=(p-2,(p-1)^2/4).

其 anchor 剩余块满足

    p-3=2*Q,    Q=(p-3)/2,    beta=2,    gcd(Q,K_r)=1.

因此 n=p 不再需要作为一个未分类的高载体参数族处理，而是被压到 G-anchor 的
规范 Q 分流。通用 p-source 的 shift=1 直接到达 (1,p-3,1)，但该 source 仍不提供
旧 charged support 的保持，也不自动支付 E5；选择器状态保持 analysis_evidence。

新增字段 n_prime_normal_form 已接入统一回执。算术边界

    (p,M,d,n)=(97,2352,1,97),

验证了 n=p 的合法高载体形态；它没有 raw Reach/source provenance，也不是猜想反例。
当前 12 条来源行的高载体样本属于 n>=p+4，因此 exact_n_prime_count=0；这不是
该分支不存在，而是冻结样本没有覆盖 n=p 行。

主张卡：[高载体 n=p overflow 的唯一 d=1 G-anchor 正规形](../claims/type-I-overflow-high-carrier-n-prime-normal-form.md)。

## 2026-08-04 高载体 n=p G-anchor bundle 的精确相位二分

exact \(n=p\) 的 G-anchor 还可以继续压缩。令

\[
B_p=\frac{(p-1)^2}{4},\qquad
Q=\frac{p-3}{2},\qquad
c=\frac{p-1}{6}.
\]

若当前 G 图表携带 proper support \(A\mid B_p\)、\(B_p/A\ge2\)，则
\(\gcd(A,Q)=1\)。令 \(t_A\) 是 \(0\le t_A<A\) 中满足

\[
c+pt_A\equiv0\pmod A
\]

的唯一相位。对 G-anchor bundle \(M=AQ\)，规范图表可直接写成

\[
R_M=R_Q+4Qt_A,\qquad
R_Q=\frac{p-4}{3},\qquad
K_M=Q(c+pt_A).
\]

因 \(p\equiv1\pmod{24}\) 且 \(p\ge73\)，得到精确二分：

\[
\boxed{
R_M<p
\iff
t_A=0
\iff
A\mid\frac{p-1}{6};
}
\]

若 \(A\mid(p-1)/6\)，则 \(M\le B_p\)，该行具备
conditional_bundle_marked_absorb 的算术形状；否则
\(R_M\ge R_Q+4Q>p\)，进入 bundle overflow；但若 \(AQ\le B_p\)，已有同图表支撑
升级在来源回执携带 \(A\) 的前提下可以支付一个继续为 overflow 的支撑递降，只有
\(AQ>B_p\) 才是真正的高载体残差。两种回执都没有自动携带 raw
source provenance、标记集提升或 E1--E5，因此统一选择器保持
analysis_evidence，不把公式误报为递归边。

选择器以没有来源路径的合成 profile 重算：
\(p=73\) 的 9 个 supports 中 6 个低相位、2 个同图表 overflow、1 个高载体；
\(p=97\) 的 9 个 supports 中 5 个低相位、3 个同图表 overflow、1 个高载体。该结果把 exact \(n=p\)
从未分类的 G-anchor 参数族压成确定相位选择器，但全称缺口仍是：来源可达的低相位是否
能补齐完整 E1--E5，非整除相位是否必有 alternate、直接证书或跨状态良基秩。

此外，现有真实 G_marked_absorb 回执连接了一个 exact \(n=p\) 行：
\((p,M,d,n)=(73,1332,1,73)\) 的原始高载体经过对偶重图表成为
\((R,K)=(71,1296)\)，其 \(A=1,Q=35\) anchor 处于低相位并带 raw source/anchor
provenance。这里的 \(M=1332\) 是原始载体，而 \(K=1296=B_{73}\) 是对偶 G 图表容量；
回执尚未补齐完整 E1--E5，故仍只作 analysis_evidence。

对真正的高载体 \(AQ>B_p\)，令 \(C=B_p/A\)。若 \(C<Q\) 且 \(3\mid C\)，相位公式
进一步给出共同的
\[
n_*=\frac{p^2-5p+7}{3},\qquad d=\frac{2C}{3},\qquad Md=\frac{2B_pQ}{3}.
\]
固定-\(n_*\) 选择 \(L=B_p/3\)（\(C>3\)）或 \(L=2B_p/3\)（\(C=3\)），逐行满足
严格支撑势下降；\(C>3\) 回到 G 图表，\(C=3\) 仍是 overflow。该结论在来源标记
和可达性成立时给出条件性 E1--E5 边，当前合成回执仍保持 analysis_evidence。

更一般地，所有 \(C<Q\) 的真高载体都可按 \(k=C\bmod3\) 写成
\[
u=A-t_A=c+\frac{kA}{3},\qquad
d_C=\frac{2C+kp}{3},\qquad
n_C=4Qu-\frac{p-4}{3},\qquad
pn_C=4(AQ)d_C+1.
\]
因此 \(C\equiv1,2\pmod3\) 的剩余部分也不再是模逆黑箱，而是明确的
fixed-\(n_C\) determinant；当前缺口转为是否存在满足 \(L\mid AQd_C\)、\(4L>n_C\)
且支付外层势的有界除子，或是否需要对偶容量/alternate。
任何 \(B_p\)-bounded fixed-\(n_C\) 后继还必须满足
\[
n_C<4B_p
\iff
C(2p^2-p-4)>4kB_pQ.
\]
这提供了一个先验空窗口筛选器：不满足该不等式的 \(C\equiv1,2\) 行无需继续枚举
有界 fixed-\(n\) 除子，应直接进入 fixed-\(s\)、alternate 或 q 进容量分支。
特别地，\(k=2\) 时阈值 \(D_2=8B_pQ/(2p^2-p-4)\) 满足
\(Q-1<D_2<Q\)，所以所有整数 \(C<Q\) 都落在空窗口一侧。由此
\[
C\equiv2\pmod3
\Longrightarrow
\text{无 }B_p\text{-bounded fixed-}n_C\text{ 后继窗口}.
\]
当前 exact \(n=p\) fixed-\(n\) 余项因此只剩 \(C\equiv1\pmod3\) 的可能窗口，以及
\(C\equiv0\) 已完成的条件性重置子族。

主张卡：[高载体 n=p G-anchor bundle 的精确相位二分](../claims/type-I-overflow-high-carrier-n-prime-g-anchor-phase.md)。

## 2026-08-04 高载体 n=p 中 C=1 mod 3 的 fixed-s 图谱

前面的闭式把真正高载体的 exact \(n=p\) 余项分成 \(C\equiv0,1,2\pmod3\)。其中
\(C\equiv2\pmod3\) 已排除 \(B_p\)-bounded fixed-\(n\) 窗口，\(3\mid C\) 有条件性
fixed-\(n\) 支撑重置；本轮对剩余的 \(C\equiv1\pmod3\) 建立了一个精确 fixed-\(s\)
除子图谱。

令 \(A=B_p/C\)、\(M=AQ\)，并令 \(r=M\bmod p\)。闭式中的
\(d=(2C+p)/3\) 给出

\[
T=rd,\qquad s=\frac{4T+1}{p},\qquad ps=4T+1.
\]

枚举 \(L\mid T\)，保留

\[
A<L\le B_p,\qquad 4L>s,\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor<C.
\]

每个保留除子都生成

\[
(R_L,K_L)=\left(4L-s,\;L\left(p-\frac{T}{L}\right)\right),
\]

并严格降低外层支撑势。选择器对六个合成行得到：

| \(p,C\) | \(A\) | \(T\) | 候选数 | 路由 |
| --- | ---: | ---: | ---: | --- |
| \((193,64)\) | 144 | 18190 | 7 | fixed-s 条件边候选 |
| \((241,64)\) | 225 | 2952 | 8 | fixed-s 条件边候选 |
| \((241,100)\) | 144 | 3675 | 7 | fixed-s 条件边候选 |
| \((5281,1408)\) | 4950 | 8466763 | 0 | 有界 Type II 终端；AC-ray 亦命中 |
| \((15601,4000)\) | 15210 | 65980529 | 0 | 有界 Type II 终端；AC-ray 亦命中 |
| \((16633,4312)\) | 16038 | 77530571 | 0 | 有界 Type II 终端；AC-ray 亦命中 |

这组数据把剩余分支从“是否有固定 \(s\) 除子”转成了可检验的 \(T=rd\) 素因子与
目标余数结构问题。前三行仍只属于 `analysis_evidence`：完整标记集、来源可达性和
恒等提升没有从合成参数自动推出。后三行虽然没有 fixed-s 除子，但都同时命中有界
Type II 探针与 \(A,C\le2\)、\(K\) 不设上限的 Type II AC 射线探针；选择器的
`hard_core_route` 当前优先前者，后者提供独立终端交叉核验。其中 \(p=15601\) 还同时有
\(x=(15601+3)/4=3901=83\cdot47\) 的 gap-3 证书。因此 fixed-s hard core 应先经过
有界 Type II 后置路由；两类终端探针均失败时，才进入 alternate、对偶容量或跨状态
良基势分析。

主张卡：[高载体 n=p 中 C=1 mod 3 的 fixed-s 除子图谱](../claims/type-I-overflow-high-carrier-n-prime-c-one-fixed-s-atlas.md)。

独立引理见：[A=1 gap=3 的因子型 Type II 终端](../claims/type-II-a-one-gap-three-factor-terminal.md)。

复现：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

## 2026-08-04 核 Fourier 的源关系格提升门

本轮把未吸收同余核分支再推进一层。对源指数盒

\[
\phi(z)=\prod_i u_i^{z_i},\qquad
L_\pi=\{n:\pi(\phi(n))=1\},\qquad
L_G=\{n:\phi(n)=1\},
\]

先按真实乘法碰撞商掉指数盒，再取目标陪集的相对支撑
\(Q_t\subset L_\pi/L_G\) 和锚点
\(\alpha=t^{-1}\phi(z_0)\)。核 Fourier 系数现在有精确仿射分解

\[
\widehat{1_{S_t}}(\chi)
=\overline{\chi(\alpha)}
  \sum_{\bar n\in Q_t}\overline{\chi(\phi(n))}.
\]

若外部频率给出相对相位 \(\theta\) 与锚点相位 \(a\)，则它能进入真实单位群的核角色
当且仅当

\[
\theta|_{L_G}=1,
\qquad
\theta(n)a^m=1
\quad\text{whenever }\phi(n)\alpha^m=1.
\]

这是一个有限 Smith 正规形可检验的相容性判据；任一失败都标记
`LIFT_OBSTRUCTED`，不再把 CRT 加法 Fourier 频率误计入 Type II 容量。\(p=97\)
的 \(P=\{1,11\}\subset U(24)\) 给出相容核角色；同一素数的 CRT 伪池化标签
\((1,3)\) 与单位 \((11,13)\) 在关系 \((3,-1)\) 上失败，给出不相容回执。

主张卡见[Type II 核 Fourier 与源关系格的仿射相容性判据](../claims/type-II-kernel-fourier-source-relation-compatibility.md)。
这一结果关闭了“对偶频率是否真正来自源块”的接口，但没有关闭最后的算术桥：相容
角色仍需被证明能够支付 q 进容量、命中 \(-1\)，或携带标记集严格下降。

## 2026-08-04 核 Fourier 对偶能量的关系边需求

在源关系格相容性门之后，本轮又把相容角色的谱幅度转成了一个精确的关系边数量。
对去重源支撑 \(Q_t\) 令
\[
N=|Q_t|,\qquad
\rho_\chi=\frac{|\widehat{1_{S_t}}(\chi)|}{N}.
\]
则
\[
\sum_{\bar n,\bar n'\in Q_t}
\left|1-\chi(\phi(n-n'))\right|^2
=2N^2(1-\rho_\chi^2),
\]
从而至少有 \(N^2(1-\rho_\chi^2)/2\) 条有序非平凡相位边。对这些边接入
互异 q 或重复 q 共同账本，可以定义最小源成本和总关系需求；但只有进一步证明
每个真实 q 层的边复用上界，才可把需求升级为 Kneser 容量矛盾。\(p=97\) 的单点
伪命中有 \(\rho=1\)，关系边需求为零，明确排除了“核角色非平凡所以 q 进超载”的
误读。

主张卡见[Type II 核 Fourier 对偶能量到源关系边的 q 进需求](../claims/type-II-kernel-fourier-pair-energy-qheight-demand.md)。
因此最后的算术子问题已经收缩为：证明 source-fiber 关系边的有限复用上界，或从
一条非平凡关系边直接构造 Type II 证书/严格递降。

同时发现，成对能量不能直接等同于独立容量：在
\(H=C_2\times C_m\)、\(\chi(\varepsilon,j)=(-1)^\varepsilon\)、\(Q_t=H\) 时，
\(\mathcal E_\chi=2|Q_t|^2\)，但有效相位商只有一个 \(C_2\) 方向。\(U(15)\)
按模 \(3\) 的二值角色给出具体实例。因而下一阶段若继续容量路线，必须证明边复用
上界，或同时积累多个独立角色并按商群秩收费；单角色的二次 pair-energy 不能直接
推出全局 q 进超载。

为修正这一点，现对差分群
\(\Delta_t=\langle Q_t-Q_t\rangle\) 记录每个 \(\ell\)-初等商秩
\[
r_\ell(Q_t)=\dim_{\mathbb F_\ell}(\Delta_t/\ell\Delta_t).
\]
该秩等于可获得的独立 \(\ell\)-角色方向数。若 q-height 账本能证明一个
\(\ell\)-primary 层至多提供一个独立方向，则有 q 层数至少为 \(r_\ell(Q_t)\)；
这比按 pair-energy 边数收费更稳健。真正缺口转为“q 层到初等商秩的注入”，以及
差分秩为 0/1 时的低秩残余处理。

## 2026-08-05 固定纤维的 q-height—初等商秩列注入

本轮将“q 层到差分群秩的注入”在固定参数纤维内严格完成。对源盒
\(\phi(z)=\prod_i u_i^{z_i}\)、稳定子商 \(\overline G=G/T\) 和定义目标纤维的商映射
\(\pi_0\)，令目标关系核 \(L_{\pi,J}\) 中的源组合像为
\[
\Delta_Q=\langle\phi(z-z')T:z,z'\in Q\rangle,
\qquad
A_{\pi,J}=\{\phi(n)T:n\in L_{\pi,J}\}.
\]
则对每个素数 \(\ell\) 有
\[
\dim_{\mathbb F_\ell}(\Delta_Q/\ell\Delta_Q)
\le
\dim_{\mathbb F_\ell}(A_{\pi,J}/\ell A_{\pi,J}).
\]
因此目标要求的独立 \(\ell\)-角色方向数不超过保持当前目标纤维的源列组合初等商秩。
重复 q 来源和相同商群残数列自动合并；单个改变参数纤维的源列不能直接收费。

这是一个真正的固定纤维 rank-capacity 映射，已排除两类重复收费：同一 q 的多来源
不能提供多个列，稳定子吸收的 q 块不能提供任何列。主张卡见
[Type II 源纤维 q-height 到差分群初等商秩的列注入](../claims/type-II-source-fiber-elementary-rank-qheight-injection.md)。
全局缺口仍在于：跨 \(A,D_*\) 纤维如何强制秩超载，或在秩 \(0/1\) 饱和时构造
Type II 证书/严格递降。

## 2026-08-05 低秩锁定与素数阶循环终端

进一步对固定纤维的差分群 \(\Delta_Q\) 做了低秩分解：

* 所有 \(\ell\)-初等商秩为零，当且仅当所有盒内目标关系都被稳定子吸收；
* 若每个初等商秩至多一，则 \(\Delta_Q\) 为循环群，目标测试化为有限循环指数集；
* 若 \(\Delta_Q\simeq C_\ell\) 且锚点位于该群内，至少 \(\ell-1\) 个合法、保持参数
  纤维的非零关系块由 Cauchy--Davenport 覆盖整个循环群，给出 Type II 命中；
* 目标锚点位于差分群外时，即使相对关系完全覆盖，也只能得到
  ANCHOR_OUTSIDE_DIFFERENCE 负证书。

这一步把秩零/素数阶秩一残余从一般容量问题中剥离出来。尚未闭合的是高阶循环孔、
关系块无法独立保持参数纤维，以及秩一锚点外分支的严格算术递降。主张卡见
[Type II 源纤维低秩锁定与素数阶循环终端](../claims/type-II-source-fiber-low-rank-lock-cyclic-terminal.md)。

## 2026-08-05 高阶循环的 \(\ell\)-primary 进位层终端

对固定参数纤维中的循环差分群 \(C_{\ell^a}\)，将每个合法二点关系块按精确
\(\ell\)-进赋值层 \(k=0,\ldots,a-1\) 分类。若每层至少有 \(\ell-1\) 个可独立
选择的块，逐层 Cauchy--Davenport 归纳给出
\[
\sum_j\{0,v_j\}=C_{\ell^a}.
\]
因此锚点在差分群内时直接构造 Type II 命中；若仍缺失，则要么锚点在群外，要么
存在明确的进位层缺口 \(c_k\le\ell-2\)。这把高阶循环孔压缩成可定位的
CYCLIC_PRIMARY_DIGIT_DEFICIT，而不是笼统的容量不足。

该终端的适用范围是固定 source-fiber。不同参数纤维之间的关系块不能自动合并，
还必须满足 source-switch 合同、重复 q 共同账本和稳定子商的独立性。下一步应将
某一层的数字缺口连接到低模数可提升实例、q-height 严格下降，或另一条 Type I/II
证书；若无法连接，则保留为严格的高阶循环负边界。主张卡见
[Type II 源纤维循环 \(\ell\)-primary 进位层终端](../claims/type-II-source-fiber-cyclic-primary-digit-terminal.md)。

## 2026-08-05 锚点外置的分离角色回执

固定 source-fiber 的目标相对截面可规范化为
\[
S_t=\alpha R_Q,\qquad R_Q\subseteq\Delta_Q.
\]
若 \(\alpha\notin\Delta_Q\)，有限阿贝尔对偶分离给出
\(\chi|_{\Delta_Q}=1\)、\(\chi(\alpha)\ne1\)。于是
\[
\widehat{1_{S_t}}(\chi)=\overline{\chi(\alpha)}|R_Q|,
\]
得到最大幅度的 ANCHOR_SEPARATING_CHARACTER 负证书。该证书把“相对关系覆盖了
但目标仍不在正确陪集”变成可枚举相位，而不是容量矛盾。

若角色对候选低模商的核平凡，并通过源关系格仿射相容性检查，则可以回译为低模
Fourier 负证书；否则必须标记 LIFT_OBSTRUCTED。\(p=97\) 的 \(U(24)\) 伪命中
中，\(\Delta_Q=1,\alpha=13\) 确有分离角色，但它不对模4商核平凡，所以不能把
模4伪命中当作 Type II 证书。主张卡见
[Type II 源纤维锚点外置的分离角色证书](../claims/type-II-source-fiber-anchor-separating-character-certificate.md)。

## 2026-08-05 数字缺口的商缺失—顶层核 Fourier 二分

在 \(C_{\ell^a}\) 的固定 source-fiber 中沿自然投影塔取目标第一次缺失的层
\(j_0\)。若 \(j_0<a\)，目标已经在严格较小的 \(\ell\)-primary 商中缺失；若
所有 \(j<a\) 的投影都命中，则顶层核 \(K_{a-1}\simeq C_\ell\) 的目标截面是
非空真子集，Parseval 给出非平凡核角色和精确 Fourier 负证书。前面的进位层终端
同时保证任何缺失都伴随某个 \(c_k\le\ell-2\) 的数字缺口。

这一步把“层容量不足”连接到已有的低模数商—核 Fourier 三分：低商分支必须检查
source-switch 参数纤维是否存在；顶层核角色作为内禀乘法角色已经是合法 Fourier
负证书，只有外部参数频率的再解释才需检查源关系格相容性。低商候选或外部相位失败
时显式标记 LIFT_OBSTRUCTED，不能假设自动递降。主张卡见
[Type II 循环 \(\ell\)-primary 数字缺口的商缺失—顶层核 Fourier 回执](../claims/type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay.md)。

本轮补上了低商的算术提升门。对当前 \(D_0\)、来源混合因子
\(h=\prod h_i\equiv-1\pmod{4D_0}\) 和 CRT 参数 \(a_0\)，完整候选集为
\[
\mathscr L_{D_0}(h,a_0;p)
=\{(D',A):D'\mid D_0,\ A\mid D',\ D'/A\text{ 平方自由},\
4AD'<p,\ AD'\equiv D_0a_0\pmod h\}.
\]
该集合中的每个元素都等价地产生 \(h\mid p+4AD'\) 及
\(K'=(h+1)/(4D')\)、\(B'=(K'p+A)/h\) 的 Type II 正规形；含严格
\(D'<D_0\) 才是递降，只有 \(D'=D_0\) 是同层 source-switch。候选集为空时，
抽象商分支必须标记 ARITHMETIC_LIFT_EMPTY。\(p=97,h=143\) 的候选集为空，
而 \(p=5113,h=119\) 包含 \((D',A)=(1,1)\)，分别验证了两种边界。详见
[数字缺口商缺失—顶层核 Fourier 回执](../claims/type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay.md)。

还需区分除子格空集与真正的算术空集。对同一 \(h\) 令
\(L=(h+1)/4\)，枚举所有 \(ACK=L\) 的 raw 三元组，并筛
\(A\equiv4D_0Ka_0\pmod h\)、\(A\le(Kp+A)/h\)。原除子格候选都嵌入该集合，
但 raw 集允许 \(A,C\) 脱离旧 \(D_0\) 除子格；非空时立即给出 Type II。小例
\(p=73,D_0=1,a_0=8,h=15\) 中旧除子格为空，而
\((A,C,K,B)=(2,2,1,5)\) 是直接证书；\(p=97,h=143\) 的 raw 集仍为空。
因此下一步记录顺序应为 ARITHMETIC_LIFT_EMPTY、raw 回退、再到
RAW_LIFT_EMPTY，而不是把第一种空集直接当作全局负结果。详见
[Type II 算术提升空集后的 raw 因子回退判据](../claims/type-II-arithmetic-lift-raw-factor-fallback.md)。

raw 集仍为空时，失败不再只保留一个布尔值。令 \(L=(h+1)/4\)，把所有
\(d\mid L,A\mid d\) 且满足 raw 序条件的 \(Ad=A^2C\) 收集为
\(\mathcal S_{L,p}^{\rm ord}\)。raw 存在当且仅当
\(D_0a_0\bmod h\in\mathcal S_{L,p}^{\rm ord}\)。不命中时，对
\(1_{\mathcal S}-\delta_{D_0a_0}\) 做循环群 Fourier，非平凡能量精确为
\[
h(|\mathcal S|+1)-(|\mathcal S|-1)^2.
\]
若所选参数频率通过源关系格仿射相容性，就得到 F/G 对偶输入；否则标记
RAW_DIVISOR_FOURIER/LIFT_OBSTRUCTED。\(p=97,h=143\) 的残数集大小为 11、目标为
83，非平凡总能量为 1616。详见
[Type II raw 空集的平方除子残数 Fourier 证书](../claims/type-II-raw-divisor-residue-fourier-certificate.md)。
对指定源群 \(H\)，还可先按
\[
h/\gcd(h,j)\mid\exp(H)
\]
筛掉不可能提升的频率；\(p=97,h=143\) 时 \(U(24)\) 指数为 2，所有非平凡频率均
被该阶筛排除。这把该边界明确归入 LIFT_OBSTRUCTED，而不是误记为 Type II 递降。
一般令 \(e=\gcd(h,\exp H)\)，把残数集投影到 \(\mathbb Z/e\mathbb Z\) 并保留重数；
投影锚定 Fourier 的非平凡能量若为正，则至少有一个阶合格频率可继续做关系格
相容性检查；若为零，则同一源群的全部非平凡角色对该空集不可见，应立即切换到
另一条射线或良基递降。

## 2026-08-05 跨参数纤维 q-height 容量 surplus

将每个 \(A\)-纤维的精确活跃容量
\[
\kappa_{i,A}=\min(d_i(A),\operatorname{ord}(u_iT_A)-1)
\]
先在纤维内计算，再取任意正权重 \(w_A\) 聚合：
\[
\mathcal Q_w=\sum_Aw_A\sum_i\kappa_{i,A},\qquad
\mathcal B_w=\sum_Aw_A(|G_*/T_A|-2).
\]
若所有纤维都遗漏 \(-1\)，逐纤维 Kneser 缺口强制
\(\mathcal Q_w\le\mathcal B_w\)；若可证明 \(\mathcal Q_w>\mathcal B_w\)，则至少一个
纤维直接命中并给出 Type II 证书。该聚合允许同一来源在不同纤维复用，但不把
不同纤维的乘积池化，因此避开 \(p=97\) 型伪命中。

这给出了当前跨状态 q-height 容量的第一个严格 surplus 门。若 surplus 不正，保留
\(\delta_A=|G_*/T_A|-2-\sum_i\kappa_{i,A}\) 的逐纤维缺口，再进入数字缺口商/核
Fourier 或算术提升门。主张卡见
[Type II 跨参数纤维 q-height 容量 surplus 证书](../claims/type-II-cross-state-fiber-capacity-surplus-certificate.md)。

## 2026-08-05 Kneser 饱和纤维的一孔 Fourier 结构

若某个目标缺失纤维满足
\[
\delta_A=|G_*/T_A|-2-\sum_i\kappa_{i,A}=0,
\]
则 Kneser 下界和目标陪集缺失上界同时取等号，严格得到
\[
P_A=G_*\setminus(-1T_A).
\]
因此它只缺稳定子商中的一个目标陪集，所有非平凡 quotient 角色都有精确 Fourier
系数 \(-|T_A|\overline{\chi(-1)}\)。若 \(\delta_A>0\)，遗漏陪集数仍至多
\(\delta_A+1\)，并可由跨纤维总 deficit 预算控制。

这把 surplus 非正时的近饱和残余转成规范 quotient Fourier 证书，而不是笼统的
“容量不足”。它仍是负证据，下一步需证明一孔/少孔角色能进入 F/G 容量、实际
Type II source-switch 或严格递降。主张卡见
[Type II Kneser 饱和纤维的一孔陪集与 quotient Fourier 证书](../claims/type-II-kneser-saturated-one-coset-hole-certificate.md)。

一孔纤维的填洞引理进一步给出严格二分：若新增源块
\(B(u)=\{1,u\}\) 保持同一参数纤维且 \(u\notin T_A\)，则
\[
P_AB(u)=G_*;
\]
若 \(u\in T_A\)，则 \(P_AB(u)=P_A\)。因此饱和分支要么由合法非平凡新增块直接
得到 Type II，要么所有新增块均被稳定子吸收；跨纤维或合同不合法的来源必须标记
UNAVAILABLE_SOURCE_BLOCK。


少孔情形也有精确的平移交公式：若当前缺口集大小为 \(c_A\)，剩余合法源积集的
商像大小超过 \(c_A\)，则所有平移缺口的交为空，必填满目标。结合
\(c_A\le\delta_A+1\)，这给出“剩余 q-height 超过缺口预算即命中”的新容量门；
等号时则进入 HOLE_LOCKED 的平移结构分支。

在 HOLE_LOCKED 等号分支，目标积集的 quotient Fourier 系数等于剩余源积集
系数乘以锚点相位并取负号；Parseval 给出
\[
\max_{\bar\chi\ne1}|\widehat{1_{\bar P}}(\bar\chi)|
\ge\sqrt{\frac{|\bar R|(|\bar G|-|\bar R|)}{|\bar G|-1}}.
\]
这是把少孔源结构直接送入 F/G 对偶容量的内禀接口。

剩余源块还满足一个直接 q-height 阈值：若其活跃容量总和
\(\sum_i\kappa_i^{\rm rem}\ge c_A\)，Kneser 给出
\(|\bar R|\ge1+\sum_i\kappa_i^{\rm rem}>c_A\)，因此必填满目标；只有容量至多
\(c_A-1\) 时才可能保留 HOLE_LOCKED。

选定 quotient 角色后还有锚点—关系二分：若角色在剩余源积集上恒相位，则关系
需求为零，只留下锚点 Fourier 证书；若相位变化，则精确成对能量
\(2N^2(1-\rho^2)\) 为正，差分群至少有一个非零初等商秩，源关系列注入必须提供
对应方向，否则输出 SOURCE_RANK_INCONSISTENT。该分派避免把纯锚点 Fourier
幅度误计为 q-height 超载。

新增的条件性桥把这类非恒相位需求接到 F/G 的真实 q 进相位胞：若一组状态已经
证明共享同一个 q-primary 方向，且每个需求 \(d_i\) 有真实清分高度
\(e_i\ge d_i\)，则相位中心
\(\gamma_i=-A_iR_i^{-1}\pmod {q^{e_i}}\) 和标签同余必须满足相位胞合同。因而
\[
\sum_i d_i\le\mu\sum_c\left(\frac{M_c}{q-1}+H_c\right).
\]
已验证的严格超载迫使目标命中、源秩不一致、相位提升受阻或已有 F/G 短证书/递降
出口。共同 q、真实相位提升及有界标签仍需独立证明；该桥的完整陈述见
[Type II HOLE Fourier 非恒相位到 F/G q 进相位胞容量桥](../claims/type-II-hole-fourier-phase-cell-capacity-bridge.md)。

随后把共同 q 假设放宽为 primary 分解：对每个状态的差分群逐素数计算
\(d_{i,q}=\dim_{\mathbb F_q}(\Delta_{i,q}/q\Delta_{i,q})\)，先用真实候选高度
\(d_q(s)=\min(L_q(s),V_q(s))\) 合并重复 q，再对各 q 的相位胞容量求和。若
\[
\sum_q\sum_i d_{i,q}>
\sum_q\mu_q\sum_{c\in\mathcal C_q}
\left(\frac{M_{q,c}}{q-1}+H_{q,c}\right),
\]
且每个计入项都已有 source-switch、相位中心和标签合同，则当前 HOLE 族必有
Type II 命中、源秩不一致、某个 q 的相位/算术提升失败或 F/G 出口。该多 primary
桥不声称每个 q 方向都能提升；完整边界见
[Type II HOLE Fourier 多 primary 到 F/G 分素数相位容量和](../claims/type-II-hole-fourier-multiprimary-phase-capacity-sum.md)。

## 2026-08-05 循环源商的 raw 频率提升矩阵

raw 残数 Fourier 的最后一个来源缺口在循环商上得到有限化。若真实源关系商
\(H=\langle g\rangle\simeq C_m\)，源单位及锚点为 \(g^{c_j}\)，参数标签为
\(\lambda_j\in\mathbb Z/e\mathbb Z\)，频率 \(k\) 可提升为真实角色当且仅当一元系统

\[
e c_j s-mk\lambda_j\equiv0\pmod{em}
\]

对所有源行和锚点行有解。逐行约化给出可除性条件；剩余同余由广义 CRT 检查。单行
不可除性或两行 CRT 不相容，分别输出有限的 LIFT_OBSTRUCTED/源关系矛盾；有解时
显式构造 \(\chi_s(g)=e^{2\pi i s/m}\)，其锚点相位才可以进入 F/G 容量账本。
这把抽象的源关系格门变成可复核的整数算法，但仍不构造 raw 标签本身，也不证明
相容角色必然超载。主张卡见
[Type II raw 参数频率的循环源商提升矩阵](../claims/type-II-raw-cyclic-source-lift-matrix.md)。

## 2026-08-05 有限阿贝尔源商的 SNF 提升

循环源商之外，raw 参数频率的来源门已扩展到
\(H=\bigoplus_{\nu=1}^{d}C_{m_\nu}\)。取
\(L=\operatorname{lcm}(e,m_1,\ldots,m_d)\)，把源坐标系数写成
\(A_{j\nu}=Lc_{j\nu}/m_\nu\)，把参数标签写成 \(b_j=Lk\lambda_j/e\)，则提升问题
等价于
\[
B x=b,\qquad B=[A\mid -LI].
\]
对 \(B\) 求 Smith 正规形后，所有非零对角元必须整除 \(Ub\)，零行必须在 \(Ub\) 上
消失；通过时解向量的角色坐标构造真实有限群字符，失败行则给出明确的
SOURCE_RELATION_FOURIER/LIFT_OBSTRUCTED 关系组合。该结果把非循环源商也从
“抽象相容性”推进为有限整数证书，但仍不构造 raw 标签映射，也不闭合容量超载。
主张卡见
[Type II raw 参数频率的有限阿贝尔源商 SNF 提升](../claims/type-II-raw-finite-abelian-source-lift-snf.md)。

## 2026-08-05 CRT 局部标签的幂等元桥

又定位到一个更早的来源错误：若 \(h=\prod_i h_i\) 且 \(h_i\) 两两互素，局部标签
\(a_i\bmod h_i\) 不能直接当作共同 \(\mathbb Z/h\mathbb Z\) 元素做 Fourier。令
\(E_i=(h/h_i)((h/h_i)^{-1}\bmod h_i)\)，则规范全局标签是
\[
\Phi(a_1,\ldots,a_r)=\sum_iE_i a_i\pmod h,
\]
全局角色的正确拉回为
\[
\exp(2\pi i k\Phi(a)/h)
=\prod_i\exp(2\pi i k t_i a_i/h_i).
\]
若直接代入局部代表，则代表替换要求 \((h/h_i)\mid k\)；两个以上互素非平凡块
合并后只有 \(k=0\) 与代表选择无关。\(p=97,h_1=11,h_2=13\) 的规范合并为
\(a_0=133\bmod143\)，不是把 \(1,3\) 分别视为两个共同模数标签。该桥接修正后，
局部相位还需继续通过有限阿贝尔源商 SNF，不能直接计入容量。主张卡见
[Type II CRT 局部标签到全局 Fourier 的幂等元桥](../claims/type-II-crt-local-label-idempotent-phase-bridge.md)。
若源商指数为 \(E\)，幂等元拉回的第 \(i\) 个频率阶为
\(h_i/\gcd(h_i,k)\)，所以允许频率恰是
\((h/\gcd(h,E))\mathbb Z/h\mathbb Z\)。这给出局部化的精确阶筛；\(p=97\) 的
\(E=2\) 与 \(h=143\) 使该子群只有零频率。

## 2026-08-05 有限阿贝尔多 primary 进位终端

固定源纤维的差分商若分解为
\[
H=\bigoplus_\nu C_{\ell_\nu^{a_\nu}},
\]
并且合法二点关系块可按 primary 因子分组、保持纤维且独立选择，则每个
\(\ell_\nu\)-进位层只要有至少 \(\ell_\nu-1\) 个块，各组由循环数字终端覆盖对应
primary，直和后整体覆盖 \(H\)，锚点在商内时直接得到 Type II 命中。目标缺失
因此给出锚点外置或一个明确的 \((\nu,k)\) 层缺口；\(\ell_\nu=2\) 时是广义
\(2^j\) 终端。该结果把 q-height 源列去重后的容量直接接到多 primary 终端，但
不假设跨 primary 混合块自动可分组。主张卡见
[Type II 源纤维有限阿贝尔多 primary 进位终端](../claims/type-II-source-fiber-multiprimary-digit-terminal.md)。

## 2026-08-05 有限阿贝尔合成列缺口回执

对任意有限阿贝尔目标差分商 \(H\)，沿素数阶合成列
\(0\leftarrow H_1\leftarrow\cdots\leftarrow H_L=H\) 追踪源和集与目标投影。第一个
未命中若发生在 \(j<L\)，得到严格较小的有限阿贝尔商；若所有较小商都命中，则
顶层核 \(C_{\ell_L}\) 的目标截面是非空真子集，Parseval 给出精确的非平凡核
Fourier 角色。该二分把循环数字缺口推广到非循环相关缺失，并与
MULTIPRIMARY_DIGIT_DEFICIT、SNF 提升和算术 source-switch 门相接。主张卡见
[Type II 源纤维有限阿贝尔合成列商缺失—素数核 Fourier 回执](../claims/type-II-source-fiber-finite-abelian-composition-relay.md)。

## 2026-08-05 顶层核角色的最小秩容量

合成列顶层 \(C_\ell\) 核的 Fourier 角色现在有了有向容量接口。若角色在目标
相对支撑上恒相位，系数只剩锚点相位，关系 q-height 需求为零；若相位非恒定，
则差分群含一个 \(\ell\)-初等方向，任何真实保持纤维的源列账本至少支付一个
独立 \(\ell\) 容量单位。多个独立角色按初等商秩收费，不能按 pair-energy 边数
重复计数。主张卡见
[Type II 合成列顶层核角色的锚点—初等秩容量二分](../claims/type-II-composition-kernel-role-rank-capacity-bridge.md)。

## 2026-08-05 跨状态 Hall q 进容量桥

把已证明的顶层秩方向、primary 数字层缺口等组成请求集，把真实 q-adic 赋值层
组成资源槽；只有通过 source-switch、SNF、范围和 shared-q 合同的请求—资源对才
连边。有限 Hall 定理给出精确二分：完整匹配时得到无重复收费的跨状态容量映射；
存在请求子集 \(U\) 满足 \(|U|>|N(U)|\) 时得到严格容量缺口；边本身不合法则独立
记为 EDGE_OBSTRUCTED。该桥为把局部 q-height 与跨状态竞争接起来提供了可计算的
最小接口。主张卡见
[Type II 跨状态源需求的 Hall q 进容量桥](../claims/type-II-cross-state-source-demand-hall-capacity-bridge.md)。

## 2026-08-05 Hall 缺口的严格递降闭包判据

进一步把 Hall 图接到良基势函数。对最大匹配从所有未匹配请求作交替可达闭包，
得到规范最小割 \((U_M,N_M,u_M)\)，并证明
\(|U_M|-|N_M|=u_M>0\)。因此多 q、多层和跨状态竞争都能压缩为一个可复核的
有限缺口，而不必凭直觉选择“最拥挤的 q”。

新判据要求每个最小割满足四类局部闭包之一：缺口请求有保持标签的 LOWER_RELAY；
候选边有 SNF/CRT/算术 OBSTRUCTED；Kneser surplus 已越过纤维缺口；或顶层角色
已有闭合锚点出口。若最大匹配覆盖所有请求但仍未越过 Kneser 缺口，还必须满足
HC5，即每个已匹配请求都有终端、严格回退或 F/G 出口；不能把“已占用资源”冒充
目标命中。有限势归纳由此给出 Type II、严格可提升递降或显式算术负证书。

若某个最小割不满足这些条件，规范回执为
UNRELAYABLE_HALL_DEFICIT；完整匹配但 HC5 失败则为
UNRELAYABLE_FULL_MATCH。这两个回执不是猜想反例，而是当前全局证明仍需补上的
最小闭包条件。主张卡见
[Type II Hall 缺口到严格递降的有限闭包判据](../claims/type-II-hall-deficit-relay-closure-criterion.md)。

## 2026-08-05 Hall 匹配的单纤维实现门

进一步修正 surplus 分支：跨状态 Hall 完整匹配只说明 q 进资源没有重复使用，
不能自动把不同整数 \(p+4s_A\) 的因子相乘。只有存在保持来源标签的
FIBER_REALIZED(A) 映射，把匹配后的层回译到同一个参数纤维，并同时满足整除、
\(h\equiv-1\pmod{4D_A}\) 和 \(B'>A\) 时，匹配才可计入该纤维的 Kneser surplus。
否则统一记 UNREALIZED_CROSS_STATE_MATCH；若映射因 SNF/CRT/范围失败则记
OBSTRUCTED。

\(p=97\)、\(M=24\) 的 \(P_1=\{1,11\}\)、\(P_2=\{1,13\}\) 各自漏掉 23，
但 \(11\cdot13\equiv23\pmod{24}\)，给出严格的混合纤维伪命中。因此 Hall 闭包的
HC3 必须升级为 HC3-FIBER。主张卡见
[Type II Hall 匹配触发 Kneser surplus 的单纤维实现门](../claims/type-II-hall-matching-fiber-realization-gate.md)。
该实现门并非只能作抽象假设：固定 \(M=4D\) 时，带来源 CRT 给出充要条件
\(a\equiv a_i\pmod{h_i}\) 的 admissible \(a\mid D\)；同模数失败后，除子格后继
等价于 \(AD'\equiv Da_0\pmod h\)。当 \(h>D^2\) 时候选至多一个，因而
HC3-FIBER 的同模数/降模来源检查可有限化；空集则记
CRT_NO_ADMISSIBLE_FIBER。该有限判据来自
[Type II 同模数与除子格 source-switch 的带来源 CRT 判据](../claims/type-II-same-modulus-source-switch-crt-criterion.md)。
对一个已经由 Hall 匹配形成的带来源混合因子 \(h\)，这道门进一步闭合为有限三分：
同模数 CRT、严格除子格和 raw 因子三类候选依次给出 Type II；三者全空才记
ALL_ARITHMETIC_LIFT_EMPTY。该回执只排除当前 \(h\) 的三种提升族，不能误写成
核心素数没有其它证书。主张卡见
[Type II Hall 混合因子的同模数—降模—raw 算术闭合三分](../claims/type-II-hall-fiber-arithmetic-closure-trichotomy.md)。
在进入该三分前新增源块束目标残数门：有限指数乘积集若含 \(-1\)，选择命中指数
形成 \(h\)；若不含 \(-1\)，则在 \(\mathbb Z/(4D)\mathbb Z\) 上由 Parseval 给出
规范非平凡 Fourier 能量。频率必须先通过源群指数阶筛和有限阿贝尔 SNF，才能
进入 F/G 容量；不相容频率记 LIFT_OBSTRUCTED。主张卡见
[Type II Hall 源块束的目标残数—Fourier 前置门](../claims/type-II-hall-bundle-target-residue-fourier-gate.md)。
进一步令 \(e=\gcd(4D,\exp H)\)，把源块乘积集投影到 \(\mathbb Z/e\mathbb Z\)；
Parseval 给出所有阶整除 \(\exp H\) 的可容许频率的精确总能量。正能量保证至少
一个频率能通过指数阶筛，零能量则是“当前源群角色完全不可见”的有限证书，随后
仍需 SNF 检查。
零能量等价于投影重数满足
\(m(y)=c+\mathbf 1_{y=\pi_e(t)}\)，因此不是频率尚未找到，而是当前源群角色
全部不可见；任何锚点分离必须改用更大的环境商或不同稳定子纤维。
零能量分支现在先检查规范锚点 \(\alpha\in\Delta\) 与否：外置时构造纯锚点环境
角色；在差分群内时任何分离角色至少产生一个 \(\ell\)-初等源秩方向，秩账本为零
则输出 SOURCE_RANK_INCONSISTENT，否则送入 SOURCE_RANK_DEMAND。主张卡见
[Type II 锚点外置—关系初等秩的 Fourier dispatch](../claims/type-II-anchor-rank-fourier-dispatch.md)。
多个独立 \(\ell\)-角色的 q 槽支付还需检查源列向量的线性独立性。Rado
rank-Hall 条件要求每个请求子集的邻域源列秩不小于请求数；普通槽数量匹配但
向量重复时输出 LINEAR_RANK_DEFICIT。主张卡见
[Type II 顶层角色的 Rado 线性 rank-Hall 容量桥](../claims/type-II-rado-linear-rank-hall-capacity-bridge.md)。

## 2026-08-05 跨状态完整匹配的算术实现—Fourier 三分

把没有 FIBER_REALIZED 映射的完整匹配进一步闭合为有限 typed 分派。先确认所有
匹配块能嵌入共同 \(U(4D_*)\) 且 shared-\(q\) 已合并；失败则记录
AMBIENT_SOURCE_OBSTRUCTED。若匹配源块束的乘积集含 \(-1\)，目标见证依次进入
同模数 CRT、严格除子格和 raw 三类算术候选：命中 Type II、较小模数后继、raw
Type II，或三类全空后转 ALL_ARITHMETIC_LIFT_EMPTY→RAW_DIVISOR_FOURIER（调用
raw 除子残数桥）。若不含 \(-1\)，
在共同单位群上由 Parseval 构造非平凡角色，再经指数阶和 SNF 分成
CROSS_STATE_SOURCE_RELATION_FOURIER 或 CROSS_STATE_ARITHMETIC_FOURIER_OBSTRUCTED。
主张卡见
[Type II 跨状态完整匹配的算术实现—Fourier 三分](../claims/type-II-cross-state-full-match-realization-fourier-trichotomy.md)。
这一步不把跨状态混合积直接写成 Type II，而是将 UNREALIZED_CROSS_STATE_MATCH
推进为可验证的算术/Fourier 后继；剩余问题是这些后继的 F/G 载体或严格势下降。

## 2026-08-05 跨状态相容角色的锚点—初等秩—Hall 分派

跨状态共同群 Fourier 通过指数阶和 SNF 后，新增一层真实源关系分派。若角色在
源差分群上恒定，它只是纯锚点相位，不产生 q-height 需求；若角色在差分群上非恒定，
则至少产生一个 \(\ell\)-初等关系方向。先检查保持纤维的合法源列秩：秩不足时输出
SOURCE_RANK_INCONSISTENT；秩足够后把独立方向接入带来源的 Hall 图，缺口转为
HALL_DEFICIT_FOURIER，完整匹配只有在稳定子商活跃容量达到 Kneser 缺口时才给出
Type II。主张卡见
[Type II 跨状态相容角色的锚点—初等秩—Hall 容量分派](../claims/type-II-cross-state-source-relation-role-capacity-dispatch.md)。
这一步仍不保证每个相容角色都有足够 q 进载体，未闭合的边界是 Hall 缺口的严格
递降或 F/G 终端。

## 2026-08-05 跨状态分层 Rado—q 进容量切割

把关系角色的源列秩与移位 q 进层放入同一个请求子集切割。对请求子集 \(U\)，
逐层移位上界
\[
\mathsf C_q(U)=\sum_{j\le E_U}C_j(S_U,q)
\]
先给出只依赖移位集的硬上界；若 \(\mathsf C_q(U)<|U|\)，输出
Q_ADIC_LAYER_CAPACITY_DEFICIT。只有该上界通过后，才检查 Rado 源列秩；
秩不足输出 LINEAR_RANK_DEFICIT，实际兼容边稀疏才输出普通 HALL_DEFICIT。
这修正了把 q 进缺口和线性秩缺口混为一个 Hall 数量缺口的逻辑跳步。
\(p=433,S=\{16,100\},q=7\) 的高度 \(1,2\) 给出层容量 \(2+1=3\)，若两条
来源都要求 \(7^2\)，需求 \(4>3\)，得到严格 q 进切割；实际高度恰好达到等号。
主张卡见
[Type II 跨状态分层 Rado—q 进容量切割](../claims/type-II-cross-state-layered-rado-qcapacity-cut.md)。

## 2026-08-05 q 进缺口到 annihilator 商递降

若固定 q 的分层容量切割给出 \(\mathsf C_q(U)<|U|\)，则实际邻域严格少于请求数，
同一 \(\ell\)-初等商中可构造一个阶 \(\ell\) 对偶角色，平凡于全部邻域源列并分离
未支付请求。若最小割满足 SOURCE-DOMINATING-CUT，即每个固定纤维源生成元都有
合法同纤维邻接列，则该角色湮灭整个源集；目标相位非平凡时进入
GLOBAL_ANNIHILATOR_LOWER_RELAY，核平凡时进入 TOP_PRIMARY_ANNIHILATOR，目标相位
平凡时保留为关系 Fourier。源列逃逸则必须补入 Hall 菜单或记录障碍。
主张卡见
[Type II 跨状态 q 进缺口的 annihilator 商递降桥](../claims/type-II-cross-state-qcapacity-deficit-annihilator-relay.md)。
该桥首次把 q 进容量缺口接到明确的商递降条件，但整数 source-switch 和 E1--E5
提升仍是全局剩余。

## 2026-08-05 秩缺口的对偶 Fourier 分离

Rado 秩条件失败不再只停留在
\(\mathrm{LINEAR\_RANK\_DEFICIT}\)。若需求方向张成 \(D_U\)，可用源槽张成
\(W_U\)，且 \(\dim W_U<\dim D_U\)，有限维对偶的双正交关系直接给出
\(\lambda\in V_\ell^*\)，使 \(\lambda|_{W_U}=0\)、\(\lambda|_{D_U}\ne0\)。
将 \(\lambda\) 提升为
\(\chi_\lambda(x)=\exp(2\pi i\lambda(x\bmod\ell A_\ell)/\ell)\)，即可得到在所有
邻域源列上平凡、在至少一个未支付需求方向上非平凡的
SOURCE_RANK_FOURIER_SEPARATION。

该证书把普通 Hall 数量缺口和真实源关系缺口统一到同一有限角色接口：锚点被
\(\lambda\) 分离时转入环境锚点/F/G 检查；锚点未被分离时保留为关系 Fourier
缺口，并要求 F/G 载体或严格良基递降。它证明了“重复 q 槽不能支付独立角色”不仅
是计数约定，而是存在一个可复核的阶 \(\ell\) 对偶角色。具体引理见
[Type II 线性秩缺口的阶 \(\ell\) 对偶分离证书](../claims/type-II-linear-rank-deficit-dual-separation-certificate.md)。

此推进仍不自动关闭全局猜想：对偶角色的 F/G 承接或其 annihilator 商的严格势下降
仍需在每个来源纤维中独立证明。

## 2026-08-05 固定纤维 Hall 缺口的线性精化

在同一参数纤维、同一 \(\ell\)-初等源商中，若 Hall 缺口请求已取成独立方向，
\(|N(U)|<|U|\) 立即给出
\[
\operatorname{rank}\operatorname{span}\{v_c:c\in N(U)\}
\le |N(U)|<|U|.
\]
因此有限维对偶构造出一个在所有可用源槽上平凡、在至少一个请求方向上非平凡的
阶 \(\ell\) 角色，回执精化为 HALL_DEFICIT_FOURIER_SEPARATION。这一步把
固定纤维的数量 Hall 缺口接入前面已有的 Rado/对偶分派；只有跨纤维、未实现来源
标签或算术边尚未合法化时，才保留粗粒度的 Hall 缺口。主张卡见
[Type II 固定纤维 Hall 缺口到线性对偶分离桥](../claims/type-II-hall-deficit-linear-dual-bridge.md)。

这仍不是整数 Type II 或素数递降定理：分离角色必须继续通过锚点/F/G 载体或
annihilator 商的严格势下降，跨纤维容量仍必须通过单纤维实现门。

## 2026-08-05 算术全空的 raw Fourier 闭合

Hall 混合因子的同模数、严格降模和 raw 三类候选若全部为空，不能把
ALL_ARITHMETIC_LIFT_EMPTY 当作最终负结论。三类全空蕴含 raw 候选集为空；将全部
合法 raw 平方除子残数与目标残数作差后，Parseval 给出严格正的非平凡 Fourier
能量。随后先做源群指数阶筛，再做循环同余/有限阿贝尔 SNF：通过者进入
SOURCE_RELATION_FOURIER，全部不通过者形成显式
ARITHMETIC_FOURIER_LIFT_OBSTRUCTED。主张卡见
[Type II 算术提升全空到 raw Fourier 的闭合桥](../claims/type-II-arithmetic-empty-raw-fourier-bridge.md)。

这一步把 HC2 的算术空集分支精化为对偶或障碍回执，但仍没有证明可提升角色必然
产生 F/G 容量或严格整数递降。

## 2026-08-05 完整匹配的稳定子增长—商 relay

对已经通过 FIBER_REALIZED 的完整匹配，把真实源块按顺序加入同一纤维积集
\(P_k=A_0B_1\cdots B_k\)，并记录 \(T_k=\operatorname{Stab}(P_k)\)。稳定子单调
增大；若 \(g_k\notin T_k\)，Kneser 给出至少 \(|T_k|\) 个新增元素，若
\(g_k\in T_k\)，该块被最终稳定子吸收。若累计下界
\[
|A_0|+\sum_{g_k\notin T_k}|T_k|>|H|-|T_m|
\]
成立，则目标陪集不可能缺失，直接得到 Type II；否则输出最终商
\(H/T_m\)、吸收块标签和精确稳定子缺口，进入合成列/Fourier/严格 relay。主张卡见
[Type II 单纤维完整匹配的稳定子增长或商 relay 证书](../claims/type-II-full-match-stabilizer-relay-certificate.md)。

这使 HC5 从抽象的“完整匹配后仍需终端”变成可枚举的增长或吸收检查，但跨纤维
匹配和稳定子商的整数解提升仍未自动闭合。

## 2026-08-05 稳定子同余核的源指数盒格判据

为处理低模数商递降的核心门 \(K\subseteq\operatorname{Stab}(P)\)，把真实源块写成
\(\varphi:\mathbb Z^r\to G\) 的有限指数盒像，令
\(\Lambda=\ker\varphi\)。严格证明：
\[
K\subseteq\operatorname{Stab}(P)
\iff
K\subseteq\operatorname{im}\varphi
\ \text{且}\
(\mathcal B+\Lambda)/\Lambda+
\varphi^{-1}(K)/\Lambda
=(\mathcal B+\Lambda)/\Lambda.
\]
前项由 SNF 源列成员检查，后项由有限商中的生成元平移检查。通过时得到
KERNEL_STABILIZER_CERT，可合法进入饱和商；失败时区分
KERNEL_NOT_IN_SOURCE 与 KERNEL_BOX_MISS。\(p=97\)、\(P=\{1,11\}\) 的模
\(24\to4\) 伪命中在第一项即失败。主张卡见
[Type II 稳定子同余核的源指数盒格判据](../claims/type-II-stabilizer-kernel-source-box-lattice-criterion.md)。

该判据把“核包含”从抽象假设变成可构造来源门，但尚未证明所有核心素数的 q-height
盒都通过该门。

## 2026-08-05 稳定子核失败的对偶 Fourier 二分

核门失败也不再只保留负标签。若 \(K\not\subseteq\operatorname{im}\varphi\)，有限
商 \(G/\operatorname{im}\varphi\) 给出一个平凡于全部源块、但在某个核元素上非平凡
的 KERNEL_SOURCE_ANNIHILATOR。若 \(K\subseteq\operatorname{im}\varphi\) 但
盒像不被 \(K\) 平移保持，取任意 \(k\) 使 \(Pk\ne P\)，则
\(1_P-1_{Pk}\) 的 Fourier 可逆性给出同时满足
\(\chi(k)\ne1\) 与 \(\widehat{1_P}(\chi)\ne0\) 的
KERNEL_BOX_FOURIER。目标商伪命中时，目标截面能量的
KERNEL_SPLIT_FOURIER 更强。主张卡见
[Type II 稳定子同余核失败的对偶 Fourier 二分](../claims/type-II-stabilizer-kernel-failure-dual-certificate.md)。

这些角色仍须通过源关系格/SNF 和 F/G 载体；该结果完成的是核失败的有限对偶化，
不是自动的整数递降。

## 2026-08-05 低模数伪命中的完整分派

把稳定子核、核失败 Fourier 和算术三分合并后，得到一个无悬空分支的伪命中定理：
若 \(-1\notin P\) 但 \(-1\in\pi(P)\)，核饱和与目标缺失矛盾；核不饱和必给出
KERNEL_SOURCE_ANNIHILATOR、KERNEL_BOX_FOURIER 或更强的
KERNEL_SPLIT_FOURIER。若商命中因子束有单纤维来源，则同模数/降模/raw 三分给出
Type II 或严格较小模数后继；三类全空时转 RAW_DIVISOR_FOURIER，再经指数/SNF
成为 SOURCE_RELATION_FOURIER 或显式障碍。主张卡见
[Type II 低模数伪命中的核—算术—Fourier 完整分派](../claims/type-II-low-modulus-pseudo-hit-complete-dispatch.md)。

该分派闭合的是低模数伪命中状态树，不等于所有 Fourier 障碍都已有 F/G 容量或
严格整数递降。

## 2026-08-05 源指数盒 Fourier 的整周期预筛

对带来源指数盒的重数测度，Fourier 系数逐列分解为几何和。若活跃列的角色像阶
\(d_i\) 整除 \(e_i+1\)，该角色系数严格为零；否则该列只留下
\(r_i=(e_i+1)\bmod d_i\) 的余段。q-primary 角色 \(d_i=q^{a_i}\) 进一步要求
\(v_q(e_i+1)<a_i\)，回执记录 PHASE_DEPTH_DEFICIT。完整周期部分从该角色中消失，
不得重复计入容量；角色阶和余段也不能直接冒充 F/G 清分高度，仍须通过真实源关系
去重、相位映射和嵌套同余。主张卡见
[Type II 源指数盒 Fourier 的整周期湮灭与相位深度缺口](../claims/type-II-source-box-fourier-full-cycle-phase-deficit.md)。

这一步把兼容 Fourier 到容量的入口变成可执行的预筛：先删除整周期湮灭角色，再把
剩余角色压缩到有限余段盒；若余段仍无法通过源关系或真实载体提升，回执继续保持
LIFT_OBSTRUCTED/PHASE_LIFT_OBSTRUCTED，而不是伪造容量超载或递降。

## 2026-08-05 q-height 集合 Fourier 与来源重数的饱和分流

补上 q-height 与 Fourier 之间的模式边界。对角色商中像阶为 \(d\) 的幂块：
当 \(e<d-1\) 时，指数幂块没有碰撞，集合 Fourier 与来源重数 Fourier 一致；
当 \(e\ge d-1\) 时，集合已经饱和为完整循环子群，非平凡集合 Fourier 为零，
Kneser 活跃容量最多 \(d-1\)。但来源重数仍可能因
\((e+1)\bmod d\ne0\) 留下非零余段。因此饱和分支输出 WEIGHTED_SOURCE_ONLY，
不能把该余段直接收费为无重数容量；必须转稳定子/碰撞去重、显式带权 source-switch
或严格递降。主张卡见
[Type II q 进幂块的集合 Fourier 与来源重数 Fourier 饱和分流](../claims/type-II-qheight-fourier-set-vs-multiplicity-saturation-boundary.md)。

## 2026-08-05 饱和带权角色的商缺失—核 Fourier 二分

进一步证明：若饱和幂块在选定商中生成子群 \(H\)，源集合像满足
\(\pi(P)H=\pi(P)\)。对目标缺失 \(t\)，若目标在 \(G/\pi^{-1}(H)\) 中仍缺失，
得到严格较小商回执 SATURATED_QUOTIENT_MISS；若商像命中，则目标核截面
\(S_t=\{k:\ tk\in P\}\) 是非空真子集，Parseval 给出
SATURATED_KERNEL_SPLIT。抽象商只有在整数 source-switch、来源标签和势下降均
通过后才具备递归资格；否则记录明确的 LIFT_OBSTRUCTED。主张卡见
[Type II 带权源饱和幂块的严格商缺失—核 Fourier 分派](../claims/type-II-weighted-source-saturated-quotient-kernel-dispatch.md)。

## 2026-08-05 线性 escaped source 的高阶 primary 加权层终端

上一轮的 \(\ell\)-初等商命题只对不同独立方向给出
\(\prod_i\min(d_i+1,\ell)\) 的乘积容量。同一循环
\(C_{\ell^a}\) 因子内的平行 source 不能这样相乘；新命题改用精确进位层加权容量
\[
W_k=\sum_{\nu_\ell(v_i)=k}\min(d_i,\ell-1).
\]
所有层 \(W_k\ge\ell-1\) 时，幂块和集覆盖整个循环 primary 因子，给出
PRIMARY_POWER_LAYER_HIT。取最高不足层 \(k^*\) 后，若 \(k^*<a-1\)，高层尾部精确
等于 \(\ell^{k^*+1}H\)，目标缺失严格投影到
\(C_{\ell^{k^*+1}}\)，形成一次性 primary 稳定子商递降；顶层不足则保留
PRIMARY_POWER_TOP_DIGIT_DEFICIT。只有 primary 坐标已分离、其它坐标饱和并且
E1--E5 通过时，才将因子级尾压缩升级为全局稳定子边；否则保留
PRIMARY_POWER_TAIL_LIFT_OBSTRUCTED。

主张卡见
[线性 escaped source 的高阶 primary 幂块进位容量终端](../claims/type-I-linear-escape-primary-digit-capacity-terminal.md)。
这一步补上了高 q-height 在同一循环 primary 内的“加法层容量”接口，并明确禁止把
初等乘积容量和高阶尾部容量重复计费；剩余决定性缺口是有限 source-switch 菜单的完备性、
尾部商的整数回译以及顶层 primary 缺口的 Type I/II 或 Fourier/annihilator 出口。

## 2026-08-05 escaped primary source-switch 的有限条件分派

为避免把抽象 primary 容量直接当作整数证书，有限菜单的 profile 只提出带来源的
q-prefix 请求。对每个候选 \(f=(D',A)\)、\(s_f=AD'\)，必须重新计算
\[
d_f(q)=\min\left\{
\sum_{i:q_i=q}\min(e_i,v_q(s_f-Da_i)),
v_q(p+4s_f)
\right\}.
\]
只有经 q-prefix Hall 见证的 \(n_{f,q}\le d_f(q)\) 才可形成唯一
\(q^{n_{f,q}}\) 整数块；同一个 q 不能由多条来源行重复收费。来源 CRT、平方自由和
范围实现的是保持来源的 D-格整数纤维；单位群映射 \(\eta\)/SNF 是独立的 relay
门，既不替代实际整除，也不推出 E1--E5。

若 \(h\equiv-1\pmod{4D'}\)，正规形直接检查 Type II。D-格候选为空仍须枚举
\(\mathscr R_{\rm raw}(h;p)\)：raw 非空时直接终端，raw 亦空才是该 \(h\) 的
RAW_LIFT_EMPTY。容量命中若缺少整数回译或明确提升合同，保持
LIFT_OBSTRUCTED；只有有目标状态、全域提升、E1--E5 和严格 E5 的 relay 才能登记
PRIMARY_BLOCK_STRICT_RELAY。

该表对声明的 source scope 是有限可回放的，却不覆盖未枚举 F/G alternate、raw
来源或下一递归层。没有菜单覆盖定理时，空候选只能记
PRIMARY_BLOCK_SOURCE_UNCLOSED，不能升级为全局算术失败。主张卡见
[线性 escaped primary source-switch 的有限条件分派](../claims/type-I-linear-escape-primary-source-switch-finite-dispatch.md)。

## 2026-08-05 canonical D-格菜单：局部闭合与固定层反例

固定 \(D\) 的标准 Type II 来源/目标除子格可以真正闭合：枚举
\[
a\mid D,\qquad (D',A),\qquad
e_{a,D',A,q}=\min\{v_q(p+4Da),v_q(p+4AD')\},
\]
并对每个 \((a,D',A,q)\) 只保留一个最大高度 route，profile 仅可选择其一个前缀，
得到有限 canonical 原子菜单。只要来源格非空，\(p+4Da\) 自动与 \(4D\) 互素，
故所有菜单 q 都是目标单位群的单位；该范围内没有 nonunit CRT 漏洞。菜单覆盖的是
一跳、保持来源的 D-格 source-switch，不包括 raw、外部 F/G alternate 或下一递归层。

这也给出可证的 residual 机制：若某目标纤维的菜单单位源子群不包含 escape 目标，
商角色给出 CANONICAL_D_LATTICE_ESCAPE_OBSTRUCTED。不能把“菜单有限”误读为
“菜单必支付”：固定
\[
(p,R,D)=(57{,}399{,}241,59,41)
\]
的所有原始来源在 \(\mathrm{QR}_{59}\) 中，对一个声明的 \(C_2\) rank-one demand
零支付；但下层 \(D'=1\) 产生新的非剩余因子。这是固定层菜单覆盖命题的严格反例，
不是 Erdős--Straus 的反例或递归 no-go。

主张和定点证书见
[canonical D-格来源菜单与纤维残余回执](../claims/type-I-linear-escape-canonical-d-lattice-source-menu.md)。

## 2026-08-05 G-anchor 的 Jacobi-odd 实际来源

高载体 \(n=p\) 的规范 G-anchor 不再只有抽象 Jacobi 分离。令
\[
R=p-2,\qquad K=(p-1)^2/4,\qquad Q=(p-3)/2.
\]
通用 source 的实际 raw 路径到达 \((1,2Q,1)\)，且 \(Q\) 正是完整超额 bundle；
所有 \(K\) 支撑在 \((\cdot/R)\) 的核中而 \(Q\) 在负陪集。因而
\[
\{d\mid Q:(d/R)=-1\}
\]
是非空、有限、可回放的 source/path 菜单。它将主余项从“没有实际来源的 G 相位”
收缩为“实际 Jacobi-odd source 如何回译到整数纤维或 strict relay”，后者仍未解决。

主张见
[G-anchor 的 Jacobi-odd 完整超额块与有限 raw 路径菜单](../claims/type-I-g-anchor-jacobi-odd-complete-excess-source-menu.md)。

## 2026-08-05 Hall 缺口的全源列闭包

现有 Hall 对偶角色只保证它在最小割的邻域槽上平凡；这不足以直接推出固定纤维
递降。新增全源列闭包检查：对同一固定纤维的全部实际源生成元逐列验证
\(\lambda(v_i)=0\)。若检查通过，源集整体落入
\(K=\ker\chi_\lambda\)；目标相位非平凡且 \(|K|>1\) 时，投影到 \(H/K\simeq C_\ell\)
得到严格商缺失和 GLOBAL_ANNIHILATOR_LOWER_RELAY，E1--E5/参数纤维通过后才是
真正递降；\(|K|=1\) 则记录 TOP_PRIMARY_ANNIHILATOR，并在二点关系块模型中精化为
CYCLIC_PRIMARY_DIGIT_DEFICIT\((\ell,0)\)。目标相位平凡时回执为
RELATION_FOURIER_NO_TARGET_SEPARATION，不能收费容量。

若某个源列被角色分离，输出 SOURCE_COLUMN_ESCAPE；有合法 source-switch 边则补入
完整 Hall 菜单重算，所有候选失败则保留 SOURCE_COLUMN_EDGE_OBSTRUCTED，跨纤维
未实现则记录 UNREALIZED_SOURCE_COLUMN。该分派见
[Type II 固定纤维 Hall 缺口的全源列闭包—商递降三分](../claims/type-II-hall-source-column-closure-relay.md)，
并将 HC6 加入 Hall 有限闭包条件。若最小割对每个源生成元都有同纤维合法邻接边，
则构成 SOURCE-DOMINATING-CUT，闭包自动通过。它消除了“当前邻域角色平凡即可递降”的逻辑跳步，
但没有解决跨纤维列实现、顶层 primary 终端或 FULL_MATCH relay 的全称问题。

## 2026-08-05 稳定子包含放宽与同余三分闭合

把同余核识别条件从 \(C_{D'}\subseteq H\) 放宽到真正必要的
\(C_{D'}\subseteq\operatorname{Stab}(P)\)。对每个候选 \(D'\)，三分为：

1. 稳定子包含：目标缺失精确传递到低模数，带来源标签的参数纤维门非空且回译
   通过时给出 STABILIZER_CONGRUENCE_LOWER_EDGE，E1--E5 完整；若某个来源子列表
   已满足 \(h_S\equiv-1\pmod{4D'}\)，先作为直接 Type II 终端处理；
2. 稳定子不包含：取 \(c\in C_{D'}\) 使 \(Pc\ne P\)，由
   \(1_P-1_{Pc}\) 构造 \(\chi(c)\ne1\) 且 \(\widehat{1_P}(\chi)\ne0\) 的
   CONGRUENCE_KERNEL_FOURIER；低模数伪命中再给出目标核截面；
3. 稳定子包含但来源参数纤维门为空：输出 ARITHMETIC_LIFT_OBSTRUCTED。

这对每个固定 \(D'\) 是穷尽且互斥的，主张卡见
[Type II 饱和源积集的同余稳定子—核 Fourier—算术三分](../claims/type-II-saturated-source-congruence-stabilizer-trichotomy.md)。

该分派的旧“同余核识别”表述现改为参数纤维门：\(C_{D'}\subseteq H\) 仍是
推出商缺失的方便充分条件，但一般递降只要求
\(C_{D'}\subseteq\operatorname{Stab}(P)\)。保留来源标签的两两互素列表
\(\mathbf h\) 必须逐项满足 \(h_i\mid p+4AD'\)、\(A\mid D'\)、平方自由和范围条件；
若子列表乘积已经满足 \(h_S\equiv-1\pmod{4D'}\)，则直接构成 Type II 终端，
不再算作“目标仍缺失”的后继。只有没有直接终端且参数纤维和 E1--E5 全部通过时，
才输出 STABILIZER_CONGRUENCE_LOWER_EDGE；否则分别保留
CONGRUENCE_KERNEL_FOURIER 或 ARITHMETIC_LIFT_OBSTRUCTED。\(p=97\)、
\(U(24)\to U(4)\) 的 \(H=\langle11\rangle\) 与
\(\ker=\{1,5,13,17\}\) 仍是核失败的严格边界。

## 2026-08-05 三条整数桥的收缩结果

本轮没有把有限菜单误报为统一递降，而是把三条看似可扩展的路径压缩到精确边界：

1. 除子分层 D-格闭包只枚举合法新来源。profile 必须固定 \((d,f)\)，并通过实际
   source-switch、标记提升与 E1--E5 后才形成边；\(d'<d\) 才有 \(\Omega(d)\) 下降。
   因此 \(p=57{,}399{,}241,D=41\) 的 \(d=1\) 非剩余因子不是现成的 \(41\to1\)
   递降。
2. G-anchor 的 label-preserving raw normal form 唯一命中
   \((A,C,k,h)=(1,1,2,7)\)。它是 \(D=1\) 的 Type II terminal，不能生成严格
   canonical D-格 source-switch；gap-3、gap-7、full-\(Q\) path 和 raw \(h=7\)
   只能作为平行分支处理。
3. 任何已带来源的 \(n=(p+4s)/h\) 都不产生新的 non-source D-only 双尾导体：
   \(h\equiv1\pmod4\) 进入既有 no-go，\(h\equiv3\pmod4\) 与
   \(n>4p/5\) 和 \(n<2p/3\) 的矛盾。保留的 gap-\(h\) 与 raw-ray 命中都是终端。

相应主张见
[分层来源闭包](../claims/type-I-linear-escape-divisor-stratified-recursive-source-closure.md)、
[G-anchor raw 终端唯一性](../claims/type-I-g-anchor-jacobi-raw-terminal-source-switch-bridge.md) 和
[primary 因子 non-source D-only no-go](../claims/type-I-linear-escape-primary-factor-donly-no-conductor.md)。

## 2026-08-05 复核后：带来源的 cofactor-supported r-chart 局部候选

上述候选已收敛为一条严格条件性正规形。令

\[
C=p-d,\qquad g=(A,C),\qquad a=A/g,\qquad
A_C=\operatorname{lcm}(A,C)=Ca,
\]

并由 \(M=kp+r\) 定义

\[
s=(4rd+1)/p,\qquad R_r=4r-s,\qquad K_r=rC.
\]

当 \(a\mid r\)、\(p<R_r\)、
`canonical_chart(p,A_C)=(R_r,K_r)`、完整 source/path 与结构化 fresh root
或经具名 adapter 重放的 charged-support 来源均已回放，且局部
\(\Pi_p(A_C)<\Pi_p(A)\) 时，真正的后继载体是

\[
M_T=A_C,\qquad C_T=r/a,\qquad d_T=p-C_T,\qquad n_T=4A_C-R_r,
\]

满足 \(K_r=M_TC_T\) 和 \(pn_T=4M_Td_T+1\)。这消除了把 \(r\) 误写为 target
carrier 的漏洞，也说明 \(r=M\) 只是 `same_chart`，不是拒绝门。

选择器已从结构化 `universal_raw_default_entry_v1` 重放两条 fresh-source
局部候选，并把 `source_tree_scope=fresh_source_tree_only` 写入 source/target state：

| 来源 | 更新 | 势 | F 见证 |
|---|---|---:|---|
| \(p=73\) root anchor | \(1\to51\) | \(1296\to25\) | \((-2,3,-1)\), \(D^-=2,D^+=9\) |
| \(p=409\) universal raw source | \(1\to209\) | \(41616\to199\) | \((-1,0,-2,-1)\), \(D^-=11,D^+=1\) |

二者均为各自 fresh source tree 内的 `candidate_transition`，不是
`verified_edge`：它们的局部 E1--E5 与恒等提升均成立，但 absorbed-support 势
尚未嵌入禁止后续 RESET 的全局 non-resetting phase rank。二者还都满足 \(r=M\)，所以只
是 same-chart 支撑更新，不是 \(k\ge1\) 的真正 r-chart 正控制。\(p+4\) 已有 gap-7 Type II
叶，故 terminal-first 调度会优先终止；这些控制仅验证正规形与来源合同，不增加困难核心
余项覆盖。已有
\(p=409,A=5\) 行还给出 \(5\to1045\)、\(8323\to39\) 的局部算术正控制，但父
charged-support ledger 未经注册 adapter 重放，严格保留 `analysis_evidence`。

值得注意的是，真正的 r-chart 在纯算术层并不受阻。由两个已保存的低载体 determinant
平移 \(M\mapsto M+p,\ n\mapsto n+4d\)，得到：

| \((p,A,M,d,n)\) | source chart | r-chart target | F 见证 | 来源状态 |
|---|---|---|---|---|
| \((73,1,107,22,129)\) | \((R,K)=(299,5457)\) | \(A_C=51,(R_r,K_r)=(95,1734)\), \(1296\to25\) | source \((-1,1,-4)\), target \((-2,3,-1)\) | 缺 source/path/anchor |
| \((409,1,659,200,1289)\) | \((1347,137731)\) | \(A_C=209,(511,52250)\), \(41616\to199\) | source \((-5,-2,-2)\), target \((-1,0,-2,-1)\) | 缺 source/path/anchor |

二者都有 \(k=1\)、\(a=1\mid r\)、canonical target 和严格局部势，但均被 gap-7
Type II 终端抢占。现有 fresh \(A=1\) anchor 的第一载体为
\(M=\operatorname{lcm}(1,Q)=Q<R<p\)，所以发生器不能直接产出上述高载体；
\(p=409,A=5\) 的现有高行 \(M=410,1240\) 又分别因
\(a=5\nmid r=1,13\) 失败。这说明下一步应优先构造并序列化一条真实的
fresh-source 或已收费父状态 \(\to M\ge p\) 路径，并先筛选
\(a\mid r\)（等价的必要过滤是 \(a\mid k\)）；随后才可能把局部势嵌入全局 phase
rank。G 目标仍须补齐分离角色型 E4 verifier。详见
[overflow 的余因子支撑 r-图表候选与同图表正控制](../claims/type-I-overflow-cofactor-r-chart-support.md)。

## 2026-08-05 饱和带权角色的商缺失—核 Fourier 二分

进一步证明：若饱和幂块在选定商中生成子群 \(H\)，源集合像满足
\(\pi(P)H=\pi(P)\)。对目标缺失 \(t\)，若目标在 \(G/\pi^{-1}(H)\) 中仍缺失，
得到严格较小商回执 SATURATED_QUOTIENT_MISS；若商像命中，则目标核截面
\(S_t=\{k:\ tk\in P\}\) 是非空真子集，Parseval 给出
SATURATED_KERNEL_SPLIT。抽象商只有在整数 source-switch、来源标签和势下降均
通过后才具备递归资格；否则记录明确的 LIFT_OBSTRUCTED。主张卡见
[Type II 带权源饱和幂块的严格商缺失—核 Fourier 分派](../claims/type-II-weighted-source-saturated-quotient-kernel-dispatch.md)。

## 2026-08-06 高 \(R\) 两锚点路径与有界单调支撑秩

\(p=1201\) 的两锚点构造现已从纯算术 r-chart 升为带专用来源回放的
source-local candidate。第一锚点把 \(A=1\) 收费为 \(986\)，高
\(R=1839\) raw source 再产生

\[
M=\operatorname{lcm}(986,919)=906134=754p+580,
\]

并经 cofactor 图表把持久化支撑更新为 \(A_C=27608\)。专用回放验证高 \(R\)
source/path、同图表 charged-parent 和 source/target F 纤维；局部 E1--E5 均真，
而输出仍保持 candidate_transition、recursive_edge_eligible=false，因为全局 E5
尚无 non-resetting phase rank。高 \(R\) bundle 的正确门为
\(p\nmid RQ\)，不需要旧的 \(Q<p\)；\(p=73,R=159,Q=79>p\) 是其正向边界例。

对固定高锚点的同 bundle 回返现在已有精确的单次耗尽定理。若第一次 cofactor target
回返原锚点并把 \(A\) 严格升为 \(A_1\)，则第二 carrier 必为
\(\operatorname{lcm}(M,C)\)，仍整除第一次 \(K_M\)，其新 cofactor 已整除
\(A_1\)，不可能再支付第二次严格支撑势。p=1201 的第二轮精确落在该边界：
\[
M_1=25371752,\quad C_1=34,\quad
\frac{27608}{(27608,34)}=812\nmid627.
\]
它不能作为 charged 后继，却给出形式低图表 \((71,21318)\)，并恢复了直接终端
\[
\frac4{1201}=\frac1{561}+\frac1{646}+\frac1{25602918}.
\]
因此 p=1201 本身应 terminal-first 结束；高 \(R\) r-chart 只保留为可复现的
source-local 候选构造。详见
[固定高锚点回返的 complete-excess 单次耗尽](../claims/type-I-fixed-high-anchor-return-one-shot-exhaustion.md)。

新的 [有界单调支撑相位秩](../claims/type-I-bounded-monotone-support-phase-rank.md)
澄清了这个缺口的精确形状：在固定 \(p\) 的递归闭合子图中，只要持久化支撑满足
\(1\le A_S<A_T\le B_p\)，则

\[
H_p=B_p-A
\]

严格下降。它只作用于 absorbed support，故两锚点中的临时
\(M=906134>B_p=360000\) 不构成反例；实际下降为
\(359014\to332392\)。但 p=73 的 \(132\to330\to132\) RESET 重入环和
\(66\to1518>B_{73}\) 的盒外边都显示，此秩不能替代全局调度器。下一项实质工作
因此是证明：每个高 \(R\) r-chart 后的非终端分支要么属于上述一次耗尽并先终端，
要么保留盒内严格增支撑，或转交到另一条已验证的外层秩。固定锚点回返已不值得
反复迭代；下一轮搜索应优先筛选不回返的新锚点或不同 bundle。

同日还补齐了 [Type II 过滤合成列来源槽终端](../claims/type-II-filtered-composition-source-slot-terminal.md)。
它不再要求循环 primary 直和项使用两两不同的素数：固定参数纤维中，只要每个合成列层
\(H_j/H_{j-1}\cong C_{\ell_j}\) 有 \(\ell_j-1\) 个带真实 \(q\)-账本的独立来源槽，
Cauchy--Davenport 归纳即覆盖全部目标群。\(p=3313,D=12\) 的
\(U(12)\cong C_2^2\) 样本以 \(5\) 与 \(7\) 两个物理来源槽命中
\(-1\bmod12\)，并回译为实际 Type II 三单位分数证书。这是一个正向终端回归，
不是困难核心反例。

相反，若同一基积账本下的相对目标缺失，新的过滤层缺口只严格推出某层
\(c_j\le\ell_j-2\)。它把未命中压缩成可检索的来源容量赤字，却不把它误报为
递降或反例；把该赤字转成 Type I/II 终端或全局秩，仍是后续接口。

## 2026-08-06 高 \(R\) non-return 的三相压缩

此前固定锚点的同 bundle 回返已被单次耗尽引理压缩，但这并不排除真正改变
anchor 的 cofactor 图表。本轮得到精确的局部替代：若高 anchor 是

\[
(p,R,K;A),\qquad p<R<4A,\qquad A\mid K,
\]

且 charged cofactor gate 已通过，则

\[
h=\frac{K_r-K}{pA}=\frac{R_r-R}{4A}
\]

只能为 \(0,1,2\)。其中 \(h=0\) 当且仅当回返旧图表；\(h=1,2\) 是严格
non-return，且仍留在高 anchor 区。这把“另一个 r-chart”压缩成两个可枚举相位，
但尚未给出跨 anchor 的良基秩。

三个独立的 source-local 控制例表明该相位不是空的：

| 素数 | 父/源/目标纤维 | non-return | 局部势 | terminal-first |
|---|---|---|---:|---|
| \(3793\) | G \(\to\) F \(\to\) F | \(h=1\), \(7011\to14255\) | \(1984\to992\) | gap-7 Type I |
| \(7393\) | F \(\to\) F \(\to\) F | \(h=1\), \(9863\to19823\) | \(5486\to5\) | gap-7 Type I |
| \(60913\) | G \(\to\) G \(\to\) F | \(h=2\), \(72259\to221435\) | \(49743\to16581\) | gap-7 Type I |

第一行还修正了一个合同实现缺口：同图表 support promotion 的 E4 是
\(\operatorname{Sol}(p)\) 的恒等提升，不应把 G 状态错误排除。对
\(p=3793\)，模 \(19\) Legendre separator 在 \(1811,3671\) 上为正、在
\(-1\) 上为负，给出可验证的 G parent；专用 high-R replay 已同步重算 F 或
Legendre-G 证书。\(p=60913\) 则以 CRT-parity discrete-log character 验证两个 G
状态，并以规范 signed witness 验证 F target。三例都有短终端，因而不能当作未解核心覆盖，但它们否定了
“所有可收费高-R cofactor 必回返”的隐含假设。

令 \(g=(A,C)\)、\(A=ga\)、\(C=gc\)、\(K=AB\)。gate 强制 \(r=at\)，因而
\(ct=B+ph\)；任何正相位都满足 \(c\ge ha+1\)。所以 \(h=1\) 至少使 support
翻倍、\(h=2\) 至少三倍，并且 canonical 余量 \(n=4A-R\) 不减。最小情形
\((h,c,a)=(1,2,1)\) 或 \((2,3,1)\) 自动落回既有 fixed-\(n\) 分支；\(60913\)
正是后者。

进一步，直接 canonical+gate cofactor 链内的正相位已被严格压缩为一次：任意相邻两步
都不可能同时有正 \(h\)，而插入的零相位要么完全停顿，要么将已消费后的 support 推到
\(>p\)，此后正相位 source barrier 排除再次发生。该结论甚至不使用 \(h\le2\) 的上界。
它是局部 `high_nonreturn_token: 1 -> 0`，不是全局 E5：\(p=13\) 的低 chart 链有
连续正相位，说明 high 条件不可删；RESET、重新锚定、same-chart support promotion 和
外部调度也仍在令牌范围外。

零相位也已被精确拆开：\(h=0,c>1\) 时 \(K\) 不变而
\[
\Omega(K/A_T)=\Omega(K/A)-\Omega(c),
\]
故严格支付；\(h=0,c=1\) 才是完整 charged checkpoint 的 macro self-loop。将其在
terminal/alternate 检查后以 capability-aware bundle digest 抑制，并令 \(T\) 记录正相位
是否已消费，则
\[
(T,\Omega(K/A))
\]
在所有非平凡 direct cofactor 宏步上按字典序严格下降。该 phase 的非平凡深度至多
\(2\lfloor\log_2(p-1)\rfloor+1\)。\(p=1201\) 的 \(c=28\) 回返给
\(\Omega:6\to3\)，而 \(p=97\) 给出真实的 \(c=1\) 自环，说明两种情形均不可省略。

这个 exit 接口现已进一步收口。对任一 charged state 定义
\[
\Lambda_p=\left(\left\lfloor\frac{B_p}{A}\right\rfloor,\Omega(K/A)\right).
\]
所有非停顿 direct cofactor 宏步都严格降低它：正相位与盒内严格零相位降低第一坐标，
盒外严格零相位固定 \(K\) 并降低第二坐标。更重要的是，任何已有 E1--E4 且显式
\(\Pi_p(A_T)<\Pi_p(A_S)\) 的外层边都可重置 token、bundle cursor 与 direct epoch；
8 条 fixed-\(n\)/fixed-\(s\) `support_reset_paid` 正属于这一类，不再是未付款的
token exit。\(p=73\) 的只读回放还确认：唯一落到 \(A<p\) 的 paid target 是
\((A,R)=(18,71)\)，仍为低锚点；当前强制 bundle 菜单没有制造实际的正相位重入。

因此现在的缺口更窄：direct cofactor candidate 仍缺逐边 E1--E4/parent-lift 与存在性，
而未付款 forgetful RESET、fresh-root 重用、noncanonical carrier、以及 capability-changing
\(c=1\) action 仍不能进入递归。后者必须由规范有限 action menu、独立 capability
rank 或更高 equation rank 处理；\(p=73\) 的 \(132\to330\to132\) 仍是禁止免费重入的
精确反例。详见
[高锚点 charged r-图表的三相非回返窗口](../claims/type-I-high-anchor-three-phase-nonreturn-window.md)
、[高锚点 direct cofactor 宏步的 token-Omega 良基秩](../claims/type-I-high-anchor-direct-cofactor-lexicographic-rank.md)
、[高锚点 direct cofactor 与外层支撑秩重置的词典序拼接](../claims/type-I-high-anchor-cofactor-outer-rank-composition.md)
和 [高锚点正相位 token 的 canonical checkpoint 传播合同](../claims/type-I-high-anchor-token-canonical-checkpoint-propagation.md)。

## 2026-08-06 高锚宏回放、有限 c=1 菜单与正相位终端边界

上段“缺 E1--E4/parent-lift 与全局 E5”的表述必须按边形状区分。旧 selector 的
\(S\to T\) cofactor receipt 把 transient overflow 当作 source，因而仍只是局部
candidate；但正确的 high-\(R\) 对象是

\[
P\longrightarrow H
\Longrightarrow S
\longrightarrow T,
\]

其中 parent 精确结束于 charged high anchor \(H\)，bundle 从 \(H\) 确定性生成
transient \(S\)，递归候选才是持久的 \(H\to T\) 宏。新的
[宏 E1--E4 准入合同](../claims/type-I-high-anchor-cofactor-macro-e1-e4-admission.md)
显式绑定 \(p\nmid R\)、完整 parent receipt digest、adapter/verifier version、
\(\operatorname{Sol}(p)\) 的 \(T\to H\) 恒等提升，以及 F/G 的 typed fiber
证书。它不放宽旧 `S -> T` registry，也不允许 terminal-first 被绕过。

独立宏回放器现已在两个不同相位上重算完整 E1--E5：\(p=1201\) 的
F-to-F-to-F 零相位给出
\[
\Lambda_{1201}:(365,6)\longmapsto(13,3),
\]
而 \(p=60913\) 的 G-to-G-to-F \(h=2\) 宏给出
\[
\Lambda_{60913}:(49743,1)\longmapsto(16581,3).
\]
这两张是 `verified_macro_replay`，但仍保持 `analysis_evidence`：
它们都有更高优先级的 Type I terminal leaf，且尚未把宏 verifier 注册进统一 selector。
因此结果闭合的是真实宏边的 E1--E5 账本，不扩大困难核心的覆盖计数。

对唯一没有被 \(\Lambda_p\) 数值坐标严格支付的 \(h=0,c=1\) checkpoint，
[有限 action 菜单耗尽合同](../claims/type-I-high-anchor-direct-c1-finite-menu-exhaustion.md)
给出第三坐标
\[
\Xi=\left(\Pi_p(A),\Omega(K/A),\sigma\right),
\qquad
\sigma=\#\{\hbox{冻结但尚未耗尽的 action}\}.
\]
算术标签由 \(u\mid A\)、\(r=(K/A)u\)、\(C=A/u\) 完全分类，至多有
\(\tau(A)\) 个；但 provenance action 只有在 registry、parent、terminal/alternate
菜单和 verifier version 均冻结后才可耗尽。H1 的 complete-excess v1 给出 singleton，
H2 性质则不唯一：\(p=73,R=159\) 有 \(Q_\ast=79\) 与另一 H2 admissible
\(Q'=158\)。\(p=1657\) 进一步显示 partial-excess 可产生不同的 c=1 回返，故不能
静默合并。未证明 action 必须保留为 `UNRESOLVED_ACTION`，不能伪造耗尽。

正相位的短终端路线则被精确限界。写 \(q=h+1\)、\(e=c-q\)，有
\[
c\,d_T=d+pe,\qquad n_T=n+4Ae\equiv1\pmod4.
\]
当 \(e=0\) 时恰是既有 fixed-\(n\) shadow；当 \(e\ge1\) 时 \(n_T>p\)，不能直接
进入 Bradford \(3\bmod4\) gap 或现有偶 dyadic predecessor 接口。\(p=1201\) 的
\(h=1,2\) 算术 normal forms 同时遗漏 gap \(3,7,11,15,19\)，首个 Type I 命中为
gap \(23\)。这否定“正相位本身强迫很小 terminal”的捷径，不构成来源或递归反例。详见
[正相位余量终端接口边界](../claims/type-I-high-anchor-positive-phase-terminal-boundary.md)。

当前不能注册 `high_anchor_cofactor_macro_replay_v1`：它还不是具 terminal-first
dispatch 的 state-to-decision normal form。此前的 `charged_history_only`
\(p=409,A=5\) 行已确认为 noncanonical low-anchor 控制，不能补作 high-macro parent；
若继续研究它，必须另建 noncanonical-low-anchor adapter。任何宏的 \(c=1\) 分支仍须
接入冻结 action 菜单，不能以内容相同的 arithmetic chart 作为跳过 E5/E4 的理由。

## 2026-08-06 高锚宏的可达性 atlas 与最小正相位固定 n pivot

宏回放的两个控制例不能误读为现有递归骨架的覆盖。对冻结 selector 工件递归抽取的
76 个 verified-edge occurrence，只有 51 个是严格的 verified-parent high canonical
anchor（31 个不同 \((p,R,A)\)）。它们都可重放 high-\(R\) complete-excess bundle，
但全部在精确 gate

\[
\frac{A}{(A,C)}\mid r
\]

失败：35 个因 \(a=A/(A,C)>r\) 失败，余下 16 个虽有 \(a\le r\) 但 \(a\nmid r\)。
因此冻结的 verified-parent
atlas 中没有任何可定义持久 \(H\to T\) 的 high-cofactor 宏候选；这是一张有限工件
边界，不是否定新来源的全称定理。更严格地，对其中 13 个具有可付款同图表单调支撑提升的
anchor，49 个 \(A\mid L\mid K,\ A<L\le B_p\) 候选仍全部 gate-fail。它排除了
“先做一条保留旧 charged-support 链的 same-chart promotion 就可救活 gate”的捷径；
非整除的 paid support reset 则须单独考察，不能从这张单调 atlas 推断。

该单独 atlas 现也已完成：31 个高锚中 25 个有非整除 reset，形成 162 个候选、135 个
严格 \(\Pi_p\)-付款 reset。唯一的随后 gate 命中为

\[
(p,R,K;A,L)=(409,511,52250;250,2090),\qquad
\Pi_{409}:166\longrightarrow19,
\]

其 bundle 满足 \(Q=51,M=106590,C=209,r=250\)，但 cofactor target 恰回到
reset 后的 \((409,511,52250;2090)\)，即 \(h=0\) exact self-loop。故这张有限 atlas
没有给出 gate-rescue 后的第二条严格 direct cofactor 推进；它既不排除新来源，也不能只靠
补 E1--E5 把现有唯一命中变成递归边。

这也澄清了此前 \(p=409,A=5\) 的 charged_history_only 控制：其

\[
(R,K;A)=(251,25665;5)
\]

不是 \(A=5\) 的 canonical chart（后者是 \((11,1125)\)），且低于 high-anchor
窗口。它既不能拿来补 high macro 的 parent，也不能由一条以其为 source 的 fixed-\(n\)
edge 倒推 predecessor。若要继续研究该行，需要一个独立的 noncanonical-low-anchor
adapter，而不是放宽当前 high-anchor 或 generic \(S\to T\) verifier。

另一方面，最小正相位现在不再只是没有出口的 fixed-\(n\) shadow。完整 direct
\(r\)-chart 条件 \(1\le r,C<p\) 下，若 \(h\in\{1,2\}\)、
\(e=c-(h+1)=0\)，则

\[
5\le n\le p-4,\qquad d_T\ge2,\qquad
L=A_Td_T=\frac{pn-1}{4}
\]

强制给出 fixed-\(n\) bounded-divisor pivot，且

\[
\Pi_p(L)<\Pi_p(A_T),\qquad
R_L=(p-1)n-1>p.
\]

所以一旦 \(T\) 已带 terminal-first 后的完整 E1--E4 receipt，第二段是已有的严格
付费后继。这里 \(C<p\) 不可省略：\(p=73,A=82,h=1,C=164\) 的形式 high chart 有
\(d_T=1\)，恰好破坏严格 pivot。该桥补的是最小正相位的后继算术，不补第一段宏的
parent、typed lift 或 dispatcher。

full-excess gate 现在有可反向使用的精确构造目标。若
\[
a=\frac{A}{(A,C)},\qquad M=kp+r,\quad0<r<p,
\]
则
\[
a\mid r\quad\Longleftrightarrow\quad a\mid k.
\]
特别地，当 \(qA<p\) 时，
\[
C=qA\quad\Longleftrightarrow\quad4qAM\equiv1\pmod p,
\]
并自动有 \(a=1\) 与 gate 通过。\(p=3793,q=2\) 和 \(p=60913,q=3\) 是冻结控制；
这是新来源的可检索算术设计模板，不补 parent provenance、local F/G、terminal-first
或宏闭包。

这个模板现可进一步反向化。写 \(K=AB\)、\(Q\) 为 complete-excess、并令
\(t=Q/(A,Q)\)，则 \(M=At\)，且 \(C=qA\) 等价于

\[
4qA^2t\equiv1\pmod p
\quad\Longleftrightarrow\quad
qAt\equiv B\pmod p.
\]

严格 support growth 时 high window 强制 \(q\in\{2,3\}\)。若 \(B\equiv1\pmod q\)，
automatic target 的相位恰为 \(h=q-1\)，故 \(q=2,3\) 分别自动接入已知的
\(h=1,2,e=0\) fixed-\(n\) pivot 算术。更窄的 \(Q=R-1,(A,R-1)=1\) 子族中，令
\(R=p+\delta\)，则

\[
\delta\equiv1+(4qA^2)^{-1}\pmod p
\]

在 \(0<\delta<4A-p\) 的 high window 内至多有一个候选；只需再检查
\(4A\mid p(p+\delta)+1\)、complete-excess 和互素条件。两条控制均满足这一模板，
但都有 terminal-first Type I 叶。这里的互素条件只定义一个方便的充分子族；完整
excess 的正确判据是逐素数幂严格超过 \((p+1)/2\) 的赋值，不能误收紧为互素。

fresh root 的入口也已被固定。若一个 core root 的第一次 complete-excess rechart 已进入
高锚，写 \(R_0-1=A\beta_0\)，则 \(\beta_0\in\{1,2\}\)。第一根型
\(\beta_0=1\) 强制高锚 \(R\equiv7\pmod8\)，故不可能有第二 bundle
\(Q_1=R-1\)；two-anchor automatic-q 来源必须从 \(\beta_0=2\) 开始。后者仍非充分：
\(p=97,A=39\) 是高锚但 \(Q_1=59\ne118\)。第二 bundle 的精确门是
\[
Q_1=R-1
\quad\Longleftrightarrow\quad
R\equiv3\pmod8,\quad
\ell^e\parallel(R-1)/2\Longrightarrow e>\nu_\ell((p+1)/2)
\]
对每个奇素数幂 \(\ell^e\) 成立；\(p=409\) 和 \(p=1033\) 的共享奇因子控制证明互素不是
必要条件。两条 automatic-q 控制又都在 \(p\equiv97\pmod{168}\)，所以可由固定的
gap-7 Type II prefix 直接抢占。这把“找新来源”收缩为定向的、带 terminal-prefix
预筛的因子条件，不是已有的全称存在性定理。

reset 的唯一命中也已有精确归因。对 gate-pass reset 写
\(L=ga,C=gc,r=au,K=LB\)，则 target support 为 \(Lc\)，
\[
h=(uc-B)/p.
\]
exact reset-state self-loop 当且仅当 \(C\mid L\)。所以 \(p=409\) 的命中是
\(c=1\) 的特殊子情形；固定 \(p=1201\) 的 \(560\to986\) 非整除、严格付款
chart-return 控制有 \(h=0,c=28\) 和 target support \(27608\)，明确排除了
“gate 命中必为 reset-state 自环”的误读。

另有 11 条 `overflow_same_chart_support_promotion_v1` high parent 已被包装为
content-addressed、有限 scope 的 parent envelope；v2 replay 还将每一张 envelope 与输入
工件 SHA-256 和原 receipt digest 重新绑定，并拒绝篡改。所有 11 条仍 gate-fail，且没有
local H/S/T fiber 或 priority receipt，所以注册 selector edge 与完整 macro E4 的数量都为零。

最后，宏即使 E1--E5 全真，也必须先具备 version/hash 绑定的 terminal-first priority
prefix：持久 anchor \(H\) 与 transient \(S\) 都要无更高优先输出，\(T\) 只能以
pending_dispatch 入队并在扩展前重新经过同一菜单。当前 selector 仍是静态结果汇编，
不能只修改 recursive_edge_eligible。\(p=3793\) 与 \(p=60913\) 已有 fresh-root
到 automatic gate 高锚的专用控制链，但均被 terminal-first 叶正确抢占，且已明确命中
gap-7 Type II prefix。因此下一项主工作是构造满足以下**全部**条件的新来源：
\(\beta_0=2\)、第二锚 strict-valuation full-excess、automatic-q high-window、未命中
已记录的有限 terminal prefix，并同时完成 parent API、typed lift、priority guard 和 E5。
prefix miss 只是必要初筛，不可被误报为非终端。若研究 reset，则必须先得到非自环、严格
付款的 gate 命中，再讨论 reset 的完整合同。
