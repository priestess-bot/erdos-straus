---
kind: claim
claim_id: type-I-linear-block-imbalance-bidirectional-dyadic
title: 线性块不平衡的双向广义二进终端
statement: 若线性块不平衡归一化为 A=2^j B mod R，则正向与反向表示分别使用 J≡j 和 J≡-j (mod ord_R(2)) 的同一广义二进传输判据；在冻结 200 素数完整线性谱的 15356 个二进状态中，双向审计得到 3683 个有终端状态、11673 个双向未决状态，反向方向从单向审计中额外救回 907 个状态。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-general-dyadic-terminal-transfer
  - type-I-general-bidirectional-dyadic-window-selector
  - type-I-linear-block-imbalance-dyadic-trichotomy
topics:
- type-I
- linear-source
- block-imbalance
- dyadic
- orientation
- even-terminal
- finite-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性块不平衡的双向广义二进终端

## 双向传输

在线性块不平衡三分中，去掉二进部分并规范取向后得到互素奇除子

\[
A\equiv2^{j_0}B\pmod R,\qquad j_0=|\lambda_2|.
\]

令 \(o=o_R(2)\)。正向传输使用

\[
J\equiv j_0\pmod o,\qquad 1\le J\le v_2(2K),
\]

并要求 \(A<2^JB\)。若这些条件成立，一般二进传输给出

\[
E_J=2^{1-J}(2K)\frac AB,\qquad
n_J=\frac{4K-E_J}{R}.
\]

同一关系也可反向书写为

\[
B\equiv2^{j_1}A\pmod R,\qquad
j_1\equiv-j_0\pmod o,
\]

其中 \(j_1=o\) 在 \(o\mid j_0\) 时取作正代表。于是对换 \(A,B\)，并检查

\[
J\equiv j_1\pmod o,\qquad
B<2^JA,
\]

仍由同一个二进传输判据得到合法偶终端。这里没有增加新的除子假设，只是保留原同余关系的另一方向；正向和反向候选可以同时存在。

由[双向广义二进窗口的规范最大指数选择引理](type-I-general-bidirectional-dyadic-window-selector.md)，
每个非空方向只须检查其窗口中的最大 \(J\)。若正反窗口同时非空，则两个高度条件不可能
同时失败，故必有终端；因此双向未决精确分成“无窗口”“仅正向窗口且高度失败”和
“仅反向窗口且高度失败”三类，不存在双窗口未决。

## 冻结审计

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_imbalance_bidirectional.py
~~~

脚本哈希锁定[线性块不平衡关系与广义二进终端三分](../reproductions/type-i-linear-block-imbalance-trichotomy-results.json)，对其中全部 15356 个二进状态同时审计正向和反向方向：

~~~text
source_dyadic_state_count: 15356
bidirectional_terminal: 3683
bidirectional_unresolved: 11673
rescued_from_forward: 907
terminal_candidate_count: 4301
forward candidates: 3017
reverse candidates: 1284
terminal_prime_count: 200
~~~

最大窗口规范选择对同一批状态给出窗口计数

~~~text
none: 7433
forward_only: 6460 = 2274 hit + 4186 unresolved
reverse_only: 232 = 178 hit + 54 unresolved
both: 1231 = 1231 hit + 0 unresolved
~~~

按正向优先的规范选择只返回每个状态一个终端，方向计数为正向 2776、反向 907，并与
原完整枚举的 3683 个命中状态逐项一致。

其中 \`rescued_from_forward\` 表示原单向三分被标记为 \`dyadic_unresolved\`、但反向方向满足预算和高度条件的状态。候选数大于状态数，是因为同一状态可能有多个合法 \(J\) 或两个方向均可行。

## 边界

双向扩展只减少了状态内二进传输的方向性假遗漏，并没有处理：

1. 11673 个双向未决状态；
2. 对称分支和核关系以外的目标平方除子命中；
3. 偶终端到 Type I 目标的平方尾提升；
4. 跨状态 \(q\)-进容量或良基下降。

因此它是统一选择器的一个严格局部增强：应优先把 4301 个候选终端送入提升核，但不能把双向覆盖误写成 Erdős–Straus 猜想的全称证明。
