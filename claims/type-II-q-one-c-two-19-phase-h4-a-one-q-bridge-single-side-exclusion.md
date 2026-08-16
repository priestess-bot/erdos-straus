---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
title: 高 H4 clean q-bridge 的单侧完整超额排除与强制 atomic split
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 的 clean
  q bridge 中，endpoint (x_q,y_q)=((q-1)y_q+h,y_q) 满足 p=hq-1、q>1、
  y_q>ph+1。若 Q_x=Q_K4(x_q)=1，则 x_q divides K4，从而
  a=(p y_q+1)/x_q 是整数。写 a=h+j，必有 j>=1，且
  (h-1-j(q-1))y_q=h(h+j)-1。由于 q 是大于 1 的奇数，得到
  y_q<=2h^2-2h-1；但 high H4 下 y_q>ph+1>=3h^2-h+1，矛盾。
  因而 Q_x>1。既有 Q_y>1、p-free endpoint 和 first-stutter closure 遂把每个
  actual nonterminal endpoint 收缩为严格容量的 p-free atomic-split pre-receipt，
  不再有 y-side single-side payload。此结论只缩小 T1 的算术/来源分支；atomic
  E1--E5、terminal-first、typed target、owner/ledger 与 serializer 仍须独立完成。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - type-I-path-anchored-atomic-split-complete-excess-admission
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - complete-excess-bundle
  - one-sided-payload
  - atomic-split
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-endpoint-identity-and-maximal-blocks
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
    role: high-H4-lower-bound-y-greater-than-ph-plus-one-and-Qy-nonempty
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: endpoint-p-free-domain
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
    role: strict-capacity-after-arithmetic-stutter-closure
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: remaining-conditional-atomic-admission-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_single_side_exclusion.py
    role: focused-high-controls-and-low-height-sharpness-control
visibility: public
last_checked: '2026-08-17'
---

# 高 H4 clean \(q\)-bridge 的单侧完整超额排除

## 1. 结论的位置

已有 clean \(q\)-bridge 分派、\(y\)-block 非空性、endpoint \(p\)-primary 排除和
first-stutter source \(D\)-gate 已知：actual high H4 endpoint 的算术余项原本可写为

\[
Q_x=1<Q_y
\quad\text{或}\quad
Q_x,Q_y>1,
\tag{1}
\]

且在两种情形中都有 \(p\nmid Q_xQ_y\) 与严格容量 \(c_q\le p-2\)。第一行是
\(y\)-side single-side payload；第二行才是双色 atomic payload。本卡证明第一行在
actual high H4 scope 中也为空。

这不是把一个算术严格性改称为已注册边。它只把 T1 的 live endpoint taxonomy 从
“single-side 或 atomic”缩成“atomic”，从而使随后需要支付的 E1--E5 义务集中到一个
具名 primitive。

## 2. 高度与 endpoint 恒等式

沿用 actual clean bridge 的记号

\[
p=hq-1,
\qquad q>1,
\qquad
R_4=qy_q+h,
\qquad x_q=R_4-y_q=(q-1)y_q+h,
\tag{2}
\]

\[
pR_4+1=4K_4.
\tag{3}
\]

这里 \(h=2d\)，而 \(d,q\mid(p+1)/2\)。由于 \(p\equiv1\pmod {24}\)，
\((p+1)/2\) 为奇数；故 \(q>1\) 为奇数，特别有

\[
q\ge3,
\qquad h\ge2.
\tag{4}
\]

H4 height 已给出严格下界

\[
\boxed{y_q>ph+1=h^2q-h+1\ge3h^2-h+1.}
\tag{5}
\]

注意 (5) 比“\(y_q\) 很大”的渐近描述更强：它正好足以和下面的整除上界发生矛盾。

## 3. 左侧 block 为空会强制一个低高度 endpoint

### 引理 1（single-side 的整数上界）

在 (2)--(4) 下，若 \(Q_{K_4}(x_q)=1\) 且 \(y_q>h+1\)，则

