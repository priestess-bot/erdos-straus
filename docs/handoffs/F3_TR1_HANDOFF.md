# Agent 6 handoff：F3 R4/R6 h-supported / TR1

## 基线与提交

- 基线：`9215f8c92c53c0eb1081849b0a03e5cb922facad`
- 分支：`sol/f3-h-supported-tr1`
- 首批 scope freeze：`f5a790298ab6235728082cfc9fe20939bad9329c`
- menu/factor partition：`6b697b3842c4696488c529e823a174814759427b`
- Agent 5 QC1 cross-audit：`933e3450097f21c8bd13bc00fe50e38d07d56726`
- Agent 5 反审后的 occurrence/protocol 修正：以当前 HEAD 为准

## 精确量词

只处理 actual persistent、terminal-first 后仍非终止的 low proper-height states：

\[
2\le h=3u<p,
\qquad k>1,
\qquad k_\perp=1,
\qquad D_*>1,
\]

以及两个 route：

```text
R4_M3_NONQ5_H_SUPPORTED: m=3, 5 does not divide D_star
R6_MGT3_H_SUPPORTED:    m>3
```

不处理 high endpoint、quotient-only R3/R5、(k=1) 或 (m=3,5\mid D_*)。

## 已证明

1. **R4 h-menu eligibility。** 写 (k=3\kappa)。已有定理给
   (kappa\equiv7\pmod {24})、(kappa\ge31)，故存在规范最小
   (q_h\equiv7\pmod {12})。`k_perp=1` 强制 (q_h\mid u)。这证明它属于
   actual root receipt 所确定的 composite root-capacity menu 输入域；不是 quotient-only，
   也不是 raw occurrence/E1。
2. **R6 h-menu eligibility。** 若 (m\equiv1\pmod3)，取 (k) 的最小素因子；
   若 (m\equiv0\pmod3,k>3)，符号证明 (v_3(k)=1)，取 (k/3) 的最小素因子。
   两者都整除 (u)。(k=3) 是唯一没有非 3 h-menu factor 的 R6 子叶。
3. **(D_*) factor existence。** 对全部 R4/R6，既有 actual theorem 给 (D_*>1) 且
   ((D_*,h)=1)。因此 least prime of (D_*) 与 whole (D_*) 是 source-bound
   arithmetic factors；“没有 (D_*) factor”子域为空。
4. **完整 terminal enumeration。** h-supported terminal 不只检查 (q_h)：必须按递增顺序
   枚举全部 (1<Q\mid u) 的 composite external menus。(D_*) 侧随后按已声明 whole/native/
   quadratic/overlap/reflection menus 的固定顺序运行。
5. **固定残余。** 上述 terminal 全 miss 后，缺口统一为：source-bound (D_*) factor
   尚未绑定成 integer raw occurrence，故没有 E1、target、E4、E5 或 re-entry。

## 没有证明

- (q_h\mid u) 不构成 raw occurrence 或 paid support；
- (q_T\mid D_*mid D) 不构成 consumable integer occurrence；
- 没有 active `TR1PhysicalTransitionV1`；
- 没有 deterministic admitted target 或全域 solution lift；
- (M\le B_p) 不推出 ABSORB；只有 (R_T<p)、marked-absorb typed semantics、完整
  ABSORB fields/rank 与 irreversible protocol commit 同时成立时才有 protocol drop；
- R4、R6、F3 与 T6 均未闭合。

## 最小 residual

```text
R4_H_MENU_AND_DSTAR_TERMINALS_MISS_NO_TR1_TARGET
R6_H_MENU_AND_DSTAR_TERMINALS_MISS_NO_TR1_TARGET
```

二者共同缺失的最小定理是：

> 对每个保存 actual parent/admission/path、完整 terminal miss、maximal (D) receipt 与
> (D_*) factorization 的 residual，构造一个 path-bound integer occurrence；随后要么恢复
> direct terminal，要么以确定 target、完整 E1--E5 和 common F1 re-entry 结束。

若无法构造 integer occurrence，备选合格结果必须是从 exact R4/R6 hypotheses 推出的符号
family-empty theorem；有限搜索不合格。

## D1–D10 状态

| Gate | 状态 | 证据/缺口 |
|---|---|---|
| D1 exact quantifier | PASS | scope freeze 与 claim §1 |
| D2 exhaustive partition | PARTIAL | terminal/menu/factor/residual 有序穷尽；最终 residual 非空 |
| D3 E1 | FAIL | (D_*) 只有 arithmetic factor，未绑定 integer raw occurrence |
| D4 E2 | FAIL | 没有全域 deterministic target theorem |
| D5 E3 | FAIL | 没有 target normal form、owner、digest、active admission |
| D6 E4 | FAIL | 没有 target，因而没有 universal lift |
| D7 E5 | FAIL | 没有 authoritative parent-to-final ticket；support 大小不决定 protocol |
| D8 re-entry | FAIL | 没有 admitted target |
| D9 negative controls | PASS（局部） | quotient-only、m3-q5、terminal priority、arithmetic-factor self-authorization 均 fail closed |
| D10 independent replay | PASS（局部） | Agent 5 反审修正了 occurrence/protocol 过强表述；不构成 D3–D8 证明 |

## Agent 5 QC1 交叉审查

Agent 6 独立审查 Agent 5 R3/R5，并拒绝其 closure：oriented quotient ideal 不是 integer raw
occurrence，不能直接收费为 (Aq_\perp)。其 serializer 还可仅把 nonactual composite control
的字符串改成 `ACTUAL_PERSISTENT`，便输出 `E1.complete=true`、recursive eligible 与 local
admission ACCEPT；它同时自建 producer rule、E1--E5 receipt 和 terminal MISS。这些都不是
active admission 证据。

正式报告：`docs/audits/F3_QC1_CROSS_REVIEW_BY_AGENT6.md`。机器回执：
`data/t6-wave1/f3-qc1-cross-audit-by-agent6-v1.json`。

## 文件

- `claims/type-I-t6-f3-h-supported-canonical-carrier-partition.md`
- `data/t6-wave1/f3-tr1-scope-freeze-v1.json`
- `data/t6-wave1/f3-tr1-residual-matrix-v1.json`
- `data/t6-wave1/f3-tr1-h-supported-carrier-v1.json`
- `data/t6-wave1/f3-tr1-minimal-residual-v1.json`
- `data/interface-requests/f3-tr1-target-shapes-v1.json`
- `reproductions/type_i_t6_f3_h_supported_carrier_partition.py`
- `tests/test_type_i_t6_f3_h_supported_carrier_partition.py`

## 验证命令

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 reproductions/type_i_t6_f3_h_supported_carrier_partition.py --verify

PYTHONDONTWRITEBYTECODE=1 \
python3 -m unittest tests.test_type_i_t6_f3_h_supported_carrier_partition -v

ruff check \
  reproductions/type_i_t6_f3_h_supported_carrier_partition.py \
  tests/test_type_i_t6_f3_h_supported_carrier_partition.py

python3 scripts/kb.py validate
```

最终全树测试与 `kb.py build` 只在本分支收口时运行一次；生成的 `index/` 不提交，由
coordinator 集成后重建。
