---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
title: q=1 full-carrier 的 d=1 接收态 p-free 门全称排除与严格 complete-excess 继电
statement: >-
  设 ordinary q=1 G full-carrier root 的第二-anchor fixed-n 宏已经进入 persistent
  high target，并经其强制 full-product fold 产生 d=1 receiver
  A=(pn-1)/4、R=(p-1)n-1、K=A(p-1)，其中 n>1。则该 receiver 的 complete-excess
  p-free 门总通过，即 n 不同于 -2 (mod p)。奇 t 时若
  14 delta+3=jp，则 1<=j<=13 且 21n=5jp+7j-15；p-free failure 会迫使唯一的
  p=97、t=4 矛盾。偶 t=2s 时若 q_*|6s-1 是宏所取强制 excess prime 且
  3q_*delta-4=jp，则 1<=j<3q_*<p、j=2 (mod 3)、4n=jp+4-j；p-free failure
  会迫使 j=12，与 j=2 (mod 3) 矛盾。因此 terminal-first 未命中时，若 raw p-source
  门通过便取 universal p-source，否则取最小互素素数 source；两者都到同一 anchor。
  完整 excess carrier 给出 p-free canonical overflow target：非再生时 capacity
  从 p-1 严格降到至多 p-2，再生时已有 p-adic eta 严格减一，故该 q=1 d=1
  receiver 总有一条完整 E1--E5 strict relay。该结论只处理立即 postmacro receiver；
  它不排除后续 d=1 regeneration target 再次落入 p-free failure，也不证明全局 selector。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-chart-least-coprime-prime-anchor-source
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - d-one
  - complete-excess
  - p-free-gate
  - raw-source
  - p-adic-regeneration
  - strict-relay
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-second-anchor-fixed-n-macro
    role: persistent-postmacro-d-one-receiver-and-parity-carriers
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: exact-complete-excess-carrier-and-p-free-gate
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: capacity-or-regeneration-strict-rank
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-p-gate-repair
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_p_free_gate_exclusion_relay.py
    role: parity-normal-forms-and-focused-E1-E5-receipts
visibility: public
last_checked: '2026-08-15'
---

# q=1 full-carrier 的 d=1 接收态 p-free 门全称排除与严格 complete-excess 继电

## 1. 唯一要处理的立即接收态

固定一个 ordinary (q=1) G full-carrier root，并执行已有的第二-anchor
fixed-(n) 宏。若其第一个 macro target 已低于 (p)，它已经是 marked absorb；若
high macro target 的 full-product fold 给出 (n=1)，其 successor 同样低于 (p)。
本卡只处理余下的 persistent (d=1) overflow receiver：

\[
p\equiv1\pmod {24},\qquad n>1,\qquad n\equiv1\pmod4,
\tag{1}
\]

\[
A=\frac{pn-1}{4},\qquad
R=(p-1)n-1,\qquad
K=A(p-1).
\tag{2}
\]

这里的 (n) 正是前一宏的 (n_T)，(A=L\delta) 是其 full-product
successor 的 charged support。因而 (2) 不是自由构造的一张 (d=1) chart：它已有
来自 q=1 宏的 persistent parent、fresh source scope、
\(\operatorname{Sol}(p)\) 恒等 lift 和严格前置势下降。

令 (Q) 为 anchor ((1,R-1,1)) 的 complete-excess block，令

\[
E=\frac{\operatorname{lcm}(A,Q)}{A}.
\tag{3}
\]

已有的 (d=1) 容量公式给出

\[
p\nmid Q
\quad\Longleftrightarrow\quad
n\not\equiv-2\pmod p.
\tag{4}
\]

通常 (4) 的反面是完整 (d=1) 分派唯一不能直接 canonical rechart 的算术门。以下证明它
在这个 q=1 image 上根本不会发生。

## 2. 奇 (t)：唯一形式例外与奇支矛盾

设 (t) 为奇数。前一宏取

\[
p=24t+1,\qquad L=2(10t+1)=\frac{5p+7}{6},
\tag{5}
\]

并写其 quotient-fold remainder 为 (1\le\delta<p)。receiver determinant 是

\[
pn=4L\delta+1.
\tag{6}
\]

由 (5)--(6) 模 (p) 化简，

\[
14\delta\equiv-3\pmod p.
\tag{7}
\]

故存在唯一整数 (j) 满足

\[
14\delta+3=jp,\qquad1\le j\le13.
\tag{8}
\]

把 \(\delta=(jp-3)/14\) 和 \(4L=(10p+14)/3\) 代入 (6)，没有任何近似地得到

\[
\boxed{21n=5jp+7j-15.}
\tag{9}
\]

若 (4) 失败，则 (n\equiv-2\pmod p)。将 (9) 模 (p) 化简给出

\[
p\mid7j+27.
\tag{10}
\]

核心奇支有 (p\ge73)，而 (34\le7j+27\le118<2p)，所以 (10) 强制

\[
p=7j+27.
\tag{11}
\]

再用 (p\equiv1\pmod {24})，得到 (j\equiv10\pmod {24})。由 (8) 的范围只可能

\[
j=10,\qquad p=97,\qquad t=4,
\tag{12}
\]

