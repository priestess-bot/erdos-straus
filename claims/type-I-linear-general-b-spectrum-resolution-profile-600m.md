---
kind: claim
claim_id: type-I-linear-general-b-spectrum-resolution-profile-600m
title: 七个补偿平方残余的全线性目标谱闭合
statement: 对全线性R补偿平方机制留下的七个冻结压力点，完整枚举每个线性E整除n源诱导的R和每个K^2目标平方除子。每点至少有一个目标谱命中；将同一R的任一线性源与该命中配对，直接重放beta=1偶终端桥。因此七点全部由普通线性一般B证书闭合，补偿平方失败不构成一般B选择器失败的证据。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- linear-source
- target-square-divisor
- centered-spectrum
- terminal-bridge
- pressure-set
- computational-profile
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 七个补偿平方残余的全线性目标谱闭合

[全线性 \(R\) 补偿平方边界](type-I-general-b-compensated-square-full-linear-profile-600m.md)
留下的七点只说明补偿平方因子族没有命中。它们不是
[线性一般 \(B\) 终端选择猜想](type-I-linear-source-general-b-terminal-selector-conjecture.md)
的残差：后者只要求同一线性源模数上的一个目标平方除子命中，并不要求该除子来自补偿平方构造。

本审计以那七点为哈希冻结输入，完整枚举每个

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4, \tag{1}
\]

的有向线性源状态。枚举使用 \(u=\min(a,s)\) 的精确有限界；对每个不同的 \(R\)，令

\[
K=\frac{pR+1}{4}, \tag{2}
\]

并穷尽

\[
d\mid K^2;\;4d\equiv-1\pmod R. \tag{3}
\]

每个命中按一般 \(B\) 正规形恢复。设其参数为 \((A,B,C,H,m)\)，则
\(d=B^2C\)、\(BCH=K\)。与同一 \(R\) 的任一 (1) 配对，令

\[
E=sR+1;\;n=p-s=aE. \tag{4}
\]

线性恒等式给出

\[
4K=(aR+1)E;\;n=\frac{4K-E}{R}. \tag{5}
\]

因此 \(E\mid n\)、\(E\mid4K^2\)、\(E\equiv1\pmod R\)，且 \(n\) 为偶数；
由 \(n\ge2\) 还得到 \(E\le4K-2R\)。故不需要任何额外的补偿因子：源端直接有

\[
\frac4n=\frac1{aK}+\frac1{ABC}+\frac1{ACH}. \tag{6}
\]

## 完整有限结果

| 项目 | 数量 |
| --- | ---: |
| 输入机制残余 | 7 |
| 目标谱闭合 | 7 |
| 未闭合 | 0 |
| 全部线性源诱导 \(R\) | 278 |
| 有向线性源状态 | 490 |
| 已检 \(K^2\) 除子 | 340,842 |
| 目标残数命中除子 | 158 |
| 恢复的目标正规形 | 79 |
| 直接终端证书候选 | 119 |

每点择一张稳定排序的证书如下；完整分母和全部局部检查保存在结果 JSON 中。

| \(p\) | \((a,s,R)\) | \((B,C)\) | \(E\) | \(n\) |
| ---: | --- | --- | ---: | ---: |
| 214729 | \((4,409,131)\) | \((9,19)\) | 53580 | 214320 |
| 878089 | \((4,3705,59)\) | \((7,16669)\) | 218596 | 874384 |
| 2210569 | \((92107,1,23)\) | \((1,684)\) | 24 | 2210568 |
| 13782409 | \((11680,9,131)\) | \((5,1141)\) | 1180 | 13782400 |
| 64214329 | \((4057,133,119)\) | \((1,13536)\) | 15828 | 64214196 |
| 105295129 | \((1643,1831,35)\) | \((1,971)\) | 64086 | 105293298 |
| 536944489 | \((1,22372687,23)\) | \((4,37)\) | 514571802 | 514571802 |

特别地，\(p=878089\) 在全部线性 \(B=1\) 版本中失败，却在 \(R=59\) 有一般 \(B\) 的目标谱命中；这与既有单点剖面相符。其余六点表明：即使补偿平方搜索已在所有线性来源上失败，普通目标平方谱仍可能有多个命中模数。

结论严格限于该七点的有限菜单。它澄清了补偿平方机制的边界，却没有证明任何未检查核心素数必有这种跨源目标谱命中，因而不能升级为全称选择引理或 Erdős--Straus 猜想的证明。

复现：

~~~bash
python3 reproductions/type_i_linear_general_b_spectrum_resolution_profile_600m.py
python3 -m unittest tests.test_type_i_linear_general_b_spectrum_resolution_profile_600m -q
~~~
