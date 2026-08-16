---
kind: claim
claim_id: type-I-g-anchor-c3-p1009-universal-source-bypass-raw-receipt
title: p=1009 的 c=3 universal-source 非 p 绕行 raw receipt
statement: 对 p=1009 的 c=3 chart，canonical p-edge 后的 m=1 raw 图严格困于 N_R(1) 与 N_R(2)，但从同一个 declared universal p-source 出发可绕开 p-edge，按 349,41,1013,13,2,2 六条实际 raw 边到达 complement seed N_R(p-3)。对 ordered universal source 首坐标的后代，source-origin mark sigma=-p^(-1) 通过 raw-lineage transport 在 t=4,2,1 自动给出 -M,-2M,-13；它不是 endpoint 倒推的自由 multiplier。新的 source-lineage grammar 已接纳这类 non-p-first receipt 并将 raw digest、lineage digest 与 orientation 纳入根 identity；但 p=1009 本身不是 q=1 G endpoint，故本例仍只是 E1--E3 raw 控制，不生成 q=1 phase edge、verified descent 或递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - type-I-g-anchor-c3-root-to-r11-reset-terminal-bridge
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - c3
  - universal-source
  - raw-path
  - source-bypass
  - root-policy
  - source-lineage
  - phase-boundary
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-r-chart-support
    role: declared-high-R-universal-source
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: ordered-raw-step-semantics
  - claim: type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
    role: canonical-p-first-m-one-trap
  - concept: denominator-escape-state-contract
    role: E1-E5-and-root-boundary
visibility: public
last_checked: '2026-08-16'
---

# \(p=1009\) 的 \(c=3\) universal-source 非 \(p\) 绕行 raw receipt

## 1. 固定 chart

取

\[
h=42,\qquad p=1009,\qquad R=4359,\qquad M=1093,
\tag{1}
\]

\[
x=p-3=1006,\qquad
K=Mx=1099558=2\cdot503\cdot1093.
\tag{2}
\]

声明式 universal source 是

\[
\mathsf S=(1009,4392863,1008),
\qquad
4392863=41\cdot307\cdot349.
\tag{3}
\]

本卡始终以这个既有 source 为起点；它不是 reverse \(p\)-parent。

## 2. 六步 source-bypass word

选中坐标、标签和 ordered destination 依次为

\[
\mathsf S
\xrightarrow{349}(12587,490,3)
\xrightarrow{41}(307,4052,1)
\xrightarrow{1013}(4,4355,1)
\xrightarrow{13}(335,4024,1)
\xrightarrow2(2012,2347,1)
\xrightarrow2(1006,3353,1)=N_R(x).
\tag{4}
\]

前两步绕开 canonical \(p\)-edge，并在 \(N_R(307)\) 重新进入 \(m=1\)。
第三步接到 \(N_R(4)\)，后三步正是 \(4\to4x\to2x\to x\) 的 even tail。

相应 shift 与关键整除为

\[
\begin{array}{c|c|c|c|c}
\text{step}&q&\text{selected coordinate}&\text{shift}&\text{selected}/q\\ \hline
1&349&4392863&39&12587=41\cdot307\\
2&41&12587&38&307\\
3&1013&4052&1012&4\\
4&13&4355&12&335\\
5&2&4024&1&2012\\
6&2&2012&1&1006
\end{array}
\tag{5}
\]

逐一按既有 ordered raw-step 合同回放，六步均满足 strict capacity、unit condition，
且每次 gcd reduction 都等于 \(1\)。其中尾部二进容量为

\[
v_2(4024)=3>v_2(K)=1,
\qquad
v_2(2012)=2>v_2(K)=1.
\tag{6}
\]

在 exact \(t=4\) 节点，

\[
\gcd(4024,K)=1006=x,
\tag{7}
\]

所以它的 physical 行字段是 \((C,M,t)=(1006,1093,4)\)，而 seed 的字段是
\((1006,1093,1)\)。

## 3. 为什么 canonical \(p\)-first 路线确实失败

这与 (4) 不矛盾。若先走 \(p\)-edge 到 \(N_R(1)\)，则

\[
R-1=4358=2\cdot2179,\qquad R-2=4357\ \text{为素数}.
\tag{8}
\]

在 \(N_R(1)\) 中，标签 \(2\) 因

\[
v_2(R-1)=v_2(K)=1
\tag{9}
\]

不具严格容量；唯一实际边为 \(2179\)，并到达 \(N_R(2)\)。在 \(N_R(2)\) 中，
标签 \(2\) 同样失败，唯一实际边为 \(4357\)，并返回 \(N_R(1)\)。因此 canonical
\(p\)-edge 后的 \(m=1\) 图严格困于

\[
\{N_R(1),N_R(2)\}.
\tag{10}
\]

