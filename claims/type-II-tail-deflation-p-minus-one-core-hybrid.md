---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-core-hybrid
title: Type II 双尾抽缩或 p-1 缩放的核心范围闭合
statement: 在 p<=100000 的1181个核心素数上，完整 Type II 双尾抽缩覆盖1179个，仅67369与85369未命中；二者均有 p-1 的 b=2 缩放严格提升。因此该有限范围有两分支纯递降闭合1181=1179+2。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- tail-deflation
- scaled-source
- p-minus-one
- selector
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# Type II 双尾抽缩或 \(p-1\) 缩放的核心范围闭合

令 Type II 证书缺口为 \(m\)。当 \(m+1\mid p-1\) 时，两个被 \(p\) 整除的尾分母
可同时除以 \(p\)，得到源

\[
n=\frac{p+m}{m+1}<p.
\]

在所有 \(p\le100\,000\)、\(p\equiv1\pmod{24}\) 的 1,181 个素数上，完整枚举
\(p-1\) 的 \(4\) 的倍数因子并在相应缺口验证 Type II 证书。该抽缩覆盖 1,179 个；
最先成功缺口的分布主要集中在 \(3\)（575 点）、\(7\)（475 点）、\(11\)（80 点），
但不能由此外推统一小缺口。

仅有

\[
67\,369,\qquad85\,369
\]

没有可抽缩 Type II 证书。对二者完整枚举 \(p-1\) 的 \(b=2,4\) 缩放候选后均有
严格提升，且实际命中比例为 \(b=2\)。所以该范围有更简单的有限闭合：

\[
1181=1179+2.
\]

这是当前最紧的小范围实验接口：要推广为定理，需要证明每个核心素数有可抽缩 Type II
证书，或落入这个 \(p-1\) 证书子类。有限分布不是这种选择定理的证明。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_p_minus_one_core_hybrid.py
python3 -m unittest tests/test_type_ii_tail_deflation_p_minus_one_core_hybrid.py -q
~~~
