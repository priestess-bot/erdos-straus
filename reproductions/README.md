# 小尺度复现

`esc_reproduce.py` 用精确整数算术复现四个可独立检查的环节：

1. 三个经典约化恒等式；
2. `S_5`、`S_7` 与 `p = 1 mod 24` 合并后模 840 的六个残余类；
3. 固定首分母后的完整因子对证书 `(ay-b)(az-b)=b^2`；
4. Bradford 2025 的 Type I/II 除子同余到显式分母的对应。

运行：

```bash
python3 reproductions/esc_reproduce.py
python3 -m unittest discover -s tests -v
```

生成的 `results.json` 记录运行范围和脚本 SHA-256。它是有限范围的交叉核对，
不是 Salez `10^17` 或 Mihnea–Dumitru `10^18` 搜索的全量复现。

两个无扫描的线性 escape 夹具分别固定重复 \(q\) 的 shared-ledger/raw 回退边界，以及
固定 \(D\) canonical 菜单的残余范围边界。运行：

```bash
python3 reproductions/type_i_linear_escape_primary_source_switch_fixture.py --verify
python3 reproductions/type_i_linear_escape_canonical_d_lattice_fixture.py --verify
python3 reproductions/type_i_linear_escape_divisor_stratified_source_fixture.py --verify
python3 reproductions/type_i_g_anchor_jacobi_raw_terminal_source_switch_fixture.py --verify
python3 reproductions/type_i_linear_escape_primary_factor_donly_no_conductor_fixture.py --verify
```

前者对应 `type-I-linear-escape-primary-source-switch-finite-dispatch`，后者对应
`type-I-linear-escape-canonical-d-lattice-source-menu`，第三个对应
`type-I-linear-escape-divisor-stratified-recursive-source-closure`，第四个对应 G-anchor
raw terminal/source-switch 退化的
`type-I-g-anchor-jacobi-raw-terminal-source-switch-bridge`，第五个对应
`type-I-linear-escape-primary-factor-donly-no-conductor`；它们只复现声明中的精确例子，
不执行历史范围扫描。

余因子支撑 r-图表分支由 `type_i_representation_dual_capacity_selector.py` 的
`overflow_cofactor_r_chart_support` 键重放。它只检查三条已保存的 source/path
回执：两个 `universal_raw_default_entry_v1` 的 fresh-source local
`candidate_transition` 控制与一个父 charged-support ledger 缺失边界，不执行
范围搜索。前两条仅有 same-chart \(r=M\)；在全局 non-resetting phase rank 建立前，它们
不递归。

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

对应主张为 `type-I-overflow-cofactor-r-chart-support`。默认入口仅能建立新鲜
source tree，不能从已收费状态重置支撑；其 `source_tree_scope` 必须随状态传播。

高 (R) cofactor 的专用 non-return 控制例不运行范围扫描：(p=3793) 验证
Legendre-G 父状态可经同图表支撑升级收费，(p=7393) 则验证独立的 F-to-F
\(h=1\) 非回返路径，(p=60913) 验证 CRT-parity G-to-G-to-F 的最小
\(h=2\) 路径。三者都有独立 Type I terminal，故只用于检验来源、F/G
证书、相位支付与局部势，不是困难余项覆盖。

```bash
python3 reproductions/type_i_high_r_chart_p3793_audit.py --verify
python3 reproductions/type_i_high_r_chart_7393_nonreturn.py --verify
python3 reproductions/type_i_high_r_chart_60913_h2_nonreturn.py --verify
```

`type_i_high_anchor_token_exit_p73_reentry.py` 是更小的只读拼接检查：它不运行 selector，
只从冻结回执抽取已付款的外层边，重算
\(\Lambda_p=(\lfloor B_p/A\rfloor,\Omega(K/A))\)，并检查 \(p=73\) 的 paid exit、
forced high-bundle 与 forgetful-RESET 边界。它对应
`type-I-high-anchor-cofactor-outer-rank-composition`，用于验证“只有严格
\(\Pi_p\) 付款的 token exit 才能开启新 epoch”，不作为范围覆盖实验。

```bash
python3 reproductions/type_i_high_anchor_token_exit_p73_reentry.py --verify
```

`type_i_high_anchor_direct_c1_finite_menu_exhaustion.py` 是另一张更小的整数夹具，
只重放 (p=97) 的实际 (c=1) 自环、(p=1657) 的 full/partial-excess 分界，及
(p=73,R=159) 的 H1/H2 非唯一边界。它不运行 selector；其用途是固定
`type-I-high-anchor-direct-c1-finite-menu-exhaustion` 的两个接口：
算术 \(u\mid A\) 标签的充要条件，以及只有冻结且完整检查的 action 才能记入
`STUTTER_EXHAUSTED`。H1/v1 的 complete-excess 菜单是 singleton，H2 或 partial
bundle 不是自动可耗尽的 action。

```bash
python3 reproductions/type_i_high_anchor_direct_c1_finite_menu_exhaustion.py --verify
```

`type_i_overflow_d_one_p_adic_regeneration_countdown.py` 只核验六个固定的完整乘积
\(d=1\) 正规形。它重算 canonical target capacity、一次与两次再生、
\(\nu_p(E-1)\) 每步恰减一，以及倒计时末端分别落入 raw-source 和 \(p\)-free 门失败的
两个 sharp 控制；不搜索素数、分母或 selector history，也不把算术链升级为已注册边。

```bash
python3 reproductions/type_i_overflow_d_one_p_adic_regeneration_countdown.py --verify
```

`type_i_chart_least_coprime_prime_anchor_source.py` 固定核验两个 \(d=1\) raw-
\(p\) 失败图表，重算最小 \(q\nmid RK\) 素数的一步 primitive source 和严格容量出口。
`type_i_overflow_d_one_p_block_peeling_obstruction.py` 则固定核验两个 \(p\)-free 失败图表，
逐步重放 \(p\)-block peeling，并验证删块后的算术 rechart 严格缺少
complete-excess residual-divisibility 来源。二者都不扫描历史 selector。

```bash
python3 reproductions/type_i_chart_least_coprime_prime_anchor_source.py --verify
python3 reproductions/type_i_overflow_d_one_p_block_peeling_obstruction.py --verify
```

`type_i_high_anchor_cofactor_macro_replay.py` 用正确的
`parent -> H -> transient S -> T` 形状回放 high-cofactor 宏，而不把 transient
overflow 错当作 parent 的直接 successor。它对 \(p=1201\) 的 F-F-F \(h=0\) 和
\(p=60913\) 的 G-G-F \(h=2\) 分别重算 E1--E5，并按持久 \(H\to T\) 边计算
\(\Lambda_p\)。两例都保留 `analysis_evidence` 与 terminal-first 叶，不注册到统一
selector。

```bash
python3 reproductions/type_i_high_anchor_cofactor_macro_replay.py --verify
```

`type_i_high_anchor_full_excess_gate_template.py` 只重放三个固定 high-R 控制例的
full-excess carrier。它固定余因子 gate 的两个等价形式：
\(A/\gcd(A,C)\mid\lfloor M/p\rfloor\) 与一个短剩余窗口；并验证
\(C=qA\) 的单同余自动通过子族，以及 \(p=1201\) 的同图表 return 除子模板。
它不扫描素数、不读取 selector/history，也不把算术命中升级为 E1--E5 边。

```bash
python3 reproductions/type_i_high_anchor_full_excess_gate_template.py --verify
```

type_i_high_anchor_automatic_q_source_template.py 将 automatic \(C=qA\) 子族反向成
complete-excess 商 \(t=Q/(A,Q)\) 的单一剩余条件。它只回放
\(p=3793,q=2\)、\(p=60913,q=3\) 两个 terminal-preempted 控制、七个指定
fresh-root 边界和一个 q-choice 近失。它验证 \(q\in\{2,3\}\)、最小正相位指纹、
root \(\beta_0\in\{1,2\}\)、\(\beta_0=1\) 对第二 full-excess 的 \(2\)-adic no-go，
以及 \(Q=R-1\) 所需的严格赋值而非互素判据；它还重建一个有限 gap-7 Type II
terminal prefix。它不扫描素数或注册 selector 边。

```bash
python3 reproductions/type_i_high_anchor_automatic_q_source_template.py --verify
```

`type_i_high_anchor_positive_phase_terminal_boundary.py` 是正相位的两个算术夹具：
它验证 \(e=0\) 的 fixed-\(n\) shadow、\(e\ge1\) 的盒外余量，以及 \(p=1201\)
在 gap \(3,7,11,15,19\) 的完整 miss 与 gap \(23\) 的首个 Type I 命中。它不提供
source/path、F/G 或 E1--E5 provenance。

```bash
python3 reproductions/type_i_high_anchor_positive_phase_terminal_boundary.py --verify
```

type_i_high_anchor_minimal_phase_fixed_n_bridge.py 只重放最小正相位 \(e=0\) 的
fixed-\(n\) 后继桥：在完整 \(1\le r,C<p\) 范围内，它强制
\(5\le n\le p-4\)、\(d_T\ge2\)，并把 \(L=A_Td_T\) 送入严格
\(\Pi_p\)-paid bounded-divisor pivot。四个夹具都只验证该第二段算术；它们不补
parent、terminal-first 或 global macro admission。脚本还保留 \(p=73,C>p\) 的
排除控制，避免删去 direct-chart 范围后误报严格 pivot。

```bash
python3 reproductions/type_i_high_anchor_minimal_phase_fixed_n_bridge.py --verify
```

type_i_high_anchor_parent_atlas.py 和
type_i_high_anchor_same_chart_gate_engineering.py 都只读取冻结 selector artifact。
前者提取 51 个严格 verified-parent 高锚并重放 bundle，确认没有一条通过 cofactor gate；
后者再枚举保留 \(A\mid L\) 的 49 条 \(\Pi_p\)-paid same-chart 提升，仍无 gate rescue。
它们是有限来源边界，不执行 selector/history，也不排除非整除 support reset。

```bash
python3 reproductions/type_i_high_anchor_parent_atlas.py --verify
python3 reproductions/type_i_high_anchor_same_chart_gate_engineering.py --verify
```

