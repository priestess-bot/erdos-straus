# 建议合并回 erdos-straus 仓库的状态修改

## 1. README / flagship 中 T4 状态

当前 `47fedc2` README 仍将 T4 标为“开放”，但同一 commit 的 theorem ledger 已有：

```text
type-II-q-one-full-carrier-phase-root-entry
claim_status: established
```

其 statement 已经明确声称：

- ordinary q=1 G；
- target-independent full-carrier Type I root；
- fresh_source_tree_only；
- E1--E5；
- Sol(p) identity lift；
- 首个 strict Type I segment。

因此建议改成：

```text
T4 Fresh-G-Handoff | ordinary relative closure established
```

核心断言建议写成：

> 对 ordinary q=1 G endpoint，full-carrier fresh root-entry 给出完整 phase-local E1--E5，并无条件接一条严格 Type I segment。nontrivial marked handoff 与 global T5 admission 分开保留。

## 2. 建议新增 consolidated claim

建议新增：

```text
claim_id: type-II-q-one-fresh-handoff-ordinary-closure
```

statement：

> 对每个 ordinary q=1 Type II G endpoint，存在由 p 唯一预声明的 low full-carrier Type I root；fresh universal p-source 支付 E1，Sol(p) identity 支付 E4，one-way phase rank 支付 E5。root 后强制 odd marked-absorb 或 even fixed-n strict edge。因此 ordinary Fresh-G-Handoff 闭合；该 claim 不含 nontrivial mark、global well-foundedness 或 general Type I selector。

这样可以避免把 T4 的结论分散在 carrier rail、root-entry 和 downstream cards 中。

## 3. 建议新增 mark-preserving 条件 schema

名称：

```text
type_i_full_carrier_low_root_mark_preserving_v1
```

准入条件：

1. source/target equation target 相同；
2. mark predicate 可在 fresh target 中逐字重新序列化；
3. mark 不引用 charged-history-only physical occurrence；
4. E4 明确登记 identity on `W_{p,theta}`；
5. 其它 E1/E2/E3/E5 与 ordinary root-entry 相同。

## 4. 将 `c=8,q_*=103` 移到 T6 子计划

不要继续把该层写成 T4 的 residual。建议命名：

```text
T6-Q1-Image-Totality
```

精确目标：

\[
\forall H\in\mathcal I_{8,103},
\quad
\exists\text{ actual endpoint}:
\text{terminal}\lor c_a<8\lor c_\Sigma<8,
\]

并要求生成完整 E1--E5 receipt。
