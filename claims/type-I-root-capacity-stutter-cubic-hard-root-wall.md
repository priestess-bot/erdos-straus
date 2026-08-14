---
kind: claim
claim_id: type-I-root-capacity-stutter-cubic-hard-root-wall
title: 根容量 actual stutter 的立方高度墙
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter，写
  h=3u、m=(D+h-1)/p、a=em-h、L=am、s=m-a，及
  B=L^2+Ls+s^2。则 a 为奇数，p<19L^3、h^2>(2/3)Lp，因而
  513h^6>8p^4。故在 actual proper-root 非终端分支中，只要
  513h^6≤8p^4，就不可能发生 D≡1-h mod p，canonical cofactor 必为算术严格
  carry。该结论无范围扫描；它不单独产生 Type I/II 证书、typed target、E1--E5
  递归边、全域解提升或全局良基势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-actual-small-root-exclusion
  - type-I-root-capacity-stutter-pair-root-divisor-gate
  - type-I-root-capacity-stutter-positive-definite-norm-bound
topics:
  - type-I
  - root-capacity
  - stutter
  - hard-root
  - height-bound
  - strict-carry
  - finite-menu
  - complete-excess
sources:
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-m-lower-bound-and-mod-three-classes
  - claim: type-I-root-capacity-stutter-pair-root-divisor-gate
    role: u-divides-pair-root-divisor-norm
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-m-less-than-h
  - reproduction: reproductions/type_i_root_capacity_stutter_cubic_hard_root_wall.py
    role: exact-envelope-and-shadow-algebra-control
visibility: public
last_checked: '2026-08-14'
---

# 根容量 actual stutter 的立方高度墙

## 1. 设置与结论

固定核心素数

\[
p\equiv1\pmod {24}.
\]

先执行 terminal-first。以下设一个 actual proper-root 的非终端 complete-excess
receipt 仍落在唯一非严格门。沿用实际参数

\[
h=3u,\qquad
D=mp+1-h,\qquad
eD=ph+1,\qquad
a=em-h,
\tag{1}
\]

\[
L=am,\qquad
s=m-a,\qquad
\mathcal B=L^2+Ls+s^2.
\tag{2}
\]

已有 actual-root 约束给出

\[
m\ge3,\qquad
(m+1)a\equiv m\pmod3,\qquad
m<1+\sqrt h<h,
\tag{3}
\]

而参数对 root-divisor gate 给出

\[
Lp=9u^2+3(a-1)u+s,
\qquad
u\mid\mathcal B.
\tag{4}
\]

本卡的结论是

\[
\boxed{
p<19L^3,\qquad
h^2>\frac{2}{3}Lp,
\qquad
513h^6>8p^4.}
\tag{5}
\]

因此在这一个 actual proper-root 非终端分支中，

\[
\boxed{
513h^6\le8p^4
\quad\Longrightarrow\quad
D\not\equiv1-h\pmod p.}
\tag{6}
\]

也就是说，(6) 的区域中 terminal-first 后 canonical cofactor 已是 arithmetic
strict carry。它与已有 \(h^2\le15p\) 排除带互补：本卡给出随 \(p\) 增长的
\(h=\Omega(p^{2/3})\) hard-root 墙，而不是另一次固定范围枚举。

## 2. Actual parity 与参数对的统一二次包络

已有 \(u=(2r+1,M_0)\) 且 \(M_0\) 为奇数，所以 \(u\) 为奇数。若 \(m\) 为奇数，
则 \(D\equiv m\pmod2\)、\(Da\equiv m\pmod2\) 强制 \(a\) 为奇数。若 \(m\) 为
偶数，则 (4) 的 \(m\mid a+3u\) 强制 \(a+3u\) 为偶数；由于 \(3u\) 为奇数，
\(a\) 仍为奇数。因此

\[
\boxed{a\equiv1\pmod2.}
\tag{7}
\]

由 (3) 的模 3 分类，若 \(m\equiv0\pmod3\)，则 \(a\equiv0\pmod3\)；
若 \(m\equiv1\pmod3\)，则 \(a\equiv2\pmod3\)。所以

