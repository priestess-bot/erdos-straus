---
kind: claim
claim_id: type-II-h19-same-r-failure-ac-profile
title: H19 同参数外部源失败的半径六直接 AC 证书
statement: 对十亿 H19 剖面中21个 r+1 不整除 p-1 的高溢出首状态，完整枚举 max(A,C)<=6 的 AC Type II 射线且 K 不设界后，21个全部有直接 Type II 证书；最小半径分布为3:7、4:6、5:4、6:4。半径5遗漏4点，故此样本内半径6确为必要。这是有限直接证书闭合，不给出一般半径界。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- short-certificate
- external-source
- finite-audit
- h19
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
- paper: bradford2024
  locator: Propositions 2 and 3
  role: Type-II-certificate-and-descent-context
visibility: public
last_checked: '2026-07-26'
---

# H19 同参数外部源失败的半径六直接 AC 证书

对 [偶源尾同证书缩减的 r 除子判据](odd-distance-even-source-same-tail-deflation-divisibility.md)
留下的 21 个高溢出状态，\(r+1\nmid p-1\)，所以不能把原 \(r\) 直接作为外部源模数。
除了已知的替代外部源外，还直接枚举 Type II 的 AC 射线

\[
h=4ACK-1\mid p+4A^2C,\qquad \max(A,C)\le6, \tag{1}
\]

其中 \(K\) 不设预先上界，而由 \(p+4A^2C\) 的全部因子恢复。每个命中都精确检验
\(p+4A^2C=h\cdot\text{gap}\) 及其三项 Type II 单位分数证书。

| 最小半径 \(\max(A,C)\) | 状态数 |
| ---: | ---: |
| 3 | 7 |
| 4 | 6 |
| 5 | 4 |
| 6 | 4 |

故 21 个点全部有直接证书；半径 5 仍遗漏四点，半径 6 在该固定样本内确为必要。一个边界例是

\[
p=540{,}645{,}121,\qquad(A,C,K,h)=(6,6,12,1727),
\]

它给出 \(p+4A^2C=1727\cdot313055\) 与 Type II 除子 \(216\)。这正是此前唯一三支持
复合尾且不能取 \(q=r\) 外部源的状态。

因此，十亿 H19 高溢出分流可更精确地表述为：70 个满足 \(r+1\mid p-1\)，故由同参数
\(q=r\) 外部源闭合；余 21 个已有半径至多 6 的**直接** Type II 证书。这个有限闭合不证明
所有同参数失败点都有有界 \(A,C\)，也不能替代“从失败强制选择另一个 \(q\)”的一般引理。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_same_r_failure_ac_profile.py \
  --input reproductions/type-ii-h19-overflow-tail-deflation-profile-1b-results.json \
  --ac-bound 6 \
  --output reproductions/type-ii-h19-same-r-failure-ac-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_same_r_failure_ac_profile.py -q
~~~
