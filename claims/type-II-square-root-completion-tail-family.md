---
kind: claim
claim_id: type-II-square-root-completion-tail-family
title: 平方根补全除子给出的 Type II 双尾递降族
statement: 设 m=4q-1、d与m互素，并令 a为满足d|q^2a^2的最小正整数。若t>=1满足t=-4d-1 (mod m)、t=-1 (mod a)、6|qt、d<=q(t+1)，且p=4qt+1为素数，则x=q(t+1)与d构成 Type II 证书，且m+1|p-1，所以双尾去p严格递降至t+1。d|q^2时a=1，故该定理包含q^2因子族。
claim_status: established
topics:
- type-II
- descent
- congruence-certificate
- explicit-family
- square-root-completion
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# 平方根补全除子的 Type II 双尾递降族

令

\[
m=4q-1,\qquad (d,m)=1. \tag{1}
\]

对每个素数 \(\ell\)，记 \(v_\ell\) 为其指数，并定义最小平方根补全因子

\[
a=\prod_\ell \ell^{\max\{0,\lceil(v_\ell(d)-2v_\ell(q))/2\rceil\}}. \tag{2}
\]

等价地，\(a\) 是满足 \(d\mid q^2a^2\) 的最小正整数。若 \(t\ge1\) 满足

\[
t\equiv-4d-1\pmod m,\qquad t\equiv-1\pmod a,
\qquad 6\mid qt,\qquad d\le q(t+1), \tag{3}
\]

且 \(p=4qt+1\) 是素数，则 \(p\equiv1\pmod {24}\)，并有严格双尾递降

\[
p\longrightarrow n=t+1. \tag{4}
\]

## 证明

置 \(x=q(t+1)=(p+m)/4\)。由 (2)--(3)，有

\[
d\mid q^2(t+1)^2=x^2. \tag{5}
\]

而 \(4q=m+1\)，所以 \(q\equiv4^{-1}\pmod m\)。第一条同余给出

\[
x\equiv q(-4d)\equiv-d\pmod m. \tag{6}
\]

于是 \(d\mid x^2\)、\(d\equiv-x\pmod m\) 与 \(d\le x\) 是 Type II 除子判据；
互素性 \((d,m)=1\) 确保补除子同样整除。又 \(m+1=4q\mid p-1\)，故标准双尾去
\(p\) 引理把该证书严格降至 (4)。

当 \(d\mid q^2\) 时，(2) 中 \(a=1\)，正好恢复
[\(q^2\) 因子同余族](type-II-factor-square-tail-descent-family.md)。

## \(m=31\) 的实际残余实例

取 \(q=8,d=7\)。此时 \(m=31\)、\(a=7\)，所以 (3) 为

\[
t\equiv2\pmod {31},\qquad t\equiv-1\pmod7,\qquad 3\mid t. \tag{7}
\]

在

\[
t=2\,803\,593\,722\,609\,700,
\qquad p=89\,714\,999\,123\,510\,401
\]

时，这给出 \(m=31,d=7\) 的 Type II 证书及严格源 \(t+1\)。该点是 H19-k23
有限残余中原 \(m=27\) 而以 \(m=31\) 替代闭合的一条记录。

本定理显式构造算术进程中的递降证书，但没有证明每个给定的核心素数会满足某个
\((q,d,t)\) 的同余系统。

重建命令：

~~~bash
python3 -m unittest tests/test_type_ii_square_root_completion_family.py -q
~~~
