---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion
title: q=1 高 C=2 19 相位 H5 的 a=1 顶容量残余有限筛完成
statement: >-
  在 q=1 high C=2 19 相位的既有 H3=>H4=>H5 complete-excess receipt 中，若所有
  source/path、terminal-first、typed 与 serializer guards 已通过，H5 canonical capacity
  c5=p-1 且其 d=1 坐标 a5=1，则矛盾。证明使用 H4 full-overlap 有限筛所产生的
  377516 个固定整数：其精确素因子分解只有 23 行命中相位素数，只有一行满足抽象 affine
  条件，且该行 p=14449 要求 d=85、lambda=1105、c4=11815；实际 H3=>H4 receipt 却有
  g=5、d=1、lambda=5、c4=13391。因此没有任何实际 H3=>H4 receipt 能到达 H5 的
  a5=1 top-capacity state。结合既有 d=1 handoff，所有 c5=p-1 的合法 H5 状态均有
  guarded strict-capacity endpoint。该结果仍不处理 H4 的 source/p-free 前置门、有限
  H4 例外、terminal-first/typed guards，或整个 G/Type I 全局出口。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve
  - type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
  - type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fifth-anchor
  - top-capacity
  - d-one
  - a-one
  - full-overlap
  - finite-sieve
  - exact-factorization
  - strict-capacity
  - guarded-macro
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve
    role: finite-divisor-supermenu-and-necessary-H4-overlap
  - claim: type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
    role: d-one-suffix-dispatch-and-all-non-a-one-exits
  - claim: type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate
    role: persistent-parent-E5-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h5_a_one_full_overlap_sieve_completion.py
    role: exact-fixed-integer-factorization-and-actual-H4-rebuild
visibility: public
last_checked: '2026-08-15'
---

# H5 \(a_5=1\) 顶容量残余的有限筛完成

## 1. 有限菜单的精确审理

保留 [H4 全重叠有限素因子筛](type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve.md)
的记号。若一个实际 H5 top-capacity receipt 有 \(a_5=1\)，则它必须给出

\[
p\mid C(\sigma,\lambda,d,j)
=D_\sigma j+2dN\lambda,
\tag{1}
\]

其中 \(u\in\mathcal U_{31}\)、\(\lambda\mid\lvert1536-\sigma\rvert\)、
\(d\mid\lvert1536-\sigma\rvert\)、\(1\le j<2d\)，并且 \(d\) 必须等于实际的
\((w,M_4)\)。这不是只检查一张方便的 H4 图表：它是每个假设的 \(a_5=1\) receipt 的
必要条件。

对全部 571777 个参数行、377516 个不同固定整数作精确因子分解，并逐因子要求

\[
p\ge p_u,\qquad p\equiv p_u\pmod {108528},\qquad p\equiv1\pmod {24}.
\tag{2}
\]

每个分解均以素数幂乘积重构原整数，并再次用素性测试核对。结果为：

\[
\begin{array}{c|r}
\text{fixed parameter rows} & 571\,777\\
\text{distinct factored integers} & 377\,516\\
\text{rows having a phase-prime factor} & 23\\
\text{rows also passing }2d\mid p+1,\ 1\le c_4\le p-2,\ D_\sigma c_4+N\lambda=tp
& 1\\
\text{rows matching the actual maximal H3=>H4 receipt} & 0.
\end{array}
\tag{3}
\]

因此 (1) 没有一个实际 H3=>H4 predecessor。

## 2. 唯一 affine 伪候选

表 (3) 中唯一通过抽象 affine 条件的行是

\[
\begin{aligned}
p&=14449,&u&=15,&\sigma&=431,\\
\lambda&=1105,&d&=85,&j&=139,\\
c_4&=11815,&t&=9330195,&
C&=887912188887.
\end{aligned}
\tag{4}
\]

它确实是固定整数的一条素因子命中：

\[
C=3\cdot229\cdot14449\cdot89449.
\tag{5}
\]

但对同一 \(p=14449\) 重放真正的 H3 maximal complete-excess receipt，得到

\[
\boxed{
g=(w,c_3)=5,\qquad
(w,M_4)=1,\qquad
\lambda_{\rm actual}=5,\qquad
c_{4,\rm actual}=13391.
}
\tag{6}
\]

特别地，(4) 要求的 \(d=85\) 不整除 \(g=5\)，已经违反有限筛的必要 H4 carrier
条件；后面的 \(\lambda,c_4\) 也同时失配。这说明 (4) 是超集参数化中的伪候选，而非
可达 H4 receipt。

## 3. H5 \(a_5=1\) 的排除

反设存在一个满足本卡前置 guards 的 H5 state，且 \(c_5=p-1,a_5=1\)。有限筛给出
(1) 的一行；精确因子审理把它压到 (4)，而 (6) 与该行所要求的 \(d\) 矛盾。因此

\[
\boxed{
\text{在这个 q=1 high C=2 19-phase receipt 域内，不存在 }
c_5=p-1,\ a_5=1\text{ 的实际 H5 state。}
}
\tag{7}
\]

这里排除的是实际 maximal H3=>H4 predecessor，不是把 377516 个整数中不存在的
phase 因子误读为证明。相反，(5) 的确保留了唯一算术素因子命中，并由 (6) 给出它为何
不具备真实 provenance。

值得区分的是，这个 exact factor screen 的 H3--H4 部分实际只使用
\(w\mid K_4\)，而不使用 H5 state 的存在。因此它还给出更强的独立推论：任何 actual
H4 full-overlap \((R_4-1,K_4)=p+1\) 都没有 predecessor；该推论已单独记录为
[H4 full-overlap 实际前驱排除](type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion.md)。
本卡后续只使用其中的 H5 \(a_5=1\) 子类。

## 4. 顶容量分派完成

既有 H5 \(d=1\) handoff 已经处理所有 \(a_5>1\) 的 p-free branch、raw p-source
repair、regeneration 后的 strict capacity，以及非 p-free/non-regeneration strict branch。
其中唯一未清除的算术类原为 \(a_5=1,\omega=-1\)。它是 (7) 的子类，故现已为空。

所以，对通过所有实际 checkpoint 的 H5 top-capacity 输入，总存在终点 \(T\) 使

\[
c_T\le p-2,\qquad
\Lambda^\sharp_p(P)=(0,p-1)>(0,c_T)=\Lambda^\sharp_p(T).
\tag{8}
\]

这使 \(c_5=p-1\) 不再是 fifth-anchor parent macro 的例外。若 \(c_5\le p-2\)，原
parent macro 已直接成立；若 \(c_5=p-1\)，则先执行本卡和既有 d=1 suffix，再以 (8)
支付同一个 persistent parent 的 E5。

## 5. 范围

本卡只关闭 q=1 high C=2 19-phase 的 H5 top-capacity \(a_5=1\) 残余。它仍以以下
合同为条件：

1. H4 p-source/p-free 的实际前置门及其有限例外；
2. H3--H5 每个 checkpoint 的 terminal-first、source/path、typed reclassification 与 serializer；
3. \(\operatorname{Sol}(p)\) 的 identity lift 和 persistent-parent E1--E5 复合。

它不证明其它 Type I/G state 已有短证书或 \(n<p\) 递降，也不把尚未通过这些 guards 的
算术候选登记为递归边。

## 6. 定向回执

~~~bash
python3 reproductions/type_ii_q_one_c2_19_phase_h5_a_one_full_overlap_sieve_completion.py --verify
~~~

这个回执精确分解固定菜单并重放唯一 affine 伪候选的 H3=>H4 receipt；它不扫描素数区间、
原始分母或 selector history。
