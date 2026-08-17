---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-marker-affine-lift-source-allocation
title: q=1 容量八 marker 的奇参数排除与仿射 source 因子分配
statement: >-
  在真实 q_star=103 的 c=8 double-low marker
  (D,c,c_Sigma,epsilon,g_b)=(1,1,4,0,47) 中，令
  n=(p^2+p-1-q)/47。则 gcd(n,M/47)=1，且存在唯一整数 rho 满足
  32n=1+p rho；并有 q=p^2+p-1-47n、lambda=32p+32-47rho、
  p lambda=32q+79。实际高 raw prime 必使 s 为奇数；否则 n 奇且 q 偶，矛盾。
  因而 n=0 (mod 16)、p=49 (mod 96)、q=1 (mod 16)、p rho=-1 (mod 512)，并且
  n=1、rho=1、q=lambda=2 (mod 3)。更细地，rho=175 (mod 192) 当 s=1 (mod 4)，
  rho=79 (mod 192) 当 s=3 (mod 4)。令 A=1+p rho、L=176s+5、
  E=3168s^2+24s-1、H=rho^2-18rho-11。将 M 的唯一一个 47 从 s 或 L 中移除后，
  marker 强制 gcd(S_odd,rho+1)=gcd(L_0,4rho-11)=gcd(E,A)=1，且
  gcd(E,H)=gcd(E,rho-11p)。故 marker 不再是自由的 quartic ray：它落在两条
  parity-refined affine rho 射线，并把三个 source 因子分别分配到三个显式小多项式。
  本结论排除全部 even-s marker，但不构造 actual marker、短证书或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - q-star-103
  - marker
  - affine-lift
  - source-allocation
  - parity-exclusion
  - capacity-map
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
    role: unique-marker-data
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
    role: exact-g-b-formula-and-split-interface
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
    role: c-one-direct-lift
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: source-normal-form-and-V-mod-three
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_marker_affine_lift_allocation.py
    role: exact-lift-parity-and-source-allocation-identities
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 marker 的奇参数排除与仿射 source 因子分配

## 1. 输入与仿射 lift

保留唯一 zero-carry marker

\[
(D,c,C,\epsilon,g_b)=(1,1,4,0,47)
\tag{1}
\]

及容量八 source

\[
p=48s+1,
\qquad M=9sLE,
\qquad L=176s+5,
\qquad E=3168s^2+24s-1.
\tag{2}
\]

已有互补支撑公式和 (c=1,D=1) direct low-gate 式分别为

\[
g_b=(M,p^2+p-1-q),
\qquad p\lambda=32q+79.
\tag{3}
\]

令

\[
N=p^2+p-1-q.
\tag{4}
\]

由 (g_b=47) 得到唯一整数 (n)：

\[
N=47n,
\qquad \boxed{(n,M/47)=1.}
\tag{5}
\]

将 (q=p^2+p-1-47n) 代回 (3)，有

\[
p\lambda=32p^2+32p+47-1504n.
\tag{6}
\]

这里 (p>47)，故 (p\mid(32n-1))。定义

\[
\boxed{\rho:=\frac{32n-1}{p}\in\mathbb Z.}
\tag{7}
\]

于是 marker 的整数层等价改写为

\[
\boxed{
32n=1+p\rho,
\quad
q=p^2+p-1-47n,
\quad
\lambda=32p+32-47\rho.}
\tag{8}
\]

反向地，若 (47\mid M)、(p\rho\equiv-1\pmod {32})，并由 (8) 定义
(n,q,\lambda)，则 (5) 恰好等价于 (g_b=47)。所以这不是放松：它是对 marker
gcd 条件的精确重参数化。

## 2. even (s) 的严格排除

(L,E) 都是奇数，因此 (s) 偶时 (M/47) 仍为偶数。由 (5)，此时 (n) 必为奇数。
但 (p) 是奇数，故

\[
p^2+p-1\equiv1\pmod2,
\qquad
q\equiv1-n\equiv0\pmod2.
\tag{9}
\]

实际 raw label (q>2(p-1)>2) 是奇素数，矛盾。因此

\[
\boxed{s\ \text{必为奇数}.}
\tag{10}
\]

反过来，实际 (q) 为奇数时，(4)--(5) 给 (n) 为偶数。于是 (7) 加强为

\[
p\rho\equiv-1\pmod {64}.
\tag{11}
\]

因为 (s) 奇，

\[
\boxed{p\equiv49\pmod {96}.}
\tag{12}
\]

这已经消除了 marker 的全部 even-(s) 半支，而不是一个有限参数观察。

## 3. 固定的模 3 与 parity-refined 射线

(9\mid M/47)，所以 (3\nmid n)。另一方面 (p\equiv1\pmod3)，
(47\equiv2\pmod3)，且 source 恒有 (V\equiv2\pmod3)，故实际 (q\mid V)
不等于 (3)。由 (8)，

