---
kind: claim
claim_id: type-I-linear-half-block-two-residue-escape
title: 线性半块的二残数注入与子群障碍逃逸
statement: 对核心素数p的线性状态p=a+s+asR，若任一端点t属于{a,s}满足t=3 mod 4，则另一端点为奇数，K=(pR+1)/4可分解为两个半块，且G=(tR+1)/2整除K并满足G=2^{-1} mod R。因此2与2^{-1}都属于K的中心化平方除子谱和生成子群。任何湮灭该生成子群的角色都在2上取1；若-1属于<2 mod R>则该状态不可能是子群角色障碍。特别地，R为3 mod 8的素数时不可能出现这种障碍。七个完整压力谱逐项复核了半块证书。该结论不保证有限指数障碍命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- centered-spectrum
- subgroup-character
- quadratic-character
- residue-class
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性半块的二残数注入与子群障碍逃逸

## 定理

设核心素数 \(p\equiv1\pmod4\) 有线性源状态

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4,
\qquad K=\frac{pR+1}{4}. \tag{1}
\]

若一个端点 \(t\in\{a,s\}\) 满足 \(t\equiv3\pmod4\)，令另一个端点为 \(u\)。则
\(u\) 为奇数，且

\[
G=\frac{tR+1}{2},
\qquad H=\frac{uR+1}{2},
\qquad K=GH. \tag{2}
\]

特别地 \(G\mid K\) 且

\[
G\equiv2^{-1}\pmod R. \tag{3}
\]

定义中心化平方除子谱与其生成子群为

\[
\mathcal C_R(K)=\{dK^{-1}\bmod R:d\mid K^2\},
\qquad
\mathcal H_R(K)=\langle q\bmod R:q\mid K\rangle. \tag{4}
\]

则

\[
\boxed{2,2^{-1}\in\mathcal C_R(K)\subseteq\mathcal H_R(K).} \tag{5}
\]

因此，若 \(\chi\) 是 \((\mathbb Z/R\mathbb Z)^\times\) 上在
\(\mathcal H_R(K)\) 上平凡的任意角色，则 \(\chi(2)=1\)。若
\(-1\in\langle2\bmod R\rangle\)，则

\[
-1\in\mathcal H_R(K), \tag{6}
\]

该状态不可能是子群角色障碍。特别地，当 \(R\) 是 \(3\pmod8\) 的素数时，Euler 判据给出
\(2^{(R-1)/2}\equiv-1\pmod R\)，故 (6) 自动成立。

## 证明

若 \(t=s\)，则 \(s\) 原本为奇数；代入 (1) 的模 \(4\) 版本得到 \(a\) 亦为奇数。若
\(t=a\)，则 \(s\) 原本为奇数。故两端的 \(tR+1,uR+1\) 都是偶数。由

\[
4K=(tR+1)(uR+1)
\]

得到 (2)，而 \(tR+1\equiv1\pmod R\) 给出 (3)。

因 \(G\mid K\)，两个数

\[
d_-=KG,
\qquad d_+=K/G
\]

都整除 \(K^2\)。将它们代入 (4)，分别得到

\[
d_-K^{-1}\equiv G\equiv2^{-1}\pmod R,
\qquad
d_+K^{-1}\equiv G^{-1}\equiv2\pmod R.
\]

这证明 (5)。角色结论立刻成立；若 \(-1\) 是 \(2\) 的幂，则由 (5) 它也在
\(\mathcal H_R(K)\) 中。素数 \(R\equiv3\pmod8\) 的结论是 Euler 判据的直接应用。

对于由奇平方自由 \(m\mid R\) 给出的二次分离角色 \(\chi_m=(\cdot/m)\)，若它还满足
\(\chi_m(-1)=-1\)，则 \(m\equiv3\pmod4\)。本定理迫使 \(\chi_m(2)=1\)，从而
\(m\equiv7\pmod8\)。这只是二次 G 型障碍的必要条件，不会排除高阶角色或有限指数障碍。

## 有限审计与范围

程序在七个完整压力谱的全部 490 个有向线性源中，逐项枚举满足 \(t\equiv3\pmod4\) 的端点，
并直接检验 \(d_-,d_+\mid K^2\) 及其中心化残数。对其中 \(R\) 为 \(3\pmod8\) 素数的记录，
再直接核验 \(-1\) 是半块 \(G\) 的幂。JSON 保存每个半块和两个除子见证。

该引理只把某些状态从“可能的 G 型”推进到 \(-1\in\mathcal H_R(K)\)。在
\(-1\in\mathcal H_R(K)\setminus\mathcal C_R(K)\) 时仍会留下有限指数障碍，因此它不是一般
\(B\) 命中或终端选择器的证明。

## 复现

~~~bash
python3 reproductions/type_i_linear_two_residue_escape_profile_600m.py
python3 -m unittest tests.test_type_i_linear_two_residue_escape_profile_600m -v
~~~
