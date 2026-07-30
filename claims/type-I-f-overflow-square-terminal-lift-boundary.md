---
kind: claim
claim_id: type-I-f-overflow-square-terminal-lift-boundary
title: 多支持较小块平方终端的奇数距离提升边界
statement: 对多支持溢出分支的 506 个确定性较小块平方终端去重后得到 253 个不同的 (p,R,source,E)；将其全部接入现有奇数距离偶源 Type I 参数化，得到 0 个合法参数、0 个平方尾候选和 0 个目标素数命中。该结果只排除当前提升族在这批终端上的直接覆盖，不排除其它距离、源族或目标选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-multi-support-square-descent-boundary
  - type-I-short-relation-odd-distance-even-source
topics:
- type-I
- F-state
- overflow-radius
- block-square
- even-terminal
- odd-distance
- lift
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-lift-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持较小块平方终端的奇数距离提升边界

## 审计范围

从多支持溢出脚本产生的 506 个确定性较小块平方终端中，按
\((p,R,\operatorname{source},E)\) 去重，得到 253 个终端。对每个终端令
\(c=p-\operatorname{source}\)，完整枚举现有奇数距离偶源提升接口要求的

\[
\operatorname{source}/d=1+cr,\qquad dr\equiv-1\pmod4,
\]

以及所有满足 \(e_1\mid M_1^2\)、\(e_1\le M_1\) 和
\(e_1\equiv-M_1\pmod r\) 的平方尾。

## 结果

```text
unresolved_record_count: 291
support_record_count: 253
assignment_count: 506
unique_terminal_count: 253
parameter_count: 0
tail_candidate_count: 0
hit_state_count: 0
hit_prime_count: 0
```

因此当前较小块平方终端虽然给出严格更小的偶源，但没有自动进入已知的奇数距离
偶源 Type I 提升族。该结果把剩余缺口从“有没有终端”收紧为“如何选择距离/源族，
使终端携带可提升的目标除子”。

## 逻辑边界

这是一个有限、定向的负面边界：

1. 它不否定其它奇数距离、偶距离、平移平方尾或一般 Type I/II 选择；
2. 它不说明 253 个源没有 Erdős–Straus 表示；
3. 它不影响较小块平方作为状态内严格下降候选的有效性。

下一步应研究由 \(E=\min(U,V)^2\) 的块因子结构直接诱导的距离参数，而不是继续把
同一个奇数距离模板套到这些终端上。

## 复现

```bash
python3 reproductions/type_i_f_overflow_square_terminal_lift.py
```

结果文件：

```text
reproductions/type-i-f-overflow-square-terminal-lift-results.json
```

结果文件 SHA-256：

```text
ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1
```
