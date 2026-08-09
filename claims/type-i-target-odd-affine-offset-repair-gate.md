---
kind: claim
claim_id: type-i-target-odd-affine-offset-repair-gate
title: target-odd 奇 q 的非零仿射偏移修复与 gcd—区间门
statement: 设 q 为奇素数、q 不整除核心素数 p，且 target-odd q-primary 相位为 gamma=0 (mod q^e)。若候选 source-map 允许标签 s=c+u gamma+h t、h>0、L<=s<=U，其中 u 为 q^e 单位，则该角色进入真实 q-prefix q^e|p+4s 的充要条件是 gcd(h,q^e) 整除 beta_e(p)-c，且相应线性同余解类在区间内非空；其中 beta_e(p)=-p*4^{-1} (mod q^e)。无步长的 affine owner s=u gamma+c 更强制 c=beta_e(p)，故偏移类是唯一的。q=2 时 p+4s 恒奇，任何偏移都不能修复 q-prefix。通过该门的标签才可进入 q-prefix 容量；失败只证明当前 affine source-map 不完备，不自动给出递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-target-odd-primary-direct-owner-dyadic-two-gate
  - type-I-qprimary-phase-affine-label-gcd-lift
  - type-I-qprimary-phase-prefix-intersection-capacity
  - type-I-fg-fourier-phase-owner-capacity-bridge
topics:
  - type-I
  - F-state
  - target-odd
  - q-primary
  - affine-source-map
  - offset-repair
  - gcd
  - interval
  - q-prefix
  - capacity
  - proof-program
sources:
  - claim: type-I-qprimary-phase-affine-label-gcd-lift
    role: exact-affine-gcd-interval-solver
  - claim: type-I-qprimary-phase-prefix-intersection-capacity
    role: prefix-center-and-layer-capacity
  - claim: type-i-target-odd-primary-direct-owner-dyadic-two-gate
    role: zero-phase-and-q2-boundary
  - reproduction: reproductions/type_i_target_odd_affine_offset_repair_gate.py
    role: p73-repair-controls
visibility: public
last_checked: '2026-08-09'
---

# target-odd 奇 q 的非零仿射偏移修复与 gcd—区间门

## 输入

固定核心素数 (p\equiv1\pmod {24})、奇素数 (q\nmid p)、高度 (e\ge1)，并令

\[
n=q^e,
\qquad
\beta=-p4^{-1}\pmod n.
\tag{1}
\]

F 态目标对合的 target-odd q-primary 相位满足 (gamma=0\pmod n)。现在不再假设
identity owner，而允许一个已声明的 affine source-map

\[
s=c+u\gamma+h t,
\qquad h>0,
\qquad L\le s\le U,
\tag{2}
\]

其中 (u\in(\mathbb Z/n\mathbb Z)^\times)，(c,h,L,U) 均由 source-map 独立给出。
真实 q-prefix 的算术条件是

\[
q^e\mid p+4s
\iff
s\equiv\beta\pmod n.
\tag{3}
\]

## 仿射修复定理

令

\[
g=\gcd(h,n),
\qquad
\Delta=\beta-c-u\gamma\pmod n.
\tag{4}
\]

则 (2)--(3) 有整数标签解，当且仅当

\[
\boxed{g\mid\Delta}
\tag{5}
\]

并且线性同余的解类在区间 ([L,U]) 内有代表。若 (5) 成立，置

\[
h_1=h/g,
\qquad n_1=n/g,
\qquad
t_0=(\Delta/g)h_1^{-1}\pmod {n_1},
\tag{6}
\]

其中 (n_1=1) 时取 (t_0=0)。所有合法参数恰为

\[
t=t_0+n_1 k,
\tag{7}
\]

并且

\[
\left\lceil\frac{L-c-u\gamma-h t_0}{h n_1}\right\rceil
\le k\le
\left\lfloor\frac{U-c-u\gamma-h t_0}{h n_1}\right\rfloor.
\tag{8}
\]

因此可以精确输出三种回执：