type_i_high_anchor_frozen_same_chart_parent_envelope.py 对其中 11 条
overflow_same_chart_support_promotion_v1 high parent 建立 content-addressed 的有限
artifact scope，并重放 source/successor、determinant、同图表提升、势下降和
\(\operatorname{Sol}(p)\) 标记。它还检查篡改会破坏 successor content hash；结果仍是
analysis_evidence，因为没有 local H/S/T fiber、terminal-first 或 selector 注册。

```bash
python3 reproductions/type_i_high_anchor_frozen_same_chart_parent_envelope.py --verify
```

`type_i_high_anchor_nonmonotone_reset_gate.py` 补上同图表但不保留
\(A\mid L\) 的有限 reset 域。冻结的 31 个高锚给出 162 个候选、135 个严格
\(\Pi_p\)-paid reset；唯一通过随后 cofactor gate 的行是 \(p=409,A=250,L=2090\)，
但 target 精确回到 reset 后状态，故按 direct action 规则是应抑制的 \(h=0\) 自环。
脚本还验证 gate-pass 情形的 \(L=ga,C=gc,r=au\) 相位分解：exact state self-loop
当且仅当 \(C\mid L\)。指定的 \(p=1201\) 控制是 \(h=0\) chart return、但 \(c=28\)
的非自环边界。脚本把算术命中与所缺的 E1--E4 parent/reset 合同分开输出，不运行
selector/history。

```bash
python3 reproductions/type_i_high_anchor_nonmonotone_reset_gate.py --verify
```

`short_certificate.py` 按递增首分母缺口搜索精确 Bradford Type I/II 证书。
它还实现 \(n=(3p+1)/4\) 的显式标记递降：若 \(n\) 有 \(2\pmod3\) 素因子，
则可把 \(4/n\) 的一个显式解提升至 \(4/p\)，并同时恢复平方根级 Type I 证书。
其中 `even_source_distance_descent_witness` 精确枚举以 \(p-c\)（正奇数 \(c\)）
为源的完整平移平方尾：它把每个允许平移降为一个 \(M_1^2\) 因子的单同余测试，并
返回严格提升及其 Type I 证书。源 \(p-c\) 是严格更小的偶数；旧的
`p_minus_one_source_descent_witness` 保留为 \(c=1\) 的兼容入口。
`external_source.py` 先用 `m=3`、`(p+1)/2`、`p+4`、`4p+1` 四条已证分支过滤，
再以 `m | p+i` 与 `4i | p+m` 搜索外部源 Type I 证书；`--source-limit` 仅是有限
实验窗口，不能解释为全体素数的统一界。

`fct_type_i_equivalence.py` 把三项 ceiling-FCT 的递推系数
`(c0,c1,c2)` 与同一外部源证书逐项双向恢复：其缺口为 `c2`，除子为 `c0*x`。
默认盒在 76 个核心素数和 source 至多 32 的条件下完整复核 386 个外部 source 见证。
它只核对 FCT 的确定性构造等价，不把文献中的独立性随机模型或有限 source 结果当作
逐点覆盖定理；见 `fct-three-term-type-I-equivalence`。

同一外部源见证还可唯一写成 \(rp+1=4qt\)、\(r\equiv3\pmod4\)、
\(q\equiv-1\pmod r\)，并恢复 \(i=(q+1)/r\)。`external_source.py` 提供双向
正规形检查；见 `type-I-rp-plus-one-external-factor-ray`。这给出缺口至多
\((p-1)/4\) 的变量因子 Type I 射线，不把有限 source 窗口误作统一界。

`type_i_root_capacity_strict_carry_complement_even_source_gate.py` 把 strict root
cofactor 规范地变成一个偶数小源 `n<p`，并只重算三条固定控制：高半区的显式
standard-even marked lift，以及 `p=73,r=3`、`p=313,r=271` 两条 actual strict-root
receipt。它验证低/中/高三分、高半区的单一 divisor-residue gate，以及 strict
cofactor 本身并不强制该 gate 或 odd-distance ray；不扫描 root 参数、素数或历史 selector。

`type_i_root_capacity_strict_carry_complement_tail_bezout_character_gate.py` 把同一
receipt multiplier `E` 归一化成 high-tail modulus 上的 Bezout 单位，并固定核对
`p=73,r=3` 的 Legendre no-go 与 `p=313,r=271` 的模 293 指数盒失败。它证明二次
character 可消去一部分 tail selector，却不能单独强制剩余 high-half gate；不做范围扫描。

`adaptive_external_escape.py` 专门审计自适应外部源递降的未命中实例：它为每个
逃逸素数列出全部允许 \(k\)、源分母的素因子残数、有限 source 窗口中的直接外部源
正规形，以及有界 Type II \(AC\) 射线证书。这个报告区分“没有该递降边”和
“没有直接证书”，不把后者从有限窗口外推为全称结论。

`targeted_descent_bridge.py` 固定一张直接证书的目标三元组，反向枚举所有保留其中
两项的严格源提升。它用于区分“有直接证书”与“该证书可直接桥接为二分母保留递降”；
空输出只排除后一种特定桥接，不排除其它递降。

`cyclic_reciprocal_lift.py` 审计最小的三坐标耦合候选：循环地将每对源倒数平均后按
\(n/p\) 缩放。该式在实数层面恒等地保持 \(4/n\mapsto4/p\)，但
`cyclic-reciprocal-transport-obstruction` 证明其三个整数分母条件对任何核心素数
不相容。它还实现任意既约循环权重；同一张卡片证明这种权重即使放宽，也无法从无条件
偶数标准源获得核心目标。脚本只作有限交叉核对，避免把证明中的整性链条实现错位。

`weighted_cyclic_repeated_tail_audit.py` 则越过标准源，固定最小显式非标准族
\(n=4k-2,\ (k,nk,nk)\)，把任意加权循环的整性压缩为两条一次整除。默认结果在
\(p\le5000\)、权重分母至多 50 的 36,181,038 个候选中均无核心命中；见
`weighted-cyclic-repeated-tail-boundary`。这是下一类带因子标记源的有限负例基准，
不是权重或源解的全称障碍。

`weighted_cyclic_complete_repeated_tail_audit.py` 则把该源形状完整化：任一
`(a,b,b)` 源在目标中间分母为整数时必有 \(b=nk\)，最小可行 \(n\) 由 \(k\) 的奇偶
精确决定。该完整审计在同一盒内给出 \(p=2161\) 的唯一无向命中；它恰重建
Type II \((m,d)=(47,12)\)，所以应读作标记证书重参数化而不是新递降。见
`weighted-cyclic-complete-repeated-tail-audit`。

`weighted_cyclic_reverse_bridge.py` 固定一个目标和既约循环权重后，以精确逆矩阵
恢复所有可能反向源倒数的有理轮廓；分子最小公倍数直接判定是否存在 \(2\le n<p\) 的
整数源。默认审计首个共同递降逃逸点 \(p=2451289\) 的全部 21 张 \(A,C\le14\) Type II
目标，以及全部 \(s\le20\) 权重，结果为空。它允许三个目标分母同时变化，故比二尾保留
桥接更宽；但仍只排除固定有限目标盒内的零偏移循环传输，见
`weighted-cyclic-reverse-bridge-boundary`。

`doubly_stochastic_reverse_bridge.py` 再把循环权重扩至约化、可逆且真正混合的
\(3\times3\) 双随机矩阵。固定矩阵的伴随逆和分子最小公倍数仍完整决定全部严格源。
默认审计 \(p=2451289\) 的同一 21 张目标，穷尽分母 \(2\) 至 \(10\) 的 5,082 个矩阵及
106,722 个目标/矩阵逆像，结果为空；这排除低复杂度非循环线性混合，不涉及高分母、
偏移或非线性状态，见 `doubly-stochastic-reverse-bridge-boundary`。

`type_ii_tail_deflation_audit.py` 审计另一种严格标记桥：对 Type II 证书，若
`m+1\mid p-1`，则同时从两条含 `p` 尾分母中去掉 `p`，得到源
`n=(p+m)/(m+1)<p`。候选缺口只来自 `p-1` 的因子。当前三百万范围审计显示，
此前自适应递降审计留下的全部 215 个机制逃逸点都被该桥覆盖；这是有限交叉核对，
不是全体素数的因子选择定理。这个桥要求源端有指定首分母的解，见
`type-II-scaled-tail-marked-lift-equivalence`；所以结果应读作带标记 Type II
证书选择，不能当作从任意较小实例开始的递归证明。

`type_ii_tail_deflation_full_audit.py` 则不预先筛选逃逸点，而是逐个扫描有限范围内
所有核心素数的 `p-1` 因子标记缺口。它保存每个最小命中的 gap、记录保持者和全部
遗漏的因子分解及普通证书，专门用于研究这个选择器的真实失败模式；当前百万范围结果
见 `type-II-tail-deflation-selector-audit`。

`type_ii_scaled_first_tail_deflation_audit.py` 放宽双尾桥的“首分母不变”限制：
源三元组 `(kx,Y,Z)` 提升为 `(x,pY,pZ)`。整性判据是
`km+1\mid kp-1`，且仍严格降低源分母。它当前在
`k<=2000,m<=20000` 的盒内覆盖三百万范围一阶选择器留下的全部 41 点；见
`type-II-scaled-first-tail-deflation` 与
`type-II-scaled-first-tail-deflation-audit`。该提升是带标记双射，不声称能提升
任意源解；这项审计也不声称固定参数盒全局充分。

`type_ii_scaled_first_ac_boundary.py` 在同一 41 点上反向检验一个常见误推：
它穷举 `A,C<=14`、可变 `K` 的全部原始 Type II 射线，并对每张证书枚举
`p+m` 的共享因子。30 点命中、11 点保留，故“小 AC 直接证书”不足以自动给出
共享因子递降；见 `type-II-scaled-first-bounded-ac-boundary`。

`type_ii_shared_divisor_full_audit.py` 则直接对全部核心素数运行有界缺口、无界首尺度
的共享因子扇：对每个 `m` 它枚举 `p+m` 的全部因子，因此不会人为截断 `k`。
当前 `m<=239` 的扇在一千万内覆盖全部核心素数，但所需 `k` 可达 664185；见
`type-II-shared-divisor-fan-audit`。这是一项强有限带标记证书审计，不是固定扇的
全称证明或无标记递降。

