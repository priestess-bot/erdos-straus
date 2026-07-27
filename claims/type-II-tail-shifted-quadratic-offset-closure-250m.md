---
kind: claim
claim_id: type-II-tail-shifted-quadratic-offset-closure-250m
title: 两亿五千万核心素数的平移平方外源全严格递降闭合
statement: 对所有 p<=250000000、p=1 mod24 的1708964个核心素数，1707968个有普通 Type II 双尾严格递降；其996个遗漏中918个有零偏移完整平方因子外源递降；余下78个均在残差偏移 s<=202521 的完整固定偏移族中有严格递降。该范围没有超过两亿记录的最小偏移。
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

# 两亿五千万核心素数的平移平方外源全严格递降闭合

对所有 $p\le250{,}000{,}000$、$p\equiv1\pmod {24}$ 的核心素数，依次执行普通 Type II
双尾递降、完整零偏移平方因子外源递降和完整固定偏移射线，得到

$$
1{,}708{,}964
=1{,}707{,}968_{\text{双尾严格递降}}
+918_{\text{零偏移平方因子外源}}
+78_{\text{平移平方外源}}. \tag{1}
$$

第三分支在固定 $s$ 时完整枚举 $k\mid(p-s)/4$，以及每个缩放尾的全部平方因子。取
$s\le202521$ 即闭合所有 78 个零偏移遗漏；没有新的最小偏移超过两亿范围的记录

$$
p=152{,}498{,}329,\qquad s=202{,}521. \tag{2}
$$

这把同一严格递降分流从两亿独立延展到两亿五千万，但不能证明该偏移界对所有核心素数
有效。它提供的是下一条记录出现前的可复现稳定区间。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_deflation_full_audit.py \
  --limit 250000000 \
  --output reproductions/type-ii-tail-deflation-250m-full-results.json
python3 reproductions/type_ii_tail_deflation_external_boundary.py \
  --input reproductions/type-ii-tail-deflation-250m-full-results.json \
  --output reproductions/type-ii-tail-deflation-external-boundary-250m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_offset_profile.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-250m-results.json \
  --offset-bound 202521 \
  --output reproductions/type-ii-tail-shifted-quadratic-offset-profile-250m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_offset_profile_250m.py -q
~~~