* `TARGET_ODD_AFFINE_REPAIR_GCD_OBSTRUCTED`：(g\nmid\Delta)；
* `TARGET_ODD_AFFINE_REPAIR_INTERVAL_EMPTY`：同余可解但 (8) 为空；
* `TARGET_ODD_AFFINE_REPAIRED`：由 (7)--(8) 得到规范最小标签及其槽数。

通过第三分支后，且只有在 source-map 的其它 E1--E3 条件也通过时，标签才可进入
q-prefix 的逐层容量账本。

### 无步长的唯一偏移

若 owner map 不含 (t)（等价于 (h=0) 的单标签 affine map）并写成

\[
s=u\gamma+c,
\tag{9}
\]

则 target-odd 的 (gamma=0) 使

\[
\boxed{c\equiv\beta\pmod n.}
\tag{10}
\]

所以 identity map (c=0) 必然失败，而任何无步长 affine 修复的偏移类都是唯一的
(eta)-类；单位系数 (u) 不能改变这一结论。带步长时，偏移本身可以不等于 (eta)，
但必须满足 (5)，并由 (8) 检查真实区间。

### 二进边界

若 (q=2)，则 (p+4s\equiv1\pmod2)，没有任何 (eta) 使 (3) 成立。因此
不存在可由 affine offset 修复的二进 q-prefix；二进请求必须改走广义 (2^j)、其它
source relation 或 Type II/严格递降门。

## 证明

把 (2) 代入 (3)，得到一次线性同余

\[
h t\equiv\beta-c-u\gamma\pmod n.
\]

标准 gcd 判据给出 (5)，约去 (g) 并求 (h_1) 的逆得到 (6)--(7)，再与
([L,U]) 相交得到 (8)。target-odd 相位 (gamma=0) 来自目标对合的
(2\gamma=0\) 且 (q) 奇；于是 (h=0) 时直接得到 (10)。q=2 的结论是奇偶性。
证毕。

## 选择器含义

该门把“需要非零 affine source-map”变成一个可证伪的最小接口：

\[
\text{target-odd }
\longrightarrow
\text{偏移 }c\text{ 与步长 }h
\longrightarrow
\gcd/区间
\longrightarrow
\text{真实 q-prefix 槽}
\longrightarrow
\text{SNF/CRT/容量}.
\]

它不把 (c=\beta) 的形式选择误认为 source-map 已存在；source-map 若未声明完备，
`GCD_OBSTRUCTED` 或 `INTERVAL_EMPTY` 只能说明当前进程不能承接角色。特别地，
Fourier 相位幅度不能补足一个缺失的偏移，q-prefix 容量也不能反向构造 source-map。

## 真实控制：(p=73,R=27,q=3,e=2)

此时 (K=493)、target-odd 相位 (gamma=0)，而

\[
\beta=-73\cdot4^{-1}\equiv2\pmod9.
\]

* identity owner (s=\gamma=0) 给出 `DIRECT_OWNER_CONFLICT`；
* 取 affine 过程 (s=5+3t)、区间 ([6,20])，有 (g=3)、
  (Delta=2-5\equiv6\pmod9)，故 (t\equiv2\pmod3)，标签为 (11,20)，
  两者都满足 (9\mid73+4s)，输出 `TARGET_ODD_AFFINE_REPAIRED`；
* 保持 (s=5+3t) 但把区间缩为 ([6,10])，同余类在区间内为空，输出
  `TARGET_ODD_AFFINE_REPAIR_INTERVAL_EMPTY`；
* 取 (s=4+3t)，则 (g=3\nmid(2-4)\)，输出
  `TARGET_ODD_AFFINE_REPAIR_GCD_OBSTRUCTED`。

这个控制说明非零偏移不是口头修补：同一 target-odd 相位可以在不同的已声明 affine
进程中得到修复、区间失败或 gcd 失败；只有第一种才产生可收费的真实 owner 槽。

## 边界

本引理完成的是奇 q target-odd 请求的最小 affine 修复判据。它没有证明任意 F 态都存在
满足 (2) 的真实 source-map，也没有把修复标签自动提升为 Type I/II 证书或 E1--E5
递降；下一步必须从实际线性块、固定 B 清分、SNF/CRT 或 Type-II source record 中
构造并证明这样的 (c,h,[L,U])。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_odd_affine_offset_repair_gate.py --verify
~~~