共享因子扇的全称目标现明确为 `type-II-shared-residue-selector-conjecture`：
在同一缺口 \(m\) 上，要求 \(4x=p+m\) 有非平凡 \(1\pmod m\) 因子，且 \(x^2\)
有 \(-x\pmod m\) 除子。后者直接给出 Type II 证书；前者只提供额外的带标记表示，
不被当作无标记递降。

`type_ii_automatic_residual_k1_funnel.py` 给出该目标的有限压力集：四个自动缺口后的
残余先由 \(k=1\) 选择器过滤，再以全部 \(m\le239\) 的无界首尺度扫描记录剩余共享
证书。加入 `--single-prime-profile` 可完整检查仅依赖 \(q\equiv1\pmod m\) 的单素因子
选择；加入 `--prime-power-profile` 则进一步检查所有 \(q^e\mid p+m\)。后一审计在
千万范围留下 74 个没有单素数幂证书的主残余，故其共享因子必有至少两个不同素因子；
见 `type-II-shared-prime-power-selection-boundary`。加入 `--support-profile` 会在
全部共享证书中最小化不同素因子数；其千万范围直方图为 \(1:10,2:54,3:18,4:2\)，
从而明确排除固定两素或三素选择，见
`type-II-shared-bounded-support-selection-boundary`。
`--totient-threshold-profile` 则执行一个可证明的单位群前缀积充分条件：若与缺口
\(m\) 互素的素因子重数至少为 \(\varphi(m)\)，便构造一个 \(1\pmod m\) 的共享
除子。这个条件在千万范围的 84 个压力点中无一命中，见
`type-II-shared-totient-threshold-lemma`；它因此是可用的正向引理，而非当前主残余的
覆盖机制。
`--subgroup-threshold-profile` 把该阈值收缩为实际单位因子残数生成子群的阶，仍由
前缀积构造共享除子。这个更强阈值在同一千万范围压力集也无一命中，见
`type-II-shared-subgroup-threshold-lemma`，所以接下来的研究必须分析短零积或跨缺口
结构。
`--factor-length-profile` 则在全部共享证书中最小化 \(\Omega(D)\)，即达到
\(1\pmod m\) 所需的最短零积长度。100M 审计出现长度 7 的必要例子，故六因子
选择器已被排除，见 `type-II-shared-six-factor-profile-boundary`。
`type_ii_shared_gap_escape.py` 对单个核心素数作完整可变缺口扫描；其
\(p=33011449,\ m\le500000\) 空结果见
`type-II-shared-half-million-gap-escape-boundary`。

`type_ii_moving_window_collision.py` 则处理不带共享标记的直接 Type II 窗口：
连续 \(x_j\) 的公共因子只能来自窗口差值的有限素数集，剥离后私有余因子两两互素，
并逐项核验碰撞/私有除子残数积集分解。记录失败点
\(p=153633769,\ j\le31\) 的输出见
`type-II-moving-window-finite-collision-reduction`。

`type_ii_moving_window_conditional_escape.py` 在同一记录点上测试更窄的一私有素因子
模型：把每个 \(x_j\) 写成窗口模数强制因子乘一个仿射余因子，并递归剥离局部覆盖素数。
它给出 \(j\le37\) 的可采纳分支；在 Dickson/Schinzel 型素数元组假设下，该分支产生
无穷多个逃过这 37 个直接 Type II 位置的核心素数。它只排除固定窗口的这类证明模型，
不构成原猜想的条件性反例，见
`type-II-moving-window-one-private-prime-conditional-escape`。

`column_stochastic_reverse_bridge.py` 枚举低分母、可逆、真正混合的三坐标列随机
线性传输。列和为一已足以保持倒数和，因而该盒严格大于双随机传输盒；固定 Type II
目标后，伴随矩阵逆像和分子最小公倍数精确决定所有严格整数源。对
(p=2451289)、(A,C\le14) 的 21 张目标，分母至多 6 的 13,026 个矩阵均无严格源，
见 `column-stochastic-reverse-bridge-boundary`。这排除的是低复杂度零偏移线性桥，
不排除带标记、偏移或非线性递降。

`type_ii_moving_window_adaptive_escape.py` 从该 \(j\le37\) 状态逐个加入新缺口，
在每一步重算全部固定因子、Type II 除子残数和线性式局部可采纳性。确定性首选分支延展
到 \(j\le51\)，随后由 \(m=207\) 的显式证书闭合。这个证书对整个起始算术进程
无条件成立，并非仅是模型或深度搜索边界。
见 `type-II-moving-window-adaptive-one-private-prime-conditional-escape`。

`type_ii_gap_207_progression_certificate.py` 单独核对上述进程闭合：
\(x=(p+207)/4\) 恒被 \(9682\) 整除，且 \(d=47x/9682\) 是缺口 207 的直接
Type II 除子。见 `type-II-gap-207-progression-certificate`。

`type_ii_progression_trap.py` 将这一步推广为固定因子进程陷阱的完整有限搜索：
若未来缺口冻结 \(x/E\) 的残数，且 \(E\) 的某个因子命中 Type II 目标，即输出整条
进程的直接证书。它既复现 \(p_0=153633769,J=31\) 的缺口 207，也记录了第二种子
的缺口 143 例子。`--all-divisors` 模式穷尽全部可能的缺口因子；对
\(p_0=8803369,J=20\) 的 3,929 个候选全部失败，见
`type-II-fixed-factor-progression-trap`。

`type_ii_hybrid_window_descent_audit.py` 将固定窗口、完整进程陷阱和严格平方因子
外部源递降并列审计。千万范围的 \(J=20\) 唯一窗口残余 \(p=8803369\) 虽无陷阱，
却有显式严格递降；见 `type-II-window-descent-hybrid-10m`。

`shared_residue_fixed_gap_boundary.py` 固定核心素数 \(p=73\) 与合法缺口 \(m=47\)，
精确枚举 \(x^2\) 和 \(4x\) 的全部除子残数，验证两个共享选择器目标同时失败。这不是
选择器猜想的反例，因为可选择其它缺口；它是单缺口群论增长路线的边界，要求后续证明
使用跨缺口选择或不同移位 \(p+m\) 的关联。

`type_ii_small_shared_gap_fan.py` 将前三个缺口 \(m=3,7,11\) 的共享因子分别固定为
\(4,8,12\)，并对其显式 Type II 子扇作精确审计。它同时输出这个子扇未命中的
因子与同余残余；这些点仍可能由同一缺口的非平凡除子或更大缺口捕获，因此不应视作
选择器失败。

`type_ii_factor.py` 在同一直接族残余中搜索 Type II 因子生成器
`4ACK-1 | Kp+A`，并按最小 `max(A,C,K)` 报告参数盒记录。固定有限参数盒会被
无穷核心素数避开，因此完整窗口只是一项有限审计。

`type_ii_ac_ray.py` 则固定 \(A,C\) 的半径、但不限制 \(K\)。它因子分解
\(p+4A^2C\)，从每个 \(h\equiv-1\pmod{4AC}\) 的因子恢复
\(K=(h+1)/(4AC)\)，再验证完整 Type II 证书。这避开了“固定三参数模板”的直接
障碍，却仍只是对有限 \(A,C\) 盒和有限素数范围的审计。
最新的半径 \(14\) 输出覆盖全部 \(p\le5\cdot10^8\) 的 \(3{,}292{,}848\) 个核心素数；
详见 `type-ii-ac-ray-500m-bound14-results.json`，不能外推为全称界。

`type_ii_canonical_ray.py` 把每个共同移位 \(s=A^2C\) 唯一改写为
\(s=a_0^2c_0\)（\(c_0\) 平方自由）。规范模数 \(4a_0c_0\) 整除同一移位下所有
原始模数，故在 \(p\ge4s\) 时规范射线吸收任意原始成功见证。它将半径 14 的
196 条原始射线压缩为 169 条不同移位的规范射线，并输出一维小移位骨架及其有限贪心
补集；详见 `type-II-canonical-squarefree-ray-dominance`。这是参数冗余消除和有限
诊断，不是新的全称覆盖结论。

`type_ii_multishift_collision.py` 针对有限规范移位扇，把每个 \(p+4s\) 的因子
分为有限差值所允许的碰撞素数与两两互素的私有余因子。它逐项验证完整除子残数集是
这两部分的集合乘积，并把失败改写为私有残数避开有限目标集；当前输出审计
\(s=1,\ldots,14\) 的共同残余。见
`type-II-multishift-finite-collision-reduction`。该工具隔离跨移位耦合的位置，尚不构成
覆盖证明。

`type_ii_private_product_state.py` 在此分解上继续记录碰撞部分诱导的全部私有目标。
它区分目标落在私有支撑外、支撑内或混合的状态，并核验私有积集恰缺一个诱导目标时的
补因子同余陷阱。前十四移位的千万范围共同残余中 1,641/1,792 条属于全支撑外主型，
其中 1,141 条私有积集已经饱和为整个支撑；所以这个一孔陷阱是精确的消去分支而不是
主要覆盖机制。该形状在前十九移位的千万范围仍为 747/855 条全支撑外、510 条支撑
饱和；见 `type-II-private-product-state`。

`type_ii_collision_factor_relay.py` 把碰撞素因子幂连同其来源移位保留，并以其
最小公倍数为闭包，精确枚举能够在自然范围 \(u\le p/4\) 形成后续规范 Type II
证书的所有因子。因 \(h\equiv-1\pmod {4ac}\) 强制
\(ac\mid(h+1)/4\)，枚举对这个因子闭包是完备的，并非设置了任意未来移位上界。
前十四条扇的一百万范围共同失败点中有 12/24 被纯碰撞闭包 relay；前十九条扇的
千万范围在允许零、一、两种来源私有素因子后分别覆盖 25/45、39/45、40/45；
对最后五点再允许三种来源私有素因子仍全部无 relay。\(p=225289\) 即使用至多三种
来源私有素因子仍无 relay，首个真实递降逃逸点
\(p=2451289\) 也没有纯碰撞 relay；所以它是直接证书的有效补充分支而非完整递降
替代，见 `type-II-collision-factor-relay-boundary`。

