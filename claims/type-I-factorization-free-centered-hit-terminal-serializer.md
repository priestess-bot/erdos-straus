---
kind: claim
claim_id: type-I-factorization-free-centered-hit-terminal-serializer
title: 无因数分解中心 hit 的 Type I 终端序列化
statement: >-
  固定核心素数 p、R>=3 与 4K=pR+1。若给出一对正整数 u,v，满足
  gcd(u,v)=1、uv|K 与 u+v=0 (mod R)，则只用 gcd、整除和整数同余即可验证并显式构造
  p 的直接 Type I 终端；不必给出 K 的完整素因子分解或中心指数向量。令
  a=min(u,v)、b=max(u,v)、mu=(a+b)/R、c=K/(ab)，则
  h=(4a^2c+1)/R 是自然 Type I 缺口，(mu,a,c) 是互素正规形，实际 Type I 证书除子为
  mu^2c，而中心 hit 除子为 a^2c；显式分母为 mu*a*c、mu*b*c、p*a*b*c。
  该结果是 terminal-first 的局部 serializer，不提供寻找 (u,v) 的全称算法，也不放松
  F/G 分类、递归 state 或 E1--E5 对完整 K-support 的要求。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-coprime-factor-normal-form
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - denominator-escape-state-contract
topics:
  - type-I
  - centered-hit
  - terminal-first
  - factorization-free
  - serializer
  - proof-boundary
sources:
  - claim: type-I-coprime-factor-normal-form
    role: Type-I-certificate-normal-form
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: center-divisor-to-natural-gap-construction
  - reproduction: reproductions/type_i_factorization_free_centered_pair_terminal.py
    role: exact-integer-terminal-receipts
  - concept: denominator-escape-state-contract
    role: terminal-leaf-versus-recursive-state-separation
visibility: public
last_checked: '2026-08-17'
---

# 无因数分解中心 hit 的 Type I 终端序列化

## 1. 结果的精确范围

固定核心素数

\[
p\equiv1\pmod {24},\qquad R\ge3,\qquad 4K=pR+1.
\tag{1}
\]

于是 \(R\equiv3\pmod4\)，且 \((K,R)=1\)。假定给出正整数 \((u,v)\)，满足

\[
(u,v)=1,\qquad uv\mid K,\qquad u+v\equiv0\pmod R.
\tag{2}
\]

令

\[
a=\min(u,v),\qquad b=\max(u,v),\qquad
\mu=\frac{a+b}{R},\qquad c=\frac K{ab}.
\tag{3}
\]

由于 \(R\ge3\)，(2) 排除 \(u=v\)，故 \(a<b\)。定义

\[
d_0=a^2c,\qquad h=\frac{4d_0+1}{R}.
\tag{4}
\]

则 \(h\) 是合法自然缺口，并有

\[
p=4\mu ac-h,\qquad (\mu,a)=1,\qquad h\mid ap+\mu,
\qquad \frac{ap+\mu}{h}=b.
\tag{5}
\]

因此 \((A,B,C)=(\mu,a,c)\) 是
[Type I 除子证书的互素因子正规形](type-I-coprime-factor-normal-form.md)中的正规三元组。
相应的**实际 Type I 证书除子**是

\[
d_{\mathrm{cert}}=\mu^2c\mid x^2,\qquad
x=\frac{p+h}{4}=\mu ac,\qquad h\mid px+d_{\mathrm{cert}}.
\tag{6}
\]

这里必须区分 \(d_{\mathrm{cert}}\) 与中心 chart 的 hit 除子 \(d_0\)。后者只负责把
\(R\) 上的反足关系变成 gap；前者才是 Bradford Type I certificate。

更直接地，(2) 给出无需任何参数化反演的三分式：

\[
\boxed{
\frac4p
=\frac1{\mu ac}+\frac1{\mu bc}+\frac1{pabc}.
}
\tag{7}
\]

所以 \((u,v)\) 是一个可独立核验的 terminal leaf receipt。验证只需计算整数 gcd、一次
\(ab\mid K\) 的整除检查、\(R\mid a+b\) 和有限次乘除；不需要分解 \(K\)。

## 2. 证明

由 (1)，\(pR\equiv-1\pmod4\)，故 \(R\equiv3\pmod4\)。又
\((K,R)=1\) 来自 \(4K-pR=1\)。由 \(ab\mid K\)，\(a,b\) 都与 \(R\) 互素。

因为 \(a+b=\mu R\)，模 \(R\) 有 \(b\equiv-a\)。所以

