---
kind: claim
claim_id: type-II-owner-projection-physical-capacity-flow-gate
title: Type II owner token 投影到物理 q 槽的流—割容量门
statement: 对由 owner 加权 Fourier 谱产生的有限请求，先把每个 owner 见证展开为 owner token，再投影到实际可复用的物理 q 槽。构造请求—owner token—物理槽三层流网络；满流当且仅当请求可以同时通过 owner 唯一性和物理槽容量。若某请求割的物理邻域容量小于请求数，输出严格 OWNER_PROJECTION_CAPACITY_DEFICIT。owner multiplicity 或 Fourier 总质量只有在该流门通过、或满足每个物理槽的 owner fiber 不超过其容量的强注入合同后，才可作为 q 进容量输入；否则它只是表示权重，不能收费或产生递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-target-fiber-owner-weighted-fourier-capacity-bridge
  - type-II-qprefix-owner-escape-capacity-decomposition
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-source-column-escape-finite-expansion-relay
topics:
  - type-II
  - owner-weight
  - physical-capacity
  - flow
  - Hall
  - q-adic-capacity
  - source-column
  - Fourier
  - proof-program
sources:
  - claim: type-II-target-fiber-owner-weighted-fourier-capacity-bridge
    role: owner-weighted-spectrum-input
  - claim: type-II-qprefix-owner-escape-capacity-decomposition
    role: owner-height-and-alternate-owner-boundary
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: request-and-source-capacity-contract
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: post-deficit-source-column-dispatch
  - reproduction: reproductions/type_ii_owner_projection_physical_capacity_flow.py
    role: real-owner-collision-and-safe-flow-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner token 投影到物理 q 槽的流—割容量门

## 1. 三层对象

固定一个目标纤维和一个已经通过 source relation、SNF、相位及范围门的请求集
\(U\)。对每个奇素数 \(q\) 和高度 \(j\)，把一个 owner 见证写成 token

\[
\tau=(q,j,a),\qquad
a\in\mathcal O_{q,j}(f),
\tag{1}
\]

其中 \(a\) 是能够支付 \(q^j\) 的 source row。token 的物理投影是

\[
\pi(q,j,a)=c=(q,j,\text{physical occurrence}),
\tag{2}
\]

它可能忘掉 source row 标签：多个 owner 可以投影到同一个实际的 \(q^j\) 因子。
记 \(\mathcal T\) 为全部 token，\(\mathcal C\) 为物理槽，\(b(c)\in\mathbb N\) 为
该物理槽在当前 source-fiber ledger 中允许的最大并发使用次数。通常 \(b(c)=1\)；
若跨状态合同明确允许重复，才取更大的 \(b(c)\)。

每个请求 \(r\in U\) 只允许使用一组已经通过整数回译的 token，记其邻域为
\(\widetilde N(r)\subseteq\mathcal T\)。owner 加权谱中的
\(\omega_q(j)\) 只记录这些 token 的数量；它没有记录不同请求之间的投影冲突。

## 2. owner 投影流网络

构造有向网络

\[
s\longrightarrow r\longrightarrow\tau
\longrightarrow\pi(\tau)\longrightarrow t,
\tag{3}
\]

其中

* \(s\to r\) 的容量为 \(1\)；
* \(r\to\tau\) 的容量为 \(1\)，当且仅当
  \(\tau\in\widetilde N(r)\)；
* \(\tau\to\pi(\tau)\) 的容量为 \(1\)；
* \(c\to t\) 的容量为 \(b(c)\)。

记该网络的最大整数流为 \(\mathsf F(U)\)。一个值为 \(|U|\) 的流恰好等价于：

1. 每个请求选择一个合法 owner token；
2. 一个 token 不被两个请求复用；
3. 同一个物理槽的总使用次数不超过 \(b(c)\)。

因此定义

\[
\boxed{\mathrm{OWNER\_FLOW\_PASS}(U)\iff\mathsf F(U)=|U|.}
\tag{4}
\]

这是把 owner 加权表示接到物理容量的精确门，而不是把 owner 数直接当作槽数。

## 3. 物理割与严格缺口