`type_ii_adaptive_factor_transition.py` 从前十九条规范射线的共同失败点出发，在每个
首个后续成功移位完整枚举所有证书因子，并优先选择旧私有因子重数最小者。千万范围的
45 个点均在移位 20--50 命中；其中 42 个可完全不使用旧私有因子，35 个使用新增
移位首次引入的新因子。故自适应扩扇应重点追踪新因子和旧碰撞因子的共同状态，而不是
继续堆叠旧私有支撑，见 `type-II-adaptive-factor-transition`。

`type_ii_one_collision_source_profile.py` 把最小碰撞重数恰为一的单新因子证书编译为
来源标签状态。若碰撞素数 \(\ell\) 同时来自基础移位 \(t\) 和目标移位 \(s\)，则
\(s\equiv t\pmod\ell\)；证书 \(h=\ell q\equiv-1\pmod{4ac}\) 又强制
\(q\equiv-\ell^{-1}\pmod{4ac}\)。十亿 H19 输出对全部10个一次碰撞状态逐项验证这两条
条件，碰撞素数频数为 \(3:4,5:2,7:1,13:2,17:1\)。这将后续选择器的输入缩减为有限来源
同余类和反元残数，而不宣称任一类必有新素因子；两碰撞延迟释放仍是必要边界，见
`type-II-collision-label-crt-state`。

`type_ii_collision_label_tail_deflation.py` 直接测试这些碰撞标签证书能否成为缩放首
分母的严格双尾递降：对固定证书缺口 \(m\)，完整枚举 \(p+m\) 的因子
\(D>1,\ D\equiv1\pmod m\)，并重建源解。十亿剖面的11个最小正碰撞重数状态中只有
\(p=345601,92421169\) 命中，且均取 \(D=m+1\)、首尺度 \(k=1\)；其余九点包括
两碰撞压力点均无此 \(D\)。因此 CRT 标签短证书不能自动变成同缺口递降，见
`type-II-collision-label-tail-deflation-boundary`。

`type_ii_collision_alternative_tail_descent.py` 随后对上述九个固定证书递降遗漏完整
枚举 \(p-1\) 的所有四倍数因子缺口，并在每个缺口穷尽 \(x^2\) 的 Type II 除子。九点
均有替代双尾严格递降，故十亿 H19 的11个最小正碰撞重数状态有 \(11=2+9\) 的纯递降
闭合；两碰撞点 \(372271201\) 在替代缺口7递降至 \(46533901\)。这只是有限状态集的
证书选择事实，不是 \(p-1\) 缺口选择器的全称证明，见
`type-II-collision-alternative-tail-descent-closure`。

`type_ii_prime_cofactor_boundary.py` 进一步检查前十四移位的极简逃逸模型：每个
`p+4s` 除去同余强制因子后只保留一个素因子。全部可能避靶的核心残数类都被模 3 的
线性型覆盖，因此不能形成无穷的同时素数族。它只迫使至少一个移位拥有更丰富的私有
因子分解，不是 Type II 覆盖定理；见
`type-II-one-prime-private-cofactor-boundary`。

该工具的 `--ac-bound B` 模式改为保留原始 \((A,C)\) 射线，而非按相同的
\(A^2C\) 合并规范移位。半径 5 与 7 的原始参数盒分别有 25 与 49 条射线；在
“每条余商只含一个新素因子”的模型下，所有安全核心类都被线性型局部覆盖，故没有
可采纳的条件性逃逸支。该结果不能推广成参数盒覆盖，因为多私有因子余商仍可能存在；见
`type-II-ac-box-one-prime-local-closure`。

对半径五盒，`--recursive-covering-prime q` 会逐个展开 \(n\bmod q\) 分支，剥离
每条余商中强制的最大 \(q\)-幂，并再次检查射线安全与线性型可采纳性。统一覆盖素数
\(q=7\) 覆盖全部 240 个首层安全类；其 1,680 个分支中有 960 个仍避靶，但没有
一个可采纳。这排除一层额外强制因子的模型，仍不排除更深因子树；见
`type-II-ac-box-recursive-covering-boundary`。

该递归在固定半径五盒并不单调终止。将状态保存为目标素数线性式、各射线固定因子和
剩余余商线性式后，连续四次局部覆盖转移重新出现可采纳状态；显式路径
\((7,0),(11,0),(13,0),(17,0)\) 的目标式为 \(245044800t+1\)。四个 60 根切片的
完整结果保存在 `type-ii-ac-box-recursive-depth4-batch-0-results.json` 至
`type-ii-ac-box-recursive-depth4-batch-3-results.json`；这是固定盒策略的条件性边界，
而非猜想反例，见 `type-II-ac-box-depth-four-recursive-escape`。

对该显式进程，任何统一一次 AC 射线因子都可写为一个固定余因子乘线性因子，因而
\(4AC\) 必整除进程系数 245044800。完整枚举由此得到的全部 896,000 个 AC 分解
与 58,230 个余因子情形没有 Type II 命中；见
`type-II-ac-escape-affine-ray-boundary`。因此补救必须使用非线性因子或
带标记递降，不能只增加一张统一仿射 AC 射线。

`type_i_escape_affine_boundary.py` 补齐同一进程的 Type I 面。固定缺口
`m` 后，`x=(p+m)/4` 的每个常数或非恒定仿射 Type I 除子都由
`S=61261200` 的一个因子和 `gcd(S,(m+1)/4)^2` 的一个除子决定；72 个合法
缺口的 434 个非恒定候选及 434 个常数候选均为空。该结果只排除统一固定缺口，
不排除非线性因子、可变缺口或递降；见 `type-I-escape-affine-boundary`。

同一强制因子阶梯已精确延至第 22 条移位。第 20、21、22 条的规范模数
\(40,84,88\) 都已整除 \(Q_{19}\)，所以没有模数更新；但二层可采纳分支从 265,001
依次降到 151,723、66,638、0。故固定模数下的新射线可以形成有限闭合块，却不能由
此推出下一次会扩模的移位也不重启逃逸；见 `type-II-prime-cofactor-forcing-ladder`。

同一脚本还执行模 3 的第二层剥离。尽管第一层一私有素因子模型不可采纳，剥离其
强制三次幂后会出现可采纳的 15 元线性型分支。因此在素数元组猜想下，固定十四移位
扇有无穷共同遗漏；这是一条限制证明策略的条件性边界，而非猜想反例，见
`type-II-mod-three-recursive-escape-boundary`。

`type_ii_minimal_canonical_shift.py` 逐素数测量首次成功的平方自由规范移位，而不是预先
固定一个参数盒。它在一亿内给出最大首次移位 52 及完整保持者表，其中
\(p=81846241\) 首次把此前的 50 推高；这提示研究随目标增长的移位选择器，但不把
有限谱解释为固定常数覆盖，见
`type-II-minimal-canonical-shift-spectrum`。

加上 `--base-shift-bound 19 --shift-cap 50` 时，同一工具改为审计前十九条规范射线的
实际共同残余、每个残余的首次后续射线，以及联合模数外的因子重数。它保存 45 个
一千万范围残余的过渡谱，并给出 \(p=1127281\)、\(p+76=7\cdot11^5\) 这一
“未固定素因子数为零但射线仍失败”的反例。见
`type-II-nineteen-shift-transition-complexity-boundary`；该模式用于排除候选势函数，
不是全称覆盖或递降定理。

`type_ii_canonical_fan_geometry.py` 记录前 H 条规范移位扇的总模数和失败横截面选择
成本。每个模数都整除 4s，因此这些成本有显式 H 界，可作为把固定扇筛法统一到缓慢
增长 H 的接口；它本身不产生逐点覆盖，见
`type-II-canonical-fan-uniform-sieve-interface`。

`divisor_residue_structure.py` 精确核验有限阿贝尔群层面的边界。它构造偶阶循环群中
达到 Kneser 上界的双向生成元序列，并把线性异常反例嵌入
\((\mathbb Z/4q\mathbb Z)^\times\)。`--prime 7` 还恢复真实整数
\(3^2 19^2\) 的全部除子残数，核对其恰好避开 \(-1\pmod {28}\)。这是否定普适
“真子群加次线性异常”压缩的精确有限见证，不是否定受移位约束的 Type II 饱和猜想。
同一脚本的 `--audit-limit 10000 --ac-bound 5` 模式还逐项检查 Type II
\(AC\) 射线的“支撑临界”层：当除子残数恰为生成子群去掉 \(-1\) 时，它核验目标素数
满足 \(p\equiv1\pmod {4AC}\)。这是 `type-II-support-critical-congruence-trap` 的
有限实现核对；同余结论本身来自补因子配对的证明，不从审计数据归纳。
审计输出还区分 \(-1\) 是否已属于生成子群，并核验支撑内缺失集在补因子对合下的轨道。
在总积不为一时，两孔只能缺 \(\{-1,-p\}\)；奇孔必须含有 \(p\) 的缺失平方根。
这对应 `type-II-support-defect-orbit-constraint`，并刻意把支撑外失败单列，避免把
“射线失败”误当作同一种 Kneser 临界现象。
对支撑外失败，脚本还计算 \(K U(M)^2\)：目标 \(-1\) 不在该平方饱和子群时，
`type-II-target-outside-support-quadratic-separation` 保证存在一个消去 \(K\) 的
二次特征，因而 \(\chi(p)=1\)。目标已进入平方饱和子群的实例单列为二次不可分核；
脚本还检查核心残数子群 \(H_M\) 是否包含于 \(K U(M)^2\)：只有不包含时，某个
分离特征才会在 \(p\equiv1\pmod{24}\) 的允许残数中非平凡。这避免把“存在某个特征”
当成已获得独立的筛法节省。
它还显式枚举 \(U(M)/U(M)^2\) 的二次特征坐标，并报告核心活跃失败可用字符的交集。
例如 \(M=80\) 的两个失败 \(p=601,3169\) 需要互异字符，见
`type-II-fixed-quadratic-character-boundary`；固定字符并不能统一覆盖它们。
脚本还计算支撑外目标的二幂饱和深度 \(\nu\)。深度 \(d\) 表示存在一个阶
\(2^{d+1}\) 的字符核包含全部因子残数，详见 `type-II-two-power-character-depth-sieve`。
它是高阶字符分层的精确审计，不将有限深度频率外推为全体覆盖。
字符核的总积条件不能单独形成多射线矛盾：任意有限组核都由
\(p\equiv1\) 模全部射线模数同时满足，见
`type-II-character-product-congruence-compatibility-boundary`。所以审计重点仍是
移位数的逐素因子残数，而不是只记录其总积角色值。

