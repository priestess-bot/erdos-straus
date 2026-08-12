---
kind: claim
claim_id: type-I-overflow-full-product-d-one-complete-excess-capacity-map
title: 完整乘积 d=1 饱和高锚的完整超额容量公式与 p-源门
statement: >-
  固定核心素数 p≡1 (mod 24)，并令 n>1、n≡1 (mod 4)、
  A=(pn-1)/4、R=(p-1)n-1、K=A(p-1)。这是完整乘积 d=1 饱和支的
  算术高锚。对其 R-1 侧的完整超额块
  Q=∏_{v_q(R-1)>v_q(K)}q^{v_q(R-1)}，令
  T=(R-1)/2、g=gcd((p+1)/2,(n+1)/2)。则精确有
  lcm(A,Q)/A=Q/gcd(A,Q)=T/g>1。并且 high-R universal p-source 的
  primitive 门与 bundle 的 p-free 门分别等价于 n≢-1 (mod p) 和
  n≢-2 (mod p)；在 1<n<p 的低分母支两门自动成立。因此在两门通过且该支已有真实
  persistent parent 时，便有唯一的 path-anchored complete-excess 严格 support
  容量升级可供后续 selector 审查。该结论只给 raw-path/E1 候选与整数容量；它不
  单独给 typed state、E2--E5、terminal 或 verified recursive edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-unbounded-full-product-quotient-fold
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - fixed-n
  - full-product
  - d-one
  - high-anchor
  - complete-excess-bundle
  - charged-support
  - universal-source
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-overflow-unbounded-full-product-quotient-fold
    role: d-one-support-saturated-overflow-normal-form
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: raw-p-source-and-path-anchored-bundle-contract
  - claim: type-I-high-anchor-cofactor-macro-e1-e4-admission
    role: high-anchor-admission-boundary
  - reproduction: reproductions/type_i_overflow_d_one_complete_excess_capacity_map.py
    role: focused-capacity-formula-and-p-gate-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 \(d=1\) 饱和高锚的完整超额容量公式与 \(p\)-源门

## 1. d=1 残余的高锚正规形

固定

\[
p\equiv1\pmod {24},
\qquad
n>1,
\qquad
n\equiv1\pmod4,
\tag{1}
\]

并写

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{2}
\]

这正是完整乘积商折叠唯一算术 stutter \((M,d;A)=(A,1;A)\) 的图表。
直接重算得

\[
pR+1=4K,
\qquad
A\mid K,
\qquad
p<R<4A,
\qquad
R\equiv3\pmod4.
\tag{3}
\]

故 (2) 是一个算术 high anchor。它还不是 persistent charged state：后者仍须有精确
parent receipt、scope 和 typed normal form。以下只研究一旦这些前提已经具备时，
该 high anchor 的唯一 complete-excess bundle 究竟携带多少新容量。

令

\[
T:=\frac{R-1}{2}=\frac{(p-1)n-2}{2},
\qquad
Q:=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)},
\qquad
\beta:=\frac{R-1}{Q}.
\tag{4}
\]

这里 \(Q\) 是现有 high-\(R\) `complete_excess_bundle` 的确定性定义，而不是可任意
挑选的因子。

## 2. 完整超额的精确 support 倍率

**定理。** 设

\[
g:=\gcd\left(\frac{p+1}{2},\frac{n+1}{2}\right).
\tag{5}
\]

则

\[
\boxed{
\frac{\operatorname{lcm}(A,Q)}{A}
=\frac{Q}{(A,Q)}
=\frac{T}{(T,A)}
=\frac{T}{g}
>1.
}
\tag{6}
\]

特别地，完整超额块必非平凡，且 path-anchored carrier 唯一确定为

\[
\boxed{
M=\operatorname{lcm}(A,Q)
=A\,\frac{((p-1)n-2)/2}
 {\gcd((p+1)/2,(n+1)/2)}
>A.
}
\tag{7}
\]

**证明。** 写 \(p-1=4c\)。由 (1)，\(T=2cn-1\) 是奇数，且

\[
(T,c)=1.
\tag{8}
\]

又 \(v_2(R-1)=1<v_2(K)\)，所以 \(2\) 不属于 \(Q\)。对每个奇素数
\(q\mid T\)，(8) 给出 \(q\nmid p-1\)，从而

\[
v_q(K)=v_q(A).
\tag{9}
\]

按 (4) 的逐素数定义，(9) 意味着

