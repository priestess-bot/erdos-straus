---
kind: claim
claim_id: type-II-q-one-factor-pair-source-compression
title: q=1 G source 到标准 Type II 两尾递降的平方根压缩
statement: >-
  令 p=24t+1、X=(p+3)/4，且一个标准 Type II factor-pair two-tail descent
  使用 m=4a-1、m+1|p-1 与 n=(p+m)/(m+1)。则 a|X-1，且 q=1 source 在
  较小分母中的精确交集为 gcd(X,n)=gcd(X,a-1)。若 q=1 endpoint 是 G 并且
  该 factor-pair certificate 实际存在，则 a>1，故 J=gcd(X,n) 满足 J^2<=X；
  等价地，完整 X source 到 n 的任何 support-preserving 叙述至少损失乘法因子
  X/J>=sqrt(X)。对任一规范根 inverse predecessor 的 H_d=gcd(X,K_d)，有
  gcd(H_d,n)=gcd(H_d,a-1)，所以只有这个平方根以下的子 carrier 可进入 n。
  p=673,a=14 给出代数等号控制 X=J^2=169；真实 gap-59 terminal p=118801,a=15
  只保留 J=7，而 X/J=4243。本卡不构造 E1/E3 adapter，也不证明所有 G 状态存在
  factor-pair certificate 或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - gap-three-criterion
  - type-II-factor-pair-carrier-strict-descent
  - type-II-q-one-canonical-root-full-product-predecessor-rigidity
topics:
  - type-II
  - q-one
  - G-state
  - factor-pair
  - two-tail-lift
  - strict-descent
  - source-carrier
  - capacity
  - source-provenance
  - proof-boundary
sources:
  - claim: gap-three-criterion
    role: q-one-G-excludes-the-a-equals-one-certificate
  - claim: type-II-factor-pair-carrier-strict-descent
    role: standard-two-tail-lift-and-explicit-solution-map
  - claim: type-II-q-one-canonical-root-full-product-predecessor-rigidity
    role: canonical-predecessor-retained-carrier-definition
  - claim: type-II-gap-59-crt-factor-pair-terminal-descent
    role: actual-nontrivial-source-overlap-control
  - reproduction: reproductions/type_ii_q_one_factor_pair_source_compression.py
    role: exact-gcd-square-root-and-terminal-controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 G source 到标准 Type II 两尾递降的平方根压缩

## 1. 设置

固定核心素数

\[
p=24t+1,
\qquad
X=\frac{p+3}{4}=6t+1,
\qquad
U=\frac{p-1}{4}=X-1.
\tag{1}
\]

考虑一张已经存在的标准 Type II factor-pair two-tail certificate。写其 gap 为

\[
m=4a-1,
\qquad
m+1\mid p-1,
\tag{2}
\]

并令其严格较小的源分母为

\[
n=\frac{p+m}{m+1}.
\tag{3}
\]

由 (1)--(3)，整除前提与源分母分别化为

\[
a\mid U=X-1,
\qquad
n=\frac Ua+1,
\qquad
x=\frac{p+m}{4}=an.
\tag{4}
\]

这里的 two-tail lift 是已有的显式标记映射；本卡只研究这张已存在 certificate 如何与
q=1 的 (X)-carrier 相交，不把它假设成一条已经通过 E1/E3 的状态边。

## 2. 精确交集公式

由 (a\mid X-1)，有

\[
(a,X)=1.
\tag{5}
\]

又 (4) 给出

\[
an=X+(a-1).
\tag{6}
\]

因此

\[
\gcd(X,an)=\gcd(X,a-1).
\tag{7}
\]

结合 (5) 即得以下精确恒等式：

\[
\boxed{
J_a:=\gcd(X,n)=\gcd(X,x)=\gcd(X,a-1).
}
\tag{8}
\]

逐素数幂地，若 \(\ell^e\Vert X\)，则

\[
\min\{e,v_\ell(n)\}
=\min\{e,v_\ell(a-1)\}.
\tag{9}
\]

所以 (8) 不是只说支撑是否相交，而是完整记录了 (X) 的每个指数层在 two-tail
源 (n) 中能留下多少。

若进一步取规范根完整乘积前驱的任意已保留 carrier

\[
H_d=\gcd(X,K_d),
\tag{10}
\]

则 (H_d\mid X)，故 (8) 限制为

\[
\boxed{
J_{d,a}:=\gcd(H_d,n)=\gcd(H_d,a-1).
}
\tag{11}
\]

也就是说，先前一步 bridge 中尚存的任何 (H_d)-层，只有恰好也落入 (a-1) 的部分
才能进入这个严格较小的 two-tail source；它不能进入参数 (a) 本身。

