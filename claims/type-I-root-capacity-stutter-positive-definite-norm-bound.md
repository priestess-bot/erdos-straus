---
kind: claim
claim_id: type-I-root-capacity-stutter-positive-definite-norm-bound
title: proper-root stutter 的正定范数与平方根菜单界
statement: >-
  对核心素数 p≡1 mod24 的实际 proper-root stutter receipt，若 2<=h<p，令
  m=(D+h-1)/p、e=(ph+1)/D、a=em-h，则 1<=a<e，并且
  h 整除 G(a,e)=a^2-ae+e^2+a-2e+1。该二次式满足
  4G=(2a-e+1)^2+3(e-1)^2；在 1<=a<e 时有 0<G<e^2。因此
  e>sqrt(h)，并且由 a=em-h 得 m<1+sqrt(h)。这把 proper-root stutter
  的线性参数从 m<=h 收缩到平方根级菜单，但不排除门、不产生证书或合法递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-general-endpoint-divisor-gate
topics:
  - type-I
  - root-capacity
  - stutter
  - positive-definite-form
  - norm
  - square-root-bound
  - finite-menu
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-parameterization-and-h-divides-F
  - reproduction: reproductions/type_i_root_capacity_stutter_norm_bound.py
    role: symbolic-identity-and-fixed-controls
visibility: public
last_checked: '2026-08-14'
---

# proper-root stutter 的正定范数与平方根菜单界

## 1. 参数与正定范数

沿用实际 stutter receipt 的记号

\[
D=mp+1-h,\qquad e=\frac{ph+1}{D},\qquad a=em-h,
\]

并假设 proper-root 的非平凡端点满足

\[
2\le h<p.
\]

已有整数曲线给出 \(a>0\)、\(pa=e(h-1)+1\) 和 \(h\mid F(e,m)\)，其中

\[
F(e,m)=e^2m^2-e^2m+e^2+em-2e+1.
\]

把 \(a=em-h\) 代入，直接得到

\[
F(e,m)-G(a,e)=h(2em-e-h+1),
\tag{1}
\]

其中

\[
\boxed{G(a,e)=a^2-ae+e^2+a-2e+1.}
\tag{2}
\]

因此

\[
\boxed{h\mid G(a,e).}
\tag{3}
\]

二次式有正定表达

\[
\boxed{4G=(2a-e+1)^2+3(e-1)^2.}
\tag{4}
\]

所以 \(G>0\)。

## 2. proper-root 的范围

由 \(pa=e(h-1)+1\) 且 \(h<p\)，有

\[
0<a=\frac{e(h-1)+1}{p}<e,
\tag{5}
\]

故 \(e\ge2\) 且 \(1\le a\le e-1\)。视 \(G\) 为关于 \(a\) 的凸二次式，在闭区间
\([1,e-1]\) 上最大值出现在端点：

\[
G(1)=e^2-3e+3,
\qquad
G(e-1)=(e-1)^2.
\tag{6}
\]

两者均严格小于 (e^2)，于是

\[
\boxed{0<G<e^2.}
\tag{7}
\]

结合 (3)，得到

\[
\boxed{e>\sqrt h.}
\tag{8}
\]

另一方面 \(a=em-h>0\) 且 \(a<e\)，所以

\[
e(m-1)<h.
\tag{9}
\]

由 (8)--(9) 得

\[
\boxed{m<1+\sqrt h.}
\tag{10}
\]

这比仅由 (D\mid ph+1) 得到的 (m\le h) 强一个平方根量级；它把每个固定
proper-root endpoint 的 stutter 候选压到显式有限菜单。

## 3. 证明边界

式 (10) 仍是必要界，不是门为空的证明。它没有使用 actual receipt 的全部
(C/T) 因子分裂、source/path provenance、terminal-first 或解提升数据；因此不能
把“平方根菜单”直接当作 Type I/II 证书或全局递降。下一步需要在这个有限菜单上联立
(D_*\mid J)、(D_T\mid S) 与容量素因子 external-source 菜单，或为每个未命中项
构造合法的全域 lift。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_norm_bound.py --verify
```

脚本核对 (1)--(10) 的恒等式和三个固定算术控制；它不把抽象控制当作核心素数的
actual receipt，也不执行范围搜索。
