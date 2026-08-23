---
kind: claim
claim_id: type-I-c8-second-full-excess-parent-anchored-universal-fallback
title: c8 第二完整超额的 parent-anchored 全称 fallback 严降宏
statement: >-
  设 P 是 actual persistent ordinary q=1 full-carrier d=1 parent，complete
  terminal-first 已 miss，且其既有 q_star=103 relay 重放到 zero-k c=8 internal
  checkpoint H=(p,R,8M;M)。令 Q=(R-1)/2。已有恒等式给出 Q odd、gcd(M,Q)=1、
  p not divide Q，且 H 的 canonical p-source 实际到达 (1,2Q,1)，所以 Q 是该节点
  相对 8M 的唯一完整 excess block，final support 为 A_T=MQ。其 canonical capacity
  c_T 满足 75c_T=64 mod p。旧局部结论 c_T>8 保持不变；但 c_T=p-1 会迫使 p divide
  139，与 p>=4129 矛盾，故 9<=c_T<=p-2。因 P 的 capacity 是 p-1，且 A_T>M>B_p，
  比较真实 persistent endpoints 得固定 T5 N7 严降 P->T；H->T 的局部升容只是
  macro internal checkpoint。target terminal/hit/F/G 从整数重算，hit 终止，F/G 通过
  type_i_a_gt_one_overflow_residual owner 重入。因此每个 terminal-first-surviving actual
  c8 parent 都有此 deterministic OTHER verified successor/terminal fallback，不依赖
  double-low endpoint 存在。本结论不关闭上游 c8 parent reachability 或全局 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-I-path-anchored-atomic-split-total-typed-rechart
  - type-I-h4-c8-atomic-target-common-admission-reentry
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - complete-excess
  - persistent-macro
  - source-provenance
  - common-admission
  - well-foundedness
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
    role: exact-Q-and-local-8-to-carry-formula
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: canonical-p-source-and-anchor-path
  - claim: type-I-h4-c8-atomic-target-common-admission-reentry
    role: target-local-terminal-F-G-and-existing-owner-reentry
  - reproduction: reproductions/f2_c8_second_full_excess_parent_macro_v1.py
    role: parent-to-final-rank-and-focused-exact-control
visibility: public
last_checked: '2026-08-24'
---
# c8 第二完整超额的 parent-anchored 全称 fallback 严降宏

## 1. 为什么旧 no-go 恰好隐藏了一条宏边

旧定理正确证明：从 c8 checkpoint

\[
H=(p,R,K;M),\qquad K=8M
\tag{1}
\]

取第二完整 excess 后，canonical capacity \(c_T\) 总满足 \(c_T>8\)。所以
\(H\to T\) 不能作为 standalone `LOCAL_DROP`。

但实际持久状态不是 \(H\)。它来自一个 q=1 d=1 parent

\[
P=(p,R_P,K_P;A_P,\sigma),
\qquad K_P=A_P(p-1),
\tag{2}
\]

而 \(H\) 是同一 source scope 内由已验证 relay 重放出的 macro checkpoint。T5 的
macro discipline 要求比较 \(P\) 与最终 \(T\)，不要求每个内部 checkpoint 下降。

## 2. 唯一 source/path 与完整 excess

c8 normal form 给出

\[
p=48s+1,\quad pR+1=32M,\quad
Q=\frac{R-1}{2},
\tag{3}
\]

\[
M=9s(176s+5)(3168s^2+24s-1).
\tag{4}
\]

由既有 source separation，\(H\) 的 canonical source

\[
(p,V,p-1),\qquad V=R(p-1)-p
\tag{5}
\]

是 primitive，且实际 p-edge 唯一到达

\[
(p,V,p-1)\xrightarrow p(1,R-1,1)=(1,2Q,1).
\tag{6}
\]

既有 gcd 定理给出

\[
Q\text{ odd},\qquad (M,Q)=1.
\tag{7}
\]

由于当前 carrier 为 \(8M\)，(7) 表明 \(2Q\) 的二因子已被 carrier 吸收，而全部
\(Q\) 是唯一完整 excess block；残余 \(\beta=2\)，并有 \(1\cdot\beta\mid8M\)。
又由

\[
8Q\equiv75\pmod p
\tag{8}
\]

和 \(p\ge4129\)，有 \(p\nmid Q\)。因此 (6)--(8) 是 p-free、source-bound、
deterministic 的 path-anchored complete-excess receipt，不依赖 V 的因子分解或任何
double-low occurrence。

定义 final support 与 chart：

\[
A_T=MQ,
\qquad
c_T=\langle(4A_T)^{-1}\rangle_p,
\tag{9}
\]