## 3. 平方根压缩定理

**定理。** 若 (a>1)，则 (8) 中的 (J_a) 满足

\[
\boxed{J_a^2\le X.}
\tag{12}
\]

因此

\[
\boxed{
J_a\le\sqrt X,
\qquad
\frac{X}{J_a}\ge\sqrt X.
}
\tag{13}
\]

**证明。** (J_a=1) 时 (12) 显然。否则由 (J_a\mid a-1) 和 (a>1)，有

\[
a\ge J_a+1.
\tag{14}
\]

又 (J_a\mid n)，所以 (n\ge J_a)。将其代入 (4) 的

\[
X-1=a(n-1)
\tag{15}
\]

得到

\[
X-1\ge(J_a+1)(J_a-1)=J_a^2-1,
\]

即为 (12)。证毕。

等号完全刚性：当 (J_a>1) 时，(J_a^2=X) 当且仅当

\[
\boxed{a=J_a+1,\qquad n=J_a,\qquad X=J_a^2.}
\tag{16}
\]

事实上，(15) 中的两个下界同时取等恰给出正向；反向直接代入即可。

若 q=1 endpoint 是 G，则 gap (3) 没有 Type I/II certificate。因而任何**实际存在**的
标准 factor-pair certificate 不会取 (a=1)，所以 (12)--(13) 对每一张这种真实
two-tail descent 都适用。由 (11)，每个 predecessor 层还满足

\[
J_{d,a}\le\min\{H_d,\sqrt X\}.
\tag{17}
\]

这给出的不是 E1 provenance：它是任何声称把完整 (X) source 带入 (n) 的 adapter
必须满足的算术容量上界。特别地，它比一步 pre-root 的固定最小损失界更强：一旦真正
进入标准严格 two-tail source，完整 (X) 的可见部分最多为平方根量级。

## 4. 三个精确控制

### 4.1 (p=673)：界在算术接口上 sharp

取

\[
p=673,
\qquad X=169=13^2,
\qquad a=14,
\qquad m=55,
\qquad n=13.
\tag{18}
\]

这里 (a\mid168=X-1)，并且

\[
J_a=\gcd(169,13)=13,
\qquad J_a^2=X.
\tag{19}
\]

所以 (12) 不能在仅使用 (1)--(4) 的层面加强为严格不等式。这个控制没有 factor-pair
certificate：完整因子对枚举在 (x=182,m=55) 处为空。因此它证明的是算术 transfer
映射的 sharpness，不是一个新的 terminal。

### 4.2 (p=118801)：真实 terminal 的非零但强压缩交集

已有 gap-59 terminal 取

\[
p=118801,
\qquad X=29701=7\cdot4243,
\qquad a=15,
\qquad m=59,
\qquad n=1981=7\cdot283.
\tag{20}
\]

其互素因子对为

\[
(A,B,C,K)=(1,1415,21,24),
\qquad ABC=29715=an,
\qquad A+B=59K.
\tag{21}
\]

于是这确实是一张标准 terminal/strict two-tail descent，而

\[
J_a=\gcd(29701,1981)=7,
\qquad
\frac{X}{J_a}=4243>\sqrt{29701}.
\tag{22}
\]

因此该定理不应被夸大为“所有 q=1 carrier 都被清零”：小的 (7)-层确实可以进入
较小分母；但完整 source 的其余 (4243) 倍容量必须被丢弃或另行 source-switch。

### 4.3 (p=1033)：大 pre-root overlap 不进入一个相容 source

已有 canonical predecessor 控制有

\[
X=259=7\cdot37,
\qquad H_{330}=37.
\tag{23}
\]

取 (a=43\mid258=X-1)，则 (n=7)，并且

\[
\gcd(X,n)=7,
\qquad
\gcd(H_{330},n)=\gcd(37,42)=1.
\tag{24}
\]

故完整 (X) 的一个小层可以满足 (8)，但这个特定的较大 pre-root overlap 完全不能进入
该 source。这是 (11) 的必要条件控制，不声称 (m=171) 已有 factor-pair terminal。

## 5. 边界

本卡没有证明每个 q=1 G 状态存在 factor-pair certificate，也没有把 (8) 自动升级为
source-reachable state 或全域 E4 lift。它的作用是缩小正确桥梁的搜索空间：标准
two-tail route 若要复用 q=1 source，只能从 (a-1) 的平方根以下交集中取材；把
pre-root carrier 重命名为 gap 参数 (a)，或把任意 (H_d) 原样传入 (n)，都与
(8)--(17) 不相容。
