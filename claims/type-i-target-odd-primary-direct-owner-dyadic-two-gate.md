---
kind: claim
claim_id: type-i-target-odd-primary-direct-owner-dyadic-two-gate
title: F 态 target-odd primary 的直接 owner—自然二进两门无局部提升
statement: 对核心素数 p、Type-I F 态和目标 t=-1 的 q-primary 角色，若 q 为奇素数且 q 不整除 p，则 target-odd 相位与 q-prefix owner 的 identity map 不相容；若 q=2，则 p+4s 对所有整数 s 都为奇数，直接 q-prefix 在正高度上恒为空。再者，任一满足广义二进前驱条件的候选 (E,n) 若使用自然标记 alpha=nK/E，其标记源非空当且仅当当前中心 Type-I 图表命中，故在 F 态也为空。于是 target-odd primary 不能同时通过直接 owner 或自然广义二进两条局部入口；若这两类已声明 source-complete，必须输出 TARGET_ODD_PRIMARY_TWO_GATE_NO_LOCAL_LIFT，并转入非零仿射/其它 source relation、Type II、支撑分离或严格递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-target-odd-qprefix-direct-owner-no-go
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-generalized-dyadic-natural-lift-equivalence
  - type-I-fg-fourier-phase-owner-capacity-bridge
topics:
  - type-I
  - F-state
  - target-odd
  - q-primary
  - direct-owner
  - q-prefix
  - generalized-dyadic
  - natural-lift
  - local-obstruction
  - source-map
  - proof-program
sources:
  - claim: type-i-target-odd-qprefix-direct-owner-no-go
    role: odd-q-direct-owner-obstruction
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: q2-phase-and-target-involution
  - claim: type-I-generalized-dyadic-natural-lift-equivalence
    role: natural-dyadic-source-equivalence
  - reproduction: reproductions/type_i_target_odd_primary_direct_owner_dyadic_two_gate.py
    role: q2-q3-and-F-dyadic-controls
visibility: public
last_checked: '2026-08-09'
---

# F 态 target-odd primary 的直接 owner—自然二进两门无局部提升

## 设置

固定一个核心素数

\[
p\equiv1\pmod {24},\qquad 4K=pR+1,
\]

其中 (R) 为奇数，并考虑一个已经完成固定层稳定子约化的 Type-I F 态。目标为

\[
t=-1.
\]

设规范目标奇角色的 q-primary 高度为 (e\ge1)，其无界目标预像相位为

\[
\gamma\in\mathbb Z/q^e\mathbb Z.
\]

直接 owner 入口要求同一个整数标签 (s) 同时满足

\[
s\equiv\gamma\pmod {q^e},
\qquad q^e\mid p+4s.
\tag{1}
\]

第二条是 q-prefix 的真实算术条件；第一条是 identity source-map。自然广义二进入口则
取一个偶前驱

\[
E\mid4K^2,\quad E\equiv1\pmod R,\quad
n=\frac{4K-E}{R},\quad 0<n<p,
\tag{2}
\]

并要求自然标记分母

\[
\alpha=\frac{nK}{E}
\tag{3}
\]

包含在 (4/n) 的一个可提升解中。

## 两门无局部提升定理

### 1. 直接 owner 门

目标对合给出

\[
2\gamma\equiv0\pmod {q^e}.
\tag{4}
\]

若 (q) 为奇素数且 (q\nmid p)，则 2 可逆，所以

\[
\gamma\equiv0\pmod {q^e}.
\tag{5}
\]

又因 (q\nmid4)，第二个同余等价于

\[
s\equiv-p4^{-1}\pmod {q^e}.
\tag{6}
\]

右侧为非零单位类，和 (5) 不相交。因此 (1) 无解。

若 (q=2)，不需要使用 (4)：核心素数 (p) 为奇数，而 (4s) 为偶数，故

\[
p+4s\equiv1\pmod2
\]

对所有整数 (s) 成立，因而 (2^e\mid p+4s) 对 (e\ge1) 永远不成立。于是

\[
\boxed{\text{q=2 的直接 q-prefix 容量在所有正高度上为零。}}
\tag{7}
\]

在 Type-I 使用的 q-prefix 中，奇素数 q 通常来自 (K)；此时自动有 (q\nmid p)，因为
若 (p\mid K)，则由 (4K=pR+1) 得 (p\mid1)，矛盾。

