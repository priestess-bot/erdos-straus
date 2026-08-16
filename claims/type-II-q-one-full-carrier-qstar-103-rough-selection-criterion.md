---
kind: claim
claim_id: type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
title: q=1 full-carrier 偶宏的 q-star=103 rough 选择判据
statement: >-
  在 ordinary q=1 full-carrier 的 even t=2s 第二-anchor 固定-n 宏中，若该宏已合法执行，
  则 selected q_star 等于 103 当且仅当 103 divides (6s-1)、25 does not divide
  (6s-1)，且每个素数 ell 满足 7<=ell<103 时 ell does not divide (6s-1)。
  因而 s=86 (mod 103) 只是 q_star=103 的必要同余条件，而非充分条件；真实的 103 域
  还要求 (6s-1) 在除至多一个 5 因子后没有小于 103 的素因子。该筛不构造 terminal 或
  recursive edge，但给出零 k c=8/56 103 相位的精确宏选择域。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
topics:
  - type-II
  - q-one
  - full-carrier
  - q-star
  - roughness
  - complete-excess
  - c-eight
  - c-fifty-six
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-second-anchor-fixed-n-macro
    role: actual-minimum-excess-prime-selection-rule
  - claim: type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
    role: q-star-103-capacity-phase-interpretation
  - reproduction: reproductions/type_ii_q_one_full_carrier_qstar_103_rough_selection_criterion.py
    role: exact-small-prime-sieve-and-three-fixed-macro-controls
visibility: public
last_checked: '2026-08-17'
---

# q=1 full-carrier 偶宏的 \(q_\star=103\) rough 选择判据

## 1. 选择发生在第一 anchor，而非只在同余层

令 \(t=2s\)。在 even second-anchor fixed-\(n\) macro 的实际第一 child 上，

\[
R_0=12s-1,
\qquad
K_0=9s(16s-1),
\qquad
A_0=9s.
\tag{1}
\]

universal \(p\)-source 到达的 anchor 是

\[
R_0-1=2(6s-1).
\tag{2}
\]

宏只在 (2) 的 complete-excess blocks 中，选取同时整除 \(6s-1\) 的最小素数：

\[
q_\star
=\min\{q:q\text{ 是 (2) 相对 }K_0\text{ 的 excess prime，且 }q\mid6s-1\}.
\tag{3}
\]

所以 \(q_\star\) 不仅由 \(s\bmod q\) 决定；还必须检查较小的 \(q\) 是否实际为
anchor 的 excess prime。

## 2. 除五以外的素因子全部是 excess

令

\[
N=6s-1,
\qquad
B=16s-1.
\tag{4}
\]

有

\[
(N,s)=1,
\qquad
8N-3B=-5.
\tag{5}
\]

故

\[
(N,B)\mid10.
\tag{6}
\]

若 \(q\ge7\) 是 \(N\) 的素因子，则由 (5)--(6)

\[
q\nmid9sB=K_0.
\tag{7}
\]

因此 \(N\) 中每个 \(q\ge7\) 的完整素数幂都严格超过 \(K_0\) 的容量，必出现在
complete-excess block 列表中。

唯一需要单独处理的是 \(q=5\)。若 \(5\mid N\)，则 \(s\equiv1\pmod5\)，从而
\(5\mid B\)。若 \(v_5(N)=1\)，则 \(v_5(K_0)\ge1\)，故 \(5\) 不 excess。若
\(v_5(N)\ge2\)，则 (5) 强制

\[
v_5(B)=1,
\tag{8}
\]

而 \(5\nmid s\)，所以 \(5\) 严格 excess。换言之，

\[
\boxed{5\text{ 是 (3) 的候选}\Longleftrightarrow25\mid N.}
\tag{9}
\]

素数 \(2\) 不整除 \(N\)，而 \(3\) 也不整除 \(N\)。

## 3. 精确 103 判据

由第 2 节，103 自身只要整除 \(N\) 就一定是 eligible excess prime；它成为 (3) 的
最小值，当且仅当所有更小候选都不存在。因此

\[
\boxed{
\begin{aligned}
q_\star=103
\quad\Longleftrightarrow\quad&
103\mid(6s-1),\\
&25\nmid(6s-1),\\
&\ell\nmid(6s-1)
\quad\text{for every prime }7\le\ell<103.
\end{aligned}}
\tag{10}
\]

第一行等价于

\[
s\equiv86\pmod{103},
\tag{11}
\]

但 (11) 本身遗漏了 (10) 的后两行。故零 \(k\) 分类中记录的 103 同余相位是
必要的 capacity phase，不是整个实际 macro selection domain 的同义改写。

## 4. 三个固定控制

\[
\begin{array}{c|c|c|c}
p&s&6s-1&\text{actual }q_\star\\
\hline
4129&86&5\cdot103&103\\
157393&3279&103\cdot191&103\\
340321&7090&7\cdot6077&7
\end{array}
\tag{12}
\]

第三行满足 \(s\equiv86\pmod{103}\)，但因 \(7\mid6s-1\) 而不能进入
\(q_\star=103\) phase。这是反对“同余充分”的严格控制，不是 terminal 或猜想反例。

## 5. 作用域

式 (10) 为 c=8 与 c=56 的 q-star=103 研究提供了真实入口筛。它没有证明这些
rough parameters 一定给出核心素数、terminal-first miss、persistent receiver 或
G/Type I global exit；这些条件仍必须在各自的状态合同中独立验证。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_qstar_103_rough_selection_criterion.py --verify
~~~

复现器只重放 (5)、(9)--(12) 及三个固定、已知 core-macro 控制；不扫描参数或重跑
历史范围。
