---
kind: claim
claim_id: two-denominator-lift-core-rank-one-no-go
title: p 减一秩的非自然 D-only 标记纤维全域空定理
statement: 设 p 为满足 p=1 (mod 4) 的奇素数，n=p-1，并取任意 non-source-supported D-only 参数。将其正规化为 mu=4lambda-1、H=p+mu 整除 4lambda^2、s=4lambda^2/H<lambda 后，标记非空性的三个平方除子目标均无解。更精确地，写 s=a^2c、lambda=abc、(a,b)=1、a<b，则 H=4b^2c、p=4bc(b-a)+1；后两个目标由大小立即排除，第一个目标若命中会导出 4ah=a^2/m+h^2/k+1/c，而 Vieta 下降证明该正整数方程无解。因此 W(p,p-1,D) 恒空。source-supported 分支仍只等价于原中心 Type I 命中，所以 n=p-1 不能提供新的 D-only 递归出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
topics:
  - descent
  - marked-solution
  - two-denominator-lift
  - D-only
  - rank-one
  - three-target-spectrum
  - Vieta-jumping
  - no-go
sources:
  - claim: two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
    role: non-source-normal-form-and-three-target-interface
visibility: public
last_checked: '2026-08-01'
---

# \(p-1\) 秩的非自然 \(D\)-only 标记纤维全域空定理

## 1. 命题范围

设 \(p\) 为奇素数，满足

\[
p\equiv1\pmod4,
\qquad
n=p-1.
\tag{1}
\]

取任意 non-source-supported \(D\)-only 参数

\[
D\in\mathcal D(p,n),
\qquad
D\nmid n^2.
\tag{2}
\]

先说明这里使用的正规形范围。通用 \(D\)-only 参数化对任意奇素数都成立：
在 non-source-supported 分支写 \(D=pd\)，消去 \(d\) 后可得
\(\mu=4\lambda-1\) 以及
\[
H=p+\mu,\qquad H\mid4\lambda^2.
\]
这个代数步骤不使用 \(p\equiv1\pmod {24}\)；核心正规形卡以模 \(24\) 类陈述，只是
因为其选择器应用固定在核心素数。因此这里可在本卡较弱的
\(p\equiv1\pmod4\) 假设下直接使用

\[
\mu=4\lambda-1,
\qquad
H=p+\mu,
\qquad
H\mid4\lambda^2.
\tag{3}
\]

令

\[
s=\frac{4\lambda^2}{H}.
\tag{4}
\]

正规形中的正性条件 \(t=\lambda-s>0\) 给出

\[
0<s<\lambda.
\tag{5}
\]

本卡证明

\[
\boxed{W(p,p-1,D)=\varnothing.}
\tag{6}
\]

证明只使用 \(p\equiv1\pmod4\)，所以范围严格强于核心条件
\(p\equiv1\pmod {24}\)。

## 2. \(s,\lambda,H,p\) 的互素参数化

由 \(\mu\equiv3\pmod4\) 和 (1) 可知

\[
4\mid H.
\]

结合 (4)，得到

\[
s\mid\lambda^2.
\tag{7}
\]

令 \(g=(s,\lambda)\)，写

\[
s=ga,
\qquad
\lambda=gb,
\qquad
(a,b)=1,
\qquad
a<b.
\tag{8}
\]

由 (7) 有 \(a\mid g\)，再写 \(g=ac\)。于是

\[
\boxed{
s=a^2c,
\qquad
\lambda=abc,
\qquad
H=4b^2c,
\qquad
p=4bc(b-a)+1.}
\tag{9}
\]

以下固定

\[
B=b^2c,
\qquad
\mu=4abc-1.
\tag{10}
\]

由 (9)--(10) 有

\[
p\lambda\equiv B\pmod\mu,
\qquad
p^{-1}\lambda\equiv s\pmod\mu.
\tag{11}
\]

所以三个规范目标化为

\[
\boxed{
\begin{array}{c|c}
e&u\pmod\mu\\ \hline
0&-B\\
1&-\lambda\\
2&-s
\end{array}}
\tag{12}
\]

其中 \(u\mid\lambda^2\)，并可由互补规范到 \(0<u\le\lambda\)。

## 3. 两个目标由大小直接排除

对 \(0<u<\lambda\)，\(e=1\) 的最小正剩余为

\[
\mu-\lambda=3\lambda-1>\lambda.
\]

