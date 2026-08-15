---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-p-free-p-block-provenance-obstruction
title: q=1 高 C=2 19 相位 H4 p-free 门失败的 p-block 来源障碍
statement: >-
  在 q=1 high C=2 19-phase 的 actual persistent H4 receipt 中，若 R4=1 (mod p)，令
  p^e||R4-1，Q5=Q_K4(R4-1)=p^e Q0，且 R4-1=Q5 beta。则 beta 整除
  gcd(R4-1,K4)=2 gcd((p+1)/2,c3-s4)，所以 beta<=p+1；M0=lcm(M4,Q0) 是 p-free
  并有唯一算术 canonical chart，但不是合法的 path-anchored complete-excess target。
  事实上，从 actual p-source anchor 真实剥离 p^e 次后得到
  y=(R4-1)/p^e=Q0 beta、x=R4-y，且恒有 x 不整除 K4，从而 x beta 不整除 K4。
  所以 Q0 不满足 peeled node 的 clean-bundle E1 条件，不能静默删除 p-block 或将 M0
  登记为 recursive edge。该 H4 残余必须继续 actual raw Reach，直到直接 Type I/II
  terminal 或新的已支付 p-free bundle；本卡不提供此 residual 的全称 exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - p-free-failure
  - p-primary-peeling
  - complete-excess
  - source-provenance
  - competing-excess
  - capacity-map
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: exact-overlap-cofactor-bound
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: actual-H4-carrier-and-persistent-parent
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: actual-raw-peeling-semantics
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: peeled-node-clean-bundle-E1-condition
  - concept: denominator-escape-state-contract
    role: path-anchored-provenance-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_p_free_p_block_provenance_obstruction.py
    role: exact-H4-local-p-block-peeling-controls
visibility: public
last_checked: '2026-08-15'
---

# H4 \(R_4\equiv1\pmod p\) 的 p-block 不能静默删除

## 1. 剩余 p-free 门的精确分解

保持 H4 的既有 persistent receipt：

\[
K_4=M_4c_4,
\qquad
pR_4+1=4K_4,
\qquad
p\nmid K_4.
\tag{1}
\]

现在设

\[
R_4\equiv1\pmod p,
\qquad
p^e\parallel(R_4-1),
\qquad e\ge1.
\tag{2}
\]

令 \(V=R_4-1\)，并按相对于 \(K_4\) 的完整素数幂定义写

\[
Q_5=Q_{K_4}(V)=p^eQ_0,
\qquad
V=Q_5\beta.
\tag{3}
\]

这里 \(p\nmid Q_0\)。完整 excess 的逐素数定义还给出

\[
(Q_5,\beta)=1,
\qquad
\beta\mid K_4.
\tag{4}
\]

H4 的 exact overlap identity 因而把 retained cofactor 压成

\[
\boxed{
\beta\mid(V,K_4)
=2\left(\frac{p+1}{2},c_3-s_4\right)
\le p+1.
}
\tag{5}
\]

所以 H4 p-free failure 不是“任意大且无结构的 p-block”：它有一个完整的

\[
\boxed{(e,Q_0,\beta),\quad p\nmid Q_0,\quad \beta\le p+1}
\tag{6}
\]

容量标签。不过 (6) 还不能构造合法的 p-free edge。

## 2. 真正的 p-primary raw path

由于 (2) 给出 \(p\nmid R_4\)，H4 的 universal \(p\)-source 是 primitive，并实际到达
anchor \(\{1,V\}\)。在 \(m=1\) 层，每次选择含 \(p\) 的坐标作 \(q=p\) raw
transition，shift 恒为 \(p-1\)。恰做 \(e\) 次后得到

\[
\boxed{
y=\frac{V}{p^e}=Q_0\beta,
\qquad
x=R_4-y=1+(p^e-1)y.
}
\tag{7}
\]

每一步都没有 gcd reduction：若当前 selected coordinate 为 \(p^j y\)，新的 pair 是

\[
\left\{p^{j-1}y,\ R_4-p^{j-1}y\right\},
\tag{8}
\]

而 \((p^{j-1}y,R_4)=1\)，因为 \(R_4=1+p^e y\)。特别地，(7) 是 actual raw
lineage 上的 primitive bottom node，而不是把 \(p^e\) 从整数式中形式约去。

## 3. p-free arithmetic candidate 的 E1 失败

形式上删掉 \(p^e\) 可写成 p-free carrier

\[
M_0=\operatorname{lcm}(M_4,Q_0).
\tag{9}
\]

因 \(p\nmid M_4Q_0\)，存在唯一 \(c_0\in\{1,\ldots,p-1\}\) 使

\[
4M_0c_0\equiv1\pmod p.
\tag{10}
\]

这只是 arithmetic canonical chart。要把 \(Q_0\) 作为 (7) 的 `path_anchored`
complete-excess bundle，E1 还要求未选侧和 retained cofactor 满足

\[
x\beta\mid K_4.
\tag{11}
\]

但 (11) 永远失败。若 \(x\mid K_4\)，则从 \(4K_4=p(x+y)+1\) 得

\[
x\mid py+1.
\tag{12}
\]

当 \(e=1\)，有 \(py+1=x+y\)，而 \(0<y<x\)，与 (12) 矛盾。当 \(e\ge2\)，

\[
0<py+1<1+(p^e-1)y=x,
\tag{13}
\]

同样矛盾。因此

\[
\boxed{x\nmid K_4,\qquad x\beta\nmid K_4.}
\tag{14}
\]

式 (14) 不是 capacity 估计不足，而是 exact provenance obstruction：\(Q_0\) 不能
在 peeled node 上承担 clean complete-excess occurrence。故 (9)--(10) 不能登记为
state transition，即使 \(c_0\) 看起来严格改善。

## 4. 对 H4 residual 的影响

结合零残数的同锚 source 修复，fifth-anchor 的剩余 H4 gate 现在有唯一合法解释：

\[
R_4\equiv1\pmod p
\quad\Longrightarrow\quad
\text{保留 (7) 的 actual p-primary competing-excess Reach}.
\tag{15}
\]

可接受的后续只有：

1. 当前或后继 node 的直接 Type I/II terminal；
2. complete raw Reach 的 sink/bottom node 上重新计算一个带 E1 receipt 的 bundle；
3. 另行证明一个具备 E1--E5 的 p-primary switch。

不能从 (9) 的 p-free chart 直接声称容量下降或 \(n<p\) 递降。这把 H4 的最后
source/p-free 残余压成一个明确、带小 cofactor \(\beta\) 的 actual raw-state problem，
而不是留下一个未定义的“有限例外”。

## 5. 范围

本卡不证明 (15) 必在有界步数终止，也不处理其 general raw Reach 的可能 SCC。它不替代
G/Type I global selector、typed reclassification、terminal-first 或全域解提升；它只排除
一条会错误地删除 source debt 的假 rechart，并给出之后必须保留的 p-primary state contract。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_p_free_p_block_provenance_obstruction.py --verify
```

回执检查两个 H4 局部整数控制（\(e=1,2\)）；它们不是 actual 19-phase H3 ancestors，
只验证 (3)--(14) 的 p-block arithmetic 与 raw lineage。
