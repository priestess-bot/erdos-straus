---
kind: claim
claim_id: five-mod-eight-nonstandard-source-lift-obstruction
title: 5 mod 8 非标准双尾源解不能作单项提升
statement: 设 p=1 mod24 为素数、5<=n<p 且 n=5 mod8。对源解 4/n=1/a+1/b+1/c，其中 a=(n+3)/4、b=n(n+3)/8、c=2b，不存在保留任意两个源分母、只替换第三个分母而得到 4/p 的正整数提升。
claim_status: established
topics:
- descent
- lifting-obstruction
- nonstandard-source
- unit-fractions
- proof-program
sources:
- paper: subramanian2026
  locator: "Equation (2.12)"
  role: nonstandard-source-identity
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: equation-and-parameterization-context
visibility: public
last_checked: '2026-07-24'
---

# \(5\pmod8\) 非标准双尾源解不能作单项提升

## 定理

设

\[
p\equiv1\pmod{24},\qquad 5\le n<p,\qquad n\equiv5\pmod8,
\]

并令

\[
a=\frac{n+3}{4},\qquad b=\frac{n(n+3)}8,\qquad c=2b. \tag{1}
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
=\frac4{n+3}+\frac8{n(n+3)}+\frac4{n(n+3)}
=\frac4n,
\]

故 (2) 是有效源解。记 \(r=p-n\)。由 \(p\equiv1\pmod8\) 及
\(n\equiv5\pmod8\)，有

\[
r\equiv4\pmod8,\qquad r\ge4. \tag{3}
\]

若替换源分母 \(w\)，two-denominator-lift-criterion 给出必要条件

\[
D_w=np-4rw>0,\qquad D_w\mid npw. \tag{4}
\]

### 替换两个大尾

对 \(b\)，

\[
D_b=np-\frac{rn(n+3)}2
=n\left(p-\frac{r(n+3)}2\right). \tag{5}
\]

而

\[
r(n+3)-2p=(r-2)n+r>0,
\]

所以 \(D_b<0\)。对 \(c\)，

\[
D_c=np-rn(n+3)=n\bigl(p-r(n+3)\bigr)<0, \tag{6}
\]

因为 \(r(n+3)-p=(r-1)n+2r>0\)。这两种替换均违反 (4) 的正性。

### 替换首项

此时

\[
D_a=np-r(n+3)=n^2-3r. \tag{7}
\]

若 \(D_a\le0\)，结论已成立。以下设 \(D_a>0\)。由 (3) 和 \(n^2\equiv1\pmod8\)，

\[
D_a\equiv5\pmod8, \tag{8}
\]

所以 \(D_a\) 为奇数且大于 \(3\)。又 \(p>n+3\)，并且

\[
\gcd(D_a,p)=1,\qquad
\gcd(D_a,n)\mid3,\qquad
\gcd(D_a,n+3)\mid3. \tag{9}
\]

这里第一式使用 \(D_a\equiv n(n+3)\pmod p\)；后二式分别由
\(D_a\equiv-3r\pmod n\) 和 \(D_a\equiv-3p\pmod{n+3}\) 得到。

若 \(3\mid D_a\)，则由 (7) 有 \(3\mid n\)。写 \(n=3s\)，并用
\(r\equiv p\equiv1\pmod3\)，得到

\[
D_a=3(3s^2-r),\qquad 3\nmid(3s^2-r). \tag{10}
\]

因此 \(D_a\) 与 \(np(n+3)/4\) 的公因子至多为 \(3\)。但 (4) 和
\(a=(n+3)/4\) 要求 \(D_a\mid np(n+3)/4\)，这与 (8) 矛盾。三种替换均不可能。

## 含义

这条障碍处理的是 \(n\equiv5\pmod8\) 的全部 Subramanian 双尾源，而不是只处理
最近的 \(n=p-4\) 实例。故用已知 \(5\pmod8\) 恒等式作为较小无条件源，再保留两个
分母进行单项提升，也不能产生当前目标所需的递降边。它仍不排除一分母保留、带因子标记，
或多坐标耦合重组。