这与奇 (t) 矛盾。因此奇支总有 (p\nmid Q)。注意 (12) 也精确说明了为什么不能在
丢失奇支条件后把该排除误写成一般 (d=1) 定理。

## 3. 偶 (t)：模三排除

设 (t=2s)。前一宏的强制 excess prime (q_\star) 满足

\[
q_\star\mid6s-1,\qquad
p=48s+1,\qquad
L=9s q_\star.
\tag{13}
\]

特别地 (q_\star\ne2,3)，故 (q_\star\ge5)，并且

\[
4L=\frac{3q_\star(p-1)}4.
\tag{14}
\]

将 (14) 代入 (pn=4L\delta+1)，得到

\[
3q_\star\delta\equiv4\pmod p.
\tag{15}
\]

所以可唯一写成

\[
3q_\star\delta-4=jp,
\qquad1\le j<3q_\star<p.
\tag{16}
\]

上界使用 (q_\star\le6s-1)。又因 (p\equiv1\pmod3)，(16) 模三给出

\[
j\equiv2\pmod3.
\tag{17}
\]

将 \(\delta=(jp+4)/(3q_\star)\) 代回 determinant，得到第二个闭式：

\[
\boxed{4n=jp+4-j.}
\tag{18}
\]

若 (4) 失败，(18) 模 (p) 给出 (j\equiv12\pmod p)。由 (16) 的
\(1\le j<p\)，这强制 (j=12)，但它与 (17) 矛盾。因此偶支也总有

\[
\boxed{p\nmid Q.}
\tag{19}
\]

由第 2--3 节，(19) 对每个仍为 overflow 的 q=1 postmacro (d=1) receiver 成立。

## 4. 真 source 与严格 relay

先按 terminal-first 检查直接 Type I/II certificate；若没有 terminal，anchor source
可完全确定：

\[
\begin{cases}
q=p,&n\not\equiv-1\pmod p,\\
q=q_{\min},&n\equiv-1\pmod p,
\end{cases}
\tag{20}
\]

其中 (q_{\min}) 是不整除 (RK(R-1)) 的最小素数。第一行是 universal
(p)-source；第二行是最小互素素数 source。两行都有实际一步 raw path 到
\((1,R-1,1)\)。第二行不与 (19) 冲突：raw (p)-gate 与 p-free bundle gate 是两个独立
门；最小互素 source 不改变 (Q\)、余块或 charged carrier。

由 (19)，

\[
C:=\operatorname{lcm}(A,Q)=AE
\tag{21}
\]

是 p-free 的 path-anchored complete-excess carrier。已有容量公式给出

\[
C>p^2>B_p:=\frac{(p-1)^2}{4},
\tag{22}

以及唯一 canonical target

\[
pR_C+1=4K_C,\qquad C\mid K_C,\qquad R_C>p.
\tag{23}

令 \(c=K_C/C\)。若 \(E\not\equiv1\pmod p\)，则

\[
1\le c\le p-2<p-1=K/A.
\tag{24}
\]

若 \(E\equiv1\pmod p\)，(23) 是下一条 (d=1) 行，且

\[
\nu_p(E_{\rm next}-1)=\nu_p(E-1)-1.
\tag{25}

所以对 receiver 和 relay target 使用

\[
\widehat\Lambda_p=
\left(
\left\lfloor\frac{B_p}{\text{support}}\right\rfloor,
\frac K{\text{support}},
\nu_p(E-1)
\right)
\tag{26}
\]

（非 (d=1) target 的第三坐标取 (0)），(22)、(24)--(25) 给出严格下降：

1. (A\le B_p) 时，第一坐标因 (C>B_p) 严格下降；
2. (A>B_p) 且非再生时，第二坐标由 (p-1) 严格降到 (c\le p-2)；
3. (A>B_p) 且再生时，前两坐标保持而第三坐标严格下降。

在 (20)--(26) 中，E1 是 q=1 macro 的 persistent parent 加实际 source/path 和
complete-excess receipt；E2 是 (21)--(23) 的整数重算；E3 保留 fresh source scope、
重新生成 canonical target state 与 normal form；E4 是两端
\(\operatorname{Sol}(p)\) 上的恒等映射；E5 正是 (26)。因此这是一条实际的
strict relay，而不是把 (p\)-free carrier 当作无来源的算术候选。

## 5. 结论的边界

本卡关闭了 q=1 宏的**立即** (d=1) receiver 上唯一的 p-free failure branch。它没有
声称后续 regeneration target 仍在 q=1 image：有限 (p)-adic countdown 之后，该 target
仍可能进入一般 (d=1) 的 p-free peeled-Reach 边界。因此本结论不构成 G/Type I
global exit，也不替代下一层的 selector；它只保证每个 postmacro (d=1) receiver 都有
一条可核验、严格支付的下一 relay。

聚焦回执：

```bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_p_free_gate_exclusion_relay.py --verify
```

它覆盖两个奇支 receiver、四个偶支 receiver、一个 raw-(p) source 失败的
least-coprime repair、一个 (p)-adic regeneration 以及一个 (g>1) control；它不做
素数范围搜索或终端枚举。
