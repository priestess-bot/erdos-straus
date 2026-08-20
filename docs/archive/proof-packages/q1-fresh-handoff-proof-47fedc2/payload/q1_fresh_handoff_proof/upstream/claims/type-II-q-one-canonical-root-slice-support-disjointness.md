---
kind: claim
claim_id: type-II-q-one-canonical-root-slice-support-disjointness
title: q=1 G 退出的规范根切片：严格 carry 与源支撑互素屏障
statement: >-
  令 p=24t+1 为核心素数，q=1 Type II 端点的首分母为 X=(p+3)/4=6t+1。
  在 a=1,d=1 根接口预先固定 r=t，则根容量 u=gcd(2t+1,(p^2+p+1)/3)
  精确属于 {1,37}，actual endpoint h=3u 永不为 bottom，且其 maximal
  complete-excess receipt 总是 p-free strict carry。u=1 时 c=37 仅发生于
  p=73；其余 c 精确属于 {2,10,22,110}。u=37 时 h=111，p>111^2 由小 endpoint
  定理严格；p<=111^2 的唯一核心素数为 433,1321,7537，直接 receipt 分别给
  c=248,1225,1850。另一方面 gcd(X,K)=1，其中 K=A(p-1) 是该规范根的完整支撑。
  所以 q=1 Type II G endpoint 的当前物理 source primes（均来自 X）不能被直接继承为这个根的
  support；该 root slice 精确支付 strict support-rebase 的 E2 和条件 E5，却不能单独
  支付跨 Type II--Type I 的 E1。任何全局 handoff 必须提供具名 fresh root-entry、
  terminal-first 与 typed reclassification，而不能把这条预定义算术切片误记为 verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
  - type-I-root-capacity-strict-carry-support-rebase
  - type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - G-state
  - type-I
  - root-capacity
  - strict-carry
  - complete-excess
  - support-disjointness
  - source-provenance
  - E1-E5
  - proof-boundary
sources:
  - claim: type-II-relation-reach-gcd-shadow-endpoint-descent
    role: q-one G endpoint and Type II phase exit
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: root capacity and h=3 exact receipt
  - claim: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
    role: small endpoint terminal-or-strict theorem
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: strict support target and potential
  - claim: type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
    role: raw reachability versus E1 distinction
  - reproduction: reproductions/type_ii_q_one_canonical_root_slice.py
    role: fixed cofactor controls and finite u-equals-37 catalog
visibility: public
last_checked: '2026-08-15'
---

# q=1 G 退出的规范根切片：严格 carry 与源支撑互素屏障

## 1. 从 q=1 状态固定根参数

令

\[
p=24t+1,
\qquad
X=\frac{p+3}{4}=6t+1.
\tag{1}
\]

这里 (X) 正是 (q=1)、gap (3) 的 Type II endpoint 首分母。该 endpoint 为
G 时，(X) 的每个素因子都为 (1\pmod3)；无论 F/G 分类如何，Type II 的物理
source support 都来自 (X) 的素因子。

考虑 (a=1,d=1) 根接口，但不再任选参数，而是预先声明

\[
r=t.
\tag{2}
\]

其余根量为

\[
g=\frac{p+1}{2},\qquad T=p^2t-g,\qquad A=gT,
\]

\[
K=A(p-1),\qquad
R=2p^3t-p^2-2pt-p+1,
\tag{3}
\]

并令

\[
M=\frac{p^2+p+1}{3},\qquad
u=(2t+1,M),\qquad h=3u.
\tag{4}
\]

这个选择只读取 Type II q=1 state 已有的根素数 (p)，不从 root endpoint 的目标
cofactor 或 complete-excess receipt 反推 (r)。它因此消除了根参数的任意性；以下先
证明它产生的算术出口，再精确说明为什么这还不是 E1 handoff。

## 2. 根容量只剩两个值

由 (p=24t+1)，有

\[
M=192t^2+24t+1.
\tag{5}
\]

写 (s=2t+1)。直接代入 (t=(s-1)/2) 得

\[
M=48s^2-84s+37.
\tag{6}
\]

故

