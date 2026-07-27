---
kind: claim
claim_id: type-II-tail-shifted-quadratic-four-layer-structural-closure-400m
title: 四亿核心素数的四层平移平方尾结构闭合
statement: 对p<=400000000的2665703个核心素数，2664243个有普通Type II双尾严格递降，1352个有零偏移完整平方外源递降，余108个均在s<=202521平移族中有严格递降；其中95个由最小偏移饱和或逆配对奇偶性、11个由后续偏移同两层、2个由双侧有界接口完成结构性闭合。故四层结构机制完全解释108条压力射线。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- external-source
- divisor-residues
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: certificate-and-lift-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
visibility: public
last_checked: '2026-07-27'
---

# 四亿核心素数的四层平移平方尾结构闭合

对全部 $p\le400{,}000{,}000$、$p\equiv1\pmod{24}$ 的核心素数，完整尾部和外源审计给出

$$
2{,}665{,}703
=2{,}664{,}243_{\rm 双尾严格递降}
+1{,}352_{\rm 零偏移平方外源}
+108_{\rm 平移平方外源}. \tag{1}
$$

108条零偏移遗漏全部在固定偏移 $s\le202{,}521$ 中闭合；最大最小偏移仍由

$$
p=152{,}498{,}329,\qquad s=202{,}521,\qquad d=16
$$

保持，四亿范围没有新的偏移记录。

将四层结构选择器施加于这108条压力射线，得到优先级分解

$$
108=95_{\rm 最小偏移饱和/奇偶性}
+11_{\rm 后续\,s\le202{,}521\,结构}
+2_{\rm 双侧接口完成}. \tag{2}
$$

后续偏移层中8条由子群饱和、3条由逆配对奇偶性释放；最后双侧接口完成的两条仍为

$$
26{,}034{,}649,\qquad212{,}973{,}049.
$$

因此，三亿得到的四层机制在新增19条四亿压力射线上无需引入第五类规则，仍完整给出严格
递降证书。这个结果是独立有限审计，而不是对 $202{,}521$ 为全称偏移界或对 Erdős--Straus
猜想的证明。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_deflation_full_audit.py \
  --limit 400000000 \
  --output reproductions/type-ii-tail-deflation-400m-full-results.json
python3 reproductions/type_ii_tail_deflation_external_boundary.py \
  --input reproductions/type-ii-tail-deflation-400m-full-results.json \
  --output reproductions/type-ii-tail-deflation-external-boundary-400m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_offset_profile.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-400m-results.json \
  --offset-bound 202521 \
  --output reproductions/type-ii-tail-shifted-quadratic-offset-profile-400m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_square_necessity.py \
  --input reproductions/type-ii-tail-shifted-quadratic-offset-profile-400m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-square-necessity-400m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_opposite_pair_profile.py \
  --input reproductions/type-ii-tail-shifted-quadratic-square-necessity-400m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-opposite-pair-profile-400m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_outer_structural_profile.py \
  --input reproductions/type-ii-tail-shifted-quadratic-opposite-pair-profile-400m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-outer-structural-profile-400m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_two_sided_completion.py \
  --input reproductions/type-ii-tail-shifted-quadratic-opposite-pair-profile-400m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-two-sided-completion-400m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_four_layer_structural_closure_400m.py -q
~~~