而 \(s<\lambda\)，故 \(e=2\) 的最小正剩余满足

\[
\mu-s>3\lambda-1>\lambda.
\]

所以这两个目标都不可能命中。

还需处理互补中点 \(u=\lambda\)。在 \(e=1\) 中，它会要求
\(\mu\mid2\lambda\)，但 \(\mu=4\lambda-1>2\lambda\)。在 \(e=2\) 中，它会
要求 \(\mu\mid\lambda+s\)，而

\[
0<\lambda+s<2\lambda<\mu.
\]

\(e=0\) 的中点与 \(e=2\) 互补等价，故中点也全部排除。现在只需处理

\[
u\mid\lambda^2,
\qquad
0<u<\lambda,
\qquad
u\equiv-B\pmod\mu.
\tag{13}
\]

## 4. 第一个目标导出的 Vieta 方程

假设 (13) 有解。写

\[
u+B=k\mu,
\qquad
k\in\mathbb N,
\tag{14}
\]

并定义

\[
h=4ak-b.
\tag{15}
\]

由 (10)、(14)--(15)，

\[
u=bch-k.
\tag{16}
\]

\(u>0\) 给出 \(h\ge1\)。另一方面，

\[
k\mu=B+u<B+\lambda=bc(a+b).
\]

因 \(\mu=4abc-1>a+b\)，有 \(k<bc\)。若 \(h>a\)，则 (16) 与
\(u<abc\) 会给出 \(bc<k\)，矛盾。因此

\[
1\le h\le a.
\tag{17}
\]

令互补因子

\[
v=\frac{\lambda^2}{u}.
\tag{18}
\]

因为 \(Bs=\lambda^2\)、\((u,\mu)=1\)，式 (14) 推出唯一正整数 \(m\) 满足

\[
v+s=m\mu.
\tag{19}
\]

将 (14)、(18)--(19) 相乘并消去 \(\mu\)，得到

\[
um=sk=a^2ck.
\tag{20}
\]

把 (16) 代入 (20)，再用 \(b=4ak-h\)，可化为

\[
\boxed{
4ah=\frac{a^2}{m}+\frac{h^2}{k}+\frac1c.}
\tag{21}
\]

## 5. Vieta 下降排除正整数解

假设 (21) 存在正整数解，取 \(a+h\) 最小的一组。方程在

\[
(a,m)\longleftrightarrow(h,k)
\]

下对称，所以不妨设 \(a\ge h\)。定义

\[
f(X)=\frac{X^2}{m}-4hX+\frac{h^2}{k}+\frac1c.
\tag{22}
\]

\(a\) 是 \(f\) 的一个根，并且

\[
f(0)>0,
\qquad
f(h)=h^2\left(\frac1m+\frac1k-4\right)+\frac1c
\le-2h^2+1\le-1.
\tag{23}
\]

所以一个根严格位于 \((0,h)\)，而 \(a\ge h\) 必为较大根。由 Vieta 公式，另一根为

\[
a'=4hm-a.
\tag{24}
\]

它是整数，并满足

\[
0<a'<h.
\]

于是 \((a',h,m,k,c)\) 仍是 (21) 的一组正整数解，却有

\[
a'+h<a+h,
\]

与极小性矛盾。故 (21) 无正整数解，(13) 也无解。结合第 3 节，三个目标全部为空，
从而证明 (6)。

## 6. 对选择器的含义

source-supported 分支 \(D\mid n^2\) 已知精确等价于原 \(p\) 图表的中心 Type I 命中；
这一消元同样只使用奇素数正规形，不使用模 \(24\) 假设。
本卡再证明 non-source-supported 分支在 \(n=p-1\) 时标记集恒空。因此

\[
\boxed{
n=p-1\text{ 只能复述已有直接 Type I，不能产生新的 }D\text{-only E4}.}
\tag{25}
\]

例如 \((p,n,D)=(73,72,2628)\) 对应

\[
(a,b,c,\lambda,H,s)=(1,2,9,18,144,9),
\]

其三个目标确实全部 miss。负 Pell 正例位于 \(p\equiv7\pmod8\)，此时
\(4\nmid H\)，不满足本证明的关键步骤 (7)，所以不存在冲突。

该 no-go 只删除 \(r=p-n=1\) 层；\(r\ge2\) 的大尺度 \(D\)-only 三目标问题仍然开放。
