---
kind: claim
claim_id: type-I-high-support-c2-ratio-two-natural-lift-no-go
title: 最小 C=2 图表的比二奇偶前驱自然标记空纤维
statement: >-
  对每个核心素数 p=1 (mod 24)，令最小 C=2 图表为
  R=2p-3、K=(p-1)(2p-1)/4、L=2K。任取互素 a,b|L，满足
  a=2b (mod R)、a<2b，并令 E=La/b、n=(2L-E)/R。则 E|nK，且
  alpha=nK/E 为整数；包含 alpha 的 n-方程标记纤维非空，当且仅当
  R/K 可分成两个正单位分数。反足 Vieta 定理排除后一个条件，故该纤维对所有
  此类比二前驱均为空。结论不要求 E 或 n 为偶数：任何奇数比二前驱也不能仅凭
  自然标记构成 E4 可提升递降。p=12409 给出 E=12854171、n=11891 的严格奇数
  控制。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-c2-centered-vieta-antipodal-no-go
  - type-I-normal-ratio-two-nondegenerate-terminal-or-descent
  - type-I-generalized-dyadic-natural-lift-equivalence
  - denominator-escape-state-contract
topics:
  - type-I
  - high-support
  - c2-boundary
  - ratio-two
  - odd-predecessor
  - marked-solution
  - solution-lift
  - strict-no-go
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_support_c2_ratio_two_natural_lift_no_go.py
    role: parity-free-algebra-and-odd-control-verifier
visibility: public
last_checked: '2026-08-12'
---

# 最小 \(C=2\) 图表的比二奇偶前驱自然标记空纤维

## 1. 问题

对核心素数 \(p\equiv1\pmod {24}\)，最小高支撑 \(C=2\) 图表为

\[
U=\frac{p-1}{4},\qquad
R=8U-1=2p-3,
\]

\[
K=U(8U+1)=\frac{(p-1)(2p-1)}4,qquad L=2K.
\tag{1}
\]

已有反足 Vieta 定理证明

\[
\frac RK\ne\frac1u+\frac1v
\qquad(u,v\in\mathbb N).
\tag{2}
\]

另一方面，比二普通除子对可以产生严格较小的算术前驱。若

\[
a,b\mid L,qquad(a,b)=1,qquad a\equiv2b\pmod R,qquad a<2b,
\tag{3}
\]

则

\[
E=L\frac ab,qquad n=\frac{2L-E}{R}
\tag{4}

\]

满足 \(0<E<2L=4K\)、\(E\mid4K^2\)、\(E\equiv1\pmod R\) 和
\(0<n<p\)。旧的广义二进表述只覆盖 \(E\) 偶数的子类；但 (3) 也可以产生
奇数 \(E\)、奇数 \(n\)。本卡确定这种奇数算术前驱不能绕过当前 \(C=2\) 边界的
标记提升障碍。

## 2. 无奇偶假设的自然标记门

先取任意满足

\[
4K=pR+1,qquad R>1,qquad
E\mid4K^2,qquad E\equiv1\pmod R,qquad0<E<4K,
\tag{5}
\]

的数据，并令

\[
n=\frac{4K-E}{R}.
\tag{6}

\]

这里不假设 \(E\) 或 \(n\) 为偶数。由 \(E\equiv1\pmod R\) 有
\((E,R)=1\)。再由 \(nR=4K-E\) 得

\[
nRK=4K^2-EK\equiv0pmod E.
\tag{7}
\]

故

\[
E\mid nK,qquad \alpha:=\frac{nK}{E}\in\mathbb N.
\tag{8}

\]

直接计算给出

\[
\frac4n-\frac1\alpha
=\frac{4K-E}{nK}
=\frac RK
=\frac4p-\frac1{pK}.
\tag{9}
\]

因此定义自然标记纤维

\[
\mathcal W_{E}:=
\left\{(\alpha,u,v):
\frac4n=\frac1\alpha+\frac1u+\frac1v\right\}.
\tag{10}
\]

有严格等价

\[
\boxed{
\mathcal W_E\ne\varnothing
\iff
\frac RK=\frac1u+\frac1v\text{ 对某些 }u,v\in\mathbb N.
}
\tag{11}
\]

在非空时，(9) 还把 \((\alpha,u,v)\) 精确提升为 \((pK,u,v)\)；在空时，
这个自然坐标没有 E4 的源对象。证明没有使用偶性，因而不能用“奇源”绕过 (11)。

## 3. C=2 比二前驱的全称空纤维

回到 (1)--(4)。由 \(a,b\mid L\) 与 \((a,b)=1\)，有

\[
E\mid L^2=4K^2.
\tag{12}

\]

又由 (3) 及 \(2L=4K\equiv1\pmod R\)，

\[
E=L\frac ab\equiv2L\equiv1pmod R.
\tag{13}

\]

而 \(a<2b\) 恰给出 \(0<E<2L=4K\)。所以 (5)--(11) 全部适用。
但对 (1) 的 \(R,K\)，反足 Vieta 定理已经全称证明 (2)。故得到：

\[
\boxed{
\mathcal W_E=\varnothing
\quad\text{对最小 }C=2\text{ 图表的每个比二算术前驱。}
}
\tag{14}

\]

这包含通常的偶前驱 \(E=2(p-1),n=p-1\)，也包含所有可能的奇数前驱。它没有说
较小的 \(4/n\) 无解；只说它不可能含自然分母 \(\alpha\)，所以不能以 (9) 作为
当前图表的可提升递降。它同样不排除原 \(p\) 有独立的 Type I/II 终端，或存在改变
标记、保留尾或正规形的其它出口。

## 4. 严格奇数控制

取

\[
p=12409,quad U=3102,quad R=24815,quad K=76982334,quad L=153964668.
\tag{15}

\]

有一组非退化比二因子

\[
a=1081=23\cdot47,qquad
b=12948=2^2\cdot3\cdot13\cdot83,
\tag{16}

\]

满足 \(a=2b-R\)、\((a,b)=1\) 及 \(a,b\mid L\)。式 (4) 给出

\[
\boxed{
E=12854171=11\cdot23^2\cdot47^2,quad
n=11891=11\cdot23\cdot47,quad
\alpha=71214.
}
\tag{17}

\]

所以这确实是一个严格奇数前驱，而非广义二进偶终端。仍有

\[
\frac4{11891}-\frac1{71214}
=\frac{24815}{76982334}
=\frac4{12409}-\frac1{12409\cdot76982334}.
\tag{18}

\]

式 (14) 说明不存在以 \(71214\) 为标记分母的左端三项解。该控制特别排除了把
“奇数 \(n<p\)”本身误记为全域可提升递降的推理。素数 \(12409\) 本身另有已有
terminal-first 的 \(R=11\) 终端；这不影响 (14) 的图表级结论。

## 5. 聚焦复核

```bash
python3 reproductions/type_i_high_support_c2_ratio_two_natural_lift_no_go.py --verify
```

复现器核对无奇偶假设的整除和标记恒等式、反足 Vieta 的小控制，以及 (15)--(18) 的
严格奇数实例；不作范围扫描。
