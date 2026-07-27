---
kind: claim
claim_id: type-II-h19-external-scale-k10-renewal
title: H19 外部源尺度 k=10 的模五覆盖重启
statement: 在 H19 安全分支 p=6Q19*t+8328961 中，完整外部源尺度 K0={1,2,3,4,5,6,8,9,12,15} 与 H19 一私有余因子模型给出可采纳线性型族。加入 k=10 后，该族恰被素数 5 局部覆盖；但对全部 t=5u+c (c mod5)，重新提取强制因子后，H19 加 K0 并 k=10 的 31 条线性型在每个分支均再次可采纳。更强地，这五个分支对所有参数均共同可用的尺度恰为 360 的 24 个约数；把它们全部加入后，每个分支的 44 条线性型仍可采纳，且每个来源的完整平方因子递降目标仍不在全部除子残数集中。故固定参数下的 k=10 覆盖及共同静态尺度全加均不构成状态闭合；在 Dickson/Schinzel 假设下，五个分支各自给出条件性共同逃逸族。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- adaptive-family
- admissibility
- conditional-boundary
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 外部源尺度 k=10 的模五覆盖重启

## 状态

令

\[
Q=Q_{19}=77\,597\,520,\qquad r=8\,328\,961,\qquad
p=6Qt+r. \tag{1}
\]

这里把此前 \(p=3Qm+r\) 的分支细分为 \(m=2t\)，以使 \(k=8\) 在整个进程中都满足
\(k\mid(p-1)/4\)。先取

\[
K_0=\{1,2,3,4,5,6,8,9,12,15\}. \tag{2}
\]

对每个 \(k\in K_0\)，将

\[
n_k=\frac{(4k-1)p+1}{4k}=D_kL_k(t)
\]

的固定因子 \(D_k\) 逐项提出，并对

\[
M_k=kD_kL_k(t),\qquad q_k=4k-1
\]

枚举 \(M_k^2\) 的全部除子模 \(q_k\) 残数。每个目标
\(-M_k\bmod q_k\) 都不在相应残数集内。H19 的 \(p\) 及 19 条余商与这十条
\(L_k\) 合成 30 条原始线性型，并且没有覆盖素数。

## k=10 的局部覆盖

加入 \(k=10\) 后，外部源仍完整失败，但 31 条线性型的覆盖素数恰为

\[
\{5\}. \tag{3}
\]

这只说明以 \(t\) 为未细分参数时，每个模 5 残数都会使至少一条显示的线性型被 5
整除。它不是某一条 Type I/II 证书，也不是递降成功。

对 (3) 的正确状态更新是

\[
t=5u+c,\qquad c=0,1,2,3,4. \tag{4}
\]

对每个 \(c\)，重新计算全部 H19 射线和全部 \(k\in K_0\cup\{10\}\) 的强制因子。
结果为：

| 分支 \(c\) | 线性型数 | 覆盖素数 |
|---:|---:|---|
| 0 | 31 | 无 |
| 1 | 31 | 无 |
| 2 | 31 | 无 |
| 3 | 31 | 无 |
| 4 | 31 | 无 |

并且在每一个分支、每一个列出的尺度上，完整平方因子递降目标仍缺失于**全部**
\(M_k^2\) 除子残数集。

## 共同静态尺度的全加

对每个分支 (4)，一个尺度 \(k\) 在该仿射进程的**每个**参数值上都可用于外部源，
当且仅当

\[
4k\mid\gcd(P,C-1),\qquad p=Pu+C. \tag{5}
\]

对五个分支把 (5) 的右边再取公因子，得到

\[
\gcd_{c=0}^{4}\gcd\left(\frac{P_c}{4},\frac{C_c-1}{4}\right)=360. \tag{6}
\]

故所有五个分支共同、全程可用的尺度不是任意选出的子集，而是

\[
\{k:k\mid360\},
\]

共 24 个。将这 24 个尺度全部加入，每个分支均有 H19 的 20 条和来源的 24 条，
合计 44 条原始线性型；有限域检查仍给出无覆盖素数，且每一个来源的完整平方因子
递降目标仍不在其完整除子残数集中。

这不涉及那些只在进一步细分某一个分支后才变为可用的尺度。恰恰因此，它隔离了
“固定地加入当前所有可用尺度”与真正自适应尺度选择之间的差别。

## 条件性含义与边界

故在 Dickson 素数元组猜想或相应 Schinzel 假设下，每个分支 (4) 都条件性地产生无穷
多个核心素数，使 H19 的一私有余因子扇及所列 11 条完整外部源递降同时失败。

这不是 Erdős--Straus 猜想的条件性反例，也不排除其它 \(k\)、其它 Type I/II
证书或其它递降。它证明的是一个方法论边界：局部覆盖素数可能在细分后转化为新的固定
因子，而不是减少可采纳状态。因此“加入一个尺度出现覆盖”不能作为自适应递归终止的
势能；后续桥接引理必须记录覆盖素数是否已被吸收及其来源。

运行

```bash
python3 reproductions/type_ii_h19_external_scale_renewal.py
python3 -m unittest tests/test_type_ii_h19_external_scale_renewal.py -q
```

可重建覆盖根、五个细分状态、全部强制因子和除子残数检查。
