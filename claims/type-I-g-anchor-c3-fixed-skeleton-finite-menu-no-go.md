---
kind: claim
claim_id: type-I-g-anchor-c3-fixed-skeleton-finite-menu-no-go
title: c=3 双中间固定 skeleton 有限菜单不完备性
statement: 任取有限多个固定 (a,b) 双中间 skeleton，即使每个 skeleton 允许 alpha、beta、gamma 复合并按素因子块 raw peeling，也不能覆盖全部 c=3 核心素数。每个可行固定 skeleton 的基础 CRT 解类都不是零类；取 h=39Lt（L 为这些 CRT 周期的最小公倍数）便同时回避所有 skeleton，且 p=936Lt+1 由 Dirichlet 定理在无穷多个 t 上为核心素数。该 no-go 不排除 a,b 随 h 自适应，也不排除其他 raw path 形状。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-two-intermediate-target-source-template
  - type-I-g-anchor-c3-factor-block-raw-source-receipts
topics:
  - type-I
  - c3
  - CRT
  - finite-menu
  - no-go
  - adaptive-skeleton
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-two-intermediate-target-source-template
    role: fixed-skeleton-integrality-system
  - claim: type-I-g-anchor-c3-factor-block-raw-source-receipts
    role: composite-block-generalization
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 双中间固定 skeleton 有限菜单不完备性

## 1. 一个固定 skeleton 的 CRT 类

固定正整数 \(a,b\)，其中 \(a\equiv7\pmod8\)。双中间 skeleton 的整数性和
\(\gamma\) 奇偶要求是

\[
104h\equiv10\pmod b,
\qquad
104h\equiv9+b\pmod a,
\qquad
h\equiv\frac{a+9}{8}+1\pmod2.
\tag{1}
\]

令

\[
g_b=(104,b),
\qquad
g_a=(104,a),
\qquad
\ell_{a,b}=\operatorname{lcm}\left(2,\frac b{g_b},\frac a{g_a}\right).
\tag{2}
\]

前两条单独可解当且仅当

\[
g_b\mid10,
\qquad
g_a\mid(9+b).
\tag{3}
\]

若完整系统 (1) 在公共 gcd 上相容，它的解集就是一个唯一的

\[
h\equiv r_{a,b}\pmod{\ell_{a,b}}.
\tag{4}
\]

## 2. 零类不可能出现

**引理。** 任意满足 (1) 的固定 skeleton 都有

\[
r_{a,b}\not\equiv0\pmod{\ell_{a,b}}.
\tag{5}
\]

**证明。** 假设反之，\(h=0\) 满足 (1)。前两条给出

\[
b\mid10,
\qquad
a\mid b+9.
\tag{6}
\]

写 \(a=8k+7\)。第三条给出

\[
0\equiv k+3\pmod2,
\tag{7}
\]

所以 \(k\) 为奇数，亦即

\[
a\equiv15\pmod{16}.
\tag{8}
\]

由 \(b\mid10\)，有 \(b\in\{1,2,5,10\}\)，从而

\[
b+9\in\{10,11,14,19\}.
\tag{9}
\]

没有正的 \(15\pmod{16}\) 整数能整除 (9) 中任一数，这与 (6) 矛盾。证毕。

## 3. 有限菜单 no-go

**定理。** 设 \(\mathcal F\) 是任意有限个兼容的固定 \((a,b)\) skeleton。令

\[
L=\operatorname{lcm}_{(a,b)\in\mathcal F}\ell_{a,b}.
\tag{10}
\]

则有无穷多个 \(c=3\) 核心素数不满足 \(\mathcal F\) 中任何一个 skeleton 的基础
整除条件。

**证明。** 令

\[
h=39Lt,
\qquad
t\ge1.
\tag{11}
\]

对每个 \((a,b)\in\mathcal F\)，有 \(h\equiv0\pmod{\ell_{a,b}}\)，而由 (5) 这不可能
等于其唯一允许类 (4)，所以全部 skeleton 都被回避。另一方面，

\[
h\equiv0\pmod3,
\qquad
h\equiv0\pmod{13},
\tag{12}
\]

故仍在 \(c=3\) 分支，且

\[
K=(26h+1)(24h-2)\equiv-2\pmod{13},
\tag{13}
\]

保持 \(13\)-tail 容量。相应核心数为

\[
p=24h+1=936Lt+1.
\tag{14}
\]

由于 \((1,936L)=1\)，Dirichlet 定理给出无穷多个使 (14) 为素数的 \(t\)。证毕。

## 4. 含义

本定理甚至不需要考察标签是否为素数、是否可拆为复合因子块、或每块的容量 reserve；
它在 skeleton 的基础 CRT 层就排除了有限菜单的全覆盖。因此下一阶段应研究
\(a,b\) 随 \(h\) 变化的自适应构造，或完全不同的 terminal/descent 形状，而不是继续
增加有限个固定 \((a,b)\) 条目。
