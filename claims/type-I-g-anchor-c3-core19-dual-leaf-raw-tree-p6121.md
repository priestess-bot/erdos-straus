---
kind: claim
claim_id: type-I-g-anchor-c3-core19-dual-leaf-raw-tree-p6121
title: p=6121 的同源 c=3 双叶 raw tree、A=19 carry 与 terminal/q19 截断
statement: 对 p=6121、R=26511、K=40568458 的 c=3 图表，同一个 declared universal p-source 有两条共享前缀的实际 primitive raw word，分别到达 C0=p-3=6118 与 C1=19。两叶解码为不同的 cofactor-overflow determinant 行；A=19 在两行均通过 E2，且当 T=I={0,1} 时 CarryCore 恰为19。p-line 的有序相位分别满足两条物理尾律，但它们没有给出跨行相位匹配。该控制必须 terminal-first 截断，因为 p=3 mod7 给出 gap 7、d=1 的直接 Type II 叶；又 phi(R)=2^3*47^2，因此任何 U(R) 的子商都没有19阶角色。故它是同源双叶 raw/E2 正控制，却不是 q=19 容量、root 或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-factor-block-raw-source-receipts
  - type-I-fg-raw-transcript-persistent-ledger-carry-core
  - type-I-ordered-raw-lineage-normalized-phase-rigidity
  - type-II-small-shared-gap-explicit-fan
topics:
  - type-I
  - c3
  - raw-source
  - raw-tree
  - source-provenance
  - E2
  - carry
  - q-primary
  - terminal-first
  - Type-II
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-factor-block-raw-source-receipts
    role: C0-factor-block-source-semantics
  - claim: type-I-ordered-raw-lineage-normalized-phase-rigidity
    role: ordered-lineage-and-physical-tail-law
  - claim: type-II-small-shared-gap-explicit-fan
    role: gap-seven-terminal-predicate
  - reproduction: reproductions/type_i_c3_p6121_dual_leaf_raw_tree.py
    role: exact-two-leaf-control
visibility: public
last_checked: '2026-08-07'
---

# \(p=6121\) 的同源 \(c=3\) 双叶 raw tree

## 1. 固定图表与范围

固定

\[
p=6121,
\qquad R=26511,
\qquad K=\frac{pR+1}{4}=40568458
=2\cdot7\cdot19^2\cdot23\cdot349.
\tag{1}
\]

这正是标准 \(c=3\) 参数 \(h=255\) 的图表：

\[
M_0=6631,
\qquad C_0=p-3=6118,
\qquad K=M_0C_0.
\tag{2}
\]

本卡证明一个固定的**同源双叶 raw provenance**控制。它不把两条 raw word 称为
sound/complete selector transcript，也不创建 root 或递归边。

声明的 high-\(R\) universal source 为

\[
\mathsf S=(6121,162241199,6120).
\tag{3}
\]

以下所有行都由 `ordered_raw_step` 逐一重放：标签为素数、严格容量和 unit 条件成立、
gcd reduction 为 \(1\)，且输出仍是 primitive formal node。这里 `side=0,1` 表示当前
有序 node 的左、右坐标。

## 2. 一条 source、两个 raw 叶

两个 word 有公共前缀

\[
\begin{aligned}
(6121,162241199,6120)
&\xrightarrow{(0,6121)}(1,26510,1)\\
&\xrightarrow{(1,5)}(5302,21209,1).
\end{aligned}
\tag{4}
\]

第一条分支是既有 \(C_0=p-3\) factor-block word 的具体化：

\[
\begin{aligned}
(5302,21209,1)&\xrightarrow{(0,11)}(482,26029,1)
\xrightarrow{(0,241)}(2,26509,1)\\
&\xrightarrow{(1,7)}(3787,22724,1)
\xrightarrow{(0,541)}(7,26504,1)\\
&\xrightarrow{(1,2)}(13252,13259,1)
\xrightarrow{(0,3313)}(4,26507,1)\\
&\xrightarrow{(1,13)}(2039,24472,1)
\xrightarrow{(1,2)}(12236,14275,1)\\
&\xrightarrow{(0,2)}(6118,20393,1).
\end{aligned}
\tag{5}
\]

第二条分支到达 companion cofactor \(C_1=19\)：

\[
\begin{aligned}
(5302,21209,1)&\xrightarrow{(1,167)}(127,26384,1)\\
&\xrightarrow{(1,2)}(13192,13319,1)\\
&\xrightarrow{(1,701)}(19,26492,1).
\end{aligned}
\tag{6}
\]

其中关键的有限因子关系是

\[
R-1=5\cdot5302,\qquad
21209=167\cdot127,\qquad
26384=2^4\cdot1649,\qquad
13319=701\cdot19.
\tag{7}
\]

