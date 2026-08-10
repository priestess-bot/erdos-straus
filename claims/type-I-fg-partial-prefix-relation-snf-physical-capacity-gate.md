---
kind: claim
claim_id: type-I-fg-partial-prefix-relation-snf-physical-capacity-gate
title: F/G 有限 partial-prefix adapter 的关系格 SNF、物理匹配容量与忠实角色边界
statement: >-
  给定有限阿贝尔源群 S、循环相对目标 C_d、有限 sheet 请求及 exact physical
  occurrence records，固定一个全局可行物理匹配后，指定 sheet phases 能由所选源记录上的群角色
  实现，当且仅当源记录的全部整数关系都被 phase 行模 d 湮灭；该条件由一次关系格
  SNF 给出充要证书。物理可行性若含共享 occurrence、共同参数或乘积约束，必须先由
  全局 feasible-matching family 刻画；只有容量已展开且约束逐请求可分离时，Hall
  才给出其充要条件。因而忠实 partial role adapter 存在，当且仅当至少一个全局可行
  matching 同时通过关系格 SNF。若 E=exp(S)，任何被指定为本原 C_d phase 的单条记录
  已强制 d|E。对 p=557281 的原 actual-F 源 S=U(199)=C_198 和隐藏 C_4 sheets，
  任意 b=1 记录都有源关系 198x=0，而目标 phase 满足 198*1=2 mod 4；故不仅 whole-source
  homomorphism，而且原状态中任意包含本原 b=1 sheet 的有限、关系保持的 partial
  adapter 都严格不存在。
  原 actual-F 指数盒中仍恰有 51 条 labelled 三点 83-prefix raw chains，分成
  27、12、12 三类 lift；每类内部两两不交，跨类同起点仅共享首尾，全部 51 条共享成
  27 个 image-level triples、覆盖 105 条 raw records。现有 integer source line 把每条链
  压成同一 row，且每条 83-edge 的阶 66 仍违反 C4 关系。后续已有一个保持 active pair、
  在完整指数盒上单射并保存 full-C9 phase 的 affine 扩展；它给出跨规范基
  2->929->182 的 83-height ladder，但 target-compatible 同基三-sheet容量严格为零，
  physical cargo adapter 仍未建立。
  任意不保持该关系的 physical set map 即使以后构造成功，也不能把 psi_4 拉回为
  homomorphic source character 或规范 role column，不能支付忠实 C_4 Fourier 容量；
  它必须保持 UNPRICED，或显式进入扩充 source state。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-marked-source-menu-saturation
  - type-I-fg-snf-canonical-role-evaluation-quotient
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - type-I-fg-qprefix-depth3-replacement-lineage
  - type-II-same-fiber-factor-box-neutral-role-capacity
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - q-prefix
  - partial-adapter
  - relation-lattice
  - SNF
  - physical-capacity
  - Hall
  - Fourier
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-fg-marked-source-menu-saturation
    role: finite-marked-relation-and-fixed-order-snf
  - claim: type-I-fg-snf-canonical-role-evaluation-quotient
    role: relation-preserving-role-evaluation-boundary
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-occurrence-token-capacity
  - claim: type-I-fg-qprefix-block-bound-first-overflow-terminal
    role: p557-actual-F-labelled-exponent-box
  - claim: type-I-fg-qprefix-depth3-replacement-lineage
    role: p557-active-integer-source-line-and-occurrence-contract
  - claim: type-II-same-fiber-factor-box-neutral-role-capacity
    role: p557-target-factor-sheets-and-unit-group-input
  - reproduction: reproductions/type_i_fg_partial_prefix_relation_snf_physical_capacity_gate.py
    role: focused-relation-hall-and-p557-controls
visibility: public
last_checked: '2026-08-11'
---

# F/G 有限 partial-prefix adapter 的关系格 SNF、物理匹配容量与忠实角色边界

## 1. 两种不能混同的 partial adapter

固定有限阿贝尔源群 \(S\)，以下用加法记号；固定循环相对目标

\[
C_d=\mathbb Z/d\mathbb Z.
\tag{1}
\]

令 \(I\) 是有限 sheet 请求集，每个请求 \(i\in I\) 带指定相对 phase

