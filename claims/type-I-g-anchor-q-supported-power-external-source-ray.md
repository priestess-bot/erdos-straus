---
kind: claim
claim_id: type-I-g-anchor-q-supported-power-external-source-ray
title: G-anchor Q-supported 幂借用平方外部源射线
statement: >-
  定义平方因子 external-source witness e 的 Q-supported 条件为 rad(e)|Q，
  其中 Q=(p-3)/2；这不同于严格条件 e|Q。令 c=6/gcd(k,6)、q=4k-1。若奇素数
  ell|6k-1 且 ell^j=-k (mod q)，则令 s=ceil(j/2) 并取 c|a0、qa0=-1 (mod ell^s)，
  素数等差列 p=4k(a0+c*ell^s*t)+1 含无穷多个核心素数；除有限初值外，
  e=ell^j 是这些 p 在尺度 k 的 Q-supported 完整平方因子 external-source witness。
  反过来，每个固定 k 的单素数幂 Q-supported witness 都必落在这一 CRT 射线形式。
  特别地，对每个素数 p=3913+15000t、t>=1，取 k=6、q=23、e=5^7，
  有 v5(Q)=1、e 不整除 Q，却有 e|M^2、e<=M、e=-M (mod 23)，并给出
  明确的 Type I 证书和 n<p 的 marked strict lift。故严格 e|Q 的 no-go
  不能升级为 Q-prime-support 的 no-go；未来 G/Type I 选择器必须记录赋值而非只记录素因子支撑。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-strict-q-carried-quadratic-external-source-classification
  - quadratic-factor-external-source-descent
topics:
  - type-I
  - G-state
  - G-anchor
  - complete-excess-bundle
  - external-source
  - quadratic-factor
  - q-supported
  - valuation
  - Dirichlet-ray
  - marked-descent
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: actual-Q-complete-excess-carrier
  - claim: type-I-g-anchor-strict-q-carried-quadratic-external-source-classification
    role: strict-divisibility-boundary
  - claim: quadratic-factor-external-source-descent
    role: complete-square-factor-lift-and-Type-I-certificate-contract
  - reproduction: reproductions/type_i_g_anchor_q_supported_power_external_source_ray.py
    role: fixed-ray-controls-and-certificate-reconstruction
visibility: public
last_checked: '2026-08-16'
---

# G-anchor \(Q\)-supported 幂借用平方外部源射线

## 1. 严格整除与素因子支撑不是同一条件

固定核心素数 \(p\equiv1\pmod{24}\)，并写

\[
Q=\frac{p-3}{2}.
\tag{1}
\]

对一个完整平方因子 external-source witness \(e\)，此前的严格接口要求

\[
e\mid Q.
\tag{2}
\]

本卡把较宽、但常被混同的条件定义为

\[
\operatorname{rad}(e)\mid Q.
\tag{3}
\]

我们称 (3) 为 **\(Q\)-supported**。它允许 \(e\) 从 source denominator 的平方
中借用同一素数的更高赋值。下面的构造说明，严格 \(e\mid Q\) 的分类不能被误读为
\(Q\)-supported witness 的分类。

## 2. 一般幂借用模板

设正整数 \(k\)，并令

\[
 c=\frac6{(k,6)},
 \qquad q=4k-1.
\tag{4}
\]

并取一个奇素数 \(\ell\) 及正整数 \(j\)，满足

\[
\ell\mid6k-1,
\qquad
\ell^j\equiv-k\pmod q.
\tag{5}
\]

令 \(s=\lceil j/2\rceil\)。因为 \(\ell\nmid6k\)，有 \((c,\ell)=1\)，故可取唯一的
\(1\le a_0\le c\ell^s\) 同时满足

\[
 a_0\equiv0\pmod c,
\qquad
qa_0\equiv-1\pmod{\ell^s}.
\tag{6}
\]

对 \(t\ge0\) 定义

\[
a_t=a_0+c\ell^s t,
\qquad
p_t=4ka_t+1.
\tag{7}
\]

