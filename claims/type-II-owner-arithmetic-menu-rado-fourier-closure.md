---
kind: claim
claim_id: type-II-owner-arithmetic-menu-rado-fourier-closure
title: Type II owner 算术菜单过滤后的 Rado—q 容量—Fourier 完整分派
statement: 固定一个已经通过稳定子、source-SNF、owner 流和 E1–E3 算术门的有限 primary 请求族。owner 流必须先产出带固定物理槽、容量副本、q 进层和源列的规范资源图；若 token 不能这样规范化，先输出物理 token 分配障碍。对规范图给出 q 容量上界、算术候选邻域、物理流和源列秩。若存在通过 E4 的目标因子掩码则得到 Type II 短证书；否则按 q 容量、算术菜单、物理流、Rado 源秩的优先级输出相应构造性证书。所有必要门均通过且目标仍未命中时，有限乘积支撑的 Parseval 证书必给一个可筛选的相容 Fourier 角色或精确 Fourier 提升障碍。该闭合固定 owner 请求族，但不把规范资源图的存在自动推广为所有核心素数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-primary-mask-arithmetic-lift-criterion
  - type-II-owner-kernel-primary-digit-certificate
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-cross-state-layered-rado-qcapacity-cut
  - type-II-cross-state-source-relation-role-capacity-dispatch
  - type-II-cross-state-full-match-realization-fourier-trichotomy
  - type-II-target-fiber-owner-weighted-fourier-capacity-bridge
topics:
  - type-II
  - owner-weight
  - arithmetic-menu
  - Rado
  - Hall
  - q-capacity
  - source-rank
  - Fourier
  - F/G
  - constructive-certificate
  - proof-program
sources:
  - claim: type-II-owner-primary-mask-arithmetic-lift-criterion
    role: E1-E3-owner-edge-filter
  - claim: type-II-owner-kernel-primary-digit-certificate
    role: primary-mask-input
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: canonical-physical-resource-flow
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: q-adic-subset-capacity-bound
  - claim: type-II-cross-state-source-relation-role-capacity-dispatch
    role: rank-and-Hall-role-dispatch
  - claim: type-II-cross-state-full-match-realization-fourier-trichotomy
    role: finite-support-Fourier-closure
  - claim: type-II-target-fiber-owner-weighted-fourier-capacity-bridge
    role: owner-weighted-target-spectrum
  - reproduction: reproductions/type_ii_owner_arithmetic_menu_rado_fourier_closure.py
    role: direct-q-rank-hall-fourier-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 算术菜单过滤后的 Rado—q 容量—Fourier 完整分派

## 1. 固定请求图

固定一个已经通过目标纤维、稳定子、source-SNF、owner 物理流以及 E1–E3
算术门的有限 primary 请求集 \(\mathcal R\)。这里的 owner 物理流不是一个只返回
总流值的标签：它必须产出一个规范的物理资源副本图。若 token 无法在保持来源
标签和源列的前提下规范化到该图，当前闭合先返回
\(\mathrm{OWNER\_TOKEN\_ASSIGNMENT\_OBSTRUCTED}\)，不把 token 数当作容量。

对每个请求 \(r\)，记 \(\mathcal T(r)\) 为 E1--E3 过滤后仍保留来源记录的
owner-token 候选。规范化后得到资源副本集合 \(\mathcal D(r)\)；副本
\(d=(c,k,\sigma)\) 包含物理槽 \(c\)、其第 \(k\le b(c)\) 个容量副本和唯一的
来源记录 \(\sigma\)。每个副本还有固定 q 进层 \(j(d)\) 和初等源列 \(v(d)\)。
不同 token 若投影到同一 \(c\) 但给出不相容的 \(\sigma\) 或 \(v\)，不能合并为
一个副本，必须由上一条物理流门报告障碍。

每条规范资源边 \(e\) 保存

\[
e=(r(e),c(e),j(e),v(e),\sigma(e)),
\tag{1}
\]

