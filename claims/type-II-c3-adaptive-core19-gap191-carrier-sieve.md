---
kind: claim
claim_id: type-II-c3-adaptive-core19-gap191-carrier-sieve
title: c=3 adaptive core-19 ray 的 gap-191 无穷 carrier sieve 与严格下降
statement: 在 c=3 adaptive core-19 ambient-19 ray 的 v=8w 子射线上，p=192N-191、x=(p+191)/4=48N，其中 N=946563871+8505305445w。令 S=R_191(48) 为 21 个精确 signed-ratio residue，T=-S^{-1}。若素数 ell mod191 属于 T 且 ell|N，则一个完整 gap-191 Type II factor pair 存在，并通过 n=N<p 给出严格 two-tail descent。特别地 ell=61、v=224+488z 给出 d=128M 的 square-only moving-divisor family 和无穷 prime parameter。利用 PNT in arithmetic progressions，这个无限 carrier sieve 在 v=8w 的 prime parameter 中具有相对密度 1；任何固定有限、仅由上述 carrier 素数条件组成的菜单仍可由 CRT 加 Dirichlet 避开。v=32 是精确边界：p=6713814844801 与 N=34967785651 都是素数，但完整 gap-191 factor-pair condition 不成立。该结果不覆盖其它 gaps，也不证明逐点 terminal cover 或 Erdos--Straus 猜想。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
  - type-II-factor-pair-carrier-strict-descent
  - type-II-coprime-factor-normal-form
  - type-II-affine-uniform-divisor-rigidity
topics:
  - type-II
  - c3
  - core19
  - terminal-first
  - gap-191
  - factor-pair
  - square-divisor
  - strict-descent
  - affine-ray
  - prime-sieve
  - density-one
  - finite-menu-no-go
  - proof-boundary
sources:
  - claim: type-II-factor-pair-carrier-strict-descent
    role: complete factor-pair normal form and two-tail lift
  - claim: type-II-affine-uniform-divisor-rigidity
    role: moving square-divisor normal form
  - concept: prime-number-theorem-in-arithmetic-progressions
    role: relative-density calculation for finite carrier sets
  - reproduction: reproductions/type_ii_c3_adaptive_core19_gap191_carrier_sieve.py
    role: exact carrier box, l=61 descent, and v=32 miss
visibility: public
last_checked: '2026-08-07'
---

# Adaptive core-19 的 gap-191 carrier sieve

## 1. 规范化

在已有 adaptive ray 上限制

\[
v=8w.
\tag{1}
\]

令

\[
N(w)=946563871+8505305445w.
\tag{2}
\]

直接代入原 ray 得

\[
p=192N-191,
\qquad
x=\frac{p+191}{4}=48N,
\qquad
N=\frac{p+191}{192}<p.
\tag{3}
\]

所以任何完整 gap \(191\) 因子对证书都会自动有严格 two-tail source \(N\)。以下所有
factor pair 都调用既有完整正规形，而不是只检验一个偶然的 divisor：

\[
x=ABC,
\qquad (A,B)=1,
\qquad A+B=191\kappa.
\tag{4}
\]

由 \(192\mid p-1\)，(4) 给出的 Type II certificate 同时给出

\[
\frac4N=\frac1{ABC}+\frac1{AC\kappa}+\frac1{BC\kappa},
\qquad
\frac4p=\frac1{ABC}+\frac1{pAC\kappa}+\frac1{pBC\kappa}.
\tag{5}
\]

## 2. 有限 carrier 与一般选择律

48 的完整 signed-ratio box 是

\[
\begin{aligned}
S=\mathcal R_{191}(48)
=\{&1,2,3,4,6,8,12,16,24,32,36,48,64,65,69,72,\\
&96,97,128,130,144\}.
\end{aligned}
\tag{6}
\]

它可直接由 \(48=2^4\cdot3\) 写成

