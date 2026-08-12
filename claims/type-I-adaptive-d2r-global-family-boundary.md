---
kind: claim
claim_id: type-I-adaptive-d2r-global-family-boundary
title: 完整 d=2r 自适应 Type I 终端族的双 G 边界
statement: 全部 d=2r 自适应 Type I 终端族等价于对每个合法 c=1,...,h 和 s=h+c 的每个因子 r 的精确同余 72r(s/r)^2+1=0 (mod 24c-1)。双 G 且当前七路 residual 的 p=2521 在这个完整有限因子盒中没有任何命中；故该终端族不能单独构成 R=3 G 或全局出口的全称 selector。相反，双 G 控制 p=118801 在唯一参数 (c,m,s,r,t,d)=(3526,84623,8476,26,326,52) 命中，说明有限小 gap 失败不等于全族失败。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-24c-minus-one-adaptive-divisor-terminal-family
  - type-I-type-II-mod-three-double-g-exit-obstruction
topics:
  - type-I
  - adaptive-divisor
  - terminal-family
  - double-G
  - strict-counterexample
  - proof-boundary
sources:
  - claim: type-I-24c-minus-one-adaptive-divisor-terminal-family
    role: complete-d-equals-two-r-normal-form
  - claim: type-I-type-II-mod-three-double-g-exit-obstruction
    role: p2521-and-p118801-double-G-controls
  - reproduction: reproductions/type_i_adaptive_d2r_global_family_boundary.py
    role: complete-finite-family-enumeration-at-named-controls
visibility: public
last_checked: '2026-08-12'
---

# 完整 \(d=2r\) 自适应 Type I 终端族的双 G 边界

## 1. 被检验的完整族

对核心素数 \(p=24h+1\)，完整 \(d=2r\) 自适应族的参数为

\[
1\le c\le h,
\qquad
m=24c-1,
\qquad
s=h+c,
\qquad
r\mid s,
\qquad
t=s/r.
\tag{1}
\]

该族的 Type I 条件精确为

\[
\boxed{
72rt^2+1\equiv0\pmod m.}
\tag{2}
\]

这与 \(rt^2\equiv-72^{-1}\pmod m\) 等价；命中时 \(d=2r\)。因此，在固定
\(p\) 上枚举 (1) 不是截断 \(c\)、截断 \(t\) 或固定小缺口菜单，而是这个完整
自适应终端族的有限因子盒穷尽。

## 2. 双 G 的严格未命中控制

令

\[
p=2521,
\qquad
h=105.
\tag{3}
\]

此点有

\[
\frac{3p+1}{4}=1891=31\cdot61,
\qquad
\frac{p+3}{4}=631.
\tag{4}
\]

三个素因子都为 \(1\pmod3\)，所以它同时属于 \(R=3\) Type I G 与 \(q=1\)
Type II G。既有 R=11/gap-7/gap-11、gap-23、gap-47、完整 \(t=3\) 和固定
\(t=5\) 分派也在此点留下 residual。

对 (1) 的所有

\[
1\le c\le105,
\qquad
r\mid105+c,
\tag{5}
\]

逐个检查 (2)，没有一个命中。因此

\[
\boxed{
p=2521\text{ 在完整 }d=2r\text{ 自适应 Type I 终端族中无 certificate}.}
\tag{6}
\]

这不是“某个有限 \(t\) 菜单未命中”的统计，而是对该已精确参数化族的穷尽反例。
所以该族不能独自承担 \(R=3\) G、双 G 或全局出口的全称量词。

## 3. 小缺口失败不意味着全族失败

同为双 G 的压力点

\[
p=118801,
\qquad h=4950
\tag{7}
\]

在完整族中有唯一命中：

\[
\boxed{
(c,m,s,r,t,d)
=(3526,84623,8476,26,326,52).}
\tag{8}
\]

故它在一个很大的合法缺口 \(m=84623\) 取得 direct Type I terminal。结合已有
gap-59 Type II 递降，这说明“有限小 gap 失败”与“完整自适应终端族失败”是不同命题。

## 4. 结论边界

这张反例卡不否定 \(p=2521\) 的 Erdős--Straus 分解：它在 gap 23 已有 Type II
terminal。它只排除一条过强策略，即从 \(d=2r\) 全族本身推出每个 G 状态都有
direct Type I terminal。后续必须使用该族外的 Type I 选择、Type II terminal/descent，
或一般 G 状态的可提升严格递降。

复现命令：`python3 reproductions/type_i_adaptive_d2r_global_family_boundary.py --verify`
