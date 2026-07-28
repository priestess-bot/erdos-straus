---
kind: claim
claim_id: type-I-general-b-compensated-square-full-linear-profile-600m
title: 十三点残余上的全线性 R 补偿平方边界
statement: 对一般B补偿平方首选形式后留下的13个压力点，完整枚举每个线性E|n源诱导的R，以及每个R上K^2的全部目标平方因子和对应H^2补偿因子。该机制闭合6点、剩余7点；累计固定流程闭合1964点中的1957点。余7点仅排除该全线性R补偿平方机制，不排除其他Type I或Type II机制。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- compensated-square
- terminal-bridge
- linear-source
- full-linear-menu
- pressure-set
- computational-profile
- residual
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 十三点残余上的全线性 \(R\) 补偿平方边界

输入为 [一般 \(B\) 补偿平方首选形式剖面](type-I-general-b-compensated-square-residual-profile-600m.md)
留下的 13 点。这里不再在首个命中 \(R\) 停止。对每个素数完整枚举

\[
p=a+s+asR,
\qquad s\ \text{为奇数},
\qquad \min(a,s)\le\left\lfloor\sqrt{(p-2)/3}\right\rfloor, \tag{1}
\]

所得的每个不同 \(R\)。在每个 \(R\) 处，穷尽

\[
d\mid K^2,
\qquad4d\equiv-1pmod R, \tag{2}
\]

的所有目标平方因子并恢复正规形；随后穷尽每张形式的 \(H^2\) 除子以检验
[一般 \(B\) 补偿平方桥](type-I-general-b-compensated-square-terminal-bridge.md)。

| 项目 | 数量 |
| --- | ---: |
| 输入残余 | 13 |
| 补偿平方闭合 | 6 |
| 机制内残余 | 7 |
| 全部线性源诱导 \(R\) | 502 |
| 有向线性源状态 | 884 |
| 已检 \(K^2\) 除子 | 571,698 |
| 目标残数命中除子 | 392 |
| 已检正规形 | 196 |
| 已检 \(H^2\) 除子 | 4,196 |
| 合格补偿候选 | 9 |
| 上半区源 | 6 |

实际检验的最大 \(\min(a,s)\) 上界为 13,378。六个新闭合中有四个使用原先首选 \(R\) 之外的
状态，证实只检查“首个目标命中”会漏掉该机制。

剩余的七个素数为

\[
214729,\ 878089,\ 2210569,\ 13782409,\ 64214329,\ 105295129,\ 536944489. \tag{3}
\]

连同前两层的 1,951 个点，固定流程已闭合

\[
1{,}951+6=1{,}957
\]

个冻结压力点。式 (3) 仅意味着：在 (1) 的完整有限线性源菜单内，所有 (2) 的目标正规形均未给出
补偿平方因子。它不排除非线性源、其他目标因子族、一般 Type I 证书或 Type II 证书，因而绝不是
Erdős--Straus 猜想的反例清单。

复现：

~~~bash
python3 reproductions/type_i_general_b_compensated_square_full_linear_profile_600m.py
python3 -m unittest tests.test_type_i_general_b_compensated_square_full_linear_profile_600m -q
~~~
