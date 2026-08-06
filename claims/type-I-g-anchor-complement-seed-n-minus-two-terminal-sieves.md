---
kind: claim
claim_id: type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves
title: G-anchor 补余 seed 的 n-2 直接终端筛与 R=11 因子射线
statement: 设 p=24h+1 为核心素数。full-Q 补余 determinant 的 (d,n)=(3,13) 分支中，若 h 不等于 2 (mod 3) 且 h 等于 10 (mod 11)，则 m=11、x=6h+3、d=3 给出显式 Type II 直接证书；(d,n)=(9,25) 分支中，若 h 等于 2 (mod 3) 且 h 等于 9 (mod 23)，则 m=23、x=6(h+1)、d=9 给出显式 Type II 直接证书。这两个固定 (m,d) 模板上的 Type I 同余条件分别由模 11 与模 23 的二次非剩余严格排除。两支共同的 R=11 算术图表满足 K=3(22h+1)；在固定第三分母 pK 的二项拆分中，存在正三项 Type I 证书当且仅当 e divides K^2 且 e is congruent to -K (mod 11)。取 e=19 得到 h=19a+6、p=456a+145 上的显式 gap-7 Type I 射线。所有结果均为原始 p 的 terminal leaf，不依赖补余 seed 的 source/path receipt；它们只覆盖所列同余子族，不证明所有核心素数的终端存在。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - G-anchor
  - complement-torsor
  - short-certificate
  - terminal-first
  - gap-11
  - gap-23
  - gap-7
  - R-11
  - proof-program
sources:
  - claim: type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
    role: complement-seed-parameters
  - claim: type-I-g-anchor-full-q-complement-r11-reset-boundary
    role: R11-chart-and-fixed-tail-factorization
  - claim: short-certificate-equivalence
    role: Type-I-Type-II-normal-form
visibility: public
last_checked: '2026-08-06'
---

# G-anchor 补余 seed 的 \(n-2\) 直接终端筛与 \(R=11\) 因子射线

## 1. 一个与 source receipt 无关的 Type II 模板

设 \(3\le m\le p-2\)、\(m\equiv3\pmod4\)、\(x=(p+m)/4\)，并取正整数 \(d\) 满足

\[
d\mid x^2,
\qquad
d\le x,
\qquad
m\mid x+d.
\tag{1}
\]

定义

\[
y=\frac{p(x+d)}m,
\qquad
z=\frac{p x(x+d)}{md}.
\tag{2}
\]

式 (1) 使两个量均为正整数，而直接计算给出

\[
\frac1x+\frac1y+\frac1z
=\frac1x+\frac{m}{p(x+d)}+\frac{md}{px(x+d)}
=\frac{p+m}{px}
=\frac4p.
\tag{3}
\]

因此 (1) 产生 Type II terminal leaf。这个结论只使用原始 \(p\) 的整除条件；下面把
full-\(Q\) 补余行的 \(d,n\) 当作一个发现 \(m=n-2\) 的提示，**不需要**该行已有
source/path receipt。

## 2. \(c=3\) 分支的 gap-11 Type II 子族

令

\[
p=24h+1,
\qquad
h\not\equiv2\pmod3.
\tag{4}
\]

补余 seed 的数据是 \((d,n)=(3,13)\)。取

\[
m=n-2=11,
\qquad
x=\frac{p+11}{4}=6h+3=3(2h+1),
\qquad
d=3.
\tag{5}
\]

前两个 Type II 条件自动成立，而剩下的整除条件精确为

\[
11\mid x+3
\Longleftrightarrow
11\mid6(h+1)
\Longleftrightarrow
h\equiv10\pmod{11}.
\tag{6}
\]

故对每个满足 (4)、(6) 的核心素数，存在直接证书

\[
\boxed{
\frac4p=
\frac1{6h+3}
+\frac1{6p(h+1)/11}
+\frac1{6p(2h+1)(h+1)/11}.
}
\tag{7}
\]

例如 \(h=10,p=241\) 给出分母

\[
(63,1446,30366).
\tag{8}
\]

在同一固定 \((m,x,d)=(11,6h+3,3)\) 模板中，Type I 所需的条件为

\[
px+3\equiv h^2+h+6\equiv0\pmod{11}.
\tag{9}
\]

该二次式的判别式是 \(-23\equiv10\pmod{11}\)，而 \(10\) 是模 \(11\) 的二次
非剩余。因此该**固定模板**没有任何 Type I 命中；这不排除其它 gap、其它 divisor
或其它 Type I 正规形。

核心 \(c=3\) 域有 \(p\ge73\)，故此处 \(3\le11\le p-2\)，已满足 (1) 的
标准 gap 范围。

## 3. \(c=9\) 分支的 gap-23 Type II 子族

令

\[
h\equiv2\pmod3.
\tag{10}
\]

补余 seed 的数据是 \((d,n)=(9,25)\)。取

