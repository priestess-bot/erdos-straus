---
kind: claim
claim_id: type-I-high-anchor-positive-phase-one-shot-token
title: 高锚点 cofactor r-图表链的正相位一次性令牌
statement: 固定素数 p，在同一 source_tree_scope 内，沿不 RESET 的 canonical、通过代数 gate 的高锚点 cofactor r-图表链，正相位 h>0 至多出现一次。更强地，任意两个相邻的这类迁移不可能同时有正整数相位；插入的 h=0 迁移要么是完全停顿，要么把已消费令牌后的支撑推至大于 p，永久排除新的正相位。该令牌不处理 h=0 停顿、外部 support promotion、RESET 或重新锚定，不能单独形成全局 E5 秩。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-same-chart-support-promotion
topics:
  - type-I
  - high-carrier
  - r-chart
  - nonreturn
  - phase-token
  - charged-support
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_r_chart_p3793_audit.py
    role: h=1 G-parented local control
  - reproduction: reproductions/type_i_high_r_chart_7393_nonreturn.py
    role: h=1 all-F local control
  - reproduction: reproductions/type_i_high_r_chart_60913_h2_nonreturn.py
    role: h=2 G-to-G-to-F local control
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 cofactor r-图表链的正相位一次性令牌

## 1. 链与记号

固定 \(p\equiv1\pmod4\)。考虑同一 `source_tree_scope` 内的一条直接 cofactor
\(r\)-chart 链；每一步都满足

\[
pR_i+1=4K_i,\qquad A_i\mid K_i,\qquad p<R_i<4A_i,
\tag{1}
\]

以及

\[
1\le r_i,C_i<p,\qquad pR_{i+1}+1=4r_iC_i,
\qquad A_{i+1}=\operatorname{lcm}(A_i,C_i)\mid r_iC_i.
\tag{2}
\]

这里没有插入 RESET、fresh-root 重建或外部 support promotion。令

\[
h_i=\frac{r_iC_i-K_i}{pA_i}.
\tag{3}
\]

三相引理保证 \(h_i\in\{0,1,2\}\)，但下面的相邻正相位排除只需
\(h_i,h_{i+1}>0\)，不使用这个上界。

写 \(K_i=A_iB_i\)、\(g_i=(A_i,C_i)\)、\(A_i=g_i a_i\)、
\(C_i=g_i c_i\)。gate 给出 \(r_i=a_i t_i\)，且

\[
A_{i+1}=A_ic_i,\qquad K_{i+1}=r_iC_i=A_{i+1}t_i,
\qquad c_it_i=B_i+ph_i.
\tag{4}
\]

若 \(h_i>0\)，则 \(a_it_i=r_i<p\)，故现有的相位支付界给出

\[
c_i\ge h_i a_i+1\ge h_i+1.
\tag{5}
\]

此外，任一正相位的 source 都满足

\[
A_i(B_i+ph_i)=r_iC_i\le(p-1)^2,
\]

所以

\[
\boxed{h_i>0\quad\Longrightarrow\quad
A_i\le\frac{(p-1)^2}{p+1}<p.}
\tag{6}
\]

这条 source barrier 后面用于阻断令牌的再次消费。

## 2. 相邻正相位不可能

**引理。** 若第 \(i\) 步与第 \(i+1\) 步都是 (1)--(2) 的直接迁移，则不可能
同时有 \(h_i>0\) 与 \(h_{i+1}>0\)。

**证明。** 为简洁略去下标，令第一步的相位为 \(h>0\)，下一步为 \(h'>0\)，
并使用 (4) 的 \(B,c,t\)。由当前 chart 的规范上界 \(R\le4A-1\)，

\[
B=\frac{pR+1}{4A}
\le p-\frac{p-1}{4A}<p.
\tag{7}
\]

第一步的 source 是高锚点，故

\[
p^2< pR+1=4K=4A(ct-ph).
\tag{8}
\]

而第二个 target 满足

\[
K_2=K_1+pA_1h'=Ac(t+ph')=r_{i+1}C_{i+1}\le(p-1)^2<p^2.
\tag{9}
\]

由 (8)--(9) 消去 \(A\)，得到

\[
3ct>p(ch'+4h).
\tag{10}
\]

另一方面，(4)、(5)、(7) 给出

\[
3ct=3(B+ph)<3p(h+1)
\le p(5h+1)
\le p(ch'+4h),
\tag{11}
\]

与 (10) 矛盾。证毕。

## 3. 零相位不能重新开启令牌

设链中已经出现一条正相位。由 (1)、(5)，其 target support 满足

\[
A_{i+1}=A_ic_i\ge2A_i>\frac p2.
\tag{12}
\]

其后的零相位有两种情形：

\[
\begin{array}{c|c|c}
h=0,\ c=1 & (R,K,A)\ \text{完全不变} & \text{可压缩的停顿}\\
h=0,\ c>1 & A_T=cA_S\ge2A_S>p & \text{永久越过 (6) 的 source barrier}
\end{array}
\]

第一行由 \(h=0\) 的 \(R_T=R\)、\(K_T=K\) 及 \(A_T=Ac=A\) 直接得到。若
所有插入的零相位都是第一行，删去它们后会得到两条相邻正相位，违反第 2 节。若其中
一条属于第二行，之后所有直接 cofactor 步的 support 都保持不降，而 (6) 排除任何新的
正相位。

因此在整条链上

\[
\boxed{\#\{i:h_i>0\}\le1.}
\tag{13}
\]

这可作为不可重置的状态位 `high_nonreturn_token: 1 -> 0`：一旦消费，后续
cofactor r-chart 迁移不能再次消费。

## 4. 锐利边界与调度含义

高锚点条件不能删去。例如 \(p=13\) 有低 chart 链

\[
(A,R,K)=(1,3,10)
\xrightarrow{(r,C,h)=(9,4,2)}
(4,11,36)
\xrightarrow{(r,C,h)=(11,8,1)}
(8,27,88),
\]

每一步都满足 chart 和 gate，但前两张图表都不是高锚点，故连续正相位确实会发生。

在高锚点内，\(p=60913\) 的专用回执给出存在的最小 \(h=2\) 消费
\(A=18647\to55941=3A\)，而 \(p=3793\) 和 \(p=7393\) 给出 \(h=1\) 控制例。
这些均是 local candidate；它们的 terminal-first 证书不把本引理提升为完整选择器。

令牌只关闭同一 scope 中、直接 cofactor 子程序的“重复正 non-return”缺口。它不处理
\(h=0\) 的零成本停顿、不同 bundle 的外部调度、same-chart support promotion、RESET、
重新锚定或跨 \(p\) 迁移；这些仍需要外层的 rank、capacity 或 terminal-first 规则。
