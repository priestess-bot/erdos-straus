---
kind: concept
concept_id: research-directions-and-proof-gap
title: 研究路线总图与逐点证明缺口
summary: 主要路线分别处理可解同余类、例外集、解的参数化与计数、有限计算、局部整体障碍和一般化问题；它们的结论不能互相替代为对每个核心素数的构造。
topics:
- research-map
- congruences
- sieve
- parametrization
- computation
- algebraic-geometry
- generalization
used_by:
- reduction-to-one-mod-24
- vaughan-exception-bound
- average-solution-count
- chamberland-type-II-equivalence
- historical-computation-ladder
- no-brauer-manin-disproof
- type-II-pure-new-canonical-fan-superlog-tail
- dynamic-low-defect-tail-or-external-exit-selector
- type-II-pure-new-exception-dynamic-selector-1m-h100
- type-II-pure-new-exception-dynamic-selector-10m-h100
- type-II-pure-new-exception-selector-counterexample-1m-h20
- h19-k23-unbridged-pressure-full-low-defect-rays
sources:
- mordell1969
- rosati1954
- yamamoto1965
- vaughan1970
- elsholtz_tao2013
- elsholtz_planitzer2020
- bright_loughran2020
- bradford2024
- chamberland2026
- pomerance_weingartner2026
visibility: public
last_checked: '2026-07-27'
---

# 研究路线总图与逐点证明缺口

主要路线分别处理可解同余类、例外集、解的参数化与计数、有限计算、局部整体障碍和一般化问题；它们的结论不能互相替代为对每个核心素数的构造。

## 数学说明

这张路线图以“能回答什么问题”而不是以论文题名分类。它也是阅读新论文时的第一层筛选器。

| 路线 | 已确立的主要结论 | 对猜想仍缺少的步骤 |
|---|---|---|
| 经典恒等式、同余类与多项式族 | 将问题约化到 \(p\equiv1\pmod{24}\)；固定多项式机制能覆盖非平方原始类。 | 证明所有核心素数落入某个可解类，或找到不受平方类障碍限制的统一构造。 |
| 解析筛法与例外集 | Vaughan 给出密度一；本库进一步证明任意固定 \(\alpha>0\) 时，\(H=(\log\log X)^\alpha\) 的纯新规范扇失败集为 \(X\exp[-\Omega_\alpha((\log\log X)\log\log\log X)]\)。 | 从“例外极稀”推出“例外为空”，或为每个真实例外构造统一出口。 |
| Type I/II、gcd 与除子参数 | 对素数解的整除型态给出穷尽分类；T/E 二分选择器在 \(E_{\mathrm{new}}(10^7,100)\) 有 7,056 个有限命中、在两条 H19-k23 压力进程上成立，但已被 \(E_{\mathrm{new}}(10^6,20)\) 的三个完整反例否定；三点各有 \(\mathrm{AC}_2\) 终端证书。 | 定义并检验状态依赖 AC 终端分支，使它与纯新筛和 T/E 严格递降形成正确的三分接口。 |
| 解计数与枚举算法 | 平均解数很大，并能在标准分解模型下较快枚举全部解。 | 平均丰富或快速枚举都不排除某个输入没有解。 |
| 模筛与大规模计算 | 公开报告已把有限检查推进到 \(10^{18}\)，代码与筛结构可审查。 | 用有限上界替代无穷量词，或得到独立的全量复现。 |
| log K3 与 Brauer-Manin | 自然 Brauer 类不制造对所需整点的该类障碍，并解释局部二次条件。 | 排除一种障碍不是构造整点，更不是局部整体原理。 |
| 一般 \(m/n\)、更多单位分数与 Erdős-Straus-Schinzel 问题 | 可迁移计数、算法和例外集工具，也显示一般固定分子存在不同的例外现象。 | 一般问题的定理不能自动回推为 \(m=4\) 的逐点结论。 |

因而，声称“解决猜想”的新工作至少应给出一条覆盖全部 \(p\equiv1\pmod{24}\) 的闭合证明链：有限同余族须证明覆盖性，除子参数须证明对所有 \(p\) 的存在性，计算则须明确其有限范围和可复现边界。

## 常见误读

- 密度一、平均正下界、有限窗口覆盖和无 Brauer-Manin 障碍都不是逐点存在性证明。
- 参数化的充要条件与这些参数对所有素数都存在，是两个不同命题。
- 一般分子或更多项的结果只能提供方法与反例边界，不能自动解决原猜想。
