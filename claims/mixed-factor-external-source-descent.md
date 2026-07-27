---
kind: claim
claim_id: mixed-factor-external-source-descent
title: 混合因子外部源 Type I 证书的严格递降族
statement: 令 p=1 mod24 为素数，k|(p-1)/4，q=4k-1，n=(qp+1)/(q+1)。若 g|kn、g<=n 且 g=-1 modq，则 u=k(n+g)/q、v=nu/g 给出 4/n=1/(kn)+1/u+1/v，并严格提升为 4/p=1/(knp)+1/u+1/v；同时 m=(4kg+1)/q=4u-p、D=u^2/(kg) 是自然范围内的 Type I 除子证书。该族严格包含 g|n 的自适应外部源族，但尚不提供全称参数选择。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- factorization
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

# 混合因子外部源 Type I 证书的严格递降族

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，且

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1}. \tag{1}
\]

设存在正整数 \(g\) 满足

\[
g\mid kn,\qquad g\le n,\qquad g\equiv-1\pmod q. \tag{2}
\]

定义

\[
u=\frac{k(n+g)}q,\qquad v=\frac{nu}{g},
\qquad m=\frac{4kg+1}{q},\qquad D=\frac{u^2}{kg}. \tag{3}
\]

则 (3) 中各量皆为正整数，且

\[
\frac4n=\frac1{kn}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{knp}+\frac1u+\frac1v. \tag{4}
\]

右式同时由缺口 \(m\) 的 Type I 除子证书 \((m,D)\) 恢复；更具体地，

\[
3\le m\le p-2,\qquad 4u-p=m,\qquad D\mid u^2, \tag{5}
\]

并且其余两个恢复分母恰为 \(v\) 与 \(knp\)。因此 (4) 是从严格较小实例
\(n<p\) 出发的一条带标记提升边，也是一张自然范围的显式 Type I 证书。

## 证明

由 (1)，\(n\) 是整数，\(2\le n<p\)，且

\[
4kn=qp+1,\qquad n\equiv1\pmod q. \tag{6}
\]

所以 (2) 蕴含 \(q\mid n+g\)，从而 \(u\) 是整数。又 \(g\mid kn\)，故
\(g\mid k(n+g)\)；由 \(u=k(n+g)/q\) 可得

\[
v=\frac{nu}{g}\in\mathbb N. \tag{7}
\]

此外 \(q\) 分别与 \(k,g\) 互素：前者来自 \(q=4k-1\)，后者来自
\(g\equiv-1\pmod q\)。因此 \(q^2\mid(n+g)^2\) 以及 \(g\mid k(n+g)\)
共同说明

\[
D=\frac{k(n+g)^2}{q^2g}\in\mathbb N. \tag{8}
\]

由 \(v=nu/g\) 与 \(u=k(n+g)/q\)，

\[
\frac1u+\frac1v
=\frac{n+g}{nu}
=\frac q{kn}.
\]

这先证明 (4) 的左半边。再用 (6)，

\[
\frac1{knp}+\frac q{kn}
=\frac{1+qp}{knp}
=\frac4p,
\]

所以替换 \(1/(kn)\) 为 \(1/(knp)\) 确为严格提升。

由 \(4k=q+1\) 和 (6)，

\[
4u-p
=\frac{4k(n+g)-qp}{q}
=\frac{4kg+1}{q}=m. \tag{9}
\]

这也说明 \(m\) 是整数且 \(m\equiv3\pmod4\)。\(g=n\) 与
\(n\equiv1\)、\(g\equiv-1\pmod q\) 矛盾，故 \(g<n\)。再由
\(n-g\equiv2\pmod q\)，有 \(n-g\ge2\)，于是

\[
p-m=\frac{4k(n-g)-2}{q}
\ge\frac{8k-2}{4k-1}=2. \tag{10}
\]

结合 \(m>0\)，即得 (5) 的缺口范围。

最后，\(D=u^2/(kg)\) 显然整除 \(u^2\)，并且直接计算得到

\[
mv-pu
=u\left(\frac{n(4kg+1)}{qg}-p\right)
=\frac{u(n+g)}{qg}
=D, \tag{11}
\]

其中第二个等号使用 \(4kn=qp+1\)。又

\[
u+p\frac{u^2}{D}=u+pkg=mkn. \tag{12}
\]

故 Type I 的两个恢复式分别给出

\[
\frac{pu+D}{m}=v,
\qquad
\frac{p\bigl(u+pu^2/D\bigr)}m=knp.
\]

这证明 \((m,D)\) 是所述 Type I 证书，证毕。

## 严格扩张例子

取

\[
p=97,\qquad k=2,\qquad q=7,\qquad n=85,\qquad g=34.
\]

旧的 `adaptive-external-source-descent` 在这个 \(p\) 上不命中：它要求
\(85\) 本身有 \(-1\pmod7\) 因子。这里 \(34\nmid85\)，但 \(34\mid2\cdot85\)，
并且 \(34\equiv-1\pmod7\)。定理给出

\[
\frac4{85}=\frac1{170}+\frac1{34}+\frac1{85}
\quad\Longrightarrow\quad
\frac4{97}=\frac1{16490}+\frac1{34}+\frac1{85},
\]

以及 Type I 证书

\[
(m,D)=(39,17).
\]

若旧分支中 \(f\mid n\)、\(f\le n/f\)、\(f\equiv-1\pmod q\)，取 \(g=f\)
便满足 (2)，故旧族包含于本定理。上例表明该包含严格。

`test_mixed_factor_external_source_descent` 对所有 \(p\le10^5\) 的核心素数逐一
枚举 \(k\mid(p-1)/4\) 及 \(g\mid kn\)，并验证 (2) 与实现完全等价。在旧自适应族
遗漏的 \(222\) 个点中，新族命中 \(185\) 个。这是精确有限审计，不是密度定理，也不
能推出全称覆盖。

## 边界

旧族可取 \(f\le\sqrt n\)，从而有平方根级缺口界。这里仅有 \(g\le n\)，所以 (10)
只给出自然范围 \(m\le p-2\)，不保证统一次线性界。更重要的是，目前尚未证明每个核心
素数总能选择 \(k\) 与 \(g\) 满足 (2)。故该定理是一条严格扩张的证书/递降分支，
而不是目标引理的全称证明。
