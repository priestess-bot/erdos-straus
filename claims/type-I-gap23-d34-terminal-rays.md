---
kind: claim
claim_id: type-I-gap23-d34-terminal-rays
title: gap 23 的 d=34 Type I 终端射线
statement: 设 p=24h+1 为核心素数。若 17|(h+1) 且 (h+1)^2=2 (mod 23)，则 gap m=23、x=6(h+1)、d=34 是直接 Type I 除子证书，显式给出 4/p=1/x+1/y+1/z。条件等价于 h=50 或 339 (mod 391)，故 p=1201+9384t 或 p=8137+9384t；两条进程均与其步长互素，因而各含无穷多个素数参数，全部直接终止。第一条射线包含 R=11/gap-7/gap-11 联合 dispatch 的控制残余 p=1201。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-I-r11-gap7-gap11-terminal-descent-dispatch
topics:
  - type-I
  - terminal-first
  - gap-twenty-three
  - dirichlet-ray
  - short-certificate
  - R11
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: Type-I-divisor-reconstruction
  - claim: type-I-r11-gap7-gap11-terminal-descent-dispatch
    role: p1201-joint-residual-control
  - reproduction: reproductions/type_i_gap23_d34_terminal_rays.py
    role: symbolic-and-Dirichlet-ray-controls
visibility: public
last_checked: '2026-08-12'
---

# gap \(23\) 的 \(d=34\) Type I 终端射线

## 1. 一个固定除子模板

令

\[
p=24h+1,
\qquad
s=h+1,
\qquad
m=23,
\qquad
x=\frac{p+m}{4}=6s.
\tag{1}
\]

考虑固定 Type I 除子

\[
d=34=2\cdot17.
\tag{2}
\]

**定理。** 若

\[
17\mid s,
\qquad
s^2\equiv2\pmod {23},
\tag{3}
\]

则 \(d\mid x^2\) 且

\[
23\mid px+d.
\tag{4}
\]

所以这是原始 \(p\) 的 Type I terminal。精确分母为

\[
\boxed{
y=\frac{px+34}{23},
\qquad
z=\frac{p(x+px^2/34)}{23},
\qquad
\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{5}
\]

**证明。** 第一条件使 \(34\mid x=6s\)，故 \(34\mid x^2\)。又模 \(23\) 下有

\[
p=24h+1\equiv h+1=s,
\qquad
x=6s,
\qquad
34\equiv11.
\tag{6}
\]

于是

\[
px+34\equiv6s^2+11\equiv6\cdot2+11=23\equiv0\pmod {23}.
\tag{7}
\]

因此 (4) 是完整的 Type I 除子条件。式 (5) 正是该条件的标准分母恢复；也可直接将
\(y,z\) 代回核验。证毕。

## 2. 两条 primitive Dirichlet 射线

模 \(23\) 的平方根满足

\[
s\equiv\pm5\pmod {23}.
\tag{8}
\]

把它与 \(s\equiv0\pmod {17}\) 合并，得到

\[
h\equiv50\quad\hbox{或}\quad339\pmod {391}.
\tag{9}
\]

相应的素数参数进程为

\[
\boxed{
p=1201+9384t
\quad\hbox{或}\quad
p=8137+9384t,
\qquad t\ge0.}
\tag{10}
\]

而

\[
\gcd(1201,9384)=\gcd(8137,9384)=1.
\tag{11}
\]

Dirichlet 定理保证每条进程含无穷多个素数；其中每个核心素数参数满足 (3)，因而由
(5) 直接终止。这里没有断言固定 \(t\) 值必为素数。

## 3. 联合残余中的控制点

第一条射线的 \(t=0\) 是

\[
p=1201,
\qquad h=50,
\qquad s=51,
\qquad x=306.
\tag{12}
\]

式 (5) 给出

\[
\boxed{
\frac4{1201}
=\frac1{306}+\frac1{15980}+\frac1{172727820}.}
\tag{13}
\]

该点此前同时逃过 R=11 固定尾、gap 7 与 gap 11 的联合 dispatch；(13) 说明那个
共同残余不是原始 \(p\) 的 terminal-free 证据。该定理只关闭 (9) 的两条显式子射线，
不声称覆盖整个联合残余。

复现：

```bash
python3 reproductions/type_i_gap23_d34_terminal_rays.py --verify
```
