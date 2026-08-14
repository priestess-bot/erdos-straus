---
kind: claim
claim_id: type-I-root-capacity-strict-carry-tail-receipt-fiber-barrier
title: 严格 root carry 尾门的 receipt-fiber 不变性与直接 D 支撑障碍
statement: >-
  对 strict proper-root carry 的 canonical even complement，固定 p 与 cofactor c 后，
  所有满足 Ec=-1 (mod p) 的 multiplier lifts 所给出的 Bezout 单位 a 都满足
  a=-n^(-1) (mod R)，其中 n 是 c 的 canonical even complement、R=4n-p。
  因而 complete retained-standard-tail selector 及其任意素数幂、角色或有限指数盒表述
  都只经过 (p,c)，不再读取 E、D、h、Q 的额外信息。actual D 的因子分裂只能在 selector
  之前限制可达 cofactor，或提供独立 terminal/descent，不能在固定 (p,c) 的 tail 盒中
  补出因子。actual high-half control p=313,r=271 还满足
  gcd(ph+1,(pn)^2)=4，而 -pn=779 (mod 879)，故 ph+1（包括 D）中没有可直接作为
  tail factor 的因子；即使 D=D_C=8、D|h^2-1、D|4n，tail 仍为空。这给出直接
  D-to-tail-support 路线的严格边界，不构成全局出口定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-strict-carry-complement-tail-bezout-character-gate
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-general-endpoint-divisor-gate
topics:
  - type-I
  - root-capacity
  - strict-carry
  - tail-selector
  - complete-excess
  - receipt-fiber
  - divisor-residue
  - obstruction
  - proof-boundary
sources:
  - claim: type-I-root-capacity-strict-carry-complement-tail-bezout-character-gate
    role: canonical-tail-selector-and-bezout-normalization
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-D-factor-split
  - reproduction: reproductions/type_i_root_capacity_strict_carry_tail_receipt_fiber_barrier.py
    role: lift-invariance-and-fixed-direct-D-support-boundary
visibility: public
last_checked: '2026-08-14'
---

# 严格 root carry 尾门的 receipt-fiber 不变性与直接 D 支撑障碍

## 1. 设置

固定一个 strict proper-root carry，令其 canonical cofactor 为

\[
1\le c\le p-2,
\qquad
c\equiv-E^{-1}\pmod p.
\tag{1}
\]

定义 canonical even complement 与高半区 tail 记号

\[
n=
\begin{cases}
c,&2\mid c,\\
p-c,&2\nmid c,
\end{cases}
\qquad
R=4n-p,
\qquad
S=pn.
\tag{2}
\]

以下假设 \(R>0\)，这包含真正独立的 high-half 域。令

\[
w_E=\frac{Ec+1}{p},
\qquad
a_E=
\begin{cases}
E-4w_E,&2\mid c,\\
3E-4w_E,&2\nmid c.
\end{cases}
\tag{3}
\]

此前的 Bezout 归一化已给出

\[
na_E\equiv-1\pmod R,
\qquad
Sa_E^2\equiv4\pmod R.
\tag{4}
\]

本卡的重点不是重证二次 character 门，而是辨认 (3) 中的 actual receipt
字段在全部高阶 residue 问题中究竟还留下了多少自由度。

## 2. Multiplier lift 的精确规范不变性

### 引理 1（receipt-fiber 单位）

对固定的 \((p,c)\)，每个满足 \(Ec\equiv-1\pmod p\) 的整数 lift 都有

\[
\boxed{a_E\equiv-n^{-1}\pmod R.}
\tag{5}
\]