moving_window.py 逐个检验固定首分母缺口 \(4j-1\) 的纯 Type II 条件，复现
moving-split/divisor-cloud 的有限窗口实验。它报告首个成功 \(j\) 与窗口遗漏；即使
有限范围完全覆盖，也不构成固定 \(J\) 对全体核心素数有效的证明。

`type_ii_h19_pressure_half_factor_pairs.py` 把受控 \(r\) 偶源射线从
\((cr+1)(dr+1)=rp+1\) 正规化为 \(M=(rp+1)/4=AB\)。两端均必须是
\((r+1)/2\pmod r\)，且对应源因子的端 \(B\) 必为偶数。它逐项复核十亿 H19 四个
压力状态的全部已选兼容射线；这是一条精确代数等价和有限数据交叉核对，不是受控
\(r\) 选择器的全称证明，见 `odd-distance-even-source-half-factor-pair`。

`type_ii_h19_pressure_tail_gap_normalization.py` 进一步将兼容平方尾
\(e\) 归一化为 Type I 缺口 \(g=(4e+1)/r\)，并以
\(e=(rg-1)/4\) 反向恢复尾因子。它在四条 H19 压力见证上逐项核验该转换及
\(x=(p+g)/4\)，将未来选择器收紧为 \((r,g)\) 的联合因子选择问题。

`type_ii_h19_p_minus_one_scaled_source_descent.py` 固定源 \(n=p-1\)，完整枚举
所有 \(an/2\)、\(an/4\) 的移位因子候选和强制平方尾。它在既有 \(r\le9999\) 的
15 个 H19 尾部残余上给出 15/15 严格提升及 Type I 证书；它不要求旧偶源标准形的
\(d\equiv1\pmod4\)，因而是更宽的带标记分支。相邻的
`type_ii_h19_p_minus_one_scaled_source_quadratic_boundary.py` 对 H19 四个完整
二次递降漏点进行同一审计，118 个候选全数失败；因此前者不能被误读为替代受控
\(r\) 偶源递降的统一机制。`type_ii_h19_p_minus_one_scaled_source_normalization.py`
进一步核验其首项恒为 \((p-1)(p-t)/4\)，故该分支精确参数化首项被 \(p\) 整除的
一类 Type I 证书，而非独立的存在性定理。

`type_ii_h19_hybrid_bounded_r_p_minus_one_descent.py` 组合
`r<=9999` 的兼容偶源审计与上述非倍数 `p-1` 审计，并检查两者的残余
集合严格相同。它给出存储十亿 H19 剖面的另一条纯递降闭合
\(664=649+15\)，但不将这个有限析取外推为全称选择器。

`type_ii_h19_hybrid_small_r_p_minus_one_descent.py` 将同一析取收紧到
`r<=103`：小 \(r\) 分支覆盖 564 个 H19 残余，流式枚举其余 100 个的
`p-1` 非倍数候选后全部闭合，得到 \(664=564+100\)。默认十点一批清理
因子分解缓存，完整复现检查 10,046 个候选和 97,636,776 个尾因子组合。

`type_ii_small_r_p_minus_one_core_boundary.py` 脱离 H19 输入，对全部
`p<=100000`、`p=1 mod 24` 的核心素数复核同一析取。它留下七个联合
未命中 \(5209,12601,21169,27481,48409,80809,97561\)，因而明确限制小 \(r\)
或 `p-1` 分支的外推；这些点不是猜想反例。

`type_ii_small_r_p_minus_one_even_source_boundary.py` 对这七点进一步完整扫描
所有奇距离标准偶源。仅 `12601`、`97561` 在距离一命中；其余
`5209,21169,27481,48409,80809` 对全部 \(0<c<p\) 均失败，因而组成当前
非标准源/新尾部模型的共同压力集。

`type_ii_small_r_p_minus_one_tail_deflation_closure.py` 对上述五点运行
Type II 双尾抽缩，全部给出严格源；加上另外两条距离一偶源，得到全部小范围核心素数
的四分支闭合 \(1181=978+196+2+5\)。因此五点是偶源/缩放分支边界，不是加入
Type II 抽缩后的总残余。

`type_ii_tail_deflation_p_minus_one_core_hybrid.py` 则直接对全部
`p<=100000` 的核心素数枚举 `p-1` 的所有合格因子并验证 Type II 双尾抽缩。该主分支
覆盖 1,179/1,181 个素数，仅 `67369`、`85369` 未命中；脚本随后对这两个残余完整枚举
`p-1` 的 `b=2,4` 缩放源，均由 `b=2` 严格提升闭合，得到更紧的两分支审计
\(1181=1179+2\)。这是有限选择器剖面，不能外推为全称结论。

type_ii_tail_deflation_p_minus_one_10m_boundary.py 把这个析取推广为一千万范围的
反证式边界：先由普通 Type II 双尾抽缩覆盖 82,803/82,887 个核心素数，再对 84 个
残余完整枚举 p-1 的 b=1,2,4 严格缩放源，额外覆盖 77 个。余下七个明确压力点给出
\(82887=82803+77+7\)，因此这两个严格递降分支不能被误作该范围内的全覆盖选择器。

type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py 随后只对那七点检查规范
Type II 位移 \(s\le2\)。七点均有直接短证书，于是得到有限“短证书或递降”闭合
\(82887=82803+77+7\)；最后一项是直接证书，不能记作递降。
其中位移 1 的四张属于 \(p+4\) 的 \(3\bmod4\) 因子分支，位移 2 的三张属于
\(p+8\) 的 \(7\bmod8\) 因子分支。

同一链条已独立复现至 \(p\le20\,000\,000\)：普通双尾抽缩覆盖 158,449/158,595 个，
完整 \(p-1\) 的 \(b=1,2,4\) 严格缩放再覆盖 135 个，最后 11 个仍均由规范位移
\(s\le2\) 短证书闭合，即 \(158595=158449+135+11\)。这扩大了有限证据，
不是统一选择定理。

在 \(p\le50\,000\,000\) 的 374,902 个核心素数中，前两种严格递降覆盖 374,882 个。
其 20 个残余若只用规范位移 \(s\le2\) 有四个明确遗漏；首次位移为 \(3,3,4,5\)。
扩至 \(s\le5\) 后全部短证书闭合，得到 \(374902=374600+282+20\)。因此固定
位移二扇已被精确反例否定，而位移五闭合仍只是有限事实。

type_ii_tail_deflation_p_minus_one_external_source_pressure.py 对上述四个 \(s\le2\)
遗漏逐项完整扫描 ordinary、mixed-factor 和 quadratic-factor 三层外部源严格递降；
三层均为零命中。它们因此是低位移扇和现有完整外部源递降族的共同压力集，不是
Erdős--Straus 猜想反例。

type_ii_tail_deflation_p_minus_one_pure_new_release.py 进一步核验四点在首次后续位移
\(3,3,4,5\) 的证书因子都是相对于 \(p+4,p+8\) 的单个新素数
\(47,3347,31,239\)。这个纯新单素因子释放是有限来源剖面，不是有界深度定理。

`type_ii_tail_deflation_p_minus_one_pure_new_100m_closure.py` 将同一析取精确重建至
\(p\le10^8\)。719,781 个核心素数中，普通双尾抽缩给出 719,281 条严格递降，
\(p-1\) 的 \(b=1,2,4\) 缩放源再给出459条；41 个剩余点中27个由 \(s\le2\) 的
直接规范 Type II 证书闭合，另14个在 \(3\le s\le48\) 得到相对于 \(p+4,p+8\) 的
纯新单素因子证书，即 \(719781=719281+459+27+14\)。纯新首次释放深度为
\(s=3,4,5,9,24,48\)，频数为 \(6,3,2,1,1,1\)。五个点在首个成功位移中按最小
\(h\) 选取的证书含多个新因子，但其中三个在同一位移已有另一张纯新证书，只有两个
必须等待后续位移。这排除“首个最小因子必纯新”的强版本，却不构成统一释放深度的定理；
详见 `type-II-tail-deflation-p-minus-one-pure-new-100m-closure`。

`type_i_fg_qprefix_block_bound_first_overflow.py` 聚焦核验三层 q-prefix 门序和两个
精确控制。它在同一 \(p=557281,R=199\) 上重建 actual-F target-odd Fourier request，
并验证 source rows \(19838,138866\)、target \(182\) 形成 typed
\(\{1,3,9\}\) full-\(C_3\) candidate-fiber prefix，同时完整枚举
\(N_x=558009\) 的因子以确认终局 `FIBER_REALIZED` 仍失败。脚本还穷尽
\(p=73\) 的 depth-2 局部 carrier candidates，验证共同 canonical base 与 target
3-primary direction 的双重 no-go；最后核对首个越界标签的 \(M=27\) CRT defect
map、\(p=557281\) 的 gap-79 Type II 分解、\(p=73\) 的 gap-43 菜单空回执以及
二分母保留一项替换提升的正性界 \(W_{73}(7)=-17\)。它不运行历史扫描，也不把数值
quotient \(n<p\) 申报为 E4 递降。

`type_i_fg_qprefix_full_section_annihilator_boundary.py` 把上述 full-\(C_3\) prefix 的
局部 singleton 与 \(N_x=3^4\cdot83^2\) 的完整 ambient divisor fiber 严格分开。它重算
\(|U(728)|=288\)、\(|\ker\eta|=96\)、六点完整截面及能量 \(540\)，验证
\(\chi_{-8}\) 在全部因子像上平凡而在目标上非平凡，并完整枚举保持 \(h=83\) 的 19 个
低模数来源候选以确认 G2 source-CRT 纤维为空；它不验证 exact physical-source
predicate 或 owner maps。

