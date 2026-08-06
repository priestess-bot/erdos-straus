---
kind: claim
claim_id: type-II-hall-deficit-relay-closure-criterion
title: Type II Hall 缺口到严格递降的有限闭包判据
statement: 对一族有限且带来源标签的 Type II 状态，若每个目标缺失沿有限阿贝尔合成列都能产生较小商缺失、已闭合的锚点出口或 typed 源需求，并且每个 Hall 最小割缺口要么含有保持标签的严格降势回退、要么含有显式 SNF/算术障碍，或满足全源列闭包的 annihilator 商三分，则有限归纳给出 Type II 短证书或严格可提升递降；否则规范最小割本身给出不可递降 Hall 缺口，精确标出尚未闭合的全局条件。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-arithmetic-lift-raw-factor-fallback
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-hall-matching-fiber-realization-gate
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-hall-bundle-target-residue-fourier-gate
  - type-II-anchor-rank-fourier-dispatch
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-linear-rank-deficit-dual-separation-certificate
  - type-II-hall-deficit-linear-dual-bridge
  - type-II-hall-source-column-closure-relay
  - type-II-cross-state-full-match-realization-fourier-trichotomy
  - type-II-cross-state-source-relation-role-capacity-dispatch
  - type-II-cross-state-layered-rado-qcapacity-cut
  - type-II-cross-state-qcapacity-deficit-annihilator-relay
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-hall-surplus-kneser-price-injection
  - type-II-hall-surplus-stabilizer-absorption-quotient-relay
  - type-II-stabilizer-tower-price-recursion
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-kernel-fourier-energy-role-capacity-dispatch
  - type-II-kernel-fourier-support-uncertainty-demand
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-II-arithmetic-empty-raw-fourier-bridge
  - type-II-raw-e1-anchor-relation-obstruction-bridge
  - type-II-full-match-stabilizer-relay-certificate
topics:
  - type-II
  - Hall
  - min-cut
  - relay
  - descent
  - SNF
  - finite-abelian
  - proof-program
sources:
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: typed-demand-resource-graph
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: quotient-or-top-kernel-relay
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: anchor-versus-demand-split
  - claim: type-II-arithmetic-lift-raw-factor-fallback
    role: arithmetic-fallback
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: well-founded-lower-modulus-potential
  - claim: type-II-raw-e1-anchor-relation-obstruction-bridge
    role: e1-environment-dispatch
visibility: public
last_checked: '2026-08-06'
---

# Type II Hall 缺口到严格递降的有限闭包判据

## 1. typed 状态和势函数

考虑有限个带来源标签的状态

\[
\sigma=(H,S,t,\mathcal R,\mathcal C),
\]

其中 \(H\) 是固定参数纤维的有限阿贝尔目标商，\(S\subseteq H\) 是合法源和集，
\(t\notin S\) 是目标，\(\mathcal R\) 是已经由合成列、数字层或顶层核角色证明的
请求，\(\mathcal C\) 是真实 q 进资源槽。为每个状态固定势

\[
\Phi(\sigma)=
\bigl(|H|,\ |H/T|,\ \delta(\sigma),\ |\mathcal R|\bigr),
\qquad T=\operatorname{Stab}_H(S),
\tag{1}
\]

并按字典序比较。在目标缺失分支中

\[
\delta(\sigma)=|H/T|-2-\sum_i\kappa_i\ge 0.
\]

