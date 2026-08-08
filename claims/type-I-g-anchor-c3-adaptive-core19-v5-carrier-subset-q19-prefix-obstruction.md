---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-carrier-subset-q19-prefix-obstruction
title: v=5 物理载体子集的 q=19 前缀分配障碍
statement: 对固定候选纤维 f=(D_*=6303,A=573)、N_f=p+4AD_* 与 q=19，考虑一个已通过通常 source-map 门、但对物理 occurrence omega 只使用其具名载体 gamma_omega 的共同 q 因子来认证连续前缀高度的新增 carrier-subset 准入过滤器。若该 proposed adapter 还要求 q 层全局不可复用，则其无放大高度精确受 cap_f,q(omega)=v_q(gcd(gamma_omega,N_f)) 限制；一族已提议的 occurrence-request 可作互异层匹配当且仅当这些 cap 的升序第 k 项至少为 k。在 v=5 三个实际物理载体 gamma=(C0=p-3,C1=19,C38=38) 都有 cap=1，故任意两条的 proposed carrier-only allocation 已有最小 Hall 缺口 1，三条缺口为 2，尽管 v_19(N_f)=3。该结论严格反驳把 candidate-record 的总深度静默拆给三个 carrier 的做法；它不生成 typed request、token、slot 或容量价格，也不否定带独立 source label、q-free provenance、source-switch 与 slot 回执的未来 adapter。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-g-anchor-c3-adaptive-core19-v5-c38-q19-phase-leaf
  - type-I-g-anchor-c3-adaptive-core19-v5-q19-phase-compatible-candidate-fiber
  - type-I-g-anchor-c3-adaptive-core19-v5-phase-provenance-boundary
  - type-I-raw-factor-block-local-cofactor-provenance
  - type-II-q-layer-prefix-kneser-price-certificate
topics:
  - type-I
  - type-II
  - c3
  - core19
  - raw-source
  - carrier-provenance
  - q-adic
  - prefix-matching
  - Hall
  - candidate-fiber
  - capacity
  - terminal-preempted
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_carrier_subset_q19_prefix_obstruction.py
    role: exact carrier caps, minimum Hall witnesses, and raw-endpoint calibration
visibility: public
last_checked: '2026-08-08'
---

# v=5 物理载体子集的 \(q=19\) 前缀分配障碍

这张卡补上一个比候选 record 高度更细、但仍然局部的**准入过滤器**：一个实际物理
carrier 与一个 candidate record 的共同因子，至多能认证多少个未经额外放大的
\(q\)-层。它的作用是排除一条常见但不合法的推理：从
\(v_q(N_f)=3\) 直接给三个物理 occurrence 各分配一层。

这不是现有 Type II `Q-PREFIX` 合同的替代品。后者还要求 source label、
source-switch、shared-q ledger、范围和其它门。本卡不会从 carrier 自动生成
request 或 token；它只规定：**若**一个已在构造中的 adapter 声称某个前缀高度完全由
carrier 的共同因子承担，则该声称必须通过下面的过滤器。

## 1. carrier-subset q-prefix 合同

固定一个 candidate fiber

\[
f=(D_*,A),\qquad N_f=p+4AD_*,\qquad q\nmid4D_*.
\tag{1}
\]

令 \(\Omega\) 是一组具名 physical occurrence。每个 \(\omega\in\Omega\) 带一个
正整数 carrier \(\gamma_\omega\)：它可以是由 raw receipt 到达的 endpoint，也可以是
physical-tail/overflow row 中明确保存的 cofactor。后一种情形尤其不允许把整个 raw
endpoint 或 character phase 偷换成这个 carrier。

定义其可审计的局部 \(q\)-容量为

\[
\boxed{
 c_{f,q}(\omega)=v_q\!\left(\gcd(\gamma_\omega,N_f)\right).
}
\tag{2}
\]