`type_i_fg_qprefix_kernel_depth_neutral_cargo_capacity.py` 在 labelled exponent
box 上重算 ambient kernel-depth 最小完成、owner-layer ideal、neutral cargo、downset
压缩和 residue collision 边界。对 \(p=557281\) 它验证
\(\kappa=(3,2)\)、当前 \(c=(2,0)\)、\(\delta=(1,2)\)，列出九条新增 records 和
十二点最小 principal box，并由实际赋值确认现有 \(3\)-lineage 只能到 depth 2。
这些是 full ambient-kernel completion 的要求，不是未知 physical source 的无条件
必要容量。脚本不把 \(h=83\) 当成 owner token，不验证 product synthesis 或
physical source，也不运行历史范围测试。

`type_i_first_overflow_common_denominator_marked_lift.py` 只处理
\((p,M,y,m,n)=(73,27,29,43,7)\)。它验证自然 \(y\) 的 source/target 双因子门均空、
quotient-multiple \(k=3\) 的 alternate Type I 命中，并完整枚举七个
\(\operatorname{Sol}_{\le}(7)\) 规范三元组，得到恰含两项的 proper marked state 及
两条全域数学像；它不生成统一 selector 的 state E2/E3 回执。

`type_ii_linear_square_gcd_allocation_core_gap_cutoff.py` 在三个聚焦控制上核对
Type II 除子与线性 \(L\)-square 条件的双射、gcd 正规形和最小余量平方根核门。它只
运行 \(p=17\) 的等号边界以及两个 \(M=27\) 控制：\(p=73\) 的大缺口全空和
\(p=557281\) 的 \(d=16\) 构造，不以有限测试代替全称证明，也不扫描历史范围。

`type_i_first_overflow_factor_pair_tail_joint_obstruction.py` 聚焦核对
quotient-multiple 命中与 \(p^2+4n\) 同余因子的双射、互补因子配对和局部降次。
脚本用 \(p=73,M=27\) 保留正控制，用 \(p=73,M=21,n=9\) 与
\(p=2161,M=173,n=25\) 核对平方商结构性空菜单；最后直接比较
\(\mathcal E_p(c)\) 与两个 \(c^2\)-除子族，并验证 \(p=193,M=27,n=15\)
的自然菜单、quotient-multiple 和两条规范尾完整门同时为空。它同时核对
\(p=193\) 的直接 Type II 终端，防止把局部四菜单障碍误报为 terminal-first
全局反例；不运行历史扫描。

`type_i_high_support_c2_centered_vieta_no_go.py` 核对最小高支撑 \(C=2\) 图表中
\(R=8U-1,K=U(8U+1)\) 的反足 Vieta 多项式、伴根传导和全部符号边界，并用
\(p=73,97,193\) 做嵌入控制。全称 centered miss 来自主张中的无限递降证明；脚本
只防止恒等式回归，不以有限枚举代替证明。

`type_i_high_support_c2_rank_one_retention_exhaustion.py` 对 \(p=73,193\) 完整重算
\(n=p-1\) 的 `D-only` 候选分拆、source-supported 与跨图表 \(E\) 菜单的双射、
容量公式、centered Type I 闭式恢复、non-source 空纤维调用条件和 gap-\(7\)
terminal-first 映射，并用 \(p=97\) 核对更早的 gap-\(3\) 单标记正控制。它是聚焦的
公式与控制例验证器，不运行历史范围测试。

`type_i_p_minus_one_equal_tail_marker_capacity.py` 核对全部 \(p-1\) 等尾显式标记的
准入条件 \(h\mid2B^2\)、gcd/赋值等价式、完整三支 \(p\)-进因子分流及其 Type I/II
恢复。它只使用 \(p=73,97\) 检查源缺失、目标空纤维和两个 terminal 控制，不运行
历史范围测试。

`type_ii_p_minus_one_fixed_source_rank_finite_menu.py` 对 \(1\le r\le10\) 双向比较
\(d\mid k^2\) 有限菜单与原 Type II 除子条件，核对三次容量界，并固定核心域
\(r\le5\) 全空、\(r=6\) 仅有 \(p=73,97\) 的边界。该范围只用于防止公式回归；
全称固定秩有限性来自主张中的双射和代数界。

`type_ii_p_minus_one_endpoint_envelope_large_prime_allocation.py` 核对保留
\(4k-r-1\) 后的端点差式、四个 \(r\bmod4\) 闭式和单大素因子分配。它只对
\(p=67369\) 重建 \(q\mid42\) 的五张 Jacobi G 证书、三张有界离散对数 F 证书及
gap-\(31\) Type I 接管；不运行素数范围或历史测试。

`type_ii_p_minus_one_divisor_downset_prime_power_allocation.py` 核对端点允许余因子的
因子下闭合同、最小禁止反链及实际 Type II 命中集合。它只使用
\(p=601,1321,67369\) 三个控制，分别验证素数幂层分配、不可拆分的跨素数禁止块和
单大素数退化情形；不运行历史素数范围测试。

`type_i_overflow_d_one_p_free_peeled_small_anchor.py` 固定核验四个 \(p=73\) 和一个
\(p=97\) 的 \(d=1\) p-free-failure 状态。它逐步重放真实 \(p^e\)-raw peeling、
两侧精确 gcd、到 \(2g\) 的容量剥离、新 clean complete-excess bundle 与 canonical
capacity；包含一个 \(e=2\) 且另一侧容量为 5 的 sharp 控制、一个非平凡 valuation
correction \(J=3\)，以及一个 \(a=1\) 后 bundle 仍含 \(p\) 的边界。脚本不扫描
素数、分母、历史 selector 或完整 Reach。

`type_i_overflow_d_one_a_one_p_primary_chain_no_go.py` 固定重放 \(p=73\) 的真实
四周期 \(1\to74\to5403\to394420\to1\)、四个含 \(p\) 的 complete-excess
bundle、peeled node 的互补容量分支及锚点 3、20 的严格 \(p\)-free target
capacities；另核对一个八条边的 \(H_j\) transient。任意有限长度由声明中的 CRT
证明承担；脚本不扫描素数、分母、历史 selector 或一般参数 \(r\)。

`type_i_overflow_d_one_a_one_two_sided_capacity_tree_no_go.py` 固定核对
\(p=73,N=3\) 的 15 个 \(P/M\) 树节点、14 条双侧容量宏公式，以及两个
double-excess split-carrier 边界：\(r=1\) 时联合 canonical 算术严格但现有 E1/E3
来源不合法，\(r=50\) 时联合 multiplier 同余 1 并发生容量 stutter。任意有限深度
由声明中的 CRT 证明承担；脚本不扫描素数、分母、历史 selector 或一般深度。

`type_i_overflow_d_one_a_one_split_carrier_stutter_relay.py` 固定核对一个带颜色的
split 来源恒等式及非交换逐侧分支、最小 receipt cell 的二次 stutter 条件、
\(p=73,r=50\) 的 \(d=1\) 继电，以及无限算术级数中的三个公式检查点。每个检查点都
重建 \((x,K)=2,(y,K)=3,(R-3,K)=4\)、联合 stutter 和 \(h=3\) 的 capacity-2
严格单侧出口；无限性由 claim 中的消元恒等式证明。脚本不扫描素数、分母、历史
selector、一般图表或完整 Type I/II 菜单；一般二次互反、\(s=0,1,-1\) 分派及
persistent/typed-state 字段不在脚本覆盖范围内。

`type_i_atomic_split_s_zero_endpoint_boundary.py` 接续核对新的
`path_anchored_atomic_split_complete_excess_v1` 与 \(s=0\) 边界。它用

\[
Q=\gcd\left(v,\left(v/\gcd(v,K)\right)^{\operatorname{bitlength}(v)}\right)
\]

的 gcd/模幂公式重算完整超额块，并固定验证：\(p=73,r=1\) 的
\((0,72)\to(0,67)\) 严格 atomic split；\(r=50\) 的 non-maximal \(c=12\) 伪目标、
规范 \(c=72\) stutter 与旧 \(p\)-进秩不降；\(r=57\) 的两个小 endpoint；
\(r=95979\) 的 root departure \(1\to2\) 层反例；\(r=21944065678\) 的两个 immediate
endpoint \(p\)-free 失败；以及一个同时保持根 \(s=0\) 的深度 3 完整容量树。脚本不
扫描素数、分母、selector history、历史测试或一般深度；它只支撑 arithmetic controls，
条件 E1--E4 schema、小 endpoint 定理与任意固定深度 CRT no-go 由两张 claim 的文本
证明承担。

运行 `python3 reproductions/type_i_atomic_split_s_zero_endpoint_boundary.py --verify`。

`type_i_s_one_saturated_endpoint_provenance_exclusion.py` 针对既有 \(p=73\) 的
\(s=1\) 静态饱和 endpoint，使用完整 \(m=1\) 反向前驱公式重建其 23 节点、23 条
带标签边的反向闭包。脚本完整分解 universal \(p\)-source 与最小互素素数
\(q_\star=5\) source 的两个坐标，回放它们全部八条合法首 raw 边并核验七个不同后继
均在闭包外；最后重算饱和 return 和直接 Type II 抢占。它不扫描素数范围、分母范围、
selector history 或历史结果。

运行
`python3 reproductions/type_i_s_one_saturated_endpoint_provenance_exclusion.py --verify`。

`type_i_all_core_dual_saturation_s_zero_tree_no_go.py` 从全核心共同根公式现场构造一个
\(p=73,d=2\) 的新 CRT 控制：先令 \(T\) 同时装入双容量平方和七个树节点，再从
\(4r^2+10r+7\) 的两个简单根中 Hensel 提升一个 \(s=0\) 类，并避开唯一的
\(p^3\) lift。脚本重算六个真实容量宏、两侧容量 \(5330,5403\)、两块相对 \(K\)
互素的 complete-excess 以及 \(\nu_{73}(L-1)=2\)。它不读取历史 artifact 或扫描
素数、分母与 selector history。

`type_i_root_coprime_capacity_fan_half_descent.py` 固定核对根容量层
\(u=(2r+1,(p^2+p+1)/3)\)。三个 \(p=73,u=1\) 控制分别覆盖
\(w=(r-3,(3p+1)/4)\) 的 1、真因子和满因子情形，并重算
\(E=Q_3/w,D=4w,c=\langle2w\rangle_p\)；其中 \(r=3\) 还固定验证 maximal
complete-excess block 不等于 \(Q_3\) 的边界。第四个 \(p=457,u=7\) 控制核验一般
\(9u^2<p\) 小 endpoint 分支。两个脚本都只检查本轮新定理。

