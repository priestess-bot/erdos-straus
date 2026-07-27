---
kind: claim
claim_id: type-II-tail-shifted-quadratic-offset-boundary-200m
title: 两亿核心素数的平移平方外源严格递降闭合与偏移记录
statement: 对所有 p<=2*10^8、p=1 mod24 的1383890个核心素数，1383059个有普通 Type II 双尾严格递降；其831个遗漏中766个有零偏移完整平方因子外源递降；余下65个均在残差偏移 s<=202521 的完整固定偏移族中有严格递降。s<=7161 在此范围恰遗漏152498329与171292489，后者最小偏移48265，前者最小偏移202521。
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

# 两亿核心素数的平移平方外源严格递降闭合与偏移记录

对全部 $p\le2\cdot10^8$、$p\equiv1\pmod {24}$ 的核心素数，顺序执行：普通 Type II
双尾递降、完整零偏移平方因子外源递降、以及固定残差偏移的完整因子射线。得到

$$
1{,}383{,}890
=1{,}383{,}059_{\text{双尾严格递降}}
+766_{\text{零偏移平方因子外源}}
+65_{\text{平移平方外源}}. \tag{1}
$$

其中固定偏移 $s$ 时，不截断 $k$，而是完整枚举 $k\mid(p-s)/4$，再枚举每个源的平方
尾因子。这个坐标的严格代数依据见
[平移平方外源射线的源距离因子参数化](shifted-quadratic-source-distance-parametrization.md)。
更进一步，所有命中的平方尾都严格正规化为 $t/L$ 的因子问题，偏移 $s$ 不参与内部尾残数，
见[平移平方外源的缩放平方尾正规形](shifted-quadratic-tail-normalization.md)。

一亿范围的 $s\le7161$ 盒在两亿范围恰新增两个遗漏：

$$
152{,}498{,}329,\qquad171{,}292{,}489. \tag{2}
$$

它们的较小偏移均已被完整排除，首次见证为

| $p$ | 最小 $s$ | $k$ | 源距离 $p-n$ |
| ---: | ---: | ---: | ---: |
| 171,292,489 | 48,265 | 10,702,764 | 4 |
| 152,498,329 | 202,521 | 2,379,622 | 16 |

因此 $s\le202521$ 重新闭合全部 65 个压力点。该结果提供了两条精确的反例边界：固定
偏移 7,161 不能从一亿样本直接外推；更重要地，记录偏移的增长不局限于源距离 4。
这仍然只是有限严格递降审计，不是对所有核心素数的统一选择器定理。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_deflation_full_audit.py \
  --limit 200000000 \
  --output reproductions/type-ii-tail-deflation-200m-full-results.json
python3 reproductions/type_ii_tail_deflation_external_boundary.py \
  --input reproductions/type-ii-tail-deflation-200m-full-results.json \
  --output reproductions/type-ii-tail-deflation-external-boundary-200m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_offset_profile.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-200m-results.json \
  --offset-bound 202521 \
  --output reproductions/type-ii-tail-shifted-quadratic-offset-profile-200m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_offset_profile_200m.py -q
~~~
