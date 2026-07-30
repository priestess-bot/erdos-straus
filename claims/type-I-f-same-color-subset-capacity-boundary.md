---
kind: claim
claim_id: type-I-f-same-color-subset-capacity-boundary
title: F 型规范 Fourier 需求的同色联合容量边界
statement: 在冻结的 200 个压力素数完整线性谱中，2748 个达标 Fourier F 状态的 141 个表面容量超载组，在确定性同色载体分配后均无超载；展开为 551 个同色方向对后仍无超载，最高需求/容量比为 1。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-bounded-fourier-full-spectrum
  - type-I-linear-labeled-block-gcd-rigidity
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
topics:
- type-I
- F-state
- finite-fourier
- q-adic
- capacity
- colored-capacity
- full-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# F 型规范 Fourier 需求的同色联合容量边界

## 主张

在冻结的 200 个压力素数完整线性谱中，先取 2748 个达到宽松 Fourier 下界的 F 状态，
再筛出“把全部活跃素数的 (q)-进需求直接相乘”所造成的 141 个表面超载组。对每个
候选状态，按固定规则选择一个线性源状态 ((a,s))，并选择 (aR+1) 或 (sR+1)
中能够承载最多活跃方向的同色载体子集。最后按

\[
\prod_{q\in Q_0}h_q,
\qquad
h_q=\left\lceil\frac{\nu_q+2\mathbf 1_{q=2}}2\right\rceil,
\]

累计该同色子集需求，并与同一素数、同一颜色、同一方向子集、同一 (R)-窗口内全部
线性源块的精确容量

\[
\sum_{(a,s,R)}\prod_{q\in Q_0}v_q(tR+1)
\]

比较。该冻结审计中没有同色容量超载；因此先前的全方向乘积超载不能直接作为跨状态
矛盾，因为它把落在 (aR+1) 与 (sR+1) 的方向错误地放进了同一乘积。

进一步把每个已选同色子集展开为全部二方向子集，得到 551 个同色方向对；配对需求
仍然没有超载，最高需求/容量比为 1，417 组达到饱和。这排除了“只需把完整角色
降到重复的同色方向对即可得到容量矛盾”的最简单加强。

## 口径

这是一个有限负面边界，不是选择器定理。源状态与颜色的分配是规范诊断策略，并不证明
所有可能的 Fourier 证书都必须采用该子集。没有超载只排除了这一种“规范 Fourier 需求
加同色载体”的简单容量闭合；仍需加入相位、投影空缺、半径和跨状态可重复性，或构造
真正的良基算术下降。

## 复现

```text
python3 reproductions/type_i_f_same_color_subset_capacity.py
```

输入哈希和完整结果保存在脚本输出 JSON 中：

```text
reproductions/type-i-f-same-color-subset-capacity-results.json
```
