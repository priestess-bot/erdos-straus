---
kind: claim
claim_id: type-II-tail-shifted-quadratic-closure-100m
title: 亿级核心素数的全严格递降闭合（含有界平移平方外源）
statement: 对所有 p<=10^8、p=1 mod24 的719781个核心素数，719281个有普通 Type II 双尾严格递降；其500个遗漏中459个有完整零平移平方因子外源严格递降；余下41个均在 k<=340574 的兼容平移平方外源盒中有严格递降。因此该固定范围有719781=719281+459+41的全严格递降闭合。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
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

# 亿级核心素数的全严格递降闭合（含有界平移平方外源）

此前一亿审计中，普通双尾与完整零平移平方因子外源递降之后仍有 41 个点，需以半径四
AC 证书备用。对这 41 点进一步枚举

\[
q=4k-1,\qquad s=p\bmod 4k,\qquad s\mid q,
\qquad 1\le k\le340{,}574,
\]

并在每条兼容射线上完整枚举平方尾因子，得到每一点的显式平移平方外源严格提升。故按顺序
分流为

\[
719{,}781
=719{,}281_{\text{普通 Type II 双尾严格递降}}
+459_{\text{零平移平方因子外源严格递降}}
+41_{\text{有界平移平方外源严格递降}}. \tag{1}
\]

每条最后分支见证都满足源分母严格小于目标素数，且源、目标三分数恒等式都以有理数精确
核验。因此在这个固定有限范围内，先前的 41 个 AC 备用点不再是递降图的终点。

该盒的最大首次命中是

\[
p=5{,}478{,}169,\quad k=340{,}574,\quad s=28{,}985,
\quad n=5{,}478{,}165,
\]

其余原先在 \(k\le10^4\) 未命中的两点分别在

\[
(p,k,s)=(878{,}089,54{,}649,3{,}705),\qquad
(6{,}294{,}649,65{,}569,25)
\]

首次命中。这是有限计算闭合，不能推出固定 \(k\) 盒对任意核心素数都闭合，也没有给出
全称递降引理；但它排除了“一亿内零平移外源遗漏必需 AC 备用”的解释。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_closure.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-100m-results.json \
  --k-bound 340574 \
  --output reproductions/type-ii-tail-shifted-quadratic-closure-100m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_closure_100m.py -q
~~~