一个 proposed adapter 只有在已保存 state/raw digest、candidate \(f\)、\(q\)、来源标签，
并通过其所需的 source-switch、CRT、SNF、范围、\(B'>A\) 和 `FIBER_REALIZED` 门后，
才可以尝试登记 carrier-subset 前缀。即使在这些前提下，它还须提供一个从 request 到
全局 q-layer token 的显式单射；尚未给出这个单射时，\(\gamma_\omega\) 仍只是 incidence。

在这种**尝试登记**中，一个 **carrier-subset q-prefix candidate** 带有连续邻域

\[
\mathcal I_\omega=\{1,\ldots,h_\omega\}
\tag{3}
\]

的 provisional request，并额外满足下面两个合同条件：

1. **子集整除性：** \(q^{h_\omega}\mid\gcd(\gamma_\omega,N_f)\)；换言之，每个
   被声称的前缀层都已在这个 carrier 中出现，而不是只在候选 record 的剩余因子中出现；
2. **层不复用：** 同一 \((f,q,j)\) 只能匹配至多一个 occurrence。

这里的 \(q\) 是 candidate/physical-cofactor 方向，而不是 raw 首标签 \(\lambda\)。合同
故意称为 *carrier-subset*：若一个未来 adapter 还提供一个不同的 raw factor
receipt、可验证的 source label 或 q-free base，并据此证明额外的 \(q\)-层，它不再仅是
(2) 的子集申请，必须另写成可追踪的 amplification/source-switch 回执。

## 2. carrier-cap 与 Hall 判据

令

\[
r_\omega=c_{f,q}(\omega).
\tag{4}
\]

**定理（carrier-subset 前缀判据）。** 假设一个 proposed adapter 已经尝试把若干
carrier-subset candidate 登记为互异 q-layer token 的请求。在 (1)--(3) 下，任何这样的
candidate 都有 \(h_\omega\le r_\omega\)。对有限子集 \(U\subseteq\Omega\)，其最大化的前缀邻域为

\[
\bigcup_{\omega\in U}\{1,\ldots,r_\omega\}
=\{1,\ldots,\max_{\omega\in U}r_\omega\}.
\tag{5}
\]

因此这个特定子集的精确 Hall 缺口是

\[
\boxed{
 \operatorname{def}_{f,q}^{\rm car}(U)
 =|U|-\max_{\omega\in U}r_\omega.
}
\tag{6}
\]

全族可匹配当且仅当每个子集的 (6) 都不为正。等价地，若把 \(r_\omega\) 升序排为
\(r_{(1)}\le\cdots\le r_{(n)}\)，则这 \(n\) 条 occurrence 存在互异层匹配当且仅当

\[
\boxed{r_{(k)}\ge k\quad(1\le k\le n).}
\tag{7}
\]

**证明。** (3) 的子集整除性立即给
\(h_\omega\le v_q(\gcd(\gamma_\omega,N_f))=r_\omega\)。使用最大允许邻域不会使
Hall 匹配变差，故 (5) 成立，(6) 正是 Hall 不等式的差额。将高度升序排列后，阈值最小的
\(k\) 条 request 的联合邻域大小为 \(r_{(k)}\)；Hall 必要性给出
\(r_{(k)}\ge k\)。反过来，若这些不等式都成立，按排序把第 \(k\) 条分配到层 \(k\)，
即得到层不复用的匹配。证毕。

式 (7) 的组合部分与已有的 q-prefix Hall 正规化相同；本卡的新内容是 (2) 给出的
**physical-carrier 到无放大前缀高度的可复现输入映射**。它是 request-to-token 注入的
拒绝条件，不是注入的构造；它不能被 candidate record 的 \(v_q(N_f)\) 直接取代。

## 3. v=5 的三个 q=19 carrier

取已有的 v=5 core-19 素数点

\[
p=1202376916441,
\qquad D_*=6303,
\qquad A=573,
\qquad q=19.
\tag{8}
\]

相应的 candidate record 是

\[
N_f=p+4AD_*
=1202391362917
=17\cdot19^3\cdot53^2\cdot3671,
\qquad v_{19}(N_f)=3.
\tag{9}
\]

三条已实际重放的 physical occurrence 提供的 carrier 不是同一种 raw object：

\[
\begin{array}{c|c|c|c}
\omega&\gamma_\omega&\gcd(\gamma_\omega,N_f)&c_{f,19}(\omega)\\ \hline
C_0& p-3&19&1\\
C_1&19&19&1\\
C_{38}&38&19&1
\end{array}
\tag{10}
\]

其中 \(C_0,C_1\) 是双叶的 raw endpoint/cofactor carrier；\(C_{38}=38\) 是第三条
raw leaf 的 physical tail \(z=38t_2\) 中的 cofactor carrier，**并不是**该 raw word
的 endpoint。这个区别正是本合同保留 \(\gamma_\omega\) 类型的原因。

由 (5)--(6)，任意两个载体已经有

\[
\left|\bigcup\mathcal I_\omega\right|=1<2,
\qquad
\operatorname{def}^{\rm car}_{f,19}=1,
\tag{11}
\]

三者一起则有

\[
\left|\bigcup\mathcal I_\omega\right|=1<3,
\qquad
\operatorname{def}^{\rm car}_{f,19}=2.
\tag{12}
\]

所以在这个无放大合同内，\(v_{19}(N_f)=3\) 不能支付三个**已提议的**
carrier-subset request：
每一个 carrier 实际只含同一个一层的 \(19\) 因子。既有 candidate fiber 的
shared-q ledger 所给的深度 \(d_{19}=3\) 来自具名来源标签 \(a_0=3,a_1=573\)，不等于
这三条 physical carrier 已各自取得三层中的一个。

## 4. 实际 raw endpoint 的校准

同一 v=5 点已有一条真正的 raw-to-cofactor 正控制：在 \(A=11\) 的 candidate record

\[
N_{11}=p+4\cdot6303\cdot11
=7^2\cdot347\cdot70715591
\tag{13}
\]

中，actual raw word

\[
(0,p),(1,5),(1,5),(0,119092570771)
\tag{14}
\]

到达 endpoint \(H=7\)。于是

\[
v_7(H)=1<2=v_7(N_{11}).
\tag{15}
\]

这说明 (2) 不是仅为 C38 设计的负面措辞：即使有完整 actual raw endpoint，endpoint
本身也只认证其自身含有的一个 \(7\)-层。把 \(N_{11}\) 的第二个 \(7\)-层附到同一
receipt，仍需要一个独立的 provenance/source-switch 回执。

## 5. 不能越过的边界

本卡的 Hall 缺口是一个 **条件性局部 allocation obstruction**，应记为
`CARRIER_SUBSET_QPREFIX_MATCHING_DEFICIT`，不是 Type II
`Q_PREFIX_MATCHING_DEFICIT`，原因如下：

1. 三条 v=5 occurrence 尚未被证明为三个 typed Fourier/source demand；现有
   \(19\)-初等方向至多给出一个 rank 方向，不能把 1215 点的 F-box 当成 1215 条请求；
2. (2) 是新增的 carrier-subset 语义，不是现有 source label/source-switch 合同的推论。
   在 request-to-token 注入、source-switch、CRT、SNF、范围和 `FIBER_REALIZED` 尚未闭合时，
   三条记录都只是不带价格的 incidence。一个完成的 adapter 可以以额外的整数输入申请
   更高层，但必须显式显示该输入；
3. 相位 provenance 的条件性重建 \((C_0,C_1,C_{38})\mapsto(0,1,3)\) 使用共同 q-free
   base \(53\cdot3671\) 的未来证明，不能从 (10) 的 carrier gcd 读出，因而不与本定理
   矛盾；
4. 本点已有 \((m,d)=(3,11)\) 的直接 Type II terminal，所有上述对象均为
   terminal-preempted analysis evidence，不能登记 selector edge。

因此，新接口给统一选择器的具体要求是：任何从 physical carrier 进入 q-prefix 的边，
要么满足 (2)，要么附带一个可审计的 **carrier amplification receipt**，明确给出额外
\(q\)-因子来自哪个 raw endpoint、source label、q-free base 或 source-switch。只有后者
再通过完整 Type II 门时，才有资格进入既有的 shared ledger、rank 与 Kneser 价格账本。

窄复现：

~~~
python3 reproductions/type_i_c3_adaptive_core19_v5_carrier_subset_q19_prefix_obstruction.py --verify
~~~
