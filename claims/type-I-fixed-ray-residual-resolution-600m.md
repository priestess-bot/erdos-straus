---
kind: claim
claim_id: type-I-fixed-ray-residual-resolution-600m
title: 固定 p 减一射线残余的三层自适应解析
statement: 六亿固定 p-1 射线剖面留下的25个点精确分为2个短盒 p-1 证书、12个更大缺口的 p-1 证书、10个 beta=1 的线性 B=1 证书和1个 beta=1 的线性 B=7 证书（p=3942409）。其中只有11个在全正规形意义下没有 p-1 桥。该分流复用有限审计，不是全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- p-minus-one
- linear-source
- b1
- general-B
- terminal-bridge
- pressure-set
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 固定 (p-1) 射线残余的三层自适应解析

[固定 (p-1) 射线剖面](type-I-fixed-pminusone-ray-pressure-profile-600m.md)把 1,964 个冻结的
普通 Type II 尾遗漏压缩到 25 个。这里不重新扫描素数，而是把这 25 个点逐项接入已经完成的
(p-1) 与线性源审计，并重新回放每张所选证书的目标、源单位分数恒等式。

| 解析层 | 数量 | 含义 |
| --- | ---: | --- |
| 短盒 (p-1) | 2 | 已在 (m\le215) 的原始 (p-1) 盒内命中，但不在九条固定 (E\mid144) 菜单中 |
| 无界 (p-1) 延伸 | 12 | 原短盒遗漏，但在去除缺口和 (B) 上界后的全 (p-1) 审计中命中 |
| 线性 (B=1) | 10 | 全正规形意义下无 (p-1) 桥，仍有 \(\beta=1\) 的线性移位源 (B=1) 证书 |
| 线性一般 (B) | 1 | (p=3942409) 在线性 (B=1) 中失败，首个已存线性退出为 (B=7\) |

因此 25 点中真正排除全部 (p-1) 正规形桥的仅有 11 点；这与“23 个短盒遗漏”不同，后者只是
带 (m\le215) 上界的较弱表述。11 点中另有 10 点仍可保持线性源的 \(\beta=1\) 归一化。

这一分流把当前普遍性难点具体化为：证明或寻找一个适应于全正规形 (p-1) 失败点的线性源选择律，
同时解释少数必须使用 (B>1) 的状态。它没有证明这类线性律对所有核心素数成立；固定有限压力集
在这里仅作为反例压力测试和机制筛选器。

复现：

~~~bash
python3 reproductions/type_i_fixed_ray_residual_resolution_600m.py
python3 -m unittest tests.test_type_i_fixed_ray_residual_resolution_600m -q
~~~