\[
S=\{2^i3^j:-4\le i\le4,\ -1\le j\le1\}\pmod {191}.
\tag{7}
\]

令

\[
\begin{aligned}
T=-S^{-1}=\{&47,61,63,94,95,119,122,126,127,143,155,159,167,175,\\
&179,183,185,187,188,189,190\}.
\end{aligned}
\tag{8}
\]

**定理（gap-191 carrier 选择律）。** 令 \(\ell\nmid192\cdot8505305445\) 是素数，
满足 \(\ell\bmod191\in T\)，且 \(\ell\mid N(w)\)。则存在互素正整数

\[
a,b\mid48,
\qquad \frac ab\ell\equiv-1\pmod {191}.
\tag{9}
\]

写 \(N=\ell M\)，并令

\[
(A,B,C)=(a\ell,b,48M/(ab)),
\tag{10}
\]

必要时交换 \((A,B)\)。则 (4) 成立，故 (5) 是一张直接 Type II terminal 与严格下降。

**证明。** 由 \(\ell\in-S^{-1}\)，可按 (6) 取互素 \(a,b\mid48\) 满足 (9)。因为
\(\ell\nmid48\)，有 \((a\ell,b)=1\)，且 \(ab\mid48\)，所以 (10) 是合法正整数分解，
并满足

\[
ABC=48\ell M=48N=x.
\tag{11}
\]

(9) 等价于 \(191\mid a\ell+b\)，即 (4)。式 (5) 的完整因子对 two-tail lift
给出结论。证毕。

这是一条因子选择律：它只要求 (N) 有一个落在 (T) 中的素因子，不把 `191|R` 或
ambient character 本身错误地当成 terminal。

## 3. 一条 square-only 无穷严格下降子射线

取 \(\ell=61\)，可选择 \(a=3,b=8\)，因为

\[
3\cdot61+8=191.
\tag{12}
\]

又

\[
N(w)\equiv31+49w\pmod {61},
\tag{13}
\]

故取 \(w=28+61z\)，等价于

\[
v=224+488z,
\qquad
M=3919592071+8505305445z.
\tag{14}
\]

于是 \(N=61M\)，并且

\[
p=11712M-191,
\qquad x=2928M.
\tag{15}
\]

将 (10) 重排为

\[
(A,B,C,\kappa)=(8,183,2M,1),
\qquad d=A^2C=128M.
\tag{16}
\]

因此对每个素数 \(p\) 参数点，

\[
\boxed{
\frac4p=
\frac1{2928M}+
\frac1{16Mp}+
\frac1{366Mp}}
\tag{17}
\]

并严格下降到

\[
\boxed{
\frac4{61M}=
\frac1{2928M}+
\frac1{16M}+
\frac1{366M}.}
\tag{18}
\]

这是固定 \((m,d)\) 整条筛看不到的 moving-divisor 机制。对参数 \(z\)，

\[
E=\gcd(2928\cdot8505305445,2928\cdot3919592071)=2928,
\tag{19}
\]

而

\[
128\mid E^2,
\qquad128\nmid E,
\qquad191\mid E+128.
\tag{20}
\]

所以 \(d=128x/E\) 是 square-only affine divisor，不能被“固定 \(d\)”的零筛排除。
该子射线的 \(p\) progression 是 primitive；因此 Dirichlet 定理给出无穷 prime parameter。
其 \(z=0\) 点 \(p=45906262335361\) 已由复现器精确验证为素数。

## 4. 密度一，但不是点态覆盖

令 \(\mathcal L\) 为满足 (8) 且不整除 \(192\cdot8505305445\) 的全部素数，并写

\[
P_0=181740263041,
\qquad
P_{\mathrm{step}}=1633018645440=192\cdot8505305445.
\tag{21}
\]

