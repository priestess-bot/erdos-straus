---
kind: claim
claim_id: type-i-ii-first-primary-layer-terminal-fork
title: 首个 primary 失败层的终端优先—源逃逸 typed 分叉
statement: 在固定层稳定子约化和 source-complete 整数合同已经通过的 F/G 或 Type II 状态中，取所有低于当前层的 primary 请求均已闭合后的首个未决层。奇素数 q 的首个未决层精确分为全 owner 闭合、紧链源逃逸、带容量松弛的 alternate-owner 搜索和严格 q 进超载；q=2 的自由广义 2^j 记录唯一归一为 j=1，只有目标纤维透镜非空时才是近邻直接终端，v_2(E)=1 是唯一二进盒外逃逸层。广义二进近邻关系属于乘法核，不产生独立 q 源需求；F 态的自然标记源为空，不能把该记录登记为 E4 递降。对固定有限 source menu，奇 q 的独立源扩张势严格下降，二进记录因归一化有限，故该首层处理器必在直接终端、q 容量/源逃逸、Fourier/关系或明确算术障碍之一停止；这不是全局选择器闭合定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-fourier-phase-owner-capacity-bridge
  - type-II-qprefix-owner-escape-capacity-decomposition
  - type-II-source-column-escape-finite-expansion-relay
  - type-I-general-dyadic-j-one-terminal-normalization
  - type-I-target-fiber-neighbor-dyadic-normalization
  - type-I-generalized-dyadic-natural-lift-equivalence
  - type-II-owner-joint-circuit-arithmetic-lift-trichotomy
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - primary-layer
  - terminal-first
  - q-adic
  - dyadic
  - owner-map
  - source-escape
  - Fourier
  - strict-descent
  - proof-program
sources:
  - claim: type-I-fg-fourier-phase-owner-capacity-bridge
    role: aligned-FG-owner-input
  - claim: type-II-qprefix-owner-escape-capacity-decomposition
    role: odd-primary-tight-slack-split
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: finite-independent-source-expansion
  - claim: type-I-general-dyadic-j-one-terminal-normalization
    role: dyadic-normalization-and-box-boundary
  - claim: type-I-target-fiber-neighbor-dyadic-normalization
    role: near-pair-provenance-and-kernel-neutrality
  - claim: type-I-generalized-dyadic-natural-lift-equivalence
    role: F-state-natural-source-zero
  - claim: type-II-owner-joint-circuit-arithmetic-lift-trichotomy
    role: relation-circuit-arithmetic-dispatch
visibility: public
last_checked: '2026-08-09'
---

# 首个 primary 失败层的终端优先—源逃逸 typed 分叉

## 1. 首层合同

固定一个已经完成稳定子商约化的状态，并假设当前整数 source contract 是
source-complete 的：每个允许的 source 列、owner、标签、范围和物理槽都已经有
有限记录，且同一物理槽的 token 共享 source signature。把所有 primary 请求按
\(\ell\)-进层编号；处理器只在 \(1,\ldots,j-1\) 层没有未决回执时处理第 \(j\) 层。
因此这里的“首个失败层”不是对所有层的事后扫描，而是一个有序的状态回执。

首层优先级如下：

1. 先检查已经存在的 Type I/II 目标命中和目标纤维近邻；
2. 再检查 source-preserving owner 与真实 q 槽容量；
3. 只有通过前两门后，才调用全源 annihilator、关系 Fourier 或低模数后继；
4. analysis_evidence、未提升的 dyadic 记录和未通过 source label 的相位都不能
   自动升级为递降边。

这个优先级的作用是防止同一个短关系同时被登记为终端和 q 容量需求。

## 2. 奇 primary 的首层分叉

令 \(q\) 为奇素数，owner map 为

\[
\mathcal O=\{(g_i,s_i):1\le i\le m\},
\]

其中 \(g_i\) 是真实 source column、\(s_i\) 是唯一保持标签的整数移位。定义

\[
e_i=v_q(p+4s_i),\qquad
O_j=\{i:e_i\ge j\},
\]

以及完整移位菜单在模 \(q^j\) 上的最大残类容量

