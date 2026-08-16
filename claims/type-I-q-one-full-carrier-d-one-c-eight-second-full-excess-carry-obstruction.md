---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
title: q=1 零 k 容量八 target 的第二完整 excess 增容障碍
statement: >-
  设 ordinary q=1 G full-carrier 的 terminal-first 未命中 even fixed-n 宏在零 k 层给出
  c=8,j=11,g=1。实际 q_star=103 的 rough 选择条件与 gap-7 terminal-first
  剩余合用时，强制 s=86+103u、u=1,6 (mod 7)。其第一条 p-free complete-excess
  strict relay 的 target 可写为 K_0=8M、pR_0+1=4K_0，其中
  M=9s(176s+5)(3168s^2+24s-1)。该 target 的精确 complete-excess block 必为
  Q=(R_0-1)/2，且 (M,Q)=1；下一 canonical rechart 的 capacity c_1 满足
  75c_1=64 (mod p)，故 c_1>8。因而重复完整-excess bundle 必严格增大 capacity，
  不能提供该 c=8 target 的 E5 strict edge。结论只排除第二个全块 carry；不排除
  非完整 bundle、不同 raw source、其它 Type I terminal 或严格递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - gap-seven-congruence-certificates
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - full-carrier
  - d-one
  - c-eight
  - complete-excess
  - carry-obstruction
  - terminal-first
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
    role: c-eight-j-eleven-g-one-and-q-star-103-normal-form
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: first-complete-excess-strict-relay-and-target-contract
  - claim: type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
    role: actual-q-star-103-roughness-excludes-the-u-equals-five-mod-seven-residue
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: exact-carry-comparison-and-its-E5-meaning
  - claim: gap-seven-congruence-certificates
    role: terminal-first-mod-seven-residual-sieve
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction.py
    role: exact-normal-form-gcd-and-capacity-increase-receipt
visibility: public
last_checked: '2026-08-17'
---

# q=1 零 \(k\) 容量八 target 的第二完整 excess 增容障碍

## 1. terminal-first 后的精确残余

零 \(k\) 的 \(c=8\) 形状为

\[
(c,j,g)=(8,11,1),
\qquad
p=48s+1,
\qquad
q_\star=103,
\qquad
s\equiv86\pmod{103}.
\tag{1}
\]

写 \(s=86+103u\)。则

\[
p=4129+4944u\equiv6+2u\pmod7.
\tag{2}
\]

进入 \(q=1\) full-carrier root 以前已经执行 terminal-first。既有 gap-7 证书覆盖
\(p\equiv3,5,6\pmod7\)，而 \(p\equiv0\pmod7\) 不能是这里的核心素数。因此仅从
terminal-first 可得到 \(u\equiv1,5,6\pmod7\)。

这里的 \(q_\star=103\) 是实际 macro selection，不是只保留
\(s\equiv86\pmod {103}\) 的同余标签。其 rough 选择判据还给出

\[
7\nmid(6s-1).
\tag{3}
\]

另一方面，代入 \(s=86+103u\) 有

\[
6s-1=515+618u\equiv4+2u\pmod7.
\tag{4}
\]

故 \(u\not\equiv5\pmod7\)。与 terminal-first 的三类残余合并，实际 persistent 输入
只能满足

\[
p\equiv1,4\pmod7,
\qquad
\boxed{u\equiv1,6\pmod7}.
\tag{5}
\]

这一步只把 \(c=8\) 的算术宏相位压缩为 terminal-first 加 roughness 的残余；它没有
终止这两个相位。

## 2. 第一条 strict relay 的 \(c=8\) target

由 \(j=11\) 的 even-branch 闭式，

\[
n=\frac{11p+4-11}{4}=132s+1.
\tag{6}
\]

令

\[
X=24s+1,
\qquad
L=176s+5,
\qquad
E=(p-1)(66s+1)-X=3168s^2+24s-1.
\tag{7}
\]

第一条 p-free complete-excess relay 的 charged support 和 target 为

\[
\begin{aligned}
A&=\frac{pn-1}{4}=9sL,\\
M&=AE=9sLE,\\
K_0&=8M,\\
R_0&=\frac{32M-1}{p}
=3345408s^3+50688s^2-1392s-1.
\end{aligned}
\tag{8}
\]

于是 \(pR_0+1=4K_0\)、\(R_0\equiv3\pmod4\)。\(K_0/M=8\) 正是本卡要比较的
当前 capacity。

## 3. 第二完整 excess block 的刚性

先注意

\[
11X-4(66s+1)=7.
\tag{9}
\]

因为 \(g=(X,66s+1)=1\)，有 \(7\nmid X\)。再有三个精确 Bezout 关系

