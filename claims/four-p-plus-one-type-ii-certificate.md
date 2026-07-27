---
kind: claim
claim_id: four-p-plus-one-type-ii-certificate
title: 来自 4p+1 的显式 Type II 证书
statement: 对核心素数 p=1 mod 24，若 4p+1 有 q=3 mod 4 的素因子，取最小此类 q，设 h=(q+1)/4、m=(p+4h^2)/q、x=(p+m)/4；则 d=min(h^2,(m-h)^2) 给出 Type II 证书，且 3<=m<=p-2。
claim_status: established
topics:
- certificate
- type-II
- factorization
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1 and equations (4)--(6)"
  role: parametric-Type-II-form
- paper: bradford2024
  locator: "Proposition 2"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 来自 \(4p+1\) 的显式 Type II 证书

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，且令 \(q\) 是 \(4p+1\) 的最小
\(3\pmod4\) 素因子。设

\[
h=\frac{q+1}{4},\qquad
m=\frac{p+4h^2}{q},\qquad
x=\frac{p+m}{4}=h(m-h),
\]

并取

\[
d=\min\{h^2,(m-h)^2\}.
\]

则 \((m,d)\) 是 `short-certificate-equivalence` 中的 Type II 证书：

\[
d\mid x^2,\qquad d\le x,\qquad m\mid x+d.
\]

特别地，\(3\le m\le p-2\)、\(m\equiv3\pmod4\)，故它是合法的 Bradford
缺口。恢复出的分母由标准 Type II 公式给出：

\[
x,\qquad \frac{p(x+d)}m,\qquad \frac{p(x+x^2/d)}m.
\]

这是 Chamberland 的形状 \(p=qm-4h^2\)（取 \(s_1=s_2=h\)）的一个受限、
可直接验证的实例；下述证明也独立核对了它落在首分母缺口的自然范围内。

## 证明

由 \(q\mid4p+1\) 和 \(16h^2=(q+1)^2\equiv1\pmod q\)，有

\[
p+4h^2\equiv-\frac14+\frac14\equiv0\pmod q,
\]

所以 \(m\) 是正整数，且 \(p=qm-4h^2\)。模 \(4\) 化简得到
\(3m\equiv1\pmod4\)，即 \(m\equiv3\pmod4\)。又

\[
m-h=\frac{p+h}{q}>0,
\]

从而 \(x=h(m-h)>0\)，且 \(4x=p+m\)。两个数 \(h^2\) 与 \((m-h)^2\)
都是 \(x^2\) 的除子，并且

\[
x\equiv-h^2\equiv-(m-h)^2\pmod m.
\]

两者中较小的一个不超过几何平均数 \(h(m-h)=x\)，故所取 \(d\) 满足全部
Type II 整除条件。

尚需验证缺口范围。核心素数的最小值为 \(73\)。由于 \(p\equiv1\pmod3\)，
\(3\nmid4p+1\)，故 \(q\ge7\)。又 \(4p+1\equiv1\pmod4\)，所有
\(3\pmod4\) 素因子的总指数为偶数；最小性给出 \(q^2\le4p+1\)。在区间
\(7\le q\le\sqrt{4p+1}\) 上，

\[
m=\frac pq+\frac{(q+1)^2}{4q}
\]

是凸函数，故其最大值在端点取得。两端分别为

\[
\frac p7+\frac{16}{7},\qquad
\frac{\sqrt{4p+1}+1}{2},
\]

且对 \(p\ge73\) 都不超过 \(p-2\)。结合正性和 \(m\equiv3\pmod4\)，即
\(3\le m\le p-2\)。

这里第一项的不等式等价于 \(p\ge5\)；对第二项，只需注意
\(\sqrt{4p+1}\le2p-5\)，因为其平方差为
\(4(p^2-6p+6)>0\)（\(p\ge73\)）。

## 剩余集与限制

这个分支未覆盖的核心素数必须使 \(4p+1\) 的每个素因子都为 \(1\pmod4\)。
它与 \((p+1)/2\)、\(p+4\) 和 \(m=3\) 的分支相交但不包含彼此。例如
\(p=313\) 取 \(q=7\)，得到 \((m,x,d)=(47,90,4)\)；\(p=1201\) 取
\(q=31\)，得到 \((47,312,64)\)。该充分条件不证明剩余集为空，也不是递降。
