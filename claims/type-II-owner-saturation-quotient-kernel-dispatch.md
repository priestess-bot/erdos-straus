---
kind: claim
claim_id: type-II-owner-saturation-quotient-kernel-dispatch
title: Type II owner 碰撞的饱和优先—商缺失/核截面分派
statement: 对固定目标纤维中的一个 owner 加权 q 幂块，先检查直接目标命中，再以所选目标商中 qT 的阶 o 与高度 e 比较：e<o-1 时块未饱和，owner 流与物理槽 source-column 扩张仍是合法后继；e>=o-1 时幂块集合像已饱和为 H=<qT>，owner multiplicity 不增加集合容量，必须优先进入严格商缺失或目标核截面 Fourier 分支。若 H 为 2-primary 子群，核截面分支接广义 2^j 终端；算术回译失败仍保留显式提升障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-owner-projection-source-column-expansion-relay
  - type-II-weighted-source-saturated-quotient-kernel-dispatch
  - type-II-qheight-fourier-set-vs-multiplicity-saturation-boundary
  - type-II-qadic-height-kneser-block-bridge
topics:
  - type-II
  - owner-weight
  - saturation
  - quotient-descent
  - kernel-fourier
  - physical-capacity
  - source-column
  - dyadic-terminal
  - proof-program
sources:
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: owner-token-physical-capacity-gate
  - claim: type-II-owner-projection-source-column-expansion-relay
    role: unsaturated-source-column-expansion
  - claim: type-II-weighted-source-saturated-quotient-kernel-dispatch
    role: saturated-quotient-kernel-dichotomy
  - claim: type-II-qheight-fourier-set-vs-multiplicity-saturation-boundary
    role: set-versus-owner-multiplicity-boundary
  - claim: type-II-qadic-height-kneser-block-bridge
    role: q-adic-active-capacity-and-dyadic-interface
  - reproduction: reproductions/type_ii_owner_saturation_quotient_kernel_dispatch.py
    role: owner-saturation-priority-and-real-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 碰撞的饱和优先—商缺失/核截面分派

## 1. 固定 owner 幂块

固定一个已经通过目标纤维、source-SNF 和整数参数门的 Type II 状态。选定有限
目标商

\[
\pi:G\longrightarrow Q
\]

以及当前稳定子约化后的 q 幂块。令 q 块的最高高度为 \(e\)，其 owner token 写成

\[
\mathcal T_q=\{(q,j,a):0\le j\le e,\ a\in O_{q,j}\}.
\tag{1}
\]

这里 \(a\) 是来源标签，所有同一 \((q,j)\) 的 owner token 都投影到同一个物理
q 槽 \(c_{q,j}\)，而不一定投影到不同的集合元素。记

\[
\bar q=\pi(q),\qquad
H=\langle\bar q\rangle,\qquad
o=|H|>1.
\tag{2}
\]

若使用的是稳定子商 \(Q/T\)，式 (2) 应理解为
\(\bar qT\) 在 \(Q/T\) 中生成的子群；下文仍把这个像记为 \(H\)。

选择器的第一条顺序约束是：若目标 \(t\) 已由合法 owner 加权谱直接命中，
先输出

\[
\mathrm{OWNER\_WEIGHTED\_TARGET\_HIT}
\tag{3}
\]

并构造实际 Type II 除子证书，不因 q 幂块随后满足饱和条件而改写为递降。

## 2. 饱和判据与 owner 流优先级

令

\[
B_q=\{1,\bar q,\ldots,\bar q^e\}\subseteq H.
\tag{4}
\]

有两个互斥的局部分支。

### 未饱和

若

\[
e<o-1,
\tag{5}
\]

则 \(1,\bar q,\ldots,\bar q^e\) 两两不同。输出

\[
\mathrm{OWNER\_Q\_BLOCK\_UNSATURATED}.
\tag{6}
\]

此时 q 幂块还没有完成一个角色商循环，owner token 的物理投影流、source-column
逃逸和新物理槽扩张仍是合法的下一门。必须继续通过
OWNER_PROJECTION_CAPACITY_DEFICIT、OWNER_COLLISION_EXPANSION 或
OWNER_PROJECTION_EXPANSION_RELEASE 等已有分支；不能提前声称商饱和。

