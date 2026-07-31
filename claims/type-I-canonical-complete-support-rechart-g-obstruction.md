---
kind: claim
claim_id: type-I-canonical-complete-support-rechart-g-obstruction
title: 规范完全换支撑重图表及其普适 G 态终点
statement: 对每个核心素数 p≡1 (mod 24)，令 a=(p-1)/4。线性图表 S=(a,1,3) 可沿因子 Q=a 转移到 T=(1,1,p-2)；其 K 值分别为 3a+1 与 4a^2，素因子支撑完全不交，且同目标势 (p,as) 从 (p,a) 严格降到 (p,1)。但 T 对所有 p 都是 G 态：Jacobi 角色 (./(p-2)) 在 2 及每个素因子 ell|a 上为 1，而在 -1 上为 -1。因此该转移只有在取图表无关的 W=Sol(p) 时才有恒等提升，并且规范终点没有中心 Type I 目标纤维；它证明合法换支撑与良基重图表存在，也同时证明该机制本身不能闭合猜想。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-source-factor-transfer-rigidity
  - type-I-f-g-fourier-obstruction-certificate
  - marked-solution-descent-closure
  - denominator-escape-state-contract
topics:
  - type-I
  - linear-source
  - factor-transfer
  - support-switch
  - rechart
  - G-state
  - Jacobi-symbol
  - well-founded-potential
  - proof-boundary
sources:
  - claim: type-I-linear-source-factor-transfer-rigidity
    role: fixed-s-factor-transfer-identity
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: G-state-separating-character-interface
  - claim: denominator-escape-state-contract
    role: typed-G-state-and-edge-contract
visibility: public
last_checked: '2026-07-31'
---

# 规范完全换支撑重图表及其普适 G 态终点

## 1. 同目标因子转移的合法势

设一个线性源图表满足

\[
p=a+s+asR.
\tag{1}
\]

若 \(Q>1\)、\(Q\mid a\) 且 \(Q\equiv1\pmod s\)，固定 \(s\) 的因子转移为

\[
(a,s,R)\longmapsto
\left(\frac aQ,s,QR+\frac{Q-1}{s}\right).
\tag{2}
\]

[因子转移引理](type-I-linear-source-factor-transfer-rigidity.md)已经证明 (2) 仍表示同一个
\(p\)。若状态的标记集取为图表无关的

\[
W_{p;a,s,R}=\operatorname{Sol}(p),
\tag{3}
\]

则反向解提升就是恒等映射。规范定向 (2) 还严格降低

\[
\Pi(p;a,s,R)=(p,as)
\tag{4}
\]

的第二分量。若需要单个自然数秩，可取 \(p^2+as\)。所以支撑退出后即使在别的图表
重新进入，也不会破坏这个预先定义的同目标良基势。

这使 (2) 成为合法的**重图表边**，但不是较小方程分母的算术递降。它能否帮助证明
\(\operatorname{Sol}(p)\ne\varnothing\)，完全取决于所有下降终点是否有直接终端或另一条
真正可闭合的边。

## 2. 每个核心素数都有完全换支撑的一步

令

\[
a=\frac{p-1}{4}.
\tag{5}
\]

核心条件 \(p\equiv1\pmod {24}\) 给出 \(a\equiv0\pmod6\)。取

\[
S=(a,1,3).
\tag{6}
\]

则 (1) 成立，因为 \(a+1+3a=4a+1=p\)。在 (2) 中取 \(Q=a\)，得到

\[
T=(1,1,4a-1)=(1,1,p-2).
\tag{7}
\]

两张图表的中心参数为

\[
K_S=\frac{3p+1}{4}=3a+1,
\qquad
K_T=\frac{p(p-2)+1}{4}=4a^2.
\tag{8}
\]

由于

\[
\gcd(3a+1,a)=1
\]

且 \(3a+1\) 为奇数，得到

\[
\boxed{\gcd(K_S,K_T)=1.}
\tag{9}
\]

所以这一步不是“稍微改变”支撑，而是把 \(K\) 的素因子支撑全部换掉，同时把
\(as=a\) 降到 \(1\)。

## 3. 规范终点必为 G 态

记

\[
R_T=4a-1=p-2.
\]

因为 \(a\equiv0\pmod6\)，有 \(R_T\equiv7\pmod8\)。考虑 Jacobi 角色

\[
\chi(x)=\left(\frac{x}{R_T}\right).
\tag{10}
\]

二次补充律给出

\[
\chi(2)=1.
\tag{11}
\]

对任意奇素数 \(\ell\mid a\)，有 \(R_T\equiv-1\pmod\ell\)。Jacobi 二次互反律与
\((R_T-1)/2\) 为奇数给出

\[
\left(\frac{\ell}{R_T}\right)
=\left(\frac{R_T}{\ell}\right)
(-1)^{(\ell-1)/2}
=\left(\frac{-1}{\ell}\right)
(-1)^{(\ell-1)/2}
=1.
\tag{12}
\]

由 \(K_T=4a^2\)，(11)--(12) 说明 \(K_T\) 支撑生成子群中的每个元素都落在
\(\ker\chi\) 中。但

\[
\chi(-1)=(-1)^{(R_T-1)/2}=-1.
\tag{13}
\]

因此

\[
\boxed{-1\notin\mathcal H_{R_T}(K_T),}
\tag{14}
\]

也就是 \(T\) 对每个核心素数都是 G 态。其中心目标纤维为空，不能产生中心 Type I
除子。

## 4. 对递降计划的精确含义

本引理同时给出正面接口和负面边界：

1. 同一 \(p\) 内确实存在完全换支撑、全域恒等提升和严格良基势；
2. 这个规范边一步就到达 \(as=1\)，无法再沿同类前向因子转移；
3. 终点又普适地是 G 态，所以“不断换支撑直到中心命中”不能由该机制证明；
4. 若把 (3) 改成图表依赖的中心标记解集，G 态的源集合为空，恒等映射不再能证明
   根状态非空。

按照[状态合同](../concepts/denominator-escape-state-contract.md)，T 应记录

```text
target_fiber.status = empty
target_fiber.emptiness_certificate = Jacobi_character
signed_defect.status = not_applicable
```

而不是继承 S 的 F/hit 见证。下一条真正有证明增量的边必须从这种 G 终点构造独立
Type II、非中心 Type I，或一个较小方程上非空且可提升的标记状态。
