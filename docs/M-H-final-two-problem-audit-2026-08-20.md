# M/H 证明包复核与边界裁定（2026-08-21）

> 输入包：[`../archive/proof-packages/raw/erdos-straus-M-H-final-two-resolution-2026-08-20.zip`](../archive/proof-packages/raw/erdos-straus-M-H-final-two-resolution-2026-08-20.zip)
>
> 外层 SHA-256：`7d736aa25b6228a3ae3a6f0abbd545e0d346b69242adcab9032e6b8677cd866c`
>
> 声明基线：`49e2e25a72f69015e7bbbcb556155363b08486a0`
>
> 处置：M 为 `CONDITIONAL_ON_E3_AND_SURFACE_ADMISSION`；H 的 C=1 同协议 no-go 为
> `ESTABLISHED`；F1、F2、T6 均保持 `OPEN`。

## 1. 复核方法

ZIP 容器通过 `unzip -t`，随包 patch 能在该基线执行 `git apply --check`。包是面向完整
仓库的增量：其两个 verifier 和 test 依赖既有 `reproductions/` 模块，因此在只解压的目录
中不能独立 import；在当前完整工作树的依赖环境下，两个 verifier 与四项 unit test 均通过。
这些结果验证了给定整数回执、公式和控制代码，不能代替全称 E3 或 reachability 证明。

## 2. M：保留为条件性适配器

M 的通用算术核是正确且有用的。对带独立 source receipt 的低支撑 marked F/G chart，
\(p\)-source 给出 anchor \((1,R-1,1)\)。若 \(R-1\mid K\)，可输出 root terminal；
否则 complete-excess \(Q\)、\(M=\operatorname{lcm}(A,Q)\) 和 congruence target
\((R',K')\) 都是确定的。\(M/A\ge2\) 以及 \(A\le B_p\) 给出

\[
\left\lfloor B_p/M\right\rfloor<\left\lfloor B_p/A\right\rfloor,
\]

故 E2、root-wide E4 和 T5 `LOCAL_DROP` 有明确的局部支付；\(p=601\) 控制也重算了
source/target 的 Jacobi G 分类。

但这个构造没有为任意 \((R',K';M)\) 给出 E3 所需的 target normal form、typed owner、
serializer、terminal-first priority 或 recursive re-entry。冻结 v2 surface 也没有登记它为
edge generator。根据状态合同的 constructor admission firewall，它在这些材料齐备以前只能是
`candidate_transition`/条件性适配器，不能称为 verified successor，更不能关闭 F1 或 F2。

活动 claim 因而准确表述为：**若 target 已由独立的版本化 surface 完成 E3/admission，则
M 构造补齐其余局部算术、lift 与严格 rank payment。**

## 3. H：接纳 C=1 边界，不缩小一般缺口

对 \(A>B_p\)、\(K=A\)、\(\eta_p=0\) 的 C=1 状态，T5 local tuple 为
\((0,1,0,0)\)。每个仍在同一 `TYPEI/CHARGED` protocol 的 complete-excess endpoint
具有 \((0,c,0,0)\)，故 \(c=1\) stutter、\(c>1\) 上升；不入队中间 chart 不能改变
parent-to-final E5 的比较。total-cofactor 同样是 identity，而两张 natural determinant
dual chart 丢失旧 charged support。这构成可接纳的全称局部 no-go。

这不证明每个 high-support empty-improvement 状态都有 C=1，也不证明 C=1 family 为空或
有付费 reset。当前仍开放：

1. actual terminal-first-miss C=1 的 root terminal、outer-rank drop、lower-protocol/phase
   target 或 family-empty 证明；
2. \(C>1\) 且 improvement set 为空的 actual terminal-first-miss high-support 状态。

随包 \(p=73\) 的 \(C=2\to6\to1\) 控制只说明某个 parent-to-final 算术宏可以降到
C=1；它被 direct root terminal 抢占且未注册为递归 edge，故仍是 `analysis_evidence`。

## 4. 规范边界

```text
T6-F1-REACHABLE-STATE-EXHAUSTION = OPEN
T6-F2-NONPROPER-DISPATCH-TOTALITY = OPEN
T6-F3-PROPER-ROOT-PHYSICALIZATION = OPEN
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
ERDOS_STRAUS_CONJECTURE = OPEN_IN_THIS_REPOSITORY
```

M/H 不修改 `data/t6-proof-frontier-v2.json` 的冻结 15-edge surface。它们分别给 F2 提供
一个待 E3 接入的低支撑局部适配器和一个 C=1 high-support 排除结果；完整 frontier 仍以
[T6 证明边界](T6-proof-boundary-2026-08-20.md) 和
[证明包总览](proof-package-consolidation-2026-08-21.md) 为准。

## 5. 聚焦复现

```bash
python3 reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py --verify
python3 reproductions/type_i_high_support_c1_local_minimum_boundary.py --verify
python3 -m unittest tests.test_type_i_mh_final_two_boundary -v
```

这些是算术控制与范围回归，不是 T6 的全域 verifier。
