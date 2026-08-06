---
kind: claim
claim_id: type-I-high-anchor-minimal-positive-phase-fixed-n-bridge
title: 高锚点最小正相位到固定 n 饱和递降的强制桥
statement: 设通过 gate 的高 canonical anchor 的 direct cofactor r-chart 处于最小正相位，且完整 direct r-chart 范围 1<=r,C<p 保留不删；即 h in {1,2}、q=h+1、e=c-q=0。则 A_T=qA=C<p、a=1、pn=4A_T d_T+1，其中 n=4A-R，并且自动有 5<=n<=p-4、d_T>=2。故 S=A_T d_T=(pn-1)/4 满足 A_T<S<=B_p=(p-1)^2/4；取 L=S 的 fixed-n pivot 给 R_L=(p-1)n-1>p、K_L=S(p-1)，并严格降低 Pi_p(A)=floor(B_p/A)：Pi_p(L)<Pi_p(A_T)。因此，只要最小正相位 target 已有完整 terminal-first、E1--E4 的 verified overflow receipt，固定-n bounded-divisor theorem 即给出一条严格 Pi-paid 可提升后继；该桥不把仅有算术或 local candidate 的 target 自动登记为 selector edge。一般 fixed-n 饱和中 n=1 的 marked_absorb 分支存在，但它与本引理的高锚最小正相位及 C<p 假设不相容；若删去 C<p，p=73 有 d_T=1 的形式反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-positive-phase-terminal-boundary
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
topics:
  - type-I
  - high-carrier
  - positive-phase
  - fixed-n
  - bounded-divisor
  - outer-rank
  - terminal-first
  - proof-bridge
sources:
  - reproduction: reproductions/type_i_high_anchor_minimal_phase_fixed_n_bridge.py
    role: targeted arithmetic and local-macro control replays
  - result: reproductions/type-i-high-anchor-minimal-phase-fixed-n-bridge-results.json
    role: frozen targeted bridge receipt
visibility: public
last_checked: '2026-08-06'
---

# 高锚点最小正相位到固定 n 饱和递降的强制桥

## 1. 范围

固定核心素数 \(p\equiv1\pmod {24}\)。设高 canonical anchor 为

\[
pR+1=4K,\qquad K=AB,\qquad p<R<4A.
\tag{1}
\]

考虑一个已经通过 cofactor gate 的 direct \(r\)-chart，并处于正相位的最小
分支。完整的 direct chart 范围是

\[
1\le r,C<p.
\tag{2a}
\]

它在后面的 \(d_T\ge2\) 推导中不可省略。沿用三相引理和正相位余量卡的记号：

\[
h\in\{1,2\},\quad q=h+1,\quad e=c-q=0,
\tag{2}
\]

\[
a=1,\qquad A_T=qA=C<p,\qquad d=p-B=q d_T,
\tag{3}
\]

其中 target chart 是

\[
K_T=A_Tt,\qquad t=p-d_T,\qquad R_T=4A_T-n,
\tag{4}
\]

并且 anchor 的 canonical residual 为

\[
n=4A-R.
\tag{5}
\]

式 (3)--(5) 正是最小相位的 fixed-\(n\) shadow；本卡补足此前未写出的
结论：它自动落在已有 fixed-\(n\) 饱和递降的输入域。

这里的结论是一个**后继桥**。它假设 (1)--(4) 已来自完整的、terminal-first
之后仍允许入队的 target receipt；仅有 r-chart 算术、source-only overflow 或 local
candidate 时，本卡不授权登记任何 selector edge。

## 2. 强制的 residual 窗口

由高锚条件，

\[
0<n<4A-p.
\tag{6}
\]

又由 \(A_T=qA<p\)，当 \(q=2\) 时 \(4A-p=2A_T-p<p\)，当 \(q=3\) 时

\[
4A-p=\frac{4A_T}{3}-p<\frac p3<p.
\tag{7}
\]

所以 \(0<n<p\)。canonical chart 方程给出 \(n\equiv1\pmod4\)。

剩余值 \(n=1\) 在一般 fixed-\(n\) 饱和中会给出 \(R_S=p-2\) 的
`marked_absorb`，但这里不可能发生。若 \(n=1\)，则 target determinant 为

\[
p=4A_Td_T+1=4qAd_T+1.
\tag{8}
\]

另一方面 \(R=4A-1\)，而 \(qd_T\ge2\)，故 \(p>R\)，与 (1) 矛盾。
因此

\[
\boxed{5\le n\le p-4.}
\tag{9}
\]

同样，\(d_T=1\) 不可能。否则 (4) 的 determinant 关系给

\[
pn=4A_T+1<4p+1,
\tag{10}
\]

即 \(n\le4\)，与 (9) 矛盾。因此

\[
\boxed{d_T\ge2.}
\tag{11}
\]

这两条不等式不是新增的数论猜测，而是高锚最小相位加上完整 \(C<p\)
direct-chart 范围的直接代数后果。

