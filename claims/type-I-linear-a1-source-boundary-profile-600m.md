---
kind: claim
claim_id: type-I-linear-a1-source-boundary-profile-600m
title: 线性一般 B 选择器的 a 等于一子族边界
statement: 在线性源p=a+s+asR中限制a=1，等价于穷尽p-1的全部奇因子s并取R=(p-1)/s-1。对冻结的1964个普通Type II压力点，这个子族有15012个源状态并闭合1463点，剩余501点；其中包含214729、297049与878089。因此a=1的p-1因子参数化不是该冻结集上的完备一般B线性选择器，后续跨源理论必须允许a与s两侧均自适应变化。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- linear-source
- shifted-source
- p-minus-one
- target-square-divisor
- selector-boundary
- pressure-set
- computational-profile
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性一般 \(B\) 选择器的 \(a=1\) 子族边界

线性一般 \(B\) 源满足

\[
p=a+s+asR;\;s\equiv1\pmod2;\;R\equiv3\pmod4. \tag{1}
\]

其中最自然的单侧子族是 \(a=1\)。它没有额外自由度：

\[
p=1+s+sR
\quad\Longleftrightarrow\quad
p-1=s(R+1). \tag{2}
\]

所以对固定核心素数，全部 \(a=1\) 状态恰由 \(p-1\) 的奇因子 \(s\) 给出：

\[
s\mid p-1;\;s\text{ 为奇数};\;
R=\frac{p-1}{s}-1. \tag{3}
\]

核心同余使 \((p-1)/s\) 自动为 (8) 的倍数，故 (3) 的 \(R\) 自动满足
\(R\equiv3\pmod4\)。此时

\[
E=sR+1=p-s=n;\;
K=\frac{pR+1}{4}. \tag{4}
\]

因此它是一个有严格有限参数域、但仍允许一般 \(B\) 目标平方除子的线性子选择器。

## 冻结压力集审计

输入为完整线性一般 \(B\) 审计使用的 1,964 个普通 Type II 双尾遗漏。对每个 (3) 的状态，
完整判定

\[
d\mid K^2;\;4d\equiv-1\pmod R, \tag{5}
\]

并在首次命中后重放两侧单位分数恒等式；对无命中素数则穷尽它的全部 \(a=1\) 状态。

| 项目 | 数量 |
| --- | ---: |
| 输入压力点 | 1,964 |
| \(a=1\) 源状态 | 15,012 |
| 审计至首次命中或穷尽的目标 \(R\) | 5,548 |
| \(a=1\) 闭合 | 1,463 |
| \(a=1\) 遗漏 | 501 |

遗漏前缀为

\[
214729, 297049, 629689, 878089, 1447609, 1511449, 2754889, 3942409. \tag{6}
\]

特别地，\(214729\)、\(297049\) 与 \(878089\) 都没有任何 \(a=1\) 一般 \(B\) 线性目标命中；
但它们分别在完整线性菜单或非线性源中有其它证书。故 (6) 是子族边界，不是任何素数的
Erdős--Straus 失败清单。

在 1,463 个命中中，所选模数最常见的是

\[
R=7\ (911\text{ 点});\;R=23\ (368\text{ 点}),
\]

但仍有 501 个遗漏。这说明固定小 \(R\) 射线的强覆盖率来自这个 \(p-1\) 因子切片，却不能
替代允许 \(a>1\) 或更一般源平方状态的自适应选择。

本页严格限于冻结压力集。它不证明 \(a=1\) 在全部核心素数上必失败，也不否定完整线性
一般 \(B\) 选择猜想；它只排除了一个过窄的、完全可枚举的证明收缩。

复现：

~~~bash
python3 reproductions/type_i_linear_a1_source_boundary_profile_600m.py
python3 -m unittest tests.test_type_i_linear_a1_source_boundary_profile_600m -q
~~~
