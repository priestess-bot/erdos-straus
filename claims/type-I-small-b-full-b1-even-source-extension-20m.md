---
kind: claim
claim_id: type-I-small-b-full-b1-even-source-extension-20m
title: 两千万小盒残余的完整B等于1偶源扩展与全范围边界
statement: 在p≤2*10^7的m≤239、B≤4规范Type I尾递降盒的2356个遗漏中，改为枚举每个B=1正规形的全部最大尾反向边并要求严格偶源。m≤999时命中2351个，剩余21169、2922529、5101441、5410441、5655049；将这五点延至m≤9999后2922529和5410441分别于1671和1479命中。特别地，对21169穷尽全部3≤m≤21167、m=3 mod4后仅有(m,A,B,C)=(31,4,1,1325)一张B=1正规形，其唯一严格反向源为奇数18441，故不存在任何B=1最大尾严格偶源反向边。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- external-source
- finite-audit
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两千万小盒残余的完整 B 等于 1 偶源扩展与全范围边界

从[小 B 小缺口 Type I 严格递降的两千万剖面](type-I-small-b-tail-deflation-profile.md)取出
\(m\le239,B\le4\) 中仍未命中的 2,356 个核心素数。这里不再限制源为规范 \(p\)-尾去缩放：
对每个 \(m\equiv3\pmod4\)，令 \(x=(p+m)/4\)，枚举每个

\[
C\mid x,\qquad 4C\equiv-1\pmod m,\qquad A=x/C. \tag{1}
\]

这恰穷尽 \(B=1\) 的 Type I 正规形。对每张正规形再穷尽最大目标尾的全部反向桥因子，只保留
严格更小的偶源。

## 两层有限剖面

在 \(m\le999\) 中，2,351 条命中，且最晚首命中为 \(m=791\)；余下仅

\[
21169,\ 2922529,\ 5101441,\ 5410441,\ 5655049. \tag{2}
\]

把这五点延至 \(m\le9999\)，其中

\[
2922529\ (m=1671),\qquad 5410441\ (m=1479)
\]

获得首个严格偶源 \(B=1\) 边，仍余 \(21169,5101441,5655049\)。因此，先前在规范尾坐标
下的 1,429 个 \(m\le999\) 遗漏绝大多数只是保留坐标的选择效应；但有限扩展也并未给出全覆盖。

## 全范围反例边界

对最小残余 \(p=21169\)，自然范围本身有限，因而可穷尽

\[
3\le m\le p-2=21167,\qquad m\equiv3\pmod4. \tag{3}
\]

整个范围只有一张 \(B=1\) 正规形：

\[
(m,A,B,C)=(31,4,1,1325).
\]

其最大尾的唯一严格反向边有源分母 \(18441\)，为奇数。故这个目标没有任何 \(B=1\)、
最大尾保留两项、严格偶源的 Type I 反向边。

这严格排除了如下过强路线：对每个核心素数，只在 \(B=1\) 正规形中寻找最大尾偶源递降。
它没有排除 \(B>1\)、改变保留坐标、Type II 边或其他源状态，因而不是对 Erdős--Straus
猜想的反例。

可复现命令：

~~~bash
python3 reproductions/type_i_small_b_full_b1_even_source_extension.py
python3 -m unittest tests/test_type_i_small_b_full_b1_even_source_extension.py -q
~~~
