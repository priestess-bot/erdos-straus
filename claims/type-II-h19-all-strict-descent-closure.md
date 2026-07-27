---
kind: claim
claim_id: type-II-h19-all-strict-descent-closure
title: H19 十亿残余的全严格递降闭合
statement: 对存储的 p<=10^9 的664个 H19 残余，662个有 Type II 双尾严格递降；普通双尾遗漏225289与2707609分别有自适应外部源严格递降，参数为(k,q,g)=(2,7,41)和(6,23,344)。因此该固定剖面的664个状态全都有显式、严格小于p的已验证源解及其提升，而不需直接证书备用。这不是一般递降选择器定理。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- tail-deflation
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: certificate-and-strict-lift-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# H19 十亿残余的全严格递降闭合

[双尾递降加两点 AC 闭合](type-II-h19-tail-deflation-short-closure.md) 已将普通 Type II
双尾缩减的遗漏精确压缩为

\[
225{,}289,\qquad 2{,}707{,}609. \tag{1}
\]

这两点并非严格递降的终点。直接验证自适应外部源分支给出：

| \(p\) | \(k\) | \(q=4k-1\) | \(g\) | 源 \(n<p\) | Type I 缺口 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(225{,}289\) | 2 | 7 | 41 | 197,128 | 47 |
| \(2{,}707{,}609\) | 6 | 23 | 344 | 2,594,792 | 359 |

每一行均验证

\[
\frac4n=\frac1{kn}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{knp}+\frac1u+\frac1v, \tag{2}
\]

其中 \(2\le n<p\)，并且源、目标的三项单位分数恒等式都逐项以精确有理数检验。

故全体存储 H19 残余有精确分流

\[
664=662_{\text{Type II 双尾严格递降}}
+2_{\text{自适应外部源严格递降}}. \tag{3}
\]

这比“短证书或递降”更强：在这个固定十亿剖面中，每个 H19 残余都已有显式严格递降，
不需要把任何状态作为直接证书终点。其理论缺口也因此更集中：必须解释为何普通双尾递降
的失败会强制某种外源递降，或证明另一个覆盖性机制。

这仍然只是有限审计。它没有给出对任意核心素数的尾缺口选择，也没有证明两个分支在范围外
仍互补。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_all_strict_descent_closure.py \
  --tail-profile reproductions/type-ii-h19-tail-deflation-short-closure-1b-results.json \
  --external-profile reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json \
  --output reproductions/type-ii-h19-all-strict-descent-closure-1b-results.json
python3 -m unittest tests/test_type_ii_h19_all_strict_descent_closure.py -q
~~~
