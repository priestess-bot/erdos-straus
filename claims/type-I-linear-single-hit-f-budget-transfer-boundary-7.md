---
kind: claim
claim_id: type-I-linear-single-hit-f-budget-transfer-boundary-7
title: 七个单命中压力点的 F 型预算边界与局部源转移闭包
statement: 在七个单命中完整线性谱中，16个共享层子群可见但有限盒外的拉回类集中于5个F状态。对473个有向源状态枚举已建立的固定s因子转移、可行变s因子转移和双向坐标交换，共得到1199条有向边；16个边界类均没有有向路径到本素数的命中模数，且没有直接命中边。只有1个边界状态落在含命中的无向连通分量中，说明把这些局部边反向使用也不等于严格递降。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- finite-exponent
- cross-modulus
- shared-layer
- exponent-budget
- source-transfer
- descent
- single-hit
- negative-boundary
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 七个单命中压力点的 F 型预算边界与局部源转移闭包

## 审计对象

上一张[七点 F 型跨源拉回剖面](type-I-linear-single-hit-f-cross-source-pullback-7.md)
给出了 16 个满足

\[
P_{\rm sub}=D_R(S_R)\cap T_\gamma\cap H_L\ne\varnothing,
\qquad
P_{\rm finite}=D_R(S_R)\cap T_\gamma\cap D_R(L)=\varnothing
\]

的边界残类。它们集中在五个状态：

\[
\begin{array}{c|c}
p&(a,s,R)\\ \hline
13782409&(2165,19,335)\\
26034649&(73,951,375)\\
57399241&(1755,211,155)\\
57399241&(101055,1,567)\\
283319689&(93,2443,1247)
\end{array}
\]

对七个核心素数的全部 473 个有向线性源状态，枚举三类已经有精确恒等式的局部操作：

1. 固定 \(s\) 的因子转移 \(q\mid a,\ q\equiv1\pmod s\)；
2. 变 \(s\) 的因子转移 \(q\mid s,\ q\equiv1\pmod a\)，并要求新模数仍为 \(3\pmod4\)；
3. \(a,s\) 都为奇数时的坐标交换，并把交换边视为双向。

命中状态按同一七点完整谱中的一般 \(B\) 命中模数定义。

## 结果

局部转移图的汇总为

\[
\begin{array}{c|r}
\text{对象}&\text{数量}\\ \hline
\text{有向源状态}&473\\
\text{已审计有向边}&1199\\
\text{预算边界残类}&16\\
\text{预算边界状态}&5\\
\text{有向可达命中的边界残类}&0\\
\text{直接指向命中的边界边}&0\\
\text{落在含命中无向分量的边界状态}&1
\end{array}
\]

五个边界状态逐项均满足：

\[
\text{directed\_reaches\_hit}=\text{false},
\qquad
\text{direct\_hit\_edge\_count}=0.
\]

其中 \(p=57399241,(a,s,R)=(101055,1,567)\) 的边界状态位于一个包含命中状态的
无向连通分量中，但沿已审计边的方向仍不能到达命中；其余四个边界状态甚至位于
不含命中的无向分量中。

## 结论边界

这项审计排除了一个具体的弱递降方案：

> 只要共享层把 F 型目标拉回送入仿射块子群，就能沿现有固定 \(s\)/变 \(s\)/交换操作
> 前进到命中模数。

它没有排除新的源构造、非局部因子重分配或普通 Type II 证书，也不反驳混合终端选择引理。
但它把“递降”要求具体化为：必须定义超出这三类操作的缺陷下降机制，或者证明某个预算
缺口可以直接转化为新的正规形。

特别地，无向连通性只能说明局部操作之间存在形式上的合流，不能提供从失败状态到命中
状态的方向性递降。因此后续证明不能只构造一个可逆源图，还必须给出严格下降势函数。

## 复现

~~~bash
python3 reproductions/type_i_linear_single_hit_f_budget_transfer_boundary_7.py
python3 -m unittest tests/test_type_i_linear_single_hit_f_budget_transfer_boundary_7.py -q
~~~

结果文件：
[type-i-linear-single-hit-f-budget-transfer-boundary-7-results.json](../reproductions/type-i-linear-single-hit-f-budget-transfer-boundary-7-results.json)
