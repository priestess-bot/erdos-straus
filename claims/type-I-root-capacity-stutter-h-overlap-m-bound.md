---
kind: claim
claim_id: type-I-root-capacity-stutter-h-overlap-m-bound
title: proper-root stutter 的 h^2-1 重叠 m 界与非平凡约化除子
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  H=h^2-1、D_H=gcd(D,H)、D*=D/D_H，且 m=(D+h-1)/p。则
  D_H|2 lcm(m,m+2)。actual 条件 m≥3、m not≡2 mod3、m<1+sqrt(h)、h<p
  进一步强制 D>2 lcm(m,m+2)，故 D*>1。结合已有约化除子结果，
  1<D*|gcd(T,h^2-h-2r,J)，其中
  J=2h^2r-hm-4hr-m^3-2m^2r-m^2+m+2r。该结论排除 actual proper-root
  stutter 的 D 完全被 h^2-1 吸收；它仍不构造 Type I/II 证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-actual-small-root-exclusion
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-reduced-divisor-product
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - valuations
  - resultant
  - divisor-filter
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-linearization-and-h-odd-root-setup
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-m-lower-bound-and-mod-three-class
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-square-root-bound-for-m
  - claim: type-I-root-capacity-stutter-reduced-divisor-product
    role: D-star-divides-T-S-J
  - reproduction: reproductions/type_i_root_capacity_stutter_h_overlap_residual.py
    role: fixed-H-overlap-and-three-m-regime-controls
visibility: public
last_checked: '2026-08-14'
---

# proper-root stutter 的 \(h^2-1\) 重叠 \(m\) 界与非平凡约化除子

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

考虑 terminal-first 后的一个 actual maximal complete-excess proper-root stutter
receipt。沿用

\[
D=mp+1-h,\qquad D\mid ph+1,\qquad 2\le h<p,
\tag{1}
\]

并定义

\[
H=h^2-1,\qquad D_H=(D,H),\qquad D_*=\frac{D}{D_H}.
\tag{2}
\]

根层写作 \(h=3u\)，其中 \(u\mid(p^2+p+1)/3\)。后者为奇数，所以

\[
\boxed{h\ \text{为奇数}.}
\tag{3}
\]

此前已知 \(D_*\mid T,S,J\)，但没有排除 \(D_*=1\)。本卡给出一个完全由 \(m\)
控制的 \(D_H\) 上界，并据此排除该退化。

## 2. \(h-1,h+1\) 的局部化

令

\[
b_-=(D,h-1),\qquad b_+=(D,h+1),\qquad L_m=\operatorname{lcm}(m,m+2).
\tag{4}
\]

在模 \(b_-\) 下，\(h\equiv1\) 且 \(D\mid ph+1\) 给出 \(p\equiv-1\)。再将其代入
\(D=mp+1-h\)，得到 \(b_-\mid m\)。同理，在模 \(b_+\) 下有
\(h\equiv-1\)、\(p\equiv1\)，从而 \(b_+\mid m+2\)。因此

\[
\boxed{b_-\mid m,\qquad b_+\mid m+2,\qquad
\operatorname{lcm}(b_-,b_+)\mid L_m.}
\tag{5}
\]

对任意奇素数 \(q\)，\(q\) 至多整除 \(h-1,h+1\) 中的一个。故 \(q\) 在
\(D_H=(D,(h-1)(h+1))\) 中的赋值恰为它在 \(\operatorname{lcm}(b_-,b_+)\) 中的
赋值，因而受 \(L_m\) 控制。

只剩 \(q=2\)。置

\[
\alpha=v_2(D),\qquad a=v_2(h-1),\qquad b=v_2(h+1),\qquad A=\max(a,b).
\]

由 (3)，相邻偶数 \(h-1,h+1\) 中恰有一个二进赋值为 1，因此

\[
v_2(H)=a+b=A+1.
\tag{6}
\]

另一方面

\[
v_2\!\left(\operatorname{lcm}(b_-,b_+)\right)
=\max\{\min(\alpha,a),\min(\alpha,b)\}
=\min(\alpha,A).
\tag{7}
\]

所以

\[
v_2(D_H)=\min(\alpha,A+1)
\le\min(\alpha,A)+1
\le v_2(L_m)+1.
\tag{8}
\]

将奇素数和 2 的结果合并，得到

\[
\boxed{D_H\mid2L_m=2\operatorname{lcm}(m,m+2).}
\tag{9}
\]

这里的额外因子 2 只来自 \(h-1,h+1\) 的共同二因子；没有把 \(D_H\) 错当成先前的
cyclotomic \(D_C\)。

## 3. actual proper-root 强制 \(D_*>1\)

actual proper-root stutter 的既有约束为

\[
m\ge3,\qquad m\not\equiv2\pmod3,\qquad
m<1+\sqrt h,\qquad h<p.
\tag{10}
\]

并由 (1) 和 \(h\le p-1\) 得

\[
D\ge(m-1)p+2.
\tag{11}
\]

核心素数满足 \(p\ge73\)。由 (10) 的模 3 条件，\(m\ge3\) 后只需分三类。

若 \(m=3\)，则

\[
D\ge148>30=2\operatorname{lcm}(3,5).
\tag{12}
\]

若 \(m=4\)，则

\[
D\ge221>24=2\operatorname{lcm}(4,6).
\tag{13}
\]

其余情形为 \(m\ge6\)。由 \(m<1+\sqrt h<h+1\) 及 \(h<p\)，有

\[
p>(m-1)^2,\qquad D>(m-1)^3.
\tag{14}
\]

而对 \(m\ge6\)，

\[
\begin{aligned}
(m-1)^3-2m(m+2)
&=(m-6)(m^2+m+5)+29>0.
\end{aligned}
\tag{15}
\]

故

\[
D>2m(m+2)\ge2L_m\ge D_H.
\tag{16}
\]

三类合并后，\(D>D_H\)。所以

\[
\boxed{D_*=\frac{D}{(D,h^2-1)}>1.}
\tag{17}
\]

已有约化除子定理进一步给出 \(D_*\mid T\)、\(D_*\mid S=h^2-h-2r\) 与
\(D_*\mid J\)，其中

\[
J=2h^2r-hm-4hr-m^3-2m^2r-m^2+m+2r.
\]

因而得到新的实际残余约束

\[
\boxed{
1<D_*\mid\gcd\!\left(T,h^2-h-2r,J\right).}
\tag{18}
\]

换言之，actual proper-root stutter 的 \(D\) 不可能全部被 \(h^2-1\) 吸收；此前
约化为 \(D_*\) 后可能为空的担忧在这个 scope 内已被排除。

## 4. 对全局出口的作用范围

式 (18) 把 hard-root stutter 的每个实际残余压到三个显式整数的非平凡公共除子，明显强于
只知道 \(D_*\mid T,S,J\) 而允许 \(D_*=1\)。但它没有证明该公因子属于任何已有
capacity source，也没有把它转换为 external-source 菜单命中、Type I/II 证书、typed
target 或 E1--E5 递降。下一步需要利用 \(T,S,J\) 的共同素因子与 actual valuation
provenance 的关系，而不是把非平凡性本身误当作 global exit。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_h_overlap_residual.py --verify
```

脚本只重算五个固定算术控制：odd/dyadic/mixed \(H\)-overlap，以及 \(m=3\)、\(m=4\)、
\(m\ge6\) 的数值比较。核心素数 proper-shape 控制明确缺少 root provenance；\(m=13\)
控制是已有的核心同余合数 shadow。它们不被冒充为 actual receipt，且脚本不扫描范围。
