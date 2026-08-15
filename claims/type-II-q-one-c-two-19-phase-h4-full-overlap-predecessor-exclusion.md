---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
title: q=1 高 C=2 19 相位 H4 full-overlap 的实际前驱排除
statement: >-
  在 q=1 high C=2 19 相位、H3 terminal-first 后的任何实际 H3=>H4 maximal
  complete-excess receipt 中，令 w=(p+1)/2、K4=M4 c4，则 w 不整除 K4；因而
  gcd(R4-1,K4) 不等于 p+1。证明把任意假设的 w|K4 映到已有的有限常数
  C(sigma,lambda,d,j)=D_sigma j+2dNlambda：其中 lambda|abs(1536-sigma)、
  d=gcd(w,M4)|abs(1536-sigma)、1<=j<2d，且 p|C。对 31 个实际 phase class
  的 571777 行、377516 个不同常数作精确分解后，只有一行通过抽象 affine gate，且其
  p=14449 的真实 H3=>H4 receipt 的 d、lambda、c4 全部不匹配。因此该 full-overlap
  没有实际前驱。特别地，H4 p-primary small-anchor renewal 中 R4=1 (mod p) 的
  h=p+1 root p-block boundary 在此 receipt 域为空，余下的 renewal 一律为 proper-overlap
  p-free；这不处理其可能的 c_alt=p-1 top-capacity continuation，也不构成全局出口定理。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
  - type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve
  - type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - full-overlap
  - complete-excess
  - finite-sieve
  - exact-factorization
  - p-primary-peeling
  - p-free-renewal
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: actual-H3-H4-lambda-and-capacity-contract
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-overlap-identity
  - claim: type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
    role: affine-H4-capacity-lift
  - claim: type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve
    role: finite-constant-supermenu
  - claim: type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion
    role: exact-factorization-and-actual-predecessor-screen
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_full_overlap_predecessor_exclusion.py
    role: full-overlap-to-menu-and-zero-predecessor-receipt
visibility: public
last_checked: '2026-08-16'
---

# H4 full-overlap 的实际前驱排除

## 1. 要排除的是 H4 的真实 full-overlap，而非一般局部图表

保留 q=1 high \(C=2\) 19-phase 中 H3 \(\Rightarrow\) H4 maximal
complete-excess receipt 的记号：

\[
w=\frac{p+1}{2},\qquad K_4=M_4c_4,\qquad
pR_4+1=4K_4.
\tag{1}
\]

设 \(\sigma=a(p)\) 是 31 个 H3 terminal-first residual phase 中的 selector，且

\[
\Delta=\lvert1536-\sigma\rvert,
\qquad
D_\sigma=11943424-2261\sigma,
\qquad N=4718592.
\tag{2}
\]

实际 H3 \(\Rightarrow\) H4 receipt 已给出一个 \(\lambda\mid\Delta\)，并满足

\[
1\le c_4\le p-2,
\qquad
D_\sigma c_4+N\lambda=tp
\quad(t\in\mathbb Z_{>0}).
\tag{3}
\]

再令

\[
d=(w,M_4).
\tag{4}
\]

H3--H4 complete-excess provenance 给出

\[
\boxed{d\mid (w,c_3)\mid\Delta.}
\tag{5}
\]

这里的结论不是说一般满足 \(pR+1=4K\) 的高图表不可能 full-overlap。事实上
\(p=73,M=110,c=37,K=4070,R=223\) 满足

\[
(R-1,K)=74=p+1.
\tag{6}
\]

排除来自 (3)--(5) 的真实 19-phase 前驱数据；没有这些数据，不能作同样结论。

## 2. full-overlap 强制进入已分解的有限菜单

反设某一实际 H4 receipt 满足

\[
h=(R_4-1,K_4)=p+1=2w.
\tag{7}
\]

则特别有 \(w\mid K_4=M_4c_4\)。按 (4) 约去 \(M_4\) 与 \(w\) 的完整 gcd，得到

