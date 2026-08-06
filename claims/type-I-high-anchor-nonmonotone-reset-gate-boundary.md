---
kind: claim
claim_id: type-I-high-anchor-nonmonotone-reset-gate-boundary
title: 高锚非整除同图表支撑重置的余因子 gate 边界
statement: 设 \(H=(p,R,K;A)\) 是满足 \(p\equiv1\pmod {24}\)、\(p<R<4A\)、\(A\mid K\)、\(K/A<p\) 的 canonical 高锚，令 \(B_p=(p-1)^2/4\) 与 \(\Pi_p(D)=\lfloor B_p/D\rfloor\)。在本卡限定的 support-growth、outer-rank 域 \(A<L\le B_p\) 内，所有非支撑单调、但保持同一图表的有限重置恰为 \(L\in\{L:L\mid K,A<L\le B_p,A\nmid L\}\)；它们满足 \(\operatorname{canonical\_chart}(p,L)=(R,K)\)。其中只有 \(\Pi_p(L)<\Pi_p(A)\) 的子集有外层秩支付。若随后 cofactor gate 通过，写 \(L=ga,C=gc,r=au,(a,c)=1,K=LB\)，则 target support 为 \(Lc\)，相位 \(h=(uc-B)/p\)，且 exact reset-state self-loop 当且仅当 \(C\mid L\)。对冻结 verified-parent atlas 的 31 个不同高锚，此域有 162 个非整除 reset，135 个严格付款；deterministic high-R full-excess bundle 后只有一个 gate 命中，且唯一行 \(p=409,R=511,K=52250,A=250,L=2090\) 恰在 \(C\mid L\) 子情形，cofactor target 为重置状态 \((409,511,52250;2090)\)，即 \(h=0\) 精确自环。因此有限 atlas 中没有一个非整除同图表 reset 产生 gate 后的第二个严格 direct cofactor 推进。该结论不把 reset 本身升级为 E1--E5 边：仍需单独的 content-addressed parent/reset、scope、typed \(H/H_L/S_L/T_L\) fiber、恒等解提升、terminal-first 和明确 support_reset_paid 合同。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-high-anchor-frozen-parent-atlas-gate-boundary
  - type-I-high-anchor-same-chart-gate-engineering-boundary
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-high-anchor-direct-c1-finite-menu-exhaustion
topics:
  - type-I
  - high-anchor
  - same-chart
  - support-reset
  - outer-rank
  - cofactor-gate
  - finite-atlas
  - self-loop
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_nonmonotone_reset_gate.py
    role: exact finite reset lattice, deterministic bundle/gate replay, and reset-contract boundary
  - result: reproductions/type-i-high-anchor-nonmonotone-reset-gate-results.json
    role: frozen 31-anchor arithmetic atlas
  - result: reproductions/type-i-high-anchor-parent-atlas-results.json
    role: frozen verified-parent high anchors
visibility: public
last_checked: '2026-08-06'
---

# 高锚非整除同图表支撑重置的余因子 gate 边界

## 1. 精确有限域

固定 high canonical anchor

\[
H=(p,R,K;A),\qquad
p<R<4A,\qquad A\mid K,\qquad \frac KA<p,
\]

并记

\[
B_p=\frac{(p-1)^2}{4},\qquad
\Pi_p(D)=\left\lfloor\frac{B_p}{D}\right\rfloor.
\]

这里专门允许丢弃旧支撑整除链，但不改变图表。本卡只讨论支撑增长且仍能进入
\(\Pi_p\) 外层秩的有限域；它不声明穷尽 \(L<A\) 或 \(L>B_p\) 的其它 reset 语义。
候选恰为

\[
\mathcal R_H=
\{L:L\mid K,\ A<L\le B_p,\ A\nmid L\}.
\tag{1}
\]

若 \(A>B_p\)，则 (1) 为空。这不是失败，而是该外层势没有可用 reset 域。

对 \(L\in\mathcal R_H\)，由 \(R<4A<4L\) 与 \(L\mid K\)，有

\[
\operatorname{canonical\_chart}(p,L)=(R,K).
\tag{2}
\]

反过来，在固定 \((p,R,K)\)、同一 \(B_p\) 容量域、且不保留 \(A\mid L\) 的 support
语义下，(1) 正是所有这种同图表重置。它们不是自动合法的递归边；只有

\[
\Pi_p(L)<\Pi_p(A)
\tag{3}
\]

时，才有可记录为 `support_reset_paid=true` 的严格外层支付。

## 2. 随后的 gate

对每个 \(L\)，令 \(Q\) 是 \(R-1\) 相对 \(K\) 的 complete-excess bundle，并令

\[
M_L=\operatorname{lcm}(L,Q),\qquad
C_L=K_{M_L}/M_L,\qquad r_L=M_L\bmod p.
\]

high-R bundle 后的 cofactor 支撑 gate 仍是

\[
\frac{L}{\gcd(L,C_L)}\mid r_L.
\tag{4}
\]

这只是 cofactor target 的 canonical-support 必要且充分算术条件，不携带 parent
可达性或 typed fiber 的含义。

## 3. 冻结 atlas 的结果

输入是 `type-i-high-anchor-parent-atlas-results.json` 的 31 个不同 verified-parent
高锚。没有重新运行 selector 或历史搜索。

| 项目 | 数量 |
|---|---:|
| 不同高锚 | 31 |
| 有至少一个非整除 reset 的锚 | 25 |
| \((1)\) 中的 reset | 162 |
| 满足严格支付 \((3)\) 的 reset | 135 |
| 所有 reset 的 gate 命中 | 1 |
| 严格付款 reset 的 gate 命中 | 1 |
| 其中 exact reset-state self-loop | 1 |