\[
\boxed{a\ge3,\qquad L=am\ge9.}
\tag{8}
\]

对 (2) 直接展开有精确分解

\[
\boxed{
13L^2-9\mathcal B
=(L+3a-3m)(4L-3a+3m).}
\tag{9}
\]

第一因子可改写为

\[
L+3a-3m=m(a-3)+3a>0,
\tag{10}
\]

第二因子为

\[
4L-3a+3m=a(4m-3)+3m>0.
\tag{11}
\]

故

\[
\boxed{0<\mathcal B<\frac{13}{9}L^2.}
\tag{12}
\]

同一第一因子还给出

\[
L-3s=m(a-3)+3a>0,
\qquad
s<\frac L3.
\tag{13}
\]

另外

\[
L-3(a-1)=a(m-3)+3>0,
\qquad
3(a-1)\le L-3.
\tag{14}
\]

这些不等式只使用 actual parity、\(m\ge3\) 和模三分类，没有按 \(p,u,m\) 做范围搜索。

## 3. 从 root-divisor gate 到 \(p<19L^3\)

由 \(u\mid\mathcal B\) 及正性有 \(u\le\mathcal B\)。将 (12)--(14) 代入 (4)，得到

\[
\begin{aligned}
Lp
&=9u^2+3(a-1)u+s\\
&<
9\left(\frac{13}{9}L^2\right)^2
+(L-3)\frac{13}{9}L^2+\frac L3.
\end{aligned}
\tag{15}
\]

所以

\[
p<
\frac{169}{9}L^3+\frac{13}{9}L^2-\frac{13}{3}L+\frac13.
\tag{16}
\]

由于 \(L\ge9\)，右端严格小于 \(19L^3\)。精确差为

\[
\begin{aligned}
19L^3
-\left(
\frac{169}{9}L^3+\frac{13}{9}L^2-\frac{13}{3}L+\frac13
\right)
&=\frac{2L^3-13L^2+39L-3}{9}>0.
\end{aligned}
\tag{17}
\]

最后一个正性可直接由 \(L\ge9\) 看出：
\(2L^3-13L^2+39L-3=L^2(2L-13)+39L-3>0\)。这证明 (5) 的第一项。

## 4. 高度墙

proper-root 范围 \(h<p\) 和 (1) 给出

\[
D=mp+1-h\ge(m-1)p+2.
\tag{18}
\]

另一方面，三参数恒等式为

\[
h^2-h+m=aD.
\tag{19}
\]

由 \(m\ge3\) 有 \(a\le L/3\)，故

\[
a(m-1)=L-a\ge\frac23L.
\tag{20}
\]

结合 (18)--(20)，并使用 (3) 的 \(m<h\)，有

\[
h^2>h^2-h+m
=aD
\ge a(m-1)p+2a
\ge\frac23Lp.
\tag{21}
\]

将 (21) 立方，再以 \(L^3>p/19\) 代入，得到

\[
h^6>\frac{8}{27}L^3p^3
>\frac{8}{27}\frac p{19}p^3
=\frac8{513}p^4,
\tag{22}
\]

即 (5) 的第三项，(6) 是其逆否命题。

## 5. 对全局出口的作用范围

这是一条 actual receipt 的必要高度墙，而不是完整 G/Type I global exit。它确实把
stutter 残余进一步限制为

\[
h>\left(\frac8{513}\right)^{1/6}p^{2/3},
\tag{23}
\]

并可与容量素因子 provenance 或 canonical valuation 联立；但 strict carry 仍须通过
真实 source、typed target、E1--E5、图表无关 identity lift 与不可重置全局势，才能
登记为 verified edge。故本卡不声称已经构造 Type I/II 短证书或更小分母。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_cubic_hard_root_wall.py --verify
~~~

脚本仅重算 (9)、(13)、(17) 的精确整数包络，并以既有 p=54481 shadow gate
复放 (4)--(5) 的代数尺度；不扫描素数、分母、参数对或 selector history。该 shadow
不被当作 actual receipt 或核心素数反例。
