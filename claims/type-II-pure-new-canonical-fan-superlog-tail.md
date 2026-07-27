---
kind: claim
claim_id: type-II-pure-new-canonical-fan-superlog-tail
title: 增长规范移位扇上的纯新单素因子证书具有超对数稀薄尾部
statement: 存在绝对常数 delta,c>0。令 L=log log X、H=floor(delta L)。对每个 H19<s<=H 写 s=a_s^2 c_s，其中 c_s 平方自由。满足 p<=X、p=1 mod24 且对所有这些 s 都不存在 H19 新素数 q 使 q|p+4s、q=-1 mod4a_sc_s 的素数数目为 O(X exp[-c L log L])。故相对密度一的核心素数有一张纯新单素因子 Type II 证书，且其规范移位 s=O(log log X)。这不排除无限例外。
claim_status: established
topics:
- type-II
- canonicalization
- sieve
- density
- pure-new-factor
- growing-family
- short-certificate
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Appendix A, shifted-prime sieve methodology
  role: upper-bound-sieve-methodology
- paper: shute2022
  locator: Section 5.5, Lemma 5.5.1
  role: uniform-fundamental-lemma
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 增长规范移位扇上的纯新单素因子证书具有超对数稀薄尾部

## 定理

令 \(L=\log\log X\)，并取

\[
H=\lfloor\delta L\rfloor, \tag{1}
\]

其中 \(\delta>0\) 是充分小的绝对常数。对每个 \(19<s\le H\)，唯一写成

\[
s=a_s^2c_s,\qquad c_s\text{ 平方自由},\qquad M_s=4a_sc_s. \tag{2}
\]

令 \(\mathcal O_p=\bigcup_{1\le t\le19}\operatorname{Supp}(p+4t)\)。记
\(E_{\mathrm{can,new}}(X)\) 为满足 \(p\le X\)、\(p\equiv1\pmod{24}\) 且对所有
\(19<s\le H\) 都不存在素数 \(q\) 使

\[
q\mid p+4s,\qquad q\equiv-1\pmod{M_s},\qquad q\notin\mathcal O_p. \tag{3}
\]

则存在绝对常数 \(c>0\)，使

\[
E_{\mathrm{can,new}}(X)\ll X\exp\bigl(-cL\log L\bigr). \tag{4}
\]

对 \(p>4H\) 的非例外点，令 \(K=(q+1)/M_s\)、\(h=q\)。则

\[
h=4a_sc_sK-1,\qquad h\mid Kp+a_s, \tag{5}
\]

且 \(p\ge4a_s^2c_s\) 使 Type II 序条件自动成立。因此相对密度一的核心素数具有
一张 H19 纯新、单素因子、规范移位

\[
s\le H=O(\log\log X) \tag{6}
\]

的 Type II 证书。

## 新性与无碰撞根

只在筛中使用 \(\ell>4H\) 的素数。若这样的 \(\ell\) 同时整除 \(p+4s\) 与
\(p+4t\)（\(1\le t\le19\)），则

\[
\ell\mid4(s-t),\qquad0<|4(s-t)|<4H<\ell,
\]

矛盾。故大筛素数自动不属于 \(\mathcal O_p\)。

写 \(p=24u+1\)。对每个 \(\ell>4H\)，定义

\[
\nu_H(\ell)=1+\#\{19<s\le H:\ell\equiv-1\pmod{M_s}\}. \tag{7}
\]

第一项为 \(p\equiv0\pmod\ell\) 的素性根。若 (3) 失败，则每个可用 \(s\) 还须避开

\[
p\equiv-4s\pmod\ell. \tag{8}
\]

这些根精确地不同：若两个移位根重合，则
\(\ell\mid4(s-t)\)，而 \(0<4|s-t|<4H<\ell\)；它们也不与零根重合。
所以 (7) 恰是禁根数。

## 有效筛维

令

\[
A_H=\sum_{s=20}^{H}\frac1{\varphi(M_s)}. \tag{9}
\]

