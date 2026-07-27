---
kind: claim
claim_id: type-II-tail-shifted-quadratic-layered-structural-boundary-300m
title: 三亿平移平方尾压力集的三层结构边界
statement: 对三亿范围89条零偏移遗漏，79条在最小偏移由对称盒饱和或逆配对奇偶性命中；其余10条中8条在后续s<=202521偏移由同两层命中，源因子完成规则命中26034649但不命中新增212973049。因此三层机制覆盖88条，唯一未由这些机制解释的压力点为212973049，其最小证书需要5个有符号素因子坐标。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- divisor-residues
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 三亿平移平方尾压力集的三层结构边界

把两亿的三层机制外推到 $p\le300{,}000{,}000$ 的89条零偏移外源遗漏：

1. 最小偏移的对称盒饱和或逆配对奇偶性直接命中79条；
2. 余下10条中，8条在后续 $s\le202{,}521$ 偏移上再由这两层命中，其中6条为饱和、2条为奇偶性；
3. 源因子完成规则仍命中 $p=26{,}034{,}649$，但不命中唯一新增外层残余
   $p=212{,}973{,}049$。

因此三层并集覆盖

$$
89-1=88 	ag{1}
$$

条压力射线。这里的遗漏并不表示没有递降：完整平方尾审计已给出该点严格递降。它只表明
目前三类**可推广的结构选择器**尚未从其因子数据强制该证书。

该唯一边界点的最小偏移状态为

$$
p=212{,}973{,}049,quad s=73,quad k=103{,}788,quad t=5{,}687,quad d=513.
$$

其最短反向对可取

$$
a=1{,}062=2\cdot3^2\cdot59,\qquad
b=27{,}373=31\cdot883,\qquad a+b=5t. \tag{2}
$$

归一化源和保留因子分别分解为

$$
N=2{,}917{,}432=2^3\cdot7\cdot59\cdot883,
$$

$$
k=2^2\cdot3^3\cdot31^2.
$$

故该证书同时混合 $k$ 与 $N$ 的因子，最小有符号支持度为5、指数位移总量为6；它既非
单侧源因子完成，也不由饱和或补集奇偶性强制。这给出下一步清晰的理论测试例：需证明一种
真正受限的双侧因子完成规则，能处理 (2) 而不退化为对全部除子对的重枚举。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_square_necessity.py \
  --input reproductions/type-ii-tail-shifted-quadratic-offset-profile-300m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-square-necessity-300m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_opposite_pair_profile.py \
  --input reproductions/type-ii-tail-shifted-quadratic-square-necessity-300m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_outer_structural_profile.py \
  --input reproductions/type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-outer-structural-profile-300m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_source_factor_completion.py \
  --input reproductions/type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-source-factor-completion-300m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_layered_structural_boundary_300m.py -q
~~~
