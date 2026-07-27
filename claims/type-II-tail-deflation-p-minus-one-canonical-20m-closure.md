---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-canonical-20m-closure
title: 双尾抽缩、p-1 递降或低位移 Type II 短证书的两千万闭合
statement: 在 p<=2*10^7 的158595个核心素数中，Type II 双尾抽缩严格递降覆盖158449个，p-1 的 b=1,2,4 严格缩放递降再覆盖135个；余下11个均由规范位移1或2的直接 Type II 证书覆盖。因此有有限短证书或递降闭合158595=158449+135+11。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- short-certificate
- tail-deflation
- scaled-source
- canonical-ray
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 双尾抽缩、\(p-1\) 递降或低位移 Type II 短证书的两千万闭合

对 \(p\le2\cdot10^7\) 的全部 158,595 个核心素数，以一千万版本相同的顺序做独立全量
审计：

\[
158\,595
=158\,449_{\mathrm{Type\,II\ strict\ descent}}
+135_{p-1\ \mathrm{strict\ descent}}
+11_{\mathrm{canonical\ Type\,II\ certificate}}.
\]

第一层的 \(p-1\) 因子标记双尾抽缩留下 146 个点；在这些点上完整枚举源 \(n=p-1\) 的
\(b=1,2,4\) 缩放候选，严格提升 135 个。剩余 11 个均在规范位移 \(s\le2\) 被直接
Type II 证书捕获，没有未闭合点。

与一千万范围相比，新增的四个短证书点为

\[
10\,170\,169,\quad13\,782\,409,\quad16\,152\,889,\quad16\,267\,729;
\]

它们首次位移依次为 \(2,1,1,1\)。因此低位移补偿并非一千万样本中七点的偶然现象，
但该有限扩展仍不能证明三分支对任意核心素数覆盖，尤其不能把最后一项改写为递降。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_full_audit.py --limit 20000000 \
  --output reproductions/type-ii-tail-deflation-20m-full-results.json
python3 reproductions/type_ii_tail_deflation_p_minus_one_10m_boundary.py \
  --input reproductions/type-ii-tail-deflation-20m-full-results.json \
  --output reproductions/type-ii-tail-deflation-p-minus-one-20m-results.json
python3 reproductions/type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py \
  --input reproductions/type-ii-tail-deflation-p-minus-one-20m-results.json \
  --output reproductions/type-ii-tail-deflation-p-minus-one-canonical-20m-results.json
~~~
