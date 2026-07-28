---
kind: claim
claim_id: type-I-general-b-compensated-square-residual-profile-600m
title: 十三点前的一般 B 补偿平方重放剖面
statement: 对B=1补偿平方后留下的21个压力点，取已有完整一般B线性审计为每点确定性选择的一张正规形，完整枚举该形式补因子H的平方除子T。一般B补偿平方桥命中8点，余13点；命中的原始选择B值分布为B=1三点、B=2两点、B=3两点、B=11一点。该剖面不穷尽每点其他线性源或正规形。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- compensated-square
- terminal-bridge
- linear-source
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

# 十三点前的一般 \(B\) 补偿平方重放剖面

本剖面输入 [\(B=1\) 补偿平方残余](type-I-b1-compensated-square-profile-600m.md) 的 21 个点，
并复用 [完整一般 \(B\) 线性源审计](type-I-linear-source-general-b-completion-profile-600m.md) 对每点
按最小坐标顺序选定的第一张命中正规形。对这张形式的 \(H^2\) 的所有除子，穷尽检验

\[
T\equiv4B^2pmod R,
\qquad q=(H-BCT)/R>0,
\qquad Tmid qH. \tag{1}
\]

结果如下：

| 项目 | 数量 |
| --- | ---: |
| 输入残余 | 21 |
| 一般 \(B\) 补偿平方闭合 | 8 |
| 仍未命中 | 13 |
| 已检所选形式的 \(H^2\) 除子 | 429 |
| 合格候选 | 12 |
| 所选源位于上半区 | 6 |

八个命中按输入线性证书的 \(B\) 分布为 \(B=1\) 三点、\(B=2\) 两点、\(B=3\) 两点、\(B=11\)
一点。故一般 \(B\) 的有效机制确实包括不同于 \(T=4B^2\) 的补偿因子。

把前面两层的 1,943 个闭合点加上这里的 8 个，得到冻结 1,964 点中的 1,951 点已由这条有限、
分层流程闭合，剩余 13 点。这里的 13 点只是对**每点一个预选线性正规形**的失败；它们仍可能有
另一个线性源、另一个正规形、一般 Type I 机制或 Type II 证书。不能将该清单解释为猜想反例，
也不能由此推出全称选择引理。

对这 13 点的全部线性源诱导 \(R\) 菜单继续穷尽后，见
[全线性 \(R\) 补偿平方边界](type-I-general-b-compensated-square-full-linear-profile-600m.md)。

复现：

~~~bash
python3 reproductions/type_i_general_b_compensated_square_residual_profile_600m.py
python3 -m unittest tests.test_type_i_general_b_compensated_square_residual_profile_600m -q
~~~
