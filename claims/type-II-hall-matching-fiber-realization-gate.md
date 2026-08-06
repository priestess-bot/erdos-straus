---
kind: claim
claim_id: type-II-hall-matching-fiber-realization-gate
title: Type II Hall 匹配触发 Kneser surplus 的单纤维实现门
statement: 跨参数纤维的 Hall 完整匹配只给出不重复的资源分配，不自动给出 Type II 命中。只有当匹配后的需求存在保持来源标签的单纤维实现映射，或一个已证明的 source-switch 恒等式把它们送入同一合法纤维，且整数整除、目标残数和 B'>A 条件同时成立时，才能把匹配计入该纤维的 Kneser surplus；否则只能记录跨状态容量证书，混合积可能是伪命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-cross-state-same-modulus-pooling-counterexample
  - type-II-cross-state-fiber-capacity-surplus-certificate
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-same-modulus-source-switch-crt-criterion
topics:
  - type-II
  - Hall
  - fiber-realization
  - source-switch
  - Kneser
  - surplus
  - pseudo-hit
  - provenance
sources:
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: cross-state-matching
  - claim: type-II-cross-state-same-modulus-pooling-counterexample
    role: mixed-product-pseudo-hit
  - claim: type-II-cross-state-fiber-capacity-surplus-certificate
    role: single-fiber-surplus
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: integer-layer-to-Kneser-injection
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: finite-fiber-realization-test
visibility: public
last_checked: '2026-08-05'
---

# Type II Hall 匹配触发 Kneser surplus 的单纤维实现门

## 1. Hall 匹配的两种含义

设跨状态兼容图的请求为 \(\mathcal R\)，资源槽为 \(\mathcal C\)，并取一个完整
匹配 \(f:\mathcal R\to\mathcal C\)。匹配只说明每个 typed 请求占用了一个不同的
真实 q 进层；它不说明这些层来自同一个整数
\[
N_A=p+4s_A
\]
或同一个单位群 \(G_A=U(4D_A)\)。

因此要把匹配计入 Kneser surplus，必须附加一个**单纤维实现映射**
\[
\rho_f:\operatorname{im}(f)\longrightarrow A
\]
（或一个已经证明的 source-switch 后继状态），满足：

1. 每个槽的 q 层和来源标签在 \(A\) 中仍整除同一个 \(N_A\)，且重复 q 遵守共同
   q 账本；
2. 匹配中选出的因子乘积 \(h_f\) 是 \(N_A\) 的合法因子，保持
   \(h_f\equiv-1\pmod{4D_A}\) 的目标残数；
3. 规范 Type II 正规形的 \(B_f=(K_Ap+A_f)/h_f\) 满足 \(B_f>A_f\)，并保留
   source-switch 与标签合同。

满足这三个条件时，才称匹配是 **FIBER_REALIZED(A)**。

## 2. 实现门定理

若一个完整 Hall 匹配是 FIBER_REALIZED(A)，则该匹配给出同一纤维中的 Kneser
容量贡献；特别地，若其活跃容量满足
\[
\sum_i\kappa_{i,A}\ge |G_A/T_A|-1,
\]
则
\[
-1\in P_A
\]
并得到合法 Type II 短证书。

### 证明

单纤维实现的第 1、2 条把匹配层回译为同一个 \(N_A\) 的合法整数因子和
\(G_A\) 中的源块乘积 \(P_A\)。于是 Type II q-height—Kneser 桥的整数注入和
Kneser 终端可直接应用；容量达到 \(|G_A/T_A|-1\) 时，Kneser 强制
\(P_A=G_A\)，因而含目标 \(-1\)。第 3 条保证残数命中能回译为规范正规形，而非
只得到一个抽象群元素。证毕。

反之，若不存在 \(\rho_f\)，Hall 匹配只是在不同 \(N_{A_i}\) 间分配资源；不能从
\(\prod_i P_{A_i}\) 的混合积推出任一单纤维的 \(P_A\) 命中。把跨状态总容量直接
代入 Kneser surplus 没有逻辑依据。

## 3. \(p=97\) 的严格伪命中

