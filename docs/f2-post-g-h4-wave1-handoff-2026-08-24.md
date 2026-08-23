# F2 post-G / C2 / H4 wave-1 handoff

基线：`9215f8c92c53c0eb1081849b0a03e5cb922facad`  
分支：`sol/f2-post-g-h4-totality`  
状态：`OPEN_MINIMAL_RESIDUAL_EXTERNAL_INTERFACES`

## 1. 本轨道完成的数学收缩

### 1.1 ordinary G producer surface

在冻结 selected graph 中，initializer 没有 Type-II F seed，唯一 G seed 是 q=1。两类
relation F/G producer 都要求先验 F source；Type-I 又不能非终端返回 Type-II。因此
positive-q G 没有 frozen source。q=1 full-carrier handoff 无附加条件地覆盖唯一 G seed，
c=3 lineage relay 的定义域是其子集；固定 full-carrier-first precedence 后，c=3 是
nonrecursive alternate。

这是 frozen-graph induction，不是 F1 semantic constructor exhaustion。coordinator 在 grammar
freeze 必须确认没有未登记 Type-II seed；若发现 positive-q G source，则已有相对 theorem
仍对每个 actual source 给出同一个 p-only handoff，但必须把 serializer 接入 common admission。

### 1.2 post-G low Type-I continuation

对任意 actual low chart，universal p-source 到 `(1,R-1,1)`；`R-1|K` 时直接 terminal，
否则唯一 maximal complete-excess block 使 support 至少翻倍。low chart 强制
`A<=K<=B_p`，所以该规则有限次后 terminal 或进入 existing A>1 overflow family。没有使用
有限 prime scan 证明全称结论。

### 1.3 C2 phase 与 macro fusion

q=1 immediate d=1 image 的 capacity-one exclusion 已全称证明 `C=1` 不可能；因此交给
Agent 2 的该 source image 中 every nonterminal target has `C>=2`。capacity-two rigidity
进一步强制 odd branch empty、even branch
`q*=19`, `p=912u+769`。因此不存在 C2 non-19 residual。H0--H4 不需要 standalone
serializer；它们可作为原 d=1 receiver 到 final H4 output 的 deterministic finite macro
checkpoints。E5 始终比较原 parent `(0,p-1)` 和最终 `(0,c_T)`。

### 1.4 H4 guard DAG

在 actual H3=>H4 receipt 域：

- full-overlap / nonproper predecessor 为空；
- proper nontop capacity 直接严格；
- top `a_alt>1` 由 d=1 suffix 严格离开；
- top `a_alt=1` 自动产生 `gcd(q,K4)=1` 的 clean q carrier，non-clean complement 为空；
- clean-q endpoint 的 y-block 非空、p-primary 为空、first stutter 为空，因此 terminal 或
  strict single-side/atomic target，最终 `c_T<=p-2`。

这覆盖计划要求的 proper/nonproper、top/nontop、a-coordinate、clean/non-clean 及 target
hit/F/G/atomic 的算术层分派。

### 1.5 H4 target owner

所有 nonterminal clean-q target 满足

\[
M_T>M_4>p^4/8>B_p,
\qquad
R_T=(4M_Tc_T-1)/p>p.
\]

所以它们统一是 high-support A>1 overflow；F/G 只属于 target-local certificate context，
不需要新 H4-F/H4-G persistent family。若有实际 sink receipt，使用 narrower
`type_i_high_support_sink`；否则使用 existing `type_i_a_gt_one_overflow_residual`。

## 2. 为什么本分支不能声明 closed

数学 guard 已收缩，但 D5、D8、D10 尚未通过：

1. coordinator 尚未把 final targets 投影到 common PersistentSelector admission；
2. coordinator 的 F1 grammar freeze 尚未确认 G seed inventory，或激活 positive-q serializer；
3. Agent 3 尚未提供 H4/c8 共用 AtomicPendingTarget serializer 与 atomic recursive closure；
4. Agent 2 尚未关闭本轨道产生的 A>1/high-support overflow targets；
5. Agent 3 尚未完成本轨道的独立 cross-audit。

因此 `pending_dispatch`、conditional target 或 local capacity inequality 均未被写成 active closure。

机器可读 residual 见
[`f2-post-g-h4-minimal-residual-v1.json`](../data/t6-wave1/f2-post-g-h4-minimal-residual-v1.json)。

## 3. Coordinator interface requests

- `f2-post-g-g-producer-disposition-v1.json`
- `f2-post-g-low-chart-overflow-handoff-v1.json`
- `f2-post-g-c2-fused-macro-v1.json`
- `f2-post-g-h4-overflow-owner-v1.json`
- `f2-post-g-h4-target-shapes-resolution-v1.json`

最终 proposal 不要求新 family、新 nontrivial mark 或新 atomic arm。保留 existing `H4_A1`
arm；C2 non-19 family request 已撤回；H4 F/G shape 归入 existing overflow owners。
`AtomicPendingTargetV1` 只能是同步、非持久内部 serializer，不能获得 owner 或入队；只有
normalize 后的 final overflow target 才能调用 common admission。

## 4. Focused replay

```bash
python3 reproductions/f2_post_g_g_producer_pruning.py --verify
python3 reproductions/f2_post_g_low_chart_exit.py --verify
python3 reproductions/f2_post_g_c2_fused_macro.py --verify
python3 reproductions/f2_post_g_h4_arithmetic_reduction.py --verify
python3 reproductions/f2_post_g_h4_target_owner.py --verify
python3 -m unittest \
  tests.test_f2_post_g_g_producer_pruning \
  tests.test_f2_post_g_low_chart_exit \
  tests.test_f2_post_g_c2_fused_macro \
  tests.test_f2_post_g_h4_arithmetic_reduction \
  tests.test_f2_post_g_h4_target_owner -v
```

这些 controls 只检查实现与公式没有漂移；全称结果来自各 claim 的符号证明。完整分支验收命令
只在最终提交前运行一次。

## 5. Validation result

- KB validate：1402 documents，PASS；KB build PASS，generated `index/` 未提交。
- pre-T6 full-tree audit：PASS；kernel tests：16 PASS。
- 本轨 focused tests：5 PASS；`ruff`、`py_compile`、`git diff --check`：PASS。
- constructor inventory structural audit：PASS，按预期 `closure_ready=false`；8 个 inventory tests PASS。
- 完整 suite 按计划只运行一次：1163 tests，13 errors + 1 failure。1 个 failure 是本轨 verifier
  读取 `recursive_edge_eligible` 被 fail-closed source census 识别为新 producer signal；已删除该
  读取，inventory audit 与对应 8 tests 聚焦重跑通过。13 个 errors 全部来自基线未包含的历史
  `h19-k23` 65536/131072/262144 JSON artifacts；已用 base SHA 核实这些文件原本就不存在，未伪造
  历史产物，也未再次运行完整 suite。

因此本分支的 track-specific checks 通过，但不能声称完整仓库 suite 绿色。
