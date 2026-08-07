---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-d6303-complete-fiber-boundary
title: v=5 的 D=6303 完整 Type II 候选纤维边界
statement: 对 v=5 核心素数 p=1202376916441，固定 D=D*=6303=3*11*191、M=4D=25212。全部八个 A|D 都满足 D/A 平方自由和 4AD<p；其 N_A=p+4AD 的完整因子格给出 102 个带 A 标签的 M-单位除子记录（去标签后为 94 个整数），但没有 h=-1 (mod M)，故这个完整参数格不产生 Type II target factor。另一方面，A=2101 的 J0=13 与 A=573 的 J1=53^2 各自整除本行 N_A，且 gcd(N_2101,N_573)=gcd(J0,J1)=1；在 chi(x)=x^10 (mod 191) 下它们分别匹配 v=5 signed marks mu0、mu1。全格的 q=19-active 记录恰为 A=3,573；A=3 不含 phase 16 或 8 的因子，而若另要求 cofactor h 本身有正 q=19 高度，则 phase 16 无命中、phase 8 仅有 (A,h)=(573,3696697)。因此固定 D=6303 给出 target-odd no-go 和有限 candidate-cofactor boundary；它不构成 raw-to-fiber adapter、physical source、capacity 或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-g-anchor-c3-adaptive-core19-v5-q19-phase-compatible-candidate-fiber
  - type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid
  - type-II-source-fiber-shared-q-ledger
  - type-II-filtered-composition-source-slot-terminal
topics:
  - type-I
  - type-II
  - c3
  - core19
  - source-fiber
  - signed-mark
  - q-adic-height
  - q-primary
  - target-odd
  - finite-enumeration
  - no-go
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_d6303_fiber_catalog.py
    role: complete eight-fiber factor, character, q-height, and target-boundary verifier
visibility: public
last_checked: '2026-08-07'
---

# v=5 的 \(D=6303\) 完整 Type II 候选纤维边界

本卡把此前单个 \(A=573\) 候选扩展为固定 \(D=6303\) 的完整参数格。结果同时给出
一个可分离的 character-factor control 和两个严格 no-go；三者都不能被误报为完整
raw-to-fiber adapter。

## 1. 有限参数格

固定 v=5 的

\[
p=1202376916441,\qquad
D=D_*=6303=3\cdot11\cdot191,\qquad
M=4D=25212.
\tag{1}
\]

\(D\) 平方自由，所以所有

\[
\mathcal A=\{1,3,11,33,191,573,2101,6303\}
\tag{2}
\]

都满足 \(A\mid D\) 和 \(D/A\) 平方自由。并且

\[
4AD\le4D^2=158911236<p.
\tag{3}
\]

令 \(N_A=p+4AD\)。因为 \(M=4D\)，每一个 \(N_A\equiv p\equiv21733\pmod M\)，
故 \(N_A\) 及其所有因子均为 \(M\)-单位。

## 2. 全部八个纤维

\[
\begin{array}{c|c|c|c}
A&N_A\text{ 的完全素因式分解}&v_{19}(N_A)&\tau(N_A)\\ \hline
1&89\cdot107\cdot151\cdot836161&0&16\\
3&19\cdot45667\cdot1385749&1&8\\
11&7^2\cdot347\cdot70715591&0&12\\
33&1202377748437&0&2\\
191&67\cdot157\cdot114305707&0&8\\
573&17\cdot19^3\cdot53^2\cdot3671&3&48\\
2101&13\cdot92494606681&0&4\\
6303&809\cdot1486447253&0&4
\end{array}
\tag{4}
\]

表中原子因子均经确定性试除复核为素数。令

\[
\mathscr D=\{(A,h):A\mid D,\ h\mid N_A\},
\qquad
|\mathscr D|=16+8+12+2+8+48+4+4=102
\tag{5}
\]

这是带 \(A\) 标签的除子记录数；去掉标签后的整数并集有 \(94\) 个元素。重复只来自
\(1\) 在全部八行出现，以及 \(19\) 在 \(A=3,573\) 两行出现。

## 3. 固定参数格的 target-odd no-go

对每一行完整枚举 \(h\mid N_A\)，均有

\[
h\not\equiv-1\pmod {25212}.
\tag{6}
\]

下面给出比枚举更短的逐行障碍：