\[
\frac{Q}{(A,Q)}
=\prod_{v_q(T)>v_q(A)}q^{v_q(T)-v_q(A)}
=\frac{T}{(T,A)}.
\tag{10}
\]

另一方面，令 \(v=(n+1)/2\)。由于 \(T\) 为奇数且

\[
4A-2T=n+1=2v,
\tag{11}
\]

有

\[
2(T,A)=(2T,4A)=(2T,2v)=2(T,v).
\tag{12}
\]

模 \(v\) 使用 \(n\equiv-1\)，得到

\[
2T=(p-1)n-2\equiv-(p+1)\pmod v.
\tag{13}
\]

而 \(v\) 为奇数，故 \((T,v)=((p+1)/2,v)=g\)。将此代入 (10) 即得 (6) 的
三个等式。

最后 \(g\le v\)，而

\[
T-v=\frac{(p-2)n-3}{2}>0,
\tag{14}
\]

故 \(T/g>1\)。证毕。

式 (6) 特别重要：即使 \(Q\) 和 \(A\) 有共同素因子，真正新增的 charged capacity
也不是 \(Q\) 本身，而是精确的 \(Q/(A,Q)\)。例如下面的 \((p,n)=(73,73)\)
有 \(T=37\cdot71\)、\((T,A)=37\)，所以 complete-excess block 是 \(Q=71\)，
不是整个 \(T\)。

## 3. 两条独立的 \(p\)-门

high-\(R\) universal source 是

\[
\bigl(p,\ R(p-1)-p,\ p-1\bigr)
\xrightarrow[q=p,\ t=1]{}
(1,R-1,1).
\tag{15}
\]

它的 primitive 条件是 \(p\nmid R\)。由 (2)，

\[
R\equiv-n-1\pmod p,
\qquad
\boxed{p\nmid R\ \Longleftrightarrow\ n\not\equiv-1\pmod p.}
\tag{16}
\]

另一方面 \(p\nmid K\)，因为 \(4A=pn-1\) 且 \(p\nmid p-1\)。所以若 \(p\mid R-1\)，
它必以完整幂进入 (4) 的超额块 \(Q\)；反向由 \(Q\mid R-1\) 立即成立。又

\[
R-1\equiv-n-2\pmod p,
\qquad
\boxed{p\nmid Q\ \Longleftrightarrow\ n\not\equiv-2\pmod p.}
\tag{17}
\]

这是两个不同的门。前者保证 (15) 是 primitive raw \(p\)-path；后者保证
\(p\nmid\operatorname{lcm}(A,Q)\)，使 high-\(R\) complete-excess adapter 的
canonical rechart 有定义。

若

\[
1<n<p,
\tag{18}
\]

则因 \(n\equiv1\pmod4\) 和 \(p\equiv1\pmod4\)，有 \(5\le n\le p-4\)。因此
\(n\) 不可能同余于 \(-1\) 或 \(-2\pmod p\)，(16)--(17) 两门自动通过。

## 4. 该容量图实际提供什么

在 (16)--(17) 都通过时，现有 `high_R_path_anchored_bundle_v1` 的完整算术输入均已
具备：

\[
Q>1,
\qquad
\beta\mid K,
\qquad
(Q,\beta)=1,
\qquad
Q\nmid K,
\qquad
p\nmid Q,
\tag{19}
\]

并且 (6) 给出严格的支撑容量升级 \(A\mapsto M\)。因此这个完整超额 bundle 不是对
\(d=1\) 残余的猜测性启发式，而是唯一的、可逐素数复算的 path-anchored 候选。

但它**尚不是递归出口**。要将其登记为边，仍缺少或仍须逐个重放的内容是：

1. \(H=(p,R,K;A)\) 的真实 persistent parent、charged ledger 与原样 scope；
2. bundle rechart 的独立 typed F/G/hit 重分类和 terminal-first 分派；
3. 若走 direct cofactor 宏，E2 的 residue gate、完整三段状态回执及 E5；
4. 若 rechart 是 marked absorb 或另一种 overflow，适用 selector 的相应全域严格势。

尤其不能把 (15) 的普遍 raw parent 反向构造当作 E1 root policy，也不能从 \(M>A\)
本身推出持久边。这些边界正是 state contract 所要求的内容。

## 5. 聚焦回执

```bash
python3 reproductions/type_i_overflow_d_one_complete_excess_capacity_map.py --verify
```

回执不搜索素数或分母。它固定核验两个低分母的双门通过例、一个 \(A\)--\(Q\) 估值重叠
例，以及分别使 (16)、(17) 失败的两个独立边界例。