## 3. 固定 n 饱和 pivot

由 target 的 chart 方程，

\[
pn=4A_Td_T+1.
\tag{12}
\]

令

\[
S=A_Td_T=\frac{pn-1}{4},\qquad L=S.
\tag{13}
\]

由 (11)，\(A_T<S\)。由 (9)，

\[
S=\frac{pn-1}{4}
\le\frac{p(p-4)-1}{4}<\frac{(p-1)^2}{4}=B_p.
\tag{14}
\]

所以 \(L=S\) 是 fixed-\(n\) bounded-divisor theorem 的最大可用 divisor。
此外 \(4S=pn-1>n\)，故它也满足该定理的正 chart 条件。
它给出

\[
R_L=4L-n=(p-1)n-1,
\qquad K_L=L(p-1).
\tag{15}
\]

因为 \(n\ge5\)，\(R_L>p\)，故这个 pivot 不是吸收状态而是严格递归 overflow。

再由 \(S\ge2A_T\) 和 \(A_T<p\)，有

\[
\left\lfloor\frac{B_p}{S}\right\rfloor
\le\left\lfloor\frac{B_p}{2A_T}\right\rfloor
<\left\lfloor\frac{B_p}{A_T}\right\rfloor.
\tag{16}
\]

末端严格性可由 \(p\ge73\) 得到：
\(B_p/A_T\ge(p-1)/4\ge18\)。因此

\[
\boxed{\Pi_p(L)<\Pi_p(A_T).}
\tag{17}
\]

这说明最小正相位并非只停在一个没有支付的 fixed-\(n\) shadow；只要其 target
能够作为合法状态进入 fixed-\(n\) 子程序，下一步的外层秩支付是强制的。

## 4. E1--E5 的精确继承条件

该桥不替代高锚 macro 的 admission。要把 (15) 写成 selector 后继，先前的最小
正相位 target \(T\) 必须已经满足：

1. 有完整 parent/source/path receipt，且 terminal 与已注册 alternate 已先检查；
2. 以 \(M=A_T,d=d_T\) 记录为 verified overflow，故 \(A_T\mid M\) 与 (12) 都在
   state contract 内；
3. 有图表无关的 \(W_T=\operatorname{Sol}(p)\) 及恒等 marked lift。

在这些前提下，(12)--(15) 是 fixed-\(n\) theorem 的 E2/E3 算术回执；E1 由已验证
target 的来源链继承，E4 由同一个 \(\operatorname{Sol}(p)\) 的恒等 lift 继承，(17)
支付 E5。若 target 只是 `analysis_evidence`、`candidate_transition`，或者该素数已在
terminal-first 步骤停止，本桥只保留为分析事实，不能绕过该 gate。

## 5. 定向控制例

专用回放重算了两个 \(p=1201\) 的 arithmetic-only 最小相位，及两个已有的 local
macro control：

| \(p\) | \(h\) | \(A_T\) | \(d_T\) | \(n\) | \(S\) | \(\Pi_p(A_T)\to\Pi_p(S)\) | provenance |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1201 | 1 | 638 | 8 | 17 | 5104 | 564 to 70 | arithmetic-only |
| 1201 | 2 | 1038 | 35 | 121 | 36330 | 346 to 9 | arithmetic-only |
| 3793 | 1 | 3622 | 61 | 233 | 220942 | 992 to 16 | local candidate |
| 60913 | 2 | 55941 | 634 | 2329 | 35466594 | 16581 to 26 | local candidate |

四行都通过 (12)--(17)。前两行没有 provenance，后两行目前也因 terminal-first/宏
admission 状态而不是全局 selector edge；它们验证的是桥的算术，而不是对全局闭包的
经验声称。

回放还保留一个排除控制：若错误删除 \(C<p\)，则

\[
p=73,\quad h=1,\quad A=82,\quad (R,K)=(319,5822),
\quad C=A_T=164,\quad r=72
\]

形式上满足 \(e=0\)、\(n=9\)、\(d_T=1\) 及 target chart，但 \(C>p\)，不属于
direct \(r\)-chart。此时 \(S=A_T\)，严格支撑增长和 (16) 的支付都消失。它说明
本桥不是单由高 chart 与相位等式推出，\(C<p\) 必须作为显式 contract 字段。

重放命令：

```bash
python3 reproductions/type_i_high_anchor_minimal_phase_fixed_n_bridge.py --verify
```

## 6. 含义与边界

非最小正相位 \(e\ge1\) 仍会将 \(n_T\) 推出 \(0<n<p\)，不在本桥范围内。最小相位
则获得一个确定的两段结构：先进入同 residual 的 target，再强制进入严格
\(\Pi_p\)-下降的 fixed-\(n\) pivot。当前剩余缺口不是第二段的算术，而是第一段
macro 的 global terminal-first admission 与 charged-history E1/E4 receipt。
