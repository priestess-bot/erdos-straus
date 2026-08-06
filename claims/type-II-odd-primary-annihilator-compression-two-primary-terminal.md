---
kind: claim
claim_id: type-II-odd-primary-annihilator-compression-two-primary-terminal
title: Type II 奇主部分 annihilator 压缩与 2-primary 终端接口
statement: 设 H 为有限阿贝尔目标群，R 含单位元且 t=-1 不在 R，令 L=<R>、Q=H/L，并分解 Q=Q_(2)×Q_(odd)。令 O 为 Q_(2) 在 H 中的原像。则 R 与 t 都包含于 O，t 仍不在 R；若 Q_(odd) 不平凡，O 是严格较小的源—目标状态，且 O 恰为所有平凡于 L 的奇阶角色核的交，因而可由有限个奇素数阶 annihilator 子群递降得到；若 Q_(odd) 平凡，则全部剩余对偶障碍都位于 2-primary 商，可交给广义 2^j 接口。只有在 source-switch、SNF、参数纤维和 E1--E5 通过时，严格群下降才可升级为整数 Type II 递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-I-general-bidirectional-dyadic-window-selector
topics:
- type-II
- annihilator
- odd-primary
- Sylow
- subgroup-descent
- two-primary
- generalized-dyadic
- target-fiber
- source-switch
- proof-program
sources:
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: prime-order-annihilator-subgroup-relay
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: stabilizer-and-lower-modulus-gate
  - claim: type-I-general-bidirectional-dyadic-window-selector
    role: two-primary-terminal-interface
visibility: public
last_checked: '2026-08-05'
---

# Type II 奇主部分 annihilator 压缩与 \(2\)-primary 终端接口

## 1. 目标状态与奇主分解

令 \(H\) 是有限阿贝尔群，\(R\subseteq H\) 是已经通过来源标签和纤维实现门的真实源
积集，并满足

\[
1\in R,
\qquad t=-1\notin R.
\tag{1}
\]

把源集生成的子群记为

\[
L=\langle R\rangle\le H,
\qquad Q=H/L.
\tag{2}
\]

有限阿贝尔群有规范的 Sylow 分解

\[
Q=Q_{(2)}\times Q_{\mathrm{odd}},
\tag{3}
\]

其中 \(Q_{(2)}\) 是 2-primary Sylow 子群，\(Q_{\mathrm{odd}}\) 是所有奇素数
primary 分量的直积。令

\[
\pi:H\longrightarrow Q,
\qquad
O=\pi^{-1}(Q_{(2)}).
\tag{4}
\]

则有精确的指数和商关系

\[
O/L\simeq Q_{(2)},
\qquad
H/O\simeq Q_{\mathrm{odd}},
\qquad
[H:O]=|Q_{\mathrm{odd}}|.
\tag{5}
\]

## 2. 奇主压缩定理

**定理。** 在 (1)--(4) 的条件下：

\[
\boxed{R\subseteq L\subseteq O,
\qquad t\in O,
\qquad t\notin R.}
\tag{6}
\]

因此，若 \(Q_{\mathrm{odd}}\ne1\)，则 \(O\) 是一个严格小于 \(H\) 的有限群状态，
且在 \(O\) 内源集与目标仍然保持同一缺失关系。

更强地，\(O\) 具有角色刻画

\[
\boxed{
O=
\bigcap_{\substack{\chi\in\widehat H\\
\chi|_L=1,\ \operatorname{ord}(\chi)\text{ 为奇数}}}
\ker\chi .}
\tag{7}
\]

如果 \(Q_{\mathrm{odd}}\ne1\)，可以选择有限条奇素数阶角色

\[
\chi_1,\ldots,\chi_s,
\qquad
\chi_i|_L=1,
\qquad
\operatorname{ord}(\chi_i)=\ell_i\text{ 为奇素数},
\tag{8}
\]

使得逐次取核得到严格链

\[
H=H_0>H_1>\cdots>H_s=O,
\qquad
H_i=H_{i-1}\cap\ker(\chi_i),
\tag{9}
\]

并且对每个 \(i\) 都有

\[
R\subseteq H_i,
\qquad t\in H_i,
\qquad t\notin R.
\tag{10}
\]

若 \(Q_{\mathrm{odd}}=1\)，则 \(H/L\) 本身是 2-primary 群；所有平凡于 \(L\) 的
非平凡有限阶角色都具有 2 的幂阶，因而没有任何奇主 quotient relay 尚未处理。

### 证明

由 \(t=-1\) 有 \(t^2=1\)，所以 \(\pi(t)\in Q\) 的阶至多为 2。在直积 (3) 中，
任何阶至多为 2 的元素的奇主分量都是单位元，故
\(\pi(t)\in Q_{(2)}\)，于是 \(t\in O\)。源集显然满足
\(R\subseteq L\subseteq O\)，而原假设给出 \(t\notin R\)，得到 (6)。若
\(Q_{\mathrm{odd}}\ne1\)，式 (5) 给出 \([H:O]>1\)，故 \(O<H\)。

