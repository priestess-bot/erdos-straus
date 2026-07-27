---
kind: claim
claim_id: type-I-small-b-normal-form-profile
title: Type I 互素正规形的小 B 一亿剖面
statement: 对所有 p<=10^8、p=1 mod24，完整枚举 m<=239 的 Type I 正规形 x=ABC、gcd(A,B)=1、m|Bp+A；每个 719781 个核心素数均命中 B<=4，其中最小 B 的频数为 B=1:719770、B=2:7、B=3:3、B=4:1。此为有限计算剖面，不推出固定 B 或固定缺口界。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- divisor-selector
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-divisor-certificate-equivalence
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-25'
---

# Type I 互素正规形的小 B 一亿剖面

## 完整检查

对每个核心素数和每个合法缺口，写

\[
x=\frac{p+m}{4}=ABC,\qquad (A,B)=1.
\]

由 [Type I 互素因子正规形](type-I-coprime-factor-normal-form.md)，这给出 Type I
证书的充要条件是

\[
m\mid Bp+A. \tag{1}
\]

程序先按 \(B=1,2,3,4\) 排序，再按缺口排序；对每个 \((B,m)\)，它枚举
\(x/B\) 的**全部**正因子 \(A\)，检查互素性和 (1)，并重建、精确核验三个分母。
因此该程序在给定的 \(B\) 与 \(m\) 截断内不是模板搜索，而是完整的正规形搜索。

## 结果

| 项目 | 数值 |
|---|---:|
| 素数上界 | 20,000,000 |
| 核心素数 | 158,595 |
| 缺口范围 | \(m\le239\) |
| \(B\le4\) 命中 | 158,595 |
| 未命中 | 0 |

以同一缺口上界将审计扩展至 \(10^8\)，结果仍为全覆盖：719,781 个核心素数全都在
\(B\le8\) 命中，实际最大最小 \(B\) 仍为 4。

| 素数上界 | 核心素数 | \(B=1\) | \(B=2\) | \(B=3\) | \(B=4\) | 未命中 |
|---:|---:|---:|---:|---:|---:|---:|
| \(2\cdot10^7\) | 158,595 | 158,590 | 2 | 2 | 1 | 0 |
| \(10^8\) | 719,781 | 719,770 | 7 | 3 | 1 | 0 |

故在一亿审计中全部 11 个非外部 source 点的溢出因子都属于 \(\{2,3,4\}\)；尚未看到
需要新溢出素数的样本。这是选择器的正向线索，不是对更大范围的外推。

最小 \(B\) 的精确分布为：

| 最小 \(B\) | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| 个数 | 158,590 | 2 | 2 | 1 |

五个非 \(B=1\) 点为：

| \(p\) | \(B\) | \(m\) | \(A\) | \(C\) |
|---:|---:|---:|---:|---:|
| 1,282,009 | 2 | 71 | 5 | 32,052 |
| 3,364,561 | 2 | 63 | 223 | 1,886 |
| 4,962,049 | 3 | 23 | 166 | 2,491 |
| 16,337,281 | 4 | 159 | 35 | 29,174 |
| 17,307,721 | 3 | 23 | 4 | 360,578 |

特别地，\(B=1\) 恰是外部 source 子类，但这里的 \(A\) 是随 \((p,m)\) 的真实因子
自适应选择，而不是一个固定或仿射除子。故该现象没有被已有的固定因子、仿射因子或固定
缺口条件性逃逸边界否定。

参数 \(B\) 的作用还可精确写出。由 \(p=4ABC-m\)，(1) 等价于

\[
m\mid A(4B^2C+1).
\]

而 \((A,m)=1\)，故再等价于

\[
m\mid4B^2C+1. \tag{2}
\]

所以 \(B=1\) 只寻找余因子 \(C\equiv-1/4\pmod m\)；较小的 \(B>1\) 则只需
\(B^2C\equiv-1/4\pmod m\)。等价地，\(B\) 是目标平方除子相对 \(x\) 的指数溢出，
见 [目标除子溢出正规形](type-I-target-divisor-overflow.md)。这是一种由真实因子平方提供的
离散“平方增益”，并非另加一条独立的线性模板。

## 为什么这是当前较强的正向信号

该剖面把原有的“完整平方除子格在小缺口内常命中”进一步压缩成一个更小的自由度：
只需解释为何存在很小的互素伴随因子 \(B\)，随后允许 \(A\mid x/B\) 自适应地命中
\(-Bp\pmod m\)。这比要求某个固定 \(m\)、固定 \(A\) 或固定 Type II 射线更贴近
可选择的算术对象。

合理的理论目标不是宣称 \(B\le4\)，而是下列二择一的可证伪命题：

\[
\text{长期小-}B\text{ 失败}
\Longrightarrow
\begin{cases}
\text{相邻缺口出现可控的 }B\text{ 正规形证书，或}\\
\text{从 }(A,B,C)\text{ 因子标记构造真正可提升的较小源状态。}
\end{cases} \tag{3}
\]

要推进 (2)，应把 \(B=1\) 的失败按缺口编译为除子残数积集状态，再研究最小的
\(B>1\) 如何以 \(B^2\) 改变余因子目标。五个例外显示 \(B\) 不能直接固定为 1；它们也给出
具体的反例训练集，用来检验任何候选闭合引理是否错误地排除了 \(B=2,3,4\)。

## 范围

这是有限审计。它没有证明：

- \(m\le239\) 对所有核心素数有效；
- 存在统一常数 \(B\)；
- \(B\) 的增长可由对数或多项式控制；
- 该选择器能转化为归纳或递降证明。

尤其，已知的条件性多缺口逃逸说明不能从高覆盖率推断固定窗口终止。该剖面的价值在于
提供一个比“继续增加分支”更窄、可反驳、可与因子残数理论直接耦合的研究对象。

## 重建

    python3 reproductions/type_i_small_b_normal_form_profile.py
    python3 reproductions/type_i_small_b_normal_form_profile.py --limit 100000000 --gap-cap 239 --b-cap 8 --output reproductions/type-i-small-b-normal-form-100m-profile.json
    python3 -m unittest tests/test_type_i_small_b_normal_form_profile.py -q