其中 \(r(e)\in\mathcal R\) 是请求，\(c(e)\) 是规范资源副本，\(j(e)\) 是 q
进层，\(v(e)\) 是当前初等源商中的源列，\(\sigma(e)\) 是带来源因子和标签的
算术记录。同一物理槽只能出现至多 \(b(c)\) 个已验证副本；边图不再包含未经
验证的 owner multiplicity。

对任意请求子集 \(U\subseteq\mathcal R\)，写

\[
N_{\rm ar}(U)=\bigcup_{r\in U}\mathcal T(r),
\qquad
N_{\rm phys}(U)=\bigcup_{r\in U}\mathcal D(r),
\qquad
\rho(U)=\operatorname{rank}\{v(d):d\in N_{\rm phys}(U)\}.
\tag{2}
\]

在进入 Rado 之前，owner token 到规范副本的三层网络给出对每个 \(U\) 的最大流
\(\mathsf F_{\rm phys}(U)\)。它同时检查请求—token 兼容、token 唯一性和物理槽
\(b(c)\) 容量；若流门通过，\(\mathcal D(r)\) 才是可供 Rado 使用的规范资源集合。
此外，已有 q-prefix 估计给出一个只依赖真实移位和层的物理资源上界
\[
|N_{\rm phys}(U)|\le \mathsf C_q(U).
\tag{3}
\]
式 (3) 可以取分层最大占用和，也可以取 shared-q 合并后的更紧上界；关键是它
对所有规范图副本都成立。

完整 owner 匹配 \(M\) 必须满足：

\[
r(e)\text{ 每个只出现一次},\qquad
\#\{e\in M:c(e)=c\}\le b(c),
\qquad
\{v(e):e\in M\}\text{ 满足所需独立性}.
\tag{4}
\]