\[
(s,X)=1,
\qquad
24L-176X=-56,
\qquad
2E-(264s-9)X=7.
\tag{10}
\]

又 \(X\equiv1\pmod3\) 且 \(X\) 为奇数。由 (10) 和 \(7\nmid X\) 得到

\[
\boxed{(M,X)=1.}
\tag{11}
\]

若 \(d\mid(M,R_0-1)\)，则由 \(pR_0+1=32M\) 及 \(R_0\equiv1\pmod d\) 有

\[
d\mid p+1=2X.
\tag{12}
\]

结合 (11)，\((M,R_0-1)\mid2\)。另一方面 \(R_0-1\equiv2\pmod4\)，而
\(K_0=8M\)。所以 \(R_0-1\) 的全部奇素数幂都相对 \(K_0\) 过量，二因子则绝不
过量。按 complete-excess 的逐素数幂定义，第二步的块不再可选：

\[
\boxed{
Q=\frac{R_0-1}{2}
=1672704s^3+25344s^2-696s-1,
\qquad (M,Q)=1.}
\tag{13}
\]

故下一 full-excess carrier 必为 \(M_1=MQ\)。这只确定算术 block；是否有其他
non-full source/path 仍是另外的问题。

## 4. carry 必然增大

由 (8)、(13) 直接化简得到

\[
8Q-75
=p(278784s^2-1584s-83),
\qquad
8Q\equiv75\pmod p.
\tag{14}
\]

令第二 full-excess canonical target 的 capacity 为 \(c_1\)。由

\[
4M\cdot8\equiv1\pmod p,
\qquad
4MQc_1\equiv1\pmod p
\]

得 \(Qc_1\equiv8\pmod p\)。合并 (14)：

\[
\boxed{75c_1\equiv64\pmod p.}
\tag{15}
\]

在 (1) 中 \(s\ge86\)，故 \(p\ge4129\)。若 \(1\le c_1\le8\)，则

\[
0<75c_1-64\le536<p,
\]

不可能被 \(p\) 整除，与 (15) 矛盾。因此

\[
\boxed{c_1>8.}
\tag{16}
\]

所以第一个 \(c=8\) target 的确定性 full-excess continuation 不是 E5 降容量，
而是严格增容。即使未来为它补齐所有 source/path 数据，也不能把这一步注册为当前
capacity rank 下的 strict edge。

## 5. 控制与边界

已有 \(c=8\) 算术 macro 控制 \(s=3279,p=157393\) 给出

\[
Q=58971931474577975,
\qquad c_1=4198>8.
\tag{17}
\]

该原始素数本身已被 terminal-first 抢占，因此它只复核 (8)--(16) 的算术，不充当
persistent 反例。

本卡的作用是排除一个具体且自然的递归设想：不能把首条 \(c=8\) p-free relay 后的
完整 excess block 再次当作自动容量递降。剩余有效路线必须使用非完整 bundle、不同
raw source、适配的 Type I terminal，或一条带独立势和 E1--E5 的跨图表边；本卡没有
排除这些路线，也没有证明 G/Type I global exit。

根层还有一组看似更短的 ordinary Type II \(p-1\) tail：若
\(m+1=(p-1)/r\)，它会直接回落到分母 \(r+1\)。对这里的 \(s\ge86\)，
\(r=2,3,4,6\)（以及偶 \(s\) 的 \(r=8\)）已由
[低分母 \(p-1\) Type II 尾扇无路](type-II-q-one-full-carrier-d-one-c-eight-low-denominator-tail-fan-no-go.md)
逐一排除。这个新增 no-go 不改变本卡的增容结论，也不排除其它 Type I/II gap；它只防止
把这些小分母 tail 误作尚未支付的 c=8 terminal-first 出口。

后续的[结构 \(m=1\) 节点增容障碍](type-I-q-one-full-carrier-d-one-c-eight-structured-node-carry-obstruction.md)
还表明两个由本 target macro 因子直接指定的不同 formal \(m=1\) 节点，其强制
完整-excess carry 同样增容；它们没有被误记作本卡的重复 action 或已验证 source/path。

新的 [source-side 支撑分离与 non-\(p\) raw 出边]
(type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation.md)
进一步表明该 high-\(R\) chart 的 canonical source 并不只有 \(p\)-edge：它总有
一条实际 \(V\)-side non-\(p\) 出边。不过该结果尚未把 endpoint 接入 typed state，
所以不能借此绕过本卡的 complete-excess 增容结论。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction.py --verify
~~~

复现器只重放 terminal-first 加 roughness 残余、(8)、(10)--(17) 及两个固定算术控制；
不扫描素数、因式分解 target
或历史 Reach。
