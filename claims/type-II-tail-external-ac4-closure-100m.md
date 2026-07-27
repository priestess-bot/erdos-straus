---
kind: claim
claim_id: type-II-tail-external-ac4-closure-100m
title: 亿级核心素数的双尾、平方因子外源递降或半径四 AC 闭合
statement: 对所有 p<=10^8、p=1 mod24 的719781个核心素数，719281个有普通 Type II 双尾严格递降；其500个遗漏中459个有完整平方因子外源严格递降；余下41个全有 max(A,C)<=4 的直接 AC Type II 证书，最小半径分布为1:16、2:21、3:2、4:2。因此该固定范围有719781=719281+459+41的严格递降或半径四短证书闭合。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- ac-rays
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

# 亿级核心素数的双尾、平方因子外源递降或半径四 AC 闭合

在 \(\ p\le10^8,\ p\equiv1\pmod {24}\) 的全部 719,781 个核心素数上，按以下顺序做完整
精确审计：

1. 枚举 \(p-1\) 因子缺口的普通 Type II 双尾严格递降；
2. 对其500个遗漏完整枚举平方因子外源 \(e\mid(kn)^2\)；
3. 对仍遗漏的点枚举 \(\max(A,C)\le4\) 的直接 AC Type II 射线。

所得不交分流为

\[
719{,}781
=719{,}281_{\text{双尾严格递降}}
+459_{\text{平方因子外源严格递降}}
+41_{\mathrm{AC}_4}. \tag{1}
\]

41 个直接 AC 补点的最小半径分布为

| 半径 | 状态数 |
| ---: | ---: |
| 1 | 16 |
| 2 | 21 |
| 3 | 2 |
| 4 | 2 |

半径四的两个边界点为

\[
56{,}040{,}889,\qquad63{,}641{,}209. \tag{2}
\]

这将千万级的半径二补充扩展到独立的一亿级范围，但不能外推为固定半径四的全称命题。
它表明下一条理论选择器应把普通双尾失败、平方因子外源残数与小 AC 射线关联起来，而不是
只试图从尾失败推出外源递降。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_deflation_external_boundary.py \
  --input reproductions/type-ii-tail-deflation-100m-full-results.json \
  --output reproductions/type-ii-tail-deflation-external-boundary-100m-results.json
python3 reproductions/type_ii_tail_external_ac2_closure.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-100m-results.json \
  --ac-bound 4 \
  --output reproductions/type-ii-tail-external-ac4-closure-100m-results.json
python3 -m unittest tests/test_type_ii_tail_external_ac4_closure_100m.py -q
~~~
