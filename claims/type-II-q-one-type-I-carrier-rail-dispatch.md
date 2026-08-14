---
kind: claim
claim_id: type-II-q-one-type-I-carrier-rail-dispatch
title: q=1 源到低 Type I 图表的精确载体 rail 与首个分派
statement: >-
  令 p=24t+1 为核心素数、X=(p+3)/4=6t+1，并令一个合法 Type I 图表满足
  4K=pR+1。恒有 gcd(X,K)=gcd(X,3R-1)。因此，对任何 J|X 且 J=1 (mod 3)，
  含 J 的全部正合法 Type I 图表恰为
  R=(8J+1)/3+4Jz、z>=0；其 K 满足
  gcd(X,K)=J*gcd(X/J,2+3z)。特别地 z=0 是唯一最小且恰保留 J 的图表。
  当 q=1 endpoint 为 G 时，X 的每个因子都可如此处理；完整载体 X 在低区间
  3<=R<=p-2 内唯一对应 R_X=16t+3、K_X=(6t+1)(16t+1)，并有 gcd(X,K_X)=X。
  该 root chart 的 universal anchor 强制完整外部 bundle M=16t+2：t 为奇数时
  它给出 R_M=20t+3<p 的 strict marked absorb；t 为偶数时它给出一个显式 overflow，
  再由 L=9t/2 给出 R_L=6t-1<p 的 fixed-n 严格 identity-lift edge。结果给出
  q=1 source 的完整算术 carrier map 和 root 后首个局部 dispatch；它不构造 Type II
  raw state 到 fresh Type I root 的 E1 语义，也不证明全局 phase scheduler、后续
  Type I selector 或 Erdos--Straus 猜想。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - G-state
  - type-I
  - carrier-transfer
  - carrier-rail
  - root-entry
  - complete-excess
  - fixed-n
  - identity-lift
  - well-founded-potential
  - proof-boundary
sources:
  - claim: type-II-relation-reach-gcd-shadow-endpoint-descent
    role: q-one-G-endpoint-and-ordinary-Sol-p-state-semantics
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: low-chart-universal-source-and-anchor-receipt
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: complete-excess-bundle-dispatch
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: initial-A-equals-one-overflow-fixed-n-edge
  - concept: denominator-escape-state-contract
    role: fresh-root-and-E1-to-E5-boundary
  - reproduction: reproductions/type_ii_q_one_type_i_carrier_rail_dispatch.py
    role: carrier-rail-and-parity-dispatch-controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 源到低 Type I 图表的精确载体 rail 与首个分派

## 1. 跨图表载体恒等式

固定核心素数

\[
p=24t+1,
\qquad
X=\frac{p+3}{4}=6t+1.
\tag{1}
\]

考虑任意正的合法 Type I 图表

\[
4K=pR+1.
\tag{2}
\]

由于 (p\equiv1\pmod4)，(2) 自动强制 (R\equiv3\pmod4)。又

\[
4K=(4X-3)R+1=4XR-(3R-1).
\tag{3}
\]

(X) 为奇数，所以乘以 (4) 不改变与 (X) 的最大公因子。由 (3) 得到完整的、逐素数幂的
carrier transfer law：

\[
\boxed{
\gcd(X,K)=\gcd(X,3R-1).
}
\tag{4}
\]

特别地，对每个 (J\mid X)，

\[
\boxed{
J\mid K
\Longleftrightarrow
3R\equiv1\pmod J.
}
\tag{5}
\]

这不是只记录素数支撑：若 (\ell^e\Vert X)，则 (4) 精确记录

\[
\min\{e,v_\ell(K)\}
=\min\{e,v_\ell(3R-1)\}.
\tag{6}
\]

因此 q=1 Type II source 与 Type I chart 的兼容性完全由一个仿射余数决定，而不是由
事后把 Type II 的素因子重命名为 Type I support 决定。

## 2. q=1 G 的完整载体 rail

先取一个 (J\mid X) 且 (J\equiv1\pmod3)。q=1 endpoint 为 G 时，(X) 的全部素因子都
是 (1\pmod3)，所以每个 (J\mid X) 都满足这个前提。定义

\[
R_{J,z}=\frac{8J+1}{3}+4Jz,
\qquad z\ge0,
\tag{7}
\]

并令

\[
K_{J,z}=\frac{pR_{J,z}+1}{4}.
\tag{8}
\]

记 (Y=X/J)。

**定理（精确 carrier rail）。** (7)--(8) 恰好给出所有满足 (J\mid K) 的正合法
Type I 图表，且

\[
\boxed{
K_{J,z}=J\bigl(YR_{J,z}-(2+3z)\bigr),
\qquad
\gcd(X,K_{J,z})=J\gcd(Y,2+3z).
}
\tag{9}
\]