再证明 (7)。所有满足 \(\chi|_L=1\) 的角色都唯一因子化为 \(Q=H/L\) 上的角色。
在 \(Q_{(2)}\) 上，任何奇阶角色都必须平凡，所以右侧至少包含
\(\pi^{-1}(Q_{(2)})=O\)。反向地，若 \(x\notin O\)，则 \(\pi(x)\) 的
\(Q_{\mathrm{odd}}\)-分量 \(u\ne1\)。有限阿贝尔奇群的角色分离定理给出一个
奇素数 \(\ell\mid|Q_{\mathrm{odd}}|\) 和一个阶为 \(\ell\) 的角色
\[
\bar\chi:Q_{\mathrm{odd}}\longrightarrow\mu_\ell
\]
使 \(\bar\chi(u)\ne1\)。把它沿 \(Q\to Q_{\mathrm{odd}}\) 和 \(H\to Q\) 拉回，
得到满足条件的 \(\chi\)，且 \(\chi(x)\ne1\)。故 \(x\) 不在右侧交集，(7) 成立。

若 \(Q_{\mathrm{odd}}\ne1\)，逐个取其有限生成的奇 primary 分量的阶为 \(\ell\)
的商角色。每一步的角色平凡于 \(L\)，且 \(tL\) 的阶至多为 2，所以
\(t\in\ker(\chi_i)\)。角色核至少消去一个奇素数阶因子，因而每一步严格下降；
所有奇主分量被消去后，交集正是 \(O\)，得到 (8)--(10)。最后，若
\(Q_{\mathrm{odd}}=1\)，(3) 已说明 \(Q\) 是 2-primary，奇阶角色只能是平凡角色。
证毕。

## 3. 与已有 annihilator 二分的关系

已有的单个阶 \(\ell\) annihilator 只给出

\[
R,t\subseteq\ker\chi
\quad(\ell\text{ 为奇素数}),
\tag{11}
\]

并把状态送到一个较小的子群。本引理把所有这类分支合并为一次规范压缩：

\[
\boxed{
\text{所有奇主障碍}
\Longrightarrow
H\rightsquigarrow O=\pi^{-1}(Q_{(2)}),
\qquad
H/O\simeq Q_{\mathrm{odd}}.}
\tag{12}
\]

因此“继续寻找另一个奇素数角色”在 \(O\) 之后不会提供新的奇主信息；剩余对偶
问题确实只在 \(O/L\simeq Q_{(2)}\) 中。

在有限群层面可使用严格势

\[
\Phi_{\mathrm{grp}}(H,R,t)=
\bigl(|H|,\ |Q_{\mathrm{odd}}|,\ |Q_{(2)}|\bigr)
\tag{13}
\]

按字典序比较第一坐标。只要 \(Q_{\mathrm{odd}}\ne1\)，一次完整压缩就使
\(|H|\) 严格变为 \(|O|=|H|/|Q_{\mathrm{odd}}|\)。逐个角色的链 (9) 则给出
每一步指数为 \(\ell_i\) 的可审计中间回执。

## 4. 2-primary 残余与广义 \(2^j\) 接口

若 \(Q_{\mathrm{odd}}=1\)，则

\[
Q=H/L=Q_{(2)}.
\tag{14}
\]

此时任意目标缺失的 quotient 证书、源关系角色或 annihilator 角色都只能具有
2 的幂阶。若 \(Q_{(2)}\) 的指数为 \(2^a\)，其任意有限 composition series
都可细分为阶 2 的初等商；目标 \(\pi(t)\) 的阶至多为 2，因而它只能出现在
这座 2-primary 塔的底层目标陪集中。

这给出与广义 \(2^j\) 终端的**精确接口**：

1. 先由 (7)--(12) 删除所有奇主 source/annihilator 方向；
2. 在 \(Q_{(2)}\) 的某个循环商 \(C_{2^a}\) 或其组合商中记录目标相位、源指数盒和
   2-height；
3. 将剩余的 \(2^j\) 相位关系送入[双向广义二进窗口选择引理](type-I-general-bidirectional-dyadic-window-selector.md)。

该接口只说明**剩余障碍的素数支撑已经纯 2-primary**；它不声称任意 2-primary
状态必然有终端。窗口为空、方向高度失败或标记提升失败时，仍须保留相应的
'TWO_PRIMARY_WINDOW_EMPTY'、'TWO_PRIMARY_HEIGHT_MISS' 或
'TWO_PRIMARY_LIFT_OBSTRUCTED' 回执。

特别地，若 \(Q_{(2)}=1\)，则 \(H=L\)：所有源列已经生成整个环境群，而目标仍不在
源积集。这是一个纯关系格/加法组合缺口，不应再被描述为“缺少奇角色”；应转入
目标纤维内的 2-primary 空洞或直接 Type II 参数检查。

