---
kind: claim
claim_id: type-II-final-stabilizer-q-fold-collapse
title: Type II 最终稳定子下 q 幂折叠的吸收塌缩
statement: 设有限阿贝尔群 G 中的完整源积集为 P=A{1,u,...,u^e}，T=Stab_G(P)，并令 o=ord_{G/T}(uT)。若 e+1>=o，则 o=1；因此在最终稳定子下，非平凡商阶必满足 e+1<o 且 q 幂块的价格恰为 e。所谓 o>=2 的有限阶折叠只能相对于插入时稳定子记录，随后必须进入稳定子塔，不能以最终 T 的价格重复计费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-qadic-height-kneser-block-bridge
topics:
- type-II
- q-adic
- stabilizer
- finite-order
- absorption
- price-ledger
- quotient-descent
- proof-program
sources:
  - claim: type-II-qadic-height-kneser-block-bridge
    role: q-block-Kneser-price
visibility: public
last_checked: '2026-08-05'
---

# Type II 最终稳定子下 q 幂折叠的吸收塌缩

## 定理

令 \(G\) 为有限阿贝尔群，\(A\ne\varnothing\) 为已经通过整数回译的其它源块积集，

\[
B=\{1,u,u^2,\ldots,u^e\},\qquad P=AB,
\]

并令

\[
T=\operatorname{Stab}_G(P),
\qquad o=\operatorname{ord}_{G/T}(uT).
\tag{1}
\]

若

\[
e+1\ge o,
\tag{2}
\]

则

\[
\boxed{o=1.}
\tag{3}
\]

因此 \(o>1\) 时必有 \(e+1<o\)，而最终稳定子下 q 块的精确价格为

\[
|BT/T|-1=e.
\tag{4}
\]

### 证明

令 \(\pi:G\to G/T\)。由于 \(T\) 是 \(P\) 的最终稳定子，\(PT=P\)，所以

\[
\pi^{-1}(\pi(P))=P.
\tag{5}
\]

条件 (2) 说明

\[
\pi(B)=\{1,uT,\ldots,(uT)^e\}=\langle uT\rangle.
\tag{6}
\]

故 \(\langle uT\rangle\) 平移稳定 \(\pi(P)=\pi(A)\pi(B)\)。任取
\(x\in\langle uT\rangle\)，取 \(g\in G\) 使 \(\pi(g)=x\)。由于 \(T\) 也稳定
\(gP\)，有 \(\pi^{-1}(\pi(gP))=gP\)；结合 \(\pi(gP)=\pi(P)\) 和 (5)，得到
\(gP=P\)，于是 \(g\in T\)，即 \(x=1\)。
因此 \(uT=1\)，得 (3)。再将 (3) 代入

\[
|BT/T|-1=\min(e,o-1)
\]

即得 (4)。证毕。

## 插入时稳定子的正确折叠语义

如果 q 块是在一个中间积集 \(A_0\) 上插入，令

\[
T_0=\operatorname{Stab}_G(A_0),
\qquad o_0=\operatorname{ord}_{G/T_0}(uT_0).
\]

当 \(e+1\ge o_0\) 时，(6) 只说明该插入使稳定子增长，或使 q 方向在
\(T_0\) 中形成一个完整循环；这时应记录

\[
\mathrm{Q\_PREFIX\_INSERTION\_FOLD}
\quad\text{或}\quad
\mathrm{Q\_PREFIX\_ORDER\_FOLD}
\]

并把新稳定子送入稳定子塔。完成所有块后重新计算最终 \(T\)；不能把
\(\min(e,o_0-1)\) 与最终稳定子价格再相加。

## 边界例子

在 \(G=C_4\) 中取 \(A=\{0\}\)、\(B=\{0,2\}\)（加法记号）。插入前
\(T_0=\{0\}\)、\(o_0=2\)，所以这是一次中间稳定子折叠；插入后
\(T=\{0,2\}\)，最终 \(o=1\)，该块没有最终商价格。

若直接取完整块 \(B=\{0,1,2,3\}\)，则最终 \(T=G\)、\(o=1\)，即便
\(e+1=4\) 很大，也不能把四层当作四个最终容量单位。

## 选择器回执

对最终稳定子计算价格时只允许以下两种 q 分支：

1. \(o>1\) 且 \(e+1<o\)：全部 \(e\) 层是最终 Kneser 活跃价格；
2. \(o=1\)：q 方向被最终稳定子吸收，价格为零，转稳定子塔或吸收回执。

若账本在中间层发现 \(e+1\ge o_0>1\)，必须保留插入时稳定子和来源标签，走
Q_PREFIX_ORDER_FOLD，不能把该事件改写成最终 \(o>1\) 的折叠。

## 研究边界

该引理修正了最终稳定子与插入时稳定子的语义混用，消除了一个潜在的 off-by-one
和重复收费路径。它不证明中间折叠后的稳定子塔一定能提升为整数降模；后者仍需
通过 source-switch、SNF、范围和 Type I/F/G 或 primary 终端门。