目标记为 \(t\)；若当前掩码对应的来源因子积 \(h_M\) 满足某个低模数参数
\((D',A)\) 的 E4 正规形，则称 \(M\) 是 direct-hit 掩码。

## 2. 优先级定理

对固定 \(\mathcal R\)，按以下顺序选择最小的请求子集 \(U\)（先按基数、再按
规范字典序）：

### q 进容量缺口

若
\[
\boxed{\mathsf C_q(U)<|U|,}
\tag{5}
\]
则输出
\[
\mathrm{OWNER\_GRAPH\_Q\_ADIC\_CAPACITY\_DEFICIT}
=(U,\mathsf C_q(U),|U|).
\tag{6}
\]
这是物理 q 层的严格必要上界，任何 owner 标签重命名、Fourier 振幅或普通
Hall 重排都不能补足它。

### 算术 Hall 缺口

若 q 上界通过，但 E1--E3 过滤后的候选 token 邻域满足
\[
\boxed{|N_{\rm ar}(U)|<|U|,}
\tag{7}
\]
则输出
\[
\mathrm{OWNER\_GRAPH\_ARITHMETIC\_HALL\_DEFICIT}
=(U,N_{\rm ar}(U),\text{failed E1--E3 edges}).
\tag{8}
\]
这是算术菜单本身的严格缺口；同一物理槽上的多个 token 尚未被计作多个物理
资源。

### 物理流—Hall 缺口

若 q 上界和算术候选邻域均通过，但 owner 流不能为 \(U\) 产出满流，即
\[
\boxed{\mathsf F_{\rm phys}(U)<|U|,}
\tag{9}
\]
则输出
\[
\mathrm{OWNER\_GRAPH\_PHYSICAL\_HALL\_DEFICIT}
=(U,\mathsf F_{\rm phys}(U),|U|,\text{minimum cut}).
\tag{10}
\]
这是请求—token—物理副本网络的精确最小割证书：候选 token 数量即使足够，也
不能把同一物理槽或同一容量副本重复使用。它不是源列秩证书，也不能被 Fourier
质量补足。

### 源秩缺口

若 q 上界、算术候选和物理流均通过，但
\[
\boxed{\rho(U)<|U|,}
\tag{11}
\]
则输出
\[
\mathrm{OWNER\_GRAPH\_SOURCE\_RANK\_DEFICIT}
=(U,\rho(U),|U|,\text{source-column basis}).
\tag{12}
\]
规范副本已经消除了物理槽冲突；Rado 对偶可取非零 \(\lambda\) 湮灭
\(N_{\rm phys}(U)\) 的源列而分离请求需求。不能把多个相同 source column 按
owner 标签重复收费。

这里的充分性不是把普通 Hall 和一个独立的秩测试机械相加：物理流通过后，
\(\mathcal D(r)\) 已经是每个请求在规范副本上的允许集合，每个副本是向量拟阵的
一个元素。于是 \(\rho(U)\ge|U|\) 正是这组请求的单一 Rado 条件，自动同时保证
不同副本和源列独立性；若 token 仍有未消解的多值投影，则不能进入此分支。

### 匹配后的目标 Fourier

若所有请求子集都通过 (5)、(7)、(9)、(11)，规范资源图上的 Rado 条件给出一个满足
(4) 的完整匹配 \(M\)。若 \(M\) 或其合法子掩码通过 E4 直接命中 \(t\)，输出
\[
\mathrm{OWNER\_GRAPH\_TYPE\_II\_SHORT\_CERTIFICATE}.
\tag{13}
\]

若没有直接命中，令 \(P_M\) 为匹配边所代表的所有合法二元选择的去重乘积支撑。
则 \(t\notin P_M\)，并定义
\[
F_M=1_{P_M}-\delta_t.
\tag{14}
\]
Parseval 给出至少一个非平凡角色 \(\chi\) 使
\[
\widehat F_M(\chi)\ne0.
\tag{15}
\]
先按角色阶、幅度和固定群坐标选择规范角色。若 \(\chi\) 通过源关系格、
目标锚点和 SNF 相容性，输出
\[
\mathrm{OWNER\_GRAPH\_SOURCE\_RELATION\_FOURIER}
=(M,P_M,t,\chi,\widehat F_M(\chi)).
\tag{16}
\]
若所有非零角色均无法通过这些提升门，输出
\[
\mathrm{OWNER\_GRAPH\_FOURIER\_LIFT\_OBSTRUCTED}
=(P_M,t,\text{failed relation rows}).
\tag{17}
\]
(16) 才能进入 F/G 相位、进一步的 q 容量或已有 primary relay；(17) 不能收费为
隐藏容量。

## 3. 穷尽性证明

先看任意请求子集 \(U\)。任何合法完整匹配都必须使用规范 q 层资源，所以
\[
|U|\le|N_{\rm phys}(U)|\le\mathsf C_q(U).
\]
若第一不等式链在右端失败，就得到 (5)--(6)。若 q 上界通过而要让源列独立，
必须先有足够的 E1–E3 候选；若 \(|N_{\rm ar}(U)|<|U|\)，得到 (7)--(8)。
候选数通过但物理流不足时，最大流—最小割定理给出 (9)--(10)。物理流门通过后，
规范副本图上的 Rado 独立代表定理要求且只要求 \(\rho(U)\ge|U|\)，否则得到
(11)--(12)。

若所有子集都通过四种必要条件，有限 Rado 定理给出满足物理槽、标签和源列
独立性的匹配 \(M\)。对它先检查所有合法掩码的 E4；命中即 (13)。若全部未命中，
\(F_M\) 不是常函数：它在目标 \(t\) 处为 \(-1\)，在 \(P_M\) 上为 \(1\)，在
其它点为 \(0\)（即使 \(P_M\) 是余一点集，取值也不恒定）。因此 Fourier 逆变换
保证至少一个非平凡系数非零，得到 (15)。有限角色逐条经过 SNF/锚点条件，只会
成功进入 (16) 或留下 (17)。这五类按优先级覆盖固定请求图的全部出口。

## 4. 与跨状态 q 容量和 F/G 的接口

(6) 可以直接接已有的分层 q 进容量切割；(8) 接 owner primary 掩码的同余纤维
菜单；(10) 接 owner 投影流—割证书；(12) 接 Rado 线性对偶或 source-column
escape；(16) 接
F/G Fourier phase-owner bridge。这样“算术菜单为空”不再是孤立负标签，而有
明确的后继：

\[
\begin{array}{c}
\text{q 上界失败}
\to\text{严格 q 进容量缺口},\\
\text{算术边失败}
\to\text{CRT/SNF/范围障碍或 source-switch},\\
\text{物理流失败}
\to\text{物理槽最小割/owner collision},\\
\text{源秩失败}
\to\text{线性 annihilator/source-column},\\
\text{四门通过且目标缺失}
\to\text{相容 Fourier / Fourier lift obstruction}.
\end{array}
\tag{18}
\]

若 (8) 的缺口对应一个 \(D'<D\) 的菜单元素，则沿 E5 记为严格递降；若只有
同模数候选或没有保持标签的群映射，保留相应的 (8) 或 (10) 而不伪造递归边。

## 5. 构造性控制

### \(p=5113\)：直接 owner 掩码

请求集只有一个请求，物理 q 槽 \(q=7\) 容量为 1，源列秩为 1，算术邻域非空；
选中因子 \(h=7\) 满足 \(h\equiv-1\pmod4\)，所以 (13) 返回
\((K,B,C)=(2,1461,1)\)。

### \(p=433,q=7\)：q 层优先于其它缺口

取两条独立请求都要求第 2 层，而移位 \(S=\{16,100\}\) 的分层上界为
\[
C_1=2,\qquad C_2=1,\qquad \mathsf C_7=3.
\]
展开两条请求的第 2 层需要四个槽；规范子集 \(U\) 先触发
OWNER_GRAPH_Q_ADIC_CAPACITY_DEFICIT，而不是源秩或 Fourier。

### \(p=97\)：算术 Hall 空缺

来源因子 \(11,13\) 的共同乘积 \(143\equiv-1\pmod{24}\)，但
\(AD'\) 合同没有合法参数纤维。算术过滤后的边邻域为空，故两个请求的
\(N_{\rm ar}(U)\) 为零，输出 OWNER_GRAPH_ARITHMETIC_HALL_DEFICIT；不能将
群乘积命中写成 Type II。

### 纯 Fourier 后继

在加法 \(C_8\) 中取 \(P_M=\{0,4\}\)、目标 \(t=1\)。所有请求/边必要条件通过，
但目标不在支撑；角色 \(\chi(x)=(-1)^x\) 给出非零 (16) 候选。若源关系格不允许
该角色，则同一实例输出 (17)。

### 共享物理槽控制

两条请求各自有两个不同 owner token，故 \(|N_{\rm ar}(U)|=2\)，q 上界也取
\(\mathsf C_q(U)=2\)；但两个 token 都投影到同一物理槽 \(c\)，且
\(b(c)=1\)。owner 三层流的最大值只有 \(1\)，所以先输出
OWNER_GRAPH_PHYSICAL_HALL_DEFICIT，而不能把两个 owner 标签收费为两个 q 槽。

## 6. 研究边界

本引理完成的是固定、有限 owner 请求图的 typed closure：它证明了算术菜单过滤后
每个请求族必有 q 容量、算术 Hall、物理最小割、源秩或 Fourier/短证书出口。它仍
不证明每个核心素数都能建立一个满足 E1–E3 且可规范化的有限完备请求图，也不保证
(8) 或 (10) 自动产生 \(D'<D\)；全局目标仍要求跨状态 source-complete 映射，或
把这些负证书接到已经证明的 Type I/F/G 终端和良基递降。
