---
kind: claim
claim_id: type-I-overflow-full-product-d-one-g-anchor-retention-rigidity
title: 完整乘积 d=1 饱和支到 p-2 G 锚点的支撑保留刚性
statement: >-
  设 p≡1 (mod 24)，n>0 且 A_n=(pn-1)/4 为整数，并令
  B_p=(p-1)^2/4。则 A_n|B_p 当且仅当 n=1。因而对完整乘积商折叠
  的 d=1 支撑饱和 target (M,d,n;A)=(A_n,1,n;A_n)，任何 target
  charged support D 若同时满足 A_n|D|B_p，必有 n=1。真正 overflow 时 n>1
  （所以 n≥5），故其固定 p-2 G 重图表 K=B_p 不存在任何保留或单调扩展旧
  charged support 的合法账本。这一刚性在 A_n≤B_p 的数值低支撑区仍成立；
  p-2 G 重图表只能以丢弃至少 A_n/gcd(A_n,B_p)>1 的旧支撑的 RESET 形式进入，
  而该 RESET 仍须独立支付 E1--E5，不能由 G 分类或恒等解提升自动获得。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-unbounded-full-product-quotient-fold
  - type-I-overflow-d-one-p-minus-two-g-rechart
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - fixed-n
  - full-product
  - d-one
  - G-state
  - p-minus-two
  - charged-support
  - support-retention
  - support-reset
  - proof-boundary
sources:
  - claim: type-I-overflow-unbounded-full-product-quotient-fold
    role: d-one-support-saturated-target-normal-form
  - claim: type-I-overflow-d-one-p-minus-two-g-rechart
    role: canonical-G-anchor-and-capacity
  - reproduction: reproductions/type_i_overflow_d_one_g_anchor_retention_rigidity.py
    role: focused-divisibility-and-support-loss-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 (d=1) 饱和支到 (p-2) G 锚点的支撑保留刚性

## 设置

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

完整乘积商折叠的唯一算术 stutter 是

\[
(M,d,n;A)=(A_n,1,n;A_n),
\qquad
A_n:=\frac{pn-1}{4}.
\tag{2}
\]

由于 (p\equiv1\pmod4)，(2) 蕴含 (n\equiv1\pmod4)。其原图表为

\[
R_n=4A_n-n=(p-1)n-1,
\qquad
K_n=A_n(p-1).
\tag{3}
\]

当 (n>1) 时，实际上 (n\ge5)，并且 (R_n>p)，所以这恰是仍待处理的
(d=1) overflow 支。反之 (n=1) 给出 (R_1=p-2<p)，不是 overflow。

已有的 (d=1) 分类把它的标准 G 重图表固定为

\[
R_G=p-2,
\qquad
K_G=B_p.
\tag{4}
\]

本卡只问一个必要的 charged-state 问题：该 G 图表是否能够保留 (2) 中已计费的
旧 support？若 target support 为 (D)，则状态合同至少要求

\[
A_n\mid D,
\qquad
D\mid K_G=B_p.
\tag{5}
\]

## 支撑保留的精确充要条件

**引理。** 对任意正整数 (n) 使 (A_n) 为整数，

\[
\boxed{
A_n\mid B_p
\quad\Longleftrightarrow\quad
n=1.
}
\tag{6}
\]

**证明。** 若 (n=1)，则

\[
A_1=\frac{p-1}{4},
\qquad
\frac{B_p}{A_1}=p-1,
\tag{7}
\]

故整除成立。

反过来设 (A_n\mid B_p)，写

\[
t:=\frac{B_p}{A_n}
=\frac{(p-1)^2}{pn-1}\in\mathbb Z_{>0}.
\tag{8}
\]

于是

\[
(pn-1)t=(p-1)^2.
\tag{9}
\]

模 (p) 化简得到

\[
-t\equiv1\pmod p,
\qquad\text{即}\qquad
t\equiv p-1\pmod p.
\tag{10}
\]

若 (n\ge2)，则

\[
0<t
\le\frac{(p-1)^2}{2p-1}
<p-1.
\tag{11}
\]

这与 (10) 矛盾，因为区间 (1,\ldots,p-2) 中没有一个整数同余于
(p-1\pmod p)。所以 (n=1)，证毕。

由 (5)，存在任一保留旧 support 的 (D) 当且仅当 (A_n\mid B_p)：必要性由
(A_n\mid D\mid B_p)，充分性可取 (D=A_n)。所以 (6) 立即给出更强的状态结论：

\[
\boxed{
\exists D\ (A_n\mid D\mid B_p)
\quad\Longleftrightarrow\quad
n=1.
}
\tag{12}
\]

## 对 overflow 和 G 重图表的后果

完整乘积 (d=1) 饱和支若仍为 overflow，必有 (n>1)，因此 (12) 说明：

\[
\boxed{
n>1
\quad\Longrightarrow\quad
\nexists D\text{ with }A_n\mid D\mid K_G.
}
\tag{13}
\]

这同时排除了下列所有把 (4) 当作递归出口的写法：

1. 把旧 support 原样带入 (p-2) 图表；
2. 用任意 (D) 的倍数扩展旧 support 后再带入该图表；
3. 特别地，用 \(\operatorname{lcm}(A_n,(p-1)/4)\) 伪造 support-monotone
   G 重图表边。

这个障碍强于单纯的大小比较。确有一个数值低支撑带：

\[
A_n\le B_p
\quad\Longleftrightarrow\quad
n\le p-2.
\tag{14}
\]

但对任意其中的 (n>1)，(6) 仍给出 (A_n\nmid B_p)。所以
`support <= B_p` 不能替代 E2 所需的精确整除。

若一定要使用 G 重图表，则其可保留的旧 support 至多为

\[
\gcd(A_n,B_p),
\tag{15}
\]

从而必须丢弃非平凡因子

\[
\Delta_p(n):=\frac{A_n}{\gcd(A_n,B_p)}>1
\qquad(n>1).
\tag{16}
\]

式 (16) 是 RESET 必须解释的精确账本损失，**不是**自动支付的势函数。G 的 Jacobi
分离只证明其中心目标纤维为空；图表无关的 \(\operatorname{Sol}(4,p)\) 恒等映射也
只给 E4。要把丢弃 \(\Delta_p(n)\) 的 rechart 登记为递归边，仍须另行给出 source
provenance、RESET 后的合法 target state、全域严格 E5 与不回返证明。

## 聚焦回执

\[
\begin{array}{c|c|c|c|c}
(p,n)&A_n&B_p&\gcd(A_n,B_p)&\Delta_p(n)\\
\hline
(73,1)&18&1296&18&1\\
(73,5)&91&1296&1&91\\
(73,9)&164&1296&4&41\\
(97,5)&121&2304&1&121
\end{array}
\]

前一行是唯一的非 overflow 边界。第二、三行都满足 (A_n\le B_p)，但仍严格失去
旧 support；第三行还说明这种损失不必是互素现象。脚本只重放这些代数回执，不做范围
扫描：

```bash
python3 reproductions/type_i_overflow_d_one_g_anchor_retention_rigidity.py --verify
```
