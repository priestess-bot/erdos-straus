---
kind: claim
claim_id: type-I-high-anchor-same-chart-gate-engineering-boundary
title: 高锚同图表单调支撑提升的余因子 gate 工程边界
statement: 设 H=(p,R,K;A) 是 overflow canonical 高锚，满足 p≡1 (mod 24)、p<R<4A、A|K、A≤B_p=(p-1)^2/4，且 K/A<p。所有同时保留旧 charged-support 整除链 A|L、能由 H 的同一图表重新分解、并由 Pi_p=floor(B_p/.) 严格付款的真支撑提升恰为 L 属于 {L:A|L|K, A<L≤B_p}；它们保持 canonical_chart(p,L)=(R,K)。对每个 L，令 Q 为 R-1 相对 K 的 full-excess bundle，M_L=lcm(L,Q)，C_L=K_{M_L}/M_L，r_L=M_L mod p。其随后 high-R full-excess cofactor gate 精确为 L/gcd(L,C_L)|r_L。对冻结 verified-parent atlas 的 51 个 occurrence、31 个不同高锚，此有限域共有 49 次候选提升，gate 命中为零；故在该冻结域内，已付款的同图表单调支撑提升不能把一个原本失败的 high-R cofactor gate 工程为成功。独立控制 p=1201 有一次提升后命中，但未提升 gate 已成功；p=3793 与 p=60913 没有允许的真提升。该命题只给出算术与 Pi_p 付款，不补齐 parent 链、typed F/G、terminal-first 或全局 selector E1--E4；非整除的 paid support reset 不在本卡枚举域内。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-overflow-same-chart-support-promotion
  - type-I-high-anchor-frozen-parent-atlas-gate-boundary
  - type-I-high-anchor-cofactor-outer-rank-composition
topics:
  - type-I
  - high-anchor
  - same-chart
  - support-promotion
  - cofactor-gate
  - finite-atlas
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_same_chart_gate_engineering.py
    role: exact divisor lattice and targeted frozen-atlas replay
  - result: reproductions/type-i-high-anchor-same-chart-gate-engineering-results.json
    role: 51-occurrence finite gate atlas and three controls
  - result: reproductions/type-i-high-anchor-parent-atlas-results.json
    role: frozen verified-parent high anchors
visibility: public
last_checked: '2026-08-06'
---

# 高锚同图表单调支撑提升的余因子 gate 工程边界

## 1. 问题与结论

固定一个 overflow canonical 高锚

\[
H=(p,R,K;A),\qquad p<R<4A,\qquad A\mid K,
\]

并令

\[
B_p=\frac{(p-1)^2}{4},\qquad \Pi_p(D)=\left\lfloor\frac{B_p}{D}\right\rfloor.
\]

这里考察的不是任意改变 metadata 的假想操作，而是可从固定图表的行列式重新分解、保持
旧 charged support 的整除链 \(A\mid L\)，并按既有 same-chart 定理由 \(\Pi_p\) 严格
付款的支撑提升。它们恰是

\[
\mathcal L_H=
\{L: A\mid L\mid K,\ A<L\le B_p\}.
\tag{1}
\]

对于每个 \(L\in\mathcal L_H\)，令 \(Q\) 是 \(R-1\) 相对 \(K\) 的 deterministic
full-excess bundle，随后定义

\[
M_L=\operatorname{lcm}(L,Q),\qquad
C_L=\frac{K_{M_L}}{M_L},\qquad
r_L=M_L\bmod p.
\tag{2}
\]

则提升后的 high-R full-excess cofactor gate 是精确而非启发式的条件

\[
\frac{L}{\gcd(L,C_L)}\mid r_L.
\tag{3}
\]

在冻结 parent atlas 的 31 个不同高锚上，(1) 一共给出 49 次可付款候选，(3) 无一成立。
所以在这个已验证父边的有限域中，同图表支撑提升不能把一个失败的 gate “工程”为成功。

## 2. 为什么 (1) 是单调提升的精确域

首先，\(L\mid K\) 与

\[
pR+1=4K,\qquad R<4A<4L
\]

给出

\[
\operatorname{canonical\_chart}(p,L)=(R,K).
\tag{4}
\]

也就是说，\(L\) 保持同一图表，而不是切换到另一个 rechart。又因 \(A<L\)，整除性给出
\(L/A\ge2\)；当 \(L\le B_p\) 时

