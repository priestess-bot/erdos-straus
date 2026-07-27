---
kind: claim
claim_id: type-II-h19-cross-half-factor-subgroup-transfer-profile
title: H19 本质跨侧零溢出的单侧支撑搬运剖面
statement: 对十亿 H19 首 r 剖面的184个本质跨侧零溢出状态，分别检查半因子 A、B 的素因子残数生成子群是否含 -1 mod r。112 个为左侧支撑内、右侧支撑外，67 个为左侧支撑外、右侧支撑内，故179个恰有一侧支撑内；仅1个两侧均支撑外，4个两侧均支撑内。因此主导跨侧形状是一个支撑外因子残数将目标搬运给另一侧的有限指数积集，而非两个独立单侧命中。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- divisor-residues
- subgroup
- product-set
- finite-audit
- h19
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: subsequence-product-structure
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19 本质跨侧零溢出的单侧支撑搬运剖面

设一个本质跨侧零溢出状态的半因子对为 \(M=AB\)。它满足

\[
\exists\alpha\mid A,\ \beta\mid B:\quad
\alpha\beta\equiv-1\pmod r,
\]

但 \(A\)、\(B\) 的各自除子均不命中 \(-1\)。令 \(H_A,H_B\) 分别为 \(A,B\)
的素因子残数在 \((\mathbb Z/r\mathbb Z)^\times\) 中生成的子群。逐项记录
\(-1\in H_A\)、\(-1\in H_B\)，得到：

| 单侧子群状态 | 状态数 |
| --- | ---: |
| \(-1\in H_A\), \(-1\notin H_B\) | 112 |
| \(-1\notin H_A\), \(-1\in H_B\) | 67 |
| \(-1\notin H_A\cup H_B\) | 1 |
| \(-1\in H_A\cap H_B\) | 4 |

于是 184 个本质跨侧状态中有 179 个恰有一侧在支撑层面已经可达 \(-1\)，只是其有限
指数除子集尚未实际命中；另一侧的一个实际因子 \(\beta\) 将目标改写为

\[
\alpha\equiv-\beta^{-1}\pmod r,
\]

并使支撑内一侧的有限积集命中。这里“搬运”只是精确描述已有交叉见证，并非已证明的
一般选择规则。

更细的检查排除了把这一步简化为子群饱和：在上述 179 个单侧支撑状态及 4 个双侧支撑
状态中，合计 187 个“支撑内侧”里，没有一个的实际除子残数集等于其生成子群。换言之，
即使 \(-1\) 在该侧的素因子支撑中可达，有限指数仍在每一例中阻止它作为该侧普通除子出现。
所以 Kneser 型子群信息只能定位可达性，不能单独完成跨侧搬运；下一步必须同时控制另一侧
给出的目标余类和支撑内侧的有限指数积集。

这个限制不只是成功样本的现象。对同一十亿首 \(r\) 剖面的 91 个高溢出状态（两侧实际
除子积均未命中 \(-1\)），\(-1\) 仍全部属于联合子群 \(H_AH_B\)。其单侧形状为

| 单侧子群状态 | 状态数 |
| --- | ---: |
| \(-1\in H_A\), \(-1\notin H_B\) | 39 |
| \(-1\notin H_A\), \(-1\in H_B\) | 46 |
| \(-1\notin H_A\cup H_B\) | 1 |
| \(-1\in H_A\cap H_B\) | 5 |

它与上表的 184 个跨侧成功状态有同样的主导形状。因此“联合子群可达”或“哪一侧支撑
\(-1\)”都不能区分命中与失败；剩余的精确难点是两个**有限指数除子积集**是否实际相交于
目标余类，而不是新的角色或生成子群障碍。

搬运侧本身也不能普遍简化为一个素因子。对 179 个恰有一侧支撑内的状态，令

\[
\mu=\min\{\Omega(\beta):\ \beta\mid E,\ -\beta^{-1}\in\operatorname{Div}(S)pmod r\},
\]

其中 \(S\) 是支撑内侧、\(E\) 是支撑外侧。完整外侧除子枚举得到：

| 最小 \(\mu\) | 状态数 |
| ---: | ---: |
| 1 | 76 |
| 2 | 91 |
| 3 | 11 |
| 6 | 1 |

故 103 个状态至少需要复合搬运因子。即使已知哪一侧应搬运目标，也不能将下一引理弱化为
“外侧总有一个合适素因子”；它必须控制外侧的受限除子积集。

该分流排除一个过弱的路线：不能要求两侧各自都产生 \(-1\) 因子。更具体的正向目标是
证明，在共同失败状态中，支撑外一侧必产生一个可控残数，使另一侧的受限除子积集命中该
搬运后的目标；或证明这种搬运失败会强制标准外部源递降。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_cross_half_factor_subgroup_profile.py \
  --input reproductions/type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json \
  --output reproductions/type-ii-h19-cross-half-factor-subgroup-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_cross_half_factor_subgroup_profile.py -q
~~~
