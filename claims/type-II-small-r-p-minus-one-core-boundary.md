---
kind: claim
claim_id: type-II-small-r-p-minus-one-core-boundary
title: 小 r 或 p-1 缩放在全部核心素数上的有限边界
statement: 在全部 p<=100000、p=1 mod 24 的1181个素数上，经完整见证复核，r<=103 偶源严格提升覆盖978个；其余203个中 p-1 的 b=2,4 缩放覆盖196个，留下7个联合未命中：5209、12601、21169、27481、48409、80809、97561。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- scaled-source
- p-minus-one
- selector
- boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 小 \(r\) 或 \(p-1\) 缩放在全部核心素数上的有限边界

对所有 \(p\le100\,000\)、\(p\equiv1\pmod{24}\) 的 1,181 个素数，先完整验证
\(r\le103\) 的偶源严格提升：只有在兼容因子对、平方尾和源--目标有理恒等式以及
Type I 证书全部成立时才计为命中。该分支覆盖 978 个，留下 203 个。

对这 203 个再完整枚举 \(n=p-1\) 的 \(b=2,4\) 缩放候选与强制平方尾，覆盖其中
196 个。七个联合未命中为

\[
5\,209,\ 12\,601,\ 21\,169,\ 27\,481,\ 48\,409,\ 80\,809,\ 97\,561.
\]

所以 H19 剖面中的 \(664=564+100\) 不能外推为“所有核心素数都由小 \(r\) 或
\(p-1\) 缩放解决”。这些点只是该**特定析取**的有限边界，不是 Erdős--Straus
猜想的反例，也不排除更大 \(r\)、其它源或其它 Type I/II 证书。

## 重建

~~~bash
python3 reproductions/type_ii_small_r_p_minus_one_core_boundary.py
python3 -m unittest tests/test_type_ii_small_r_p_minus_one_core_boundary.py -q
~~~
