---
kind: claim
claim_id: type-II-tail-shifted-quadratic-offset-closure-300m
title: 三亿核心素数的平移平方外源全严格递降闭合
statement: 对所有 p<=300000000、p=1 mod24 的2030611个核心素数，2029455个有普通 Type II 双尾严格递降；其1156个遗漏中1067个有零偏移完整平方因子外源递降；余下89个均在残差偏移 s<=202521 的完整固定偏移族中有严格递降。该范围仍没有超过两亿记录的最小偏移。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- external-source
- tail-deflation
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

# 三亿核心素数的平移平方外源全严格递降闭合

对所有 $p\le300{,}000{,}000$、$p\equiv1\pmod {24}$ 的核心素数，按普通 Type II 双尾、
完整零偏移平方因子外源、完整固定偏移射线的顺序，得到

$$
2{,}030{,}611
=2{,}029{,}455_{\text{双尾严格递降}}
+1{,}067_{\text{零偏移平方因子外源}}
+89_{\text{平移平方外源}}. \tag{1}
$$

固定偏移时完整枚举 $k\mid(p-s)/4$ 与缩放尾平方因子。旧盒 $s\le202521$ 仍闭合全部
89 个零偏移遗漏；最大最小偏移仍为

$$
p=152{,}498{,}329,\qquad s=202{,}521. \tag{2}
$$

因此两亿的偏移记录至少稳定延续至三亿。这是独立的有限严格递降闭合，而不是固定偏移界的
全称证明。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_deflation_full_audit.py \
  --limit 300000000 \
  --output reproductions/type-ii-tail-deflation-300m-full-results.json
python3 reproductions/type_ii_tail_deflation_external_boundary.py \
  --input reproductions/type-ii-tail-deflation-300m-full-results.json \
  --output reproductions/type-ii-tail-deflation-external-boundary-300m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_offset_profile.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-300m-results.json \
  --offset-bound 202521 \
  --output reproductions/type-ii-tail-shifted-quadratic-offset-profile-300m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_offset_profile_300m.py -q
~~~
