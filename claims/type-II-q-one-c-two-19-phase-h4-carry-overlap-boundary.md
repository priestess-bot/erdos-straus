---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
title: q=1 高 C=2 19 相位 H4 carry-overlap、Type I carrier/reset 边界与有限标签边界
statement: >-
  在 q=1 high C=2 19 相位每个未被 H3 terminal 抢占、经最大 complete-excess
  构造到 H4 的状态中，令 L=M4/M3、c4 为 H4 canonical capacity，并定义唯一第四 carry
  s4=(L*c4-c3)/p。则 0<=s4<L，且 H4 p-anchor 的精确 overlap 为
  gcd(R4-1,K4)=2*gcd((p+1)/2,c3-s4)。所以该 gcd 的任一 3 (mod 4) 素因子给出
  可直接核验的 Type II raw-ray 证书，但同一素因子已经给出根级 p+1 Type I 证书；故在
  p+1 terminal-first 后，该 H4 gate 不增加全局 terminal 覆盖。同时 L(c4-c3)=p*s4-c3(L-1)
  精确判定本地 capacity 势方向。H4 的 R4 具有超过 p^3/2 的下界，而任一标准 Type I
  正规形的合法图表总满足 mR-1<=(p+m)^2/4<=(p-1)^2。更强地，任何同一 p 的
  标准 Type I 图表都必须满足 R_I<R4/p、K_I<K4/p；因此保留同一
  (p,R4,K4) 的 typed Type I reclassification 都不可能存在。这给出换图表所需的
  超过 p 倍高度塌缩。进一步，H4 的 charged carrier M4 已超过任何标准 Type I 的
  K 上界，所以任何保留 M4|K_I 的 Type I 目标（特别是 lcm 支撑扩张）也不可能。
  H4 仍可精确写为 A=M4>B_p 的 overflow，但现有 joined-support outer-rank RESET
  只允许 A<=B_p，故不能作为该状态的已登记 reset。这不声称 H4 本身已有 Type I
  正规形，也不排除高支撑 carry continuation、新型已付款 reset 或实际换图表路径。H4 的首个
  最大 complete-excess anchor 候选在 p=14449 时 c5<c4、在 p=665617 时 c5>c4，故其
  carry 势方向不统一，不能自动作为全域出口。然而 H4 overlap 与该势方向都不由此前的有限 H3 标签
  (u mod 119,a,g,lambda) 决定：p=184993 与 p=727633 均有
  (u,a,g,lambda)=(83,1723,1,1) 且 H3 clean，但 H4 的奇 overlap 分别为 1 与 17。
  另有 p=448561 与 p=665617 共享 (u,a,g,lambda)=(15,431,1,1)，但前者 c4>c3、
  后者 c4<c3。因此不能把 H3 的有限 mask 直接当作 H4 全域 selector 或势下降证明；
  任何继续该路线的 selector 至少必须携带 s4（或等价的实际 H4 carry）信息。该结果没有证明
  H4 总能终端或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-raw-ray-certificate
  - p-plus-one-sqrt-certificate
  - type-I-normal-chart-height-bound
  - type-I-overflow-outer-rank-reset
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - carry-capacity
  - terminal-first
  - short-certificate
  - strict-counterexample
  - selector-boundary
  - terminal-preemption
  - p-minus-one
  - same-chart-no-go
  - cross-chart-height-collapse
  - carrier-retention
  - overflow-reset
  - high-support-carry
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: H3-to-H4-maximal-excess-construction
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: H3-coprime-support-and-terminal-dispatch
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: high-H3-capacity-lower-bound
  - claim: type-II-raw-ray-certificate
    role: overlap-factor-to-Type-II-certificate
  - claim: p-plus-one-sqrt-certificate
    role: root-level-terminal-preemption
  - claim: type-I-normal-chart-height-bound
    role: standard-normal-form-height-necessary-condition
  - claim: type-I-overflow-outer-rank-reset
    role: current-joined-support-reset-domain
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: H4-canonical-high-support-carry-interface
  - concept: denominator-escape-state-contract
    role: named-normal-form requirement for a legal recursive state
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary.py
    role: exact-carry-identity-and-label-boundary-controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的 H4 carry-overlap、Type I carrier/reset 边界与有限标签边界

