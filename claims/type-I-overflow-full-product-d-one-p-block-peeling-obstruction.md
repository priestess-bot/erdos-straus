---
kind: claim
claim_id: type-I-overflow-full-product-d-one-p-block-peeling-obstruction
title: 完整乘积 d=1 的 p-free 失败块剥离与来源丢失障碍
statement: >-
  在完整乘积 d=1 饱和行的 p-free failure 类中，设 p^e||E 且完整超额块
  Q=p^e Q_0。完整 carrier M=AE 含 p，故绝无 canonical Type I chart。形式删除
  p^e 后的 M_0=A(E/p^e) 虽为 p-free 并有唯一算术 canonical chart，却不保留原
  path-anchored complete-excess receipt：从 anchor (1,R-1,1) 沿真实 q=p raw 边
  恰剥离 e 次后到达 y_0=(R-1)/p^e、x_0=R-y_0；全称有 x_0不整除K，因而原余块
  beta 即使整除K，也有 x_0 beta不整除K。故 Q_0 不是 peeled node 上的 clean
  complete-excess bundle，M_0 只是无来源算术候选，不能登记 recursive edge。合法后续
  必须保留 peeled competing-excess node 并继续完整 raw Reach，直到直接 Type I
  terminal 或重新得到新的 p-free sink bundle。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - p-free-failure
  - p-primary-peeling
  - competing-excess
  - complete-excess-bundle
  - source-provenance
  - strict-obstruction
sources:
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: exact-excess-multiplier-and-p-free-gate
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: actual-m-one-raw-peeling-semantics
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: clean-complete-excess-receipt-condition
  - reproduction: reproductions/type_i_overflow_d_one_p_block_peeling_obstruction.py
    role: focused-p-block-peeling-and-provenance-loss-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 \(d=1\) 的 \(p\)-free 失败块剥离与来源丢失障碍

## 1. p-primary 完整块

固定核心素数 \(p\equiv1\pmod {24}\) 和完整乘积 \(d=1\) 饱和行

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{1}
\]

令 \(Q\) 是 anchor \((1,R-1,1)\) 的完整超额块，\(R-1=Q\beta\)，并令

\[
M=\operatorname{lcm}(A,Q)=AE
\tag{2}
\]

为其规范 carrier。现在假设 \(p\)-free 门失败，即

\[
p\mid Q
\quad\Longleftrightarrow\quad
p\mid E
\quad\Longleftrightarrow\quad
n\equiv-2\pmod p.
\tag{3}
\]

因为 \(p\nmid A,K\)，\(p\) 在 \(R-1\) 中的完整幂全部属于 \(Q\)，且

\[
e:=\nu_p(R-1)=\nu_p(Q)=\nu_p(E)\ge1.
\tag{4}
\]

写

\[
Q=p^eQ_0,
\qquad
E=p^eE_0,
\qquad
p\nmid Q_0E_0.
\tag{5}
\]

## 2. 完整 carrier 不可能 canonical rechart

任何合法 Type I chart 都满足

\[
4K_T=pR_T+1,
\tag{6}
\]

所以 \(p\nmid K_T\)。若 support \(M\) 合法，还须 \(M\mid K_T\)；但 (3)--(5)
给出 \(p\mid M\)，立即矛盾。等价地，若

\[
4M\mid pR_T+1,
\tag{7}
\]

则模 \(p\) 得 \(0\equiv1\)。因此完整 carrier 没有 canonical chart，这不是实现层
缺少 modular inverse，而是严格的算术不可能。

形式删去该块会得到

\[
M_0:=\operatorname{lcm}(A,Q_0)=AE_0=\frac{M}{p^e}.
\tag{8}
\]

由于 \(p\nmid M_0\)，它确实有唯一算术 canonical chart；若写目标 cofactor 为
\(c_0\)，则

\[
c_0\equiv-E_0^{-1}\pmod p.
\tag{9}
\]

但 (8)--(9) 尚不构成 path-anchored action。下一节证明来源条件全称失败。