### 饱和

若

\[
e\ge o-1,
\tag{7}
\]

则

\[
B_q=H,\qquad \pi(P)H=\pi(P)
\tag{8}
\]

对任何包含该块的源积集 \(P\) 成立。输出

\[
\mathrm{OWNER\_Q\_BLOCK\_SATURATED}.
\tag{9}
\]

从此刻起，owner 标签只改变来源重数函数

\[
W(x)=\#\{\tau\in\mathcal T_q:\pi(\tau)=x\}
\tag{10}
\]

及其 Fourier 系数，不改变集合像 \(B_q=H\) 的物理容量。若物理槽 \(c\) 的预算
为 \(b(c)\)，饱和 q 块在该槽上可收费的容量仍是 \(b(c)\)，而不是
\(|O_{q,j}|b(c)\)。只有 source contract 明确增加物理重复预算时，预算才会改变。

因此一旦 (7) 成立，选择器不得再把同一 q 块的 owner 标签作为新的 Kneser 槽，
也不得调用 owner source-column 扩张作为饱和块的第一后继；必须先执行下一节的
集合级分派。

## 3. 饱和块的商缺失—核截面二分

令 \(P\subseteq G\) 为当前源积集，目标 \(t\in G\setminus P\)，
\(K=\pi^{-1}(H)\)，并令

\[
\rho:Q\longrightarrow Q/H
\tag{11}
\]

为自然商。由 (8)，\(\pi(P)H=\pi(P)\)。于是有精确二分。

### 严格商缺失

若

\[
\rho(\pi(t))\notin\rho(\pi(P)),
\tag{12}
\]

则目标在严格较小商 \(G/K\) 中仍缺失，输出

\[
\mathrm{SATURATED\_OWNER\_QUOTIENT\_MISS}.
\tag{13}
\]

因为 \(o>1\)，\(K\) 非平凡且
\(|G/K|=|Q/H|<|Q|\)。该状态可以交给已有的
SATURATED_QUOTIENT_MISS 递降器；只有当来源标签、整数参数和 E1--E5
回译门通过时，(13) 才升级为可提升的较小模数实例。否则必须记录
ARITHMETIC_QUOTIENT_LIFT_OBSTRUCTED。

### 目标核截面

若

\[
\rho(\pi(t))\in\rho(\pi(P)),
\tag{14}
\]

则定义

\[
S_t=\{k\in K:tk\in P\}.
\tag{15}
\]

商像命中给出 \(S_t\ne\varnothing\)；又因 \(t\notin P\)，有
\(1\notin S_t\)，所以 \(S_t\) 是 \(K\) 的非空真子集。对 \(K\) 的角色群
\(\widehat K\)，Parseval 给出

\[
\boxed{
\sum_{\substack{\psi\in\widehat K\\\psi\ne1}}
\left|\sum_{k\in S_t}\overline{\psi(k)}\right|^2
=|S_t|(|K|-|S_t|)>0.
}
\tag{16}
\]

输出

\[
\mathrm{SATURATED\_OWNER\_KERNEL\_SPLIT}.
\tag{17}
\]

若 \(H\) 或目标稳定子商的活跃部分是 \(2^r\)-阶 primary 循环，则 (17) 直接接
已有的广义 \(2^j\) 核终端；若是奇 primary，则先执行奇主 annihilator 压缩。
式 (16) 仍需通过源关系格、同模数 source-switch 和整数回译，不能把抽象
Fourier 能量自动宣称为原始 Type II 除子。

## 4. 证明

若 \(e\ge o-1\)，指数 \(0,\ldots,o-1\) 已覆盖 \(H\)，故 \(B_q=H\)。将
该块写入 \(P=P_0B_qP_1\)，阿贝尔性给出
\(\pi(P)=\pi(P_0)H\pi(P_1)\)，从而 \(\pi(P)H=\pi(P)\)。因此目标在 \(Q/H\)
中的陪集要么完全没有源像，要么已有源像。