## 1. H4 的缺失状态变量

保留最大 complete-excess H3 \(\Rightarrow\) H4 构造的记号。令

\[
w=\frac{p+1}{2},
\qquad
M_4=M_3L,
\qquad
K_4=M_4c_4,
\qquad
pR_4+1=4K_4,
\tag{1}
\]

其中 \(L=M_4/M_3>1\)，并且 \(c_4\) 是唯一满足

\[
c_4\equiv c_3L^{-1}\pmod p,
\qquad 1\le c_4\le p-2
\tag{2}
\]

的 canonical capacity。因此有唯一整数

\[
\boxed{s_4=\frac{Lc_4-c_3}{p}.}
\tag{3}
\]

它不是可忽略的记账量。由于 \(L\ge2\) 且 \(1\le c_3,c_4\le p-2\)，

\[
-p<Lc_4-c_3<Lp.
\]

左式又是 \(p\) 的倍数，故

\[
\boxed{0\le s_4<L.}
\tag{4}
\]

这是 H4 canonicalization 的真实 carry，而非新的自由选择。

## 2. 精确 H4 anchor-overlap 恒等式

此前 H3 的精确计算给出

\[
p\equiv1\pmod {16},
\qquad (w,M_3)=1,
\tag{5}
\]

并且 \(M_3\) 为偶数。最大超额块和其与 \(M_3\) 的 overlap 都为奇数，故 \(L\)
为奇数、\(K_4\) 为偶数，且 \(p\nmid K_4\)。从 (1) 得

\[
\begin{aligned}
(R_4-1,K_4)
&=(p+1,K_4)\\
&=2(w,K_4)\\
&=2(w,Lc_4).
\end{aligned}
\tag{6}
\]

另一方面，(3) 和 \(p\equiv-1\pmod w\) 给出

\[
Lc_4=c_3+ps_4\equiv c_3-s_4\pmod w.
\tag{7}
\]

合并 (6)--(7)，得到所需的完整公式

\[
\boxed{(R_4-1,K_4)=2\,(w,c_3-s_4).}
\tag{8}
\]

因此 H4 的 complete-excess/anchor selector 不应只继承 H3 的 \(g=(w,c_3)\)：
它需要实际 carry residual \(c_3-s_4\)。

同一个 carry 也精确支付容量变化：由 (3)，

\[
\boxed{L(c_4-c_3)=ps_4-c_3(L-1).}
\tag{9}
\]

所以 \(c_4<c_3\) 当且仅当右端为负。这个判据不把 H3 \(\Rightarrow\) H4 自动
称为 local capacity descent；先前的 persistent 宏只比较其终点与 \(P\) 的 \(p-1\)
容量。

## 3. 状态局部的 Type II terminal 与根级预先截断

设 \(\ell\equiv3\pmod4\) 是 \((w,c_3-s_4)\) 的一个素因子。则
\(\ell\mid p+1\)。取

\[
A=1,
\qquad C=\frac{\ell+1}{4},
\qquad k=1,
\qquad B=\frac{p+1}{\ell}.
\tag{10}
\]

有 \(4ACk-1=\ell\mid kp+A\)，故 raw-ray 公式给出一张合法 Type II
证书。这是一个可核验的 H4 terminal gate；它没有声称 \(\ell\) 在所有状态存在，
也没有声称 \(C\) 有统一常数上界。

但这个 gate 不能为根级 terminal-first selector 增加新的覆盖。事实上，\(\ell\mid w\)
且 \(\ell\equiv3\pmod4\)。直接令

\[
x=\frac{p+\ell}{4},
\qquad d=x,
\qquad y=\frac{x(p+1)}{\ell},
\qquad z=py.
\tag{11}
\]

则 \(\ell\mid px+d=x(p+1)\)，并且 \(d=x\mid x^2\)，所以 \((\ell,d)\)
是根素数 \(p\) 的直接 Type I 除子证书。这正是
[\(p+1\) 平方根证书](p-plus-one-sqrt-certificate.md)的同一构造；取最小的
\(3\pmod4\) 因子时还得到其平方根界。

因此有严格包含关系

\[
\boxed{
 \{p:\text{H4 overlap gate 有 }3\pmod4\text{ 因子}\}
 \subseteq
 \{p:\text{\(p+1\) Type I terminal 存在}\}.}
\tag{12}
\]

