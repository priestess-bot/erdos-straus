---
kind: claim
claim_id: shifted-quadratic-factor-external-source-descent
title: 非零平移下平方因子外部源的完整 Type I 递降族
statement: 令 p=1 mod24 为素数，0<d<p，p=d mod4k，q=4k-1，n=(qp+d)/(q+1)，M=kn。若 d|M，且 e|M^2、e<=M、d|e、q|M+e、q|M+M^2/e，则 u=(M+e)/q、v=Mu/e 给出 4/n=1/M+1/u+1/v，并严格提升为 4/p=1/(Mp/d)+1/u+1/v；m=(4e+d)/q=4u-p、D=du^2/e 是自然范围的 Type I 证书。固定源的全部二项尾仍由 (qu-M)(qv-M)=M^2 参数化，附加 d|e 精确刻画其中恢复为该 Type I 证书的部分。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- factorization
- unit-fractions
- shifted-source
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

# 非零平移下平方因子外部源的完整 Type I 递降族

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，取正整数 \(k,d\) 满足

\[
0<d<p,\qquad p\equiv d\pmod{4k},\qquad q=4k-1,
\qquad n=\frac{qp+d}{q+1},\qquad M=kn. \tag{1}
\]

假设 \(d\mid M\)，并存在正整数 \(e\) 使

\[
e\mid M^2,\qquad e\le M,\qquad d\mid e,
\qquad q\mid M+e,\qquad q\mid M+\frac{M^2}{e}. \tag{2}
\]

定义

\[
u=\frac{M+e}{q},\qquad v=\frac{Mu}{e},
\qquad m=\frac{4e+d}{q},\qquad D=\frac{du^2}{e}. \tag{3}
\]

则这些量均为正整数，且

\[
\frac4n=\frac1M+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{Mp/d}+\frac1u+\frac1v. \tag{4}
\]

同时 \((m,D)\) 是 Type I 除子证书，且

\[
3\le m\le p-2,\qquad4u-p=m. \tag{5}
\]

当 \(d=1\) 时，这正是 `quadratic-factor-external-source-descent`。固定
\(p,k,d,M\) 后，不带 \(d\mid e\) 限制的 (2) 前两项及两个模条件恰好参数化所有
按 \(u\le v\) 排序的尾项 \(q/M=1/u+1/v\)；附加 \(d\mid e\) 精确刻画其中
恢复为 (3) 所示 Type I 证书的部分。

## 证明

由 (1)，\(2\le n<p\) 且

\[
4M=qp+d. \tag{6}
\]

由 \(d\mid M\)、(6) 及 \(d<p\) 可得 \(d\mid q\)：因为 \(d\mid qp\)，
且 \(p\) 为素数、\(d<p\)。写 \(q=dr\)。又 \(p\equiv d\pmod4\)、
\(q\equiv3\pmod4\)，所以 \(d\equiv1\pmod4\)、\(r>1\) 为奇数。由于
\(\gcd(d,q+1)=1\)，(1) 还给出 \(d\mid n\)。故可写

\[
n=dn_1,\qquad M=dM_1,\qquad e=de_1. \tag{7}
\]

两个模条件确保

\[
u=\frac{M+e}{q},\qquad
v=\frac{M+M^2/e}{q}=\frac{Mu}{e}
\]

均为正整数。于是

\[
\frac1u+\frac1v=\frac{M+e}{Mu}=\frac qM,
\]

从而得到 (4) 的左式。又

\[
\frac1{Mp/d}+\frac qM
=\frac{d+qp}{Mp}=\frac{4M}{Mp}=\frac4p. \tag{8}
\]

所以 (4) 成立。

由 \((q+1)n=qp+d\) 得 \(n\equiv d\pmod q\)，故
\(M\equiv kd\pmod q\)。第一个模条件给出 \(e\equiv-kd\pmod q\)，从而

\[
4u-p=\frac{4(M+e)-qp}{q}=\frac{4e+d}{q}=m. \tag{9}
\]

为验证自然范围，(7) 的第一个模条件给出 \(r\mid M_1+e_1\)。由
\((q+1)n=d(rp+1)\) 可得 \(n_1\equiv1\pmod r\)，所以
\(M_1\equiv k\pmod r\)。又 \(4k=dr+1\)，故

\[
2k\equiv\frac{r+1}{2}\pmod r.
\]

于是 \(M_1-e_1\equiv(r+1)/2\pmod r\)。它不可能为零（否则
\(r\mid2k\)，与 \(r>1\)、\(\gcd(k,r)=1\) 矛盾），所以
\(M_1-e_1\ge(r+1)/2\)。因此

\[
p-m
=\frac{4(M-e)-2d}{q}
=\frac{4(M_1-e_1)-2}{r}
\ge2. \tag{10}
\]

结合 \(m>0\) 即得 (5)。

再由 \(v=Mu/e\)、\(qp=4M-d\)，

\[
mv-pu
=u\left(\frac{M(4e+d)}{qe}-p\right)
=\frac{du(M+e)}{qe}=D. \tag{11}
\]

而 \(u^2/D=e/d\)，并且

\[
qd\left(u+\frac{pe}{d}\right)
=d(M+e)+pqe
=M(d+4e)=qmM. \tag{12}
\]

所以 Type I 的两个恢复分母是

\[
\frac{pu+D}{m}=v,
\qquad
\frac{p\bigl(u+pu^2/D\bigr)}m
=\frac{p(u+pe/d)}m=\frac{Mp}{d}.
\]

式 (12) 即给出第二个等式。又 \(D=u^2/(e/d)\)，所以 \(D\mid u^2\)。
这证明证书部分。

尾项完备性仍来自恒等式

\[
(qu-M)(qv-M)=M^2. \tag{14}
\]

它给出全部 \(e=qu-M\) 的因子和两项模条件；反向代入即可恢复尾项。由 (11)
\(u^2/D=e/d\)，故这类尾项恢复为这里的 Type I 证书当且仅当 \(d\mid e\)。

## 例子与边界

取

\[
p=8329,\quad k=160,\quad d=9,\quad q=639,\quad n=8316,
\quad e=4950.
\]

则

\[
\frac4{8316}=\frac1{1330560}+\frac1{2090}+\frac1{561792}
\quad\Longrightarrow\quad
\frac4{8329}=\frac1{1231359360}+\frac1{2090}+\frac1{561792},
\]

并得到 \((m,D)=(31,7942)\)。`test_shifted_quadratic_factor_external_source_descent`
还逐一审计固定射线 \((k,d)=(19,5)\) 在 \(p\le10^5\) 的全部可用核心素数，验证
条件 (2) 与程序输出精确等价。

该定理扩展了零平移和先前 \(e=kf\) 的平移构造，却没有给出对所有 \(p\) 的
\((k,d,e)\) 选择器。因此仍不是目标引理的全称证明。