由 \(M_s=4s/a_s\le4s\)，有完全初等的下界

\[
A_H\ge\frac14\sum_{s=20}^{H}\frac1s
\ge\frac14\log H-O(1). \tag{10}
\]

为记录筛维增长，标准的 \(1/\varphi\) 上界以及按 \(s=a^2c\) 分组还给出

\[
A_H\ll(\log H)^2\log\log(3H). \tag{11}
\]

对每个模数 \(M_s\le4H\) 一致应用算术级数 Mertens 估计，得到

\[
\sum_{4H<\ell\le z}\frac{\nu_H(\ell)}{\ell}
=(1+A_H)\log\log z+O(H\log H). \tag{12}
\]

又 \(\nu_H(\ell)\le H+1<\ell\)，且
\(\sum_{\ell>4H}\nu_H(\ell)^2/\ell^2=O(H/\log(3H))\)。故筛积为

\[
V_H(z)\ll\exp(CH\log H)(\log z)^{-1-A_H}. \tag{13}
\]

这里没有一般因子扇的横截面枚举成本：每个移位只要求一个明确的素数残数
\(-1\pmod{M_s}\)，而非允许任意因子积命中目标残数。

## 有参数上界筛

对仅含 \(4H\) 以上素因子的平方自由 \(d\)，中国剩余定理给出

\[
\#\{u\le X/24:u\text{ 落在 }d\text{ 的禁根}\}
=\frac X{24}\frac{\nu_H(d)}d+O(\nu_H(d)), \tag{14}
\]

其中 \(\nu_H(d)=\prod_{\ell\mid d}\nu_H(\ell)\)。取

\[
D=X^{1/3},\qquad w\asymp H\log H,\qquad z=D^{1/w}. \tag{15}
\]

式 (11)--(13) 满足基本上界筛的随维正则性条件；并且
\(\sum_{d\le D}\nu_H(d)\le D(1+\log D)^H\)。于是

\[
E_{\mathrm{can,new}}(X)\ll
X\exp(CH\log H)
\left(\frac{H\log H}{\log X}\right)^{1+A_H}
\;+\;X^{1/3}\exp\bigl(H\log\log X+O(H\log H)\bigr)
\;+\;O(z+H). \tag{16}
\]

其中 \(O(z)\) 单独计入被零根筛掉的 \(p\le z\)，而 \(O(H)\) 吸收
\(p\le4H\) 的序条件小点。代入 \(H=\lfloor\delta L\rfloor\)，用 (10)，并将
\(\delta\) 取足够小，第一项的指数为 \(-\Omega(L\log L)\)；其余项更小，得到 (4)。

## 与有限状态和平方子族的关系

[H19 十亿新因子状态在移位一千零八内纯新闭合](type-II-h19-pure-new-1008-1b.md)
已在 \(H=1008\) 对存储的 541 个 H19 新因子状态逐点给出 (3) 形见证。
相比之下，限制 \(C=1\) 的平方子族在同一状态集中有 11 个完整穷尽遗漏，见
[十亿 H19 新因子状态中刚性平方射线的完整边界](type-II-h19-pure-new-square-ray-boundary-1b.md)。
这解释了为何 (4) 使用完整规范扇，而不能只保留平方移位。

## 边界

这是密度定理，不是逐点选择器或严格递降引理。它允许极稀薄但可能无限的例外集合；
更不提供对单个例外素数选取 \(s\) 的确定性规则。全称证明仍需把这个稀薄失败状态接到
可终止的递降，或证明其来源标签不可能无限持续。

## 复现

~~~bash
python3 reproductions/type_ii_pure_new_canonical_fan_sieve.py \
  --bounds 50 100 1008 \
  --prime-bound 100000 \
  --output reproductions/type-ii-pure-new-canonical-fan-sieve-results.json
python3 -m unittest tests/test_type_ii_pure_new_canonical_fan_sieve.py -q
~~~
