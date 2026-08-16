---
kind: claim
claim_id: type-I-g-anchor-q-supported-power-external-source-ray
title: G-anchor Q-supported 幂借用平方外部源射线
statement: >-
  定义平方因子 external-source witness e 的 Q-supported 条件为 rad(e)|Q，
  其中 Q=(p-3)/2；这不同于严格条件 e|Q。对固定 k，令 q=4k-1，取 6k-1 的
  任意非空素因子集及正指数向量 E，且 E=-k (mod q)。由对应半指数幂 L 和
  c=6/gcd(k,6) 的 CRT 类可构成无穷多个核心素数 p=4k(a0+cLt)+1；除有限初值外，
  E 是这些 p 在尺度 k 的 Q-supported 完整平方因子 external-source witness。
  反过来，每个 Q-supported witness 都唯一落在这种指数向量及 CRT 射线形式。因而
  -k 是否属于由 6k-1 素因子生成的单位群子群，是固定尺度存在 Q-supported prime ray
  的充要条件。
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

## 2. 全 \(Q\)-supported 赋值菜单的 CRT 正规形

设正整数 \(k\)，并令

\[
c=\frac6{(k,6)},
\qquad q=4k-1.
\tag{4}
\]

取 \(6k-1\) 的一个非空素因子集合 \(S\)，并为每个 \(\ell\in S\) 取正整数
\(j_\ell\)。定义

\[
E=\prod_{\ell\in S}\ell^{j_\ell},
\qquad
L=\prod_{\ell\in S}\ell^{\lceil j_\ell/2\rceil}.
\tag{5}
\]

唯一的群论输入是

\[
E\equiv-k\pmod q.
\tag{6}
\]

每个 \(\ell\mid6k-1\) 都与 \(6kq\) 互素：若 \(\ell\mid q\)，则
\(3q-2(6k-1)=-1\) 矛盾。因此 \((c,L)=(L,q)=1\)，可以取唯一的
\(1\le a_0\le cL\) 使

\[
a_0\equiv0\pmod c,
\qquad
qa_0\equiv-1\pmod L.
\tag{7}
\]

对 \(t\ge0\) 定义

\[
a_t=a_0+cLt,
\qquad
p_t=4ka_t+1.
\tag{8}
\]

**定理（全 \(Q\)-supported CRT 正规形）。** 等差列 \(p_t\) 含无穷多个素数。对每个
充分大的素数 \(p_t\)，令

\[
n_t=qa_t+1,
\qquad M_t=kn_t,
\qquad Q_t=\frac{p_t-3}{2}=2ka_t-1.
\tag{9}
\]

则 \(p_t\) 是核心素数，\(k\mid(p_t-1)/4\)，且 \(e=E\) 满足

\[
\operatorname{rad}(e)\mid Q_t,
\qquad e\mid M_t^2,
\qquad e\le M_t,
\qquad e\equiv-M_t\pmod q.
\tag{10}
\]

故 \(e\) 是该尺度上完整平方因子 external-source 的 \(Q\)-supported witness，给出
显式 \(n_t<p_t\) marked strict lift 与自然范围 Type I 证书。

**证明。** 由 (7)，\(L\mid n_t\)。对每个 \(\ell\in S\)，有
\(q\equiv-2k\pmod\ell\)，故 \(qa_t\equiv-1\pmod\ell\) 蕴含

\[
2ka_t\equiv1\pmod\ell,
\qquad \ell\mid Q_t.
\tag{11}
\]

式 (5) 因而逐素数给出 \(E\mid n_t^2\mid M_t^2\)。又
\(n_t\equiv1\pmod q\)，所以 \(M_t\equiv k\pmod q\)，而 (6) 正是
\(E\equiv-M_t\pmod q\)。随着 \(t\) 增大，\(M_t\) 线性增大，故 \(E\le M_t\)
除有限多个 \(t\) 外成立。并且 \(p_t-n_t=a_t>0\)。

由 \(c\mid a_t\)，有 \(6\mid ka_t\)，所以 \(p_t\equiv1\pmod{24}\)，且
\((p_t-1)/4=ka_t\)。取 \(p_0=4ka_0+1\)。它与 \(4kc\) 互素，且由 (11) 对
每个 \(\ell\in S\) 都有 \(p_0\equiv3\pmod\ell\)，故

\[
\gcd(p_0,4kcL)=1.
\tag{12}
\]

Dirichlet 定理给出 (8) 中无穷多个素数；(10) 遂成为
`quadratic-factor-external-source-descent` 的完整输入。\(\square\)

### 逆向完备性

反过来，固定核心素数 \(p\)，令 \(k\mid(p-1)/4\)、
\(q=4k-1\)、\(n=(qp+1)/(q+1)\)、\(M=kn\)、\(Q=(p-3)/2\)。若 \(e\) 是
一个 \(Q\)-supported 的完整平方因子 witness，写

