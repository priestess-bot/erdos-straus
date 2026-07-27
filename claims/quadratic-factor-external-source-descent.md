---
kind: claim
claim_id: quadratic-factor-external-source-descent
title: 平方因子外部源的完整二项尾递降参数化
statement: 令 p=1 mod24 为素数，k|(p-1)/4，q=4k-1，n=(qp+1)/(q+1)，M=kn。若 e|M^2、e<=M 且 e=-M modq，则 u=(M+e)/q、v=Mu/e 给出 4/n=1/M+1/u+1/v，并严格提升为 4/p=1/(Mp)+1/u+1/v；m=(4e+1)/q=4u-p、D=u^2/e 是自然范围的 Type I 证书。反之，固定 M 后每个按 u<=v 排序的二项尾 q/M=1/u+1/v 都唯一来自这样的 e=qu-M。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- factorization
- unit-fractions
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-reconstruction
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-context
visibility: public
last_checked: '2026-07-24'
---

# 平方因子外部源的完整二项尾递降参数化

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，且

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad M=kn. \tag{1}
\]

若正整数 \(e\) 满足

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod q, \tag{2}
\]

定义

\[
u=\frac{M+e}{q},\qquad v=\frac{Mu}{e},
\qquad m=\frac{4e+1}{q},\qquad D=\frac{u^2}{e}. \tag{3}
\]

则各量均为正整数，且

\[
\frac4n=\frac1M+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{Mp}+\frac1u+\frac1v. \tag{4}
\]

同时 \((m,D)\) 是 Type I 除子证书，满足

\[
3\le m\le p-2,\qquad 4u-p=m. \tag{5}
\]

固定 \(p,k\) 和被保留的第一分母 \(M=kn\) 后，(2) 与所有按 \(u\le v\) 排序的
二项尾

\[
\frac qM=\frac1u+\frac1v \tag{6}
\]

一一对应，对应参数为 \(e=qu-M\)。故它穷尽了这个外部源、这个被保留分母上的二项尾，
不是一个特殊的充分条件。

## 证明

由 (1)，

\[
4M=qp+1,\qquad n\equiv1\pmod q,\qquad\gcd(M,q)=1. \tag{7}
\]

条件 (2) 先给出 \(q\mid M+e\)。令 \(\bar e=M^2/e\)。由 \(e\equiv-M\pmod q\)
和 \(M\) 在模 \(q\) 下可逆，\(\bar e\equiv-M\pmod q\)。因此

\[
u=\frac{M+e}{q},\qquad v=\frac{M+\bar e}{q}=\frac{Mu}{e}
\]

都是正整数。又 \(q\) 与 \(e\) 互素，且
\((M+e)^2\equiv M^2\equiv0\pmod e\)，故 \(D=u^2/e\) 也是整数。

现在

\[
\frac1u+\frac1v=\frac{M+e}{Mu}=\frac qM,
\]

所以得到 (4) 的左式；结合 \(qp+1=4M\)，

\[
\frac1{Mp}+\frac qM=\frac{1+qp}{Mp}=\frac4p,
\]

得到严格提升。又因 \(M\equiv k\pmod q\)、\(e\equiv-k\pmod q\)，\(m\) 为整数，且

\[
4u-p=\frac{4(M+e)-qp}{q}=\frac{4e+1}{q}=m. \tag{8}
\]

\(e=M\) 会推出 \(2M\equiv0\pmod q\)，与 (7) 矛盾，故 \(e<M\)。进一步

\[
M-e\equiv2M\equiv2k\pmod q.
\]

由于 \(0<2k<q=4k-1\)，有 \(M-e\ge2k\)，因而

\[
p-m=\frac{4(M-e)-2}{q}
\ge\frac{8k-2}{4k-1}=2. \tag{9}
\]

这给出 (5)。最后，使用 \(v=Mu/e\) 及 \(qp=4M-1\)，

\[
mv-pu
=u\left(\frac{M(4e+1)}{qe}-p\right)
=\frac{u(M+e)}{qe}=D, \tag{10}
\]

以及

\[
q(u+pe)=M+e+pqe=M(4e+1)=qmM. \tag{11}
\]

所以 Type I 的两个恢复式恰为

\[
\frac{pu+D}{m}=v,
\qquad
\frac{p\bigl(u+pu^2/D\bigr)}m=\frac{p(u+pe)}m=Mp.
\]

这证明了证书部分。

反之，若 (6) 成立，则清分母并配方：

\[
(qu-M)(qv-M)=M^2. \tag{12}
\]

令 \(e=qu-M\)。两项皆正，故 \(e>0\)；由 \(u\le v\) 有
\(e\le qv-M=M^2/e\)，所以 \(e\le M\)。式 (12) 给出 \(e\mid M^2\) 和
\(e\equiv-M\pmod q\)。反向构造已证，且 \(e=qu-M\) 唯一，故对应完整。

## 与较窄分支的关系

`mixed-factor-external-source-descent` 是本定理的特例 \(e=kg\)：由
\(g\mid kn\)、\(g\le n\)、\(g\equiv-1\pmod q\) 可知 (2) 成立。更早的
`adaptive-external-source-descent` 再限制 \(g\mid n\)。

同一个 \(k\) 切片确实可以出现更宽的平方因子。例如

\[
p=409,\quad k=6,\quad q=23,\quad n=392,\quad M=2352,\quad e=63
\]

满足 (2)，而 \(63\) 不是 \(6g\) 形。于是

\[
\frac4{392}=\frac1{2352}+\frac1{105}+\frac1{3920}
\quad\Longrightarrow\quad
\frac4{409}=\frac1{961968}+\frac1{105}+\frac1{3920},
\]

并有 Type I 证书 \((m,D)=(11,175)\)。

`test_quadratic_factor_external_source_descent` 在 \(p\le10^5\) 上精确枚举全部
\(k\mid(p-1)/4\) 和 \(e\mid(kn)^2\)。它在混合因子族遗漏的 37 个点中额外命中 21 个，
留下 16 个：

\[
5209,8329,18169,21169,27481,31849,33529,39769,
48409,52369,68329,73849,80809,87481,88729,94009.
\]

这是有限审计，不能推至全体素数。

## 边界

本定理已穷尽固定 \(k\) 时保留 \(kn\) 的二项尾。因此某个 \(p\) 对所有
\(k\mid(p-1)/4\) 都失败时，继续搜索同一 \(n=(qp+1)/(q+1)\) 和同一被保留分母
不会得到新递降；必须改变源、改变被保留分母，或使用另一类 Type I/II 证书。它仍未证明
每个核心素数至少有一个成功的 \(k\)，故不是目标引理的全称选择器。
