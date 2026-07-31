---
kind: claim
claim_id: type-I-tail-reverse-single-surplus-boundary-500m
title: 五亿普通尾遗漏的反向证书平方剩余量边界
statement: 对p<=500000000的1,717个普通Type II尾遗漏，在m<=127的完整Type I正规形盒中，1,683个有严格反向边使S=E/gcd(E,4K)为1或单个素数幂q^a；其余34个中，穷尽所有严格边后的最小S有28个含两个不同素因子、6个含三个。故“线性或单素幂平方剩余量”在该盒中覆盖98.02%，但并非全覆盖选择规则。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- finite-audit
- selector-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿普通尾遗漏的反向证书平方剩余量边界

令 Type I 正规形的最大尾反向选择器中

$$
S=\frac{E}{\gcd(E,4K)}.
$$

其中 $S=1$ 等价于线性条件 $E\mid4K$，而 $S=q^a$ 表示在线性因子之外只需增加一个
不同素因子。对普通 Type II $p-1$ 尾抽缩的 $1{,}717$ 个五亿遗漏，完整枚举

$$
3\le m\le127,\qquad m\equiv3\pmod4
$$

内的所有 Type I 正规形与所有严格最大尾反向边，得到：

| 最小允许支撑 | 点数 |
|---|---:|
| $S=1$（线性） | 243 |
| $S=q^a$（一个不同素因子） | 1,440 |
| 至少两个不同素因子 | 34 |

因此“线性或单素幂”选择族覆盖

$$
1{,}683/1{,}717=98.02\%.
$$

它是强而明确的有限规律，但不是全称引理：剩余 $34$ 点在同一完整盒内没有这样的边。

## 真正边界

对这 $34$ 点再穷尽全部严格边，并按

$$
(\#\operatorname{supp}S,\ \Omega(S),\ S,\ B,\ m,\ \text{source})
$$

取字典序最小证书，有 $28$ 个最小 $S$ 的素因子支撑为 $2$，其余 $6$ 个为 $3$；没有更高
支撑。相应的 $Omega(S)$ 分布为 $2:25$、$3:7$、$4:1$、$5:1$。

六个三素因子边界点为

$$
22{,}605{,}361,\ 49{,}996{,}489,\ 52{,}387{,}729,
81{,}209{,}209,\ 161{,}964{,}889,\ 357{,}834{,}409.
$$

这排除了“每个普通尾遗漏都可由单个额外素数幂处理”的最自然强版本。下一步理论工作应当
解释为什么支撑至多三在这里足够，或将上述 $34$ 点与另一类源侧可维护的递降规则拼接。

另外，$34$ 条字典序最小边的源分母均有一个 $q\not\equiv1\pmod{24}$ 的素因子，且所选
$q\le107$；故这些有限边仍能按比例缩放至既知终止素数类。这一终止性质不应与尚未获得的
全局源侧选择器混为一谈。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_single_surplus_profile.py
python3 reproductions/type_i_tail_reverse_single_surplus_boundary.py
python3 -m unittest tests/test_type_i_tail_reverse_single_surplus_profile.py -q
~~~