\[
\boxed{u=(s,M)=(s,37)\in\{1,37\}.}
\tag{7}

在核心域 (t\ge3)，所以 (u<M)，是 proper-root。若 (u=37)，则

\[
2t+1=37k,\qquad k\text{ 为奇数},\qquad p=444k-11,
\tag{8}

\]

因而最小该分支为 (p=433)，始终 (h=111<p)。根容量公式给出一条 actual
capacity path

\[
(R-(p+1),K)=3u=h
\tag{9}

\]

到 primitive endpoint ((h,R-h))。

## 3. 该 endpoint 从不 bottom，且总是严格

令 (z=R-h)。由 (pz=4K-(ph+1))，

\[
(z,K)\mid ph+1.
\tag{10}

\]

另一方面 (t\ge3)、(p\ge73)、(h\le111) 给出

\[
z-(ph+1)
\ge 6p^3-p^2-7p-111(p+1)>0.
\tag{11}

\]

所以 (z\nmid K)，不存在这个 endpoint 的 bottom Type I terminal。又
(3\le h<p) 且 (R\equiv1\pmod p)，所以 (p\nmid z)。于是 (z) 的
maximal complete-excess receipt

\[
z=Q\beta,\qquad g_A=(A,Q),\qquad E=Q/g_A,\qquad D=\beta g_A
\tag{12}

\]

自动是 (p)-free，且 (hD\mid K)。

若 (u=1)，(h=3)，小 endpoint 定理立即排除 stutter。更精确地，令

\[
H=\frac{3p+1}{4}=18t+1,
\qquad
w=(t-3,H)=(t-3,55).
\tag{13}

\]

既有 (h=3) receipt 公式给出

\[
E=\frac{(R-3)/4}{w},\qquad D=4w,
\qquad c=\langle-E^{-1}\rangle_p.
\tag{14}

\]

当 (p=73,t=3) 时 (w=H=55)，故 (c=37)。其余核心素数有 (t>3)、
(w<H)；又 (w\mid55)，于是

\[
\boxed{c=2w\in\{2,10,22,110\}.}
\tag{15}

\]

若 (u=37)，则 (h=111)。当 (p>111^2) 时，小 endpoint 定理直接给出 strict
carry。剩余的有限支由 (8) 给出 (k\le27)。奇 (k) 的完整因子表是

| (k) | (444k-11) 的分解 |
|---:|---|
| 1 | (433) |
| 3 | (1321) |
| 5 | (47^2) |
| 7 | (19\cdot163) |
| 9 | (5\cdot797) |
| 11 | (11\cdot443) |
| 13 | (7\cdot823) |
| 15 | (61\cdot109) |
| 17 | (7537) |
| 19 | (5^2\cdot337) |
| 21 | (67\cdot139) |
| 23 | (101^2) |
| 25 | (13\cdot853) |
| 27 | (7\cdot29\cdot59) |

所以仅需重算三张 actual receipt：

| (p) | (D) | (c) |
|---:|---:|---:|
| 433 | 1 | 248 |
| 1321 | 8 | 1225 |
| 7537 | 1 | 1850 |

三者都严格小于 (p-1)。因此对每个核心素数，(2) 的 proper-root endpoint 都给出
strict carry，且该 carry 的 support rebase 是

\[
M_{\rm ex}=\operatorname{lcm}(A,Q)=AE,
\qquad
\Lambda_p^\sharp:(0,p-1)\longmapsto(0,c).
\tag{16}

\]

这支付 strict support-rebase 的算术 E2，以及在 root state 已 persistent 时的 E5。

## 4. q=1 source support 与根支撑严格互素

这个自然 root slice 同时暴露了目前不能跳过的 E1 障碍。由 (1)，

\[
g=12t+1=2X-1,
\qquad
p-1=24t=4(X-1).
\tag{17}

\]

所以 ((X,g)=(X,p-1)=1)。又 (p\equiv-3\pmod X)，故

\[
2T=2p^2t-(p+1)
\equiv18t+2=3X-1\equiv-1\pmod X.
\tag{18}

\]

因为 (X) 为奇数，(18) 给出 ((X,T)=1)。结合 (3)，得到

\[
\boxed{(X,K)=(X,A(p-1))=1.}
\tag{19}

\]

因此 q=1 Type II endpoint state 的当前实际 source carrier（其素因子均来自 (X)）都不能
被保留为这个 root chart 的 charged support。这个结论并不说不存在某种跨图表动作；它
精确排除的是把 q=1 source factorization 直接重命名为 root-path provenance 的做法。

所以 (2) 是一个强的、预定义的**算术 selector**，但尚不是合法的 Type II G 到 Type I
递归边。要把它接入全局出口，还必须由一个具名的 `fresh_source_tree_only` root-entry
回执独立支付：

1. 新 root source 的 target-independent origin 和连续 scope；
2. root chart 前的 terminal-first miss；
3. root source、endpoint 与 support-rebase target 的 typed F/G/hit 重分类及内容寻址；
4. 与 Type II phase 不可重入相容的外层 phase rank。

在这些字段落地前，本卡只能把 strict arithmetic 记为 `analysis_evidence` 的可用 payload，
不能将 (q=1) G 出口或 Erdős--Straus 猜想标为闭合。

## 5. 聚焦复现

```bash
python3 reproductions/type_ii_q_one_canonical_root_slice.py --verify
```

验证器只重算五个 (u=1) cofactor、三个有限 (u=37) receipt、一个高于
(111^2) 的 (u=37) 控制，以及 (19)。它不扫描素数范围、分母范围或 selector history。
