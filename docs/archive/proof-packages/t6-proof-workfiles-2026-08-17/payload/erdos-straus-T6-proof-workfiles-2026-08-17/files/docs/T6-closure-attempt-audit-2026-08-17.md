# T6 全闭合尝试审计（2026-08-17）

> 结论：`T6_GLOBAL_SELECTOR_TOTALITY = OPEN`。
>
> 本轮建立了四个全称或 closed-world 子结果，并删除一条伪数值线索；它们仍不足以证明
> 每个 actual reachable nonterminal state 都有 terminal 或 verified successor。

## 1. 闭合标准

T6 要求一个不读取未知解的确定性 selector。对每个核心素数
\(p\equiv1\pmod {24}\) 和每个实际可达 legal state \(S\)，它必须给出

\[
\operatorname{terminal}(S)
\quad\lor\quad
\exists T\;\bigl(E1(S,T)\land E2(T)\land E3(T)
\land E4(T\to S)\land\Pi_{T5}(T)<\Pi_{T5}(S)\bigr).
\tag{T6}
\]

T5 已证明右支中**一旦**边被合同接纳就严格下降；它没有证明右支存在。因此不能用
“verified edge 的定义包含 rank drop”、有限测试全过或有限范围内没有 dead end 来替代
\((T6)\) 的全称存在量词。

## 2. 本轮真正建立的结果

| 子问题 | 结果 | 精确边界 |
|---|---|---|
| ordinary positive-\(q\) G handoff | 对任意 actual terminal-first ordinary source，相对 adapter 确定进入同一个 \(p\)-only full-carrier root；两种注册 origin 再由同一规则重放首条 local edge | focused controls 不制造 actual source receipt；nontrivial mark 与首条边之后的 Type-I totality 不在结论内 |
| 当前 T2/T3 live surface | 当前 14 个 concrete named generators 都保持 \(W=\operatorname{Sol}(p)\)；两个 atomic families 恰等于 T2-v1 arms | 只对 frozen named graph；future marked/atomic generator 会重开审计 |
| proper-root \(c=h\) fan | existing odd-distance translated-square family 全称为空 | 只排除该 named family，不产生 terminal 或 edge |
| proper-root \(k=1\) | actual 子域全称为空 | cyclotomic gcd 排除加 Vieta 无限下降；不使用范围扫描，不处理 \(k>1\) |
| T6-V1 数值线索 | \(p=20\,065\,847\,377\) 的唯一反解不满足 root divisibility，且被 gap-3 terminal 抢占 | 只删除该线索，不是 general no-go |

对应证据：

- [positive-q G relative adapter](../claims/type-II-positive-q-G-full-carrier-phase-root-entry.md)
- [current named reachability coverage](T6-actual-reachable-coverage-audit-2026-08-17.md)
- [proper-root (c=h) named-fan no-go](../claims/type-I-root-capacity-stutter-c-equals-h-odd-distance-fan-no-go.md)
- [proper-root (k=1) universal exclusion](../claims/type-I-root-capacity-stutter-k-one-universal-exclusion.md)
- [proper-root numeric-clue preemption](../claims/type-I-root-capacity-stutter-t6-numeric-clue-preemption.md)

## 3. 仍未闭合的最小量词

### 3.1 没有全局 reachable-state exhaustion

当前 taxonomy 是“已构造边族”的 closed world，不是对每个 actual state 的 exhaustive case
split。一般 \(A>1\) overflow、high-support 和其它 T1 后续状态尚无定理证明必进入某个已覆盖
guard。因此即使下面两个局部分支被解决，仍须给出全局 state-family exhaustion。

### 3.2 Proper-root (k>1) physicalization

令 \(\mathcal S_{\rm pr}\) 为 actual、terminal-first 后仍非终端的 proper-root stutter
states。本轮证明 \(k(S)\ne1\)，但仍缺

