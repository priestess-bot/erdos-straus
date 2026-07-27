---
kind: claim
claim_id: shifted-quadratic-tail-normalization
title: 平移平方外源的缩放平方尾正规形
statement: 在平移平方外源的兼容状态中，写 q=st、n=sN、M=sL。所有可用平方尾因子唯一写成 e=sf，且完整尾条件等价于 f|L^2、f<=L、f=-L mod t；目标 Type I 缺口为 (4f+1)/t，目标首分母为 pL。
claim_status: established
topics:
- type-I
- descent
- external-source
- factorization
- unit-fractions
- parametrization
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 平移平方外源的缩放平方尾正规形

在[平移平方外源射线的源距离因子参数化](shifted-quadratic-source-distance-parametrization.md)
中，令

$$
q=st,\qquad n=sN,\qquad M=kn=sL,\qquad L=kN.
$$

这里 $s$ 是偏移，$q=4k-1$。原完整平移平方尾要求一个因子 $e$ 满足

$$
e\mid M^2,\qquad e\le M,\qquad s\mid e,\qquad
q\mid M+e,\qquad q\mid M+M^2/e. \tag{1}
$$

## 定理

式 (1) 的因子唯一写成 $e=sf$，并且它等价于单一的平方因子残数条件

$$
f\mid L^2,\qquad f\le L,\qquad f\equiv-L\pmod t. \tag{2}
$$

令

$$
u=\frac{L+f}{t},\qquad v=\frac{Lu}{f}.
$$

则源和目标恒等式为

$$
\frac4n=\frac1{sL}+\frac1u+\frac1v,
\qquad
\frac4p=\frac1{pL}+\frac1u+\frac1v. \tag{3}
$$

相应 Type I 证书的参数不再含 $s$：

$$
m=\frac{4f+1}{t},\qquad D=\frac{u^2}{f}. \tag{4}
$$

## 证明

由 $s\mid e$ 写 $e=sf$。令 $A=M^2/e=sL^2/f$。式 (1) 的第二个同余中，
$q=st$ 与 $M=sL$ 都被 $s$ 整除，因此 $s\mid A$。于是
$L^2/f=A/s$ 是整数，即 $f\mid L^2$。第一个同余除以 $s$ 给出
$f\equiv-L\pmod t$。

还要说明第二个同余已经被前者强制。由 $t\mid4k-1$ 可知 $\gcd(k,t)=1$；又
$N=dt+1$，所以 $\gcd(N,t)=1$，从而 $\gcd(L,t)=1$。令 $g=L^2/f$。在模 $t$ 下，
由 $fg=L^2$ 和 $f\equiv-L$ 得

$$
g\equiv L^2(-L)^{-1}\equiv-L\pmod t.
$$

故 $t\mid L+g$，正是原来的第二个尾同余。反向乘回 $s$ 也恢复式 (1)。

## 残数集推论

记

$$
\Pi_t(L^2)=\{a\bmod t: a\mid L^2\}.
$$

则存在满足式 (2) 的排序因子 $f\le L$ 当且仅当

$$
-L\bmod t\in\Pi_t(L^2). \tag{5}
$$

事实上，若任意因子 $f\mid L^2$ 命中 $-L$，则其补因子 $g=L^2/f$ 也命中同一
残差；$f,g$ 之一不大于 $L$。反向显然。这说明大小约束不是另一个选择障碍。
两亿压力集中“普通尾失败而平方尾成功”的 25 条最小偏移射线，精确地说就是

$$
-L\notin\Pi_t(L),\qquad -L\in\Pi_t(L^2).
$$

进一步把平方因子约化为一对普通除子，可得等价的反向除子对判据
[缩放平方尾的反向普通除子对判据](shifted-quadratic-tail-opposite-divisor-pair.md)。

将 $M=sL,e=sf,q=st$ 代入原尾公式即得前述分数恒等式，且

$$
\frac{4e+s}{q}=\frac{4f+1}{t},\qquad
\frac{su^2}{e}=\frac{u^2}{f},\qquad
\frac{Mp}{s}=pL,
$$

故证书公式成立。

这不是全称选择器：仍须对某个外层 $(d,s,t)$ 找到满足式 (2) 的 $f$。但它排除了一个
表面复杂度：偏移 $s$ 不再参与平方尾的内部残数问题。因而下一步应研究 $L^2$ 的因子残数
能否被 $t$ 的结构强制命中，而不是把偏移本身当作尾部因子搜索维度。