\[
C_j=\max_{a\bmod q^j}\#\{i:s_i\equiv a\pmod {q^j}\},
\qquad
\Delta_j=C_j-|O_j|\ge0.
\tag{1}
\]

设第 \(j\) 层独立请求数为 \(R_j\)，每个真实槽的最大重复度为 \(\mu\)。记

\[
G_j=(R_j-\mu|O_j|)_+,\qquad
S_j=\mu\Delta_j,\qquad
D_j=(R_j-\mu C_j)_+.
\tag{2}
\]

则有精确恒等式

\[
\boxed{D_j=(G_j-S_j)_+.}
\tag{3}
\]

若第 \(j\) 层仍有 active owner \(a\in O_j\)，而 \(i\notin O_j\) 的高度为
\(k=e_i<j\)，则

\[
\boxed{v_q(s_i-s_a)=k.}
\tag{4}
\]

若 \(O_j=\varnothing\)，用 OWNER_QPREFIX_TOP_EMPTY 代替 (4)；此时不能凭空
选择比较 owner。

### 奇 q 的互斥回执

在 source-complete 合同下，首层恰落入以下互斥分支：

| 条件 | 回执 | 后继含义 |
|---|---|---|
| \(O_j=\{1,\ldots,m\}\)、\(D_j=0\) | OWNER_CLOSED_CAPACITY_PASS | 进入目标纤维、Rado/Kneser 或 source-closed Fourier；不再收费 owner escape |
| \(O_j=\{1,\ldots,m\}\)、\(D_j>0\) | Q_ADIC_LAYER_CAPACITY_DEFICIT | 源列已全闭合，可构造 annihilator/Rado 对偶；整数降模仍需 E1--E5 |
| \(O_j\ne\{1,\ldots,m\}\)、\(\Delta_j=0\) | OWNER_QPREFIX_TIGHT_ESCAPE | (4) 是紧链边界；若 \(G_j>0\) 同时得到 \(D_j=G_j>0\) |
| \(O_j\ne\{1,\ldots,m\}\)、\(\Delta_j>0\)、\(D_j=0\) | OWNER_QPREFIX_SLACK_SOURCE_SWITCH | 最多 \(S_j\) 个需求可尝试 alternate-owner/source-switch；每条边重过 SNF/CRT |
| \(O_j\ne\{1,\ldots,m\}\)、\(D_j>0\) | Q_ADIC_LAYER_CAPACITY_DEFICIT_WITH_ESCAPE | 完整残类也不足，任何 owner 重排都不能支付剩余 \(D_j\) |

在最后三行中，若存在一个带逃逸 source column 的独立外部请求 \(r\)，将其加入
独立请求集 \(U\)。令

\[
k(r\mid U)=|N(U\cup\{r\})\setminus N(U)|.
\]

则

\[
\delta(U\cup\{r\})
=\delta(U)-(k(r\mid U)-1)\le\delta(U),
\tag{5}
\]

而

\[
\Psi_{\rm esc}(U)=|\mathcal R|-|U|
\]

严格减一。因 \(\mathcal R\) 有限，独立扩张不循环；每次重算后若 q 流释放，停止
沿用旧的缺口角色。若外部方向依赖，输出最小 circuit 的关系 Fourier/算术三分；
若没有合法边，保留完整 SNF/CRT/范围失败行。故 (4) 不是一个模糊的“owner 缺失”，
而是会进入有限 typed 后继的严格整数见证。

## 3. 二进 primary 的首层分叉

令 \(4K=pR+1\)、\(L=2K\)，并取一个自由广义二进记录

\[
(A,B,j),\qquad
A,B\mid L,\quad (A,B)=1,\quad
A\equiv2^jB\pmod R,\quad A<2^jB.
\]

其终端数据为

\[
E_j=2^{1-j}L\frac AB,\qquad
n_j=\frac{2L-E_j}{R}.
\tag{6}
\]

把 \(2^{1-j}A/B\) 约成唯一既约对 \(A^\sharp/B^\sharp\)。则

\[
(A^\sharp,B^\sharp,1)
\]

是同一自由终端的唯一 \(j=1\) 记录，并且 \(E_1=E_j,n_1=n_j\)。因此 \(j>1\)
不是新的 source token，也不能产生新的 q 容量单位。