## 3. 真实 p-peeling 后的 competing excess

从 anchor

\[
\{1,R-1\},\qquad m=1,
\tag{10}
\]

每次选择 \(R-1\) 所在一侧的 \(q=p\) raw 边。因为 \(m=1\)，shift 为 \(p-1\)，
且节点始终保持在 \(m=1\)。恰做 \(e\) 次后，得到 primitive bottom node

\[
\boxed{
y_0=\frac{R-1}{p^e}=Q_0\beta,
\qquad
x_0=R-y_0=1+(p^e-1)y_0.
}
\tag{11}
\]

### 定理 2（删 p-block 的 clean-receipt 障碍）

对 (11) 全称有

\[
\boxed{x_0\nmid K},
\qquad
\boxed{x_0\beta\nmid K}.
\tag{12}
\]

**证明。** 若 \(x_0\mid K\)，则由 \(4K=pR+1\) 和 \(R=x_0+y_0\) 得

\[
x_0\mid py_0+1.
\tag{13}
\]

当 \(e=1\) 时，

\[
py_0+1=x_0+y_0,
\qquad
0<y_0<x_0,
\tag{14}
\]

所以 (13) 不可能。当 \(e\ge2\) 时，

\[
0<py_0+1<1+(p^e-1)y_0=x_0,
\tag{15}
\]

同样不可能。第一式得证，第二式立即随之成立。证毕。

complete-excess receipt 在定向节点 \(\{x,y\}\)、\(y=Q\beta\) 上不仅要求所选侧
包含超额块，还要求

\[
x\beta\mid K.
\tag{16}
\]

式 (12) 说明 peeled node 对 \(Q_0\) 严格不满足 (16)。换言之，剥去 \(p^e\) 后，
另一坐标 \(x_0\) 必然携带新的 competing excess。直接把 \(Q_0\) 送入 (8) 会丢失
真实 raw lineage 的另一半容量债务。

## 4. 精确结论与合法后续

因此，下面的捷径不合法：

```text
Q = p^e Q0 is not p-free
=> silently replace Q by Q0
=> canonical rechart support M0
```

失败原因不是 target rank 未知，而是 E1 的 path-anchored residual divisibility 已由
(12) 严格否定。即便 (9) 给出很小的 target capacity，仍不能把它登记为 candidate
transition。

合法后续必须保留 (11) 这个真实 primitive competing-excess node，并运行完整 raw
Reach。有限 Reach 定理保证最终进入以下分派之一：

1. 无出边节点，直接恢复 Type I terminal；
2. bottom sink-SCC，在其最小节点重新计算两侧全部完整超额块；
3. 新 bundle 若 \(p\)-free，再按真实 parent capacity 审查 canonical target 与 E5；
4. 新 bundle 若仍含 \(p\)，继续保留实际 raw 路径，而不是静默删除块。

后续的
[真实剥离小锚点定理](type-I-overflow-full-product-d-one-p-free-peeled-small-anchor.md)
已经把这条合法后续进一步算清：沿 (11) 的 \(y_0\) 侧继续做真实容量剥离，必到达
\(\{2g,R-2g\}\)，下一容量坐标整除 \(2gp+1\)，且除 \(a=1\) 外重新得到
\(p\)-free clean bundle；该分支的 \(L\equiv1\pmod p\) 等容量情形也已被整除反证
全称排除。算术上只剩 \(a=1\) 的继续 Reach。因此本卡是一个全称 no-go 和精确接口
收缩，不是 \(p\)-free failure 类的最终出口定理。

## 5. 聚焦回执

```bash
python3 reproductions/type_i_overflow_d_one_p_block_peeling_obstruction.py --verify
```

回执只检查固定 \(p=73\) 的初始 \(n=217\) 与倒计时端点
\(n=1020794549\)。它逐步重放真实 \(p\)-raw peeling、验证 (11)--(16)，并确认删块
carrier 的算术 chart 存在但 complete-excess 来源条件失败；不运行完整 Reach 或历史
selector。
