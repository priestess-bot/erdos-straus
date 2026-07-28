---
kind: claim
claim_id: type-I-universal-pminusone-prime-factor-menu-sieve
title: 九条固定 p 减一单素因子桥菜单的 536219/212520 维筛残余
statement: 令 R 属于 {3,7,11,15,23,35,47,71,143}，c_R=-4^{-1} mod R。对核心素数 p，若 K_R=(Rp+1)/4 有素因子 q=c_R mod R，则 p 有源 p-1 的 B=1 上半区偶终端桥。再并入 p+1 的三模四因子桥，九条 R 分支共同未覆盖的核心素数数目为 O(X/(log X)^(536219/212520))。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- p-minus-one
- terminal-bridge
- factorization
- sieve
- density
- fixed-ray
sources:
- paper: shute2022
  locator: Sections 5.2--5.5, especially equations (5.3.5)--(5.3.6) and Lemma 5.5.1
  role: explicit-fixed-dimension-upper-bound-sieve
- paper: montgomery_vaughan2007
  locator: Chapter 11, Corollaries 11.19/11.21
  role: fixed-modulus-PNT-in-arithmetic-progressions
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 九条固定 (p-1) 单素因子桥菜单的 (536219/212520) 维筛残余

令

\[
\mathcal R=\{3,7,11,15,23,35,47,71,143\},
\qquad
c_R\equiv-4^{-1}\pmod R. \tag{1}
\]

下表列出全部目标素数类：

| (R) | (c_R) | \(\varphi(R)\) |
| ---: | ---: | ---: |
| 3 | 2 | 2 |
| 7 | 5 | 6 |
| 11 | 8 | 10 |
| 15 | 11 | 8 |
| 23 | 17 | 22 |
| 35 | 26 | 24 |
| 47 | 35 | 46 |
| 71 | 53 | 70 |
| 143 | 107 | 120 |

对核心素数 (p)，设

\[
K_R=\frac{Rp+1}{4}.
\]

若某个 (R\in\mathcal R) 的 (K_R) 有素因子

\[
q\equiv c_R\pmod R, \tag{2}
\]

则取 (C=q)。由于 (K_R\equiv4^{-1}\pmod R)，有

\[
\frac{K_R}{q}\equiv4^{-1}c_R^{-1}\equiv-1\pmod R.
\]

所以 (C) 满足固定 (p-1) 菜单的除子条件 (4C\equiv-1\pmod R)，并由
[九条固定射线](type-I-fixed-universal-pminusone-b1-rays.md)给出源 (p-1) 的 (B=1)
上半区偶终端桥。这里 (2) 是完整除子条件的一个单素因子充分条件，而非必要条件。

## 联合筛界

再加入 [(p+1) 三模四因子桥](type-I-p-plus-one-b1-upper-bridge.md)。令 (T_{\mathcal R}(X))
计数 (p\le X)、(p\equiv1\pmod {24}) 的素数，要求该 (p) 同时避开 (p+1) 分支和所有
(R\in\mathcal R) 的 (2)。则

\[
T_{\mathcal R}(X)
\ll\frac{X}{(\log X)^\kappa},
\qquad
\kappa
=1+\frac12+\sum_{R\in\mathcal R}\frac1{\varphi(R)}
=\frac{536219}{212520}
\approx2.523146. \tag{3}
\]

证明只需固定维上界筛。写 (p=24t+1)，并以

\[
F_0=24t+1,
\qquad F_+=12t+1,
\qquad F_R=24Rt+R+1 \quad(R\in\mathcal R) \tag{4}
\]

编码素性、(p+1) 分支和九条菜单分支。除有限多个坏素数外，所有根均两两不同：

\[
\det(F_0,F_+)=12,
\quad \det(F_0,F_R)=24,
\quad \det(F_+,F_R)=12(1-R),
\quad \det(F_R,F_S)=24(R-S). \tag{5}
\]

故局部禁根数为

\[
\nu(\ell)=1+\mathbf1_{\ell\equiv3\ (4)}
+\sum_{R\in\mathcal R}\mathbf1_{\ell\equiv c_R\ (R)}. \tag{6}
\]

对固定模数
\(\mathrm{lcm}(4,\prod_{R\in\mathcal R}R)\) 使用 PNT-AP，再分部求和，给出

\[
\sum_{\ell<v}\frac{\nu(\ell)}\ell
=\kappa\log\log v+O(1).
\]

于是筛积 (V(v)\asymp(\log v)^{-\kappa})。其余 CRT 计数和上界基本筛步骤与
[三分支 (13/6) 维筛](type-I-b1-three-factor-sieve-bridge.md)相同；这里
\(\nu(d)\le11^{\omega(d)}\le\tau_{11}(d)\)，故 (D=X^{1/3}) 时余项
\(O(X^{1/3}(\log X)^{10})\) 被 (3) 吸收。

在冻结的 1,964 个六亿普通尾压力点上，按 (p+1,R=3,7,11,15,23,35,47,71,143) 的顺序，
这些**单素因子**分支首次覆盖数为

\[
760,431,158,82,99,17,21,12,4,4,
\]

合计 1,588 点。完整除子菜单的有限覆盖更强，但不具备这里的简单筛描述。

这个结果仍不证明 Erdős--Straus 猜想：有限菜单的共同筛余可能无限。它给出的是一个可构造
(B=1) 子族的更强解析密度界，以及继续研究共同残余时应保留的九条因子方向。

~~~bash
python3 -m unittest tests.test_type_i_universal_pminusone_prime_factor_menu -q
~~~