特别地，若 \(E'=E+tp\)，则

\[
\boxed{
a_{E'}-a_E=
\begin{cases}
-tR,&2\mid c,\\
 tR,&2\nmid c.
\end{cases}}
\tag{6}
\]

**证明。** 由于 \((n,R)=1\)，(4) 的第一式立即给出 (5)。为直接看见
receipt lift 的作用，注意 \(w_{E'}=w_E+tc\)。若 \(c\) 为偶数，\(n=c\)、
\(R=4c-p\)，故

\[
a_{E'}-a_E=tp-4tc=t(p-4c)=-tR.
\]

若 \(c\) 为奇数，\(n=p-c\)、\(R=3p-4c\)，故

\[
a_{E'}-a_E=3tp-4tc=t(3p-4c)=tR.
\]

任意两个满足 (1) 的 multiplier 在模 \(p\) 下相等，故它们正是这种 \(E'\) 的
情形。证毕。

这比“二次角色消去”更强：\(a_E\) 在整个单位群
\((\mathbb Z/R\mathbb Z)^\times\) 中的元素已经由 \((p,c)\) 唯一决定，
而不是只决定其平方类。

## 3. 完整 tail selector 只经过 \((p,c)\)

记 retained-standard-tail 的精确有限 selector 为

\[
\mathcal T(p,c)=
\left\{e:
e\mid S^2,\quad e\le S,\quad e\equiv-S\pmod R
\right\}.
\tag{7}
\]

由 (4)--(5)，它也可等价地写成

\[
\mathcal T(p,c)=
\left\{e:
e\mid S^2,\quad e\le S,\quad
ea_E^2\equiv-4\pmod R
\right\},
\tag{8}
\]

其中 (8) 的同余系数仍只依赖 \((p,c)\)。而 \(S=pn\)、\(R=4n-p\) 和
\(S^2\) 的全部素因子与指数也只由 \((p,c)\) 决定。因此：

\[
\boxed{
\mathcal T(p,c)\text{ 以及它在任意 }q^v\mid R\text{ 上的完整指数盒，
都只经过 }(p,c).}
\tag{9}
\]

这里的“完整指数盒”包括把 \(e\mid S^2\) 写成各素因子指数
\(0\le\alpha_\ell\le2v_\ell(S)\) 后，在任一 \(q^v\mid R\) 上的所有高阶
角色或离散对数约束。它们的底数、指数范围与目标残类都由 \(p,c\) 固定；
改变同一个 cofactor fiber 内的 \(E,D,h,Q\) 不会改变其中任何一个问题。

对于 actual receipt，\(D,h,Q\) 当然可以影响最终出现的 \(c\)，因为

\[
c=\left\langle D(h-1)^{-1}\right\rangle_p.
\tag{10}
\]

但一旦 (10) 已经给出 \(c\)，它们不能再在 (7) 中制造一个新因子。故任何想从
actual \(D\mid ph+1\)、\(D\mid K\) 强制 high-half tail 的成功论证，必须在
进入 (7) **之前**证明一个 cofactor 限制，例如实际 receipt 不会落入

\[
\{c:\mathcal T(p,c)=\varnothing\},
\tag{11}
\]

或从 receipt 独立构造 terminal / registered support-rebase edge。仅在已固定的
tail exponent box 内继续读取 \(D\) 的分解不会产生额外条件。

## 4. Actual \(p=313,r=271\) 的直接 \(D\)-support 边界

这个 strict high-half receipt 具有

\[
p=313,\qquad h=543,\qquad D=D_C=8,\qquad D_T=1,
\]

\[
c=n=298,\qquad R=879,\qquad S=93274=2\cdot149\cdot313.
\tag{12}
\]

它满足实际因子分裂的强侧条件

\[
D\mid K,\qquad D\mid ph+1,\qquad D\mid h^2-1,\qquad D\mid4n.
\tag{13}
\]

然而

\[
ph+1=169960=2^3\cdot5\cdot7\cdot607,
\qquad
\gcd(ph+1,S^2)=4,
\tag{14}
\]

而 tail 的目标残类为

\[
-S\equiv779\pmod{879}.
\tag{15}
\]

所以 (14) 的全部可能 direct receipt-supported tail factors 只有
\(1,2,4\)，没有一个满足 (15)。特别地，不存在既是 \(ph+1\)（因而也可由
\(D\) 或其 receipt quotient 直接供给）的因子、又满足 (7) 的 tail factor。
完整 \(S^2\) 指数盒也确实为空。

这不是说 \(D\) 在全局证明中无用；它只排除一种常见的偷换：把
\(D\mid ph+1\) 或其 \(p\pm1/T\) 分裂当作能直接提供 (7) 的因子。即使 (13)
中的所有简单支撑关系都成立，actual hard control 仍不会命中 tail。

## 5. 对 global-exit 目标的影响

本卡关闭了当前“在既定 high-half selector 内从 \(D\) 的额外赋值强制因子”的路线。
它没有关闭 strict root 的其它出口：

1. 可以寻找真正利用 maximal receipt 来源的 pre-cofactor theorem，排除 (11) 中的
   bad \(c\)；
2. 可以把已知 strict support-rebase 的算术 rank decrease 序列化为具备 persistent
   provenance、terminal-first priority 与 typed replay 的正式递归边；
3. 也可以从 high-half miss 独立回译出 Type I/II terminal，而不是要求其本身是
   retained-standard tail。

因此全称“短证书或递降”引理仍未证明；本卡的贡献是把下一步从无效的 post-cofactor
\(D\)-factor 尝试，收紧为上述三个可证伪对象。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_strict_carry_tail_receipt_fiber_barrier.py --verify
```

脚本只重放 \(p=73,r=3\) 与 \(p=313,r=271\) 的 multiplier-lift 不变性，并在后者
核对 (12)--(15) 的 direct \(D\)-support boundary；不扫描素数、root 参数、分母或历史
selector。
