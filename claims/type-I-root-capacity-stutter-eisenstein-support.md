---
kind: claim
claim_id: type-I-root-capacity-stutter-eisenstein-support
title: proper-root stutter 范数的 Eisenstein 素因子支撑限制
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter，令 b=e-1、
  N=a^2-ab+b^2=G(a,e)。则 h|N，且 N 的每个素因子 q 都满足 q=3 或
  q≡1 mod3；特别地，范数商 N/h 也没有 2 mod3 素因子。这排除了把该范数
  直接用作 gap 3 的 Type I/II 证书来源，但尚未给出其它 gap 的证书或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - gap-three-criterion
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-norm
  - prime-support
  - gap-three
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-identities-and-h-divides-norm
  - claim: gap-three-criterion
    role: 2mod3-factor-certificate-obstruction
  - reproduction: reproductions/type_i_root_capacity_stutter_eisenstein_support.py
    role: fixed-control-support-check
visibility: public
last_checked: '2026-08-14'
---

# proper-root stutter 范数的 Eisenstein 素因子支撑限制

## 定理

沿用 proper-root stutter 的参数

\[
D=mp+1-h,\qquad eD=ph+1,\qquad a=em-h,
\]

并令

\[
b=e-1,\qquad N=a^2-ab+b^2.
\]

正定范数恒等式已经给出

\[
N=G(a,e),\qquad h\mid N,
\]

而 stutter 曲线还给出

\[
pa=e(h-1)+1=h(b+1)-b. \tag{1}
\]

假设 q 是 N 的素因子且 q ≡ 2 (mod 3)。先看 q=2。此时
N = a^2+ab+b^2 (mod 2)，它只有在 a、b 都为偶数时才为零；代入 (1)
会迫使 h 为偶数，与 h=3u 且 u 为奇数矛盾。因此 q 为奇素数。若
q 不整除 b，则 x=ab^(-1) (mod q) 满足

\[
x^2-x+1=0.
\]

乘以 x+1 得 x^3=-1。同时 x 不等于 -1，因为
(-1)^2-(-1)+1=3 不被 q 整除。于是 -x 是非平凡的三次单位根，
这要求 3 | (q-1)，与 q ≡ 2 (mod 3) 矛盾。因此必有 q | b；
再由 N ≡ a^2 (mod q) 得 q | a。

将 a ≡ b ≡ 0 (mod q) 代入 (1)，得到 q | h。q 不可能等于 p，
因为 h | p^2+p+1 会给出 p | 1。又 h | p^2+p+1，所以 p^3 ≡ 1 (mod q)。
若 p ≡ 1 (mod q)，则同时由 q | p^2+p+1 得 q | 3，这与 q 为奇素数且
q ≡ 2 (mod 3) 矛盾。因此 p 在有限域 F_q 的乘法群中的阶恰为 3，
从而 q ≡ 1 (mod 3)，再次矛盾。

故

\[
\boxed{q\mid N\Longrightarrow q=3\ \text{或}\ q\equiv1\pmod3.}
\]

由于 (h\mid N)，同样的支撑限制传给范数商 (N/h)。

## 对证书路线的直接含义

gap (3) 的精确判据要求
(x=(p+3)/4) 含有 (2\pmod3) 的素因子。上面的结论说明，
proper-root stutter 的 Eisenstein 范数及其商不可能提供这样的素因子。因此，
“从 stutter 范数中抽取一个 (2\pmod3) 素因子来关闭 gap 3”这条直觉路线被
严格排除；必须另用 (p+3) 的因子、其它 gap 的 Type I/II 正规形，或构造真正
的分母递降。

## 边界

该引理只限制范数的素因子同余类。它没有说明 (N/h) 是否为 1，也没有把
(q\equiv1\pmod3) 的素因子转成 external-source 菜单命中；后者的菜单可能为空。
更重要的是，证明仍只处理 stutter 分支，不能替代 actual receipt 的 provenance、
source/target fiber 和全局严格势。因此它是一个排除型结构结果，而非“短证书或
递降”全局出口。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_eisenstein_support.py --verify
```

脚本使用几个固定的整数曲线控制，重算 h | N、范数分解和素因子支撑；控制
元组不被宣称为核心素数的 actual receipt，也不执行范围搜索。
