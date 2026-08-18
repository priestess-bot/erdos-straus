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
| T2 | 当前具名 atomic surface 闭合；full open | H4 \(a=1\) 与 c=8 double-low 两个 `v1` arm 恰好穷尽当前 taxonomy | future raw arm、pooled-capacity、输入覆盖与全域 admission |
| T3 | 抽象命题开放；当前具名图中不可达 | 当前 14 个 concrete generators 都保持 \(W=\operatorname{Sol}(p)\)，无 nontrivial-mark seed | 任意 future marked edge 的 serializer、membership 与 lift |
| T4 | ordinary \(q\ge1\) 相对闭包已建立 | actual terminal-first ordinary G 统一进入同一个 p-only fresh full-carrier root，并通过 origin-normalized 首条 local edge | nontrivial mark、首条边之后的 Type-I totality |
| T5 | 合同层闭合 | 所有 contract-recognized persistent edge 的七元势严格下降 | 任何 E1--E4 candidate 自动有 ticket，或 selector totality |
| T6 | 开放 | terminal-first 与五类输出的验收规则 | 每个实际可达 nonterminal state 的 terminal 或 verified successor |

closed-world 审计说明 full T2 与 nontrivial T3 不是**当前具名图**的 live blocker；但 future
selector 若新增 atomic arm 或 marked generator，就必须重开相应义务。其它 T1 input、c=8
outgoing existence、一般 overflow 与 high-support 分支仍没有全局归约定理，不能把 T6 缩写为
只剩 proper-root。

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

### 4.1 Ordinary G 的 positive-\(q\) adapter 已相对闭合

对每份 actual、terminal-first、ordinary positive-\(q\) G source，新增 adapter 从当前整数重算
endpoint downset 与 canonical finite-abelian G separator，重放 source state / terminal-first
摘要和 target universal \(p\)-source，并构造不含 source \(q\) 的 target serialization。因此

\[
\text{every actual ordinary positive-}q\text{ G endpoint}
\longrightarrow
\text{fresh full-carrier Type-I root}.
\]

已在相对 source hypothesis 下建立。E4 是 \(\operatorname{Sol}(p)\) 上的恒等 lift，E5 使用
canonical T5 major phase \(3\to2\)。focused controls 不制造 actual source receipt，所以仍标为
conditional adapter controls；actual root 的两种注册 origin 已由同一个 semantic projection
接入首条 Type-I local edge，并以 `LOCAL_DROP` 支付。

### 4.2 High-support / proper-root stutter 是优先残余，而非全局压缩定理

对已进入 Type-I `CHARGED` 的状态，\(A>B_p=(p-1)^2/4\) 时
\(\lfloor B_p/A\rfloor=0\)。此时必须通过 \(K/A\) 的真实下降、phase drop、outer-rank
source 或 terminal 处理；不能只凭内部 checkpoint 支付 E5。

proper-root stutter 提供了较强的算术结构：正定 Eisenstein 范数、小商和约化除子；详见
[T6-V1.md](T6-V1.md)。它是当前最具体的 Type-I 残余之一，但尚未证明所有实际可达状态都会
归入此分支。

该子域已有两项全称收缩：\(c=h\) 的 named odd-distance fan 已严格排空；Eisenstein quotient
的 \(k=1\) actual 子域也由 cyclotomic common-divisor 排除与 Vieta 无限下降严格排空。另有
\(\gcd(a,e-1)\mid\gcd(h,k)\) 的公共因子对齐：共享 Eisenstein 因子必是 \(h\)-supported，
而 \(q\mid k,\ q\nmid h\) 的 quotient-only 因子不能被误投到旧 root-capacity source menu。
这只是 provenance 收缩，不保证菜单命中或 physical edge。真正剩余的是 \(k>1\) quotient
carrier 的 physicalization（QC1），或 transverse \(D_*\) carrier 的全称 E1--E5 出口（TR1）。
其中 \(k=3\) 现在还有一个严格的 primitive fiber 约化：写
\(A=a/3,B=(e-1)/3\) 后，每个 fixed-\(d\) 候选都必须满足
\(A\mid3d^2+d-1\)。最小 \(d=1\) fiber 唯一恢复为 \(p=939\)，与已有
\((m,a)=(6,3)\) small-root 排除行一致；但 \(d\) 没有全局上界，不能把该局部收缩误写成 QC1。见
[\(k=3\) primitive fiber reduction](../claims/type-I-root-capacity-stutter-k-three-primitive-fiber-reduction.md)。