\[
\omega_i\in C_d.
\tag{2}
\]

物理层先给出一个 **exact available-token table** \(\mathcal T\)。每个 token 已经保存：

1. 一条真实整数/source record 及其 provenance；
2. 当前 source state 中的群坐标 \(x_t\in S\)；
3. 去重后的 owner/occurrence key；
4. 扣除已有 load 后仍可消费的一单位容量；
5. 它可服务哪些请求的 exact predicate。

若 owner 容量大于一，应先展开成互异可用 occurrence tokens；同一物理 record 是否允许
多次使用必须由 ledger 决定，不能由展开过程擅自复制。记 \(A_i\subseteq\mathcal T\)
为请求 \(i\) 的允许 tokens。

一个 **set-theoretic token assignment** 先只是一个 raw matching

\[
\sigma:I\hookrightarrow\mathcal T,
\qquad \sigma(i)\in A_i.
\tag{3}
\]

它只保存有限 record identity。仅当它属于第 4 节的全局可行族
\(\Sigma_{\rm phys}\) 时，才是 **globally feasible set-theoretic physical
adapter**；逐请求边本身不排除共享资源冲突。若还要把目标角色拉回源状态、形成
Fourier/evaluation column 或支付 \(C_d\) role capacity，则必须存在同态

\[
\rho_\sigma:S_\sigma\longrightarrow C_d,
\qquad
S_\sigma=\langle x_{\sigma(i)}:i\in I\rangle,
\tag{4}
\]

满足

\[
\rho_\sigma(x_{\sigma(i)})=\omega_i
\qquad(i\in I).
\tag{5}
\]

满足 \(\sigma\in\Sigma_{\rm phys}\) 及 (3)--(5) 的才称为
**relation-preserving partial role adapter**。式 (4) 只要求定义在所选记录生成的
子群上，不要求延拓到整个 \(S\)；所以下面的 no-go 严格强于只排除 whole-source
homomorphism，同时仍不排除任意的 set map (3)。

## 2. 关系格充要判据

固定一个物理匹配 \(\sigma\)。定义

\[
\pi_\sigma:\mathbb Z^I\longrightarrow S_\sigma,
\qquad e_i\longmapsto x_{\sigma(i)},
\tag{6}
\]

及其整数关系格

\[
\mathcal R_\sigma=\ker\pi_\sigma.
\tag{7}
\]

phase 行唯一延拓为同态

\[
\Omega:\mathbb Z^I\longrightarrow C_d,
\qquad e_i\longmapsto\omega_i.
\tag{8}
\]

**有限 partial-role 关系格定理。** 存在且唯一存在满足 (4)--(5) 的
\(\rho_\sigma\)，当且仅当

\[
\boxed{\mathcal R_\sigma\subseteq\ker\Omega.}
\tag{9}
\]

**证明。** 若 \(\rho_\sigma\) 存在，则
\(\Omega=\rho_\sigma\circ\pi_\sigma\)，故 (9) 必要。反之，(9) 说明
\(\Omega\) 在 \(\pi_\sigma\) 的每条纤维上常值，所以由商映射的泛性质唯一下降为

\[
\mathbb Z^I/\mathcal R_\sigma\simeq S_\sigma
\longrightarrow C_d,
\]

并满足 (5)。证毕。

这一定理不要求 \(\mathcal T\) 覆盖完整 source universe；但若要把得到的角色用于
后续全源 Fourier、Rado 或 successor，仍须另证 exact source contract 和相应 ambient
extension。这里关闭的只是“所选有限 records 自身能否一致承载指定 phase”。

## 3. SNF 证书与局部指数障碍

写

\[
S\simeq\mathbb Z^r/D\mathbb Z^r,
\qquad D=\operatorname{diag}(m_1,\ldots,m_r),
\tag{10}
\]

并令 \(X_\sigma\) 的第 \(i\) 列为 \(x_{\sigma(i)}\) 的 invariant-factor 坐标。
则

\[
\mathcal R_\sigma
=\{a\in\mathbb Z^I:\exists z\in\mathbb Z^r,
\ X_\sigma a-Dz=0\}.
\tag{11}
\]

