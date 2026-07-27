---
kind: claim
claim_id: type-I-h19-reverse-two-tail-square-necessity-1b
title: H19 零溢出反向二尾中的平方因子必要性
statement: 在存储的664个十亿H19源自由残余上，完整枚举m<=127、B=1的7,175张Type I正规证书及其37,075条严格最大尾反向边。599点至少有一条边满足E|4K；其余65点没有任何此类边，尽管每点仍有一般E|4K^2的严格边。因此该有限盒中的65点真正需要K^2提供的额外素因子指数。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- reverse-lift
- factorization
- bounded-parameter
- h19
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# H19 零溢出反向二尾中的平方因子必要性

在[零溢出反向二尾终止闭合](type-I-h19-reverse-two-tail-terminal-1b.md)的同一 H19 输入上，
不止选择首个证书，而是完整枚举所有

$$
3\le m\le127,\qquad m\equiv3\pmod4,\qquad B=1
$$

的 Type I 正规形及其每一条严格最大尾反向边。令

$$
E=4K-nR,\qquad E\mid4K^2.
$$

检验更强的线性限制 $E\mid4K$，得到

$$
664=599_{E\mid4K}+65_{E\nmid4K}.
$$

审计共检查 $7{,}175$ 张正规证书和 $37{,}075$ 条严格边。65 个遗漏点在该完整盒中仍都有
一般选择器的严格边，却没有**任何**一条满足 $E\mid4K$。因此它们不能由“只取 $K$ 的普通
除子，外加固定二幂”的线性版本处理；必有素因子的指数来自 $K^2$ 而超过 $4K$ 所允许的量。

这种平方预算并不总是单一素因子的偶然重复。对每个65点取所有严格边中最小的

$$
S=\frac{E}{\gcd(E,4K)}>1
$$

并按 $S$ 的素因子指数总数分类，得到 $1:54,2:9,3:1,5:1$；按不同素因子支持数分类为
$1:55,2:9,4:1$。特别地

$$
p=334{,}152{,}361
$$

在此盒内仅有一条严格边，其最小剩余为

$$
S=1{,}654{,}220=2^2\cdot5\cdot107\cdot773,
$$

需要五个额外指数单位和四种素因子。因此“每次至多把一个素因子多取一次”的平方尾规则也
不足以覆盖这个有限残余。

这是一条有限范围的必要性边界。它不排除更大缺口、$B>1$、替换不同坐标或其它递降机制，
也不说明65点的最小额外指数相同。它的作用是排除一个自然但过弱的源侧简化：不能把完整
$E\mid4K^2$ 选择器普遍降为 $E\mid4K$。

允许任意溢出也不能消除这一障碍：在同一 $m\le127$ 缺口盒中，线性版本仍精确遗漏42点，见
[无B上界的线性尾边界](type-I-h19-reverse-two-tail-linear-e-full-b-boundary-1b.md)。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_reverse_two_tail_square_necessity.py \
  --h19 reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --gap-cap 127 \
  --output reproductions/type-i-h19-reverse-two-tail-square-necessity-1b-results.json
python3 -m unittest tests/test_type_i_h19_reverse_two_tail_square_necessity.py -q
~~~
