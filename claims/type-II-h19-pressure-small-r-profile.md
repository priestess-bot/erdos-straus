---
kind: claim
claim_id: type-II-h19-pressure-small-r-profile
title: H19 十亿压力集的小 r 偶源尾选择剖面
statement: 对 p<=10^9 的四个 H19 平方因子递降遗漏，完整扫描 r=3 mod4、r<=103 的兼容因子对 (cr+1)(dr+1)=rp+1 及 M1^2 尾部。四点均闭合，首个命中 r 依次为103、31、31、15；对应较短距离为7、3、3、34091。因此该压力集支持小 r 状态选择器，却明确反对固定小距离选择器。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- selector
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

# H19 十亿压力集的小 r 偶源尾选择剖面

完整平方因子外部源递降在十亿 H19 残余剖面中留下四个压力点。对每个点，不按距离 \(c\)
扫描，而按

\[
r\equiv3\pmod4,\qquad (cr+1)(dr+1)=rp+1 \tag{1}
\]

枚举全部兼容因子对，并检查唯一尾状态

\[
M_1=\frac{rp+1}{4},\qquad
e_1\mid M_1^2,\quad e_1\equiv-M_1\pmod r. \tag{2}
\]

在 \(r\le103\) 的有限审计中，四点均有命中：

| \(p\) | 首个 \(r\) | 最短对应距离 |
|---:|---:|---:|
| 35,840,809 | 103 | 7 |
| 132,285,169 | 31 | 3 |
| 141,326,089 | 31 | 3 |
| 640,775,689 | 15 | 34,091 |

所以小 \(r\) 不是小距离的同义词：第四点仍要求较长距离，却有最小的首个 \(r\)。这给出
一个比固定 \(c\) 更有希望的有限选择器坐标。

结论仍只是四个已知压力点的计算事实。特别是它没有证明每个 H19 残余有
\(r\le103\)，也没有控制因子对中的 \(c,d\) 大小。下一步理论问题是：平方因子递降失败
时，能否强制某个受控 \(r\) 的 \(rp+1\) 出现兼容因子对，并使 (2) 命中。

将这四条状态实际重建为严格源--目标提升后，便与 660 条标准递降共同给出十亿 H19
剖面的纯递降闭合，见
[H19 十亿标准递降或受控 r 偶源递降闭合](type-II-h19-hybrid-small-r-descent.md)。

## 重建

~~~bash
python3 reproductions/type_ii_h19_pressure_small_r_profile.py
python3 -m unittest tests/test_type_ii_h19_pressure_small_r_profile.py -q
~~~