对整数矩阵 \([X_\sigma\ -D]\) 做 SNF，再对其整数核向 \(a\)-坐标的投影做
Hermite/SNF 基约化，可得 \(\mathcal R_\sigma\) 的整数基 \(N_\sigma\)。于是 (9) 等价于

\[
\boxed{(\omega_i)_{i\in I}N_\sigma\equiv0\pmod d.}
\tag{12}
\]

若 (12) 失败，任一非零失败列 \(a\) 同时给出

\[
\sum_i a_i x_{\sigma(i)}=0\quad\text{in }S,
\qquad
\sum_i a_i\omega_i\ne0\quad\text{in }C_d,
\tag{13}
\]

即一个可复核的 `PARTIAL_PREFIX_RELATION_SNF_OBSTRUCTED` 证书，而不是笼统的
“adapter 未找到”。

令 \(E=\exp S\)。对每个单独请求 \(i\)，都有

\[
Ee_i\in\mathcal R_\sigma.
\]

所以 (9) 立即强制

\[
\boxed{E\omega_i\equiv0\pmod d\qquad(i\in I).}
\tag{14}
\]

若 \(\omega_i\) 是 \(C_d\) 的生成元，则 (14) 等价于

\[
\boxed{d\mid E.}
\tag{15}
\]

重要的是，(15) 不需要 \(\rho\) 定义在整个 \(S\) 上：只要一条原状态 record 被要求
承载本原 phase，它自己的有限关系 \(Ex=0\) 已经产生障碍。

### provenance 坐标不是免费的例外

若 records 实际带有一个已经定义群律的标记坐标

\[
\widetilde x_i=(x_i,\lambda_i)\in S\oplus E,
\tag{15a}
\]

令 \(\widetilde{\mathcal R}\) 与 \(\mathcal R\) 分别为映到
\(\langle\widetilde x_i\rangle\) 和 \(\langle x_i\rangle\) 的关系格，则

\[
\widetilde{\mathcal R}\subseteq\mathcal R.
\tag{15b}
\]

若 phase 行湮灭 \(\widetilde{\mathcal R}\) 而不湮灭 \(\mathcal R\)，它只在 labelled
extension 上定义角色；该角色在

\[
\ker(\langle\widetilde x_i\rangle\to\langle x_i\rangle)
\simeq\mathcal R/\widetilde{\mathcal R}
\tag{15c}
\]

上非平凡。正确回执是

\[
\texttt{PROVENANCE\_KERNEL\_CARRIES\_PHASE},
\tag{15d}
\]

而不是“原 \(S\) 内的 partial adapter”。只有 \(E\) 的群律、record-to-label map
和 physical receipts 均由 exact contract 给出时，这个 labelled extension 才合法。
只保存互不运算的 record identifiers 仍只是 set map，不能自动缩小关系格。

## 4. 全局物理可行性与关系格门必须联合

先把全部 exact predicates、owner/occurrence 容量、共享底层资源、共同参数、
shared-\(q\) 条件及乘积等式同时实施，记所得**全局可行注入族**为

\[
\Sigma_{\rm phys}
=\{\sigma:I\hookrightarrow\mathcal T:
\sigma\text{ 满足全部联合物理约束}\}.
\tag{16}
\]

若这些约束还没有 exact contract，唯一诚实状态是

\[
\texttt{EXACT\_GLOBAL\_PHYSICAL\_MATCHING\_FAMILY\_UNPROVED}.
\tag{17}
\]

忠实角色 adapter 的一般精确有限门是

\[
\boxed{
\exists\ \sigma\in\Sigma_{\rm phys}
\quad\text{s.t.}\quad
\mathcal R_\sigma\subseteq\ker\Omega.}
\tag{18}
\]

只有在每个 token 容量已经展开为一、所有合法性逐请求可分离、不同 tokens 不会复用
同一底层 occurrence 时，\(\Sigma_{\rm phys}\) 才恰是二部图
\((I,\mathcal T;A_i)\) 的 matchings。此时 Hall 定理给出 set adapter (3) 的充要条件

\[
\boxed{|N(J)|\ge |J|\qquad(J\subseteq I),}
\tag{19}
\]