\[
\boxed{y_q\le2h^2-2h-1.}
\tag{6}
\]

**证明。** \(Q_{K_4}(x_q)=1\) 的定义等价于 \(x_q\mid K_4\)。由 (3) 和
\(R_4=x_q+y_q\)，有

\[
x_q\mid py_q+1.
\tag{7}
\]

令

\[
a=\frac{py_q+1}{x_q}\in\mathbb Z_{>0}.
\tag{8}
\]

使用 \(p=hq-1\) 与 (2)，直接得到

\[
py_q+1-hx_q=(h-1)(y_q-h-1)>0.
\tag{9}
\]

于是 \(a=h+j\)，其中 \(j\ge1\)。把它代回 (8) 给出精确恒等式

\[
\bigl(h-1-j(q-1)\bigr)y_q=h(h+j)-1.
\tag{10}
\]

右侧为正，所以左侧系数也为正。因而

\[
j(q-1)\le h-2,
\qquad j\le h-2.
\tag{11}
\]

式 (10) 的左侧系数至少为 \(1\)，故

\[
y_q\le h(h+j)-1\le h(2h-2)-1=2h^2-2h-1,
\]

即得 (6)。\(\square\)

### 定理 2（actual high H4 没有 y-side single-side endpoint）

在 actual high H4 clean \(q\)-bridge 中，

\[
\boxed{Q_x=Q_{K_4}(x_q)>1.}
\tag{12}
\]

**证明。** 若 \(Q_x=1\)，则 (5) 自动蕴含 \(y_q>h+1\)，可应用引理 1。于是同时有

\[
y_q\le2h^2-2h-1
\quad\text{和}\quad
y_q>3h^2-h+1.
\tag{13}
\]

但右端下界减去左端上界为 \(h^2+h+2>0\)，矛盾。\(\square\)

## 4. endpoint taxonomy 的收缩

既有 high-H4 \(y\)-block 引理给 \(Q_y>1\)。配合 (12)、endpoint p-primary
排除和 first-stutter closure，任何 actual nonterminal endpoint 现在满足

\[
\boxed{
Q_x,Q_y>1,
\qquad p\nmid Q_xQ_y,
\qquad c_q\le p-2.
}
\tag{14}
\]

所以它是 `path_anchored_atomic_split_complete_excess_v1` 的完整算术输入，且相对于
H4 persistent parent 的容量坐标已严格付款。被删除的恰是

\[
Q_x=1<Q_y
\tag{15}
\]

这条 single-side branch；它不再需要单独寻找 source/serializer repair。

仍未支付的项目不能被 (14) 掩盖：actual source 必须有可重放 persistent path，atomic
adapter 必须重算两端 typed state 和 scope，terminal/alternate priority 必须先执行，owner
tuple 与所需 ledger 语义必须闭合，最后才可把 identity solution lift 和已付款的 E5 登记为
verified edge。因此这是一条 T1 约化引理，不是 T1 或 F0 的完成。

## 5. 高度假设不可删除

低高度的纯整数控制说明结论并不是 (2)--(3) 的形式恒等式。取

\[
(p,h,q,y,x,R,K)=(433,62,7,71,488,559,60512).
\tag{16}
\]

它满足

\[
p=hq-1,
\quad R=qy+h=x+y,
\quad pR+1=4K,
\quad h=(R-1,K),
\quad (q,K)=1,
\tag{17}
\]

且

\[
x\mid K,
\qquad Q_K(x)=1,
\qquad Q_K(y)=71>1.
\tag{18}
\]

但是 \(y=71<ph+1=26847\)，因此它不满足 actual H4 high condition。这个控制固定了
引理真正使用的是 high-height 与整除的组合，而不是把一般 clean endpoint 的
single-side 行误删。

## 6. 聚焦复现

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_single_side_exclusion.py --verify
```

脚本重放两个既有 high H4 local controls，检查 (4)--(6) 与两侧 complete-excess block；
再重放 (16) 的低高度 single-side 控制。它不扫描素数、分母、Reach graph 或 terminal 菜单。