若参数回译保持，严格商递降或稳定子包含的降模递降会严格降低第一或第二坐标；
若处理的是一个已闭合的请求，则降低最后坐标。势的取值在每一条递降边上良基。
这里的 \(\Phi\) 只用于递降证明，不把抽象群商自动当作原猜想的整数实例；整数
source-switch、\(B'>A\) 和标签合同仍须单独验证。

## 2. Hall 最小割的规范提取

在状态的兼容图

\[
\Gamma=(\mathcal R,\mathcal C;E)
\tag{2}
\]

上取一个最大匹配 \(M\)。若它覆盖全部请求，记为 **FULL_MATCH**。否则从所有未匹配
请求出发，沿未匹配的请求边和匹配边做交替可达闭包，记左、右可达集合为
\(U_M\subseteq\mathcal R\) 与 \(N_M\subseteq\mathcal C\)。则

\[
N(U_M)=N_M,
\qquad
|U_M|-|N_M|=u_M>0,
\tag{3}
\]

其中 \(u_M\) 是未匹配请求的数目。因此
\((U_M,N_M,u_M)\) 是规范的 **HALL_DEFICIT** 证书。

### 证明

若 \(U_M\) 有一个邻点不在 \(N_M\)，该邻点按未匹配边应可达，矛盾，故
\(N(U_M)=N_M\)。最大匹配下，\(N_M\) 中不存在未匹配资源槽，否则从某个未匹配请求
到该槽的交替路会增广 \(M\)。所以每个 \(N_M\) 中的槽都由 \(U_M\) 中唯一的请求匹配；
而 \(U_M\) 中除 \(u_M\) 个根请求外，其余请求均对应一个不同的 \(N_M\) 槽，得到
\(|U_M|=|N_M|+u_M\)。证毕。

这比“请求都争用同一 q”的描述更强：它给出最小割实际涉及的请求、资源和缺口整数，
且适用于多 q、不同层和不同状态的混合竞争。

## 3. 可递降回退和局部闭包

对每个请求 \(r\in\mathcal R\)，允许记录下列两类有限回退：

* **LOWER_RELAY**\((r,\sigma')\)：保持整数来源标签和目标解释的后继状态
  \(\sigma'\)，满足 \(\Phi(\sigma')<\Phi(\sigma)\)。它可以来自合成列的较小商、
  稳定子包含的降模商，或 raw 因子回退后得到的严格核心素数下降；
* **OBSTRUCTED**\((r,\omega)\)：有限 SNF、CRT 标签、\(B'>A\) 或算术提升的关系
  证书 \(\omega\)，明确说明候选边不能合法加入 \(E\)。

称状态族满足 **Hall 缺口闭包条件 (HC)**，若对每一个由 (3) 得到的最小割 \(U_M\)，
至少有一个下列事实已经证明：

\[
\begin{array}{ll}
\mathrm{HC1}:&
\text{某个 }r\in U_M\text{ 有 LOWER\_RELAY};\\
\mathrm{HC2}:&
\text{某个 }r\in U_M\text{ 有 OBSTRUCTED 或 ALL\_ARITHMETIC\_LIFT\_EMPTY};\\
\mathrm{HC3\text{-}FIBER}:&
\text{某个固定纤维的 Kneser surplus 已超过 }\delta(\sigma)，\text{且匹配通过}\\
&\text{FIBER\_REALIZED(A)，直接命中 }-1;\\
\mathrm{HC4}:&
\text{顶层角色是已闭合的锚点出口（Type I/F/G 或更小状态）。}
\end{array}
\tag{4}
\]

HC1 是真正的严格递降；HC2 是合法性负证书，不把伪边计入容量；HC3-FIBER 是带
单纤维回译的 Type II 短证书；HC4 排除纯锚点 Fourier 被错误收费。跨状态完整匹配
若没有 FIBER_REALIZED，先对完整匹配执行共同环境的算术实现—Fourier 三分；只有
该三分仍留下未承接的 Fourier/算术障碍时，才记 UNREALIZED_CROSS_STATE_MATCH。
其中通过 SNF 的 SOURCE_RELATION_FOURIER 不直接计为容量：先按真实源关系商检查
纯锚点/关系相位；关系相位再经过源列初等秩门和 Hall 缺口，只有稳定子商达到
Kneser 阈值才进入 Type II。该角色分派见
[Type II 跨状态相容角色的锚点—初等秩—Hall 容量分派](type-II-cross-state-source-relation-role-capacity-dispatch.md)。
对固定 q 的请求子集，还先应用逐层 q 进上界；若
\(\sum_{j\le E_U}C_j(S_U,q)<|U|\)，直接输出
Q_ADIC_LAYER_CAPACITY_DEFICIT，不能把该缺口误写成普通秩失败或继续池化。
分层切割见
[Type II 跨状态分层 Rado—q 进容量切割](type-II-cross-state-layered-rado-qcapacity-cut.md)。
若 q 进缺口的最小割满足 SOURCE-DOMINATING-CUT，则其 Rado 对偶角色湮灭整个
固定纤维源列；目标相位非平凡时转为 GLOBAL_ANNIHILATOR_LOWER_RELAY，核平凡时
转为 TOP_PRIMARY_ANNIHILATOR，目标相位平凡时转为
ANNIHILATOR_SUBGROUP_LOWER_RELAY，源列逃逸时补边或记录算术障碍。该下降桥见
[Type II 跨状态 q 进缺口的 annihilator 商递降桥](type-II-cross-state-qcapacity-deficit-annihilator-relay.md)。
HC 需要独立的算术证明，并非 Hall 定理自动给出的结论。

还需加入完整匹配的闭合条件

\[
\mathrm{HC5}:\quad
\text{若 FULL\_MATCH 未越过 Kneser 缺口，则先有稳定子增长—吸收证书；}
\text{其商 relay 随后必须有已闭合终端、LOWER\_RELAY 或等价 F/G 出口；若吸收发生在多个有序块之间，}
\text{必须逐层投影并删除单位块，不能把最终稳定子价格倒推到历史插入步骤。}
\tag{5}
\]

仅仅从图中删除一个已匹配请求并不等于原目标已解决；稳定子证书先区分真实增长
与被吸收的块，再由商 relay 检查后继，防止“账本消耗冒充证明”。精确证书见
[Type II 单纤维完整匹配的稳定子增长或商 relay 证书](type-II-full-match-stabilizer-relay-certificate.md)。

对固定纤维的 Hall 对偶角色，还加入全源列闭包条件

\[
\mathrm{HC6}:\quad
\begin{array}{l}
\text{对同一最小割构造的真实阶 }\ell\text{ 角色，逐一检查当前纤维的全部源列；}\\
\text{若角色在全部源列上平凡，则目标非平凡相位给出全局 annihilator 商 relay，}\\
\text{目标平凡相位给出真核子群 relay；只有整数提升失败时才保留关系 Fourier。若有源列逃逸，则加入完整 Hall 菜单或}\\
\text{记录该列的有限 SNF/CRT/范围障碍。}
\end{array}
\tag{HC6}
\]

HC6 把“只在当前邻域槽上平凡”的角色与真正的固定纤维商递降区分开来；完整三分见
[Type II 固定纤维 Hall 缺口的全源列闭包—商递降三分](type-II-hall-source-column-closure-relay.md)。
若最小割对每个源生成元都有同纤维合法邻接边，则构成
SOURCE-DOMINATING-CUT，HC6 自动通过；若源列菜单未包含跨纤维角色，只能记录
UNREALIZED_SOURCE_COLUMN，不能套用商 relay。

对逐层 q 进上界已经给出缺口的最小割，再加入独立的 q 进闭包条件。其触发式为

\[
\mathsf C_q(U_M)<|U_M|.
\tag{HC7-q}
\]

**HC7** 要求先保留 \((q,S_{U_M},(C_j),u_q)\) 的分层证书，并由 Rado 对偶角色
\(\lambda\) 检查真实源列。若源列全部被湮灭（直接满足 SOURCE\_COLUMN\_CLOSED，
或经过有限逃逸扩张后满足），必须完成下列前三类分支之一：

* 若 \(\chi_\lambda(t)\ne1\) 且
  \(|H/\ker\chi_\lambda|>1\)，同时给出保持来源标签的整数 source-switch、
  \(B'>A\) 与 E1--E5 后继，把
  GLOBAL\_ANNIHILATOR\_LOWER\_RELAY 记为 LOWER\_RELAY；
* 若 \(\chi_\lambda(t)\ne1\) 且 \(\ker\chi_\lambda=1\)，给出已闭合的广义
  \(2^j\)/primary 终端或 Type I/F/G 出口；
* 若 \(\chi_\lambda(t)=1\)，先调用
  [Type II 全源列闭合的 annihilator 子群—商双向严格递降](type-II-annihilator-two-sided-subgroup-quotient-descent.md)：
  由于全源列均被湮灭，目标与源集同落在真核子群中，输出
  ANNIHILATOR\_SUBGROUP\_LOWER\_RELAY；若 SNF/source-switch/标签提升通过则记为
  LOWER\_RELAY，若失败则同时保留 ANNIHILATOR\_SUBGROUP\_LIFT\_OBSTRUCTED 和
  RELATION\_FOURIER\_NO\_TARGET\_SEPARATION，且不得再次收费目标容量。具体 G1--G4
  菜单和直接 Type II 子列表终端由
  [Type II annihilator relay 的带来源同余纤维提升判据](type-II-annihilator-congruence-fiber-lift-criterion.md)
  完成；
若源列逃逸，则运行
[Type II 源列逃逸的有限独立请求扩张递降桥](type-II-source-column-escape-finite-expansion-relay.md)：
独立外部边扩张后重新提取规范最小割，q 容量释放时转入秩/Hall 分派，依赖外部边
记录关系 Fourier，无合法边时给出 SOURCE\_COLUMN\_EDGE\_OBSTRUCTED。扩张和重新
提割本身不计为当前割的闭包；若扩张 surplus 满足 Kneser-PRICE-INJECTION，
则进一步按
[Type II Hall surplus 到 Kneser 活跃容量的价格注入桥](type-II-hall-surplus-kneser-price-injection.md)
检查目标纤维容量，否则记 HALL\_SURPLUS\_UNPRICED。

HC7 将 q 进容量缺口与普通线性秩缺口分开：前两项是可下降或已闭合终端，第三项先是
严格子群 relay、在整数提升失败时才保留不收费的关系 Fourier 回退，最后一项只允许真实的
SNF/CRT/范围障碍作为负证书。其
annihilator 三分和整数提升门见
[Type II 跨状态 q 进缺口的 annihilator 商递降桥](type-II-cross-state-qcapacity-deficit-annihilator-relay.md)；
有限扩张的终止回执见
[Type II 源列逃逸的有限独立请求扩张递降桥](type-II-source-column-escape-finite-expansion-relay.md)；
因此仅有抽象有限商，或仅有一个可补的跨纤维相似列，都不足以满足 HC7。

在输出 Hall 缺口回执前，还应先应用固定纤维的线性精化门：若 \(U_M\) 的请求已在
同一 \(\ell\)-初等源商中取成独立方向，且所有合法邻域槽来自同一参数回译，则
\(|N_M|<|U_M|\) 自动给出一个
\(\mathrm{HALL\_DEFICIT\_FOURIER\_SEPARATION}\)。该角色随后进入锚点—秩
dispatch；只有没有 FIBER_REALIZED 或固定 primary 线性化时，才保留粗粒度的
UNRELAYABLE_HALL_DEFICIT。精确桥见
[Type II 固定纤维 Hall 缺口到线性对偶分离桥](type-II-hall-deficit-linear-dual-bridge.md)。

HC2 中的 ALL_ARITHMETIC_LIFT_EMPTY 也有固定的精化顺序：三类候选全空必然包含
raw 候选集为空，先由 raw 残数 Parseval 桥构造
RAW_DIVISOR_FOURIER，再按源群指数和 SNF 分成可提升 SOURCE_RELATION_FOURIER
或 ARITHMETIC_FOURIER_LIFT_OBSTRUCTED。只有这些角色仍没有 F/G/严格递降承接时，
才保留未闭合的算术 Hall 缺口。精确桥见
[Type II 算术提升全空到 raw Fourier 的闭合桥](type-II-arithmetic-empty-raw-fourier-bridge.md)。
若允许阶投影 \(e=\gcd(h,\exp H)>1\) 的 Parseval 能量为零，则不得直接结束：
必须调用
[Type II raw 空集的平方除子残数 Fourier 证书](type-II-raw-divisor-residue-fourier-certificate.md)
中的核参数 relay，生成规模 \(h/e\) 的非空真核截面，并按相容角色容量、
RAW_PARAMETER_KERNEL_LIFT_OBSTRUCTED 或
RAW_PARAMETER_KERNEL_CAPACITY_DEFICIT 三分。该核状态若通过来源标签和
整数提升，才可作为 LOWER_RELAY；否则保留具体障碍，不能把原始零能量重复收费。
当 \(e=1\) 时，HC2 必须检查是否已有环境目标纤维：
若锚点脱离源差分群，调用
[Type II raw e=1 空洞的锚点—源关系—提升障碍三分](type-II-raw-e1-anchor-relation-obstruction-bridge.md)。
若 \(\Delta\ne1\)，先检查 E1_ANCHOR_QUOTIENT_SOURCE_SWITCH；只有 Q1--Q4
失败时才保留 E1_ANCHOR_QUOTIENT_LIFT_OBSTRUCTED，并同时保存锚点分离 Fourier。
若 \(\Delta=1\)，商没有严格变小，直接得到 E1_ANCHOR_SEPARATING_FOURIER；
若锚点在差分群内，则把相容源关系角色送入 Rado/Hall 分派。两者均失败时才保留
E1_ENVIRONMENT_UNREALIZED 或具体 SOURCE_RELATION_LIFT_OBSTRUCTED，不能把
\(e=1\) 本身当作全局负证书。商菜单若为空，还要保留 CRT 参数关系 Fourier、
算术空集或目标映射 SNF 的最小失败行，不能把三类失败重复计入容量。

## 4. 有限闭包定理

若一个有限状态族满足：

1. 每个目标缺失均可由有限阿贝尔合成列 relay 分成较小商缺失、顶层核角色或
   已知锚点出口；
2. 每个顶层非恒相位角色和数字层缺口都已转成 typed 请求；
3. 每个状态的合法边均通过 source-switch、SNF、真实 q 整除、shared-q 账本和范围门；
4. Hall 缺口闭包条件 HC1、HC2、HC3-FIBER、HC4、HC6、HC7 以及完整匹配闭合条件 HC5 对所有
   状态成立；每个触发 surplus 的匹配都通过单纤维实现门，未越过 surplus 的完整
   匹配都先通过跨状态算术实现—Fourier 三分，再由稳定子增长—吸收证书闭合其商
   relay；

则从任意初始状态出发，有限归纳必输出下列之一：

\[
\boxed{\text{Type II 短证书}\quad\text{或}\quad
\text{保持来源标签的严格可提升递降}\quad\text{或}\quad
\text{显式算术/SNF 负证书}.}
\tag{6}
\]

### 证明

按势 \(\Phi\) 对状态做良基归纳。若源和集已含 \(t\)，直接得到 Type II；若 Kneser
活跃容量超过缺口且匹配通过 FIBER_REALIZED，适用 HC3-FIBER。否则应用合成列 relay：较小商分支严格降低 \(|H|\)
或 \(|H/T|\)，由归纳假设处理；顶层非恒相位或数字缺口进入请求图，恒相位分支按
HC4 处理。

对请求图取最大匹配。**FULL_MATCH** 时，若匹配后的活跃容量越过该纤维缺口且通过
FIBER_REALIZED，再由 Kneser 得 HC3-FIBER；否则先运行稳定子增长—吸收证书：
增长超过缺口时直接命中，未超过时把吸收块送入稳定子商，再由 HC5 检查该商的
终端或 LOWER_RELAY，不能仅凭“请求已匹配”结束。若不是完整匹配，用 (3) 提取 \(U_M\)。
HC1 给出势严格下降并归纳；HC2 先经 raw Fourier/SNF 桥精化为对偶角色或显式关系
障碍，再按相应出口处理；HC4 给出已闭合的终端。HC6 若源列全被角色湮灭且目标
相位非平凡，则按有限商阶严格下降；目标相位平凡时调用 annihilator 子群 relay，
先在真核子群中保留目标缺失，再由 SNF/source-switch 门决定是否是可提升下降；源列
逃逸则先运行有限独立请求扩张；依赖边进入关系 Fourier，无边时保存有限障碍。
HC7 对 q 进分层缺口执行同一检查，但额外要求分层容量证书、全源列湮灭和整数
提升门同时成立；目标相位平凡时不得继续沿用旧角色，必须完成子群 relay 或保留
具体的 lift obstruction。
若匹配跨纤维却没有实现映射，则输出 UNREALIZED_CROSS_STATE_MATCH。每一步都严格
降低势或终止，因此不会无限回环，得到 (6)。证毕。

## 5. 失败回执的精确定义

若某状态的最小割 \(U_M\) 不满足 HC1、HC2、HC3-FIBER、HC4、HC6、HC7，则不应声称“已递降”。应输出

\[
\mathrm{UNRELAYABLE\_HALL\_DEFICIT}
=(\sigma,U_M,N_M,u_M).
\tag{7}
\]

并保留所有合法边的来源、层数和 SNF 证明。该回执表示当前有限资源确实不足，但尚未
证明缺口能转为 Type II、严格下降或算术不相容；它是全局选择器的真实剩余假设，
而不是猜想反例。

但若该最小割满足固定纤维线性化门，则优先输出
\[
\mathrm{HALL\_DEFICIT\_FOURIER\_SEPARATION}
=(\ell,U_M,N_M,\lambda)
\]
并转入锚点/Fourier 分派；只有该角色仍没有 F/G 载体、source-switch 后继或严格
势下降时，才可把状态保留为未闭合的 Hall 缺口。跨纤维混合的请求不能套用这一
精化，仍须先通过 FIBER_REALIZED。

若回执中出现 ALL_ARITHMETIC_LIFT_EMPTY，则不得直接把它当作最终负结论；必须
先记录对应的 RAW_DIVISOR_FOURIER 频率、指数筛结果和 SNF 行。可提升频率进入
SOURCE_RELATION_FOURIER，全部失败才记录
ARITHMETIC_FOURIER_LIFT_OBSTRUCTED；这些都仍需 F/G 或严格递降承接。

若 HC7 的有限逃逸扩张返回
Q\_ADIC\_ESCAPE\_EXPANSION\_RELEASE，则原 q 进角色失效，必须从新的 \(U'\)
重新运行线性秩/Hall 分派；若返回 DEPENDENT\_SOURCE\_ESCAPE\_RELATION，则只
登记关系 Fourier，不把外部边计作独立容量；若返回
SOURCE\_COLUMN\_EDGE\_OBSTRUCTED，则该失败行可作为 HC2 型显式算术障碍。三者
均不能直接冒充 Type II 或整数递降。若释放后的 q 槽带有固定来源标签，先调用
[Type II q 层请求的来源 CRT 纤维集中与唯一候选](type-II-q-prefix-source-crt-fiber-concentration.md)；
当 \(Q>D^2\) 时它给出唯一共同纤维或精确的 CRT/范围空集。共同纤维中的 q 槽再调用
[Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩](type-II-q-layer-prefix-kneser-price-certificate.md)，
用前缀排序把槽压缩为一个幂块；只有该门通过且所得 surplus 满足价格注入桥，式
(9) 的 Kneser 阈值才可给出 Type II；价格注入失败时保留
HALL\_SURPLUS\_UNPRICED。若失败类型是 STABILIZER\_ABSORBED\_PRICE，则调用
[Type II Hall surplus 稳定子吸收的商递降—Fourier 二分](type-II-hall-surplus-stabilizer-absorption-quotient-relay.md)：
非平凡稳定子给出商缺失，核门失败则记录 KERNEL\_SOURCE\_ANNIHILATOR 或
KERNEL\_BOX\_FOURIER；平凡吸收只删除恒等源块。若同一完整匹配中先后出现多个
非平凡稳定子，改调用[Type II 稳定子塔的非重复价格递归与有限终端](type-II-stabilizer-tower-price-recursion.md)：
逐层保存当前精确积集、剩余块和价格缺口；每个非平凡商严格降低群阶，投影成单位
块的来源永久退出账本，稳定子平凡时才继续收取插入时的 active price。塔的整数门
失败保留该层最小失败行，塔到达平凡稳定子且没有活跃块时进入顶层 primary/Fourier
或数字缺口终端。

若稳定子核门失败而产生目标核截面，则先运行
[Type II 核分裂 Fourier 能量的相容角色—容量分派](type-II-kernel-fourier-energy-role-capacity-dispatch.md)：
不相容能量输出 KERNEL\_FOURIER\_LIFT\_OBSTRUCTED，不收费容量；全相容能量按最小
角色阶进入 \(\ell\)-初等 Rado/Hall、较高 \(2^j\)/primary 或混合 primary 分支。
只有独立角色的源列秩和 q 槽价格同时通过，才可继续 Kneser/Type II；Parseval
能量本身不等于独立容量。对相容角色的非零支撑，先应用
[Type II 核 Fourier 支撑不确定性下界与 simultaneous-role 容量门](type-II-kernel-fourier-support-uncertainty-demand.md)：
支撑下界只提供候选角色数量，必须有互异源槽、独立关系限制和共同实现的
SIMULTANEOUS\_ROLE 证书；否则回执为 FOURIER\_SUPPORT\_NOT\_A\_DEMAND，不能把
非零系数数量直接计入 Hall/q 容量。

若 **FULL_MATCH** 已通过稳定子增长—吸收证书，但其剩余商 relay 仍未满足 HC5，
则对应回执为

\[
\mathrm{UNRELAYABLE\_FULL\_MATCH}
=(\sigma,M,\delta(\sigma)).
\tag{8}
\]

它表示所有当前 typed 请求都能占用资源，但这些资源尚未被证明足以填补目标缺口，也
没有闭合的后继；同样不能把匹配本身写成 Type II 证明。

若候选边因代表依赖、CRT 局部标签或 SNF 不可解而不存在，则应记 **OBSTRUCTED**，
不能把它们从邻域删除后把空邻域解释为“q 容量不足”。

## 6. 边界样例

### \(p=433\) 的真实匹配

取来源移位 \(S=\{16,100\}\)、\(q=7\)。逐层账本为

\[
C_1=2,\qquad C_2=1,\qquad
v_7(433+4\cdot16)=1,\qquad
v_7(433+4\cdot100)=2.
\]

实际需求高度为 \((1,2)\) 时，两个第一层槽和一个第二层槽可给出完整匹配；若再有
Kneser surplus，HC3 直接得到 Type II。

### 反事实 Hall 缺口

若两个状态都声称必须使用唯一的第二层槽，则最大匹配只能覆盖一个请求，交替闭包
给出

\[
U_M=\{r_1,r_2\},\qquad N_M=\{c_{7,2}\},\qquad u_M=1.
\]

若没有已证明的 LOWER_RELAY、OBSTRUCTED 或闭合锚点出口，这只能输出
**UNRELAYABLE_HALL_DEFICIT**，不能把同一层重复收费，也不能把 Hall 缺口本身写成
Type II 证明。这正是当前全局计划仍需补上的条件；同理，实际完整匹配但没有 HC5
时应输出 **UNRELAYABLE_FULL_MATCH**。

## 研究边界

本判据把“Hall 缺口如何进入严格递降”从口头目标化为有限、可枚举的 HC 条件，并证明
HC 一旦对所有核心状态成立就足以闭合短证书/递降选择器。全源列闭包、q 进 HC7 和
有限逃逸扩张现在消除了三类可精化缺口；目标相位平凡的固定纤维还可通过
annihilator 子群 relay 进入更小群。当前仍未证明 q 容量释放、**UNREALIZED_SOURCE_COLUMN**、
整数 source-switch/E1--E5 提升、顶层 primary 终端和 **UNRELAYABLE_FULL_MATCH** 是否
总能转成 Type I/F/G 出口或保持标签的严格下降。
