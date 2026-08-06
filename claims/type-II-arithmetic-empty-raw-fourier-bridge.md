---
kind: claim
claim_id: type-II-arithmetic-empty-raw-fourier-bridge
title: Type II 算术提升全空到 raw Fourier 的闭合桥
statement: 对 Hall 混合因子 h 的同模数、严格降模和 raw 三类算术候选，若三者全部为空，则 raw 候选集必为空；将其对应的 admissible 平方除子残数集与目标残数作差，Parseval 给出严格正的非平凡 Fourier 能量。故 ALL_ARITHMETIC_LIFT_EMPTY 必须先精化为 RAW_DIVISOR_FOURIER、可提升的 SOURCE_RELATION_FOURIER 或显式 LIFT_OBSTRUCTED，不能直接作为无后继结论。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-raw-divisor-residue-fourier-certificate
  - type-II-hall-bundle-target-residue-fourier-gate
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-raw-e1-anchor-relation-obstruction-bridge
topics:
  - type-II
  - arithmetic-lift
  - raw
  - Fourier
  - Parseval
  - obstruction
  - SNF
  - Hall
sources:
  - claim: type-II-hall-fiber-arithmetic-closure-trichotomy
    role: all-three-empty-input
  - claim: type-II-raw-divisor-residue-fourier-certificate
    role: raw-empty-Parseval-certificate
  - claim: type-II-hall-bundle-target-residue-fourier-gate
    role: exponent-screen-and-Fourier-dispatch
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-lift-test
  - claim: type-II-raw-e1-anchor-relation-obstruction-bridge
    role: e1-environment-dispatch
visibility: public
last_checked: '2026-08-05'
---

# Type II 算术提升全空到 raw Fourier 的闭合桥

## 1. 输入

固定 \(p,D\)、\(M=4D\)，以及一个由带来源 Hall 匹配得到的混合因子
\[
h=\prod_i h_i,\qquad h\equiv-1\pmod M,\qquad h\mid p+4Da_0.
\]
算术闭合三分使用三个有限候选集：
\[
\mathscr C_{\mathrm{same}}(h),\qquad
\mathscr C_{\mathrm{lower}}(h),\qquad
\mathscr R_{\mathrm{raw}}(h;p).
\]
其中 raw 集是所有
\[
(A,C,K),\qquad ACK=L:=\frac{h+1}{4},
\]
满足
\[
h\mid Kp+A,\qquad A\le\frac{Kp+A}{h}
\]
的三元组。

若三类均为空，回执为
\[
\mathrm{ALL\_ARITHMETIC\_LIFT\_EMPTY}.
\tag{1}
\]

## 2. 全空蕴含 raw 空集

由 (1) 立即有
\[
\mathscr R_{\mathrm{raw}}(h;p)=\varnothing.
\tag{2}
\]
令
\[
t_0\equiv Da_0\pmod h
\]
并定义 raw admissible 残数集
\[
\mathcal S_{L,p}^{\mathrm{ord}}
=
\left\{
Ad\bmod h:
d\mid L,\ A\mid d,\
\frac Ld(p-4Ad)+2A\ge0
\right\}.
\tag{3}
\]
raw 残数判据给出
\[
\mathscr R_{\mathrm{raw}}(h;p)\ne\varnothing
\iff
t_0\in\mathcal S_{L,p}^{\mathrm{ord}}.
\tag{4}
\]
所以 (2) 等价于
\[
t_0\notin\mathcal S_{L,p}^{\mathrm{ord}}.
\tag{5}
\]

这里同模数和严格降模候选的空缺只说明旧纤维菜单失败；真正触发 Fourier
闭合的是 raw 集的空缺 (2)，其候选范围已经包含所有 \(ACK=L\) 的 raw 正规形。

## 3. Parseval 闭合

在 \(G_h=\mathbb Z/h\mathbb Z\) 上令
\[
f=1_{\mathcal S_{L,p}^{\mathrm{ord}}}-\delta_{t_0}.
\]
由 (5) 支持不相交。对未归一化 Fourier 变换
\[
\widehat f(j)=\sum_{x\in G_h}f(x)e^{-2\pi ijx/h}
\]
有
\[
\widehat f(0)=|\mathcal S_{L,p}^{\mathrm{ord}}|-1,
\]
以及
\[
\sum_{j=1}^{h-1}|\widehat f(j)|^2
=
h\bigl(|\mathcal S_{L,p}^{\mathrm{ord}}|+1\bigr)
-\bigl(|\mathcal S_{L,p}^{\mathrm{ord}}|-1\bigr)^2
>0.
\tag{6}
\]
严格正性来自
\(0\le|\mathcal S_{L,p}^{\mathrm{ord}}|\le h-1\)。因此存在非平凡
\(j\) 使 \(\widehat f(j)\ne0\)，并可取幅度最大的最小频率作为规范回执：
\[
\mathrm{RAW\_DIVISOR\_FOURIER}
=(h,t_0,\mathcal S_{L,p}^{\mathrm{ord}},j,\widehat f(j)).
\tag{7}
\]

