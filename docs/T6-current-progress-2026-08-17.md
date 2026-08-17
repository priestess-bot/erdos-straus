# T6 Global Selector 当前进度（复核整理版）

> 复核日期：2026-08-17
> 文档角色：T6 的状态入口；技术推导和候选引理见 [T6-V1.md](T6-V1.md)。
> 结论状态：`T6_GLOBAL_SELECTOR_TOTALITY = OPEN`。本页不把 T6、任一 high-support exit 或 Erdős--Straus 猜想标记为已证明。

## 1. 当前结论

对每个核心素数 \(p\equiv1\pmod{24}\)，T6 要求一个确定性的 selector
\(\Sigma(p,S)\)，它对每个由已验证边实际可达的 legal state
\(S\in\mathcal R_p\) 输出终端，或输出一条完整的递归边：

\[
\operatorname{terminal}(S)
\quad\text{or}\quad
\operatorname{verified\_edge}(S,T).
\]

后一项必须同时包含 E1--E5：实际 source/path、确定 target、target normal form、
\(W_T\to W_S\) 的全域解提升，以及固定 T5 势的严格下降。selector 不能读取未知目标解，
不能依赖有限搜索上界，并且必须对自己的后继继续有定义。精确量词见
[旗舰证明纲领](../concepts/flagship-proof-program-2026-08-16.md) 和
[状态合同](../concepts/denominator-escape-state-contract.md)。

目前已经建立的是“已承认 recursive edge 必然下降”，而不是“每个 nonterminal state 都已有边”：

\[
\boxed{
\operatorname{verified\_edge}(S,T)
\Longrightarrow
\Pi_{T5}(T)<\Pi_{T5}(S),
\qquad
\text{但 }\operatorname{Out}_{\mathrm{verified}}(S)\text{ 的非空性仍待证明。}
}
\]

因此，在当前合同的实际可达域中排除 dead end 是 T6 的首要存在性缺口；随后还须把可用
出口固定为不读取未知解的确定性规则。T6 不是 T5 的同义改写。

## 2. 已接纳结果与边界

| 项目 | 当前状态 | 已接纳范围 | 仍未覆盖的部分 |
|---|---|---|---|
| T1 / H4 clean \(q\) | 相对闭包已建立 | 归档的 actual arm 与其具名 receipt | 其它 H4 selector branch、后续 F/G 出口 |
| T2 | `v1` 局部 grammar 闭合 | H4 \(a=1\) actual arm；条件性的 c=8 double-low arm | 所有 raw path、pooled-capacity、输入覆盖与全域 admission |
| T3 | 开放 | Type-II gcd-shadow 的部分端点机制 | nontrivial marked terminal membership 的全称处理 |
| T4 | ordinary \(q=1\) 相对闭包已建立 | \(W=\operatorname{Sol}(p)\) 的 q=1 G 到 fresh full-carrier Type-I root，及首个严格段 | nontrivial mark、positive-\(q\) G、后续 Type-I totality |
| T5 | 合同层闭合 | 所有 contract-recognized persistent edge 的七元势严格下降 | 任何 E1--E4 candidate 自动有 ticket，或 selector totality |
| T6 | 开放 | terminal-first 与五类输出的验收规则 | 每个实际可达 nonterminal state 的 terminal 或 verified successor |

T2/T3 和未覆盖的 T1/T4 输入域不能因 T5 已闭合而从 T6 的总量词中删除。它们在当前
proof spine 中也许不会都落到同一个 high-support 分支，但尚无“只剩 high-support/root-stutter”
的全局归约定理。

## 3. 已确认不能使用的捷径

1. **只凭 \(A\mid K\) 重置到 fresh low chart。** 这会丢弃 charged history；缺少实际
   persistent receipt 时不能通过 E1--E5。
2. **PRE/ABSORB 的形式调度或有限图无环。** 它们至多提供 E5 的相位规则。没有 E1--E4 和
   全域 lift 的 cursor edge 仍不是递归边。
3. **Fourier、商群或 q-adic 必要条件。** `analysis_evidence` 不会自动成为
   `support_switch`、`q_adic_lift` 或 `verified_edge`。
4. **把更小整数或一张 Type-I chart 当作递降。** \(n<p\) 或 \(k\mid K\) 不产生
   \(\operatorname{Sol}(n)\to\operatorname{Sol}(p)\) 的 lift，也不支付旧 support 的账。

这些边界由 [状态合同的 E1--E5 规则](../concepts/denominator-escape-state-contract.md) 和
[T5 合同](../concepts/t5-global-well-foundedness-contract-v2.md) 固定。