对任意请求子集 \(U'\subseteq U\)，定义 owner token 邻域和物理投影容量

\[
\widetilde N(U')=\bigcup_{r\in U'}\widetilde N(r),
\qquad
\mathsf P(U')=
\sum_{c\in\pi(\widetilde N(U'))}b(c).
\tag{5}
\]

任意可行流都满足

\[
|U'|\le\mathsf F(U')\le\mathsf P(U').
\tag{6}
\]

所以

\[
\boxed{
|U'|>\mathsf P(U')
\Longrightarrow
\mathrm{OWNER\_PROJECTION\_CAPACITY\_DEFICIT}(U',\mathsf P(U'),|U'|).
}
\tag{7}
\]

式 (7) 是严格的物理容量缺口：即使每个物理槽的全部 owner 标签都存在，
也不能同时服务 \(U'\)。该回执可进入 source-column 扩张、q-prefix 逃逸或
其它 Type I/II 终端，但不能直接写成 annihilator relay；还必须检查源列是否被
当前割湮灭。

更强地，最大流最小割定理给出精确等价：

\[
\boxed{
\mathsf F(U)=|U|
\iff
\text{网络 (3) 的每个 }s\text{--}t\text{ 割容量至少 }|U|.
}
\tag{8}
\]

因此当 (7) 未触发时，仍不能仅凭 \(\omega_q(j)\) 宣称可收费；必须通过完整流门，
因为 token 邻域本身也可能因 source-switch 或跨 q 兼容性而稀疏。

## 4. 何时 owner 权重可以安全收费

定义 owner-label mass

\[
\mathsf L(U')=|\widetilde N(U')|,
\qquad
\mathsf K_b(U')=\mathsf L(U')-\mathsf P(U').
\tag{9}
\]

\(\mathsf K_b>0\) 表示 owner 标签相对于物理预算的碰撞债务；它可能在请求数较少
时只是预警，但 \(\mathsf P(U')<|U'|\) 时必然成为严格缺口。Fourier 中的
\(\omega_q(j)\) 和 \(V_f\) 统计的是类似 \(\mathsf L\) 的表示质量，不是
\(\mathsf P\) 或 \(\mathsf F\)。

有一个简单的强充分条件。若

\[
\boxed{
\#\{\tau\in\mathcal T:\pi(\tau)=c\}\le b(c)
\quad\text{对每个物理槽 }c,
}
\tag{10}
\]

则任意 owner-token 匹配都自动投影为物理可行匹配。因此在 (10) 及 token 图
普通 Hall 条件同时成立时，owner 权重可以安全地进入 q 进容量账本。若 (10) 失败，
必须使用网络 (3)；不能用 \(\sum_a1\) 代替物理容量。

条件 (10) 不是必要条件：不同 owner token 可能从未出现在同一个请求割中，或者
跨状态合同允许相应的 \(b(c)>1\) 复用。正因如此，网络流是精确门，而不是简单地
把所有 owner 数删重。

## 5. 与 owner 加权 Fourier 的接口

owner 加权谱仍然合法地定义群代数函数

\[
W_f(g)=
\sum_{\mathbf u:\prod q^{u_q}=g}
\prod_{q:u_q>0}\omega_q(u_q),
\tag{11}
\]

并保留其稳定子、Fourier 缺口和直接命中结论。但从一个非平凡角色产生
\(R_{q,j}\) 个 q-prefix 请求时，收费顺序应改为：

1. 展开每个请求的 owner token 邻域 \(\widetilde N(r)\)；
2. 通过网络流 (3)，得到 \(\mathsf F(U)\)；
3. 若满流，才把这些请求送入 q 进容量、Rado 对偶和 source-column 闭包；
4. 若不满流，先记录最小割。若其物理投影容量满足 (7)，输出
   'OWNER_PROJECTION_CAPACITY_DEFICIT'；否则保存完整最小割作为
   'OWNER_TOKEN_ASSIGNMENT_OBSTRUCTED'。

这一区分保留了 Fourier 表示的 owner multiplicity，同时禁止把同一个物理 q 因子
在不同 owner 标签下重复收费。若 source contract 明确把 owner 标签本身定义为
互不相同的物理 token，则令 \(\pi\) 为恒等映射，网络退化为普通 Hall 图。

## 6. 严格算术控制

### \(p=57399241,D=41\)：真实 owner 碰撞

取目标 \(f=(1,1)\)，标准 source rows \(a=1,41\)。目标和两个来源共同拥有
\(q=5\) 的一层 owner，故

\[
\mathcal T=\{(5,1,1),(5,1,41)\},
\qquad
\pi(5,1,1)=\pi(5,1,41)=c_5.
\tag{12}
\]

若两个独立请求都可见这两个 owner token，而物理 ledger 对 \(c_5\) 只允许一次
使用，则

\[
\mathsf L(U)=2,\qquad
\mathsf P(U)=b(c_5)=1,\qquad
\mathsf F(U)=1<2.
\tag{13}
\]

因此 owner 加权谱中的 \(1+\omega_5(1)=3\)（包括空选择）不能被解释为三个
物理容量单位；即使只把两个非空 owner 当作两个单位，也会高估一倍。该控制是
真实目标纤维的投影冲突，不是抽象群的伪造例子。

### \(p=409,D=8,f=(4,2)\)：无冲突正控制

两个 active owners 分别为 \(q=3,a=4\) 与 \(q=7,a=8\)。若每个物理槽容量为
一，取两个请求各自只连接自己的 token，则

\[
\mathsf L(U)=\mathsf P(U)=\mathsf F(U)=2.
\tag{14}
\]

此时 owner 计数通过流门，可以继续进入加权 Fourier 稳定子商；这与 (13) 的
物理碰撞严格区分。

## 7. 证明

网络 (3) 中一单位从请求到 token 再到物理槽的流就是一个合法 owner assignment；
容量约束分别实现 token 唯一性和物理槽预算。反过来，任一合法 assignment 逐条
发送一单位流，故 (4) 成立。对请求子集 \(U'\)，所有流必须经过
\(\pi(\widetilde N(U'))\) 的物理槽，得到 (6)；若 (7) 成立则不可能满流。
最大流最小割定理给出 (8)。

若 (10) 成立，任意 token 匹配在每个物理槽上的投影数量不超过该槽的容量，因而
自动是物理可行匹配。式 (9) 只是标签数与物理容量之差；它说明为什么
\(\omega_q(j)\) 不能单独代替物理账本。式 (11) 的 Fourier 正交关系不受投影模型
影响，但其 q-demand 拉回必须经过 (3)。证毕。

## 研究边界

该门完成了 owner 加权表示到物理 q 容量的精确映射，并给出一个真实的 owner
collision 反例。它没有声称物理流缺口本身就是整数递降；后续仍需把最小割中的
源列按有限 source-column expansion 接回，或证明 q-prefix 紧链/广义 \(2^j\) 终端。
但从此以后，任何使用 owner multiplicity 的容量证明都必须明确给出 \(\pi\)、\(b\)
和流/割证书。