**定理（\(Q\)-supported 幂借用）。** 等差列 \(p_t\) 含无穷多个素数。对每个
充分大的素数 \(p_t\)，令

\[
n_t=qa_t+1,
\qquad M_t=kn_t,
\qquad Q_t=\frac{p_t-3}{2}=2ka_t-1,
\qquad e=\ell^j.
\tag{8}
\]

则 \(p_t\) 是核心素数，\(k\mid(p_t-1)/4\)，并且

\[
e\mid M_t^2,
\qquad e\le M_t,
\qquad e\equiv-M_t\pmod q,
\qquad \operatorname{rad}(e)=\ell\mid Q_t.
\tag{9}
\]

因此 \(e\) 是该尺度上的完整平方因子 external-source witness，给出一个显式
\(n_t<p_t\) 的 marked strict lift 和自然范围的 Type I 证书。

**证明。** \(\ell\nmid k\) 显然；若 \(\ell\mid q\)，则
\(3q-2(6k-1)=-1\) 矛盾，故 \(\ell\nmid kq\)，且 \(\ell\ne3\)。
由 (6) 及

\[
q+2k=6k-1\equiv0\pmod\ell
\tag{10}
\]

得到

\[
2ka_t\equiv1\pmod\ell,
\qquad \ell\mid Q_t.
\tag{11}
\]

同时 \(\ell^s\mid n_t\)，故 \(e=\ell^j\mid M_t^2\)，因为 \(j\le2s\)。
又 \(n_t\equiv1\pmod q\)，所以 \(M_t\equiv k\pmod q\)；(5) 正是
\(e\equiv-M_t\pmod q\)。随着 \(t\) 增大，\(M_t\) 线性增大，故 \(e\le M_t\)
除有限多个 \(t\) 外成立。并且 \(p_t-n_t=a_t>0\)，所以 source 确实严格较小。

由 \(c\mid a_t\)，有 \(6\mid ka_t\)，所以 \(p_t\equiv1\pmod{24}\)，而
\((p_t-1)/4=ka_t\)。最后，取 \(p_0=4ka_0+1\)。它与 \(4kc\) 互素；又由 (11)
有 \(p_0\equiv3\pmod\ell\)，故

\[
\gcd(p_0,4kc\ell^s)=1.
\tag{12}
\]

Dirichlet 定理于是给出 (7) 中无穷多个素数。对这些素数，(9) 是
`quadratic-factor-external-source-descent` 的完整输入，结论随之成立。\(\square\)

### 单素数幂的逆向完备性

反过来，固定一个核心素数 \(p\)，令 \(k\mid(p-1)/4\)、
\(q=4k-1\)、\(n=(qp+1)/(q+1)\)、\(M=kn\)、\(Q=(p-3)/2\)。若

\[
e=\ell^j
\]

是一个 \(Q\)-supported 的完整平方因子 witness，则令
\(a=(p-1)/(4k)\)、\(s=\lceil j/2\rceil\)。必有

\[
\ell\mid6k-1,
\qquad
\ell^j\equiv-k\pmod q,
\qquad
c\mid a,
\qquad
qa\equiv-1\pmod{\ell^s}.
\]

确实，\(\operatorname{rad}(e)\mid Q\) 与 \(e\mid M^2\) 给出
\(\ell\mid(Q,M)\)。又 \((Q,k)=1\)，故 \(\ell\mid n\)；既有精确公式
\((Q,M)=(Q,3q+1)\) 遂给 \(\ell\mid3q+1=2(6k-1)\)。\(Q\) 为奇数，
所以 \(\ell\mid6k-1\)。witness 的余类条件及 \(M\equiv k\pmod q\) 给出第二式；
\(\ell\nmid k\) 且 \(e\mid M^2\) 给出 \(\ell^s\mid n=qa+1\)。最后
\(6\mid(p-1)/4=ka\) 等价于 \(c\mid a\)。因此 \(a\) 正是 (6) 的 CRT 类，
而 \(p\) 落在 (7) 的同一射线上。

