---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-pure-new-100m-closure
title: 双尾抽缩、p-1 递降与状态依赖纯新因子的亿元闭合
statement: 在 p<=10^8 的719781个核心素数中，Type II 双尾抽缩和 p-1 的 b=1,2,4 严格递降覆盖719740个。余下41个中27个在规范位移s<=2有短证书，另14个均在3<=s<=48由相对于p+4,p+8的纯新单素因子 Type II 证书闭合；其中5个首个成功位移的最小 h 证书含两个新因子，但3个同位移另有纯新证书，余2个在后续位移释放。因此该有限范围有719781=719281+459+27+14的短证书或递降闭合。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- short-certificate
- tail-deflation
- scaled-source
- canonical-ray
- new-factor
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-26'
---

# 双尾抽缩、\(p-1\) 递降与状态依赖纯新因子的亿元闭合

在 \(p\le10^8\) 的 719,781 个核心素数上，先运行两条严格递降：

\[
719\,781=719\,281_{\mathrm{Type\,II\ strict\ descent}}
+459_{p-1\ \mathrm{strict\ descent}}
+41_{\mathrm{certificate\ residual}}.
\]

对最后 41 点，以 \(p+4,p+8\) 的全部素因子为旧来源，分两步检查规范 Type II 射线：

\[
41=27_{s\le2}+14_{\text{later pure-new one-prime}}.
\]

后 14 点的纯新单素因子首次释放深度分布为

\[
\begin{array}{c|rrrrrr}
s&3&4&5&9&24&48\\
\hline
\#&6&3&2&1&1&1.
\end{array}
\]

在五点的首个成功位移上，按最小 (h) 选择的证书含两个新素因子；其中三点在同一位移已有较大的纯新单素因子替代，余下两点才须等待更后位移释放。
最深样本为

\[
p=56\,040\,889:
\quad h=171\,379=13\cdot13\,183\text{ 在 }s=11,
\quad h=789\,311\text{ 在 }s=48.
\]

后一因子是相对于 \(p+4,p+8\) 的新素数。故把“首个最小因子证书”强制为单新素因子在此范围已失败，
但同一位移的其他证书有时已足够；完整扫描后的“稍后存在状态依赖的单新因子释放”仍覆盖全部这 14 个样本。

这不是有界深度定理，更不把最后的 Type II 证书当作严格递降；它将下一研究靶明确为
证明或反驳某个状态依赖的纯新因子释放原则。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_p_minus_one_pure_new_100m_closure.py
python3 -m unittest tests/test_type_ii_tail_deflation_p_minus_one_pure_new_100m_closure.py -q
~~~