## 5. 算术 source-switch 与严格递降门

本引理的 \(H\rightsquigarrow O\) 是有限群层面的严格子群下降。对 Type II 图表，
设 \(H\) 已嵌入某个合法单位群 \(U(4D_*)\)，并保留每个源块的整数来源标签。要把
(9) 中的一步或完整压缩升级为原素数的后继，必须依次检查：

1. 'FIBER_REALIZED'：\(O\) 不是抽象子群占位，而有真实源参数纤维；
2. 'SNF/CRT'：源列、目标 \(-1\) 和各 \(\ker\chi_i\) 的关系在整数格中可回译；
3. 'B'>A' 与正性：回译后的 Type II 正规形仍满足大小门；
4. 'E1--E5'：源解可全域提升，且算术势严格下降。

在运行完整 SNF 之前，可先使用
[奇主压缩 relay 的单位群阶—指数必要过滤器](type-II-odd-primary-relay-unit-group-order-exponent-filter.md)：
\(|O|\mid\varphi(4D')\)、\(\exp(O)\mid\lambda(4D')\) 以及所有固定来源像的阶约束
是每条低模数边的必要条件。前筛为空时直接保留不变量障碍；前筛通过仍必须执行
联合目标同余、满射 SNF、参数纤维和 E1--E5。

若四项通过，记录

~~~text
certificate_type = odd_primary_subgroup_descent
selector_status = verified_edge
source_quotient = H/<R>
removed_index = |Q_odd|
residual_quotient = Q_2
recursive_edge_eligible = true
~~~

并以 \(D'<D_*\) 或既定的源势下降支付整数递降。若任一门失败，记录

~~~text
certificate_type = odd_primary_subgroup_descent
selector_status = lift_obstructed
failed_gate = FIBER_REALIZED | SNF_CRT | RANGE | E1_E5
residual_quotient = Q_2
recursive_edge_eligible = false
~~~

抽象严格下降仍然有效，但不能把它冒充为 Erdős--Straus 的 Type II 后继。

## 6. 构造性边界例子

以下用加法记号表示群中的单位元为 \(0\)，目标 \(t\) 为阶 2 元。

### 奇主压缩确实严格下降

取

\[
H=C_6,
\qquad R=\{0\},
\qquad t=3.
\]

则 \(L=0\)、\(Q=C_6=C_2\times C_3\)，

\[
Q_{(2)}=C_2,
\qquad Q_{\mathrm{odd}}=C_3,
\qquad O=\{0,3\}.
\]

目标 \(3\) 保留在 \(O\) 中且仍不在 \(R\)；阶 3 角色的核正是 \(O\)，所以
\(|O|=2<6=|H|\)。这是单个奇角色链的最小非平凡例子。

### 奇主压缩为空、2-primary 残余保留

取

\[
H=C_8,
\qquad R=\{0\},
\qquad t=4.
\]

这里 \(Q=Q_{(2)}=C_8\)，\(Q_{\mathrm{odd}}=1\)，所以没有任何奇阶 annihilator
可以分离源与核；目标缺失完全属于 2-primary 残余，应由 2-power 商或广义 \(2^j\)
接口处理。

### 不能跳过算术提升门

抽象群中取 \(H=C_6\) 的奇主压缩没有问题，但若把 \(H\) 解释为某个
\(U(4D_*)\) 的源积集，而 \(O=C_2\) 不是任何允许的 \(U(4D')\) 参数纤维，
则只能得到 'ODD_PRIMARY_LIFT_OBSTRUCTED'。这与 \(p=97\) 的模 4 伪命中边界相同：
群商下降成立，不代表整数 Type II 图表存在。

## 7. 统一选择器中的新分派

对一个已经通过 'FIBER_REALIZED' 的 Type II F/G 缺口，现可按如下顺序分派：

\[
\text{源关系商 }Q=H/\langle R\rangle
\longrightarrow
\begin{cases}
Q_{\mathrm{odd}}\ne1:&
\text{奇主压缩，随后检查整数 source-switch},\\
Q_{\mathrm{odd}}=1:&
\text{直接进入 2-primary/广义 }2^j\text{ 菜单},\\
\text{任一提升门失败}:&
\text{保留精确 lift obstruction，不重复收费角色}.
\end{cases}
\tag{15}
\]

它把“奇素数 annihilator 太多、无法决定下一步”这一分支压成一次确定的
Sylow 约化，并把目标为 \(-1\) 的剩余障碍严格限制到 2-primary 层。仍未解决的是：
对每个核心素数，是否总能把 \(O\) 回译成合法较小 Type II 图表，或在
'ODD_PRIMARY_LIFT_OBSTRUCTED' 时构造 Type I/另一种可提升递降。这正是下一阶段
应验证的算术桥，而不是继续增加抽象奇角色枚举。