特别地，若根级 selector 已先检查并排除了 \(p+1\) terminal，则 \(w\) 的每个素因子
都是 \(1\pmod4\)。因为 \((w,c_3-s_4)\mid w\)，H4 overlap gate 在这一全局残余上
必为空。它仍可作为**状态局部**的 Type II 证书，但不能被当作尚未覆盖根素数的新增出口。

作为正控制，\(p=114769\) 在 H3 clean 分支上到达 H4，且

\[
(w,c_3-s_4)=23.
\]

取 \((A,C,k)=(1,6,1)\) 得

\[
\frac4{114769}
=\frac1{29940}+\frac1{688614}+\frac1{3436183860}.
\tag{13}
\]

同一个 \(\ell=23\) 也给出被预先选择的根级 Type I 证书：

\[
\frac4{114769}
=\frac1{28698}+\frac1{143203020}+\frac1{16435267402380}.
\tag{14}
\]

## 4. 同图表 Type I 正规形的绝对高度 no-go

H4 目前是 complete-excess 的 canonical capacity target，而不是已经附有三分母
Type I `normal_form` verifier 的状态。因而不能从图表恒等式直接宣布 H4 已有 Type I
前两项或 Type I 递降边。不过，若未来 typed reclassification 保留**同一**
\((p,R_4,K_4)\) 并声称得到一张标准 Type I 正规形，那么该断言已经被正规图表的必要
高度条件排除。

三 anchor 宏的首个高容量为

\[
M_0=\frac{(p-1)(2p+1)(2p^2-3p-1)}8.
\tag{17}
\]

对 \(p\ge73\)，三个因子分别严格大于 \(p/2\)、\(2p\)、\(p^2\)，故

\[
M_3>M_0>\frac{p^4}{8}.
\tag{18}
\]

另一方面，H4 有 \(M_4=M_3L\)、\(L>1\)、\(c_4\ge1\)，所以
\(M_4>M_3>M_0\) 且 \(K_4=M_4c_4>M_0\)。由 \(pR_4+1=4K_4\)，

\[
R_4=\frac{4K_4-1}{p}
>\frac{p^3}{2}-\frac1p.
\tag{19}
\]

令 \(U_R(p)\)、\(U_K(p)\) 是
[Type I 正规图表的二次高度上界](type-I-normal-chart-height-bound.md)中的全局界。则同一
\(p\) 的任意标准 Type I 正规形 \((R_{\mathrm I},K_{\mathrm I})\) 必有

\[
R_{\mathrm I}\le U_R(p),
\qquad
K_{\mathrm I}\le U_K(p).
\tag{20}
\]

对 \(p\ge73\)，(19) 与定义 \(U_R(p)\) 的实数上界之间的差为

\[
\left(\frac{p^3}{2}-\frac1p\right)
-\frac{p((p+3)^2+4)}{12}
=\frac{5p^4-6p^3-13p^2-12}{12p}>0.
\tag{21}
\]

因此

\[
R_4>pU_R(p)\ge pR_{\mathrm I}.
\tag{22}
\]

所有量均为整数，故 \(R_4-pR_{\mathrm I}\ge1\)。再由两个图表的
\(4K=pR+1\) 恒等式，

\[
\begin{aligned}
4(K_4-pK_{\mathrm I})
&=p(R_4-pR_{\mathrm I})-(p-1)\\
&\ge1.
\end{aligned}
\tag{23}
\]

所以

\[
\boxed{
R_{\mathrm I}<\frac{R_4}{p},
\qquad
K_{\mathrm I}<\frac{K_4}{p}.}
\tag{24}
\]

这给出 H4 到任意标准 Type I 图表的必要**超过 \(p\) 倍高度塌缩**。特别地，若保留
\((p,R_4,K_4)\)，取 \(R_{\mathrm I}=R_4\)、\(K_{\mathrm I}=K_4\) 会与 (24) 矛盾，
因此不存在保留 H4 同一图表的标准 Type I 正规形。

这严格强于原先的条件 \(p-1\) 最大尾桥边界：这里并非只排除该桥，而是量化地排除任何
同图表重分类，并规定换图表至少需要的尺度跃迁。它仍然不是 H4 的 typed transition，
也不排除根素数在另一张低 \(R\) 图表中有 \(p-1\) terminal、其它 \(n<p\) 的提升，或
Type II 路径。