因而 (5) 和 (6) 是从同一个实际 source 出发、共享两个 raw step 后分叉的两叶树；
它不是逆造的 \(p\)-parent，也不是把到达 \(C_0\) 的路径误作 \(C_1\) 的来源。

## 3. 两叶的 determinant、E2 与 carry

两叶在同一个 \((p,R,K)\) 图表中解码为

\[
\begin{array}{c|c|c|c|c|c}
i&C_i&M_i&d_i=p-C_i&n_i=4M_i-R&M_i\bmod p\\ \hline
0&6118&6631&3&13&510\\
1&19&2135182&6102&8514217&5074.
\end{array}
\tag{8}
\]

每行均有

\[
pn_i=4M_id_i+1,
\qquad
4M_i-n_i=R>p.
\tag{9}
\]

两行的 \(M_i,C_i\) 都被 \(19\) 整除。因此取候选旧账本 \(A=19\) 时

\[
\frac{A}{(A,C_i)}=1,
\tag{10}
\]

两行均通过 E2。若且只若声明这两行都是 E2 行，即
\(\mathcal T=I=\{0,1\}\)，则

\[
\boxed{
\operatorname{CarryCore}(\mathcal T,I)
=\gcd(M_0,M_1,C_0(M_0\bmod p),C_1(M_1\bmod p))=19.
}
\tag{11}
\]

这把一般同图表的两行算术 pair 补成了一个**固定点的同源 raw provenance**正控制；
它仍不自动产生 selector 所需的持续 old ledger 或 complete transition universe。

## 4. 有序 p-line 与两条物理尾律

从 source 的 \(p\)-coordinate 出发，令

\[
\sigma=-p^{-1}=1988\pmod R,
\qquad
E_i=\prod_{j\le i}q_jg_j,
\qquad
\Phi_i=\sigma E_i.
\tag{12}
\]

所有 \(g_j=1\)。在 \(C_0\) 分支终点，p-line coordinate 为
\(R-C_0=20393\)，且

\[
E_{C_0}=26471,
\qquad
\Phi_{C_0}=13=n_0\pmod R.
\tag{13}
\]

这正是 orientation \(-1\)、\(t=1\) 的 physical-tail law。
在 \(C_1\) 分支终点，p-line coordinate 为 \(C_1=19\)，且

\[
E_{C_1}=12880,
\qquad
\Phi_{C_1}=22325=-4186=-n_1\pmod R,
\tag{14}
\]

因为 \(n_1\equiv4186\pmod R\)。这是 orientation \(+1\)、\(t=1\) 的
physical-tail law。两个方向及相位并不相同；(13)--(14) 不提供共同 F layer、
row-to-anchor assignment、跨行 phase matching 或 `demand_to_slot`。

## 5. terminal-first 与 \(q=19\) 双重截断

该点不应进入 root。首先

\[
p\equiv3\pmod7,
\qquad
m=7,
\qquad
x=\frac{p+7}{4}=1532,
\qquad d=1.
\tag{15}
\]

于是 \(d\mid x^2\)、\(d\le x\)、\(7\mid x+d\)，给出直接 Type II 叶

\[
\boxed{
\frac4{6121}
=\frac1{1532}
+\frac1{1340499}
+\frac1{2053644468}.
}
\tag{16}
\]

因此 terminal-first dispatcher 必须输出 (16)，而不是调度 (4)--(6) 的 raw tree。

其次

\[
R=3\cdot8837,
\qquad
\varphi(R)=17672=2^3\cdot47^2.
\tag{17}
\]

所以 \(19\nmid |U(R)|\)。任意 \(H\le U(R)\) 及其稳定子商 \(H/P\) 的阶也都不被
\(19\) 整除，故

\[
\operatorname{Hom}(H/P,\mu_{19^e})=\{1\}
\qquad(e\ge1).
\tag{18}
\]

换言之，(11) 的局部 `CarryCore` 含 \(19\) 并不产生 \(19\)-primary Fourier 方向。

## 6. 准确推进与未闭合接口

本控制完成了此前最小的来源缺口：在一个实际核心素数上，双行 \(A=19\) 算术 pair 的
两叶都有同一 universal source 下的逐步 raw receipt。它同时精确说明为什么这个点不能
承担当前目标：已有短 Type II terminal，且 \(q=19\) Fourier 空间为空。

下一条有意义的目标不是重复搜索本点，而是在 terminal residual 中寻找同样的 mixed-side
双叶树，同时要求 \(R\) 含有 \(1\pmod {19}\) 的因子，并分别补齐 fixed-layer 角色存活、
terminal-first、source-image/ancestry、相位匹配以及 E4/E5。完成前，本卡不是
`verified_edge`，更不构成 Erd\H{o}s--Straus 猜想的全称证明。

复现：

```bash
python3 reproductions/type_i_c3_p6121_dual_leaf_raw_tree.py --verify
```
