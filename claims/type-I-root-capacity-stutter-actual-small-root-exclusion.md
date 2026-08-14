---
kind: claim
claim_id: type-I-root-capacity-stutter-actual-small-root-exclusion
title: 根容量实际 stutter 的低系数障碍与 30p 高度排除带
statement: >-
  对核心素数 p≡1 mod24 的真实 maximal complete-excess proper-root receipt，设
  h=3u、2≤h<p、h|(p^2+p+1)，且已经通过 terminal-first 分流。若剩余 canonical
  carry 发生 stutter，即 D≡1-h (mod p)，并定义 m=(D+h-1)/p、a=em-h，则
  m≥3、a(m-1)≥30，且 h^2>30p。因此在 h^2≤30p 的实际根端点，terminal-first
  之后 canonical carry 必为算术严格；本结论只关闭这条 arithmetic stutter 门，不单独给出
  E1--E5、Type I/II 证书、解提升或全局良基势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-pair-root-divisor-gate
  - type-I-root-capacity-stutter-positive-definite-norm-bound
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - complete-excess
  - cyclotomic
  - congruence
  - strict-carry
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-root-receipt-terminal-first-and-stutter-gate
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-cyclotomic-exclusion-for-D
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-parameter-identities
  - claim: type-I-root-capacity-stutter-pair-root-divisor-gate
    role: root-divisor-finite-low-coefficient-gate
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-square-root-menu-bound
  - reproduction: reproductions/type_i_root_capacity_stutter_actual_small_root_exclusion.py
    role: fixed-actual-receipt-low-coefficient-and-defect-controls
visibility: public
last_checked: '2026-08-14'
---

# 根容量实际 stutter 的低系数障碍与 \(30p\) 高度排除带

## 1. 设置与结论

固定核心素数

\[
p\equiv1\pmod {24},\qquad
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u.
\tag{1}
\]

考虑一个真实 maximal complete-excess 的 proper-root receipt，并假设

\[
2\le h<p,\qquad h\mid p^2+p+1.
\tag{2}
\]

先执行 terminal-first；以下只讨论 \(R-h\nmid K\) 的剩余 carry。令其实际除子为
\(D\)。若唯一非严格门命中，写成

\[
D\equiv1-h\pmod p,\qquad D\mid ph+1,
\tag{3}
\]

并置

\[
m=\frac{D+h-1}{p},\qquad
e=\frac{ph+1}{D},\qquad
a=em-h.
\tag{4}
\]

则

\[
\boxed{m\ge3,\qquad a(m-1)\ge30,\qquad h^2>30p.}
\tag{5}
\]

所以只要 \(h^2\le30p\)，(3) 不可能在实际 receipt 中发生；终端分流失败后，
canonical cofactor 必落在严格范围 \(c\le p-2\)。

## 2. 真实 receipt 排除 \(m=1\)

令 \(P=p^2+p+1=3M_0\)。实际根回执的 cyclotomic 排除给出

\[
(D,M_0)=1.
\tag{6}
\]

又因为 \((h,D)=1\) 且 \(3\mid h\)，有 \(3\nmid D\)。故

\[
\boxed{(D,P)=1.}
\tag{7}
\]

三参数恒等式给出

\[
D=mp+1-h,\qquad eD=ph+1,
\tag{8}
\]

从而

\[
D(p+e)=mp^2+p+1.
\tag{9}
\]

若 \(m=1\)，则 \(D\mid P\)。结合 (7) 得 \(D=1\)，再由 (8) 得 \(h=p\)，
这与 (2) 矛盾。因此 \(m\ge2\)。另一方面，\(ph+1\equiv1\pmod3\)，所以
\(3\nmid D\)；而由 (8) 又有

\[
D\equiv m+1\pmod3.
\tag{10}
\]

于是 \(m\not\equiv2\pmod3\)。配合 \(m\ge2\)，得到

\[
\boxed{m\ge3.}
\tag{11}
\]

这一步必须保留 actual receipt：仅有抽象 stutter 等式时，\(m=1\) 可与
\(D\mid P\) 同时出现；其被排除正是因为真实 root 的 (7)。

## 3. Actual parity 与五个低系数对的 root-divisor 排除

从 \(D=mp+1-h\)、\(Da=m+h(h-1)\) 模 3 化简，得到

\[
(m+1)a\equiv m\pmod3.
\tag{12}
\]

这再次给出 \(m\not\equiv2\pmod3\)，并给出更细的系数约束：

\[
m\equiv0\pmod3\Longrightarrow a\equiv0\pmod3,\qquad
m\equiv1\pmod3\Longrightarrow a\equiv2\pmod3.
\tag{13}
\]

根层 \(u\) 是奇数。若 \(m\) 为奇数，则 \(D\equiv m\pmod2\) 和
\(Da\equiv m\pmod2\) 强制 \(a\) 为奇数；若 \(m\) 为偶数，则参数对 gate 的
\(m\mid a+3u\) 强制 \(a+3u\) 为偶数，仍给出 \(a\) 为奇数。因此

\[
\boxed{a\equiv1\pmod2.}
\tag{14}
\]

同一 gate 给出