其中 \(N(J)=\bigcup_{i\in J}A_i\)。即使 (19) 通过，也只得到 set map；仍须对所选
coordinates 检查 (9)。

若唯一的联合约束是 owner blocks \(\mathcal T=\bigsqcup_o\mathcal T_o\) 上的 quota
\(\kappa_o\)，则可使用 partition-matroid rank

\[
r_\kappa(A)=\sum_o\min\{\kappa_o,\ |A\cap\mathcal T_o|\},
\tag{20}
\]

Rado 判据

\[
\boxed{
r_\kappa\left(\bigcup_{i\in J}A_i\right)\ge |J|
\qquad(J\subseteq I)
}
\tag{21}
\]

恰刻画 owner-capacitated set adapter。若还存在共同参数、shared-\(q\)、乘积等式或
不同 bundles 对同一底层 occurrence 的竞争，则局部合法组合即使各自做成 bundle token，
普通 Hall 仍可能重复使用隐藏资源。只有 bundle ground elements 已编码完整的全局
allocation，且所有互斥冲突也已展开时，才能重新应用 Hall；否则必须直接保留
\(\Sigma_{\rm phys}\)。

关系格依赖所选 token 坐标，所以一般不能先分别最大化 physical capacity 与
source-SNF capacity 再把两个数相乘或取最小值。对每个 \(J\subseteq I\)，令
\(\Sigma_{\rm phys}(J)\) 为由全局合同允许的 partial allocations，定义容量函数

\[
\kappa_{\rm set}(J)
=\max_{\sigma\in\Sigma_{\rm phys}(J)}|\operatorname{dom}\sigma|,
\tag{21a}
\]

\[
\kappa_{\rm rel}(J)
=\max\{|\operatorname{dom}\sigma|:
\sigma\in\Sigma_{\rm phys}(J),\
\mathcal R_\sigma\subseteq\ker\Omega\}.
\tag{21b}
\]

这里 (21b) 中的 \(\Omega\) 与 \(\mathcal R_\sigma\) 均限制到
\(\operatorname{dom}\sigma\)。

总有

\[
\kappa_{\rm rel}(J)\le\kappa_{\rm set}(J)\le |J|,
\tag{21c}
\]

而完整 relation-preserving adapter 恰对应
\(\kappa_{\rm rel}(I)=|I|\)。除非另证交换律和次模性，不能把
\(\kappa_{\rm rel}\) 称为 matroid rank。有限实现可以枚举
\(\Sigma_{\rm phys}\) 后逐个运行 (12)，或把失败关系作为 branch-and-cut 约束加入
全局可行性问题；无论采用哪种算法，(18) 才是一般数学合同。

最小严格反例说明 Hall 不能代替 SNF。取 \(S=C_6=\langle g\rangle,d=4\)，一个请求
的 phase 为 \(1\)，唯一 token 的坐标为 \(g\)。Hall 完全匹配通过，但源关系

\[
6g=0
\]

被送到 \(6\equiv2\pmod4\)，故 (9) 失败。反过来，局部 phase 相容也不能制造
不存在的 occurrence token；SNF 通过而 Hall 亏损时仍无 physical adapter。

一个正控制是 \(S=C_{12}=\langle g\rangle,d=4\)，三条互异 tokens 的坐标为

\[
0,\ 3g,\ 6g
\]

并分别指定 phases \(0,1,2\)。同态

\[
\rho(g)=3\pmod4
\]

实现全部指定值；若三条 token 均可用，Hall 与关系格门同时通过。

## 5. \(p=557281\) 的 finite-partial 严格 no-go

原 actual-F 源群为 \(S=U(199)\simeq C_{198}\)。目标侧直接计算得到

\[
\operatorname{ord}_{728}(3)=6,\qquad
\operatorname{ord}_{728}(83)=4,
\]

\[
\langle3\rangle\cap\langle83\rangle=\{1\}.
\]

而

\[
\psi_4(u)=(u\bmod13)^3
\]

满足 \(\psi_4(3)=1\)、\(\psi_4(83)=8\)，且 \(8\) 在
\(U(13)\) 中的阶为 \(4\)，所以它是这个相对商的忠实角色。因此原源群与相对目标为

