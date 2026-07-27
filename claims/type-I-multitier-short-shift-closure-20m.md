---
kind: claim
claim_id: type-I-multitier-short-shift-closure-20m
title: 两千万前缀的Type I多层短移位闭合
statement: 对p不大于20000017的158595个核心素数，完整二幂p减一桥、固定12项非二幂p减一菜单、E不大于10^6的源平方允许p减一因子对、两个固定移位B一状态和四移位动态桥选择器依次闭合151684、6657、227、9、18点，合计全部158595点。最后一层使用移位集合{3,7,9,25}、E不大于10^6、B不大于7，实际B仅为1、2、3、5、7。合成见证的E最大20808、B最大5564、源距离最大25；此为有限计算结论，不推出全称界。
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
- shifted-source
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两千万前缀的 Type I 多层短移位闭合

对所有

\[
p\le20{,}000{,}017,\qquad p\equiv1\pmod{24},
\]

按下列顺序应用精确选择器。每层只作用于先前的遗漏，故计数两两不交。

| 层 | 机制 | 新闭合点数 |
|---|---|---:|
| 1 | 完整允许二幂 \(E=2^t\) 的 \(n=p-1\) 因子对 | 151,684 |
| 2 | 固定 12 项非二幂 \(E\) 菜单、\(B\in\{1,2\}\)、\(n=p-1\) | 6,657 |
| 3 | \(E\le10^6\)、\(E\mid(p-1)^2/4\) 的完整 \(BC\mid K\) 对、\(n=p-1\) | 227 |
| 4 | 固定 \((s,R)=(9,31),(25,19)\) 的 \(B=1\) 移位源除子剩余类 | 9 |
| 5 | 动态桥的短移位 \(s\in\{3,7,9,25\}\)，\(E\le10^6\)、\(B\le7\) | 18 |

因此

\[
151684+6657+227+9+18=158595. \tag{1}
\]

最后一层逐一枚举每个 \(n=p-s\) 的平方因子允许桥 \(E\)，令

\[
R=\frac{E-1}{s},\qquad K=\frac{pR+1}{4},
\]

再穷尽 \(B\le7\) 与 \(BC\mid K\)，并以[源状态实现判据](type-I-normal-source-state-realization.md)
重建目标、偶源和最大尾桥。18 个实际选中的 \(B\) 只属于

\[
\{1,2,3,5,7\}. \tag{2}
\]

按五层组合后，实际最坏参数是

\[
E\le20808,\qquad B\le5564,\qquad p-n\le25. \tag{3}
\]

这里 \(B\le5564\) 来自第 1 层二幂 \(p-1\) 因子对，而非短移位层。第 5 层所用移位集合是由
千万边界及两千万最后状态逐步发现的；它不能被解释为已经证明的全称菜单。故 (1)--(3) 是严格的
两千万前缀计算结论，不是 Erdős--Straus 猜想的证明。其重要的结构性信息是：在该前缀内，所有
基础 \(p-1\) 选择器残余仍可用距离至多 25 的偶源 Type I 状态释放。

可复现命令：

~~~bash
python3 reproductions/type_i_multitier_short_shift_closure_20m.py
python3 -m unittest \
  tests/test_type_i_short_shift_low_e_profile.py \
  tests/test_type_i_multitier_short_shift_closure_20m.py -q
~~~