## 5. H4 carrier 保留与现有 RESET 的双重边界

上节的塌缩是对任意标准 Type I 图表的数值必要条件。H4 的实际 carrier 还给出一个更强的
状态级限制。由 (18) 与 (20)，标准 Type I 的 \(K\) 上界满足

\[
\begin{aligned}
U_K(p)
&\le\frac{p((p+3)^2+4)+12}{48}\\
&<\frac{p^4}{8}
<M_4.
\end{aligned}
\tag{25}
\]

中间严格不等式等价于

\[
6p^4-p^3-6p^2-13p-12>0,
\]

对 \(p\ge73\) 显然成立。因此，若某个同一 \(p\) 的标准 Type I 目标
\((R_{\mathrm I},K_{\mathrm I})\) 保留 H4 的全部 charged carrier，即

\[
M_4\mid K_{\mathrm I},
\tag{26}
\]

则 \(K_{\mathrm I}\ge M_4>U_K(p)\)，与 (20) 矛盾。故

\[
\boxed{
\text{任何标准 Type I 目标都必须丢弃 H4 的完整 carrier }M_4.}
\tag{27}
\]

这也排除所有从 H4 出发的普通 complete-excess lcm 延续：这类边将 support 更新为
\(A_T=\operatorname{lcm}(M_4,Q)\)，并要求 \(A_T\mid K_T\)，因而必有
\(M_4\mid K_T\)，正落入 (26) 的矛盾。

H4 自身确实处在 overflow 语义中。令

\[
d_4=p-c_4,
\qquad
n_4=4M_4-R_4.
\tag{28}
\]

由 \(1\le c_4\le p-2\) 和 \(pR_4+1=4M_4c_4\)，有

\[
2\le d_4\le p-1,
\qquad
n_4=\frac{4M_4(p-c_4)+1}{p}>0,
\qquad
pn_4=4M_4d_4+1.
\tag{29}
\]

又 (19) 给出 \(R_4>p\)。H3 \(\Rightarrow\) H4 的 maximal complete-excess receipt
把 target ledger 更新为 \(A=\operatorname{lcm}(M_3,Q^*)=M_4\)，故 H4 是一个带旧
charged support \(A=M_4>B_p\) 的真正 overflow。现有
[overflow RESET 的 joined-support 外层秩递降](type-I-overflow-outer-rank-reset.md)要求
\(1\le A\le B_p\) 才能登记 overflow_outer_rank_reset_v1；因此它在 H4 上**不在定义域内**，
而不是某个尚待选择的 \(d/r\) 通道。

这里必须区分标准 Type I 重分类与高支撑 canonical continuation。(27) 只说明保留/扩张
\(M_4\) 的边不能**同时**成为标准 Type I 正规形；它不排除高支撑状态自己的
complete-excess carry 边。事实上 H4 已满足

\[
M_4>B_p,\qquad K_4=M_4c_4,\qquad 1\le c_4<p,
\tag{30}
\]

所以它正落在[高支撑 bundle 的精确 carry 容量门](type-I-high-support-bundle-carry-capacity-terminal-dispatch.md)
的定义域。若 H4 anchor 的唯一最大 complete-excess 块给出

\[
M_5=\operatorname{lcm}(M_4,Q_5)=M_4L_5,
\qquad
c_5\equiv c_4L_5^{-1}\pmod p,
\qquad 1\le c_5<p,
\tag{31}
\]

则唯一 carry \(s_5=(L_5c_5-c_4)/p\) 满足

\[
L_5(c_5-c_4)=ps_5-c_4(L_5-1).
\tag{32}
\]

若 H4 已作为独立 high-support 状态入队，在来源、path、F/G 重分类与 E1--E4 另行成立时，
\(c_5<c_4\) 才是这类**独立边**的 E5 门。它不是自动成立的：两个 H4 local-anchor
控制分别为

| \(p\) | H3 dispatch | \(c_4\) | \(c_5\) | carry 方向 |
|---:|---|---:|---:|---|
| \(14449\) | bounded \(q=1\) mask | \(13391\) | \(12552\) | 下降 |
| \(665617\) | clean fourth anchor | \(20388\) | \(94177\) | 上升 |

