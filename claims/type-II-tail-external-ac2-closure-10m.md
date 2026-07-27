---
kind: claim
claim_id: type-II-tail-external-ac2-closure-10m
title: 千万核心素数的双尾、平方因子外源递降或半径二 AC 闭合
statement: 对所有 p<=10^7、p=1 mod24 的82887个核心素数，82803个有普通 Type II 双尾严格递降；其84个遗漏中77个有完整平方因子外源严格递降；余下214729、297049、878089、1511449、3942409、5478169、6294649全有 max(A,C)<=2 的直接 AC Type II 证书。因此该固定范围有82887=82803+77+7的严格递降或半径二短证书闭合。
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

# 千万核心素数的双尾、平方因子外源递降或半径二 AC 闭合

对所有 \(p\le10^7\)、\(p\equiv1\pmod {24}\) 的 82,887 个核心素数，依次使用三条
独立出口：

1. 普通 Type II 双尾缩减；
2. 对双尾遗漏枚举全部 \(k\mid(p-1)/4\) 的完整平方因子外源严格递降；
3. 对仍遗漏的点枚举 \(\max(A,C)\le2\) 的直接 AC Type II 射线。

三个分支在这个按序分流中给出

\[
82{,}887
=82{,}803_{\text{双尾严格递降}}
+77_{\text{平方因子外源严格递降}}
+7_{\mathrm{AC}_2}. \tag{1}
\]

最后七点为

\[
214{,}729,\ 297{,}049,\ 878{,}089,\ 1{,}511{,}449,\
3{,}942{,}409,\ 5{,}478{,}169,\ 6{,}294{,}649,
\]

其直接 AC 见证只使用

\[
(A,C)\in\{(1,1),(1,2)\}. \tag{2}
\]

故这些点确实否定“尾失败必强制标准外源递降”，但并未构成短证书障碍。它们反而表明：
在这一独立样本中，一个非常小的 AC 补充盒足以封闭三个递降分支的共同遗漏。

该结果是有限范围审计，不证明固定 \((A,C)\) 盒或三分支组合对所有核心素数都成立。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_external_ac2_closure.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-10m-results.json \
  --ac-bound 2 \
  --output reproductions/type-ii-tail-external-ac2-closure-10m-results.json
python3 -m unittest tests/test_type_ii_tail_external_ac2_closure.py -q
~~~
