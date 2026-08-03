---
kind: claim
claim_id: type-I-overflow-d-one-p-minus-two-g-rechart
title: d=1 overflow 的 p-2 G 重图表正规形
statement: 设核心素数 p≡1 (mod 24) 的 verified overflow 满足 pn=4M+1（即 d=1）。则 n≡1 (mod 4)、M mod p=(p-1)/4，载体 r=(p-1)/4 的规范图表为 R_r=p-2、K_r=(p-1)^2/4。对 K_r 的每个素因子 q 都有 (q/(p-2))=1，而 (-1/(p-2))=-1；因此该后继是 G 态，支撑内目标纤维为空。它不是保持旧支撑的递归边；若 p+4 含 3 (mod 4) 素因子，则另由独立的 p+4 Type II 终端闭合，否则必须寻找非支撑终端或其它 marked/容量出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-canonical-complete-support-rechart-g-obstruction
topics:
  - type-I
  - overflow
  - d-one
  - p-minus-two
  - G-state
  - jacobi-symbol
  - rechart
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: d-one-normal-form-and-jacobi-separator-receipt
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused-d-one-boundary-receipt
visibility: public
last_checked: '2026-08-03'
---

# d=1 overflow 的 (p-2) G 重图表正规形

## 定理

设 (pequiv1pmod {24}) 为素数，一个已验证的 overflow 满足

\[
pn=4M+1.
\tag{1}
\]

这正是 overflow 行列式 (pn=4Md+1) 的 (d=1) 分支。令

\[
r=\frac{p-1}{4}.
\tag{2}
\]

则

\[
n\equiv1\pmod4,
\qquad
M= p\frac{n-1}{4}+r,
\qquad
M\equiv r\pmod p.
\tag{3}
\]

载体 (r) 的规范图表为

\[
R_r=p-2,
\qquad
K_r=r(p-1)=\frac{(p-1)^2}{4}=4r^2.
\tag{4}
\]

而且对每个 (q\mid K_r)，都有

\[
\left(\frac q{p-2}\right)=1,
\qquad
\left(\frac{-1}{p-2}\right)=-1.
\tag{5}
\]

所以 ((p,p-2,K_r)) 是 G 态：由 (K_r) 的素支撑生成的 Jacobi 角色在 (-1)
上分离，目标纤维在支撑内为空。

## 证明

由 (p\equiv1\pmod4) 及 (1)，有 (n\equiv1\pmod4)。写

\[
n=4k+1.
\]

则

\[
M=\frac{p(4k+1)-1}{4}=pk+\frac{p-1}{4},
\]

得到 (3)。因为 (p-2\equiv-1\pmod {4r})，规范同余

\[
pR_r\equiv-1\pmod {4r}
\]

的代表为 (R_r=p-2)，代回 (K_r=(pR_r+1)/4) 得 (4)。

再证 Jacobi 分离。首先 (p\equiv1\pmod8)，故 (p-2\equiv7\pmod8)，从而

\[
\left(\frac2{p-2}\right)=1.
\]

设 (q) 是任意奇素数且 (q\mid K_r)。此时 (q\mid p-1)，所以

\[
p-2\equiv-1\pmod q.
\]

又 (p-2\equiv3\pmod4)，且 ((p-3)/2) 为奇数。二次互反律给出

\[
\left(\frac q{p-2}\right)
=(-1)^{(q-1)/2}\left(\frac{p-2}{q}\right)
=(-1)^{(q-1)/2}\left(\frac{-1}{q}\right)=1.
\]

最后，(p-2\equiv3\pmod4)，故

\[
\left(\frac{-1}{p-2}\right)=-1.
\]

这证明 (5) 及 G 分类。证毕。

## 与选择器的关系

该正规形给出一个无样本的分支收缩，但不构成递归边：

1. (r=(p-1)/4) 通常不包含旧 charged support (A>1)，所以不能把载体变小误写为
   support-preserving RESET；
2. 后继的目标纤维在 (K_r) 支撑内为空，不能由恒等标记提升闭合；
3. 既有的 universal (p)-source 可把 G 状态一步送到 ((1,p-3,1))，但这仍是
   source/analysis 证书，不是 E1--E5 递归边；
4. 若 (p+4) 有 (3\pmod4) 因子，则 `terminal-first` 先独立登记 p+4 Type II
   证书。若没有该因子，d=1 分支的剩余任务明确变成非支撑 Type I/II、marked lift
   或跨状态容量，而不是继续寻找固定-(n) 支撑边。

还有一个与 fixed-s 有界除子选择器直接相容的负边界。d=1 时

\[
r=\frac{p-1}{4},\qquad s=1,\qquad rd=r.
\]

由于 \(B_p=(p-1)^2/4=4r^2\)，若 \(A<r\)，则取 \(L=r\) 有
\[
\left\lfloor\frac{B_p}{L}\right\rfloor=4r
<
\left\lfloor\frac{B_p}{A}\right\rfloor,
\]
且 \(4L>s\)，所以 \(L=r\) 给出完整 fixed-s 恒等提升边。反之若当前 charged
support 满足 \(A\ge r\)，则任意 \(L\mid rd\) 都有 \(L\le r\le A\)，不可能满足
固定-s 外层秩边所需的 \(A<L\)。因此
\[
\boxed{A<r\Longleftrightarrow L=r\text{ 是 fixed-s 严格降边；}\quad
A\ge r\Longrightarrow\text{fixed-s 有界除子图谱为空}.}
\]
后者不是选择器漏检；后继只能来自非支撑 Type I/II、marked lift 或跨状态容量。

因此该定理把 d=1 从“固定-(n) 候选为空”的算术杂项，收缩为一个普适的 G 边界；它
没有关闭一般 (A>1, R_M>p) overflow。

## 聚焦回执

统一选择器记录的 d=1 行为为

\[
(p,M,n)=(73,91,5),
\qquad
r=18,
\qquad
(R_r,K_r)=(71,1296),
\]

支撑 (2,3) 的 Jacobi 值均为 (+1)，而目标 (-1) 的值为 (-1)。同一素数的
(p+4=77=7\cdot11) 提供独立 Type II 终端，因此回执保持
`selector_status=analysis_evidence`、`recursive_edge_eligible=false`。

聚焦命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```
