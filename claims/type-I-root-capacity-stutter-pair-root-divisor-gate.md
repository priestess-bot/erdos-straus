---
kind: claim
claim_id: type-I-root-capacity-stutter-pair-root-divisor-gate
title: 根容量 stutter 的参数对 root-divisor gate 与 actual 边界
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter，写 h=3u、
  m=(D+h-1)/p、a=em-h，并令 L=am、s=m-a、B=L^2+Ls+s^2。则
  Lp=9u^2+3(a-1)u+s、m|(a+3u)，且 u|B。故固定 (m,a) 后，候选根层 u
  落在 B 的有限除子菜单中，e 和 p 均由显式公式恢复。若素数 ell|u，则
  ell|m 当且仅当 ell|a；在该共同因子情形 ell|e-1。核心同余但合数的
  p=54481 shadow control 满足整个 gate，却在 canonical maximal receipt 中由
  D=16D0 失去 stutter，同一 gate 因而是必要的有限容量映射，不是 actual receipt
  的充分条件，也不单独给出 Type I/II 证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-actual-maximality-boundary
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - divisor-filter
  - finite-menu
  - cyclotomic
  - complete-excess
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-proper-root-stutter-gate
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: m-a-e-stutter-identities
  - claim: type-I-root-capacity-stutter-actual-maximality-boundary
    role: canonical-receipt-sharpness-control
  - reproduction: reproductions/type_i_root_capacity_stutter_pair_root_divisor_gate.py
    role: fixed-pair-gate-and-canonical-boundary-control
visibility: public
last_checked: '2026-08-14'
---

# 根容量 stutter 的参数对 root-divisor gate 与 actual 边界

## 1. 设置

固定一个 actual proper-root stutter。沿用

\[
h=3u,\qquad h\mid P,\qquad P=p^2+p+1,
\]

\[
D=mp+1-h,\qquad eD=ph+1,\qquad a=em-h,
\qquad Da=m+h(h-1).
\tag{1}
\]

定义两个只依赖参数对 \((m,a)\) 的整数

\[
L=am,\qquad s=m-a,\qquad
\mathcal B(m,a)=L^2+Ls+s^2.
\tag{2}
\]

## 2. 有限 root-divisor gate

把 \(h=3u\) 代入 (1) 的最后一式并消去 \(D\)，得到

\[
\boxed{
Lp=9u^2+3(a-1)u+s.}
\tag{3}
\]

同时 \(a=em-3u\) 给出

\[
\boxed{m\mid a+3u,\qquad e=\frac{a+3u}{m}.}
\tag{4}
\]

由 (3) 模 \(u\) 化简，

\[
Lp\equiv s\pmod u.
\tag{5}
\]

另一方面 \(u\mid P\)。将 \(P=p^2+p+1\) 乘以 \(L^2\)，并用 (5) 替换
\(Lp\)，可得

\[
\boxed{u\mid\mathcal B(m,a).}
\tag{6}
\]

更精确地，直接展开有

\[
\boxed{
L^2P
=\mathcal B(m,a)
+3u(em-1)\bigl(Lp+a(m-1)+m\bigr).}
\tag{7}
\]

因此对于每个固定 \((m,a)\)，所有可能的根高度只能按以下有限菜单重建：

\[
u\mid\mathcal B(m,a),\qquad
m\mid a+3u,\qquad
L\mid 9u^2+3(a-1)u+s,
\tag{8}
\]

\[
e=\frac{a+3u}{m},\qquad
p=\frac{9u^2+3(a-1)u+s}{L}.
\tag{9}
\]

最后仍须检查 \(p\) 为核心素数、\(h<p\)、actual complete-excess 赋值及状态合同；
(8)--(9) 不是这些条件的替代。

## 3. 根层与参数对的共同素因子

令 \(\ell\) 为素数且 \(\ell\mid u\)。由 (6)：

* 若 \(\ell\mid m\)，则模 \(\ell\) 有 \(\mathcal B\equiv a^2\)，故
  \(\ell\mid a\)；
* 若 \(\ell\mid a\)，则模 \(\ell\) 有 \(\mathcal B\equiv m^2\)，故
  \(\ell\mid m\)。

所以

\[
\boxed{\ell\mid u\Longrightarrow
\bigl(\ell\mid m\Longleftrightarrow\ell\mid a\bigr).}
\tag{10}
\]

在这个共同因子情形，(1) 中
\(pa=e(h-1)+1\) 模 \(\ell\) 给出

\[
\boxed{\ell\mid e-1.}
\tag{11}
\]

这把 root capacity 素因子分成两种可追踪类型：不整除 \(ma\) 的 primitive
root-divisor 因子，或同时整除 \(m,a,e-1\) 的退化因子。它仍不保证相应的
external-source 菜单命中。

## 4. Canonical actual 边界

这个 gate 确实压缩了固定参数对，但不能脱离 actual maximal receipt 使用。已有的
core-congruent shadow control

\[
(p,u,m,a,e)=(54481,4021,13,209,944)
\tag{12}
\]

满足 \(h=12063<p\)、\(p\equiv1\pmod {24}\) 和全部 (3)--(9)。具体地，

\[
L=2717,\qquad s=-196,\qquad
\mathcal B=6887973=4021\cdot1713,
\tag{13}
\]

\[
a+3u=12272=13\cdot944.
\tag{14}
\]

但 \(p=7\cdot43\cdot181\) 为合数，且其 shadow divisor
\(D_0=696191\) 在实际 canonical valuation 中被容量内 \(2^4\) residual 扩大为

\[
D=16D_0,
\tag{15}
\]

从而失去 stutter 同余。它不是核心素数上的反例，却严格说明：即使保留
root-divisor menu、\(e\) 整性、所有三参数恒等式和 core congruence，也不能把
抽象 divisor 误当作 actual receipt。

## 5. 对全局出口的作用范围

(8) 把每个固定 \((m,a)\) 的 root 层变成有限除子菜单，因而可作为把高根
\(h^2>15p\) 残余联立到 canonical valuation 或容量素因子 external-source 菜单的
输入。它没有统一界住 \((m,a)\)，没有证明菜单为空或必命中，也没有产生
Type I/II 证书、可提升递降或全局良基势。下一步必须保留 \(Q,\beta,(A,Q),D\) 的
逐赋值数据，并把 menu 结果接到 E1--E5 的真实 target contract。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_pair_root_divisor_gate.py --verify
~~~

脚本只检查 (3)、(4)、(6)、(7) 及固定 canonical-boundary control；不扫描素数、
分母或一般参数对。
