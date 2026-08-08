---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-q137-raw-c19-same-fiber-owner
title: q=137 raw C=19 原子到同纤维 Type II target 的实际 owner 控制
statement: 在 q=137 actual raw family p(w)=193+772716168w 中，取 w=4+13t。每个 prime parameter 都有 endpoint H=19 的 actual primitive raw receipt。令 Type II candidate fiber 为 (D,a,c,M)=(2,2,1,8)，N=p+16。则 19|N 且 v_19(N)=1；因此单一 raw 原子 (omega_w,19,1) 可无条件映到同一 fiber 的 canonical candidate token ((2,2),19,1)。同时 N=247 m_t，247=19*13=-1 (mod 8)，其中 m_t=12513623+40669272t；令 (A,C,K)=(2,1,31)、B_t=(31p+2)/247=31m_t-2，则 247=4ACK-1 且 247|(Kp+A)，给出直接 Type II 终端。因而 raw 19 因子实际参与同纤维 target product，而非仅与某个 phase 或 normal-form coordinate 数值相同。另一方面，19 不可能单独成为该 raw family 的 Type II normal-form target factor：19=4ACK-1 强制 ACK=5，而 p(w)=3 (mod 19) 时三个可能三元组的 Kp+A 残数为 16,4,8。该结果建立单原子 raw-to-owner 的算术 pre-admission 和一个同纤维 terminal control；它不生成 typed Fourier demand、Hall slot、q=19 容量价格或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-q137-first-entry-family
  - type-II-coprime-factor-normal-form
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-hall-matching-fiber-realization-gate
  - type-I-raw-certified-q-layer-charge-key-nonreuse
topics:
  - type-I
  - type-II
  - raw-source
  - q137
  - q-adic
  - source-fiber
  - source-owner
  - fiber-realization
  - normal-form
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_q137_raw_c19_fiber_owner.py
    role: raw-word replay, singleton owner atom, same-fiber target product, and direct Type-II control
visibility: public
last_checked: '2026-08-08'
---

# q=137 raw (C=19) 原子到同纤维 Type II target 的实际 owner 控制

此前的 raw-to-cofactor 正控制只证明 endpoint 整除某个 candidate integer；另一侧的
direct Type II terminal 又往往与 raw factor 没有物理交集。本卡给出一个更紧的控制：
同一 actual raw endpoint (19) 是同一 candidate fiber 的因子，并且实际参与该 fiber
的 target factor (247=19cdot13)。

这不是全称 selector，也不是容量结论。它只关闭 `raw occurrence -> candidate q-layer`
的一个真实单原子实例，并明确显示剩余的 typed-demand 门。

## 1. raw family 与共同 candidate fiber

已有 q=137 family 为

\[
p(w)=193+772716168w,
\qquad 772716168=2^3 3^2\cdot7\cdot19^2\cdot31\cdot137.
\tag{1}
\]

每个 prime parameter 的 primitive word 到达

\[
\omega_w:\quad (1,R-1,1)\longrightarrow(19,R-19,1).
\tag{2}
\]

因为 (p(w)\equiv3\pmod {19})，固定

\[
D=2,\qquad a=2,\qquad c=D/a=1,\qquad M=4D=8
\tag{3}
\]

时，candidate integer 是

\[
N_a=p+aM=p+16\equiv0\pmod {19}.
\tag{4}
\]

所以 (2) 不是只在 group coordinate 上碰巧出现 (19)：它给出一个有相同 prime
parameter、相同实际 raw digest 和实际整除的 source atom。写

\[
\alpha_w(\omega_w,1)=((D,a),19,1).
\tag{5}
\]

在这一个 occurrence 上，(alpha_w) 是单射。它的定义不需要先选择 Fourier
character、需求、slot 或价格。

## 2. target-tuned subray

取

\[
w=4+13t,\qquad t\ge0.
\tag{6}
\]

则

\[
\begin{aligned}
p_t&=3090864865+10045310184t,\\
N_t=p_t+16&=3090864881+10045310184t\\
&=247\,(12513623+40669272t).
\end{aligned}
\tag{7}
\]

初项与步长互素，且分别为 (1,0\pmod {24})，所以 Dirichlet 定理给出无穷多个
prime terms。它们仍属于 (1) 的 actual raw family。

记