\[
e=\prod_{\ell\in S}\ell^{j_\ell}
\]

为其素因子分解。则每个 \(\ell\in S\) 同时整除 \(Q,M\)。由 \((Q,k)=1\)，
\(\ell\mid n\)；再由精确交集

\[
(Q,M)=(Q,3q+1)
\]

可知 \(\ell\mid3q+1=2(6k-1)\)。\(Q\) 为奇数，故 \(S\) 正是 \(6k-1\)
的奇素因子子集。witness 余类及 \(M\equiv k\pmod q\) 给出 (6)。同时
\(e\mid M^2\) 给 \(L\mid n=qa+1\)，其中 \(a=(p-1)/(4k)\)；核心同余给
\(c\mid a\)。因此 \(a\) 必在 (7) 的唯一 CRT 类中，\(p\) 也必在 (8) 的射线上。

这说明 (4)--(10) 对 **所有** \(Q\)-supported witness 都是双向精确的，而不只是
单素数幂。

### 固定尺度的有限群门

令

\[
\Gamma_k=
\left\langle\ell\bmod(4k-1):\ \ell\text{ 为 }6k-1\text{ 的素因子}\right\rangle
\subseteq(\mathbb Z/(4k-1)\mathbb Z)^\times.
\]

则存在一条尺度 \(k\) 的 \(Q\)-supported external-source prime ray，当且仅当

\[
\boxed{-k\bmod(4k-1)\in\Gamma_k.}
\]

必要性由逆向完备性直接给出。反过来，有限群中的任意负指数可用该元素的有限阶改写为
非负指数；\(-k\not\equiv1\pmod{4k-1}\)，故删去零指数后仍得到非空的 (5)--(6)，
并应用正向模板。故这个群成员资格是
\(Q\)-supported 分支的完整、固定尺度选择门；它不保证给定 \(p\) 已落在相应 CRT 类。

## 3. 一个严格非 \(Q\)-carried 的单素数幂射线

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

## 4. 双素数赋值借用控制

同一尺度 \(k=6\) 已有真正的 composite control。取

\[
S=\{5,7\},
\qquad
E=5^3 7^6=14706125,
\qquad
L=5^2 7^3=8575.
\]

则 \(E\equiv17\equiv-6\pmod{23}\)，且 \(a_0=6338\) 满足
\(23a_0+1=17L\)。对应射线为

\[
p=152113+205800t,
\qquad
n=8575(23t+17),
\qquad
M=51450(23t+17).
\]

这里

\[
Q=35(2173+2940t),
\qquad
v_5(Q)=v_7(Q)=1.
\]

所以两个 \(Q\)-素数都可在 \(M^2\) 中被放大；当 \(t\ge12\) 时 \(E\le M\)。例如
\(t=16\) 给出素数

\[
(p,n,M,Q,E,u,v,m,D)
=(3444913,3301375,19808250,1722455,14706125,
1500625,2021250,2557587,153125).
\]

它满足两条 external-source 单位分数恒等式和 \((m,D)\) Type I 证书。这里
\(E\nmid Q\)，但 \(\operatorname{rad}(E)=35\mid Q\)。因此这个控制排除了另一种
错误简化：不能把完整 \(Q\)-supported 菜单拆成互不相干的单素数幂菜单。

## 5. 对全局选择器的准确影响

严格 \(Q\)-carried no-go 仍然正确：它排除了 `e|Q`。但 future selector 不能把
它提升成“成功平方 witness 必有一个不在 \(Q\) 中的素因子”。上面的无穷射线反而证明：

\[
\boxed{\text{必须区分 prime support、各 \(\ell\)-adic capacity 与其 residue product。}}
\tag{21}
\]

因此，若 G-anchor 的 complete-excess bundle 要和 external-source 菜单共用账本，
至少须记录每个 \(v_\ell(Q)\)、\(v_\ell(M)\) 及其模 \(q\) 乘积；仅记录
\(\gcd(Q,M)\) 或素因子集合会漏掉 (16) 及本节的有效 strict lift。

本卡没有证明所有 G/Type I 状态都命中这种幂模板，也没有声称 (15) 的素数在
terminal-first 后都实际进入同一个 G state。它提供的是一条无限、显式的正向 external-source
分支和一个严格的容量边界：任何全称 exit 证明都必须能容纳这种赋值借用，而不能把它误删为
“非 \(Q\)-carried”残余。

## 6. 聚焦回执

~~~bash
python3 reproductions/type_i_g_anchor_q_supported_power_external_source_ray.py --verify
~~~

回执只检查单素数射线中的两个固定素数 \(t=1,4\)，以及本节的双素数 \(p=3444913\)
控制，重算严格赋值边界、两条单位分数恒等式及 Type I 恢复；它不扫描素数、分母或
Reach history。