\[
S=U(199)\simeq C_{198},
\qquad
\langle3,83\rangle/\langle3\rangle\simeq C_4.
\tag{22}
\]

三张 arithmetic sheets 的相对 phases 是

\[
b=0,1,2\pmod4.
\tag{23}
\]

考虑任意 finite physical token table，并假设其群坐标仍落在**原状态** \(S\) 中。
若某个匹配 token \(t_1\) 服务 \(b=1\) sheet，则无论 \(x_{t_1}\in S\) 是什么，恒有

\[
198x_{t_1}=0\quad\text{in }S.
\tag{24}
\]

但指定 phase 给出

\[
198\cdot1\equiv2\not\equiv0\pmod4.
\tag{25}
\]

所以 (24) 本身就是 (13) 的失败关系，得到

\[
\boxed{
\texttt{P557\_ORIGINAL\_STATE\_RELATION\_PRESERVING\_C4\_ADAPTER\_INCLUDING\_B1\_NO\_GO}.}
\tag{26}
\]

这个结论与候选 tokens 是否已枚举、owner 是否充足无关；它把此前 whole-source no-go
严格加强到原 \(C_{198}\) 状态中任何**包含本原 \(b=1\) sheet** 的有限
selected-record subgroup。对 \(b=2\)，
\(198\cdot2\equiv0\pmod4\)，所以该单条指数关系不排除 \(C_2\) 影子；这与
\(\psi_4^2\) 的既有诊断一致，但不构造 physical token。

### actual-F raw \(83\)-chains 的完整 lift 分类

[actual-F full-\(C_3\) 控制](type-I-fg-qprefix-block-bound-first-overflow-terminal.md)
给出的真实 labelled exponent-box records 是

\[
\mathcal B=[-1,1]\times[-1,1]\times[-3,3]\times[-1,1]\cap\mathbb Z^4,
\tag{26a}
\]

四个坐标依次对应 \(2,5,11,2083\)。设

\[
\phi(z)=2^{z_2}5^{z_5}11^{z_{11}}2083^{z_{2083}}\pmod{199}.
\tag{26b}
\]

先分类盒中任意一条有向 \(83\)-edge \(z\to z+\delta\)。坐标差范围为

\[
\delta_2,\delta_5,\delta_{2083}\in[-2,2],
\qquad
\delta_{11}\in[-6,6].
\tag{26c}
\]

利用

\[
(\log_3 2,\log_3 5,\log_3 11,\log_3 2083)
=(106,138,189,165),
\qquad \log_3 83=183,
\]

\(\phi(\delta)=83\) 等价于

\[
106\delta_2+138\delta_5+189\delta_{11}+165\delta_{2083}
\equiv183\pmod{198}.
\tag{26d}
\]

模 \(3\) 迫使 \(\delta_2=0\)。除以 \(3\) 后，

\[
46\delta_5+63\delta_{11}+55\delta_{2083}\equiv61\pmod{66}.
\tag{26e}
\]

对 \((\delta_5,\delta_{2083})\in[-2,2]^2\) 的 \(25\) 个可能先检查模 \(3\)
相容性；相容时除以 \(3\) 得到 \(\delta_{11}\) 的唯一模 \(22\) 类，再与
\([-6,6]\) 相交。范围内恰有四个 lifts：

\[
\begin{aligned}
a&=(0,0,-2,1),&
r&=(0,1,-5,0),\\
s&=(0,-1,1,2),&
t&=(0,2,3,2).
\end{aligned}
\tag{26f}
\]

现在要求

\[
z,\quad z+\delta_1,\quad z+\delta_1+\delta_2\in\mathcal B,
\qquad
\delta_1,\delta_2\in\{a,r,s,t\}.
\tag{26g}
\]

对每个坐标 \(j\)，合法起点数等于该坐标盒长减去
\(\{0,\delta_{1,j},\delta_{1,j}+\delta_{2,j}\}\) 的 span；四个坐标相乘即可精确
计数。检查 \(16\) 个有序 step pairs 后，只有以下三类非空：

