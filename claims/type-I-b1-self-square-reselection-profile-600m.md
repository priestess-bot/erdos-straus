---
kind: claim
claim_id: type-I-b1-self-square-reselection-profile-600m
title: 六亿普通尾压力集上 B 等于一自平方桥的正规形重选
statement: 在六亿冻结的1,964个普通 Type II 双尾遗漏中，完整枚举 B=1 正规形并用 A 奇且 A>=2m 的自平方上半区判据重选：m<=215 时命中1,844个；将同一有限盒扩至m<=999时命中1,907个，余57个。两个结论都只是有限目标盒剖面，不能推出无界 B=1 选择律。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- b1
- self-square
- terminal-bridge
- upper-half
- normal-form-selection
- pressure-set
- computational-profile
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 六亿普通尾压力集上 \(B=1\) 自平方桥的正规形重选

[自平方终端桥](type-I-b1-self-square-terminal-bridge.md)把可检验条件化为

\[
A\equiv1\pmod2,
\qquad A\ge2m. \tag{1}
\]

因此本审计不沿用先前为其他终端桥选定的单一 \(B=1\) 形式。对冻结的 1,964 个普通 Type II
双尾遗漏，逐个枚举指定 \(m\)-盒中的**全部** \(B=1\) Type I 正规形；每个满足 (1) 的形式都以
\(E=16C^2\) 重放目标、偶源及上半区三项单位分数恒等式。

| 目标盒 | 命中 | 剩余 | 已检 \(B=1\) 正规形 | 上半区自平方候选 | 最大所选 \(m\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(m\le215\) | 1,844 | 120 | 17,492 | 6,012 | 215 |
| \(m\le999\) | 1,907 | 57 | 27,531 | 7,856 | 971 |

在 \(m\le999\) 层，早期 \(p\le5\times10^8\) 部分命中 1,662、剩余 55；连续的
\(5\times10^8<p\le6\times10^8\) 部分命中 245、剩余 2。故增加目标正规形选择显著缩小了
压力集，但没有消除残余。

这里“完整”只限定在表中的固定素数集、\(B=1\) 与给定的 \(m\) 上界。57 个点不意味着不存在
其他 Type I、一般 \(B\)、Type II 或更大缺口的证书；反过来，1,907 个命中也不蕴含每个核心素数
都能选择满足 (1) 的正规形。这是一条对后续全称选择引理的有限压力测试，而不是该引理的证明。

复现：

~~~bash
python3 reproductions/type_i_b1_self_square_reselection_profile_600m.py
python3 reproductions/type_i_b1_self_square_reselection_profile_600m.py \\
  --gap-cap 999 \\
  --output reproductions/type-i-b1-self-square-reselection-profile-600m-m999-results.json
python3 -m unittest tests.test_type_i_b1_self_square_reselection_profile_600m -q
~~~
