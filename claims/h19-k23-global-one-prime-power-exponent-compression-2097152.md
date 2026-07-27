---
kind: claim
claim_id: h19-k23-global-one-prime-power-exponent-compression-2097152
title: H19-k23 全局尾的一素因子幂指数压缩
statement: 对任意合法 Type II 一非基底素因子幂证书 d=b*ell^e，令 m 为其缺口。由于 gcd(x,m)=1，ell 是模 m 的单位；把 e 替换为与 e 模 ord_m(ell) 同余的最小正整数 e'，仍得到同一尾的 Type II 证书及严格双尾递降，且 1<=e'<=lambda(m)。因此 H19-k23 的72个固定全局尾中，一素因子幂选择器只需检查 e<=82798；二百万层实际最终一支持剖面所用尾更只需 e<=78。
claim_status: established
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- factor-support
- prime-powers
- group-theory
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾的一素因子幂指数压缩

设 \(p\) 为素数，\(m\equiv3\pmod4\) 是合法 Type II 缺口，且

\[
x=\frac{p+m}{4},\qquad
d=b\ell^e\mid x^2,\qquad
d\le x,\qquad d\equiv-x\pmod m, \tag{1}
\]

其中 \(\ell\) 是唯一的非基底素数，\(e\ge1\)，并且 \(b\) 不含 \(\ell\)。

## 指数压缩引理

因 \(m<p\)、\(p\) 为素数，\(\gcd(p,m)=1\)。又 \(m\) 为奇数且
\(4x=p+m\)，所以

\[
\gcd(x,m)=1. \tag{2}
\]

由 \(d\equiv-x\pmod m\) 可知 \(\gcd(d,m)=1\)，特别地
\(\gcd(\ell,m)=1\)。令

\[
o=\operatorname{ord}_m(\ell),\qquad
e'=1+((e-1)\bmod o). \tag{3}
\]

则 \(1\le e'\le o\le\lambda(m)\)，且 \(e'\le e\)。因此

\[
d'=b\ell^{e'}\mid d\mid x^2,\qquad d'\le d\le x,
\]

并且 \(\ell^{e'}\equiv\ell^e\pmod m\)，故

\[
d'\equiv d\equiv-x\pmod m. \tag{4}
\]

所以 \(d'\) 仍是同一尾的 Type II 证书。若还满足 \(m+1\mid p-1\)，它给出的双尾
去 \(p\) 严格递降也原样保留。

这个引理不要求知道 \(\ell\) 是什么，只把一素因子幂选择的指数坐标变为有限坐标。

## H19-k23 的显式边界

对全局因子 \(165600\) 给出的 72 个尾，逐尾计算 Carmichael 函数 \(\lambda(m)\)，得到

\[
\max_m\lambda(m)=82\,798,
\]

最大值在 \(m=82\,799\) 达到。因此全局一素因子幂搜索无损地只须检查

\[
1\le e\le82\,798. \tag{5}
\]

对 [二百万层最终一支持递降剖面](h19-k23-global-one-prime-power-descent-profile-2097152.md)
实际使用的尾集合，最大值更小：

\[
\max\lambda(m)=78\qquad(m=79). \tag{6}
\]

脚本逐个压缩全部 5,128 条已存证书并以精确有理数重建严格源；该有限样本中原选指数
\(1,2,3,4\) 都恰已是各自的最小正阶同余代表。式 (5) 不是对所有核心素数的覆盖定理，
也没有强迫任何 \(\ell\) 出现；真正未解的部分仍是从实际 \(u=(p+m)/(m+1)\) 因子化中
自适应地选择 \(\ell\) 及尾 \(m\)。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_one_prime_power_exponent_compression.py \
  --profile-input reproductions/h19-k23-global-one-prime-power-descent-profile-2097152.json \
  --output reproductions/h19-k23-global-one-prime-power-exponent-compression-2097152.json
python3 -m unittest tests/test_h19_k23_global_one_prime_power_exponent_compression.py -q
~~~
