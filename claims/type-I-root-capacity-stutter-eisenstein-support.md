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

## 范数素因子的来源分流

上面的同余限制还可以和 (1) 一起区分 (h)-部分与商部分。设
(q\mid h) 且 (q\mid N)，并且 (q\nmid a)。由 (N\equiv0\pmod q) 得

\[
\left(\frac{b}{a}\right)^2-\frac{b}{a}+1\equiv0\pmod q,
\]

所以 (p\equiv-b/a\pmod q)（这里使用 (pa\equiv-b\pmod q)）。令

\[
\rho_q=\langle p\rangle_q,\qquad i_q=q-\rho_q.
\]

则 (q\mid p+i_q)，这正是（对 (q\ne3)）容量素因子 external-source 菜单的
入口。更重要的是，非退化条件并不是该菜单的前提：因为 (h=3u) 且
((u,3)=1)，每个 (q\mid h)、(q\ne3) 的素因子都满足 (q\mid u)，所以
退化的 (q\mid a,b) 也可以使用同一个容量菜单。退化时范数线性式只额外给出
  (q\mid m)：由 (N\equiv b^2\pmod q) 得 (q\mid b)，再由
  (a=em-h)、(e=b+1\equiv1\pmod q) 得 (q\mid m)。

因此精确的 provenance 分派是：

* (q\mid h, q\ne3)：无论是否退化，都有根容量 q-source 菜单；非退化时还
  可由 (pa\equiv-b\pmod q) 独立恢复源余数；
* (q=3)：(3\nmid u)，是 h-支撑中的唯一容量例外；
* (q\nmid h)：这是 quotient-only 因子，没有被当前根容量强制的 source provenance。

容量菜单仍可能为空，所以范数的 (1\bmod3) 素因子不自动构成短证书；完整的
三分派见[根容量 stutter 范数因子的 provenance 三分派](type-I-root-capacity-stutter-provenance-dispatch.md)。

## 对证书路线的直接含义

gap (3) 的精确判据要求
(x=(p+3)/4) 含有 (2\pmod3) 的素因子。上面的结论说明，
proper-root stutter 的 Eisenstein 范数及其商不可能提供这样的素因子。因此，
“从 stutter 范数中抽取一个 (2\pmod3) 素因子来关闭 gap 3”这条直觉路线被
严格排除；必须另用 (p+3) 的因子、其它 gap 的 Type I/II 正规形，或构造真正
的分母递降。

## 边界

该引理只限制范数的素因子同余类，并修正了 h-支撑因子的来源类型。它没有说明
容量菜单必非空，也没有把 (q=3) 或 quotient-only 因子转成证书。更重要的是，
证明仍只处理 stutter 分支，不能替代 actual receipt 的 source/target fiber 和全局
严格势。因此它是一个带 provenance 修正的结构结果，而非“短证书或递降”全局出口。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_eisenstein_support.py --verify
```

脚本使用几个固定的整数曲线控制，重算 h | N、范数分解和素因子支撑；控制
元组不被宣称为核心素数的 actual receipt，也不执行范围搜索。
