---
kind: claim
claim_id: type-I-h19-reverse-two-tail-linear-e-overflow-boundary-1b
title: H19 低溢出不能线性化反向二尾的边界
statement: 在存储的664个十亿H19源自由残余上，完整枚举m<=127、B<=20的14,453张Type I正规证书及其44,624条严格最大尾反向边。要求E|4K时，累积命中数随B=1,2,3,4,5为599,610,618,621,622，且B=6至20没有新增命中；即使B<=20仍有42点遗漏。因此有限低溢出不能替代E|4K^2所需的平方因子指数。
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

# H19 低溢出不能线性化反向二尾的边界

对 H19 十亿残余完整枚举

$$
3\le m\le127,\qquad m\equiv3\pmod4,\qquad B\le20,
$$

的 Type I 正规形和全部严格最大尾反向边。保持一般选择器的 $E\mid4K^2$，但额外要求
线性化限制 $E\mid4K$，所得累积命中数为

| 溢出上界 | (B\le1) | (B\le2) | (B\le3) | (B\le4) | (B\le5) |
|---|---:|---:|---:|---:|---:|
| 命中 | 599 | 610 | 618 | 621 | 622 |
| 遗漏 | 65 | 54 | 46 | 43 | 42 |

所以允许 $B=2,3,4,5$ 分别只恢复 $11,8,3,1$ 个线性尾状态；从 $B=6$ 到 $B=20$
完全没有新增命中。42个点仍无 $E\mid4K$ 的严格边，其中包括平方预算极端点
$334{,}152{,}361$。这说明低溢出与平方尾存在有限互补，但前者不能替代后者。

该结论仅排除固定盒 $m\le127,B\le20$ 中的线性化策略。它不排除随 $p$ 增长的 $B$ 或缺口，
也不排除替换其它目标坐标的递降。

事实上，去除 $B$ 上界后这42点仍均未释放，故当前 $m\le127$ 盒内任意溢出都不足以线性化；
见[无B上界的线性尾边界](type-I-h19-reverse-two-tail-linear-e-full-b-boundary-1b.md)。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_reverse_two_tail_linear_e_overflow_profile.py \
  --h19 reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --gap-cap 127 --b-cap 20 \
  --output reproductions/type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json
python3 -m unittest tests/test_type_i_h19_reverse_two_tail_linear_e_overflow_profile.py -q
~~~
