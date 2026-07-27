---
kind: claim
claim_id: type-II-gap-seventy-one-tail-descent-family
title: m=23 mod24 的显式 Type II 双尾递降同余族
statement: 设 m=24r-1，且素数 p=(m+1)t+1，其中 t=-145 modm。令 x=(p+m)/4、d=36，则 d|x^2 且 d=-x modm，故为 Type II 证书；又m+1|p-1，故两条 p-尾可同时去 p，严格递降至 n=(p+m)/(m+1)=t+1。m=71、p=5112u+4897 是 r=3 的特例。
claim_status: established
topics:
- type-II
- descent
- congruence-certificate
- explicit-family
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# \(m\equiv23\pmod{24}\) 的显式 Type II 双尾递降同余族

设 \(m=24r-1\)，并令

\[
p=(m+1)t+1,\qquad t\equiv-145\pmod m. \tag{1}
\]

若 \(p\) 为素数，则 \(p\equiv1\pmod {24}\)。写

\[
x=\frac{p+m}{4}=6r(t+1).
\]

所以 \(36\mid x^2\)。又 \(6r=(m+1)/4\equiv4^{-1}\pmod m\)，故由 (1)

\[
x\equiv4^{-1}(-144)\equiv-36\pmod m.
\]

于是 \(d=36\) 满足 \(d\mid x^2\) 且 \(d\equiv-x\pmod m\)，给出 Type II 证书。
同时 \(m+1\mid p-1\)，故双尾去 \(p\) 严格递降至 \(n=t+1\)。

## \(m=71\) 特例

取 \(r=3\)，即 \(m=71\)。此时

\[
p=5112u+4897=72t+1,\qquad t=71u+68.
\]

取 \(m=71\)，则

\[
x=\frac{p+71}{4}=18(t+1).
\]

因此 \(36\mid x^2\)。又因 \(t\equiv68\pmod {71}\)，

\[
x\equiv18\cdot69\equiv35\pmod {71},
\qquad 36\equiv-35\equiv-x\pmod {71}.
\]

故 \(d=36\) 是缺口 \(71\) 的 Type II 除子，给出 \(4/p\) 的显式 Type II
证书。另一方面 \(72=m+1\mid p-1\)，所以 Type II 双尾去 \(p\) 引理适用，源分母为

\[
n=\frac{p+m}{m+1}=\frac{p+71}{72}=t+1<p.
\]

该特例解释了 16,384 层审计中 \(p=5\,771\,131\,031\,426\,401\) 的 \(m=71\) 命中。
它也是更一般的 [\(q^2\) 因子 Type II 双尾递降族](type-II-factor-square-tail-descent-family.md)
在 \((q,d)=(18,36)\) 时的特例；一般族仍只覆盖显式算术进程，不能替代跨缺口选择器。