**证明。** 因为 (J\equiv1\pmod3)，((8J+1)/3) 是整数。并且

\[
3\frac{8J+1}{3}=8J+1\equiv1\pmod J,
\qquad
\frac{8J+1}{3}\equiv3\pmod4.
\tag{10}
\]

所以 (R_{J,z}) 是 (R\equiv3\pmod4) 且满足 (5) 的解。反之，(5) 与
(R\equiv3\pmod4) 的 CRT 解唯一模 (4J)；它正是 (7)。若 (z=-1)，则

\[
R_{J,-1}=\frac{1-4J}{3}<0,
\tag{11}
\]

故每个正解恰有 (z\ge0)。

再由 (3) 和

\[
3R_{J,z}-1=4J(2+3z),
\tag{12}
\]

可得

\[
K_{J,z}=XR_{J,z}-J(2+3z)
=J\bigl(YR_{J,z}-(2+3z)\bigr).
\tag{13}
\]

于是

\[
\gcd(X,K_{J,z})
=J\gcd\bigl(Y,YR_{J,z}-(2+3z)\bigr)
=J\gcd(Y,2+3z),
\tag{14}
\]

即 (9)。证毕。

因为 (X) 与 (J) 都是奇数，(Y) 也是奇数。因此 rail 的首点有

