---
kind: claim
claim_id: type-II-h19-pure-new-scaled-tail-mark-boundary-1b
title: 纯新规范证书的缩放首项标记尾在十亿 H19 状态中的边界
statement: 对十亿范围541个 H19 新因子状态，完整枚举20<=s<=1008的纯新单素因子规范 Type II 证书以及每张证书缺口 m 的全部 D|p+m、D=1 mod m 后，330个状态有缩放首项标记严格源。其中282个已有 k=1 的普通同证书双尾递降，另48个仅能以 k>1 命中；余211个在该窗口没有此类标记桥。这是有限短证书/标记提升边界，不是无标记递降或原猜想的反例。
claim_status: computationally_reproduced
topics:
- type-II
- pure-new-factor
- marked-solution
- scaled-first
- strict-descent
- H19
- finite-audit
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 纯新规范证书的缩放首项标记尾在十亿 H19 状态中的边界

## 命题

取 [H19 源自由状态剖面](type-II-source-free-transition-profile.md) 中
\(p\le10^9\) 的 541 个新因子状态。对每个 \(20\le s\le1008\)，唯一写成

\[
s=a^2c,\qquad c\text{ 平方自由},\qquad M=4ac,
\]

并只允许 H19 新素数 \(q\) 满足

\[
q\mid p+4s,\qquad q\equiv-1\pmod M. \tag{1}
\]

令 \(m=(p+4s)/q\)。对每张由 (1) 重建的原始 Type II 证书，完整枚举

\[
D\mid p+m,\qquad D>1,\qquad D\equiv1\pmod m. \tag{2}
\]

每个 (2) 给出

\[
k=\frac{D-1}{m},\qquad n=k\frac{p+m}{D}<p, \tag{3}
\]

以及首分母为 \(kx\) 的标记源解。精确审计得到

\[
541=282_{k=1}+48_{\text{only }k>1}+211_{\text{no marked bridge}}. \tag{4}
\]

也就是说，330 个状态在窗口中至少有一张纯新规范证书带有缩放首项标记尾；其中
282 个已经有普通 \(k=1\) 双尾去 \(p\)，48 个则在整个审计窗口中只能由 \(k>1\)
的此类见证命中。其余 211 个状态没有满足 (1)--(2) 的证书。最晚首次命中仍在
\(s=1000\)。

## 一个新增的缩放例

\[
p=176089,\quad s=238,\quad (a,c)=(1,238),\quad q=5711,
\]

给出缺口 \(m=31\)。这里

\[
D=280\mid p+m=176120,\qquad 280\equiv1\pmod {31},
\]

故 \(k=9\)，并有严格较小的标记源

\[
n=9\frac{176120}{280}=5661.
\]

此点在整个窗口没有 \(k=1\) 的同纯新证书尾，因而属于式 (4) 的 48 个新增状态。
复现逐项以有理数验证

\[
\frac4{5661}=\frac1{9x}+\frac1{y/p}+\frac1{z/p},
\qquad
\frac4{176089}=\frac1x+\frac1y+\frac1z. \tag{5}
\]

## 含义与限制

这将 [纯新规范证书与普通同证书双尾递降的边界](type-II-h19-pure-new-tail-mark-boundary-1b.md)
从 282 个普通尾扩展为 330 个**带标记**尾。因而“纯新单素因子与共享
\(1\bmod m\) 除子”是一个确实出现、但并不自动闭合的交集；后续可把 211 个遗漏状态
作为研究多来源递降或不同证书的更小压力集。

它们不是整个 H19 剖面的未闭合点。与
[H19 十亿残余的全严格递降闭合](type-II-h19-all-strict-descent-closure.md) 的已验证尾表
逐项相交，211 个纯新标记遗漏精确分为

\[
211=210_{\text{另一路普通 Type II 双尾}}+1_{\text{自适应外源}}. \tag{6}
\]

前 210 点都有一张不属于这里纯新规范标记窗口的普通 Type II 双尾证书；唯一的余点
\(p=225289\) 则由外源 \((k,q,g)=(2,7,41)\) 严格递降至 \(197128\)。所以该有限
样本已经显示“换证书或换源”能够完全闭合，但尚未给出从纯新扇的失败到这种替代支路的
统一选择定理。

不过，(3) 的源端要求首分母恰为 \(kx\)。根据
[缩放首分母双尾提升与固定 Type II 证书等价](type-II-scaled-tail-marked-lift-equivalence.md)，
这与目标的固定 Type II 证书是双射关系，不能由“\(n<p\) 有某个三项解”的普通归纳
假设推出。因此式 (4) 不是新的无标记递降定理，也不增加 Erdős--Straus 猜想的已证明
范围；它只给出短证书/带标记提升接口的精确有限剖面。

## 复现

~~~bash
python3 reproductions/type_ii_h19_pure_new_scaled_tail_profile.py \
  --shift-cap 1008 \
  --output reproductions/type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json
python3 -m unittest tests/test_type_ii_h19_pure_new_scaled_tail_profile.py -q
~~~
