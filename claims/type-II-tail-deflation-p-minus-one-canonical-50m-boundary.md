---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-canonical-50m-boundary
title: 双尾抽缩、p-1 递降与规范短证书的五千万位移边界
statement: 在 p<=5*10^7 的374902个核心素数中，Type II 双尾抽缩严格递降覆盖374600个，p-1 的 b=1,2,4 严格缩放递降再覆盖282个。对余下20个，规范位移s<=2仅覆盖16个，遗漏25073689、33011449、42622969、48825529；将扇扩至s<=5则全部20个有直接 Type II 证书，给出有限短证书或递降闭合374902=374600+282+20。
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
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 双尾抽缩、\(p-1\) 递降与规范短证书的五千万位移边界

对 \(p\le5\cdot10^7\) 的 374,902 个核心素数，前两条严格递降分支给出

\[
374\,902=374\,600_{\mathrm{Type\,II\ strict\ descent}}
+282_{p-1\ \mathrm{strict\ descent}}
+20_{\mathrm{direct\ certificate}}.
\]

最后 20 点只检查规范 Type II 射线时，固定 \(s\le2\) 仍留下恰好四点：

\[
25\,073\,689,\quad33\,011\,449,\quad42\,622\,969,\quad48\,825\,529.
\]

故位移 \(1,2\) 的补偿扇在这个有限范围不是全称选择器。其四点首次成功位移分别为

\[
3,\quad3,\quad4,\quad5.
\]

具体可取的射线因子为

\[
\begin{array}{c|c|c|c}
p&s&h\mid p+4s&4a c\\
\hline
25\,073\,689&3&47&12\\
33\,011\,449&3&3347&12\\
42\,622\,969&4&31&8\\
48\,825\,529&5&239&20
\end{array}
\]

其中 \(s=a^2c\)，并且每行 \(h\equiv-1\pmod{4ac}\)，故由规范 Type II 射线直接
给出证书。将搜索扇扩至 \(s\le5\) 后，全部 20 点被捕获，没有剩余。

这项结果同时给出正反两面信息：五千万范围仍有有限短证书或递降闭合，但任何正向选择
定理不能预设统一位移上界为 2。真正待证明的量应允许位移随因子状态增长，或给出另一条
严格递降来吸收这种增长。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_full_audit.py --limit 50000000 \
  --output reproductions/type-ii-tail-deflation-50m-full-results.json
python3 reproductions/type_ii_tail_deflation_p_minus_one_10m_boundary.py \
  --input reproductions/type-ii-tail-deflation-50m-full-results.json \
  --output reproductions/type-ii-tail-deflation-p-minus-one-50m-results.json
python3 reproductions/type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py \
  --input reproductions/type-ii-tail-deflation-p-minus-one-50m-results.json \
  --canonical-shift-cap 2 \
  --output reproductions/type-ii-tail-deflation-p-minus-one-canonical-50m-s2-boundary.json
python3 reproductions/type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py \
  --input reproductions/type-ii-tail-deflation-p-minus-one-50m-results.json \
  --canonical-shift-cap 5 \
  --output reproductions/type-ii-tail-deflation-p-minus-one-canonical-50m-results.json
~~~