\[
\forall S\in\mathcal S_{\rm pr},\ k(S)>1
\Longrightarrow
\left[
\operatorname{terminal}(S)
\ \lor\
\exists q\mid k(S)\ \exists T\;
\operatorname{PhysicalE1toE5}(S,q,T)
\right].
\tag{QC1}
\]

形式 low chart \(k\mid K_k\) 不满足这里的 `PhysicalE1toE5`：它没有把 quotient factor
连接到 actual source occurrence，也没有保留或合法重置旧 charged support。

transverse 路线同样缺

\[
\forall S\in\mathcal S_{\rm pr},\quad
\operatorname{terminal}(S)
\ \lor\
\exists q\mid D_*(S)\ \exists T\;
\operatorname{PhysicalE1toE5}(S,q,T).
\tag{TR1}
\]

这里 \(D_*\) 有 actual receipt occurrence，却没有现有 root menu 所需的 \(q\mid u\)
provenance。固定有限 same-\(q\) gap 菜单又受已有 Dirichlet--CRT no-go 限制。

### 3.3 c=8 outgoing existence

对 terminal-first-surviving c=8 parent \(P\)，现有 theorem 只在 actual double-low receipt 已经
出现时给 strict macro。仍需证明

\[
\operatorname{terminal}(P)
\ \lor\
\exists q\in\mathcal Q_V(P):
q>2(p-1),\ 1\le c_a(q),c_\Sigma(q)\le7
\ \lor\
\exists T\;\operatorname{verified\_edge}_{\rm other}(P,T).
\tag{C8}
\]

仓库没有 actual persistent c=8 dead-end fixture；已冻结的 \(p=157393\) 与最小 residual
\(p=241441\) controls 都被 terminal 菜单抢占。这是有用的有限证据，但不能证明 \((C8)\)。

## 4. 为什么本轮不能把状态改成 closed

若把 T6 标为 closed，T5 的良基性会把 selector 路径强制终止，并与 terminal lift 一起推出
旗舰 F0，进而覆盖 Erdős--Straus 的核心素数类。当前没有 \((QC1)\)、\((TR1)\)、\((C8)\)
或全局 reachable-state exhaustion 的证明；把条件性 constructor、形式 chart 或有限 scan
当成这些量词中的 witness 会违反仓库自己的 E1--E5 合同。

因此本轮唯一可审计的状态更新是：

```text
POSITIVE_Q_ORDINARY_G_RELATIVE_HANDOFF = ESTABLISHED
Q_ONE_POSITIVE_Q_FIRST_LOCAL_ORIGIN_NORMALIZATION = ESTABLISHED
T2_CURRENT_NAMED_ATOMIC_SURFACE = CLOSED
T3_NONTRIVIAL_MARK_IN_CURRENT_NAMED_REACHABILITY = UNREACHABLE
PROPER_ROOT_C_EQUALS_H_NAMED_FAN = EMPTY
PROPER_ROOT_K_ONE_ACTUAL_DOMAIN = EMPTY
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
```

## 5. 重放命令

```bash
python3 reproductions/type_ii_positive_q_g_full_carrier_phase_root_entry.py --verify
python3 reproductions/type_i_t6_actual_reachable_coverage_audit.py --verify
python3 reproductions/type_i_root_capacity_stutter_c_equals_h_odd_distance_fan_no_go.py --verify
python3 reproductions/type_i_root_capacity_stutter_k_one_universal_exclusion.py --verify
python3 reproductions/type_i_root_capacity_stutter_t6_numeric_clue_preemption.py --verify
python3 reproductions/type_i_t5_transition_surface_audit.py
python3 scripts/kb.py validate
python3 scripts/kb.py build
```

这些 focused verifiers 检查精确整数/多项式恒等、合同字段和 frozen controls；全称证明仍由
对应 claim 正文承担。任何 verifier 输出都不把 finite controls 升级为 T6 totality。