有 \(\gcd(P_0,P_{\mathrm{step}})=1\)。对固定 \(\ell\in\mathcal L\)，因
\(\ell\nmid192\cdot8505305445\)，\(N(w)\equiv0\) 与
\(p(w)\equiv0\pmod\ell\) 各有唯一的 \(w\) residue class；它们彼此不同。事实上，
若两式同时成立，则 \(p=192N-191\) 迫使 \(\ell\mid191\)，但
\(\ell\bmod191\in T\subset(\mathbb Z/191\mathbb Z)^\times\) 排除了这一点。

避开 \(p\)-root 的每一个参数类上，\(p(r+\ell z)\) 都是 primitive arithmetic
progression；\(p(w)=\ell\) 至多给出一个零密度例外。因此，算术进程素数定理在
\(p(w)\) 为素数的参数中给出避开该 carrier 的相对比例

\[
\frac{\ell-2}{\ell-1}.
\tag{22}
\]

令

\[
\mathscr P=\{w\ge0:p(w)\text{ 是素数}\},
\qquad
A_F=\{w\in\mathscr P:\ell\nmid N(w)\text{ 对每个 }\ell\in F\}.
\tag{23}
\]

对任何有限 \(F\subset\mathcal L\)，CRT 和同一素数定理给出相对密度

\[
\boxed{
d_{\mathscr P}(A_F)
=\prod_{\ell\in F}\frac{\ell-2}{\ell-1}}
\tag{24}
\]

\(T\) 包含 \(21\) 个模 \(191\) 的约化 residue class。PNT in arithmetic progressions
给出这些类中的素数倒数和发散，故当有限 \(F\) 递增到 \(\mathcal L\) 时，(24) 趋于零。
令

\[
A_\infty=\bigcap_{\substack{F\subset\mathcal L\\F\text{ 有限}}}A_F.
\tag{25}
\]

则对每个有限 \(F\)，相对上密度满足

\[
\overline d_{\mathscr P}(A_\infty)
\le d_{\mathscr P}(A_F)
=\prod_{\ell\in F}\frac{\ell-2}{\ell-1}.
\tag{26}
\]

先固定 \(F\) 使用 PNT in arithmetic progressions，再令 \(F\) 递增；不需要对增长模数
使用一致的素数定理。由 (26)，\(A_\infty\) 的相对上密度为零。因此，至少有一个
\(\mathcal L\)-carrier 素因子整除 \(N(w)\) 的 prime parameter 集合具有相对密度 \(1\)。

这不等于逐点覆盖。对任何有限 \(F\)，每个 \(\ell\in F\) 都有 \(\ell-2\) 个
residue class 可同时避开 \(N(w)\equiv0\) 和 \(p(w)\equiv0\pmod\ell\)。CRT 给出
\(r\pmod {Q_F}\)，其中 \(Q_F=\prod_{\ell\in F}\ell\)，且
\(\gcd(p(r),P_{\mathrm{step}}Q_F)=1\)；所以 \(p(r+Q_Fz)\) 是 primitive
progression，Dirichlet 再次给出无穷 prime parameter。故任何固定有限的
\(\mathcal L\)-carrier-prime menu 都不能代替这个无限 sieve；此结论不涉及其它 gap、
复合因子规则或不同的证书机制。

## 5. 一个完整 gap-191 miss

取 \(v=32\)，即 \(w=4\)。此时

\[
p=6713814844801,
\qquad N=34967785651,
\tag{27}
\]

二者均为素数，且 \(N\equiv150\pmod {191}\)。因为

\[
\mathcal R_{191}(48N)=S\{N^{-1},1,N\},
\tag{28}
\]

完整 gap-191 factor-pair condition \(-1\in\mathcal R_{191}(48N)\) 等价于

\[
\{41,190,14\}\cap S\ne\varnothing.
\tag{29}
\]

由 (6) 右端为空，故该点没有任何 gap-191 Type II factor pair。它没有反驳密度一结论，
也不排除其它 gap、Type I 或其它 terminal。

复现：

```bash
python3 reproductions/type_ii_c3_adaptive_core19_gap191_carrier_sieve.py --verify
```
