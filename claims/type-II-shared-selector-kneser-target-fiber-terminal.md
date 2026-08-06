---
kind: claim
claim_id: type-II-shared-selector-kneser-target-fiber-terminal
title: Type II 共享选择器的 Kneser 目标纤维容量终端
statement: 设 m=3 mod4、x=(p+m)/4 且 x=ER，其中 E 是窗口碰撞部分、R 是私有部分，H 由 4ER 的单位素因子残数生成。令 C=Pi_m(E^2)、A=Pi_m(R)、D=Pi_m(4E)，并分别保留非平凡残数 D+、A+。若 -x 属于 H 且 Kneser 下界对 C A^2 达到 |H|，则直接得到 Type II 目标命中；若 D+ A 或 D A+ 的 Kneser 下界达到 |H|，则得到非平凡共享除子命中。若这些阈值均未达到，联合失败强制三个严格容量缺口。该判据是有限目标纤维终端，不是全称选择器或递降定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
- type-II-shared-selector-finite-collision-state
- type-I-linear-multiblock-kneser-terminal-selector
topics:
- type-II
- shared-divisor
- target-fiber
- Kneser
- finite-abelian-groups
- collision-state
- capacity
- terminal-selector
- proof-program
sources:
- claim: type-II-shared-selector-finite-collision-state
  role: collision/private product decomposition
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: Kneser product-set inequality
- result: reproductions/type-ii-shared-selector-collision-p33011449-j31-results.json
  role: exact joint-failure replay
visibility: public
last_checked: '2026-08-04'
---

# Type II 共享选择器的 Kneser 目标纤维容量终端

## 设置

令 \(p\equiv1\pmod{24}\)，\(m\equiv3\pmod4\)，
\[
x=\frac{p+m}{4}=ER,
\]
其中 \(E\) 是由有限窗口碰撞素因子组成的部分，\(R\) 是私有部分。令 \(H\) 为
\(4ER\) 的单位素因子残数生成的有限阿贝尔群，并定义

\[
C=\Pi_m(E^2),\qquad A=\Pi_m(R),\qquad D=\Pi_m(4E).
\]

记 \(D^+\subseteq D\)、\(A^+\subseteq A\) 为由非平凡整数除子产生的残数集合。于是

\[
\text{Type II target}:\quad -x\in C A A, \tag{1}
\]

而共享目标的正确标记条件是

\[
\text{shared target}:\quad
1\in D^+A\ \cup\ DA^+. \tag{2}
\]

把 \(D A\) 的平凡除子 \(1\cdot1\) 单独排除是必要的；否则会把形式上的单位元误报为
非平凡共享证书。

## Kneser 终端判据

令
\[
T_2=\operatorname{Stab}_H(CAA),\qquad
T_c=\operatorname{Stab}_H(D^+A),\qquad
T_p=\operatorname{Stab}_H(DA^+).
\]

若 \(-x\in H\) 且
\[
|CT_2|+2|AT_2|-2|T_2|\ge |H|, \tag{3}
\]
则 \(CAA=H\)，从而 (1) 必成立。若
\[
|D^+T_c|+|AT_c|-|T_c|\ge |H|, \tag{4}
\]
或
\[
|DT_p|+|A^+T_p|-|T_p|\ge |H|, \tag{5}
\]
则相应的共享乘积等于 \(H\)，从而 (2) 必成立。

反之，若 \(-x\in H\) 且 Type II 与共享目标都失败，则三个严格缺口同时成立：
\[
\begin{aligned}
|CT_2|+2|AT_2|-2|T_2|&\le |H|-1,\\
|D^+T_c|+|AT_c|-|T_c|&\le |H|-1,\\
|DT_p|+|A^+T_p|-|T_p|&\le |H|-1.
\end{aligned} \tag{6}
\]

## 证明

Kneser 定理对三重积 \(CAA\) 给出
\[
|CAA|\ge |CT_2|+2|AT_2|-2|T_2|.
\]
若 (3) 成立，右端达到 \(|H|\)，故 \(CAA=H\)，目标 \(-x\in H\) 必被命中。
对二重积 \(D^+A\)、\(DA^+\) 分别应用 Kneser，得到 (4)、(5) 的充分性。
若相应目标失败，产品集是 \(H\) 的真子集，大小至多 \(|H|-1\)，于是得到 (6)。
式 (1)、(2) 与碰撞--私有分解的精确性保证这些群乘积命中都能回译成实际除子证书。
证毕。

## 联合失败实例

在已有精确状态 \(p=33\,011\,449\)、\(j=16\) 上，
\[
m=63,\qquad x=8\,252\,878=E R,\qquad
E=2\cdot19\cdot29=1102,\quad R=7489.
\]
完整单位残数生成群满足 \(|H|=36\)。逐项枚举得到：

| 目标分支 | 稳定子群阶 | Kneser 下界 | \(|H|\) 减下界 | 目标 |
|---|---:|---:|---:|---|
| \(CAA\) | \(6\) | \(30\) | \(6\) | \(-x\equiv59\) 未命中 |
| \(D^+A\) | \(2\) | \(24\) | \(12\) | \(1\) 未命中 |
| \(DA^+\) | \(1\) | \(16\) | \(20\) | \(1\) 未命中 |

这是一条真实联合失败行：三个阈值都未达到，且缺口分别为 \(6,12,20\)。因此该
判据把“Type II 失败且共享失败”从一个黑箱状态压缩为三个可度量的目标纤维容量
缺口；后续可以把这些缺口与 q 进容量、Fourier 相位或严格递降势连接。

## 边界

若 \(-x\notin H\)，Type II 分支首先是 G 型支撑外障碍，(3) 不适用；这不是
Kneser 缺口。若某个共享产品阈值达到 \(|H|\)，判据只保证存在残数命中，实际标记
除子仍需沿 \(D^+\) 或 \(A^+\) 的来源记录回译。该卡不声称三个缺口必然产生递降，
也不把有限状态的容量不足提升为全称结论。
