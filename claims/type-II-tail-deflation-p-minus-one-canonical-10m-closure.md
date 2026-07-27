---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-canonical-10m-closure
title: 双尾抽缩、p-1 递降或低位移 Type II 短证书的一千万闭合
statement: 在 p<=10^7 的82887个核心素数中，Type II 双尾抽缩严格递降覆盖82803个，p-1 的 b=1,2,4 严格缩放递降再覆盖77个；余下7个均由规范位移1或2的直接 Type II 证书覆盖。因此有有限短证书或递降闭合82887=82803+77+7。
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

# 双尾抽缩、\(p-1\) 递降或低位移 Type II 短证书的一千万闭合

对 \(p\le10^7\) 的全部 \(82\,887\) 个 \(p\equiv1\pmod{24}\) 素数，先运行
完整的 \(p-1\) 因子标记 Type II 双尾抽缩；其 84 个遗漏再完整枚举源 \(n=p-1\) 的
\(b=1,2,4\) 缩放严格递降。后者留下的七点逐项检查规范 Type II 射线
\(s=a^2c\le2\)，均有直接证书：

\[
82\,887=82\,803_{\mathrm{Type\,II\ strict\ descent}}
+77_{p-1\ \mathrm{strict\ descent}}
+7_{\mathrm{canonical\ Type\,II\ certificate}}.
\]

七张补充证书首次出现的规范位移依次为

\[
(2,1,1,1,2,1,2),
\]

对应素数

\[
(214729,297049,878089,1511449,3942409,5478169,6294649).
\]

其中位移 \(1\) 的四张分别由 \(p+4\) 的 \(3\bmod4\) 因子触发，位移 \(2\) 的三张
由 \(p+8\) 的 \(7\bmod8\) 因子触发；后二者可分别取
\(h=31,71,1671\)。所以这七点不是不可解释的例外，而是两个显式低位移因子扇的交界。

这正是“短证书或递降”的有限闭合，而不是纯递降：最后七项只验证了目标
\(4/p\) 的 Type II 分解，未声称从任意较小源实例可归纳提升。它也不证明这三分支对
任意核心素数覆盖。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_p_minus_one_10m_boundary.py
python3 reproductions/type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py
python3 -m unittest tests/test_type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py -q
~~~
