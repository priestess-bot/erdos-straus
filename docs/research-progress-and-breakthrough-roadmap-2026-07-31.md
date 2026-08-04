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
   规范限制到商群角色，阈值分母由 \(|H|-1\) 改为 \(|H/P|-1\)。真实核心
   \((193,63,3040)\) 的聚焦回执给出 \(|P|=6\)、\(|H/P|=6\)，商谱最大幅度
   \(2\sqrt3\)，并核验了每个固定目标的计数恒等式。这是状态内精确约化，不是
   跨状态容量定理；下一步要把商角色阶、幅度和相位分子转成 overflow 的带符号载体
   需求。

   该回执已按统一状态合同登记为
   `certificate_type=fixed_layer_quotient_fourier`、`selector_status=analysis_evidence`、
   `recursive_edge_eligible=false`；幅度以精确平方范数 `12` 保存，而不是用浮点值承担
   证据。这样可以把表示、对偶和容量字段放进同一状态记录，同时保留“对偶证书不是
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

主张卡：[高载体 n=p G-anchor bundle 的精确相位二分](../claims/type-I-overflow-high-carrier-n-prime-g-anchor-phase.md)。
