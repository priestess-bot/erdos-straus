---
kind: claim
claim_id: type-I-three-p-plus-four-external-descent-bridge
title: 3p+4 内部 Type I 证书的外部源递降桥
statement: >-
  设核心素数 p 有 3p+4 内部 (A,B)=(4,3) Type I 证书，亦即 m|3p+4、
  m=-p (mod 48)，并令 C=(p+m)/48、q=(36C+1)/m。则 q=3 (mod 4)、
  (3p+4)/m=4q-3，且 q+1|(p-1) 当且仅当 q+1|84C。该整除门成立时，令
  k=(q+1)/4、n=(qp+1)/(q+1)、M=kn、e=9C，则 e|M^2、e<=M、e=-M (mod q)，
  并给出显式标记提升 (M,u,v)->(Mp,u,v)，其中 u=12C、v=Mu/e。它恢复原
  Type I 证书 (m,D)=(m,16C)，且 n<p。p=2521,m=23 是正控制，给出 k=21、
  n=2491；p=4729,m=23 满足直接证书却失败整除门，故该桥不是全部 3p+4 证书的
  自动升级。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - three-p-plus-four-internal-type-I-certificate
  - quadratic-factor-external-source-descent
  - marked-solution-descent-closure
topics:
  - type-I
  - internal-certificate
  - external-source
  - marked-descent
  - two-tail-lift
  - integrality-gate
  - double-G
  - proof-program
sources:
  - claim: three-p-plus-four-internal-type-I-certificate
    role: direct-internal-Type-I-normal-form
  - claim: quadratic-factor-external-source-descent
    role: complete-external-source-tail-parameterization
  - reproduction: reproductions/type_i_three_p_plus_four_external_descent_bridge.py
    role: exact-positive-and-negative-bridge-controls
visibility: public
last_checked: '2026-08-12'
---

# \(3p+4\) 内部 Type I 证书的外部源递降桥

## 1. 内部证书的固有外部参数

设 \(p\equiv1\pmod {24}\) 为素数，并有

\[
m\mid3p+4,
\qquad
m\equiv-p\pmod {48}.
\tag{1}
\]

令

\[
C=\frac{p+m}{48},
\qquad
q=\frac{36C+1}{m}.
\tag{2}
\]

式 (2) 的 \(q\) 自动为正整数。事实上 \(p=48C-m\)，所以

\[
3p+4=144C-3m+4=4(36C+1)-3m.
\tag{3}
\]

由 (1) 的 \((m,4)=1\)，可知 \(m\mid36C+1\)。又 \(36C+1\equiv1\pmod4\)、
\(m\equiv3\pmod4\)，所以

\[
q\equiv3\pmod4,
\qquad
\frac{3p+4}{m}=4q-3.
\tag{4}
\]

原内部 Type I certificate 是

\[
x=12C,
\qquad
D=16C.
\tag{5}
\]

## 2. 精确的外部源门

**定理。** 由 (1) 导出的 \(q\) 能作为对应的外部源模数，即

\[
k=\frac{q+1}{4}\mid\frac{p-1}{4},
\tag{6}
\]

当且仅当

\[
\boxed{q+1\mid84C.}
\tag{7}
\]

在这个门成立时，设

\[
n=\frac{qp+1}{q+1},
\qquad
M=kn,
\qquad
e=9C,
\qquad
u=12C,
\qquad
v=\frac{Mu}{e}.
\tag{8}
\]

则

\[
e\mid M^2,
\qquad
e\le M,
\qquad
e\equiv-M\pmod q,
\tag{9}
\]

并有两个显式恒等式

\[
\boxed{
\frac4n=\frac1M+\frac1u+\frac1v,
\qquad
\frac4p=\frac1{Mp}+\frac1u+\frac1v.
}
\tag{10}
\]

因此令

\[
W_{p,m}=\{(M,u,v)\}\subseteq\operatorname{Sol}(n),
\tag{11}
\]

就得到不读取目标解的标记提升

\[
\Phi_{p,m}:W_{p,m}\longrightarrow\operatorname{Sol}(p),
\qquad
(M,u,v)\longmapsto(Mp,u,v),
\tag{12}
\]

且 \(n<p\)。它重建的 Type I 证书正是 (5)，而不是一个不同的 terminal。

## 3. 证明

由 \(qm=36C+1\)，模 \(q+1\) 有

\[
m\equiv-36C-1\pmod {q+1}.
\tag{13}
\]

代入 \(p-1=48C-m-1\) 得

\[
p-1\equiv84C\pmod {q+1}.
\tag{14}
\]

所以 \(q+1\mid p-1\) 与 (7) 等价；再用 \(q\equiv3\pmod4\)，这又等价于
(6)。此时 (8) 中 \(n,M\) 都是整数，且 \(4M=qp+1\)。

由 (3)--(4)，

\[
qp+1
=q(48C-m)+1
=48qC-(36C+1)+1
=12C(4q-3),
\]

从而

\[
M=3C(4q-3).
\tag{15}
\]

于是 \(e=9C\) 满足

\[
M\equiv-9C=-e\pmod q,
\qquad
e\mid9C^2(4q-3)^2=M^2,
\qquad
e\le M.
\]

而

\[
\frac{M+e}{q}
=\frac{3C(4q-3)+9C}{q}
=12C=u,
\tag{16}
\]

所以 `quadratic-factor-external-source-descent` 直接给出 (10)。同时

\[
\frac{4e+1}{q}=\frac{36C+1}{q}=m,
\qquad
\frac{u^2}{e}=\frac{144C^2}{9C}=16C=D.
\tag{17}
\]

因此外部源证书与原内部证书逐项相同。最后 \(q>0\) 给

\[
n=\frac{qp+1}{q+1}<p.
\]

## 4. 正控制与严格边界

对双 G 控制 \(p=2521\)、\(m=23\)，有

\[
C=53,
\quad q=83,
\quad q+1=84\mid2520,
\quad k=21,
\quad n=2491,
\quad M=52311,
\quad e=477.
\]

于是

\[
\frac4{2491}=\frac1{52311}+\frac1{636}+\frac1{69748}
\longmapsto
\frac4{2521}=\frac1{131876031}+\frac1{636}+\frac1{69748}.
\tag{18}
\]

其 \((m,D)=(23,848)\) 正是 \(3p+4=23\cdot329\) 的内部 Type I
certificate。故该双 G 点除已有 gap-23 Type II terminal 外，还有一条独立的严格
marked descent。

这个升级不是自动的。对 \(p=4729\)、\(m=23\)，仍有 (1)，但

\[
C=99,
\qquad q=155,
\qquad (p-1)\bmod(q+1)=48.
\tag{19}
\]

所以其直接 Type I certificate 不能沿本卡的固有 \(q\) 变成合法外部源递降。该例
不排除另一种 \(k\) 或另一种提升，只精确划定了本桥的范围。

聚焦验证：

~~~bash
python3 reproductions/type_i_three_p_plus_four_external_descent_bridge.py --verify
~~~