两例都避开 \(p+1\) 的 \(3\pmod4\) 因子终端，且均由同一个精确 maximal-block 算法重算。
因此不能把“取 H4 的首个最大块”登记为独立状态上的全域 E5；它只是下一条 rank-aware
sink-bundle 选择器需要处理的一个 canonical 候选。不过，H4 也可以保留为既有
\(P\Rightarrow H_4\) strict macro 的内部 checkpoint：只要第五锚的 p-source/p-free gate
通过且 \(c_5\le p-2\)，端点秩直接比较 \((0,p-1)>(0,c_5)\)，不要求 \(c_5<c_4\)。
这个更弱而可证明的 parent-macro 准入门见
[H4 \(\Rightarrow\) H5 的 parent-macro 准入门](type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate.md)。
若独立候选表与该固定宏门都严格空，才应转交 \(A>B_p\) 的新型 paid reset 或不经 \(p+1\)
因子的 Type II 短证书。这是对**当前 adapter 域**的边界，不排除已有高支撑 carry selector
的其它候选或尚未构造的新 reset。

## 6. H3 有限标签不足的严格反例

下面两点都通过 H3 clean 分支，且有相同的 H3 有限标签：

| \(p\) | \(u\) | \(a\) | \(g\) | \(\lambda\) | \(c_4\) | \((w,c_3-s_4)\) |
|---:|---:|---:|---:|---:|---:|---:|
| \(184993\) | \(83\) | \(1723\) | \(1\) | \(1\) | \(178654\) | \(1\) |
| \(727633\) | \(83\) | \(1723\) | \(1\) | \(1\) | \(594031\) | \(17\) |

所以不存在一个只读取 \((u,a,g,\lambda)\) 的函数，能够给出 H4 的精确
odd overlap \((w,c_3-s_4)\)。这不是从两个点外推整体行为，而是对该特定
有限标签 selector 的直接反例：同一输入标签被要求同时输出 \(1\) 和 \(17\)。
此前的 hard \(q=1\) mask 控制 \(p=14449\) 也满足 (8)，其
\((w,c_3-s_4)=1\)；所以该公式同时覆盖 clean 与原 mask 两类 H3 前身。

同样的有限标签也不能确定 (9) 的符号：

| \(p\) | \(u\) | \(a\) | \(g\) | \(\lambda\) | \(c_3\) | \(c_4\) | 方向 |
|---:|---:|---:|---:|---:|---:|---:|---|
| \(448561\) | \(15\) | \(431\) | \(1\) | \(1\) | \(85507\) | \(423624\) | 上升 |
| \(665617\) | \(15\) | \(431\) | \(1\) | \(1\) | \(126883\) | \(20388\) | 下降 |

故不可能仅从该 H3 标签宣布 H3 \(\Rightarrow\) H4 是严格容量递降；需要实际 \(s_4\)
或等价的 carry gate。

## 7. 边界与下一接口

式 (8) 把 H4 的状态局部 terminal 输入压缩为一个明确的 carry residual，并给出它命中时的
构造性证书；但 (12) 证明该终端在根级已被 \(p+1\) 分支预先截断。故在真正的全局残余上，
不能再试图从 \((w,c_3-s_4)\) 的 \(3\pmod4\) 因子获得新出口；(24)、(27) 进一步规定：
任何标准 Type I 重分类不仅必须大幅改变 \(R,K\)，还必须显式丢弃 \(M_4\)，而当前
joined-support reset 不具备这一权限。另一方面，(30)--(32) 保留了真正尚未解决的高支撑
接口：先检查固定第五锚的 p-source/p-free/top-capacity gate，以已有 persistent parent
把 H4 作为内部 checkpoint；其失败后才以 H4 的实际 source/path 枚举 rank-aware
complete-excess 候选，并证明 terminal 或 \(c_5<c_4\) 的完备析取。首个最大块已有正、反
两个方向的控制，故不能只重复 H3 的 \((u,\lambda)\) 有限 mask。两个接口都严格空，才需要
一个对 \(A>B_p\) 有独立良基支付的 reset，或一个不经 \(p+1\) 因子的 Type II 短证书。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary.py --verify
```
