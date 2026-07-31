---
kind: claim
claim_id: type-I-formal-natural-tail-integrality-rigidity
title: 形式节点自然双尾的整数性刚性与 E4 空纤维边界
statement: 设p是1 mod24的素数、R至少为3且等于3 mod4、4K=pR+1，正互素形式节点满足A+B=Rm。令U=mK/B、V=mK/A为保留根分母pK后的两条自然有理尾，则4/p=1/(pK)+1/U+1/V，且U,V同时为整数当且仅当AB|K；此时节点已经直接给出中心Type I终端。若仅B|K而A不整除K，则固定pK与整数尾U后，目标解中第三坐标的像纤维为空。对single-external slab A=Qalpha、B=beta、K=alpha beta c、Q=q^e、q不整除K，坏残余Q/(m beta c)已既约；它能写成4/n仅当Q|4，且此时n>p。large-slab锚点保留pK与K/alpha时也只有“锚点已为汇点”或“该固定目标像纤维为空”两种情形。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-formal-external-slab-collision-absorption-rechart
  - two-denominator-lift-source-supported-tail-ratio-rigidity
topics:
  - type-I
  - formal-target-pair
  - marked-lift
  - natural-tail
  - external-slab
  - integrality
  - rigidity
  - proof-boundary
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: formal-node-and-sink-interface
  - claim: type-I-formal-external-slab-collision-absorption-rechart
    role: single-external-slab-interface
visibility: public
last_checked: '2026-07-31'
---

# 形式节点自然双尾的整数性刚性与 E4 空纤维边界

## 1. 给定形式节点规范确定的自然双尾

固定素数与图表数据

\[
p\equiv1\pmod {24},
\qquad
R\ge3,
\qquad
R\equiv3\pmod4,
\]

\[
4K=pR+1
\tag{1}
\]

以及一个正互素形式节点

\[
A+B=Rm,
\qquad (A,B)=1.
\tag{2}
\]

若 \(d\mid m,A\)，则 \(d\mid Rm-A=B\)，故 \(d=1\)。交换 \(A,B\) 同理，得到

\[
\boxed{(m,A)=(m,B)=1.}
\tag{3}
\]

定义正有理数

\[
U=\frac{mK}{B},
\qquad
V=\frac{mK}{A}.
\tag{4}
\]

由 (1)--(2)，

\[
\frac1U+\frac1V
=\frac{A+B}{mK}
=\frac RK
=\frac4p-\frac1{pK}.
\]

所以

\[
\boxed{
\frac4p=\frac1{pK}+\frac1U+\frac1V.
}
\tag{5}
\]

这里 (5) 首先只是有理恒等式。由 (3)，

\[
U\in\mathbb N\iff B\mid K,
\qquad
V\in\mathbb N\iff A\mid K.
\tag{6}
\]

再由 \((A,B)=1\)，两者同时成立当且仅当

\[
\boxed{AB\mid K.}
\tag{7}
\]

此时 (5) 本身就是原素数 \(p\) 的三单位分数解；在形式图中，这也正是没有容量超额
的汇点条件。反之，若例如 \(B\mid K\) 而 \(A\nmid K\)，固定根分母 \(pK\) 与好尾
\(U=mK/B\) 后，定义固定目标坐标的像纤维

\[
\mathcal F_{A,B,m}
=\left\{w\in\mathbb N:
\frac4p=\frac1{pK}+\frac1U+\frac1w
\right\}.
\tag{7a}
\]

剩余项由 (5) 唯一强制为 \(1/w=1/V=A/(mK)\)。因为 \(V\notin\mathbb N\)，
\(\mathcal F_{A,B,m}=\varnothing\)。这里证明为空的是指定目标坐标的像纤维；它不声称
某个尚未定义的较小方程源标记集本身为空。

## 2. single-external slab 的既约坏残余

再设节点可定向为

\[
A=Q\alpha,
\qquad B=\beta,
\qquad Q=q^e,
\qquad K=\alpha\beta c,
\qquad q\nmid K.
\tag{8}
\]

由 \(Q\alpha+\beta=Rm\) 模 \(q\) 化简可知 \(q\nmid Rm\)：若 \(q\mid Rm\)，便有
\(q\mid\beta\)，与 \(\beta\mid K,q\nmid K\) 矛盾。因此

\[
(Q,m\beta c)=1.
\tag{9}
\]

式 (4)--(5) 化为

\[
U=m\alpha c\in\mathbb N,
\qquad
V=\frac{m\beta c}{Q}\notin\mathbb N,
\tag{10}
\]

以及

\[
\boxed{
\frac4p
=\frac1{pK}+\frac1{m\alpha c}+\frac{Q}{m\beta c}.
}
\tag{11}
\]

由 (9)，最后一项已经既约。若试图把它解释成一个较小普通目标 \(4/n\)，则

\[
\frac{Q}{m\beta c}=\frac4n
\quad\Longleftrightarrow\quad
nQ=4m\beta c.
\]

式 (9) 强制 \(Q\mid4\)。因 \(Q\ge2\)，只有 \(Q=2,4\) 可能；反过来这两种情形
确实给出整数 \(n=4m\beta c/Q\)。但 (11) 中前两项严格为正，所以

\[
\frac4p>\frac4n,
\qquad\text{即}\qquad n>p.
\tag{12}
\]

因此坏残余要么根本不是普通 \(4/n\)，要么只产生更大的目标，不能作为严格递降。

## 3. 三锚点上的相同刚性

large-slab 的规范 peeling 到达

\[
(A,B,m)=(\alpha,R-\alpha,1),
\qquad \alpha\in\{1,2,3\},
\qquad \alpha\mid K.
\tag{13}
\]

固定根分母 \(pK\) 与好尾 \(K/\alpha\) 后，唯一剩余项为

\[
\frac4p-\frac1{pK}-\frac{\alpha}{K}
=\frac{R-\alpha}{K}
=\frac1{K/(R-\alpha)}.
\tag{14}
\]

所以自然第三尾为整数当且仅当 \(R-\alpha\mid K\)。又因
\((\alpha,R-\alpha)=1\) 且 \(\alpha\mid K\)，这等价于

\[
\alpha(R-\alpha)\mid K,
\tag{15}
\]

即锚点已经是形式汇点并由 (5) 直接终端。否则对应固定目标像纤维为空。

## 4. 对 E4 路线的含义

这一定理排除了以下特定方案：沿 formal peeling 保留根分母 \(pK\)，再保留由当前
\(K\)-内坐标给出的自然好尾，只递归求解另一尾。该方案不是一个尚待证明的 E4；在
非汇点上，指定的目标像纤维就是空集。因而任何非空源标记集都不可能通过一个保持
\(pK\) 与该好尾的映射落入此像纤维；这不是对任意其它标记状态非空性的断言。

它没有排除改变根分母、同时改变两条尾、改变 equation target、使用非自然标记，或先
跨图表再构造新的全域提升。下一条合法 E4 若要产生新信息，至少必须改变这些数据之一。

冻结源见证锚定 formal Reach 上的聚焦算术核验见
[large-slab 完整 formal Reach 边界](type-I-psi-one-actual-reach-large-slab-boundary.md)及其复现程序
`reproductions/type_i_psi_one_large_slab_reach_boundary.py`。
