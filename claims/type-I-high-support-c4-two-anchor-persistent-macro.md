---
kind: claim
claim_id: type-I-high-support-c4-two-anchor-persistent-macro
title: C=4 双高锚 complete-excess 的内部 checkpoint 严格宏
statement: 设 p=25 (mod 48) 为核心素数，且 H0=(p,4p+3,4A0;A0,sigma) 是已收费的 persistent canonical 高锚，其中 A0=(p(4p+3)+1)/16。令 Q0=2p+1，H1 是 H0 的 canonical complete-excess target，Q1=(R1-1)/2，H2 是 H1 的 canonical complete-excess target。则两个 high-R universal-source bundle 都有 residual beta=2，且 H1 可作为同一 scope 内的内部 checkpoint 而无需入队；H2 的 canonical cofactor 为 2。因此，只要 H0 具有真实 persistent parent 且 terminal-first guard 不抢占，组合宏 H0=>H2 满足 E1--E5，并使 Lambda_p^sharp=(floor(Bp/A),K/A) 严格从 (0,4) 降到 (0,2)。p=2137 给出独立重分型的 G-to-F-to-F 控制。该定理不证明每个 C=4 图表都有这样的 persistent parent，也不完成全局 terminal-first guard。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-c4-canonical-stutter-boundary
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - high-support
  - c4-boundary
  - complete-excess
  - persistent-macro
  - internal-checkpoint
  - G-state
  - F-state
  - well-founded-descent
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_support_c4_two_anchor_persistent_macro.py
    role: two-bundle arithmetic, typed G-to-F-to-F p=2137 replay, and endpoint-rank check
visibility: public
last_checked: '2026-08-12'
---

# C=4 双高锚 complete-excess 的内部 checkpoint 严格宏

## 1. 结论的准确范围

固定核心素数

\[
p\equiv25\pmod {48},\qquad
B_p=\frac{(p-1)^2}{4},
\tag{1}
\]

并设第一个最小 \(C=4\) 高支撑图表是

\[
R_0=4p+3,\qquad
A_0=\frac{pR_0+1}{16},\qquad
K_0=4A_0.
\tag{2}
\]

本卡的输入不是裸图表，而是已经有真实 E1--E5 父边的 persistent state

\[
P\longrightarrow H_0=(p,R_0,K_0;A_0,\sigma).
\tag{3}
\]

其中 \(\sigma\) 是原样传播的 source-tree scope。调用者还必须先按版本化
terminal-first prefix 排除优先终端或 alternate。下面构造的不是 fresh root，也不把
任意 charged history 重新标成 fresh-source-tree-only。

在这两个明确前提下，存在 deterministic macro

\[
\boxed{H_0\Longrightarrow H_2}
\tag{4}
\]

满足 E1--E5，且

\[
\boxed{
\Lambda_p^\sharp(H_0)=(0,4)
\quad\longmapsto\quad
\Lambda_p^\sharp(H_2)=(0,2).}
\tag{5}
\]

所以单步 \(4\mapsto4\) 并不是这类已收费 \(C=4\) 高锚的最终 E5 障碍：它可以
压入一个不入队的内部 checkpoint，再由第二次 bundle 一起支付。式 (4) 不证明 (3)
对每个 \(C=4\) 图表都可达，故它不是全局出口定理。

## 2. 两个 bundle 的闭式构造

令

\[
Q_0=2p+1,\qquad
A_1=A_0Q_0,\qquad
R_1=R_0Q_0+2,\qquad K_1=4A_1.
\tag{6}
\]

第一个 high-\(R\) universal source 一步到 \((1,R_0-1,1)\)。由于

\[
R_0-1=2Q_0,\qquad (Q_0,A_0)=1,\qquad (Q_0,K_0)=1,
\tag{7}
\]

其 complete-excess receipt 是 \(Q_0\)、\(\beta_0=2\)、残余
\(2\beta_0=4\mid K_0\)，并给出 (6)。这正是单步 stutter 的来源。

现在不把 \((R_1,K_1;A_1)\) 登记为 recursive successor。它是从 \(H_0\) 的确定
算术构造出的内部 checkpoint，携带同一个 \(\sigma\)，随后立即重新调用该精确
canonical chart 的 high-\(R\) raw source。令

这里的 universal \(p\)-source 是 chart-local 的 E1 回执，而不是 source-tree 的
所有权对象。按状态合同，只有具名 root-entry 才能创建 fresh scope；因此第二次调用
不会重建或更改 \(\sigma\)，只会在既有宏内补充一段可重放的 source provenance。