唯一命中是

\[
(p,R,K;A)=(409,511,52250;250),\qquad L=2090.
\]

它有

\[
\Pi_{409}(250)=166>19=\Pi_{409}(2090),
\]

所以 reset 本身有严格外层支付。bundle 的具体值为

\[
Q=51,\quad M_L=106590,\quad C_L=209,\quad r_L=250,
\]

并且

\[
\frac{L}{\gcd(L,C_L)}=10\mid250.
\]

不过其 cofactor target 是

\[
(R_T,K_T;A_T)=(511,52250;2090)=(R,K;L),
\]

故 \(h=0\)，并严格回到 reset 后的同一状态。它必须按 direct-cofactor 的 exact
self-loop 规则抑制，而不是作为第二条递归推进边。换言之，有限 atlas 只显示一条
“付费重置后到达自环”的算术路径，并没有展示一条 gate rescue 后的严格 direct macro。

## 4. Gate 后的相位分解与自环判据

固定一个通过 (4) 的 reset support \(L\)，写

\[
g=(L,C),\qquad L=ga,\qquad C=gc,\qquad r=au,\qquad(a,c)=1,
\]

并令 \(K=LB\)。gate 保证 \(a\mid r\)，所以 target 的支撑和图表变化精确为

\[
A_T=\operatorname{lcm}(L,C)=Lc,
\]
\[
K_T=rC=L(uc)=K+h\,pL,\qquad
R_T=R+4hL,
\]
\[
\boxed{h=\frac{uc-B}{p}\in\mathbb Z_{\ge0}.}
\tag{5}
\]

因此

\[
h=0
\quad\Longleftrightarrow\quad
(R_T,K_T)=(R,K)
\quad\Longleftrightarrow\quad
uc=B.
\tag{6}
\]

chart return 仍不等于 reset-state self-loop：后者还要求 \(A_T=L\)。结合
\(A_T=Lc\) 和 target 的 canonicality，得到精确判据

\[
\boxed{\text{exact reset-state self-loop}
\quad\Longleftrightarrow\quad C\mid L
\quad\Longleftrightarrow\quad c=1.}
\tag{7}
\]

冻结 atlas 的 \(p=409\) 命中恰有

\[
L=2090,\ C=209,\ g=209,\ a=10,\ c=1,\ r=250=10\cdot25,\ B=25,
\]

所以它必为 exact self-loop。这个现象不是 nonmonotone reset + gate 的一般定律。
固定 \(p=1201\) 控制给出反向边界：

\[
(R,K;A,L)=(1839,552160;560,986),\qquad
\Pi_{1201}:642\longrightarrow365.
\]

这是合法的非整除、严格付款同图表 reset。其 full-excess cofactor 有

\[
C=952,\quad r=580,\quad (g,a,c,u,B)=(34,29,28,20,560),
\]

故 \(h=0\) 且 chart return，但

\[
A_T=Lc=27608\ne L.
\]

它证明即使 gate 后回到同一图表，也不能把 chart return 错认成 direct action 的 exact
self-loop；该控制仍由 terminal-first 抢占，不能登记 reset macro。

若要构造真正正相位的 nonmonotone reset，算术目标现在明确为 \(uc\ge p\)，再加入
\(R/4<A<L\)、\(A\nmid L\) 与 \(L\le B_p\)。这只是新候选的筛选条件，parent、scope、
typed fiber、terminal-first 和 E1--E5 仍不可省略。

## 5. 合法 reset 所缺的合同

要把 \(H\to H_L\) 本身提升为真正的外层 reset，算术 \((2)\)--\((3)\) 还不足够。回执至少需要：

- E1：内容寻址的父回执结束于 \(H\)，并显式给出 \(H\to H_L\) 的同图表分解；若多个 legacy 回执共享 endpoint edge id，reset 必须绑定一个规范的 parent digest；
- E2：从 \(H_L\) 的 deterministic bundle，及若采用则符合 \((4)\) 的 cofactor normal form；
- E3：\(H,H_L,S_L,T_L\) 处于同一 `source_tree_scope`，各自有 state id；reset hash 绑定父回执和被丢弃的 \(A\)；
- E4：四个状态的 typed F/G/hit 或 terminal 证书，以及递归方向上
  \(\operatorname{Sol}(p)\to\operatorname{Sol}(p)\) 的恒等提升；
- E5：严格式 \((3)\)，并把 `support_reset_paid`、`outer_rank_reset` 标为真；旧支撑的
  phase token、耗尽菜单或 capability 不得跨 \(A\nmid L\) 被继承；
- terminal-first：任何 nonterminal reset/macro 入队前，相关终端与 alternate 菜单必须有
  自己的有界穷尽回执。

冻结 legacy parent 只保证其原边已验证，不提供上述 reset API。因此这里的唯一命中仍是
`analysis_evidence`，不是 selector edge。

唯一命中的 \(p=409,A=250\) 还实际出现了这一去歧义需求：冻结 atlas 给它列出三条
相同 endpoint edge id、但 digest 分别不同的 legacy 父回执（fixed-\(s\) reset、generic
reset 与 same-chart promotion）。三者都缺少 replay adapter、scope、内容地址与 typed
fiber。因此 endpoint 相等不能作为选择其中一条父链的依据。

## 复现

```bash
python3 reproductions/type_i_high_anchor_nonmonotone_reset_gate.py --verify
```
