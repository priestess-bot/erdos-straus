---
kind: claim
claim_id: type-II-h19-tail-deflation-short-closure
title: H19 十亿残余的双尾递降加两点 AC 闭合
statement: 对存储的 p<=10^9 的664个 H19 残余，完整枚举 p-1 的4倍数因子缺口并作 Type II 双尾缩减，662个有严格递降；仅225289和2707609失败，但分别有半径4和5的直接 AC Type II 证书。双尾递降的最小缺口最大为263。因此该固定剖面由662条严格递降和两张直接证书闭合，不推出全称选择器。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- ac-rays
- short-certificate
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 2 and 3
  role: Type-II-certificate-and-lift-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
visibility: public
last_checked: '2026-07-27'
---

# H19 十亿残余的双尾递降加两点 AC 闭合

对前19条规范 Type II 射线未命中的全部 664 个存储残余，完整枚举

\[
m+1\mid p-1,\qquad 4\mid m+1,
\]

并对每个候选缺口 \(m\) 检查 Type II 证书。若

\[
\frac4p=\frac1x+\frac1{pY}+\frac1{pZ},
\]

则将两条尾同时除以 \(p\)，得到严格较小的已解实例

\[
\frac4{(p+m)/(m+1)}=\frac1x+\frac1Y+\frac1Z. \tag{1}
\]

结果为：

| 路径 | 状态数 |
| --- | ---: |
| Type II 双尾严格递降 | 662 |
| 直接 AC 备用证书 | 2 |
| 未闭合 | 0 |

双尾分支中最小缺口的最大值为 \(263\)。仅有的两条双尾遗漏为

| \(p\) | 直接 AC \((A,C,K,h)\) | 半径 |
| ---: | --- | ---: |
| \(225{,}289\) | \((4,2,81,2591)\) | 4 |
| \(2{,}707{,}609\) | \((4,5,2,159)\) | 5 |

所以这份 H19 十亿剖面可表达为

\[
664=662_{\text{双尾严格递降}}+2_{\text{直接 AC}}. \tag{2}
\]

这比只对半径六失败点补双尾递降更强：双尾选择器本身几乎闭合全部 H19 残余。另一方面，
它在这两个具体点完全失败，故不能被误写为全称递降定理；这两个点是下一步应分析的最小
尾缩减残余。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_tail_deflation_short_closure.py \
  --input reproductions/type-ii-h19-residual-ac-profile-1b-results.json \
  --output reproductions/type-ii-h19-tail-deflation-short-closure-1b-results.json
python3 -m unittest tests/test_type_ii_h19_tail_deflation_short_closure.py -q
~~~