| step pair | 全部起点 \(z=(u,v,c,-1)\) | labelled chains |
|---|---|---:|
| \((a,a)\) | \(u,v\in\{-1,0,1\},\ c\in\{1,2,3\}\) | \(27\) |
| \((r,s)\) | \(u\in\{-1,0,1\},\ v\in\{-1,0\},\ c\in\{2,3\}\) | \(12\) |
| \((s,r)\) | \(u\in\{-1,0,1\},\ v\in\{0,1\},\ c\in\{1,2\}\) | \(12\) |

\(t\) 可以形成单 edge，但不能出现在盒内三点链。故完整 labelled 总数为

\[
\boxed{27+12+12=51.}
\tag{26h}
\]

三类的总位移相同：

\[
a+a=r+s=s+r=(0,0,-4,2).
\tag{26i}
\]

同一起点的不同 lifts 因而共享首尾点，但中点的最后坐标分别为
\(0,-1,1\)，所以彼此不同；不同起点的链不相交。三类各自内部 record-disjoint，
而每个 \((r,s)\) 或 \((s,r)\) 起点都属于 \((a,a)\) 的 \(27\) 个起点。lift 数的
image-level 分布为

\[
6\times1,\qquad18\times2,\qquad3\times3.
\tag{26j}
\]

因此全部 \(51\) 条 labelled chains 覆盖的 distinct raw records 恰为

\[
\boxed{6\cdot3+18\cdot4+3\cdot5=105,}
\tag{26k}
\]

而不是把 \(51\) 条链误算成两两不交的 \(153\) 条 records。

\((a,a)\) 的 \(27\) 个起点群像两两不同。事实上两个起点差
\((d_u,d_v,d_c,0)\) 若群像相同，则离散对数同余先模 \(3\) 得 \(d_u=0\)，
除以 \(3\) 后再模 \(3\) 得 \(d_v=0\)，最后
\(21d_c\equiv0\pmod{22}\) 得 \(d_c=0\)。所以恰有 \(27\) 个 absolute
image triples，每一个归一化后都是

\[
(1,83,83^2).
\tag{26l}
\]

代表性 \((a,a)\) 链

\[
(0,0,2,-1)\longrightarrow(0,0,0,0)\longrightarrow(0,0,-2,1)
\tag{26m}
\]

的绝对群像为 \((12,1,83)\)。由此得到构造性回执

\[
\boxed{\texttt{P557\_RAW\_EXPONENT\_BOX\_83\_THREE\_RECORD\_CHAIN\_CLASSIFIED}.}
\tag{26n}
\]

但是每个 \(a,r,s,t\) 都表示群元素 \(83\)，且

\[
\operatorname{ord}_{199}(83)
=\frac{198}{\gcd(198,183)}=66.
\tag{26o}
\]

所以每条 edge 都有源关系 \(66\delta=0\)，而指定 \(C_4\) phase 把它送到
\(66\equiv2\pmod4\)。即使删去中间 sheet，令
\(\Delta_{02}=\delta_1+\delta_2=(0,0,-4,2)\)，则首尾比值
\(\phi(\Delta_{02})=83^2\) 的阶也是 \(33\)，但 phase 差为 \(2\)，故

\[
33\Delta_{02}=0\text{ in }S,
\qquad
33\cdot2\equiv2\pmod4.
\tag{26p}
\]

因此端点 \(b=0,2\) 也不能单独形成 relation-preserving pair。

四个 lifts 的 factor-\(2\) 坐标均为零；actual-F \(C_9\) 因子相位
\((4,3,0,3)\) 在每个 lift 上都取 \(3\pmod9\)，降到 elementary \(C_3\) 才为零；
源端 \(C_2\) 相位均为 \(183\equiv1\pmod2\)。未来 adapter 必须保存或补偿完整
\(C_9\) 相位，不能只检查 \(\eta\)-neutral 性。

现有
[depth-\(3\) active assignment](type-I-fg-qprefix-depth3-replacement-lineage.md)
的 integer source line 是

\[
\mathcal L(z)=14924+89544z_{(2)}.
\tag{26q}
\]

因为四个 lifts 的 \(z_{(2)}\) 增量全为零，它把全部 \(51\) 条 raw chains 的三个
records 分别压成同一个 integer row；当前 owner/occurrence contract 也只登记
\(q=3\) lineage 与 factor-\(2\) shallow edge，没有 \(b\)-labelled cargo slots。
因此当前 active assignment 还有严格的