所以本节的模板对 **单素数幂** \(Q\)-supported witness 是双向精确的；尚未把这个结论
外推至多个 \(Q\)-素数共同构成的 composite witness。

## 3. 一个严格非 \(Q\)-carried 的无穷射线

取

\[
k=6,
\qquad q=23,
\qquad \ell=5,
\qquad j=7.
\tag{13}
\]

这里 \(5\mid6k-1=35\)，并且

\[
5^7\equiv17\equiv-6\pmod{23}.
\tag{14}
\]

取 \(s=4\) 及 \(a_0=163\)，则 \(23\cdot163+1=3750\) 被 \(5^4\) 整除。
模板给出

\[
p=3913+15000t,
\qquad t\ge1.
\tag{15}
\]

由于 \(\gcd(3913,15000)=1\)，该进程含无穷多个素数。对其中任一素数，设

\[
\begin{aligned}
n&=625(23t+6), & M&=3750(23t+6),\\
Q&=5(1500t+391), & e&=5^7,\\
u&=625(6t+7), & v&=30(23t+6)(6t+7),\\
m&=13587, & D&=5(6t+7)^2.
\end{aligned}
\tag{16}
\]

则 \(v_5(Q)=1\)，所以

\[
\operatorname{rad}(e)=5\mid Q,
\qquad e\nmid Q.
\tag{17}
\]

而 \(t\ge1\) 时 \(e\le M\)，并且

\[
e\mid M^2,
\qquad
e\equiv17\equiv-M\pmod{23}.
\tag{18}
\]

所以 (16) 给出直接可检验的两条恒等式

\[
\frac4n=\frac1M+\frac1u+\frac1v,
\qquad
\frac4p=\frac1{pM}+\frac1u+\frac1v.
\tag{19}
\]

此外 \(m=(4e+1)/23\)、\(D=u^2/e\)、\(4u-p=m\)，故 \((m,D)\) 是 Type I
除子证书；\(t\ge1\) 还给出 \(3\le m\le p-2\)。例如 \(t=1\) 时

\[
(p,n,M,Q,e,u,v,m,D)
=(18913,18125,108750,9455,78125,8125,11310,13587,845).
\tag{20}
\]

这不是一个偶然的有限控制：它是一条无限 prime ray，其中 witness 的唯一素数支撑
来自 G-anchor 的 \(Q\)，但其七次幂来自 \(M^2\) 的 source 赋值，而不可能满足
严格 \(e\mid Q\)。

## 4. 对全局选择器的准确影响

严格 \(Q\)-carried no-go 仍然正确：它排除了 `e|Q`。但 future selector 不能把
它提升成“成功平方 witness 必有一个不在 \(Q\) 中的素因子”。上面的无穷射线反而证明：

\[
\boxed{\text{必须区分 prime support 与 \(\ell\)-adic exponent capacity。}}
\tag{21}
\]

因此，若 G-anchor 的 complete-excess bundle 要和 external-source 菜单共用账本，
至少须记录 \(v_\ell(Q)\) 与 \(v_\ell(M)\) 的分离；仅记录 \(\gcd(Q,M)\) 或素因子集合
会漏掉 (16) 的有效 strict lift。

本卡没有证明所有 G/Type I 状态都命中这种幂模板，也没有声称 (15) 的素数在
terminal-first 后都实际进入同一个 G state。它提供的是一条无限、显式的正向 external-source
分支和一个严格的容量边界：任何全称 exit 证明都必须能容纳这种赋值借用，而不能把它误删为
“非 \(Q\)-carried”残余。

## 5. 聚焦回执

~~~bash
python3 reproductions/type_i_g_anchor_q_supported_power_external_source_ray.py --verify
~~~

回执只检查射线中的两个固定素数 \(t=1,4\)，重算 (16)--(20)、严格赋值边界、两条单位
分数恒等式及 Type I 恢复；它不扫描素数、分母或 Reach history。