若 \(K=2^{\nu_2}K_{\rm odd}\)，在扩展指数坐标中令

\[
\ell=v(A)-v(B)-j e_2.
\]

则

\[
v_2(E_j)=\nu_2+\ell_2+2,\qquad
\ell_2\ge-\nu_2-1.
\tag{7}
\]

所以只有一层可能越出扩展目标盒：

\[
\boxed{v_2(E_j)=1
\Longleftrightarrow
\ell_2=-\nu_2-1.}
\tag{8}
\]

令 \(\mathcal Z^-_{R,K}\) 为目标指数纤维，\(B_\nu\) 为原目标盒，并定义二进关系透镜

\[
\mathcal L(\ell)
=\mathcal Z^-_{R,K}\cap(\mathcal Z^-_{R,K}+\ell).
\tag{9}
\]

二进记录的终端优先分叉为：

| 条件 | 回执 | 是否计作 q 源需求 |
|---|---|---|
| \(\mathcal L(\ell)\ne\varnothing\) | DYADIC_NEAR_PAIR_DIRECT_TERMINAL | 否 |
| \(\mathcal L(\ell)=\varnothing,\ v_2(E_j)=1\) | DYADIC_OUTER_BOX_ESCAPE | 否，转二进关系/标签障碍 |
| \(\mathcal L(\ell)=\varnothing,\ v_2(E_j)\ge2\) | DYADIC_RELATION_UNOCCUPIED | 否，转 Fourier/source-label 分支 |

第一行的直接终端由近邻定理给出；第二行是唯一二进盒外层；第三行说明关系向量
虽然落在扩展盒内，却没有目标纤维占据，不能反向伪造近邻。

若状态被标为 finite-exponent F，广义二进记录的自然标记分母
\(\alpha=n_jK/E_j\) 的源集合为空：

\[
W_{n_j,\alpha}\ne\varnothing
\iff
\text{当前图表已有中心 Type I 命中}.
\tag{10}
\]

因此 F 态的二进候选只能走上表三行，不能登记为 E4 递降。若标准偶源的一分母或
E-split 通道成功，已有分类说明它已经是原 \(p\) 的直接 Type I/II 证书或中心重图表，
不属于新的 E4 类型。

## 4. 统一的“不重复计费”结论

上述两种 primary 分支满足三个严格不重复性质。

### 4.1 近邻不收费 q 高度

若 \(\mathcal L(\ell)\ne\varnothing\)，则 \(\ell\) 是同一乘法目标纤维中的关系：

\[
\phi(\ell)=1.
\tag{11}
\]

任意有限群角色在 \(\ell\) 上取单位值。因此近邻终端不能再次产生
SOURCE_RANK_DEMAND(q)；它只保留 terminal provenance。否则同一个短关系会被
同时计为终端和容量，导致虚假的 q 超载。

### 4.2 二进指数不收费新槽

由 \(j=1\) 归一化，所有自由二进记录映射到唯一 \((E,n)\)；同一 \((E,n)\) 的不同
\(j\) provenance 必须共用一个物理终端槽。

### 4.3 奇 q 紧链不冒充 source closure

若 \(\Delta_j=0\) 而某个 owner 逃逸，(4) 给出精确分叉层。即使完整残类数量
等于 owner 数，也没有该 owner 的合法 source label；因此不能把
OWNER_QPREFIX_TIGHT_ESCAPE 送入全源 annihilator。

## 5. 证明

奇 q 部分中，owner 高度条件
\(q^j\mid p+4s_i\) 等价于 \(e_i\ge j\)，故所有 owner 通过当且仅当
\(O_j=\{1,\ldots,m\}\)。完整菜单的最大残类容量是 \(C_j\)，从而
\(\Delta_j=C_j-|O_j|\)。将 \(C_j=|O_j|+\Delta_j\) 代入三段正部，得到 (3)。
若 \(i\notin O_j\)、\(a\in O_j\)，相减

\[
4(s_i-s_a)
=q^{e_i}\left(q^{e_a-e_i}u_a-u_i\right)
\]

且括号模 \(q\) 为单位，得到 (4)。逃逸边的邻域增量给出 (5)，独立请求集势
\(\Psi_{\rm esc}\) 严格下降；依赖边和无边分别是有限关系或算术失败回执。