### 4.3 c=8 residual 只在实际可达且未被抢占时处理

c=8 / \(q_\star=103\) 的四次整除门可作为必要条件记录，但不能单独作为 T6 exit。只有在
actual provenance、terminal-first 和 target receipt 都保留后，才应继续尝试导出 terminal 或
带 T5 ticket 的 successor。

## 5. 本轮复核后的技术状态

| 技术项 | 结论 | 证据等级 |
|---|---|---|
| \(q=1\) G full-carrier handoff | 已建立，范围不扩张 | `established`, `independent_review` |
| ordinary positive-\(q\) G universal handoff | 对 actual terminal-first ordinary source 相对闭合 | `established`, `internal_review` |
| \(c=h\) 奇距离 translated-square fan | named family 在 actual proper-root scope 内全称 no-go | `established`, `internal_review` |
| proper-root \(k=1\) quotient | actual 子域全称为空；无有限扫描 | `established`, `internal_review` |
| proper-root \(\gcd(a,e-1)\) 对齐 | 公共因子只可落在 \(\gcd(h,k)\)；拆开 h-supported 与 quotient-only residual | `established`, `internal_review`；不构成 edge |
| proper-root \(k=3\) fixed-\(d\) fiber | primitive Pell-type 约化；\(d=1\) 重现已排除的 \((m,a)=(6,3)\) 行 | `established`, `internal_review`；\(d\ge4\) fibers 及 QC1 仍开放 |
| Eisenstein quotient \(k\) 的 EQ1--EQ7 | 由已知 stutter 恒等式可推的代数包 | `analysis_evidence`；不构成 edge |
| canonical low chart from \(k>1\) | 图表存在 | 缺 E1--E4/provenance，不构成 edge |

`T6-V1.md` 的原始公式分隔符已修复，并把上述证据等级明确写入。原
\(p=20\,065\,847\,377\) 数值线索已被精确反解：它不满足 actual root divisibility，且有
gap-3 Type II terminal，被 terminal-first 抢占，故已从 proper-root evidence 中删除。

## 6. 下一批可判真假的问题

1. 从 positive-\(q\) 已接入的首条 local edge 继续证明后续 Type-I totality。
2. 将 high-support dispatch 表限制在已知实际 state class，逐行产出 terminal、完整 E1--E5
   receipt 或唯一的 `MINIMAL_SELECTOR_GAP`。
3. 对 \(k>1\)，证明某个 \(q\mid k\) 的 provenance/physicalization，或从 \(D_*\) 构造
   合法 terminal / E1--E5 successor；仅构造 \((p,R_k,K_k)\) 不够。
4. 对每个 actual c=8 parent，证明 high-\(q\) double-low label 或其它 verified outgoing edge
   存在；有限 controls 中没有 dead end 不能替代该量词。

## 7. 参考入口

- [T6 证明工作包复核与合并记录](T6-proof-workfiles-package-audit-2026-08-18.md)
- [T6 全闭合尝试审计](T6-closure-attempt-audit-2026-08-17.md)
- [T2/T5 合并复核](T2-T5-full-integration-review-2026-08-17.md)
- [旗舰证明纲领](../concepts/flagship-proof-program-2026-08-16.md)
- [状态合同](../concepts/denominator-escape-state-contract.md)
- [T5 全局良基合同](../concepts/t5-global-well-foundedness-contract-v2.md)
- [q=1 G full-carrier phase-root claim](../claims/type-II-q-one-full-carrier-phase-root-entry.md)
- [positive-q G full-carrier phase-root claim](../claims/type-II-positive-q-G-full-carrier-phase-root-entry.md)
- [当前 named graph 的 T2/T3 coverage audit](T6-actual-reachable-coverage-audit-2026-08-17.md)
- [proper-root 最小缺口审计](T6-proper-root-minimal-gap-audit-2026-08-17.md)
- [proper-root k=1 全称排除](../claims/type-I-root-capacity-stutter-k-one-universal-exclusion.md)
- [proper-root \(k=3\) primitive fiber reduction](../claims/type-I-root-capacity-stutter-k-three-primitive-fiber-reduction.md)
- [proper-root 公共因子对齐](../claims/type-I-root-capacity-stutter-common-divisor-alignment.md)
- [proper-root stutter 的 Eisenstein 支撑](../claims/type-I-root-capacity-stutter-eisenstein-support.md)
