---
kind: claim
claim_id: type-I-mixed-terminal-dense-upper-b1-reselection-profile-600m
title: 五亿至六亿连续区间经上半区源重选的 B 等于一闭合
statement: 对500000000<p<=600000000的247个普通Type II p-1双尾遗漏，207个初始m<=215的B=1正规形已经给出偶上半区源n>=(p+1)/2。其余40个从同一有限盒完整生成上半区源状态后，按正规形缺口优先重选均有m<=87的B=1实现；初始直接记录的最大缺口为131。故此连续有限区间的混合终端闭合可加强为“普通双尾或m<=131的上半区B=1 Type I桥”。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- p-minus-one
- upper-half-source
- source-reselection
- small-B
- finite-audit
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿至六亿连续区间经上半区源重选的 \(B=1\) 闭合

[连续区间 B等于一剖面](type-I-mixed-terminal-dense-b1-600m.md)对每个普通 Type II
\(p-1\) 双尾遗漏给出一张 \(B=1\) 的 Type I 终端桥，但该桥的源未必在上半区。本审计只对
初始源满足

\[
2n<p+1
\]

的记录重新搜索。对每一个这样的素数，完整枚举同一有限盒

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

中的所有 Type I 正规形与严格最大尾反向提升，保留偶且满足

\[
n\ge\frac{p+1}{2}
\]

的源状态。这里的 \(m\le215\) 只约束源状态的生成；对每个状态 \((p,n,E)\)，按

\[
R=\frac{E-1}{p-n},\qquad K=\frac{pR+1}{4}
\]

用精确 \(B=1\) 条件

\[
C\mid K,\qquad 4C\equiv-1\pmod R
\]

重新构建 Type I 正规形，同时复核目标和源的单位分数恒等式。

## 结果

| 项目 | 数值 |
| --- | ---: |
| 普通双尾遗漏 | 247 |
| 初始 \(B=1\) 源已在上半区 | 207 |
| 初始下半区 \(B=1\) 源 | 40 |
| 经上半区源重选恢复 \(B=1\) | 40 |
| 上半区 \(B=1\) 遗漏 | 0 |
| 重选后 \(B=1\) 正规形缺口超过 215 | 0 |
| 重选后 \(B=1\) 正规形最大缺口 | 87 |
| 合并后所选 \(B=1\) 正规形最大缺口 | 131 |
| 重选枚举的正规形 | 2,331 |
| 重选枚举的严格反向边 | 6,643 |

因此该区间的精确有限分流可写成

\[
621{,}951
=621{,}704_{\mathrm{ordinary\ Type\ II\ tail}}
+247_{\mathrm{Type\ I\ upper\!-\!half,\ B=1}}.
\]

这与五亿范围内 \(p=218{,}482{,}009\) 的短源窗口 \(B=1\) 失败形成必要对照：源重选确实是
一阶关键自由度。按最短源距离选出的重建缺口可能很大，但按缺口优先重选后，本连续区间全部
回到 \(m\le131\)。这仍不自动给出全称 \(B=1\) 界，也不把第一个阶段的源选择变成固定规则。

## 范围

这是一个与先前五亿残余不重叠的连续区间压力测试。它支持“先选源、再选小 \(B\) 正规形”的
二层研究方向；没有证明任意核心素数都有相应终端桥，也没有给出跨区间可用的源状态构造或
重建正规形的全称缺口界。

重建命令：

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_upper_b1_reselection_profile.py
python3 -m unittest tests/test_type_i_mixed_terminal_dense_upper_b1_reselection_profile.py -q
~~~