取 \(p=97\)、共同模数 \(M=24\)。两条状态分别为
\[
N_1=121=11^2,\qquad N_2=169=13^2,
\]
其单状态残数积集是
\[
P_1=\{1,11\},\qquad P_2=\{1,13\}\subset U(24),
\]
且两者都不含 \(-1=23\pmod{24}\)。若把两个状态的 q 层跨状态匹配后直接相乘，
\[
11\cdot13=143\equiv23\pmod{24},
\]
看似得到目标，但 \(11\) 只整除 \(N_1\)，\(13\) 只整除 \(N_2\)，不存在把这两个
因子同时回译到单个 \(N_A\) 的 \(\rho_f\)。所以这不是 Type II 证书，而是
**MIXED_FIBER_PSEUDO_HIT**。

该例也说明“同一模数”不等于“同一参数纤维”：模数相同只能共用群坐标，不能合并
整数来源。

## 4. 对 Hall 闭包的修正

Hall 闭包中的 surplus 分支必须写成：

* **HC3-FIBER**：某个固定纤维 \(A\) 的匹配需求超过其 Kneser 缺口，且匹配经过
  FIBER_REALIZED(A)；
* 若只有跨状态完整匹配而没有实现映射，则保留
  **UNREALIZED_CROSS_STATE_MATCH**，不能标记 Type II。若这些块能嵌入共同环境且
  shared-\(q\) 已合并，先执行[跨状态完整匹配的算术实现—Fourier 三分](type-II-cross-state-full-match-realization-fourier-trichotomy.md)：
  命中目标时走同模数/降模/raw 候选，未命中时走共同群 Fourier；只有三分留下
  未承接的算术或角色障碍时，才保留该回执；
* 若候选 source-switch 映射本身因 SNF、CRT 或 \(B'>A\) 失败，则记录
  **OBSTRUCTED**，不把失败边计入容量。

这道门把“资源竞争证明”和“整数 Type II 证书”分开，防止跨纤维池化重新引入
已经排除的伪命中。

## 5. 同模数和除子格的有限实现判据

对固定 \(M=4D\)，设匹配选择的互素混合块为
\[
h_i\mid p+a_iM,\qquad h=\prod_i h_i,\qquad h\equiv-1\pmod M.
\]
由带来源 CRT 判据，存在同一纤维的 FIBER_REALIZED(A) 映射，当且仅当 CRT 类
\[
a\equiv a_i\pmod{h_i}
\]
含有 admissible \(a\mid D\)，且 \(D/a\) 平方自由、\(aM<p\)。一旦存在，取
\[
K=(h+1)/M,\qquad B=(Kp+a)/h
\]
自动有 \(B>a\)，所以实现门不再是抽象存在性，而是一个有限的平方自由除子检查。

若同模数类为空，可转查 \(D'\mid D\) 的较小模数。令 \(a_0\) 为 CRT 类的一个代表，
则存在除子格后继当且仅当存在 \(A\mid D'\) 使 \(D'/A\) 平方自由、\(4AD'<p\)，且
\[
AD'\equiv Da_0\pmod h.
\]
这给出严格较小的 source-switch 候选；若所有 \(D'<D\) 均为空，得到有限的
**CRT_NO_ADMISSIBLE_FIBER** 负证书，而不是把混合积当作 Type II。

当 \(h>D^2\) 时，\(1\le AD'\le D^2\) 的候选至多一个；因此该分支只需检查
\(r\equiv Da_0\pmod h\) 的最小剩余是否满足平方自由分解、整除和大小条件。这为
HC3-FIBER 提供了一个可直接枚举的有限门。

同一个混合因子的完整算术闭合还包括 raw 回退：同模数和严格除子格候选均为空时，
只要有限 raw 因子三元组存在就仍直接给出 Type II；三类候选全空才输出
ALL_ARITHMETIC_LIFT_EMPTY。完整三分见
[Type II Hall 混合因子的同模数—降模—raw 算术闭合三分](../claims/type-II-hall-fiber-arithmetic-closure-trichotomy.md)。

## 研究边界

本门证明了 Hall 匹配进入 Kneser surplus 所必需的单纤维回译条件，并给出
\(p=97\) 的不可省略反例。当前仍未证明所有跨状态完整匹配都存在
FIBER_REALIZED 映射；这正是 Hall 闭包条件 HC3-FIBER 的算术核心。没有该映射时，
Hall 结果只能作为资源账本或后续 source-switch/严格递降的输入。