\[
h=247=19\cdot13\equiv-1\pmod8,
\qquad K=\frac{h+1}{8}=31.
\tag{8}
\]

由 (7)，(h\mid N_t)。同模数 source-switch 恒等式给出

\[
h\mid Kp_t+a,
\qquad
B_t=\frac{31p_t+2}{247}=31(12513623+40669272t)-2.
\tag{9}
\]

因此

\[
(A,C,K)=(2,1,31),\qquad h=4ACK-1,
\tag{10}
\]

是合法 Type II normal form。令

\[
m_t=12513623+40669272t,
\quad x_t=2B_t,
\quad d=4,
\quad y_t=62p_t,
\quad z_t=31B_tp_t.
\tag{11}
\]

则 (m_t=(A+B_t)/K)、(d\mid x_t^2)、(m_t\mid x_t+d)，并且

\[
\boxed{
\frac4{p_t}=\frac1{x_t}+\frac1{y_t}+\frac1{z_t}.}
\tag{12}
\]

这同时通过 (a\mid D)、(D/a=1) squarefree、(aM<p_t)、(h\mid N_t)、
(h\equiv-1\pmod M) 和 (B_t>a) 的全部整数实现门。若未来一个 typed matching
选中 (19,13) 两个 source block，它已经具备同纤维回译；本卡本身不凭空声明这个
matching。

## 3. raw 因子确实进入 target product

在模 (8) 的单位群中，两个实际整数 source block 是

\[
B_{19}=\{1,19\}=\{1,3\},
\qquad
B_{13}=\{1,13\}=\{1,5\}.
\tag{13}
\]

所以

\[
B_{19}B_{13}=U(8)=\{1,3,5,7\},
\qquad 19\cdot13\equiv7=-1\pmod8.
\tag{14}
\]

raw endpoint 的 exact height 也没有被放大。式 (7) 中

\[
12513623+40669272t\equiv11\pmod {19},
\tag{15}
\]

故

\[
v_{19}(N_t)=v_{19}(H)=1.
\tag{16}
\]

因此 (5) 的 image 只是 canonical ((19,1)) token；它不是第二层，也不是一份
自动的 rank 或 Kneser price。

## 4. 为什么 target 必须是复合块

这里不能把 raw endpoint (19) 自身误报为完整 normal-form factor。若

\[
19=4ACK-1,
\tag{17}
\]

则 (ACK=5)，仅有

\[
(A,C,K)=(1,1,5),(1,5,1),(5,1,1).
\tag{18}
\]

而 (1) 恒有 (p(w)\equiv3\pmod {19})，故相应的 (Kp+A) 依次为

\[
16,\quad4,\quad8\pmod {19},
\tag{19}
\]

没有一个满足 normal-form divisibility。(19) 能作为 (14) 的一个 source factor，
却不能单独承担 target factor 的角色；额外的 (13) 正是把它调到 (-1\pmod8) 的
必要补块。

## 5. 实际 prime/raw/terminal 控制

取 (t=2)，即 (w=30)，可由完整 Pocklington 条件认证

\[
p=23181485233.
\tag{20}
\]

此时

\[
\begin{aligned}
R&=100453102663,\\
Q&=5248414123,\\
N&=23181485249
=13\cdot19\cdot23\cdot83\cdot211\cdot233,\\
B&=2909417175,\\
x&=5818834350.
\end{aligned}
\tag{21}
\]

(Q) 是 prime，且 (137;Q) 的 actual primitive replay 到达 (2)。同时

\[
\frac4{23181485233}
=\frac1{5818834350}
+\frac1{1437252084446}
+\frac1{2090782949645871380025}.
\tag{22}
\]

这是一条同时包含 raw occurrence、owner atom、target product 和直接 Type II
terminal 的有限可复核控制。

## 6. 边界与下一缺口

(5) 是 raw-to-owner 的算术 pre-admission，而非完整 capacity admission。以下对象仍未
建立：

* 从 F/G Fourier 或 source relation 独立产生的 (q=19) typed demand；
* request-to-token 与 demand-to-slot 的全局单射；
* (q=19) 的 Kneser/stabilizer price；
* 超出本 raw family 的全称 owner functor，或任何 selector edge。

不过，该控制排除了一个此前未分开的逻辑缝隙：actual raw endpoint 可以真实地进入
同纤维 target product；它既不必等于完整 target factor，也不能仅凭这种参与就被重复
收费。