### 2. 自然广义二进门

对 (2) 定义

\[
W_{n,\alpha}=\left\{(u,v)\in\mathbb N^2:
\frac4n=\frac1\alpha+\frac1u+\frac1v\right\}.
\]

由自然标记提升等价，

\[
W_{n,\alpha}\ne\varnothing
\iff
\frac RK\text{ 有两个正单位分数分解}
\iff
\text{当前 }(R,K)\text{ 图表有中心 Type-I 命中}.
\tag{8}
\]

F 态的定义正是当前固定层目标 (-1) 没有这个中心命中，所以

\[
\boxed{W_{n,\alpha}=\varnothing\quad\text{对每一个满足 (2) 的自然广义二进候选。}}
\tag{9}
\]

这一步排除的是自然标记提升，不是所有可能的偶前驱；改变标记集或尾项仍需独立的
E4/E5 证明。

### 3. 选择器回执

若当前 source universe 已声明只包含 (1) 的直接 owner 和 (3) 的自然广义二进标记，
则 target-odd primary 请求的局部候选集合为空，应输出

\[
\boxed{\texttt{TARGET\_ODD\_PRIMARY\_TWO\_GATE\_NO\_LOCAL\_LIFT}}.
\]

这不是 Type I/II 证书，也不是自动递降。合法后续必须显式进入以下至少一条：

1. 非零仿射 source-map (s\equiv u\gamma+c) 并通过 phase-prefix/SNF/整数门；
2. alternate source relation、CRT、raw lineage 或 Type-II source record；
3. G 型支撑分离（若该角色在源差分上恒等）；
4. 一个已验证的 Type I/II 短证书或满足 E1--E5 的严格可提升递降。

因此不能把 q=2 重新计入 q-prefix 容量，也不能把自然二进候选的偶性当作 source lift。

## 证明

(4) 是目标对合 (t^2=1) 在 q-primary 角色上的相位约束。奇 q 时得到 (5)，再由
4 的可逆性得到 (6)，而 (q\nmid p) 使其非零；q=2 时直接由奇偶性得到 (7)。

对于自然二进门，(8) 是自然标记提升等价：由 (E\equiv1\pmod R) 和
(nR=4K-E) 可得 (E\mid nK)，并有

\[
\frac4n-\frac1\alpha=\frac RK
=\frac4p-\frac1{pK}.
\]

所以含 (alpha) 的源解与含 (pK) 的目标解精确对应；两尾方程
(R/K=1/u+1/v) 又等价于中心 Type-I 除子条件。F 态排除该除子，得 (9)。两门结论合并即证。

## 真实控制

### 直接 owner：(p=73,R=27,K=493)

取 (q=3,e=2)。(U(27)) 的生成元 2 满足 (-1=2^9)，阶 18 的角色 q-primary
目标相位为

\[
\gamma=2\cdot9\equiv0\pmod9.
\]

而

\[
-73\cdot4^{-1}\equiv2\pmod9,
\]

所以奇 q 直接 owner 为空。对同一个 p，q=2 的所有正高度也由 (7) 为空。

### 自然二进：真实 F 态 (p=67369,R=27)

取

\[
K=454741=7\cdot167\cdot389,
\qquad E=28,
\qquad n=67368.
\]

则

\[
4K=pR+1,
\quad E\mid4K^2,
\quad E\equiv1\pmod {27},
\quad n=\frac{4K-E}{27},
\]

且

\[
\alpha=\frac{nK}{E}=1094106846.
\]

该状态的中心 Type-I 除子条件 (D\mid K^2, D\equiv-K\pmod {27}) 在完整的
(K^2) 除子表中为空；因此这是一个真实的 F 态广义二进候选，而 (8) 给出的自然
标记源为空。它保留了“偶前驱存在”与“自然递归提升不存在”之间的严格区别。

## 边界

本引理把 target-odd primary 的两个最自然局部入口同时判为空，但不证明所有 alternate
source relation 都不存在，也不提供全称 E1--E5 递降。它将剩余工作精确压缩为：构造一个
带非零偏移的 source-map、从 source-difference/Type-II 核中给出直接证书，或证明
两门失败后存在严格良基后继。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_odd_primary_direct_owner_dyadic_two_gate.py --verify
~~~
