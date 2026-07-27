---
kind: claim
claim_id: type-I-direct-b1-gap-extension-500m
title: 五亿尾遗漏的目标级B等于1缺口扩展闭合
statement: 对五亿普通Type II尾遗漏的1717个存储目标，逐目标完整重选Type I正规形并保留严格偶源反向边。m≤215时B=1命中1713个；其四个遗漏39407449、63332329、172657489、193288489在继续枚举至m≤999后，分别首次于m=535、351、707、271以B=1命中。因此全体1717点均有B=1、m≤999的严格偶源Type I反向边，最大首次缺口为707。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- external-source
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿尾遗漏的目标级 B 等于 1 缺口扩展闭合

[目标级小 B 偶源闭合](type-I-direct-small-b-even-source-audit.md) 在
\(m\le215\) 已给出

\[
1717=1713_{B=1}+3_{B=2}+1_{B=8}.
\]

这里不固定先前选定的桥，而是保留其中直接 \(B=1\) 阶段的四个遗漏，继续对每个目标的每个
\(m\equiv3\pmod4\)、\(m\le999\) 枚举全部 Type I 正规形，且对每张正规形枚举最大尾反向提升并要求源分母为严格更小的偶数。四个残余的首次 \(B=1\) 偶源边为：

| \(p\) | 首次 \(B=1\) 缺口 \(m\) | \((A,B,C)\) | 偶源 \(n\) |
|---:|---:|---:|---:|
| 39,407,449 | 535 | \((116,1,84931)\) | 34,030,458 |
| 63,332,329 | 351 | \((5,1,3166634)\) | 62,430,164 |
| 172,657,489 | 707 | \((1809,1,23861)\) | 105,179,288 |
| 193,288,489 | 271 | \((64862,1,745)\) | 48,853,822 |

故在这个存储的五亿压力集上有更强的有限闭合：

\[
1717=1717_{B=1},\qquad m\le999,\qquad \max m_{\rm first}=707. \tag{1}
\]

这说明此前 \(B=2,8\) 的四条边是短缺口盒中的选择结果，而非这些目标必须有指数溢出。它仍不能推出
对任意核心素数存在统一 \(B=1\) 缺口界，也没有把每张证书统一转成递归选择律；结论只覆盖已存储的
1,717 个目标和明确的 \(m\le999\) 盒。

可复现命令：

~~~bash
python3 reproductions/type_i_direct_b1_gap_extension_500m.py
python3 -m unittest tests/test_type_i_direct_b1_gap_extension_500m.py -q
~~~