\[
\begin{array}{c|c}
A&\text{障碍}\\ \hline
1&h\bmod11\in\{1,7,8,9\}\\
3,33,191,2101&h\equiv1\pmod3\\
11&h\bmod11\in\{1,5,6,7,8,9\}\\
6303&h\equiv1\pmod4
\end{array}
\tag{7}
\]

剩余 \(A=573\) 行取

\[
\chi(x)=x^{10}\pmod {191}.
\tag{8}
\]

若 \(h\equiv-1\pmod M\)，则 \(\chi(h)=1\)。但在该行的 \(48\) 个因子中，phase
为 \(1\) 的只有

\[
1,\qquad53371=19\cdot53^2,\qquad
70237243=19^2\cdot53\cdot3671,
\tag{9}
\]

它们都为 \(1\pmod3\)。所以 (6) 对该行也成立。

由同纤维 target-factor 到 Type II 证书的既有回译，这精确排除
\(D=D_*=6303\)、\(A\in\mathcal A\) 的 target-factor mechanism；它不否定这个
\(p\) 已有的 \((m,d)=(3,11)\) 直接 terminal，也不外推到其它 \(D_*\)。

## 4. 分离的相位余因子与 q-active candidate-record 边界

令 \(\zeta=150\)，并记 v=5 signed marks 的 phase 为

\[
\eta_R(\mu_0)=\zeta^{16},\qquad
\eta_R(\mu_1)=\zeta^8.
\tag{10}
\]

一个可分离的 character-factor control 是

\[
\begin{array}{c|c|c|c}
A&J&J\mid N_A&\chi(J)\\ \hline
2101&13&\text{是}&\zeta^{16}\\
573&2809=53^2&\text{是}&\zeta^8.
\end{array}
\tag{11}
\]

这里严格有

\[
\gcd(N_{2101},N_{573})=\gcd(13,2809)=1,
\tag{12}
\]

且 \(2809\cdot19^j\mid N_{573}\) 对 \(0\le j\le3\) 成立。它给出相位因子在候选
记录内的分离 provenance；但仍没有 raw occurrence 到这些记录的 functor。

记录自身的 \(q=19\) 高度由

\[
N_A\equiv3-A\pmod {19}
\tag{13}
\]

确定：只有 \(A=3,573\) 是 \(q\)-active，且记录高度分别为 \(1,3\)。在 \(A=3\) 的
完整因子格中，phase \(16\) 和 \(8\) 都不存在；因此两个 signed phase 不能在两个不同
的 \(q\)-active \(A\)-标签中分别落地。这个结论只限制 candidate-record allocation，
不把 \(A\) 标签解释为 physical source。

进一步若合同要求 cofactor \(h\) 本身满足 \(v_{19}(h)>0\)，则全八行中 phase
\(16\) 完全没有这种因子；phase \(8\) 只有

\[
(A,h)=(573,3696697).
\tag{14}
\]

不附加这个正高度要求时，\(A=573\) 的 phase \(16\) 唯一因子为
\(53\cdot3671\)，phase \(8\) 的因子为

\[
53^2,\qquad19\cdot53\cdot3671,
\tag{15}
\]

其与 phase \(16\) 因子的 gcd 分别为 \(53\) 和 \(53\cdot3671\)。这是同一候选记录
内的次级 cofactor 重叠事实，不能提升为 raw-source 或 slot no-go。

[第三条 C=38 实际 raw 叶](type-I-g-anchor-c3-adaptive-core19-v5-c38-q19-phase-leaf.md)
提供了 \(\zeta^{11}=\chi(194563\cdot19^3)\) 的实际 raw mark。它是 \(A=573\) 内一个
精确的 selected cofactor correspondence，但在缺少 raw functor 时不唯一分配这个
occurrence；因此不改变本节的 candidate-record 条件。

## 5. 结论边界

本卡的正向部分只是候选记录内的 character cofactor correspondence；负向部分只覆盖
固定 \(D=6303\) 的八个 \(A\) 及上述 candidate-record/cofactor 条件。仍缺少完整 raw transition/source universe、
occurrence projection、逐项因子 provenance、prefix request/slot allocation、
target-odd carrier、demand-to-slot、E4/E5 和 terminal-first clearance。因此它不是
integer adapter、capacity 注入或 selector edge。
