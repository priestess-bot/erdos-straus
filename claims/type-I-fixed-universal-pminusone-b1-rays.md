---
kind: claim
claim_id: type-I-fixed-universal-pminusone-b1-rays
title: 核心素数的九条固定 p 减一 B 等于一因子射线
statement: 对每个核心素数 p=24t+1，E 属于 {4,8,12,16,24,36,48,72,144} 时均有 E|(p-1)^2/4。令 R=E-1、K=(pR+1)/4；若 K 有因子 C 满足 4C=-1 mod R，则 A=(K/C+1)/R、m=(4C+1)/R 给出 B=1 的 Type I 正规形，且以 n=p-1、桥因子 E 给出严格上半区偶终端桥。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- p-minus-one
- terminal-bridge
- factorization
- divisor-residue
- fixed-ray
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 核心素数的九条固定 (p-1) (B=1) 因子射线

令

\[
p=24t+1,
\qquad
E\in\{4,8,12,16,24,36,48,72,144\},
\qquad R=E-1.
\]

这些 (E) 正是 (144) 中可被 (4) 整除的正因子。因此

\[
E\mid144t^2=\frac{(p-1)^2}{4}. \tag{1}
\]

对每个这样的 (E)，令

\[
K=\frac{pR+1}{4}.
\]

若 (K) 有一个正因子 (C) 满足

\[
4C\equiv-1\pmod R, \tag{2}
\]

则令 (H=K/C)，并定义

\[
A=\frac{H+1}{R},
\qquad
m=\frac{4C+1}{R}. \tag{3}
\]

由 (4K\equiv1\pmod R) 与 (2)，有 (H\equiv-1\pmod R)，所以 (3) 为整数；并且

\[
p=4AC-m,
\qquad
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK}. \tag{4}
\]

式 (1) 正是 (p-1) 源状态的平方条件。更直接地，令

\[
n=p-1.
\]

则

\[
\frac{4K-E}{R}=\frac{pR+1-(R+1)}R=p-1=n. \tag{5}
\]

又 (E\mid4K^2)、(E\equiv1\pmod R)，而 (p\ge73) 时 (E<2K)。故最大尾可反向替换，且

\[
\frac4n=\frac1{nK/E}+\frac1{AC}+\frac1{ACH}. \tag{6}
\]

这里 (n=p-1\ge(p+1)/2) 为偶数，因而 (4)--(6) 是严格上半区偶源的 (B=1) Type I
终端桥。它正是 [(p-1) 的 (B=1,2) 除子剩余类选择器](type-I-pminusone-b12-divisor-residue-selector.md)
在九个对所有核心素数均可用的 (E) 上的显式有限菜单。

## (R=3) 与 \((3p+1)/4\) 分支

取 (E=4,R=3) 时

\[
K=\frac{3p+1}{4}.
\]

条件 (2) 是 (C\equiv2\pmod3)。由于 (K\equiv1\pmod3)，它成立当且仅当 (K)
有一个素因子 (q\equiv2\pmod3)：一个方向取 (C=q)，另一方向把 (C) 的素因子分解
模 (3) 即可。这正是
[\((3p+1)/4\) 因子桥](type-I-three-p-plus-one-b1-upper-bridge.md)的因子条件，但这里给出更短的
偶终端源 (n=p-1)，桥因子固定为 (E=4)。

这九条射线只是固定有限菜单，不能推出每个核心素数都命中。固定菜单可以有无穷逃逸；其用途是将
全称问题的困难集中到菜单共同残余的自适应源选择上。

~~~bash
python3 reproductions/type_i_fixed_pminusone_ray_pressure_profile_600m.py
python3 -m unittest tests.test_type_i_fixed_pminusone_ray_pressure_profile_600m -q
~~~