\[
L=am,\qquad s=m-a,\qquad
\mathcal B=L^2+Ls+s^2,\qquad
Lp=9u^2+3(a-1)u+s,\qquad
u\mid\mathcal B,\qquad m\mid a+3u.
\tag{15}
\]

由 \(m\ge3\)、(13)--(14) 分类，所有可能满足 \(a(m-1)<30\) 的对恰为

\[
\boxed{
(m,a)\in\{(3,3),(3,9),(4,5),(6,3),(9,3)\}.}
\tag{16}
\]

这里无需扫描：\(m\equiv0\pmod3\) 时只有 \(m=3,6,9\) 仍可能低于该阈值，
而 \(m\equiv1\pmod3\) 时 \(a\ge5\) 且只有 \(m=4\) 仍可能。五个对均可用
(15) 的有限除子门精确排除：

| \((m,a)\) | \(\mathcal B\) 与 \((u,6)=1\) 候选 | 排除 |
|---|---|---|
| \((3,3)\) | \(\mathcal B=81\) | \(3p=u(3u+2)\) 与 \(3\nmid u\) 矛盾。 |
| \((3,9)\) | \(603=3^2\cdot67\), \(u=1,67\) | \(u=1\) 给 \(p=1\)；\(u=67\) 时 \(27\nmid42003\)。 |
| \((4,5)\) | \(381=3\cdot127\), \(u=1,127\) | \(u=1\) 给 \(p=1\)；\(u=127\) 时 \(4\nmid386=a+3u\)。 |
| \((6,3)\) | \(387=3^2\cdot43\), \(u=1,43\) | \(u=1\) 给 \(p=1\)；\(u=43\) 给 \(p=939\)，不是核心素数。 |
| \((9,3)\) | \(927=3^2\cdot103\), \(u=1,103\) | 两个候选均有 \(9\nmid3+3u\)。 |

故所有低于 30 的参数对均不可能发生：

\[
\boxed{a(m-1)\ge30.}
\tag{17}
\]

## 4. \(30p\) 高度排除带

由 \(h<p\) 及 \(D=mp+1-h\)，有

\[
D\ge(m-1)p+2.
\tag{18}
\]

因此 stutter 的精确等式给出

\[
h^2-h+m=aD
\ge a(m-1)p+2a
\ge30p+2a.
\tag{19}
\]

proper-root 的正定范数界给出 \(m<1+\sqrt h\)。这里 \(h=3u\ge3\)，故
\(1+\sqrt h<h\)，从而 \(m<h\)。于是 (19) 左端严格小于 \(h^2\)，并得到

\[
\boxed{h^2>30p.}
\tag{20}
\]

这已经在 terminal-first 后关闭全部 \(h^2\le30p\) 的 actual arithmetic stutter。

## 5. 补充：缺陷同余与 \(\delta=6\) 的排除

由三参数恒等式

\[
Da=m+h(h-1),\qquad a>0,
\tag{21}
\]

以及 (8)，得到

\[
m(p-1)\le h^2-1.
\tag{22}
\]

由 (11) 可知，若定义

\[
\delta=h^2-3p,
\tag{23}
\]

则 \(\delta\ge-2\)。再令

\[
c=3u^2-p,\qquad \delta=3c.
\tag{24}
\]

由于 \((M_0,6)=1\)，\(u\) 与 6 互素，故 \(u^2\equiv1\pmod8\)。由核心同余
\(p\equiv1\pmod {24}\)，有

\[
c\equiv3u^2-p\equiv2\pmod {24},
\qquad
\boxed{\delta\equiv6\pmod {72}.}
\tag{25}
\]

结合 \(\delta\ge-2\)，唯一可能的最小值是 \(\delta=6\)，即 \(c=2\)。但 (24) 给出
\(p=3u^2-c\)，故

\[
P
=3\left(3u^4+(1-2c)u^2+\frac{c^2-c+1}{3}\right).
\tag{26}
\]

这里 \(c\equiv2\pmod3\)，所以括号内确为整数。根条件 \(3u=h\mid P\) 因而强制

\[
\boxed{u\mid\frac{c^2-c+1}{3}.}
\tag{27}
\]

若 \(c=2\)，(27) 给出 \(u\mid1\)，即 \(u=1\)，继而 \(p=1\)，不可能为素数。
所以 \(\delta\ne6\)。由 (25)，下一个允许值为 78，故仍有 \(h^2\ge3p+78\)。

## 6. 可使用范围与剩余缺口

该结论把此前仅由 \(h^2<p\) 保证的 arithmetic strict-carry 带扩大为

\[
\boxed{h^2\le30p.}
\]

它不是全局出口定理：严格 cofactor 仍须由真实 state contract 证明其 E1--E5 准入、
目标 fiber、identity lift 和全局良基势。带外区域也仍可能由 terminal、外部源证书或
其它容量动作关闭；本引理只说明实际 proper-root stutter 不会在该小根带内留下残余。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_actual_small_root_exclusion.py --verify
~~~

脚本只重算一个真实小根 receipt、一个 \(m=1\) 的非 root 边界、低于 30 的五个固定
参数对及四个 \(\delta=6\) 代数控制；它不扫描素数、分母或历史图表。
