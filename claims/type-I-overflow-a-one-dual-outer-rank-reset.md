---
kind: claim
claim_id: type-I-overflow-a-one-dual-outer-rank-reset
title: A=1 overflow 的对偶外层秩 RESET
statement: 对任一 verified overflow pn=4Md+1、1≤d<p、R_M>p 且旧 support A=1，写 M=kp+r、ps=4rd+1。令 (R_d,K_d)=(4d-s,d(p-r))、(R_r,K_r)=(4r-s,r(p-d))。两图表均为正的 3 mod 4 canonical chart，且 min(R_d,R_r)<p；其中至少存在 t∈{d,r} 满足 t>1、R_t<p。于是 t≤B_p、t|K_t、floor(B_p/t)<floor(B_p)，该 t 通过 overflow_outer_rank_reset_v1 给出完整 E1--E5、Sol(p) 恒等提升和严格外层秩下降。该定理关闭通用 A=1 的算术 RESET 子族，但不关闭 RESET 后的 A>1 overflow。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-outer-rank-reset
  - type-I-overflow-a-one-generic-determinant-boundary
topics:
- type-I
- overflow
- A-one
- dual-carrier
- outer-rank
- reset
- marked-solution
- well-founded-descent
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: dual RESET implementation and focused boundary replay
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: dual-chart arithmetic evidence
visibility: public
last_checked: '2026-08-03'
---

# A=1 overflow 的对偶外层秩 RESET

## 1. 对称图表

设 verified overflow 满足

\[
pn=4Md+1,\qquad R_M=4M-n>p,\qquad M=kp+r,\quad 1\le r<p.
\tag{1}
\]

determinant 正规形给出 \(K_M=MC\)、\(d=p-C\)，其中 \(1\le C\le p-1\)，所以
\(1\le d<p\)；又因 \((M,p)=1\)，有 \(1\le r<p\)。

令

\[
s=n-4kd.
\]

代入 (1) 得

\[
ps=4rd+1,\qquad s\equiv1\pmod4.
\tag{2}
\]

定义两个对偶图表

\[
R_d=4d-s,\qquad K_d=d(p-r),
\]
\[
R_r=4r-s,\qquad K_r=r(p-d).
\tag{3}
\]

因为 \(1\le r,d<p\)，有

\[
4rd+1<4pd,\qquad 4rd+1<4pr,
\]

故 \(s<4d\) 且 \(s<4r\)。所以两个 \(R_t\) 都正，并由 (2) 满足
\(R_t\equiv3\pmod4\)。直接计算给出

\[
pR_d+1=4K_d,\qquad pR_r+1=4K_r,\qquad d\mid K_d,\qquad r\mid K_r.
\tag{4}
\]

若二者都大于 \(p\)，则

\[
4d(p-r)>p^2,\qquad 4r(p-d)>p^2.
\]

相乘并使用 \(4rd=ps-1\)，得到

\[
16rd>(p+s)^2,\qquad 16rd=4ps-4.
\]

这要求

\[
4ps-4>(p+s)^2,
\qquad\text{即}\qquad
0>(p-s)^2+4,
\]

矛盾。因此

\[
\min(R_d,R_r)<p.
\tag{5}
\]

这里没有遗漏等号情形：\(p\equiv1\pmod4\)，而两个 \(R_t\equiv3\pmod4\)，所以
\(R_t\ne p\)。

## 2. 至少一个下降载体严格大于 1

若 \(d,r>1\)，(5) 直接给出 \(t>1\) 且 \(R_t<p\)。若 \(d=1\)，则
\(0<4r+1<4p\)、\(ps=4r+1\) 和 \(s\equiv1\pmod4\) 强制

\[
s=1,\qquad r=\frac{p-1}{4}>1,\qquad R_r=p-2<p.
\]

若 \(r=1\)，对称地有

\[
s=1,\qquad d=\frac{p-1}{4}>1,\qquad R_d=p-2<p.
\]

两者不可能同时为 1，因为核心素数 \(p>5\)。故总能选择

\[
t\in\{d,r\},\qquad t>1,\qquad R_t<p.
\tag{6}
\]

## 3. A=1 的 E1--E5 RESET

对 \(A=1\)，令 \(A'=\operatorname{lcm}(1,t)=t\)。由于 \(t<p\) 且 \(p\ge5\)，

\[
t\le p-1\le B_p=\frac{(p-1)^2}{4},\qquad
t\mid K_t,\qquad A'>A.
\]

并且

\[
\left\lfloor\frac{B_p}{A'}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor
=B_p.
\]

因此对 \(W_S=W_T=\operatorname{Sol}(p)\) 使用恒等提升，
\((p,R_t,K_t;t)\) 是 overflow_outer_rank_reset_v1 的完整 E1--E5 边；由于
\(R_t<p\)，目标是 marked_absorb。这是由外层势支付的 RESET，不是固定-\(n\) 窗口边，
也不声称 target fiber 自动非空。

对负边界

\[
(p,M,d,n)=(73,1297,29,2061),
\]

有 \(r=56,s=89\)，从而

\[
(R_d,K_d)=(27,493),\qquad (R_r,K_r)=(135,2464).
\]

固定-\(n\) 的 \(L=d\) 失败，但 \(t=d=29\) 的对偶 RESET 合法；这正是两种边界必须
分开的原因。

## 4. 全称范围

该引理只处理旧 charged support 为 \(A=1\) 的来源可达 overflow。RESET 后的目标支撑
\(t>1\) 进入一般 \(A>1\) 问题；因此它消除了“初始 support=1 没有任何严格边”这一
错误余项，却没有给出 Erdős--Straus 猜想的全称证明。

重放命令：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