```bash
python3 reproductions/type_i_all_core_dual_saturation_s_zero_tree_no_go.py --verify
python3 reproductions/type_i_root_coprime_capacity_fan_half_descent.py --verify
```

`type_i_root_capacity_general_endpoint_divisor_gate.py` 把 \(h=3u\) 推进到一般
proper-root hard 层：固定重算 \(p=313,r=271,h=543\) 的真实 maximal receipt、
\(D\mid ph+1\) 与严格 \(c=298\)，并以 \(p=73,u=M\) 固定唯一非 \(p\)-free
饱和层。两个放宽假设控制只验证抽象除数门可以命中，不把它们误写成 actual receipt。

`type_i_root_capacity_strict_carry_support_rebase.py` 把 actual strict root carry 的
cofactor 精确对齐到 complete-excess 支撑 \(M_{\rm ex}=\operatorname{lcm}(A,Q)=AE\)。
它固定重放 \(p=73,r=3\) 与 \(p=313,r=271\)：旧支撑的 total-cofactor 投影恒为
\(p-1\) 且回到原图表，严格 \(c\) 则只在新支撑上成为 canonical overflow target；
同时核验 \(M_{\rm ex}\nmid K\) 和高支撑秩 \((0,p-1)\to(0,c)\)。它不搜索素数、
参数、selector history 或历史测试。

该脚本也重算 strict receipt 的单侧 payload 门 \(Q>1\)、\(p\nmid Q\)、
\((Q,\beta)=1\) 与 \(h\beta\mid K\)，把缺口准确收缩为 persistent source、
terminal-first priority 和 typed serializer。

`type_i_root_capacity_prime_external_terminal_coupling.py` 核对容量素因子 \(q\) 与
\(q\) 关联最小正外部源的精确有限除子菜单。它固定验证 gap-7 Dirichlet 类、
\(p=2137,t=9\) 的非平凡命中，以及 \(p=457,q=7\) 的 source-5 菜单和 gap-7
Type I/II 双空边界。

`type_i_root_capacity_composite_divisor_external_terminal.py` 把同一菜单从单素因子
扩展到任意 \(1<Q\mid u\)。固定 proper-root 控制 \(p=177433,u=91\) 中，原有
\(Q=7,13\) 两个 prime menu 都为空，而 composite \(Q=91\) 以 \(t=5\) 给出
gap \(455\) 的直接 Type I 证书。它核对严格覆盖增量，不扫描范围，也不把菜单命中
推广为全称出口。

~~~bash
python3 reproductions/type_i_root_capacity_composite_divisor_external_terminal.py --verify
~~~

`type_i_s_zero_rechart_standalone_potential_no_go.py` 核对形式 \(s=0\) 半群压缩、
\(p=73\) 根高度 \(1\to2\to1\)、等支撑形式边，以及既有 \(p=97\) 实际源端 raw
receipt 关联的两个 conditional target 容量重置控制。它不把形式 target 升级为
admitted successor。

三个脚本均不运行历史测试或范围扫描：

```bash
python3 reproductions/type_i_root_capacity_general_endpoint_divisor_gate.py --verify
python3 reproductions/type_i_root_capacity_strict_carry_support_rebase.py --verify
python3 reproductions/type_i_root_capacity_prime_external_terminal_coupling.py --verify
python3 reproductions/type_i_s_zero_rechart_standalone_potential_no_go.py --verify
```

`type_i_root_capacity_stutter_receipt_factor_split.py` 只重放四个固定根端点回执，验证
实际 `D` 与 cyclotomic `M0=(p^2+p+1)/3` 互素、`M0` 素因子全部落在 `E`，以及
`D_C | h^2-1`、`D_T | h^2-h-2r` 的 p±1/T 因子分裂；它不执行范围搜索。

```bash
python3 reproductions/type_i_root_capacity_stutter_receipt_factor_split.py --verify
```

`type_i_root_capacity_stutter_c_side_m_localization.py` 固定核对 stutter 的
`D_C=gcd(D,(p^2-1)/2)` 可以精确写成 `lcm(gcd(D,p+1),gcd(D,p-1))`，且两部分分别
整除 `m` 与 `m+2`。它复放一个奇 C-side 控制和三个核心素数 proper-shape 控制，覆盖
奇、dyadic 与混合 C-side 赋值，并核对 `D_C|lcm(m,m+2)` 以及数值上强制 `D_T>1` 的
两种 \(m\) 情形。后三个控制明确不是 actual root receipt；脚本不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_c_side_m_localization.py --verify
```

`type_i_root_capacity_stutter_h_overlap_residual.py` 固定验证更强的
`D_H=gcd(D,h^2-1) | 2*lcm(m,m+2)`。它分别复放 odd、dyadic、mixed overlap 控制，
并覆盖 actual 推论所需的 `m=3`、`m=4`、`m>=6` 三类数值包络，从而验证约化
`D*=D/D_H` 在这些固定 shape 控制中确为非平凡。它明确区分核心素数 proper-shape、
核心同余合数 shadow 与 actual receipt，不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_h_overlap_residual.py --verify
```

`type_i_root_capacity_stutter_transverse_residual.py` 固定验证约化残余的横向商容量图：
`2T=u(p^2*w-3*v)`、`D*|T/u`、`D*|m+2r`，以及
`gcd(D*, p*M0*(2r+1)*(m-1))=1`。四个控制覆盖 core-congruent composite shadow、
odd、mixed 与 dyadic `D*`；它们只检验必要整数恒等式，不冒充 actual core-prime
receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_residual.py --verify
```

`type_i_root_capacity_stutter_transverse_residual_local_terminal_dispatch.py` 固定验证横向
残余的两条局部 terminal 分支：`q|m`、`q=3 mod4` 时的 `p+1` Type I 证书，以及
`q|m+2`、`q|2p+1`、`q=5 mod8` 时的 Type II 证书。它还固定检查
`p=4441,q=47` 的一个 `q=7 mod8` 候选：`(q+1)/2|C` 虽给出另一张 Type II
证书，却强制 `3|C`，故落在已有 `L=3q` 的 K=2 桥中而不是第三条终端。脚本逐项恢复
`p=433` 的 Type I、`p=97,409` 的直接 Type II 及这个回缩控制的分母，不扫描素数，
也不把控制当作 actual stutter receipt。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_residual_local_terminal_dispatch.py --verify
```

`type_i_root_capacity_stutter_transverse_quadratic_shift_type_ii_fan.py` 固定验证横向
`m+K(K-1)` 二次移位的偶 `K` Type II 终端扇：局部 (q)-条件分解为
`((K-1)p-1)(Kp+1)`，而正支 `q|Kp+1` 与
`q=3K-1 (mod 4K)` 给出
`1/(qC)+1/(KpC)+1/(KpqC)`。`K=2` 重放已知 `2p+1` 行；`K=4,6` 分别以
`(p,q)=(1009,11),(337,17)` 检查新扇行。控制只验证 (q)-局部同余和证书恢复，
不把它们当作 actual stutter receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_quadratic_shift_type_ii_fan.py --verify
```

`type_i_root_capacity_stutter_transverse_general_quadratic_type_ii_fan.py` 固定验证一般
`A` 型横向二次移位扇。对 `A|p+3` 为奇数、偶 `K>A`、`gcd(A,K)=1`，局部条件
`q|m*A^2+K*(K-A)` 分解为 `((K-A)*p-A)*(K*p+A)`；正支
`q|K*p+A` 与 `q=3K-A (mod 4*A*K)` 给出 `(A,B,C)=(A,q,(p+s)/(4*A*q))`
的 Type II 证书，并自动使 `q` 横向于 `h^2-1`。脚本以 `(A,K)=(1,6)` 重放旧扇
的一行，并以 `p=1297,A=5,K=6,q=13` 检查新的 `A>1` 行；控制只验证 q-局部
同余和证书恢复，不冒充 actual stutter receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_general_quadratic_type_ii_fan.py --verify
```

`type_i_root_capacity_stutter_transverse_native_raw_type_ii_menu.py` 固定验证由 actual
`D|ph+1` 诱导的原生 Type II raw-ray 菜单：任意 menu 因子
`Q|D` 且 `Q=-1 (mod 4h)` 都以 `(A,C,K)=(1,(Q+1)/(4h),h)` 直接恢复 Type II
证书；`Q|D*` 是其中的横向子菜单。`p=4657,h=39,Q=311` 与
`p=10369,h=21,Q=335=5*67` 分别检查素数和合数生成模数；它们仅是
root-shape/raw-ray 控制，不冒充 actual receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_native_raw_type_ii_menu.py --verify
```

`type_i_root_capacity_stutter_transverse_overlap_valuation_alignment.py` 固定验证横向
residual 在 `p+1,h-1,m` 与 `p-1,h+1,m+2` overlap 中的三重赋值对齐，以及
`D*` 和 `D_T` 中相同的 T-side excess。两个控制都只是抽象 stutter 算术，明确不
冒充 actual root receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_valuation_alignment.py --verify
```

`type_i_root_capacity_stutter_transverse_overlap_complete_excess_valuation.py` 固定验证
两个 \(p\pm1\) overlap 在 actual maximal complete-excess 归一化中的逐素数分型：
特别是 \(p-1\) 分支进入 `E` 时必须越过完整 \(K\)-容量门。它还核对两个
T-high 残余锁定控制。全部控制都只是局部整数算术，不冒充 actual root receipt，
也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_complete_excess_valuation.py --verify
```

`type_i_root_capacity_stutter_transverse_overlap_receipt_relay.py` 固定验证
\(p\pm1\) complete-excess overlap 到 receipt quotient 与下一 checkpoint 的
q-primary relay。尤其 \(p-1\) excess 控制同时检查
`e`、`s+1`、`r-1` 和 `E1+1` 的同一基准赋值，并核对该 \(q\) 在
Eisenstein 范数 `N` 中严格为单位。两个控制都只是局部 receipt 整数算术，
不冒充 actual root receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_receipt_relay.py --verify
```