\[
q\equiv1-2n\pmod3.
\tag{13}
\]

(n\not\equiv0\pmod3) 且 (q\not\equiv0\pmod3) 强制

\[
\boxed{n\equiv1\pmod3.}
\tag{14}
\]

再用 (1+p\rho=32n)，得到

\[
\boxed{\rho\equiv1,
\qquad q\equiv2,
\qquad\lambda\equiv2\pmod3.}
\tag{15}
\]

将 (11) 与 (15) 合并。若 (s\equiv1\pmod4)，则 (p\equiv49\pmod {64})；若
(s\equiv3\pmod4)，则 (p\equiv17\pmod {64})。因此

\[
\boxed{
\rho\equiv
\begin{cases}
175\pmod {192},&s\equiv1\pmod4,\\
79\pmod {192},&s\equiv3\pmod4.
\end{cases}}
\tag{16}
\]

这两条是 actual marker 的全部 parity-refined affine carry 射线。

还可用 marker 自带的 \(\epsilon=0\) 再作一次严格的二进收缩。由 (10)，
\(M\) 为奇数；而 \(R\)、\(V\)、\(q\)、\(a=V/q\) 都是奇数，所以
\(b=R-a\) 为偶数。定义 \(\epsilon\) 的规则此时排除
\(v_2(b)=1,2,3\)，故

\[
16\mid b.
\tag{17}
\]

又 \(p\equiv1\pmod {16}\)、\(pR+1=32M\) 和
\(V=R(p-1)-p\) 分别给 \(R\equiv V\equiv15\pmod {16}\)。由 (17) 得
\(a\equiv15\pmod {16}\)，再由 \(qa=V\) 得

\[
q\equiv1\pmod {16}.
\tag{18}
\]

式 (8) 因而强制 \(n\equiv0\pmod {16}\)，并将 (11) 加强为

\[
\boxed{p\rho\equiv-1\pmod {512}.}
\tag{19}
\]

所以 (16) 只是更强条件 \(\rho\equiv-p^{-1}\pmod {512}\)、
\(\rho\equiv1\pmod3\) 的模 \(192\) 投影；对每个固定的 \(s\pmod {32}\)，它实际上
给出唯一的 \(\rho\pmod {1536}\) 类。

## 4. 三个 source 因子的显式分配

写

\[
A:=1+p\rho=32n,
\qquad H:=\rho^2-18\rho-11.
\tag{20}
\]

source 正规形给出三条精确恒等式：

\[
\begin{aligned}
A-\rho(p-1)&=1+\rho,\\
3L&=11p+4,\\
\rho(11p+4)-11A&=4\rho-11,\\
8E&=11p^2-18p-1,\\
pH-A(\rho-11p)&=8E\rho.
\end{aligned}
\tag{21}
\]

已知 (47\mid M) 当且仅当 (47\mid s) 或 (47\mid L)，且两者不同时发生。
从命中因子中只除去一个 (47)：

\[
S:=s/47^{[47\mid s]},
\qquad L_0:=L/47^{[47\mid L]},
\qquad S_{\rm odd}:=S/2^{v_2(S)}.
\tag{22}
\]

那么 (S_{\rm odd},L_0,E\mid M/47)。由 (5)、(20)--(21)，得到不是启发式而是
逐因子强制的分配：

\[
\boxed{
(S_{\rm odd},1+\rho)=1,
\qquad
(L_0,4\rho-11)=1,
\qquad
(E,A)=1.}
\tag{23}
\]

最后一条恒等式还精确区分 (E) 的另一条二次根支。因为 ((p,E)=1)，而
(A) 在 (E) 上是单位，(21) 给出

\[
\boxed{(E,H)=(E,\rho-11p).}
\tag{24}
\]

所以 (E) 与 (H) 的任何重叠不再能被误读为 (A=1+p\rho) 的 marker 共享因子；它
必须全部走明确的 alternate branch \(\rho\equiv11p\) 。

## 5. 作用范围

本引理给出一个严格排除和一个可继续推进的因子图：actual marker 不可能有 even (s)，并且
剩余候选被压到模 \(1536\) 的仿射 \(\rho\) 射线及 (23)--(24) 的 source 分配。它尚未证明

- (q\mid V) 与这些射线没有交；
- 任一剩余射线产生 Type I/II 短证书；
- 或 source/path、typed guards 和 E1--E5 可升级为 (n<p) 的递降。

下一步必须把 (q\mid V) 的四次因子条件同 (23)--(24) 的分配联立；只重复局部
(q,\lambda) 同余无法再缩小实际 marker。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_marker_affine_lift_allocation.py --verify
~~~

复现器只检查有限的 parity 表、三条多项式恒等式和两个明确标为 formal 的算术控制；不搜索
source、素数、(V) 因子或 terminal。