\[
d_0=a^2c=\frac{Ka}{b}\equiv-K\pmod R,
\tag{8}
\]

其中使用 \(b^{-1}\equiv-a^{-1}\pmod R\)。结合 \(4K\equiv1\pmod R\)，得到
\(4d_0+1\equiv0\pmod R\)，故 (4) 中的 \(h\) 为正整数。

把 \(a+b=\mu R\) 和 \(K=abc\) 代入，得到

\[
\begin{aligned}
R(4\mu ac-h)
 &=4ac(a+b)-(4a^2c+1)\\
 &=4abc-1=pR,
\end{aligned}
\tag{9}
\]

从而有 (5) 的第一个等式。并且

\[
ap+\mu
=a(4\mu ac-h)+\mu
=\mu(4a^2c+1)-ah
=h(\mu R-a)=hb.
\tag{10}
\]

\((\mu,a)=1\) 也成立：任一公共素因子同时整除 \(a\) 与 \(\mu\)，便会整除
\(\mu R-a=b\)，这与 \((a,b)=1\) 矛盾。由 \(a<b\)，

\[
R(p-h)=4ac(b-a)-2>0.
\tag{11}
\]

又 \(hR=4d_0+1\equiv1\pmod4\) 与 \(R\equiv3\pmod4\) 给出
\(h\equiv3\pmod4\)，故 \(3\le h\le p-2\)。这证明 (5) 是合法 Type I 正规形，
(6) 随其标准对应立即成立。

最后，(7) 的前两项之和是

\[
\frac1{\mu ac}+\frac1{\mu bc}
=\frac{a+b}{\mu abc}
=\frac RK.
\tag{12}
\]

再加 \(1/(pK)\)，利用 \(pR+1=4K\) 即得 \(4/p\)。

## 3. 与完整中心指数盒的等价性

若完整分解写成

\[
K=\prod_i q_i^{e_i},
\tag{13}
\]

一个中心 hit \(\prod_iq_i^{z_i}\equiv-1\pmod R\)、
\(-e_i\le z_i\le e_i\) 可取

\[
u=\prod_iq_i^{\max(z_i,0)},\qquad
v=\prod_iq_i^{\max(-z_i,0)}.
\tag{14}
\]

于是 (2) 成立。反过来，(2) 中 \(uv\mid K\) 和 \((u,v)=1\) 保证：在 (13) 的素数坐标上，
\(u\) 的指数减去 \(v\) 的指数构成一个范围内的 \(z\)，并且
\(u/v\equiv-1\pmod R\)。因此 (2) 与 center box hit 在存在性意义下等价。

关键差别是 verification direction：完整指数向量需要已知全部 \((q_i,e_i)\)，而 pair receipt
只检查 \(uv\mid K\)。这使 raw complete-excess H4 target 可在建立完整 typed target state
之前先尝试直接 terminal-first dispatch。

## 4. 两个聚焦控制

| control | \(p,R,K\) | \((u,v)\) | \((\mu,c,h)\) | \(d_0,d_{\mathrm{cert}}\) | 三个分母 |
|---|---|---|---|---|---|
| nontrivial multiplier | \(73,3,55\) | \(1,5\) | \(2,11,15\) | \(11,44\) | \(22,110,4015\) |
| full-excess sink pair | \(73,23,420\) | \(2,21\) | \(1,10,7\) | \(40,10\) | \(20,210,30660\) |

第一行确保 serializer 不只覆盖 \(\mu=1\) 的 sink 情形；第二行复核
`type-I-formal-full-excess-cycle-or-hit-reduction` 中的中心 hit 构造。复现器还拒绝一个
\(uv\mid K\) 但不满足反足同余的负控制。

```bash
python3 reproductions/type_i_factorization_free_centered_pair_terminal.py --verify
```

## 5. 对 H4 闭包的作用与边界

这条结果缩小的是 H4 atomic target 的一个**终端序列化**缺口：完整 complete-excess block
可以由 gcd 与模幂重算，却可能尚未有实际可用的完整 factorization；若此时搜索或构造给出
\((u,v)\)，仍可直接输出 (7)，无需等待 F/G/hit 全纤维对象。

它没有给出如何对任意 raw target 找到该 pair，也没有证明任意 actual H4 target 存在 pair。
更不改变递归 state 的 `K_context`、F/G 分离角色、canonical Fourier witness、signed defect、
source provenance、solution lift 或 E1--E5 的要求。没有 pair 的 target 仍必须回到完整 typed
classification 和 atomic-admission 路径。因此这是 T1 的 terminal-first branch 增强，不是 T1
或全局 selector 的证明。