\[
m=n-2=23,
\qquad
x=\frac{p+23}{4}=6(h+1),
\qquad
d=9.
\tag{11}
\]

在 (10) 下 \(x\) 为 \(18\) 的倍数，故 \(9\mid x^2\)。余下条件为

\[
23\mid x+9
\Longleftrightarrow
23\mid6h+15
\Longleftrightarrow
h\equiv9\pmod{23}.
\tag{12}
\]

连同 (10)，这等价于 \(h\equiv32\pmod{69}\)。因此有直接 Type II certificate

\[
\boxed{
\frac4p=
\frac1{6(h+1)}
+\frac1{3p(2h+5)/23}
+\frac1{2p(h+1)(2h+5)/23}.
}
\tag{13}
\]

例如 \(h=32,p=769\) 给出

\[
(198,6921,152262).
\tag{14}
\]

同样地，固定 \((m,x,d)=(23,6(h+1),9)\) 的 Type I 条件等价于

\[
6(h+1)^2+9\equiv0\pmod{23}
\Longleftrightarrow
(h+1)^2\equiv10\pmod{23}.
\tag{15}
\]

\(10\) 是模 \(23\) 的二次非剩余，故此固定 Type I 模板也没有解。

核心 \(c=9\) 域有 \(p\ge193\)，故 \(3\le23\le p-2\)。

## 4. 共同 \(R=11\) 图表的固定尾判据

两类补余行的 d-dual 都指向同一张算术图表

\[
R=11,
\qquad
K=\frac{11p+1}{4}=3(22h+1).
\tag{16}
\]

因此

\[
\frac4p=\frac{11}{K}+\frac1{pK}.
\tag{17}
\]

若固定第三分母为 \(pK\)，将第一项拆为 \(1/u+1/v\)。标准因式分解为

\[
(11u-K)(11v-K)=K^2.
\tag{18}
\]

因为 \(K\equiv3\pmod{11}\)，所以 \((K,11)=1\)。从而存在正整数 \(u,v\) 当且仅当
存在一个正 divisor \(e\) 满足

\[
\boxed{
e\mid K^2,
\qquad
e\equiv-K\pmod{11}.
}
\tag{19}
\]

此时可取

\[
u=\frac{K+e}{11},
\qquad
v=\frac{K+K^2/e}{11},
\qquad
\frac4p=\frac1u+\frac1v+\frac1{pK}.
\tag{20}
\]

式 (19)--(20) 是现有固定尾因子条件在共同 \(R=11\) 图表上的专门化；它本身没有
source receipt 前提，但也不自动对每个 \(h\) 成立。

## 5. \(e=19\) 的显式 gap-7 Type I 射线

令 \(e=19\)。条件 (19) 的第一部分等价于

\[
19\mid22h+1
\Longleftrightarrow
h=19a+6.
\tag{21}
\]

在此子族中

\[
p=456a+145,
\qquad
K=57(22a+7),
\qquad
19\equiv-K\pmod{11},
\tag{22}
\]

所以 (20) 已经给出一个直接 terminal。等价地，它有一张特别透明的 gap-7 Type I
正规形：

\[
x=38(3a+1),
\qquad
D=76(3a+1)^2,
\qquad
\frac{x^2}{D}=19,
\tag{23}
\]

且

\[
px+D=7\cdot114(3a+1)(22a+7).
\tag{24}
\]

于是对每个为素数的 \(p=456a+145\)，有

\[
\boxed{
\frac4p=
\frac1{38(3a+1)}
+\frac1{114(3a+1)(22a+7)}
+\frac1{57p(22a+7)}.
}
\tag{25}
\]

这里 \(a\not\equiv2\pmod3\) 时属于 \(c=3\) 支，而 \(a\equiv2\pmod3\) 时属于
\(c=9\) 支；例如 \(a=1,p=601\) 与 \(a=8,p=3793\)。

判据不是自动的。以 \(p=193,h=8\) 为例，\(K=531=3^2\cdot59\)，而 \(K^2\)
的全部除子模 \(11\) 只落在

\[
\{1,3,4,5,9\},
\tag{26}
\]

不含所需的 \(-K\equiv8\pmod{11}\)。这只排除固定 \(pK\) 尾的二项拆分，不否定
该素数的其它 Type I/II certificate。

## 6. 选择器含义与边界

式 (7)、(13) 和 (25) 都是对原始 \(p\) 的直接 terminal leaf；它们应在任何
even-tail source-switch、overflow 或 \(R=11\) RESET 前运行。特别地，(7)、(13)
从补余 determinant 的常数 \(n\) 提取了新的 terminal-first sieve，但不要求把那个
determinant seed 错当作递归状态。

这些结论只覆盖明确的同余子类。两个 Type I 非剩余论证也只排除了各自固定的
\((m,x,d)\) 模板；它们不构成一般 Type I impossibility，更不构成 Erdos--Straus
猜想的证明。
