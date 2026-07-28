---
kind: claim
claim_id: type-I-fixed-source-window-linear-escape-boundary-600m
title: 固定源窗口不能判定线性 B 等于一逃逸的平方本质
statement: 在五亿至六亿上半区重选的完整 m<=215 源状态菜单中，p=512335849 的3个B=1候选源均有beta属于{9142,37630,420637}，p=531010489的唯一候选有beta=5，因此该窗口内均无beta=1候选；但分别完整穷尽全部线性源p=a+s+asR后，前者在R=39,231、后者在R=7,11,31,75均有beta=1的B=1命中，最小目标缺口分别为535和267。故固定源窗口中的非线性现象不能升级为全局平方本质障碍。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- b1
- linear-source
- source-square
- source-reselection
- finite-window
- selector-boundary
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 固定源窗口不能判定线性 \(B=1\) 逃逸的平方本质

## 精确问题

五亿至六亿的上半区 \(B=1\) 重选审计，从所有 \(m\le215\) 的 Type I 正规形及其严格
最大尾反向提升中，生成一个有限的偶上半区源状态菜单。对源状态写

\[
n=p-s,\qquad E=sR+1,
\]

并用[源平方正规分解](type-I-source-square-normal-factorization.md)写成

\[
\frac n\lambda=\alpha\beta\gamma,\qquad
\frac E\lambda=\beta^2\gamma. \tag{1}
\]

这里 \(\beta=1\) 当且仅当 \(E\mid n\)，即该源是线性的
\(p=a+s+asR\)。本页比较两个不同的量化域：

1. 固定的 \(m\le215\) 源状态菜单；
2. 给定 \(p\) 的全部线性源，按
   \(u=\min(a,s)\) 和 \(p-u=v(1+uR)\) 完备枚举。

## 两个窗口假象

对下列两个五亿至六亿普通双尾遗漏，窗口内的所有 \(B=1\) 源候选均已直接检查：

| \(p\) | 窗口源状态数 | 枚举正规形 / 反向边 | 窗口内 \(B=1\) 候选的 \(\beta\) |
| ---: | ---: | ---: | --- |
| 512,335,849 | 3 | 43 / 8 | \(9142,37630,420637\) |
| 531,010,489 | 4 | 35 / 6 | \(5\) |

所以两点在这个完整的固定窗口内都没有 \(\beta=1\) 的 \(B=1\) 候选。若只看该窗口，
很容易误判平方额外指数已经是必要的。

## 全线性反证

线性源有严格界

\[
u\le\left\lfloor\frac{\sqrt{1+3p}-1}{3}\right\rfloor,
\]

故下表中的全线性枚举不是搜索截断：

| \(p\) | \(u\) 上界 | 定向线性源 | 不同 \(R\) | \(B=1\) 命中 \(R\) | 最小缺口线性见证 |
| ---: | ---: | ---: | ---: | --- | --- |
| 512,335,849 | 13,067 | 87 | 52 | \(39,231\) | \((a,s,R,C,m)=(2073,6337,39,5216,535)\) |
| 531,010,489 | 13,303 | 99 | 58 | \(7,11,31,75\) | \((1,66376311,7,467,267)\) |

两张最小缺口见证都满足 \(E=sR+1\mid n=p-s\)，因而 \(\beta=1\)。例如第一张有

\[
E=247144,\qquad n=512329512=2073E,
\]

且第二张有 \(E=n=464634178\)。程序对每个诱导 \(R\) 穷尽 \(K=(pR+1)/4\) 的
全部正除子，检查 \(4C\equiv-1\pmod R\)，并用精确有理数重放目标和源的三单位分数
恒等式。

## 含义与边界

这不是新的全局线性 \(B=1\) 定理，也不反驳 \(p=878089\) 的全局线性 \(B=1\) 反例。
它证明的是更精确的研究方法边界：**从固定缺口生成的源状态菜单中观察到
\(\beta>1\)，不能推出该素数的所有线性 \(B=1\) 源都失败。**

因此，若要证明平方额外指数在某个点确实全局必要，必须像 \(p=878089\) 一样穷尽全部
线性源或全部相关源平方状态；不能以一个固定 \(m\) 盒作为替代。对全称选择器的后续研究，
源状态菜单必须允许随素数自适应扩展，而不是先假定一个统一的有限缺口窗口。

## 可复现检查

~~~bash
python3 reproductions/type_i_fixed_source_window_linear_escape_boundary_600m.py
python3 -m unittest tests.test_type_i_fixed_source_window_linear_escape_boundary_600m -v
~~~
