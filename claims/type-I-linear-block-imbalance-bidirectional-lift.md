---
kind: claim
claim_id: type-I-linear-block-imbalance-bidirectional-lift
title: 双向块不平衡终端的奇数距离偶源提升
statement: 对冻结 200 个核心素数完整线性谱中的正向和反向块不平衡广义二进候选，按 (p,R,source,E) 去重并调用精确奇数距离偶源 Type I 提升核，得到 1923 个候选终端、906 个参数和 495 条严格命中，覆盖 47 个样本素数。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-linear-block-imbalance-bidirectional-dyadic
  - type-I-short-relation-odd-distance-even-source
topics:
- type-I
- linear-source
- block-imbalance
- dyadic
- odd-distance
- marked-descent
- finite-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 双向块不平衡终端的奇数距离偶源提升

## 审计对象

双向块差审计保留每个状态满足正向或反向广义二进传输的候选

\[
E=2^{1-J}(2K)\frac AB,\qquad
n=\frac{4K-E}{R}.
\]

同一 \((p,R,\mathrm{source},E)\) 只保留一次；这避免一个终端同时由两个方向或多个 \(J\)
重复计数。随后令 \(c=p-n\)，对每个终端枚举全部

\[
n=d(1+cr),\qquad dr\equiv-1\pmod4,
\]

并枚举 \(e_1\mid M_1^2\)、\(e_1\le M_1\)、\(e_1\equiv-M_1\pmod r\)，逐项验证有理数恒等式、Type I 缺口和目标除子同余。

## 精确结果

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_imbalance_bidirectional_lift.py
~~~

输入为双向终端结果文件
\`type-i-linear-block-imbalance-bidirectional-results.json\`，其哈希锁定为
\`83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f\`。输出为：

~~~text
candidate_row_count: 4301
unique_terminal_count: 1923
parameter_count: 906
hit_count: 495
hit_state_count: 49
hit_prime_count: 47
~~~

命中素数为：

~~~text
15648649, 16002529, 20297209, 30997849, 38333689, 41708209,
53712409, 55375609, 83445289, 84624409, 111810169, 151911769,
155533849, 161342449, 164150809, 178790089, 179700889, 204971209,
274883569, 300873169, 304959769, 312918169, 328186681, 339576169,
355341529, 362050441, 369577849, 371160409, 371275249, 373561609,
383592169, 401426041, 405791929, 457986169, 461890489, 472918009,
475619929, 486323161, 487572409, 508542169, 522155209, 540252409,
542688169, 547053049, 559650361, 590499529, 597694729
~~~

命中是严格的源—目标提升：脚本对每个候选同时检查整数性、平方除子、Type I 缺口范围、同余条件和源/目标有理数恒等式。

## 边界

这是一组有限样本上的局部提升结果，不是全称选择器。仍未解决的部分包括：

1. 双向二进状态中 11673 个没有可行 \(J\) 的状态；
2. 200 个对称状态以及非线性一般 Type I 状态；
3. 906 个参数之外的终端和其它距离/提升族；
4. 如何由这些局部命中或失败证书推出跨状态容量矛盾或良基下降。

线性源本身已有平凡终端 \(E=U=sR+1\)，因此这里的 47 个素数只表示“块不平衡候选族”
中的提升覆盖，不能直接解释成相对于所有线性终端基线的净新增。4301 个候选行中有
4102 个不等于该平凡 \(E=U\)；这些非平凡候选的独立基线差分仍待完成。当前结果仍只是一条可复用的局部 Type I 出口。