\[
\frac wd\mid c_4.
\tag{8}
\]

所以存在唯一正整数 \(j\) 使

\[
\boxed{
c_4=\frac{jw}{d}=\frac{j(p+1)}{2d},
\qquad 1\le j<2d.
}
\tag{9}
\]

上界来自 (3)：\(c_4\le p-2<p+1\)。把 (9) 代入 (3)，并乘以 \(2d\)，有

\[
(2dt-D_\sigma j)p=D_\sigma j+2dN\lambda.
\tag{10}
\]

右端为正，因此必有

\[
\boxed{
p\mid C(\sigma,\lambda,d,j):=D_\sigma j+2dN\lambda.
}
\tag{11}
\]

这正是此前 H5 \(a_5=1\) 有限筛的 fixed-integer supermenu，但这里的推导只使用
\(w\mid K_4\)，不使用 \(a_5=1\) 或 H5 的存在。故任何 H4 full-overlap 都必须在
该菜单中留下一个实际 H3 \(\Rightarrow\) H4 predecessor。

## 3. 精确屏幕没有实际前驱

对 31 个 terminal-first residual phase，令 \(\lambda,d\) 各遍历 \(\Delta\) 的正因子，
并令 \(1\le j<2d\)。已完成的 exact factor screen 给出：

| 检查 | 数量 |
|---|---:|
| 参数行 \((u,\lambda,d,j)\) | 571,777 |
| 不同固定整数 \(C\) | 377,516 |
| 含 phase-prime 因子的行 | 23 |
| 同时通过抽象 affine 条件的行 | 1 |
| 与真实 maximal H3 \(\Rightarrow\) H4 receipt 匹配的行 | 0 |

唯一抽象 affine 行为

\[
p=14449,\quad \sigma=431,\quad
(\lambda,d,j,c_4)=(1105,85,139,11815).
\tag{12}
\]

但同一 \(p\) 的真实 receipt 是

\[
(w,c_3)=5,\qquad
(w,M_4)=1,\qquad
\lambda=5,\qquad c_4=13391.
\tag{13}
\]

它与 (12) 的 \(d,\lambda,c_4\) 均不相容。因此 (11) 不能由任何实际 H3
\(\Rightarrow\) H4 receipt 实现，反设 (7) 矛盾。

\[
\boxed{
\text{在该实际 19-phase receipt 域中，}\quad
w\nmid K_4,\qquad (R_4-1,K_4)\ne p+1.
}
\tag{14}
\]

## 4. 对 p-primary renewal 的后果

在 H4 p-primary residual \(R_4\equiv1\pmod p\) 中，small-anchor renewal 已证明

\[
p\mid Q\quad\Longleftrightarrow\quad h=p+1.
\tag{15}
\]

由 (14)，右侧为空。因此这一 actual phase domain 内所有该类 residual 都满足

\[
2\le h<p+1,
\qquad p\nmid Q,
\tag{16}
\]

即 renewal 一律是 path-anchored p-free bundle。若其 canonical capacity
\(c_{\rm alt}\le p-2\)，已有 persistent parent macro 给出严格 E5 出口；若
\(c_{\rm alt}=p-1\)，其 \(a_{\rm alt}>1\) d=1 suffix 也已严格离开顶容量，见
[proper-overlap 顶容量 d=1 handoff](type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff.md)。
本卡仍不排除 \(a_{\rm alt}=1\) return，也没有把有限 H4 p-adic gate、terminal-first
或 typed guards 误报为全局完成。

## 5. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_full_overlap_predecessor_exclusion.py --verify
```

回执先用 (6) 保留一般局部 full-overlap 的正控制，再核对 (7)--(11) 的整数约束，并复用
精确 fixed-constant factor screen 的 0 个实际 H3 \(\Rightarrow\) H4 命中。它不扫描素数
区间或原始分母。
