---
kind: claim
claim_id: type-I-h19-reverse-two-tail-linear-e-full-b-boundary-1b
title: H19 固定缺口盒内任意溢出仍不能线性化反向二尾
statement: 对存储的664个十亿H19源自由残余，在m<=127的完整Type I正规形盒中，不限制B并要求反向因子E|4K，恰有622点命中、42点遗漏。先由B<=20闭合622点；对余42点完整枚举1,708张无B上界的正规证书及507条严格最大尾反向边，仍无E|4K边。因此固定缺口盒内增大B不能替代E|4K^2的平方因子机制。
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

# H19 固定缺口盒内任意溢出仍不能线性化反向二尾

[低溢出线性化边界](type-I-h19-reverse-two-tail-linear-e-overflow-boundary-1b.md) 已在
$B\le20$ 命中664个 H19 残余中的622个，留下精确的42点集合。对这42点去除 $B$ 上界，
枚举全部

$$
3\le m\le127,\qquad m\equiv3\pmod4
$$

的 Type I 正规形及其严格最大尾反向边，再要求

$$
E\mid4K.
$$

结果是42点均未释放。审计了 $1{,}708$ 张正规证书和 $507$ 条严格边，却没有一条线性尾边。
与前一阶段组成精确的固定缺口盒结论

$$
664=622_{E\mid4K}+42_{E\nmid4K,\ \text{all }B}.
$$

因此，在这个 H19 有限压力集上，增大正规形溢出 $B$ 不会把平方尾机制替换为普通线性尾。
若要进一步线性化，必须增大缺口、替换其它坐标或改变递降机制；若要保持当前缺口范围，
则必须控制真正的 $E\mid4K^2$ 多素因子指数积集。

不过无界 $B$ 确实压缩了平方层的复杂度。对每个42点取所有严格边中最小的

$$
S=\frac{E}{\gcd(E,4K)}>1,
$$

其额外指数总数分布为 $1:39,2:2,5:1$，不同素因子支持数分布为 $1:39,2:2,4:1$。
所以仅有三点仍需多素因子支持：

$$
243{,}145{,}681,\qquad334{,}152{,}361,\qquad707{,}590{,}321.
$$

前、后两点的最小支持各为两个素因子；中间点的唯一严格边仍有
$S=2^2\cdot5\cdot107\cdot773$。这把当前固定盒内“真正多支持”的研究压力精确压缩到
三条状态，而不说明单支持的39点已有统一构造。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_reverse_two_tail_linear_e_full_b_boundary.py \
  --profile reproductions/type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json \
  --gap-cap 127 \
  --output reproductions/type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json
python3 -m unittest tests/test_type_i_h19_reverse_two_tail_linear_e_full_b_boundary.py -q
~~~
