---
kind: claim
claim_id: four-divisible-nonstandard-source-lift-obstruction
title: 4 的倍数非标准平方尾源解不能作单项提升
statement: 设 p=1 mod24 为素数、4<=n<p 且 4|n。对源解 4/n=1/a+1/b+1/c，其中 a=n/4+1、b=(n/4+1)^2、c=(n/4)(n/4+1)^2，不存在保留任意两个源分母、只替换第三个分母而得到 4/p 的正整数提升。
claim_status: established
topics:
- descent
- lifting-obstruction
- nonstandard-source
- unit-fractions
- proof-program
sources:
- paper: subramanian2026
  locator: "Equation (2.1)"
  role: nonstandard-source-identity
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: equation-and-parameterization-context
visibility: public
last_checked: '2026-07-24'
---

# \(4\mid n\) 非标准平方尾源解不能作单项提升

## 定理

设

\[
p\equiv1\pmod{24},\qquad 4\le n<p,\qquad 4\mid n.
\]

写 \(n=4t\)，并令

\[
a=t+1,\qquad b=(t+1)^2,\qquad c=t(t+1)^2. \tag{1}
\]

则

\[
\frac4n=\frac1a+\frac1b+\frac1c, \tag{2}
\]

但不能保留其中任意两个分母、只替换剩余一个分母而得到 \(4/p\) 的正整数解。

## 证明

由 (1)，

\[
\frac1a+\frac1b+\frac1c
=\frac1{t+1}+\frac1{(t+1)^2}+\frac1{t(t+1)^2}
=\frac1t=\frac4n,
\]

故 (2) 是有效源解。记

\[
r=p-n=p-4t.
\]

因 \(p\equiv1\pmod4\)，有

\[
r\equiv1\pmod4. \tag{3}
\]

若替换源分母 \(w\)，two-denominator-lift-criterion 给出必要条件

\[
D_w=np-4rw>0,\qquad D_w\mid npw. \tag{4}
\]

### 替换平方尾 \(b\)

\[
D_b=4\bigl(4t^2-r(t^2+t+1)\bigr). \tag{5}
\]

若 \(r\ge5\)，括号内为负，故只须考虑 \(r=1\)。此时 \(p=4t+1\)，又
\(p\equiv1\pmod{24}\)，所以 \(6\mid t\)。令

\[
F=3t^2-t-1;
\]

则 \(D_b=4F\)，而 (4) 要求

\[
F\mid tp(t+1)^2. \tag{6}
\]

但

\[
\gcd(F,t)=1,\qquad
\gcd(F,t+1)\mid3,\qquad
F\equiv-1\pmod3. \tag{7}
\]

并且由 \(p=4t+1\)，在模 \(p\) 下有

\[
16F=48t^2-16t-16\equiv-9\pmod p. \tag{8}
\]

因为 \(p>3\)，这给出 \(\gcd(F,p)=1\)。由 (7) 可知 \(F\) 与 (6) 右侧互素，
因而 \(F=1\)；但 \(t\ge6\) 时 \(F>1\)，矛盾。

### 替换平方尾 \(c\)

\[
D_c=4t^2\bigl(4-r(t+2)\bigr). \tag{9}
\]

若 \(r\ge5\)，右侧显然为负。若 \(r=1\)，如上 \(6\mid t\)，故同样为负。
这违反 (4) 的正性。

### 替换首项 \(a\)

\[
D_a=4E,\qquad E=4t^2-r=4t(t+1)-p. \tag{10}
\]

若 \(E\le0\)，结论已成立。以下设 \(E>0\)。由 (4) 及 \(a=t+1\)，得到

\[
E\mid tp(t+1). \tag{11}
\]

另一方面，

\[
\gcd(E,t)=\gcd(r,t)=1,\qquad
\gcd(E,p)=\gcd(4t(t+1),p)=1, \tag{12}
\]

其中 \(p>t+1\)。故 (11) 强制 \(E\mid t+1\)。代入 (10) 即有

\[
p=4t(t+1)-E\equiv0\pmod E.
\]

然而 \(0<E\le t+1<p\)，这不可能与 \(p\) 为素数兼容。三种替换均不可能，定理得证。

## 含义

Subramanian 2026 的偶数源恒等式在 \(4\mid n\) 的细分上有不同于标准重复尾
\((n/2,n,n)\) 的平方尾结构。该结构也没有产生二分母保留的单项提升，因而不能作为
核心类的递降边。此结论只排除这种固定源解与一个坐标替换的机制；一分母保留、因子标记
或多坐标耦合重组仍是未解决的正向空间。
