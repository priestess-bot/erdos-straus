---
kind: claim
claim_id: type-II-source-fiber-qheight-kneser-bridge
title: Type II 源参数纤维的 q 进高度—Kneser 幂块精确桥
statement: 固定 p、D 与互异奇素数 q_i，若 q_i^{e_i}|p+4Da_i 且 q_i 不整除 4D。对候选 D_*|D、admissible A|D_*，定义 d_i(A)=max{0<=d<=e_i:q_i^d|AD_*-Da_i}。则 q_i^{d_i(A)}|p+4AD_*，并在 G_*=U(4D_*) 中形成 B_{i,A}={1,q_i,...,q_i^{d_i(A)}}。取最终稳定子 T_A，活跃容量精确为 kappa_{i,A}=min(d_i(A),ord_{G_*/T_A}(q_iT_A)-1)；若目标 -1 缺失则 sum_i kappa_{i,A}<=|G_*/T_A|-2，若总和达到 |G_*/T_A|-1 则该纤维给出 Type II 短证书。p=97 与 p=5113 分别给出逐纤维缺失与真实降模边界。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-qadic-height-kneser-block-bridge
topics:
- type-II
- q-adic-height
- parameter-fiber
- fibered-kneser
- exact-relay
- source-switch
- target-fiber
- constructive-certificate
- proof-program
sources:
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: parameter-fiber-source-carrier
  - claim: type-II-qadic-height-kneser-block-bridge
    role: single-state-q-height-Kneser-identity
visibility: public
last_checked: '2026-08-04'
---

# Type II 源参数纤维的 q 进高度—Kneser 幂块精确桥

## 源层与候选参数

固定核心素数 \(p\)、原始 \(D\)，以及互异奇素数 \(q_1,\ldots,q_r\) 和来源参数
\(a_i\)，满足

\[
q_i^{e_i}\mid p+4Da_i,\qquad
q_i\nmid 4D,\qquad e_i\ge1.
\tag{1}
\]

固定一个候选除子格模数 \(D_*\mid D\)，并取

\[
A\mid D_*,\qquad D_*/A\text{ 平方自由},\qquad 4AD_*<p.
\tag{2}
\]

定义候选参数 \(s_A=AD_*\) 的第 \(i\) 个可用 q 进层数

\[
d_i(A)=
\max\{0\le d\le e_i:q_i^d\mid AD_*-Da_i\}.
\tag{3}
\]

这里 \(d=0\) 总是可行；若差值为零，最大值按上限 \(e_i\) 截断。

## 整除恒等式与精确 q 进 relay

由 (1) 和 (3)，若 \(d=d_i(A)\)，则

\[
p+4AD_*
=(p+4Da_i)+4(AD_*-Da_i)
\equiv0\pmod{q_i^d}.
\tag{4}
\]

所以

\[
\boxed{q_i^{d_i(A)}\mid p+4AD_* .}
\tag{5}
\]

反过来，如果 \(q_i^d\) 同时整除 \(p+4Da_i\) 和 \(p+4AD_*\)，由于
\(q_i\nmid4\)，就有

\[
q_i^d\mid4(AD_*-Da_i)
\iff
q_i^d\mid AD_*-Da_i.
\tag{6}
\]

因此 \(d_i(A)\) 不是一个假设的 relay 需求，而是该候选参数从来源状态真实继承的
最大 q 进高度。互异 \(q_i\) 使这些层可作为互素的源块分别计数；同一个 q 来自多条
来源时，必须先合并其共同 q 进账本，不能按来源重复计费。

## 纤维 Kneser 幂块

令

\[
G_*=(\mathbb Z/4D_*\mathbb Z)^\times,\qquad
u_i=q_i\bmod4D_*,
\]

并在候选参数 \(A\) 的源纤维中定义

\[
B_{i,A}=\{1,u_i,u_i^2,\ldots,u_i^{d_i(A)}\},
\qquad
P_A=\prod_{i=1}^{r}B_{i,A}.
\tag{7}
\]