\[
\boxed{\texttt{P557\_CURRENT\_ACTIVE\_SOURCE\_LINE\_83\_PREFIX\_COLLAPSED}.}
\tag{26r}
\]

后续
[同规范基容量零与跨基 ladder](type-I-fg-qprefix-h83-common-base-capacity-cross-base-ladder.md)
已经给出保持 active pair、在完整 189 点指数盒上单射且保存 full-\(C_9\) phase 的扩展线。
该线把一条合法 \((r,s)\) chain 映到 \(2,929,182\)，精确实现
\(v_{83}(p+4s_b)=0,1,2\)。因此“新的 integer line”与一个 selected-chain 的算术
owner-window state injection 已经构造；原式 (26r) 只描述未扩展的 active line。

于是当前状态中的 faithful \(C_4\) role capacity 为零：任何同时承载 (23) 的
relation-preserving matching 都被 (25) 排除。式 (26n) 已构造 raw exponent-box 层的
set map skeleton；后续扩展又完成 integer 分离、full-\(C_9\) phase 和跨基算术状态
注入。但是 target-compatible 共同规范基的三-sheet容量已被严格证明为零，跨基候选仍缺
获授权的 exact physical-source predicate、fixed-factor-sheet product synthesis、
nonduplicating owner/charge、共同稳定子、E4 与 E5。因此严格状态仍是

\[
\boxed{
\texttt{P557\_SET\_THEORETIC\_PARTIAL\_PREFIX\_PHYSICAL\_ADAPTER\_UNPROVED}.}
\tag{27}
\]

即使以后 (27) 被构造，它也不能把 \(\psi_4\) 拉回原 source span，不能生成规范
role-evaluation column，不能登记 faithful \(C_4\) price。它可以作为一种独立的
finite cargo/terminal search mechanism，但必须保持 `UNPRICED`。若 token 另带一个
使 (24) 不再成立的四阶 coordinate，则 source state 已经发生扩充，应进入既有的
index-\(2\) relative extension 或 index-\(4\) external/full-joint extension 门，而不是
把新坐标伪装成原状态 partial adapter。

## 6. 统一分派

~~~text
finite partial-prefix request
  -> exact global feasible-matching family Sigma_phys proved?
       no: EXACT_GLOBAL_PHYSICAL_MATCHING_FAMILY_UNPROVED
       yes:
         separable unit tokens? use Hall
         owner quota only? use partition-Rado
         otherwise retain the joint feasibility contract
         Sigma_phys empty:
           PARTIAL_PREFIX_GLOBAL_PHYSICAL_CAPACITY_DEFICIT
         Sigma_phys nonempty:
           run relation-lattice SNF for every globally feasible selected tuple
             some tuple passes:
               PARTIAL_PREFIX_RELATION_PRESERVING_ADAPTER_CERT
               -> ambient/source-completeness + final stabilizer + E4/E5
             every tuple fails:
               PARTIAL_PREFIX_RELATION_SNF_OBSTRUCTED
               -> physical set map may exist, but faithful role price is zero
               -> direct cargo/terminal route or explicit state extension
~~~

对 \(p=557281\)，式 (25) 在全局匹配/Hall/Rado 之前已经关闭任何包含 \(b=1\) 的
faithful original-state
\(C_4\) 分支；不应继续用 `PARTIAL_PREFIX_PROVENANCE_ADAPTER_UNPROVED` 同时混装
“任意 set map”和“可支付 Fourier 容量的 role adapter”。该素数已有独立 \(D'=13\)
Type II 终端，所以本卡只校准统一选择器的 transport 量词，不新增递归边，也不改变
terminal-first 顺序。

## 聚焦验证

```bash
python3 reproductions/type_i_fg_partial_prefix_relation_snf_physical_capacity_gate.py --verify
```

验证器只检查本卡的三个小型 Hall/SNF 控制、\(C_{198}\to C_4\) 的同态像与失败关系，
以及 actual-F 指数盒的四种 edge lifts、三类 51 条 chains 和 source-line collapse；
不运行历史测试或素数范围扫描。
