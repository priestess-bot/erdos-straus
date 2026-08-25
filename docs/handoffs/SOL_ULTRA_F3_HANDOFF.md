# sol-ultra F3 handoff：proper-root 路由与 policy-endpoint $p^2$ 正规形

## BASELINE

- Base commit: `c851bd213936b3bc8b3103b469292c139d229e97`
- Branch: `sol-ultra/f3-proper-root-physicalization`
- Result date: `2026-08-23`
- Result commit: 见本分支本轮提交；本文件不以自引用 SHA 代替证明证据。

## CLAIMED RESULT

- Exact result 1: 区分 factor-proper 与 strict-height proper，建立 terminal-first、QC1/TR1
  physical route 和显式 residual 的确定分区。
- Exact result 2: 对 source-bound $m=3,q=5$ p-free policy endpoint，证明
  $L_\omega=E_uE_v$ 的一般二侧 divisor-source 正规形，并在 full-capacity 分支化为单侧
  factor-pair 系统。
- Quantifier domain: 带活动 `ACTUAL_PERSISTENT` envelope 的 proper-root receipt；第二个结果
  进一步限定为已绑定 source path 与 priority misses 的 $m=3,q=5$ 子域。
- Status: domain/normal-form `ESTABLISHED`; F3 `OPEN_MINIMAL_GAPS`。

## NEW MATHEMATICAL CONTENT

对 policy 最终 primitive p-free node $u+v=R$，重新 maximal-normalize：

\[
u=E_uD_u,\qquad v=E_vD_v,
\]

\[
D_uD_v\mid K,\qquad
D_u\mid pE_vD_v+1,\qquad
D_v\mid pE_uD_u+1,
\]

并得到

\[
\boxed{L_\omega=E_uE_v}.
\]

所以正确的二阶门是 $E_uE_v=1+p^2\chi$。first child 的
$L_1=(E/\ell)F_y$ 与 $L_\omega$ 是不同 canonicalization 层；旧
`(20zz-factor-21/23)` 约束 $L_1$，不能直接移植到 $L_\omega$。

full-capacity 单侧分支写

\[
v=(1+p^2\chi)d,\quad
c=\frac{pu+1}{d},\quad
m=\frac{d+u-1}{p},\quad
w=\frac K{ud},
\]

则新证明

\[
\tau=m+p\chi d,\qquad
4uw=c+p+p^3\chi,\qquad
p+c\mid mc^2-c+1,\qquad
u^2\ge p.
\]

这些是 actual-source divisor gates，不是 terminal 或 T5 ticket。

## EVIDENCE

- Domain concept: `concepts/t6-f3-proper-root-domain-v1.md`
- Routing claim: `claims/type-I-t6-f3-proper-root-routing-with-explicit-residuals.md`
- Routing data/verifier/test: `data/t6-f3-proper-root-routing-v1.json`,
  `reproductions/type_i_t6_f3_proper_root_routing.py`,
  `tests/test_type_i_t6_f3_proper_root_routing.py`
- $p^2$ claim: `claims/type-I-t6-f3-policy-endpoint-p2-divisor-source-normal-form.md`
- $p^2$ data/verifier/test: `data/t6-f3-policy-endpoint-p2-residual-v1.json`,
  `reproductions/type_i_t6_f3_policy_endpoint_p2_gate.py`,
  `tests/test_type_i_t6_f3_policy_endpoint_p2_gate.py`
- Object-boundary note: `docs/T6-F3-policy-endpoint-p2-gate-2026-08-23.md`
- Independent F1 delta: `docs/audits/SOL_ULTRA_F1_INDEPENDENT_DELTA.md`

## ACCEPTANCE MATRIX

| Criterion | Verdict | Evidence |
|---|---|---|
| 独立 F1 delta | **PASS; integration blocked** | active-source reconstruction and earliest trace break |
| 覆盖全部 proper-root 语义 | **PASS as domain partition** | factor-proper high residual + strict-height residuals |
| routing precedence 确定 | **PASS** | terminal/QC1/TR1/residual fixed order |
| 每条 nonterminal edge 有 actual E1 | **FAIL** | 只有 source-bound $m=3,q=5$ suffix 的相对 E1 |
| E2/E3/E4 对全分支成立 | **PARTIAL** | arithmetic E2；E3 open；target admitted 后 E4 identity |
| checkpoint/second-child 确定且 nonrepeat | **PASS arithmetic-only** | deterministic word and strict selected-coordinate shrink |
| checkpoint 有 E5 | **FAIL on $p^2$ residual** | $L_\omega\equiv1\pmod {p^2}$ 时 local rank stutters |
| $p^2$ residual empty/terminal/paid | **FAIL** | source normal form established; closure remains open |
| successor 属 F1 grammar | **BLOCKED** | F1 grammar freeze not published |
| finite exploration not used as proof | **PASS** | claims use symbolic identities; controls are explicitly focused |
| conditional adapter 未登记成 edge | **PASS** | README/frontier unchanged |
| 全部要求的仓库命令 | **PASS, deduplicated** | 共享基线 1143 项全量通过；F3 增量 15 项、KB 与 pre-T6 通过 |

## NON-RESULTS

- 没有证明每个 proper-root source 都有 bound raw path。
- 没有活动 QC1/TR1 serializer。
- 没有证明 short-word two-sided residual 或 full-capacity factor-pair system 为空。
- 没有 E3 owner/re-entry，也没有 $p^2$ residual 的严格 T5 ticket。
- 没有关闭 B5、F3、F2、F4、F5、T6 或猜想。

## RESIDUALS

- Full-capacity residual: 单侧 $(p,u,d,m,c,w,\chi)$ factor-pair system，需证明
  EMPTY、TERMINAL 或最终 strict macro。
- Short-word residual: $E_u,E_v>1$、$E_uE_v=1+p^2\chi$ 的 canonical two-sided
  atomic system。
- Domain residual: factor-proper high endpoint、其它 $(m,q)$ slice、QC1/TR1 source
  physicalization。
- Next theorem: 先对单侧 factor-pair system 联立 actual $m=3$ divisor/size gates，尝试
  排空或构造 terminal；它比继续提升无来源同余更小且更接近 B5 验收式。

## INTEGRATION NOTES

- README/frontier/T6 status: 未修改。
- New active family/constructor: 无。
- Candidate targets: 必须等待 F1 grammar freeze；当前只保留 claim/data receipt。
- First-wave disposition: `F1 OPEN_MINIMAL_GAPS + F3 OPEN_MINIMAL_GAPS`。按执行计划，F2
  第二波不得启动。

## VALIDATION

```text
python3 reproductions/type_i_t6_f3_proper_root_routing.py --verify          PASS
python3 reproductions/type_i_t6_f3_policy_endpoint_p2_gate.py --verify     PASS
python3 -m unittest <two focused F3 modules> -v                            15/15 PASS
python3 -m py_compile <four modified Python files>                         PASS
ruff check <four modified Python files>                                   PASS
python3 scripts/kb.py validate                                             PASS (1395 docs)
python3 scripts/kb.py build                                                PASS
python3 reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
                                                                             PASS
git diff --check                                                           PASS after staging
```

旧测试没有在第二个 worktree 重复运行：F3 分支从同一 `c851bd2` 基线只新增互不覆盖的文件；
该基线加 F1 增量已在同一轮完整运行 `unittest discover`，1143/1143 通过。F3 的全部 Python
增量由上面的 15 项 focused tests 覆盖。这个去重不被用作数学全称证明，只避免重复历史审计。