因 (5)，\(P_A\) 中任一元素
\(\prod_i u_i^{z_i}\)（\(0\le z_i\le d_i(A)\)）都有对应的整数因子
\(\prod_i q_i^{z_i}\mid p+4AD_*\)。故得到精确回译：

\[
\boxed{
-1\in P_A
\Longrightarrow
\text{候选 }(D_*,A)\text{ 有 Type II 短证书}.
}
\tag{8}
\]

取 \(T_A=\operatorname{Stab}_{G_*}(P_A)\)，并令

\[
\kappa_{i,A}
=|B_{i,A}T_A/T_A|-1
=\min\{d_i(A),\operatorname{ord}_{G_*/T_A}(u_iT_A)-1\}.
\tag{9}
\]

多集合 Kneser 给出

\[
|P_A|\ge |T_A|
\left(1+\sum_{i=1}^{r}\kappa_{i,A}\right).
\tag{10}
\]

若

\[
\sum_i\kappa_{i,A}\ge |G_*/T_A|-1,
\tag{11}
\]

则 \(P_A=G_*\)，特别命中 \(-1\)，由 (8) 得 Type II 证书。反之若
\(-1\notin P_A\)，目标陪集 \(-1T_A\) 整体缺失，故

\[
\boxed{
\sum_i\kappa_{i,A}\le |G_*/T_A|-2.
}
\tag{12}
\]

式 (12) 是源参数纤维内的真实 q 进容量缺口；它不需要额外假设“q 进高度注入
Kneser 块”，因为 (4)--(6) 已完成整数层到目标幂块的同余映射。

## 两个边界例子

### \(p=97\) 的逐纤维缺失

取 \(D=6\)，来源

\[
(a_1,q_1^{e_1})=(1,11^2),\qquad
(a_2,q_2^{e_2})=(3,13^2),
\]

因为 \(11^2\mid121=p+24\)、\(13^2\mid169=p+72\)。取 \(D_*=6\)：

- \(A=1\) 时 \(d_1(1)=2,d_2(1)=0\)，故 \(P_1=\{1,11\}\pmod{24}\)；
- \(A=2\) 时 \(d_1(2)=d_2(2)=0\)，故 \(P_2=\{1\}\)；
- \(A=3\) 时 \(d_1(3)=0,d_2(3)=2\)，故 \(P_3=\{1,13\}\pmod{24}\)。

三个纤维都遗漏 \(-1=23\)，而把两条 q 幂块无纤维池化才会产生
\(11\cdot13\equiv-1\pmod{24}\) 的伪命中。

### \(p=5113\) 的真实降模

取 \(D=6\)、来源

\[
(a_1,q_1^{e_1})=(3,17),\qquad
(a_2,q_2^{e_2})=(6,7),
\]

分别整除 \(p+72\) 与 \(p+144\)。取 \(D_*=1,A=1\)，则

\[
d_1(1)=v_{17}(1-18)=1,\qquad
d_2(1)=v_7(1-36)=1.
\]

在 \(G_*=(\mathbb Z/4\mathbb Z)^\times\) 中，
\(P_A=\{1,17\}\{1,7\}=\{1,-1\}\)，从而 \(h=17\cdot7=119\)、
\(K=30\)、\(B=1289\)，得到 \(m=43,d=1\) 的 Type II 证书。

## 研究边界

(3)--(12) 解决了“源 q 进高度如何进入参数纤维 Kneser 容量”的整数层注入问题，
但只在互异 q 的源块模型中成立。重复 q 的多来源碰撞仍需先做共同 q 进账本和
稳定子合并；此外，所有候选 \(D_*,A\) 的容量缺口还没有被证明必然导致另一个
纤维命中、Type I/II 证书或严格核心素数递降。下一步应处理重复 q 的标记合并，
并尝试把 (12) 的缺口统一注入一个可提升的 Fourier/商群下降。
