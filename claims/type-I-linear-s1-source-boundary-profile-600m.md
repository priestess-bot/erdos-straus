---
kind: claim
claim_id: type-I-linear-s1-source-boundary-profile-600m
title: 线性一般 B 选择器的 s 等于一子族边界
statement: 在线性源p=a+s+asR中限制s=1，等价于穷尽p-1的全部因子a并取R=(p-1)/a-1。对冻结的1964个普通Type II压力点，这个子族有31046个源状态并闭合1827点，仍剩137点；其中包含214729、297049、878089、13782409、64214329和105295129。任意a=1状态交换两个坐标后给出同一R的s=1状态，故a=1目标谱包含在s=1目标谱内。于是这137点在完整线性一般B审计中必须使用a>1且s>1的证书。
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

# 线性一般 \(B\) 选择器的 \(s=1\) 子族边界

在线性源

\[
p=a+s+asR;\;s\equiv1\pmod2;\;R\equiv3\pmod4, \tag{1}
\]

中取 \(s=1\)，精确得到

\[
p=a+1+aR
\quad\Longleftrightarrow\quad
p-1=a(R+1). \tag{2}
\]

因此，固定核心素数的全部 \(s=1\) 状态恰由 \(p-1\) 的因子 \(a\) 参数化：

\[
a\mid p-1;\;
R=\frac{p-1}{a}-1\equiv3\pmod4. \tag{3}
\]

它们都有源 \(n=p-1\)、桥因子 \(E=R+1\)。这里仍允许目标端的任意一般 \(B\)：

\[
d\mid K^2;\;4d\equiv-1\pmod R;\;K=\frac{pR+1}{4}. \tag{4}
\]

## 与 \(a=1\) 切片的精确关系

若 \(a=1\)，则 \(p=1+s+sR\) 且 \(s\) 为奇数。交换两个坐标给出

\[
p=s+1+sR, \tag{5}
\]

即同一 \(R\) 的 \(s=1\) 状态。目标条件 (4) 只依赖 \((p,R)\)，所以

\[
\mathcal R_{a=1}^{\rm tgt}(p)\subseteq
\mathcal R_{s=1}^{\rm tgt}(p). \tag{6}
\]

故先前的 \(a=1\) 审计不是独立的更强路线，而是本页 \(s=1\) 因子切片的真子集。

## 冻结压力集审计

在完整线性一般 \(B\) 审计的 1,964 个普通 Type II 双尾遗漏上，程序穷尽每个 (3) 的状态，
对每个状态完整判定 (4)。有命中时保存并重放两侧单位分数证书；无命中素数则穷尽其全部
\(s=1\) 状态。

| 项目 | 数量 |
| --- | ---: |
| 输入压力点 | 1,964 |
| \(s=1\) 源状态 | 31,046 |
| 审计至首次命中或穷尽的目标 \(R\) | 5,701 |
| \(s=1\) 闭合 | 1,827 |
| \(s=1\) 遗漏 | 137 |

遗漏前缀为

\[
214729, 297049, 878089, 1511449, 3942409, 5478169, 6294649, 10170169. \tag{7}
\]

其中包括 \(214729\)、\(297049\)、\(878089\)、\(13782409\)、\(64214329\) 与
\(105295129\)。它们在完整线性一般 \(B\) 审计中均有证书，但不存在任何 \(s=1\) 的目标
命中；由 (6) 也不存在 \(a=1\) 的目标命中。因此这些冻结点的线性证书必须满足

\[
a>1;\;s>1. \tag{8}
\]

这比只排除 \(a=1\) 更直接地否定了“仅由 \(p-1\) 的一侧因子化选择线性源”的证明收缩。
它仍是有限压力集结论，不排除这些素数的非线性源平方证书或其它 Type II 坐标，也不构成
Erdős--Straus 猜想的反例。

复现：

~~~bash
python3 reproductions/type_i_linear_s1_source_boundary_profile_600m.py
python3 -m unittest tests.test_type_i_linear_s1_source_boundary_profile_600m -q
~~~
