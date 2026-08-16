---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-fresh-q-ac-fan-bounded-intersection
title: H4 fresh q-carrier 与固定 AC/Chamberland 扇的有界公共因子障碍
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 receipt 中，令
  q=((p+1)/2)/d4>1，d4=gcd((p+1)/2,M4)，并令 S 为有限个 AC 参数对 (A,C)。记
  N_(A,C)=p+4A^2C，C_S=product_(A,C in S)(4A^2C-1)。则
  gcd(q,product_(A,C in S) N_(A,C))=gcd(q,C_S)，故 fixed fan 与 q 的全部共同因子
  由一个与 p 无关的常数限制。特别地，若同一条 AC 因子 h=4ACK-1 同时满足 h|q 与
  h|N_(A,C)，则 h|4A^2C-1，进而 K<=A。对盒 1<=A,C<=B，任何这样直接 q-carried
  的因子都满足 K<=B、h<=4B^3-1。actual H3-to-H4 provenance 还给
  d4<=1535，故 q> C_S 时 q 不整除该 fixed fan 的移位积；具体地 p>3070 C_S-1
  已足够。该障碍只排除将 fresh q 本身或其无界部分直接作为固定 AC/Chamberland 扇的
  因子来源；它不排除不整除 q 的 AC 因子、Chamberland 的因子重选，或任何全局证书/递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
  - chamberland-ac-ray-translation
  - type-II-raw-ray-certificate
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - fresh-carrier
  - ac-rays
  - chamberland
  - divisor-intersection
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: actual-fresh-q-carrier-and-q-scale
  - claim: type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
    role: actual-H3-to-H4-bound-d4-divides-Delta-at-most-1535
  - claim: chamberland-ac-ray-translation
    role: AC-factor-and-Chamberland-translation-boundary
  - claim: type-II-raw-ray-certificate
    role: direct-AC-factor-to-certificate-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_fresh_q_ac_fan_bounded_intersection.py
    role: focused-fixed-fan-gcd-and-q-carried-factor-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 fresh \(q\)-carrier 与固定 AC 扇的有界公共因子障碍

## 1. 适用域和要排除的桥接方式

保留 actual q=1 high \(C=2\) 19-phase H4 proper-overlap top-capacity
\(a_{\rm alt}=1\) receipt 的记号：

\[
w=\frac{p+1}{2},\qquad d_4=(w,M_4),\qquad q=\frac w{d_4}>1.
\tag{1}
\]

于是

\[
p\equiv-1\pmod q.
\tag{2}
\]

actual H3 \(\Rightarrow\) H4 provenance 还给

\[
d_4\mid\lvert1536-a(p)\rvert\le1535,
\qquad
q=\frac{p+1}{2d_4}\ge\frac{p+1}{3070}.
\tag{3}
\]

本卡只研究一个很窄的接口：H4 注入的 \(q\)-carrier 能否直接为一组**固定**
AC/Chamberland 射线提供其因子。它不把 \(q\) 误作所有 Type II 证书的来源。

令 \(\mathcal S\) 是任意有限个正整数对 \((A,C)\)，并定义

\[
N_{A,C}(p)=p+4A^2C,
\qquad
P_{\mathcal S}(p)=\prod_{(A,C)\in\mathcal S}N_{A,C}(p),
\qquad
C_{\mathcal S}=\prod_{(A,C)\in\mathcal S}(4A^2C-1).
\tag{4}
\]

这里 \(N_{A,C}\) 正是 AC 射线的因子整数；成功因子满足
\(h=4ACK-1\mid N_{A,C}\)。

## 2. 固定扇与 \(q\) 的精确交集

**引理 1（fixed-fan intersection）。** 在 (1) 的域内，

\[
\boxed{
\gcd\bigl(q,P_{\mathcal S}(p)\bigr)
=\gcd\bigl(q,C_{\mathcal S}\bigr).
}
\tag{5}
\]

**证明。** 由 (2)，逐项有

\[
N_{A,C}(p)=p+4A^2C\equiv4A^2C-1\pmod q.
\tag{6}
\]

将 (6) 在有限积中相乘，得到
\(P_{\mathcal S}(p)\equiv C_{\mathcal S}\pmod q\)。与 \(q\) 取 gcd
即为 (5)。\(\square\)

因此 fixed fan 从 \(q\) 中可复用的全部素因子及其高度，都被与 \(p\) 无关的
\(C_{\mathcal S}\) 限制。尤其当

\[
p>3070C_{\mathcal S}-1,
\tag{7}
\]

时，(3) 给出 \(q>C_{\mathcal S}\)，从而

\[
q\nmid P_{\mathcal S}(p).
\tag{8}
\]

所以在足够大的 actual H4 receipt 中，整个 fresh \(q\)-carrier 不可能被任何固定
AC 扇的这些移位数完全吸收。

## 3. 直接 \(q\)-carried AC 因子的 \(K\) 也有界

设一条 AC 射线的同一因子满足

\[
h=4ACK-1,
\qquad h\mid q,
\qquad h\mid p+4A^2C.
\tag{9}
\]

由 (6)，

\[
h\mid4A^2C-1.
\tag{10}
\]

另一方面 \(h=4ACK-1>0\)，故 (10) 强制

\[
4ACK-1\le4A^2C-1,
\qquad\boxed{K\le A.}
\tag{11}
\]

这不是对所有 AC 射线的 \(K\) 界；它只针对**显式复用 H4 的 \(q\)** 的同一因子。
但它说明这种桥接无法承载有界 \((A,C)\) 扇中一般允许增长的 \(K\)。例如在
\(1\le A,C\le B\) 的盒内，(11) 给出

\[
K\le A\le B,
\qquad h\le4A^2C-1\le4B^3-1.
\tag{12}
\]

故所有直接 q-carried 候选都落入一个与 \(p\) 无关的有限因子菜单。

## 4. 边界而非全局出口

这个结论刻意保留以下可能性：

1. \(p+4A^2C\) 可以有完全不整除 \(q\) 的合格 AC 因子；
2. Chamberland 形状在有序化时可以重选因子，不能把原因子标签静默保持；
3. 一个小的 \(q\)-因子确实可能给出短证书。例如局部 H4 算术控制
   \(p=241,q=121\) 有 \(h=11=4\cdot1\cdot3\cdot1-1\)，且
   \(11\mid q\) 与 \(11\mid p+4\cdot1^2\cdot3=253\)。这正好满足
   \(K=A=1\)；再由 \(B=(Kp+A)/h=22\ge A\)、
   \(p=4ABC-(A+B)/K\)，它确实恢复一张 AC Type II 证书，与 (11) 一致。

因此本卡不是 AC 射线猜想的反例，更不是 global G/Type I exit。它只给出一个可复用的
stop route：任何试图把 H4 的 growing fresh \(q\)-carrier **直接**接到固定 AC 扇的证明，
必须另外解释如何越过 (5)、(11) 的固定公共因子界；否则该桥接没有新增的全称力量。

## 5. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_fresh_q_ac_fan_bounded_intersection.py --verify
```

回执只重放两个既有 local H4 arithmetic fixtures 上的 \(3\times3\) fixed fan：
\(p=73,q=37\) 的交集为 \(1\)，\(p=241,q=121\) 的交集为 \(11\)，并逐项验证
\(h=11\) 的 direct q-carried AC 因子与 \(K\le A\)。它不扫描素数、分母或 Reach history，
也不把 local fixture 误称为 actual H3 predecessor。
