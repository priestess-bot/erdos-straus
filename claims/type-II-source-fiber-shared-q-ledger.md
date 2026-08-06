---
kind: claim
claim_id: type-II-source-fiber-shared-q-ledger
title: Type II 源参数纤维的重复 q 共同账本
statement: 固定奇素数 q 与来源标签 b_i，使 q^{e_i}|p+4b_i 且 q 不整除 4D。对候选整数 s=AD_* 定义 ell_i(s)=min(e_i,v_q(s-b_i))、L_q(s)=sum_i ell_i(s)、V_q(s)=v_q(p+4s)。在允许源 q 层逐层标记拆分的模型中，可回译到候选 s 的重复-q 总层数恰为 d_q(s)=min(L_q(s),V_q(s))，而不是 sum_i e_i；对应 Kneser 幂块的活跃容量为 min(d_q(s),ord_{G/T}(qT)-1)。p=241,D=6,q=5 的两个来源均含 5，但候选高度仅为 1，严格排除把 5^2 当作可用因子。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-shared-factor-q-adic-difference-bound
topics:
- type-II
- q-adic-height
- repeated-q
- shared-ledger
- parameter-fiber
- Kneser
- exact-relay
- source-switch
- proof-program
sources:
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: distinct-q-fiber-injection
  - claim: type-II-shared-factor-q-adic-difference-bound
    role: shared-q-height-boundary
visibility: public
last_checked: '2026-08-04'
---

# Type II 源参数纤维的重复 \(q\) 共同账本

## 来源层与候选层

固定奇素数 \(q\)，并取若干带来源标签的 q 幂

\[
q^{e_i}\mid p+4b_i,\qquad q\nmid4D,\qquad e_i\ge1.
\tag{1}
\]

这里 \(b_i=Da_i\) 可以来自不同 Type II 参数；同一个 q 的不同来源不视为互素
来源块。对候选 \(s=AD_*\) 定义

\[
\ell_i(s)=
\min\{e_i,v_q(s-b_i)\},
\qquad
L_q(s)=\sum_i\ell_i(s),
\qquad
V_q(s)=v_q(p+4s).
\tag{2}
\]

若 \(s=b_i\)，约定 \(v_q(0)=+\infty\)，所以
\(\ell_i(s)=e_i\)。由 (1) 有精确的逐层恒等式

\[
q^{\ell_i(s)}\mid p+4s.
\tag{3}
\]

证明是
\[
p+4s=(p+4b_i)+4(s-b_i),
\]
并使用 \(q\nmid4\)。

## 重复 q 的精确可用层数

把每个来源 \(i\) 的 \(e_i\) 个 q 因子拆成带标签的单位层，并规定来源 \(i\)
至多贡献 \(\ell_i(s)\) 层。若从这些层中选出总数 \(d\)，要形成候选整数因子
\(q^d\)，还必须有 \(d\le V_q(s)\)。因此可用总层数集合恰为

\[
\boxed{
\{d:\text{存在可回译的源层选择}\}
=\{0,1,\ldots,d_q(s)\},
\qquad
d_q(s)=\min\{L_q(s),V_q(s)\}.
}
\tag{4}
\]

### 证明

任意可回译选择从来源 \(i\) 取至多 \(\ell_i(s)\) 层，故总数
\(d\le L_q(s)\)；其整数因子 \(q^d\) 必须整除 \(p+4s\)，故
\(d\le V_q(s)\)。这是上界。

反过来，给定 \(0\le d\le\min(L_q(s),V_q(s))\)，从各来源的
\(\ell_i(s)\) 个标记层中任取总数 \(d\) 个。所有层的整数乘积都是 \(q^d\)，
且 \(q^d\mid p+4s\)。所以每个区间内的 d 都可实现，得到 (4)。
证毕。

式 (4) 说明重复 q 的正确账本是“来源兼容总层数”和“候选实际 q 高度”的最小值；
直接使用 \(\sum_i e_i\) 会在候选高度不足时重复收费。

## 进入 Kneser 幂块

在候选模数 \(M_*=4D_*\) 的单位群

\[
G_*=(\mathbb Z/M_*\mathbb Z)^\times
\]

中令 \(u_q=q\bmod M_*\)，并取

\[
B_q(s)=\{1,u_q,u_q^2,\ldots,u_q^{d_q(s)}\}.
\tag{5}
\]

若与其它互异 q 的源块及固定碰撞积集一起形成 \(P_s\)，最终稳定子为
\(T_s=\operatorname{Stab}(P_s)\)，则重复 q 的真实活跃容量是

\[
\boxed{
\kappa_q(s)=
\min\{d_q(s),\operatorname{ord}_{G_*/T_s}(u_qT_s)-1\}.
}
\tag{6}
\]

目标 \(-1\notin P_s\) 时，多集合 Kneser 强制所有 q 块的总活跃容量满足相应商群
缺口；重复 q 只出现一次 \(B_q(s)\)，不能按来源 i 重复加入。

## 严格边界例子

取

\[
p=241,\qquad D=6,\qquad q=5.
\]

两个来源参数 \(a_1=1,a_2=6\) 给出

\[
5\mid p+24=265,\qquad
5\mid p+144=385.
\]

对候选 \(s=6\)，有

\[
\ell_1(6)=\min(1,v_5(0))=1,\qquad
\ell_2(6)=\min(1,v_5(-30))=1,
\]

所以 \(L_5(6)=2\)。但

\[
V_5(6)=v_5(265)=1,
\qquad
d_5(6)=\min(2,1)=1.
\]

因此 \(5^2=25\nmid265\)，不能把两个来源的 5 因子作为两个独立 q 层直接相乘。
候选 \(s=36\) 同样有 \(V_5(36)=v_5(385)=1\)，再次得到 \(d_5(36)=1\)。
这是一条实际算术的重复-q 双计费反例，而不是抽象群论例子。

## 研究边界

(4)--(6) 关闭了重复 q 的整数层双计费问题，但“逐层标记拆分”本身必须在具体
source-switch 合同中被保留；若只允许整块来源而不允许拆分，应使用更小的整块账本。
该共同账本仍只给出纤维内的 q 幂块，不证明所有候选纤维中至少一个命中，也不自动
生成核心素数递降。下一步要把 (4) 与所有 \(D_*,A\) 的参数纤维联合起来，寻找
容量超载或构造保持标记集的严格下降。