\[
K_T=A_Tc_T,
\qquad
R_T=\frac{4K_T-1}{p}.
\tag{10}
\]

## 3. 相对 checkpoint 升高，相对 parent 严降

由 \(4M\cdot8\equiv1\pmod p\) 与 (8)--(9)，

\[
\boxed{75c_T\equiv64\pmod p.}
\tag{11}
\]

对 \(1\le c\le8\)，有

\[
0<75c-64\le536<p,
\tag{12}
\]

所以 (11) 排除这些值，得到 \(c_T>8\)。这是旧 no-go。

另一方面，若 \(c_T=p-1\)，则

\[
75c_T-64=75p-139,
\tag{13}
\]

而 (11) 会给 \(p\mid139\)，不可能，因为 \(p\ge4129\)。因此

\[
\boxed{9\le c_T\le p-2<p-1.}
\tag{14}
\]

第一条 c8 relay 已证明 \(M>B_p\)，故 \(A_T=MQ>M>B_p\)。固定 CHARGED rank 为

\[
J(S)=\left(\left\lfloor\frac{B_p}{A_S}\right\rfloor,
\frac{K_S}{A_S},\eta_p,0\right).
\tag{15}
\]

若 \(A_P\le B_p\)，从 \(P\) 到 \(T\) 的第一坐标由正数降到零；若
\(A_P>B_p\)，第一坐标都为零，而 (14) 使第二坐标从 \(p-1\) 严降到 \(c_T\)。
即使 parent 带有任意非负 immediate-regeneration \(\eta_p\)，比较也已经在更早坐标
严格。因此

\[
\boxed{\Pi_{T5}(T)<\Pi_{T5}(P).}
\tag{16}
\]

而 \(H\to T\) 的 \(8\to c_T\) 上升只发生在 atomic macro 内，不写入 persistent queue。

## 4. E1--E5 与 terminal/F/G 重入

完整 macro 是

\[
P\Longrightarrow H
\xRightarrow[\text{internal p-source}]{(6)}
T.
\tag{17}
\]

E1 由 actual persistent \(P\)、既有 \(P\Rightarrow H\) relay receipt、(5)--(7) 的
actual path 与 unique complete-excess block 支付。E2 由 (9)--(10) 支付。E3 绑定
parent id、两个 path digest、scope、target integers 与完整 \(K_T\) factorization，并按
完整 Bradford/centered hit/F/G policy 从头重算，禁止继承 \(H\) 的标签。E4 是

\[
W_T=W_P=\operatorname{Sol}(p),\qquad \Phi_{T\to P}=\operatorname{id}.
\tag{18}
\]

E5 是 (16)。若 target 为 direct/centered hit，则输出 terminal；否则 (9)、
\(A_T>B_p\) 与 \(R_T\equiv3\pmod4\) 给出 \(R_T>p\)，因此 F/G final target 通过现有
`type_i_a_gt_one_overflow_residual` owner 重入 common selector。

## 5. c8 outgoing 三分

固定 precedence：

1. 完整 terminal-first 命中则 `TERMINAL`；
2. MISS 后若固定 candidate order 中存在第一个 actual double-low receipt，可选择已有
   `DOUBLE_LOW_VERIFIED_SUCCESSOR`；
3. 否则无条件执行 (17)，得到 target-local terminal 或
   `OTHER_VERIFIED_SUCCESSOR`。

第 3 项其实对第 2 项也可用；保留 double-low 优先只为了兼容冻结三分和较短目标选择。
因此 double-low existence 不再是 c8 outgoing totality 的前提，non-double-low complement
也不再为空白。

focused control \(s=3279,p=157393\) 给出

\[
p-1=157392,qquad8<c_T=4198<p-1,
\tag{19}
\]

且完整 endpoint 为

\[
A_T=34210241115566771375771444426075973075,
\tag{20}
\]

\[
R_T=3649834292583515308444175375033627543.
\tag{21}
\]

该素数自身会被更早 terminal-first 抢占，所以 (19)--(21) 只检验公式和 macro
端点比较，不作为 terminal-free actual control。

本结果关闭 `GAP-O3-C8-OUTGOING` 的数学 outgoing existence，但 shared producer
registration、F1 grammar freeze 与独立 cross-audit 仍由 coordinator 处理；它不宣称
上游所有 c8 parent 已经实际可达，也不关闭全局 F2/T6。

聚焦验证：

```bash
PYTHONPATH=reproductions python3 \
  reproductions/f2_c8_second_full_excess_parent_macro_v1.py --verify
```
