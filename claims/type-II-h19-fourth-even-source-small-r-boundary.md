---
kind: claim
claim_id: type-II-h19-fourth-even-source-small-r-boundary
title: H19 十亿第四压力点的最小偶源尾模数
statement: 对 p=640775689，完整枚举 r=3,7,11,15 的兼容偶源因子对与 M1^2 尾部除子。r=3、11 没有兼容源，r=7 有五条兼容源但平方尾均失败，r=15 首次命中且有12个尾部因子；其较短源表示为 c=34091、d=1253。因此该点的最小可用尾模数是 r=15，而非大距离本身。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- state-compression
- divisor-residues
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿第四压力点的最小偶源尾模数

兼容偶源参数满足

\[
(cr+1)(dr+1)=rp+1. \tag{1}
\]

因此对固定 \(r\)，只需分解 \(rp+1\)，枚举其中两个 \(1\bmod r\) 的因子，即可得到所有
距离 \(c\) 与源因子 \(d\)。尾部尺度为 \(M_1=(rp+1)/4\)，再对 \(M_1^2\) 检查目标
残数。

对

\[
p=640{,}775{,}689,\qquad r=3,7,11,15
\]

逐项穷尽后：

| \(r\) | 兼容源数 | \(M_1^2\) 尾部命中数 |
|---:|---:|---:|
| 3 | 0 | 0 |
| 7 | 5 | 0 |
| 11 | 0 | 0 |
| 15 | 2 | 12 |

所以 \(r=15\) 是该点最小的可用尾模数。它有两条兼容源表示：

\[
(c,d)=(34{,}091,1253),\qquad(8{,}431{,}259,5).
\]

前者给出此前记录的最短距离严格递降。由此可见，\(c=34091\) 并不表示尾部同余的复杂度
必须很大；它来自小 \(r=15\) 状态的一种因子对表示。

这是一个单点有限边界，不是“所有 H19 残余都有小 \(r\)”的猜想。它提示下一步可优先
研究小 \(r\) 的因子对 \((cr+1)(dr+1)=rp+1\) 如何与平方尾残数共同强制命中。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_small_r_boundary.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_small_r_boundary.py -q
~~~