\[
\Pi_p(L)<\Pi_p(A).
\tag{5}
\]

若原 high anchor 的 overflow 余因子为 \(K/A<p\)，则

\[
0<\frac KL<\frac KA<p,\qquad 4L-R>0,
\]

并且重分解仍满足

\[
p(4L-R)=4L\left(p-\frac KL\right)+1.
\tag{6}
\]

所以 (1) 中每个 \(L\) 都是 same-chart support-promotion 定理所需的代数 overflow
carrier；反之，一个保持图表、真增加支撑、保留 \(A\mid L\) 的 charged-support 链，且留在
该定理 \(B_p\) 势域的 carrier 必然满足 (1)。

若允许 \(A\nmid L\)，严格 \(\Pi_p\) 仍可能支付一个 support reset；那是外层 reset 的
另一种 state contract，不保持本节的支撑单调语义，也没有被本卡的 49 次枚举排除。

full-excess bundle 只由 \((R,K)\) 决定，故在同图表提升时 \(Q\) 不变。把 support 从
\(A\) 换成 \(L\) 后，唯一改变的高 bundle carrier 是 (2) 的 \(M_L\)。标准 cofactor
正规形给出 target support \(\operatorname{lcm}(L,C_L)\)，其可整除 target determinant
当且仅当 (3) 成立。这证明了 gate 的精确判据。

## 3. 冻结 atlas

输入是
`type-i-high-anchor-parent-atlas-results.json` 中严格 verified-parent 后继的高锚；它有
51 个 occurrence，压缩后为 31 个不同的 \((p,R,K,A)\)。没有重新运行 selector 或搜索
未冻结历史。

| 项目 | 数量 |
|---|---:|
| 不同高锚 | 31 |
| occurrence | 51 |
| 有至少一个 \(L\in\mathcal L_H\) 的高锚 | 13 |
| 已付款提升候选 | 49 |
| 原 support 的 gate 命中 | 0 |
| 提升后的 gate 命中 | 0 |

这排除了一个具体策略：不能在这些 verified parents 后面先插入一条保持 \(A\mid L\) 的
外层 \(\Pi_p\)-paid same-chart 边，再期望 deterministic full-excess cofactor 分支因此跨过
gate。

## 4. 三个独立控制例

这三个控制例不属于上面的冻结 parent atlas，故单列为机制边界。

| \(p\) | 原 gate | 真提升数量 | 提升后 gate | 结论 |
|---:|---|---:|---|---|
| 1201 | 通过 | 18 | 仅 \(L=1972\) 通过 | 不是由失败到成功的 rescue |
| 3793 | 通过 | 0 | 无 | 最小真提升 \(L=K\) 已越过 \(B_p\) 域 |
| 60913 | 通过 | 0 | 无 | 最小真提升 \(L=K\) 已越过 \(B_p\) 域 |

\(p=1201,L=1972\) 的通过行有

\[
M_L=1812268,\quad C_L=476,\quad r_L=1160,
\quad \frac{L}{\gcd(L,C_L)}=29,
\]

其 target 仍回到 \((R,K)=(1839,552160)\)，但 support 为 \(13804\)。两段势均严格下降：

\[
\Pi_{1201}(986)=365>182=\Pi_{1201}(1972)>26=\Pi_{1201}(13804).
\]

它说明 gate 对 support 没有一般单调性，却没有提供 gate rescue 的反例：\(A=986\) 的
原 gate 已经通过。

## 5. 组合与边界

若某行 (3) 通过，前一段 same-chart promotion 的 E5 是 (5)，后续 direct cofactor macro
仍必须独立验证 target 的 \(\Lambda_p\) 下降。二者可以在同一外层势中串联，但不应把
“算术 gate 命中”混同为完整宏边。

本卡尤其不补充以下缺项：

- legacy parent 是否具备内容寻址、scope 连续的高宏 parent API；
- H、transient S、target T 的 typed F/G/hit 纤维及恒等解提升；
- terminal/alternate 菜单是否已经先行耗尽；
- 跨 RESET 或 token-exit 的全局 E5。

因此结果是一条单调支撑策略排除和精确有限检索域，不是全称 selector 定理，也不排除
非整除 support reset 后的其它宏入口。

## 复现

```bash
python3 reproductions/type_i_high_anchor_same_chart_gate_engineering.py --verify
```