## 4. 当前研究焦点

### 4.1 Ordinary G 的 positive-\(q\) adapter 仍是开放接口

T5 的 `TYPEII_G_HANDOFF -> TYPEI` 相位下降会自动支付 E5，**前提是**已经有 E1--E4。
但现存 full-carrier adapter 的 source guard 明确是 `q=1`，并要求 q=1 G separator、
实际 \(p\)-edge 和具名 state digest。故下列说法尚未建立：

\[
\text{every ordinary positive-}q\text{ G endpoint}
\longrightarrow
\text{fresh full-carrier Type-I root}.
\]

这是一条值得研究的 adapter 设计问题，而不是已从 q=1 定理自动推广出的结论。需要新增
source guard、E1 replay、canonical target serialization 和 ordinary-mark preservation 的完整回执。

### 4.2 High-support / proper-root stutter 是优先残余，而非全局压缩定理

对已进入 Type-I `CHARGED` 的状态，\(A>B_p=(p-1)^2/4\) 时
\(\lfloor B_p/A\rfloor=0\)。此时必须通过 \(K/A\) 的真实下降、phase drop、outer-rank
source 或 terminal 处理；不能只凭内部 checkpoint 支付 E5。

proper-root stutter 提供了较强的算术结构：正定 Eisenstein 范数、小商和约化除子；详见
[T6-V1.md](T6-V1.md)。它是当前最具体的 Type-I 残余之一，但尚未证明所有实际可达状态都会
归入此分支。

### 4.3 c=8 residual 只在实际可达且未被抢占时处理

c=8 / \(q_\star=103\) 的四次整除门可作为必要条件记录，但不能单独作为 T6 exit。只有在
actual provenance、terminal-first 和 target receipt 都保留后，才应继续尝试导出 terminal 或
带 T5 ticket 的 successor。

## 5. 本轮复核后的技术状态

| 技术项 | 结论 | 证据等级 |
|---|---|---|
| \(q=1\) G full-carrier handoff | 已建立，范围不扩张 | `established`, `independent_review` |
| ordinary positive-\(q\) G universal handoff | 未建立；是 adapter 假设 | `open` |
| \(c=h\) 奇距离 translated-square fan | 在 actual proper-root terminal-first 假设下得到一个条件性 no-go 推导 | 待写成独立 claim / verifier；当前为 `analysis_evidence` |
| Eisenstein quotient \(k\) 的 EQ1--EQ7 | 由已知 stutter 恒等式可推的代数包 | `analysis_evidence`；不构成 edge |
| canonical low chart from \(k>1\) | 图表存在 | 缺 E1--E4/provenance，不构成 edge |

`T6-V1.md` 的原始公式分隔符已修复，并把上述证据等级明确写入。该文件中的
\(p=20\,065\,847\,377\) 数值候选的素数性与 \(p\equiv1\pmod{24}\) 已复算；但其
\((a,k,m)\) 到完整 stutter 参数的映射没有可重放来源，故不作为当前 T6 证据使用。

## 6. 下一批可判真假的问题

1. 为 positive-\(q\) ordinary G 写出一个完整 source guard；若失败，给出最小的
   source/mark obstruction，而非只记录“没有 handoff”。
2. 将 high-support dispatch 表限制在已知实际 state class，逐行产出 terminal、完整 E1--E5
   receipt 或唯一的 `MINIMAL_SELECTOR_GAP`。
3. 将 \(c=h\) fan no-go 写成独立、可重放的条件性 claim；其结论只能排除现有 named fan，
   不能排除一切 even-source lift。
4. 在 actual receipt 约束下分类 \(k=1\)；对 \(k>1\)，证明某个 \(q\mid k\) 的
   provenance/physicalization，或构造一个合法 reset/terminal。仅构造 \((p,R_k,K_k)\) 不够。

## 7. 参考入口

- [T2/T5 合并复核](T2-T5-full-integration-review-2026-08-17.md)
- [旗舰证明纲领](../concepts/flagship-proof-program-2026-08-16.md)
- [状态合同](../concepts/denominator-escape-state-contract.md)
- [T5 全局良基合同](../concepts/t5-global-well-foundedness-contract-v2.md)
- [q=1 G full-carrier phase-root claim](../claims/type-II-q-one-full-carrier-phase-root-entry.md)
- [proper-root stutter 的 Eisenstein 支撑](../claims/type-I-root-capacity-stutter-eisenstein-support.md)
