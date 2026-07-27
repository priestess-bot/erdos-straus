---
kind: claim
claim_id: h19-k23-m39-m47-selector-boundary
title: H19-k23 的 m=39 未命中到 m=47 平滑基底边界
statement: 在524288层 H19-k23 原m=27替代记录的170个m=39支持度至多二的未命中中，全部14条进程满足48|p-1。允许m=47的完整2,3平滑基底扩展后，42条由基底闭合，68条由基底加一个新增素数幂闭合，6条需两个不同新增素因子，余54条在完整m=47扫描中失败而首次转到m=59,63,71,79，频数为45,3,4,2。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- divisor-selection
- factor-support
- smooth-numbers
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 的 \(m=39\) 未命中到 \(m=47\) 平滑基底边界

对前一层 170 个 \(m=39\) 支持度至多二的未命中，全部 14 条进程仍有

\[
48\mid p-1.
\]

令

\[
m=47=4\cdot12-1,\qquad u=\frac{p+47}{48},\qquad x=12u.
\]

相应普通 Type II 双尾条件是

\[
1\le d\le12u,\qquad d\mid144u^2,\qquad d\equiv-12u\pmod{47}. \tag{1}
\]

## 正确的平滑基底

因为

\[
12^2=2^4 3^2,
\]

完整基底必须包括 \(u\) 中的 \(2,3\) 次幂：

\[
d=2^a3^b,\qquad
0\le a\le4+2v_2(u),\quad 0\le b\le2+2v_3(u). \tag{2}
\]

其后才按不同于 \(2,3\) 的新增素因子数目增加支持度。该指数界来自
\(144u^2=x^2\)，并在每个候选上直接复核平方根补全标准形。

## 524,288 层边界

完整审计给出

\[
170=42_{\text{smooth base}}+68_{\text{one new prime}}
+6_{\text{two new primes}}+54_{\text{no }m=47}. \tag{3}
\]

剩余 54 条的第一次成功尾缺口为

\[
45_{59}+3_{63}+4_{71}+2_{79}. \tag{4}
\]

因此 \(m=47\) 恢复了 42 条完全平滑的出口，但仍不能把单新增素数提升为全称原则；
全部 54 个残余同时排除了本层的零、一、二新增素因子选择器。这仍是有限闭包产物的
分类，不提供无限范围的支持度上界。

重建命令：

~~~bash
python3 reproductions/h19_k23_m39_m47_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m39-m47-selector-profile-524288.json
python3 -m unittest tests/test_h19_k23_m39_m47_selector_profile.py -q
~~~