这正是 c=3 adaptive-divisor normal form 在该点的局部 no-go；它只排除
\(p\)-first \(m=1\) 路线，不排除 (4)。

此外，绕开 \(p\)-edge 时 source 的右坐标只含首标签 \(41,307,349\)。
每一个单独首步后的层数分别为 \(25,4,3\)，均不为 \(1\)。故若要求绕开
\(p\)-edge 后重新进入 \(m=1\)，至少需要两条 non-\(p\) raw 边；(4) 的
\(349,41\) 恰达到该下界。这个最小性不声称是到 seed 的全局最短 word。

## 4. source-lineage phase 的可验证来源

先给出不读取 endpoint 的一般传输式。对 ordered universal source 的首坐标 \(p\)，令
\(z_i\) 是第 \(i\) 步后该坐标的确定后代；第 \(i\) 步的标签、实际 gcd reduction
分别记为 \(q_i,g_i\)。raw transition 的坐标同余给出

\[
q_i g_i z_i\equiv z_{i-1}\pmod R.
\tag{11}
\]

每个 \(q_i\) 是 unit，且 \(z_0=p\) 是 unit。由 (11) 归纳，右侧是 unit；
在交换环 \(\mathbb Z/R\mathbb Z\) 中，一个乘积为 unit 蕴含每个因子为 unit，
故 \(g_i,z_i\) 也都是 unit。令

\[
\sigma=-p^{-1}\pmod R,
\qquad
E_i=\prod_{j\le i}q_jg_j,
\qquad
\Theta_i=\sigma E_i.
\tag{12}
\]

则归纳地有

\[
E_i z_i\equiv p,
\qquad
\Theta_i z_i\equiv-1\pmod R.
\tag{13}
\]

\(\sigma\) 是唯一将 declared source 的有序首坐标归一到 \(-1\) 的 mark：
\(\sigma p=-1\)。因此 (13) 完全由 source、ordered raw transcript 与每步实际
gcd reduction 决定，不能由目标 endpoint 后置制造。

在 (4) 中所有 \(g_i=1\)，p-line 和 raw 积依次为

\[
\begin{array}{c|cccccc}
i&1&2&3&4&5&6\\ \hline
z_i&490&4052&4&4024=4x&2012=2x&1006=x\\
E_i&349&1232&1342&10&20&40\\
\Theta_i&2393&2215&3269&3266&2173&4346
\end{array}
\pmod{4359}.
\tag{14}
\]

特别地 \(\sigma=2942\)，并且

\[
\sigma=(-M)10^{-1}\equiv-p^{-1}\pmod R.
\tag{15}
\]

证明顺序应是先由 source 定义 \(\sigma\)，再由 (13) 验证尾门，而不能将 (15) 当作
endpoint-derived 定义。因为 \(4Mx\equiv1\pmod R\)，(13) 在 \(z_i=4x,2x,x\)
时精确给出

\[
\Theta_{t=4}=-M=3266,\qquad
\Theta_{t=2}=-2M=2173,\qquad
\Theta_{t=1}=-13=4346\pmod{4359}.
\tag{16}
\]

orientation 是必要字段：若 p-line 落在 \(R-tx\) 的另一侧，上式符号会反转。
本绕行在三个尾点都落在 \(+4x,+2x,+x\) 侧；canonical p-first word 的 p-line
方向不同，且其 \(W\) 是 p-edge 后的 anchor-relative 相位。因此 (16) 不能被错误
当作对旧 \(W\) 合同的全局替代。

现有 p-first root adapter 硬编码首条 \(q=p\) edge、canonical anchor 和随后
anchor-relative phase；它没有 source-lineage 或 \(g_i\)-transport 字段，故 (4)
仍不能被它接纳。

## 5. 后续接口

(4) 已建立 E1 raw-source receipt 与 source-lineage transport evidence。现在
[q=1 G c=3 source-lineage phase relay](type-II-q-one-c3-source-lineage-phase-root-entry.md)
已实现通用 grammar：它检查 ordered universal source、source-first-coordinate lineage 与
全部 \(q_i,g_i\)，验证三个尾点的 orientation gate，并把 raw digest、lineage digest、
orientation、fresh scope 与 terminal-first 绑定到 c=3 根及后续 \(d=3\) RESET。

这不改变本控制的状态。这里的 \(p=1009\) 有

\[
\frac{p+3}{4}=253=11\cdot23,
\qquad 11\equiv2\pmod3,
\tag{17}
\]

所以它不是 ordinary `q=1 G` endpoint，不能进入该 phase relay。它继续只验证 non-p-first
source provenance 与 (16) 的正 orientation，不创建 selector edge 或递归状态。

复现：

    python3 reproductions/type_i_c3_p1009_universal_source_bypass.py --verify
