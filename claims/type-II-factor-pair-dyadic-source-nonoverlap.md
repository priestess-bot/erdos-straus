---
kind: claim
claim_id: type-II-factor-pair-dyadic-source-nonoverlap
title: Type II 两尾严格源与广义二进终端的不交定理
statement: 设同一 Type I 图表满足 4K=pR+1，其中 p 是 1 (mod 4) 素数；设 m 是合法的 3 (mod 4) gap，存在完整 Type II 互素因子对 x=(p+m)/4=ABC、(A,B)=1、A<=B、A+B=m*kappa，且 m+1|p-1。则其严格两尾源 n=(p+m)/(m+1) 不可能同时是该图表的任何广义 2^j 偶终端的源；因而也不可能由该图表目标指数纤维的近邻对产生。这个不交结论不否定 Type II 终端或其显式两尾提升，只禁止按同一 source denominator 把两种回执合并。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-factor-pair-carrier-strict-descent
  - type-II-c3-adaptive-core19-gap191-carrier-sieve
  - type-I-general-dyadic-terminal-transfer
  - type-I-generalized-dyadic-natural-lift-equivalence
  - type-I-target-fiber-neighbor-dyadic-normalization
topics:
  - type-I
  - type-II
  - strict-descent
  - two-tail-lift
  - generalized-dyadic
  - target-fiber
  - nonoverlap
  - terminal-first
  - proof-boundary
sources:
  - claim: type-II-factor-pair-carrier-strict-descent
    role: complete-Type-II-factor-pair-and-two-tail-lift
  - claim: type-II-c3-adaptive-core19-gap191-carrier-sieve
    role: adaptive-core19-61-carrier-parameterization
  - claim: type-I-general-dyadic-terminal-transfer
    role: generalized-dyadic-terminal-arithmetic
  - claim: type-I-target-fiber-neighbor-dyadic-normalization
    role: near-pair-implies-dyadic-terminal
  - reproduction: reproductions/type_ii_factor_pair_dyadic_source_nonoverlap.py
    role: affine-core19-carrier-control
visibility: public
last_checked: '2026-08-07'
---

# Type II 两尾严格源与广义二进终端的不交定理

## 1. 设置

设

\[
4K=pR+1,
\qquad
p\equiv1\pmod4,
\tag{1}
\]

其中 \(p\) 是素数。于是 \(R\equiv3\pmod4\)。令 \(m\) 为合法 gap，满足

\[
m\equiv3\pmod4,
\qquad
3\le m\le p-2,
\qquad
m+1\mid p-1.
\tag{2}
\]

再设已有完整的 Type II 互素因子对

\[
x=\frac{p+m}{4}=ABC,
\qquad
(A,B)=1,
\qquad
A\le B,
\qquad
A+B=m\kappa.
\tag{3}
\]

按既有 factor-pair two-tail lift，这给出直接 Type II 终端及严格可提升的源

\[
n=\frac{p+m}{m+1}
=1+\frac{p-1}{m+1},
\qquad
2\le n<p.
\tag{4}
\]

本卡只研究这个已经存在的 two-tail source 能否同时被解释为同一图表的广义二进偶终端。
它不否定 (3) 的 Type II 证书，也不把下面的不交结论登记为新的 selector edge。

## 2. 不交定理

**定理。** 在 (1)--(4) 下，不存在互素 \(L=2K\) 除子 \(u,v\) 和 \(j\ge1\)，使

\[
u\equiv2^jv\pmod R,
\qquad
1\le j\le v_2(L)+v_2(u)-v_2(v),
\qquad
u<2^jv,
\tag{5}
\]

且其广义二进终端恰为 (4) 中的 \(n\)。换言之，严格 Type II two-tail source 与同图表
的任意广义 \(2^j\) 偶终端不交。

### 证明

反设 (5) 的广义二进终端正是 \(n\)。终端因子由 \(n=(4K-E)/R\) 唯一强制为

\[
E=4K-nR=(p-n)R+1.
\tag{6}
\]

由 (4)，

\[
p-n=m(n-1).
\tag{7}
\]

若记 \(a=mR\)，则

\[
\boxed{E=a(n-1)+1.}
\tag{8}
\]

广义二进终端给出 \(E\mid(2K)^2=4K^2\)。另一方面，

\[
4K=nR+E.
\tag{9}
\]

将这个整除式乘以 \(4\) 后有 \(E\mid(4K)^2\)，再由 (9) 得
\(E\mid n^2R^2\)。由 \(E\equiv1\pmod R\)，
\((E,R)=1\)，故

