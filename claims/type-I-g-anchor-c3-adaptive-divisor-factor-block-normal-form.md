---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
title: c=3 双中间因子块路径的自适应除子正规形
statement: 对既定的 c=3 双中间 factor-block raw normal form，实际 raw receipt 当且仅当先选择 b=2d（d 整除 52h-5），再选择 a 整除 R-2d 且 a=7 (mod 8)，并满足三个端点 reserve 容量条件和既有 13-tail 条件。该结论不需要额外假设 (a,b)=1。它给出一条非固定 (a,b) 的无穷 Dirichlet 正族 h=35u，同时给出核心素数 p=1009 的严格 topology 反例。两类结论都只针对这一指定 raw normal form，不构成 selector edge、短证书有界性或 Erdos--Straus 全称证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-factor-block-raw-source-receipts
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-g-anchor-even-tail-complement-source-switch
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - c3
  - factor-block
  - adaptive-divisor
  - exact-normal-form
  - capacity
  - topology-counterexample
  - Dirichlet-ray
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-factor-block-raw-source-receipts
    role: endpoint-reserve-peeling-lemma-and-fixed-skeleton
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: raw-transition-semantics
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: declared-universal-p-source
  - concept: denominator-escape-state-contract
    role: root-entry-and-edge-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 双中间因子块路径的自适应除子正规形

## 1. 作用范围

令

\[
p=24h+1\ \text{为素数},\qquad
h\not\equiv2\pmod3,\qquad
h\not\equiv12\pmod{13},
\tag{1}
\]

并写

\[
R=104h-9,\qquad M=26h+1,\qquad x=p-3,\qquad K=Mx.
\tag{2}
\]

本卡只讨论下列固定的因子块 normal form：

\[
\begin{aligned}
\mathsf S_T
&\xrightarrow p N_R(1)
 \xRightarrow{\operatorname{Fac}(\alpha)}N_R(b)
 \xRightarrow{\operatorname{Fac}(\beta)}N_R(a)
 \xrightarrow2N_R(4\gamma)\\
&\xRightarrow{\operatorname{Fac}(\gamma)}N_R(4)
 \xrightarrow{13}N_R(4x)
 \xrightarrow2N_R(2x)
 \xrightarrow2N_R(x).
\end{aligned}
\tag{3}
\]

双箭头表示按素因子逐步回放的 raw word，绝不压缩为合数标签边。这里

\[
R-1=b\alpha,\qquad R-b=a\beta,\qquad R-a=8\gamma.
\tag{4}
\]

特别地，(3) 没有描述所有可能的 \(c=3\) raw path；以下的“当且仅当”始终只指
这个指定拓扑和指定尾部。

## 2. 精确自适应除子正规形

令

\[
S=\frac{R-1}{2}=52h-5.
\tag{5}
\]

**定理（指定 topology 的实际 raw 条件）。** 在 (1)--(4) 的 chart 中，(3) 的
三个因子块可作为实际 raw word 回放，且块内没有 gcd reduction，当且仅当存在正整数
\(d,a\) 使

\[
b=2d,\qquad d\mid S,\qquad a\mid R-2d,\qquad a\equiv7\pmod8,
\tag{6}
\]

并且对

\[
\alpha=\frac Sd,\qquad
\beta=\frac{R-2d}{a},\qquad
\gamma=\frac{R-a}{8}
\tag{7}
\]

满足端点 reserve

\[
\begin{aligned}
v_\ell(2d)&\ge v_\ell(K) &&(\ell\mid\alpha),\\
v_\ell(a)&\ge v_\ell(K) &&(\ell\mid\beta),\\
v_\ell(4)&\ge v_\ell(K) &&(\ell\mid\gamma).
\end{aligned}
\tag{8}
\]

这里还包括既有的 \(p\)-source 首边与 \(13\)-tail 条件；(1) 已保证后者
\(13\nmid K\)。结论不需要另列 \((a,b)=1\) 或 block-unit 假设。

**必要性。** 由于

\[
v_2(R-1)=v_2(2S)=1,
\qquad
v_2(K)=1,
\tag{9}
\]

若 \(\alpha=(R-1)/b\) 仍含因子 \(2\)，其末次剥离没有严格容量。因此唯一的
\(2\) 必须留在端点 \(b\)，即 \(b=2d\) 且 \(d\mid S\)。第二块的终点给出
\(a\mid R-b=R-2d\)。指定的 \(2\)-进入和 \(\gamma\)-块终点为 \(4\) 强制
\(8\mid R-a\)，而 \(R\equiv7\pmod8\)，故 \(a\equiv7\pmod8\)。

**充分性。** 由 (6)，有

\[
(b,R)=1,\qquad (a,R)=1.
\tag{10}
\]

而任何 \((a,b)\) 的公因子同时整除 \(R-b\) 与 \(b\)，从而同时整除
\(R\) 与 \(R-1\)，所以自动有 \((a,b)=1\)。因此各块中的每个素因子均不整除
\(R\) 或另一坐标；\(m=1\) 的 unit、primitive 和“无 gcd reduction”条件
自动成立。端点保留容量引理把全部严格容量精确化为 (8)。