二进部分直接使用自由二进 \(j=1\) 归一化：约分 \(2^{1-j}A/B\) 保留
\(E,n\)，并给出唯一正规记录。指数式 (7) 给出唯一盒外层 (8)。若关系透镜非空，
近邻归一化定理给出同一 \(E,n\) 的偶终端；若为空，反向近邻条件不成立。式 (10)
是自然标记提升的充要条件，F 态定义排除中心 Type I 命中，故自然标记源为空。
最后，(11) 说明近邻关系在所有角色上中性，结合唯一 \(j=1\) 记录即得不重复计费。
各分支按 owner 完整性、\(\Delta_j\)、\(D_j\)、透镜非空性和二进赋值互斥，且覆盖
首层输入，证毕。

## 6. 构造性控制

### 奇 q 紧链

取

\[
p=433,\quad q=7,\quad S=\{16,100\}.
\]

有

\[
v_7(433+4\cdot16)=1,\qquad
v_7(433+4\cdot100)=2.
\]

第 \(j=2\) 层 \(O_2=\{100\}\)、\(C_2=1\)、\(\Delta_2=0\)。若
\(\mu=1,R_2=2\)，则

\[
(G_2,S_2,D_2)=(1,0,1),
\qquad
v_7(100-16)=1.
\]

这是 OWNER_QPREFIX_TIGHT_ESCAPE 与严格 q 进缺口的同层共存；它不能被 source-
dominating annihilator 静默吸收。

### 奇 q 松弛

仍取 \(p=433,q=7\)，加入 \(S=\{3,10,17\}\)。第 1 层
\[
(|O_1|,C_1,\Delta_1)=(2,3,1).
\]

当 \(\mu=1,R_1=3\) 时
\[
(G_1,S_1,D_1)=(1,1,0).
\]

完整残类容量恰好能吸收一个 owner 缺口，但这只表示一个 alternate-owner 搜索预算，
不表示已经存在 source-switch 边。

### 二进盒外与近邻对照

对

\[
p=673,\ R=83,\ K=13965,
\]

记录 \((A,B,j)=(30,49,2)\) 唯一归一为 \((15,49,1)\)，并给出
\[
E=8550,\quad n=570,\quad v_2(E)=1.
\]

目标纤维只有
\[
(-1,0,-2,1),\quad(1,0,2,-1),
\]
两点差超过原指数盒，所以 \(\mathcal L(\ell)=\varnothing\)，输出
DYADIC_OUTER_BOX_ESCAPE，而不是近邻终端。

相反，在
\[
p=164150809,\quad R=23,\quad
K=2^4\cdot3^2\cdot61\cdot107453
\]
的已知近邻控制中，\(\mathcal L(\ell)\ne\varnothing\)，给出
\(E=157311192\) 且 \(v_2(E)=3\)，应直接输出
DYADIC_NEAR_PAIR_DIRECT_TERMINAL，不能再为同一关系建立 q 容量请求。

## 7. 研究边界

该引理完成的是首个未决 primary 层的 typed 处理和终端优先去重：

* 奇 q 的 owner 逃逸、容量松弛和严格缺口现在有同一个首层回执；
* q=2 的 \(j>1\)、二进盒外层和目标近邻被压到互斥分支；
* 近邻与自由二进关系不再重复计为 Fourier/q 容量；
* 固定有限 source menu 上的独立逃逸扩张有严格有限势。

它仍不证明 source-complete owner map 对每个核心素数存在，也不证明
SOURCE_COLUMN_EDGE_OBSTRUCTED、DYADIC_OUTER_BOX_ESCAPE 或
DYADIC_RELATION_UNOCCUPIED 必然给出 E1--E5 递降。全局缺口因此被收缩为：

1. 为首层的 source escape 或二进关系障碍构造实际 source-switch/标签提升；
2. 或把这些 typed 障碍送入已有的稳定子、F/G Fourier、目标纤维加法终端；
3. 对通过首层的状态，建立跨状态 q 容量支付或严格较小的整数后继。

这三个条件中任何一个未通过，都不能把本引理升级为 Erdős--Straus 猜想的证明。
