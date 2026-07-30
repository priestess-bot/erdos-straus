---
kind: claim
claim_id: type-I-f-square-obstruction-carrier-census
title: 混合奇偶平方障碍的 F 型 Fourier 载体普查
statement: 在冻结的 200 个完整线性谱中，4524 个较小块平方机制的混合奇偶障碍包含 877 条 F 型源状态行、874 个唯一 F 状态键。校正后的 Fourier 记录完整保留 2752 个有限指数状态键；F 障碍行的 2718 个活跃方向均有 U=sR+1 或 V=aR+1 载体达到保守 q 进高度需求。按 (p,q,颜色) 及阶/相位细分的原始和去重容量组均无超载，最大需求/容量比为 1。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-linear-block-square-terminal-boundary
  - type-I-f-bounded-fourier-radius-boundary
  - type-I-linear-labeled-block-gcd-rigidity
topics:
- type-I
- F-state
- finite-fourier
- q-adic
- carrier-vector
- colored-capacity
- data-integrity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 混合奇偶平方障碍的 F 型 Fourier 载体普查

## 审计对象

较小块平方边界把双向未决状态分成三类。这里取其中精确失败的

\[
U<V,\qquad U=sR+1\text{ 为偶数},\qquad V=aR+1\text{ 为奇数},
\]

共 4524 条源状态行。按完整谱的状态键

\[
(p,R,K)
\]

回查其 G/F/hit 分类，得到

\[
3279\ \mathrm{G},\qquad 877\ \mathrm{F},\qquad 368\ \mathrm{hit}.
\]

4524 条记录对应 3856 个唯一状态键；F 行对应 874 个唯一 F 状态键，三条重复行来自
同一个状态键的不同定向源状态。

## Fourier 输入完整性

本审计先检查完整谱和 Fourier 结果的状态键集合相同，并逐条验证

\[
4K=pR+1,
\qquad
K=\prod_{q^e\parallel K}q^e.
\]

校正后的 Fourier 结果包含全部 2752 个有限指数状态键，恒等式失败数为零。F 障碍
行中有 876 条使用达到宽松缺失下界的有界角色，1 条使用未达到下界的候选；后一条仍
作为边界记录保留，不被当作统一 Fourier 定理。

## 载体规则

对每个 F 障碍行和每个规范 Fourier 活跃素数 (q)，记录

\[
h_s=v_q(U),\qquad h_a=v_q(V),
\]

并把载体颜色规范选为高度较大的块；并列时固定选 `a`。需求采用此前容量审计中的
宽松下界

\[
h_q^{\mathrm{req}}
=
\left\lceil
\frac{v_q(K)+2\mathbf 1_{q=2}}2
\right\rceil.
\]

由于

\[
v_q(U)+v_q(V)=v_q(4K),
\]

逐状态直接检查得到 2718 个活跃方向全部满足

\[
\max(h_s,h_a)\ge h_q^{\mathrm{req}};
\]

局部高度缺口数为零，并列载体方向数为 27。

## 跨状态容量边界

对每个载体记录，按以下三种键分组：

1. \((p,q,\mathrm{color})\)；
2. 上述键加角色阶；
3. 上述键加活跃素数集合和目标相位分子/分母。

每组需求是所选记录的 (h_q^{\mathrm{req}}) 之和，容量是在该组最小和最大 (R)
窗口内所有完整线性源块的

\[
\sum v_q(tR+1)
\]

之和。原始源行和按 ((p,R,K,q,\mathrm{color})) 去重后分别得到：

\[
\begin{array}{c|c|c|c}
\text{分组键}&\text{组数}&\text{超载组}&\max(\text{需求}/\text{容量})\\ \hline
\text{p,q,color}&2449&0&1\\
\text{加角色阶}&2683&0&1\\
\text{加活跃集合与相位}&2710&0&1
\end{array}
\]

去重后的三行组数相同，超载数仍为零；饱和组很多，但没有严格超载。

## 逻辑边界

这项结果只排除一个具体的简化闭合：把混合奇偶平方障碍的规范 Fourier 活跃方向
逐个转成高度需求，再装入同色线性块容量，不能产生全局容量矛盾。它没有证明：

- 规范有界 Fourier 候选是所有角色中的全局最大者；
- 每个 F 状态必须使用该候选或同一载体颜色；
- 相位质量、盒溢出半径和多方向联合需求可被当前标量容量替代；
- 因而也没有得到全称 Type I/II 选择器或算术下降。

当前最明确的后续桥梁是把盒溢出层数、相位余量或目标纤维稀疏度转成额外需求；否则
继续细分同一个保守容量账本只会得到更多饱和而不是超载。

## 复现

```bash
python3 reproductions/type_i_f_square_obstruction_carrier_census.py
```

结果文件：

```text
reproductions/type-i-f-square-obstruction-carrier-census-results.json
```