\(R-a=8\gamma\) 还使指定的进入 \(2\)-边有至少三层二进高度，大于 (9)。
若 \(\gamma\) 为偶数，\(\gamma\)-块中的 \(2\)-因子由
\(v_2(4)=2\ge v_2(K)=1\) 支付；因此 \(\gamma\) **不必**为奇数。
最后按既有 \(13,2,2\) tail 回放即可完成 (3)。证毕。

原 skeleton 的相位只依赖总标签积，仍为

\[
P=2\alpha\beta\gamma,\qquad W=13P,\qquad
4P\equiv-1,\quad W\equiv-M,\quad4W\equiv-13\pmod R.
\tag{11}
\]

## 3. 一条非固定 \((a,b)\) 的无穷正族

令 \(u\ge1\)，并取

\[
\begin{aligned}
h&=35u,& p&=840u+1,& R&=3640u-9,\\
M&=910u+1,& x&=840u-2,\\
b&=728u-2,& a&=416u-1,\\
\alpha&=5,&\beta&=7,&\gamma&=403u-1.
\end{aligned}
\tag{12}
\]

直接计算给出

\[
R-1=5b,\qquad R-b=7a,\qquad R-a=8\gamma,\qquad a\equiv7\pmod8.
\tag{13}
\]

\(5,7\) 都不整除 \(K=Mx\)。对 \(\gamma\) 的奇素数容量风险，两个欧几里得
恒等式给出完整局部控制：

\[
403M-910\gamma=1313=13\cdot101,
\qquad
403x-840\gamma=34=2\cdot17.
\tag{14}
\]

其中 \(13\nmid\gamma\)，而 \(\gamma\) 的 \(2\)-因子由端点 \(4\) 吸收。因此若

\[
u\not\equiv1\pmod3,\qquad
u\not\equiv10\pmod{13},\qquad
u\not\equiv10\pmod{17},\qquad
u\not\equiv100\pmod{101},
\tag{15}
\]

且 \(p=840u+1\) 为素数，则 (8) 与所有 tail 条件都成立，故 (3) 是实际
factor-block raw receipt。

相位在这条族上甚至有整数恒等式：

\[
4P=31R-1,\qquad
W+M=101R,\qquad
4W=403R-13.
\tag{16}
\]

取

\[
u=3+66963t,
\qquad
66963=3\cdot13\cdot17\cdot101,
\tag{17}
\]

则 (15) 恒成立，且

\[
p=2521+56248920t.
\tag{18}
\]

因为 \((2521,56248920)=1\)，Dirichlet 定理给出无穷多个素数值 \(p\)。
这证明该拓扑确有非固定 \((a,b)\) 的无穷正族，但其因子块词长一般无界。

基点 \(u=3\) 给出

\[
(p,R,K)=(2521,10911,2\cdot1259\cdot2731),
\tag{19}
\]

\[
(b,a,\alpha,\beta,\gamma)=(2182,1247,5,7,1208),
\qquad
1208=2^3\cdot151.
\tag{20}
\]

它明确展示了偶数 \(\gamma\) 的有效性。逐边 word

\[
p;\quad 5,7,2,2,2,2,151,13,2,2
\tag{21}
\]

在每一步都有严格容量、unit 条件和 gcd reduction \(=1\)，并到达
\((x,R-x,1)=(2518,8393,1)\)。

## 4. 严格 topology 反例

该拓扑不能被误作全称 selector。取

\[
h=42,\qquad p=1009,\qquad R=4359.
\tag{22}
\]

这是一个满足 (1) 的核心素数，且

\[
S=2179\ \text{为素数},\qquad R-2=4357\ \text{为素数},\qquad
4357\equiv5\pmod8.
\tag{23}
\]

由 (6)，\(d\) 只能为 \(1\) 或 \(2179\)：

\[
\begin{array}{c|c|c}
d&b=2d&R-b\\ \hline
1&2&4357\\
2179&4358&1
\end{array}
\tag{24}
\]

第一行中 \(a\) 只能为 \(1\) 或 \(4357\)，均不为 \(7\pmod8\)；第二行只允许
\(a=1\)。故 (6) 本身无解，甚至无需进入容量筛。

因此 \(p=1009\) 没有 (3) 这一固定 normal form 的 factor-block receipt。
这只排除当前双中间拓扑，既不排除其它 raw path，也不涉及 \(p=1009\) 是否有
其它 Type I/II 证书。事实上，同一 declared universal source 存在绕开 canonical
\(p\)-edge 的六步 raw word 到达该 seed；它不反驳本节的 \(p\)-first 结论，但把下一
个障碍转为 source-bypass root policy，见
[p=1009 的 universal-source 绕行 receipt](type-I-g-anchor-c3-p1009-universal-source-bypass-raw-receipt.md)。

## 5. 合同边界

本卡建立的是 target-source raw provenance 的精确局部容量图。它尚未把任一 receipt
登记为 selector root，未提供 E4 lift、E5 势下降或有界长度证书。任何 direct terminal
命中的实例仍须 terminal-first 停止；(3) 不能据此变成全域递归边。

复现：

    python3 reproductions/type_i_c3_adaptive_divisor_factor_block_normal_form.py --verify