这不是把 raw 空集当作 Type II；(7) 只证明目标残数与全部 raw 候选残数在有限
加法商上可被非平凡角色分离。

## 4. 源关系提升分派

频率 \(j\) 先通过源关系商指数筛：
\[
\frac h{\gcd(h,j)}\mid \exp(H).
\tag{8}
\]
若 (8) 失败，直接记录该频率的 LIFT_OBSTRUCTED。若 (8) 通过，则用循环同余
或有限阿贝尔 SNF 检查源单位和锚点的仿射相容性：

1. 至少一个规范频率通过 SNF：得到 SOURCE_RELATION_FOURIER，可进入 F/G
   相位或容量接口；
2. 所有阶允许频率的 SNF 均失败：记录
   \(\mathrm{ARITHMETIC\_FOURIER\_LIFT\_OBSTRUCTED}\)，保留失败行和关系；
3. 指数筛后的总能量为零：当前源群的角色完全看不见该 raw 空洞，必须换环境商、
   稳定子纤维或良基递降，不能继续在同一角色菜单重复搜索；若
   \(e=\gcd(h,\exp H)>1\)，先调用
   [Type II raw 空集的核参数 Fourier relay](type-II-raw-divisor-residue-fourier-certificate.md)
   的 (14)--(19)，得到严格的加法核状态 \(h\to h/e\)，再检查其源关系提升。
   核状态随后按 (20)--(21) 分为可提升角色容量、
   RAW_PARAMETER_KERNEL_LIFT_OBSTRUCTED 或
   RAW_PARAMETER_KERNEL_CAPACITY_DEFICIT；只有 \(e=1\) 时才没有非平凡的允许核层。
   当 \(e=1\) 时，若已有环境目标纤维表示 \(S=\alpha R\)，转入
   [Type II raw e=1 空洞的锚点—源关系—提升障碍三分](type-II-raw-e1-anchor-relation-obstruction-bridge.md)：
   \(\alpha\notin\langle R\rangle\) 且 \(\langle R\rangle\ne1\) 时先检查严格商
   E1_ANCHOR_QUOTIENT_SOURCE_SWITCH；Q1--Q4 失败则保留
   E1_ANCHOR_QUOTIENT_LIFT_OBSTRUCTED 与锚点 Fourier。
   \(\langle R\rangle=1\) 时只给出 E1_ANCHOR_SEPARATING_FOURIER；
   \(\alpha\in\langle R\rangle\) 给出源关系能量三分；没有环境嵌入时只能保留
   E1_ENVIRONMENT_UNREALIZED，不能把参数频率继续重复枚举。
   商菜单的 CRT 不相容、算术空集和目标映射 SNF 失败分别保留其最小回执及
   参数关系 Fourier/SNF 对偶行，不得合并成无类型的 LIFT_OBSTRUCTED。

因此 ALL_ARITHMETIC_LIFT_EMPTY 的规范分派不是一个无向终点，而是
\[
\text{Type II}
\ \text{(若其它候选非空)}
\quad\text{或}\quad
\text{RAW\_DIVISOR\_FOURIER}
\ \longrightarrow\
\text{SOURCE\_RELATION\_FOURIER/LIFT\_OBSTRUCTED}.
\tag{9}
\]

## 5. Hall 闭包中的作用

在 Hall 最小割的 HC2 分支中，若某个请求触发
ALL_ARITHMETIC_LIFT_EMPTY，应先执行 (7)--(8)：

- 可提升 Fourier 角色转入锚点—秩、Rado 容量或 F/G 出口；
- 提升失败转为显式的算术关系障碍，并保留当前混合因子和全部失败频率；
- 只有在跨纤维来源未实现、或角色没有 F/G/严格递降承接时，才保留
  UNRELAYABLE_HALL_DEFICIT。

这一步缩小了 HC2 的未闭合范围，但不声称任意 Fourier 障碍自动给出核心素数下降。

## 6. 边界例子

在 \(p=97,D=6,h=143,a_0=133\) 的混合因子中，同模数、严格降模和 raw
三类候选均为空，故 (2) 成立。raw 残数集与 \(t_0=6\cdot133\bmod143\)
分离，(6) 给出至少一个非平凡参数频率；源商指数筛和 SNF 再决定它能否成为
真实 F/G 角色。无论提升结果如何，不能把该行直接写成“没有任何证书”。

## 研究边界

该桥把算术三分的 ALL_ARITHMETIC_LIFT_EMPTY 精化为一个确定的 Fourier/障碍
流程，消除了“raw 空集但无后续 typed 出口”的表述漏洞。它仍未证明可提升频率
一定造成容量超载，也未证明不可提升障碍必然产生严格整数递降；这两点仍是全局
HC 的核心剩余。