\[
\boxed{
\gcd(X,K_{J,0})=J.
}
\tag{15}

换言之，每个 q=1 G source carrier (J) 都有一个**唯一最小**的合法 Type I chart，
在那里它被完整保留而不混入其它 (X)-carrier。式 (14) 还给出所有额外层如何进入：
它们恰是 (Y) 与 (2+3z) 的交集。

## 3. 唯一的低 full-carrier chart

令 (J=X)。式 (7)--(9) 化为

\[
\boxed{
R_X=\frac{8X+1}{3}=16t+3,
\qquad
K_X=X(R_X-2)=(6t+1)(16t+1).
}
\tag{16}

显然

\[
\gcd(X,K_X)=X.
\tag{17}

由于任一核心素数都有 (t\ge3)，

\[
3\le R_X=16t+3\le24t-1=p-2.
\tag{18}

所以 (16) 落在现有 `universal_raw_default_entry_v1` 的低图表定义域内。

更强地，它是该定义域中唯一携带**全部** (X) 的 Type I chart。事实上，令 (J=X)，
则 (7) 的下一正解为

\[
R_X+4X=16t+3+24t+4=40t+7>p-2.
\tag{19}

因此

\[
\boxed{
3\le R\le p-2,
\quad X\mid K
\Longleftrightarrow
(R,K)=(R_X,K_X).
}
\tag{20}

这个唯一性也统一解释了此前的 (R=3) 伴随图表。取 (J=1) 时 (R_{1,0}=3)、
(K_{1,0}=(3p+1)/4)，而 (15) 只保留平凡 carrier；直接由 (4) 也有

\[
\gcd\left(X,\frac{3p+1}{4}\right)=\gcd(X,8)=1.
\tag{21}

所以 (R=3) 不是错误的 chart，而是 carrier rail 的最小、完全不保留 (X) 的端点。
与之相对，(16) 是同一 rail 的唯一低区间 full-carrier 端点。

## 4. full-carrier root 的强制首个 bundle

设一个将 (16) 预先声明为 `fresh_source_tree_only` root 的独立 policy 已经通过 E1
准入。这里只分析该 root **之后**的 Type I 算术；本节不把这个条件性假设伪装成
Type II--Type I verified edge。

令

\[
M=R_X-1=16t+2.
\tag{22}

由

\[
3M-8X=-2,
\qquad
\gcd(M,16t+1)=1,
\tag{23}

得到

\[
\gcd(M,K_X)=1.
\tag{24}

所以 universal source 到达 anchor (1,R_X-1) 后，其完整 external excess 没有选择：

\[
Q=M,
\qquad
\beta=1,
\qquad
A=1\longmapsto M.
\tag{25}

这里 (M<p)，且 (Q) 为 p-free。故 (25) 是一个可重放的 path-anchored complete-excess
bundle receipt，而不是由 factorization 偶然挑选的 block。

规范 target 由

\[
1\le R_M<4M,
\qquad
pR_M\equiv-1\pmod {4M}
\tag{26}

唯一确定；它按 (t) 的奇偶完全分派。

### 4.1 (t) 为奇数：直接进入严格 marked absorb

若 (t) 为奇数，则

\[
\boxed{
R_M=20t+3<p,
\qquad
K_M=(8t+1)(15t+1)=M\frac{15t+1}{2}.
}
\tag{27}

确有

\[
p(20t+3)+1=4M\frac{15t+1}{2}.
\tag{28}

因此，在 (16) 已被合法 root-entry 创建的条件下，(25)--(28) 正是已有
`marked_complete_excess_bundle_edge_v1` 的低图表分支。两端取
(W=\operatorname{Sol}(p))，恒等映射给出 E4，而

\[
\left\lfloor\frac{(p-1)^2/4}{M}\right\rfloor
<
\left\lfloor\frac{(p-1)^2/4}{1}\right\rfloor
\tag{29}

给出局部 E5。

### 4.2 (t) 为偶数：显式 overflow 后的固定-(n) 严格边

若 (t) 为偶数，则

\[
\boxed{
R_M=52t+7>p,
\qquad
K_M=(8t+1)(39t+2)=M\frac{39t+2}{2}.
}
\tag{30}

它的 bundle-overflow determinant 是

\[
\boxed{
n=4M-R_M=12t+1=\frac{p+1}{2},
\qquad
d=p-\frac{39t+2}{2}=\frac{9t}{2},
\qquad
pn=4Md+1.
}
\tag{31}

因为 (M<p) 且初始 charged support 为 (1)，固定 (n) 图谱的规范小载体就是
(L=d)。它给出

\[
\boxed{
R_d=4d-n=6t-1,
\qquad
K_d=d(p-M)=\frac{9t}{2}(8t-1),
\qquad
3\le R_d\le p-2.
}
\tag{32}

直接验算

\[
n<4d<p+n,
\qquad
pR_d+1=4K_d,
\qquad
d\mid K_d.
\tag{33}

故在同一个已验真的 root/bundle provenance 下，(32) 是现有
`overflow_determinant_charged_support_v1` 的完整 fixed-(n) identity-lift edge，
其 support 从 (1) 严格更新为 (d>1)。这不是“overflow 存在一个较小数”的非正式说法：
(31)--(33) 给出具体后继、全域恒等 lift 和已有 absorbed-support 势的严格支付。

## 5. 精确控制

下表只重算固定 q=1 G 核心素数的 carrier rail 与首个分派；它不作素数范围搜索。

| (p) | (t) | full chart ((R_X,K_X)) | 首个 bundle 后的 target |
|---:|---:|---|---|
| 73 | 3 | ((51,931)) | odd: ((R_M,K_M;M)=(63,1150;50)) |
| 241 | 10 | ((163,9821)) | even: overflow ((527,31752))，再到 ((R_d,K_d;d)=(59,3555;45)) |
| 2521 | 105 | ((1683,1060711)) | odd: ((2103,1325416;1682)) |
| 118801 | 4950 | ((79203,2352348901)) | even: overflow 后到 ((29699,882067725;22275)) |

此外，实际 q=1 G 控制 (p=76129)、(X=19033=7\cdot2719) 的 (J=7) rail 首点为

\[
R_{7,0}=19,
\qquad
K_{7,0}=361613,
\qquad
\gcd(19033,361613)=7.
\tag{34}

取 (z=1812=2(2719-1)/3) 恰回到 full chart

\[
R_{7,1812}=50755=R_X,
\qquad
\gcd(19033,K_{7,1812})=19033.
\tag{35}

这验证 (9) 对 partial carrier 与 full-carrier 汇合的精确解释。

## 6. 边界与下一接口

本卡解决的是此前 q=1 G handoff 的**算术 carrier compatibility**：完整 (X) 现在有唯一、
预先由 (p) 定义、位于低图表范围内的 target，而不是只能面对 canonical high root 的
support 互素障碍。它还把该 target 后的第一步压成 (27) 或 (30)--(33) 两个明确的、已有
Type I local contract。

但这仍不是 G/Type I 全局出口定理。尚未闭合的义务恰是：

1. 定义一个不能由 charged history 伪造的 `q_one_full_carrier_root_entry`，把实际 q=1
   Type II endpoint 与 (16) 的 `fresh_source_tree_only` root 以具名 E1 semantics 连接；
2. 为该 root 及 (27)/(32) 的所有 Type I F/G/hit 重分类接入 terminal-first dispatcher；
3. 把 q=1 endpoint phase 到 fresh Type I tree 的一次转换嵌入不可重入的全局良基 phase
   scheduler，并完成后续 Type I selector 的全称闭合。

所以 (16) 不是从目标反向补造的 raw parent，也不是把同一方程的常值映射当作递降。它给出
的是一个唯一的、完整 carrier-preserving root **候选**和其已确定的局部算术后续；在上述
root-policy 与 global scheduler 被真正证明前，不得把它登记为 verified Type II--Type I edge
或 Erdos--Straus 猜想的证明。