在前一种情况下即 (12)，严格商缺失显然成立。在后一种情况下，取
\(x\in P\) 使 \(\pi(x)\in\pi(t)H\)，则 \(k=xt^{-1}\in K\) 且 \(tk=x\in P\)，
所以 \(S_t\ne\varnothing\)。若 \(1\in S_t\)，则 \(t\in P\)，与目标缺失矛盾；
故 \(S_t\subsetneq K\)。有限群 Parseval 给出 (16)。

owner 标签没有出现在 \(B_q=H\) 的集合像中，只出现在 (10) 的带权函数中，故
不能恢复额外物理槽。若 (5) 成立则幂块未绕满，以上不变性尚未得到，因而只能
回到物理流和 source-column 分派。证毕。

## 5. 三个算术控制与一个抽象控制

### \(p=409\) 的 F 型饱和商缺失

取 \(D=8\)、目标 \(441=p+4\cdot2\cdot4\)，来源
\(537=p+4\cdot8\cdot4\) 与 \(665=p+4\cdot8\cdot8\)。在
\(U(16)\) 中，q=7 的高度为 \(e=1\)，且

\[
\operatorname{ord}_{U(16)}(7)=2,\qquad H=\{1,7\}.
\]

源集合像为 \(P=\{1,3,5,7\}=H\cup3H\)，而目标 \(t=15\) 的陪集
\(15H=\{9,15\}\) 不在 \(\rho(P)\) 中。因此 owner q 块虽满足饱和条件，
正确输出是 SATURATED_OWNER_QUOTIENT_MISS，而不是把 F 型 Fourier 缺口当成
额外 owner 容量。

### \(p=5113\) 的直接命中优先

取 \(D=6\)、目标 \(5117\)，来源标签 3、6。q=7 在模 4 的像阶为 2，且
\(e=1\)，所以 q 块饱和；但 owner 加权支持在 \(t=3\) 处非零，已有
\(K=2,B=1461,C=1\) 的直接 Type II 证书。因此选择器必须先输出
OWNER_WEIGHTED_TARGET_HIT，不生成饱和递降边。

### 加法 \(C_8\to C_4\) 的核截面

令 \(G=\mathbb Z/8\mathbb Z\)，\(\pi(x)=x\bmod4\)，
\(P=\{0,2\}\)、\(t=4\)。q 块 \(B=\{0,2\}\) 在 \(Q=C_4\) 中饱和为
\(H=\{0,2\}\)，且 \(K=\pi^{-1}(H)=\{0,2,4,6\}\)。目标在 \(Q/H\) 中命中，
但不属于 \(P\)，并且

\[
S_t=\{4,6\},\qquad |S_t|(|K|-|S_t|)=2(4-2)=4.
\]

这给出非平凡 SATURATED_OWNER_KERNEL_SPLIT，而不是 owner 槽扩张。

### 未饱和对照

在循环群 \(C_4\) 中取生成元阶 \(o=4\) 的 q 像和 \(e=1\)。此时
\(e<o-1\)，即使存在多个 owner 标签，也只能输出
OWNER_Q_BLOCK_UNSATURATED；后继仍由 owner 流、source-column 和物理容量门决定。

## 6. 研究边界

本引理闭合的是“owner 碰撞何时必须停止物理扩张并转入集合级饱和分派”这一
接口，不等于已经证明每个严格商都能整数回译。剩余决定性缺口是：

1. 为 (13) 建立带来源标签的统一 E1--E5 低模数回译；
2. 为 (17) 建立所有 primary 的源关系相容性，并把 \(2^j\) 终端写成可提升
   的 Type I/II 除子；
3. 在未饱和分支证明跨状态 owner 流或 source-column 扩张最终释放物理容量。

若任何一门失败，状态应保留为可定位的 LIFT_OBSTRUCTED、OWNER_COLLISION_ONLY
或 OWNER_PROJECTION_CAPACITY_DEFICIT，不得将 owner multiplicity 当作隐藏的
Kneser 容量。
