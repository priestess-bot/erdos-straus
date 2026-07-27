---
kind: claim
claim_id: type-I-small-gap-variable-divisor-profile
title: 变量除子 Type I 小缺口扇在一千万内全覆盖
statement: 对全部 \(p\le10^7\) 的82,887个核心素数，完整枚举每个 \(m\le239\)、\(m\equiv3\pmod4\) 的 Type I 平方除子条件。每个素数均有证书；首命中缺口最大为151，仅 \(p=8803369\) 达到该值。首缺口3和7分别覆盖47,137和28,606个点。此为变量除子的精确有限剖面，不证明固定有限缺口扇对所有核心素数的全称覆盖。
claim_status: computationally_reproduced
topics:
- type-I
- small-gap
- divisor-selector
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 变量除子 Type I 小缺口扇在一千万内全覆盖

## 完整检查

对核心素数 \(p\)，每个合法缺口写作

\[
x_m=\frac{p+m}{4},\qquad 3\le m\le239,\qquad m\equiv3\pmod4.
\]

程序完整枚举 \(x_m^2\) 的正因子，并检查 Type I 的等价残数条件

\[
e\mid x_m^2,\qquad e\equiv-\frac14\pmod m, \tag{1}
\]

再由 \(d=x_m^2/e\) 重建并以有理数核验

\[
\frac4p=\frac1{x_m}+\frac1y+\frac1z. \tag{2}
\]

因此没有把除子限制为常数、线性因子、单个素因子或外部源子类。

## 结果

| 项目 | 数值 |
|---|---:|
| 素数上界 | 10,000,000 |
| 核心素数 | 82,887 |
| \(m\le239\) 内命中 | 82,887 |
| 未命中 | 0 |
| 最大首命中缺口 | 151 |

首命中缺口分布的主体为：

| \(m\) | 3 | 7 | 11 | 15 | 19 | 23 | 31 | 其余 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 个数 | 47,137 | 28,606 | 4,463 | 949 | 768 | 635 | 159 | 170 |

唯一首次达到 \(m=151\) 的点是

\[
p=8{,}803{,}369,\qquad x=2{,}200{,}880,\qquad d=180{,}472{,}160.
\]

最小缺口扇 \(3,7,11,15,19,23\) 已在 \(p=21169\) 首次失效，故不能把两万内的
小范围现象提升为六缺口结论；该点在 \(m=31\) 恢复。

## 意义与边界

这是与共享 Type II 小缺口扇相互独立的直接证书信号：前者要求一个额外共享因子，
而这里仅使用完整 Type I 除子格。它表明剩余困难不应被理解为“短缺口没有解”，而是
“如何从 \(x_m\) 的真实因子残数中选择正确的平方除子”。

但该事实并不证明猜想。有限计算不能排除未来出现更大的首缺口，也不能从有限个固定
\(m\) 推出全称命中。尤其，[深层 AC 逃逸的 Type I 仿射边界](type-I-escape-affine-boundary.md)
已经表明在一条条件性进程上，不存在统一的固定缺口常数或仿射除子；任何可能的证明必须
允许随 \(p\) 更新的非仿射因子标记，或跨缺口的因子关系。

因此该剖面给出的研究目标不是“证明 \(m\le239\)”，而是证明一个自适应选择原则：
当较小缺口的除子残数集避开 \(-1/4\) 时，某个可控的新缺口会带来可验证的残数扩张，
并且该扩张不能永久维持失败。

## 重建

    python3 reproductions/type_i_small_gap_profile.py
    python3 -m unittest tests/test_type_i_small_gap_profile.py -q
