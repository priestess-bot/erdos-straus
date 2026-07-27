---
kind: claim
claim_id: type-I-multitier-short-source-closure-10m
title: 千万前缀的Type I多层短源闭合
statement: 对p不大于10000009的82887个核心素数，按完整二幂p减一桥、固定12项非二幂p减一菜单、E不大于10^6的源平方允许p减一全因子对、两个固定移位B一状态以及最终七条低B一般源边依次闭合，计数为79062、3673、140、5、7，总计82887。所选见证中E最大24986，B最大2701，源距离最大263。该结论是有限计算闭合，不给出全称界。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- factorization
- dyadic
- source-state
- selector
- finite-audit
- closure
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 千万前缀的 Type I 多层短源闭合

对所有

\[
p\le10{,}000{,}009,\qquad p\equiv1\pmod{24},
\]

按下表顺序应用证书选择器。每层只处理此前未命中的点，因此计数无重叠。

| 层 | 机制 | 新闭合点数 |
|---|---|---:|
| 1 | 完整允许二幂 \(E=2^t\) 的 \(n=p-1\) 因子对 | 79,062 |
| 2 | 固定 12 项非二幂 \(E\) 菜单、\(B\in\{1,2\}\)、\(n=p-1\) | 3,673 |
| 3 | \(E\le10^6\)、\(E\mid(p-1)^2/4\) 的完整 \(BC\mid K\) 对、\(n=p-1\) | 140 |
| 4 | 固定移位 \((s,R)=(9,31),(25,19)\) 的 \(B=1\) 除子剩余类 | 5 |
| 5 | 最终七点的完整自然缺口、\(B\le4\) 一般源审计 | 7 |

所以

\[
79062+3673+140+5+7=82887. \tag{1}
\]

最后七点仍全部属于[源状态实现判据](type-I-normal-source-state-realization.md)的同一 Type I
坐标；其中五点为 \(B=1\)，另两点分别为 \(B=2\) 与 \(B=3\)。按最短源选择，它们的源距离为

\[
25,25,9,49,263,9,3. \tag{2}
\]

合成的实际参数边界为

\[
E\le24986,\qquad B\le2701,\qquad p-n\le263. \tag{3}
\]

这里的第 3 层仅搜索 \(E\le10^6\)，第 4 层只含两个固定移位状态，第 5 层也仅对最后七点完整。
因此 (1)--(3) 是已验证的千万前缀事实，绝非对所有素数的统一界或猜想的证明。它的推进意义是：
相较百万前缀，新的边界仍只留下 152 个二层 \(p-1\) 共同残余，其中 140 个由一般 \(p-1\) 因子对、
5 个由既有短移位状态、7 个由极小 \(B\) 的新短源状态释放。

可复现命令：

~~~bash
python3 reproductions/type_i_multitier_short_source_closure_10m.py
python3 -m unittest tests/test_type_i_multitier_short_source_closure_10m.py -q
~~~