`type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py` 固定验证
pure-T negative-root 的 actual maximal complete-excess q-primary 分型、receipt quotient
桥以及 checkpoint relay。它同时检查
`pB0-1=2T`、`pB1-1=2ET`、`pE1+1=2(p-1)ET`，从而确认 `pE1+1` 的 q 因子只是
`E` 与 `T` 的继承；两个控制都只是 q-primary 整数算术，不冒充 actual root receipt，
也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
```

`type_i_root_capacity_stutter_transverse_pminusone_source_tail_boundary.py` 固定验证
两个 source-tail 边界：`p=241` 的局部 complete-excess relay，以及 `p=8641` 的
proper-root/receipt-q-primary 定向输入。后者仍使 `p-1=8640` 的四条完整 fan 行
全空，说明这些输入仍不强制平方尾 witness；两个控制都不冒充完整 actual stutter
receipt，且不扫描素数。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_source_tail_boundary.py --verify
```

`type_i_root_capacity_stutter_transverse_pminusone_root_quotient_offsets.py` 固定验证
一个 proper-root q-primary 控制中的 \(v+3,w+9\) 偏移饱和：两者都有 overlap
基准幂，但不能同时带更高 \(q\)-幂。该控制只验证 root-layer 恒等式，不冒充完整
actual stutter receipt，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_root_quotient_offsets.py --verify
```

`type_i_root_capacity_stutter_transverse_pminusone_root_quotient_orientation.py` 固定验证
actual receipt-q-primary 与 proper-root 条件共同强制的定向结论：`v+3` 恰有基准
q 幂，而 `w+9` 至少多一层 q 幂。控制不冒充完整 actual stutter receipt，且不扫描
范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_root_quotient_orientation.py --verify
```

type_i_root_capacity_stutter_transverse_pminusone_w_offset_valuation_staircase.py 固定验证
\(p-1\) complete-excess 输入下 \(w+9\) 的精确赋值阶梯：非共振时由 \(t\) 相对
\(b=v_q(p-1)\) 的大小给出等式，共振时由一条显式 q-primary 剩余类决定是否再升一层。
两个 proper-root 控制和两个局部整数控制分别覆盖这些分支；后者不冒充 actual root
receipt，且脚本不扫描范围。

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_w_offset_valuation_staircase.py --verify
~~~

`type_i_root_capacity_strict_carry_tail_receipt_fiber_barrier.py` 只重放
`p=73,r=3` 与 `p=313,r=271` 的 strict-root multiplier lifts，验证对固定
canonical cofactor，Bezout 单位在 tail 模数下不变。对 actual high-half
`p=313` 控制，它还核对 `gcd(ph+1,(pn)^2)=4` 与 target 残类 `779 mod 879`，
因而当前 `D|ph+1` 的直接因子不能成为 tail selector。它不扫描素数、
root 参数、分母或历史 selector。

```bash
python3 reproductions/type_i_root_capacity_strict_carry_tail_receipt_fiber_barrier.py --verify
```

`type_i_root_capacity_strict_carry_eisenstein_precofactor_quotient.py` 将 strict
receipt 的 \(D,h,c\) 在进入 fixed-cofactor tail fiber 之前写成 Eisenstein ideal
quotient。它只重放四个 actual receipts，构造
`(h, omega-p)` 的范数-\(h\) generator，并检查
`D+tau*delta-s*omega=gamma*beta`、`N(beta)=t`。控制包括 `p=313` 的单位商、
`p=193` 的 \((h,t)=7\) 非互素边界，以及 `p=577` 中 inert prime \(5\) 必须同时
落在 `D, delta, s` 的精确来源定位；不执行范围扫描。

```bash
python3 reproductions/type_i_root_capacity_strict_carry_eisenstein_precofactor_quotient.py --verify
```

`type_i_root_capacity_strict_carry_eisenstein_small_norm_distance_gate.py` 从 strict
receipt 的 Eisenstein quotient norm `t` 重算互补距离的显式小范数盒。它只检查
`p=313` 的 sharp unit fiber、`p=73` 的 odd-cofactor 分支与 `p=193` 的非小-norm
边界；不执行范围扫描或 tail divisor 搜索。

```bash
python3 reproductions/type_i_root_capacity_strict_carry_eisenstein_small_norm_distance_gate.py --verify
```

`type_i_root_capacity_proper_endpoint_stutter_exclusion.py` 审计两个真实 proper-root
回执的有效整除门，并固定重现已撤回低端证明中的抽象整除反例；它不执行历史范围扫描。

```bash
python3 reproductions/type_i_root_capacity_proper_endpoint_stutter_exclusion.py --verify
```

`type_i_root_capacity_stutter_finite_curve.py` 固定验证 stutter 门的三参数整数曲线：
重算 (D=mp+1-h)、(pa=e(h-1)+1)、(Da=m+h(h-1))、
(me^2-e+1=a(p+e)) 与 (h\mid F(e,m))，并保留一个核心同余合数控制和一个
非核心素数控制，另检查一单位扰动不能伪造 stutter。它不扫描范围，也不把抽象元组
当作 actual receipt。

```bash
python3 reproductions/type_i_root_capacity_stutter_finite_curve.py --verify
```

`type_i_root_capacity_stutter_reduced_divisor_product.py` 固定验证
`D*=D/gcd(D,h^2-1)` 的新约化除子约束：`D*|T`、`D*|S`、`D*|J` 以及
`D*|(h^2-h+m)(h^2-2h-m^2-m+1)`。控制元组只验证必要算术，不冒充核心素数的
actual stutter receipt，也不执行范围搜索。

```bash
python3 reproductions/type_i_root_capacity_stutter_reduced_divisor_product.py --verify
```

`type_i_root_capacity_stutter_norm_bound.py` 固定验证 stutter 参数的正定二次范数
`G(a,e)`、`h|G` 及 `m<1+sqrt(h)` 平方根菜单界；控制元组只验证整数恒等式，
不冒充 actual receipt，也不执行范围搜索。

```bash
python3 reproductions/type_i_root_capacity_stutter_norm_bound.py --verify
```

`type_i_root_capacity_stutter_eisenstein_support.py` 固定验证
`N=a^2-a(e-1)+(e-1)^2` 的 `h|N` 以及其素因子只能为 `3` 或 `1 mod 3`；
它也检查范数商的同样支撑限制，以及非退化 `h` 素因子到容量 source residue 的
精确关系；不冒充 actual receipt，也不执行范围搜索。

```bash
python3 reproductions/type_i_root_capacity_stutter_eisenstein_support.py --verify
```

`type_i_root_capacity_stutter_provenance_dispatch.py` 修正并验证范数因子的来源分派：
所有 `q|h, q!=3`（包括退化 `q|a,b`）都进入现有容量 q-menu；`q=3` 和只在范数商中
出现的 `q` 不带强制容量 provenance。它固定验证一个菜单命中、一个菜单为空、以及
抽象 stutter 控制，不冒充 actual receipt，也不执行范围搜索。

```bash
python3 reproductions/type_i_root_capacity_stutter_provenance_dispatch.py --verify
```

`type_i_root_capacity_stutter_actual_maximality_boundary.py` 固定验证两个接近真实图表的
反例：一个 shadow `D0` 即使同时满足 root layer、`D0|z`、`D0|K`、stutter 曲线和
同余门，也可能在 canonical complete-excess receipt 中被容量内 residual 或 `(A,Q)`
归一化强制扩大为另一个实际 `D`，从而失去 stutter 同余。两个控制分别缺少核心素数性
或目标范围，所以它们只否定这种放松，不宣称核心 proper-root 门为空，也不扫描范围。

```bash
python3 reproductions/type_i_root_capacity_stutter_actual_maximality_boundary.py --verify
```

type_i_root_capacity_stutter_actual_small_root_exclusion.py 固定验证真实 \(p=73,r=3\)
小根 receipt 在 \(h^2\le30p\) 带内的严格 carry，并验证 \(m=1\) 只能在丢失真实根
条件的边界出现。它还精确核对 parity 后低于 30 的五个 \((m,a)\) 对及其
root-divisor 排除，以及 \(\delta=h^2-3p=6\) 的 defect 分解；不扫描素数、分母或
历史图表。

~~~bash
python3 reproductions/type_i_root_capacity_stutter_actual_small_root_exclusion.py --verify
~~~

type_i_root_capacity_stutter_ten_thousand_coefficient_barrier.py 将同一 actual
root-stutter 的必要参数门精确推进到 \(a(m-1)<10000\)：它先枚举 8549 个由
parity/mod-3 强制的 \((m,a)\) 对，再只枚举每个 \(\mathcal B(m,a)\) 的正除子
\(u\)。60 个整性 gate survivor 中，17 个满足核心同余的 \(p\) 均非素数，故得到
\(a(m-1)\ge10000\) 与 \(h^2>10000p\)。这是有限系数门证明，不扫描素数范围、
分母或历史图表，也不把它宣称为完整 global exit。

~~~bash
python3 reproductions/type_i_root_capacity_stutter_ten_thousand_coefficient_barrier.py --verify
~~~

type_i_root_capacity_stutter_pair_root_divisor_gate.py 固定验证一般 \((m,a)\) 的
root-divisor 恒等式、\(u\mid\mathcal B(m,a)\) 与 \(e\) 整性，并用
\(p=54481\) 检查该有限 gate 在 canonical receipt 前仍可通过 shadow divisor、
却被实际 \(D=16D_0\) 排除。它不扫描素数、分母或一般参数对。

~~~bash
python3 reproductions/type_i_root_capacity_stutter_pair_root_divisor_gate.py --verify
~~~

type_i_root_capacity_stutter_cubic_hard_root_wall.py 固定核对 actual stutter
参数对的二次包络
\(13L^2-9\mathcal B=(L+3a-3m)(4L-3a+3m)\)、由其导出的
\(p<19L^3\) 尺度，以及 \(513h^6>8p^4\) 的整数形式。它只复放既有
p=54481 shadow gate 的代数尺度，不把该合数控制当作 actual receipt，也不扫描
素数、分母、参数对或 selector history。

~~~bash
python3 reproductions/type_i_root_capacity_stutter_cubic_hard_root_wall.py --verify
~~~