\[
Q_1=\frac{R_1-1}{2}=Q_0+16A_0,\qquad A_2=A_1Q_1.
\tag{8}
\]

已有的互素计算给出

\[
(Q_1,A_1)=(Q_1,K_1)=1,\qquad R_1-1=2Q_1.
\tag{9}
\]

所以第二个 complete-excess receipt 同样是 \(Q_1\)、\(\beta_1=2\)、残余
\(2\beta_1=4\mid K_1\)。它的 canonical target 为

\[
\boxed{
R_2=\frac{R_1Q_1+R_0+2}{2},\qquad K_2=2A_2.}
\tag{10}
\]

等价地，\(4K_2=pR_2+1\)、\(\operatorname{canonical\_chart}(p,A_2)=(R_2,K_2)\)。
这便是从两个 raw bundle 得到的 \(4\to4\to2\)；关键区别是中间的 \(4\) 不再是
未支付 persistent edge 的 endpoint。

## 3. E1--E5

记 \(H_1=(p,R_1,K_1;A_1,\sigma)\) 为内部 checkpoint，
\(H_2=(p,R_2,K_2;A_2,\sigma)\)。宏的回执按如下方式闭合。

| 项 | 支付内容 |
|---|---|
| E1 | 输入 (3) 固定已收费 \(H_0\) 与 scope；两个 high-R path-anchored bundle 分别从 \(H_0,H_1\) 的精确 canonical chart 重放 actual universal \(p\)-source、首个 \(p\)-edge、完整 excess block 和 residual-divisibility。第二个 source 只是内部 receipt，不创建 root 或 state scope。 |
| E2 | (6)--(10) 给出两个 lcm carrier、canonical chart、overflow determinant 以及 \(A_2\mid K_2\)。 |
| E3 | \(H_0,H_1,H_2\) 都由完整字段重算 content-addressed state ID；\(\sigma\) 在两个内部构造中保持不变，macro digest 绑定两个 bundle 和三个 typed digest。 |
| E4 | 三张图表均标为 \(\operatorname{Sol}(4,p)\)，所以 \(H_2\to H_0\) 使用显式恒等映射；F/G/hit 分类不能继承，必须逐图表重算。 |
| E5 | \(A_0>B_p\)，故两端第一坐标均为零；由 \(K_0/A_0=4\) 与 \(K_2/A_2=2\)，(5) 严格成立。 |

这比将 \(H_1\) 单独入队更强也更窄：单步 sharp-rank stutter 仍真实存在，但它不再
阻止已付费 \(H_0\) 直接采取这个复合动作。没有 (3) 时不得把内部 receipt 的
\(4\to2\) 比较回填到未知 parent；没有 terminal-first guard 时也不得注册 recursive edge。

## 4. p=2137 的 G-to-F-to-F 控制

取 \(p=2137\)。第一高锚为

\[
(R_0,A_0,K_0)=(8551,1142093,4568372).
\tag{11}
\]

\(K_0=2^2\cdot337\cdot3389\) 的全部支撑 Jacobi 值为 \(+1\)，而
\(\left(\frac{-1}{8551}\right)=-1\)，故 \(H_0\) 是 G。两个 bundle 给出

\[
\begin{aligned}
&(R_1,A_1,K_1)=(36555527,4882447575,19529790300),\\
&(R_2,A_2,K_2)=(334076629427327,89240219635774725,
178480439271549450).
\end{aligned}
\tag{12}
\]

中间与终点都重新分类为 F，而不是从 G 继承标签。按各自支撑素数的递增次序，

\[
5^{18277763}\equiv-1\pmod {36555527},
\tag{13}
\]

及

\[
2^{171932900936}5^3\equiv-1
\pmod {334076629427327}.
\tag{14}
\]

两个有限中心盒分别不含 \(-1\)，故 (13)--(14) 是完整的 provided-unbounded F
certificates，而非仅有局部因子模数的命中。这个控制重放两个 raw receipt、三张
typed chart、scope 传播以及 (5)，但刻意不伪造 (11) 的 persistent parent 或完整
terminal-first guard。

## 5. 聚焦复核

~~~bash
python3 reproductions/type_i_high_support_c4_two_anchor_persistent_macro.py --verify
~~~

该命令只重放 \(p=73\) 的通用算术控制和 \(p=2137\) 的 typed 控制，不产生结果文件，
也不重跑历史普查。