\[
E\mid n^2.
\tag{10}
\]

式 (8) 还给出 \(an\equiv a-1\pmod E\)。将其平方，并使用 (10)，得到

\[
E\mid(a-1)^2.
\tag{11}
\]

现在只用大小比较。由 (8)、(10)，

\[
0\le n^2-E=(n-1)(n-a+1).
\tag{12}
\]

因 \(n>1\)，故 \(n\ge a-1\)。又由 (8)、(11)，

\[
0\le(a-1)^2-E=a(a-n-1),
\tag{13}
\]

故 \(n\le a-1\)。于是被迫有

\[
n=a-1,
\qquad
E=n^2.
\tag{14}
\]

但 \(m\equiv R\equiv3\pmod4\)，所以 \(a\equiv1\pmod4\)，进而 \(4\mid n\)。将
(14) 代回 (9) 得

\[
4K=n(R+n).
\tag{15}
\]

这里 \(R+n\) 是奇数。令 \(t=v_2(n)\ge2\)，则 (15) 给出

\[
v_2(4K)=t,
\qquad
v_2(4K^2)=2t-2,
\tag{16}
\]

而 (14) 给出 \(v_2(E)=2t\)。这与广义二进必要整除
\(E\mid4K^2\) 矛盾。证毕。

这个证明的核心是仿射平方刚性：若 \(a,n>1\) 且
\(a(n-1)+1\mid n^2\)，则比较 (12)--(13) 已强制 \(n=a-1\)。二进矛盾排除了
这个唯一形式在本图表中成为偶终端的可能性。

## 3. 目标纤维近邻的推论

目标指数纤维近邻对规范地产生一个广义 \(2^j\) 偶终端，且保留完全相同的 \((E,n)\)。
因此定理立即给出

\[
\boxed{
\text{Type II 两尾严格源 }\frac{p+m}{m+1}
\text{ 不可能是同图表 target-fiber near-pair 的源。}}
\tag{17}
\]

这里的量词是“同一个 source denominator”。同一素数当然仍可能在不同的分母上同时拥有
Type II 两尾递降和一个无关的 dyadic 或 near-pair 终端。

## 4. Adaptive core-19 的 gap-191 / 61-carrier 控制

在 c=3 adaptive core-19 ray 的 \(v=8w\) 子射线上，已有

\[
p=192N-191,
\qquad
R=832N-841,
\qquad
n=\frac{p+191}{192}=N.
\tag{18}
\]

gap \(191\) 的 carrier 选择律在 \(61\mid N\) 时给出完整因子对。取已有
\(61\)-carrier 子射线的进一步限制

\[
z=1+4u,
\qquad
v=712+1952u,
\tag{19}
\]

则

\[
\begin{aligned}
M&=12424897516+34021221780u,\\
N&=61M,\\
p&=145520399707201+398456549487360u.
\end{aligned}
\tag{20}
\]

其中 \(4\mid M\)，故 \(4\mid N\)，并且

\[
\gcd(145520399707201,398456549487360)=1.
\tag{21}
\]

Dirichlet 定理因而给出无穷多个使 \(p\) 为素数的参数。对每一个这种素数参数点，

\[
(A,B,C,\kappa)=(8,183,2M,1)
\tag{22}
\]

满足 \(ABC=2928M=(p+191)/4\) 与 \(A+B=191\)，所以它给出已有的显式两尾恒等式

\[
\frac4p
=\frac1{2928M}
+\frac1{16Mp}
+\frac1{366Mp},
\qquad
\frac4{61M}
=\frac1{2928M}
+\frac1{16M}
+\frac1{366M}.
\tag{23}
\]

尽管这里 \(4\mid N\)，即它通过了 target-neighbor 所需的粗二进奇偶筛，定理仍排除
同一 \(N\) 是该 adaptive 图表的任意 generalized-dyadic 或 near-pair terminal。
复现器还直接重算

\[
4K-NR=191R(N-1)+1>N^2
\tag{24}
\]

在复现器选取的实际素数控制点，因此可见该实例的失败并非只靠奇偶性。

这个 affine family 提供直接 Type II terminal 和显式 two-tail lift，但本卡没有定义
source marked-solution set、representation--dual capacity map 或 E1--E5 回执。因此它不是
统一 selector 的新 edge，也不证明逐点 terminal cover 或 Erdos--Straus 猜想。

复现：

```bash
python3 reproductions/type_ii_factor_pair_dyadic_source_nonoverlap.py --verify
```
