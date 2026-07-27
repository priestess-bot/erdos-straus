---
kind: claim
claim_id: type-I-upper-half-mixed-terminal-selector-conjecture
title: 上半区偶源混合终端选择猜想
statement: 对每个核心素数p，或者p具有普通Type II p-1双尾证书，或者存在一个Type I正规形4K=pR+1，令L=2K后存在互素除子a,b|L，满足a<b、a=2b mod R且2|a或b|L/2。等价地，第二分支有偶桥因子E|4K^2、E=1 modR，其源n=(4K-E)/R满足n≥(p+1)/2。该猜想严格强于只要求2≤n<p的原混合终端选择引理。
claim_status: open
proof_provenance: mixed
review_status: internal_review
topics:
- type-I
- type-II
- mixed-selector
- upper-half-source
- even-source
- divisor-pairs
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 上半区偶源混合终端选择猜想

对核心素数 \(p\equiv1\pmod {24}\)，提出以下加强析取：

\[
\boxed{
\begin{aligned}
&\text{存在普通 Type II \(p-1\) 双尾证书，}\\
&\quad\text{或}\\
&\exists\ \text{Type I 正规形 }4K=pR+1,\ L=2K,\ a,b\mid L:\\
&(a,b)=1,\quad a<b,\quad a\equiv2b\pmod R,\quad
\left(2\mid a\ \text{或}\ b\mid L/2\right).
\end{aligned}}
\tag{1}
\]

第二行的因子对由

\[
E=\frac{La}{b},\qquad n=\frac{2L-E}{R}
\tag{2}
\]

重构。根据[小侧普通除子对引理](type-I-normal-even-source-small-side-simplification.md)，
它精确给出偶桥

\[
E\mid4K^2,\qquad E\equiv1\pmod R,
\qquad n\ge\frac{p+1}{2}.
\tag{3}
\]

反之，任何满足 (3) 的 Type I 偶桥都恢复 (1) 的因子对。因此本猜想不是另一种记号，
而是把 Type I 选择压缩为 \(L=2K\) 的**小侧互素除子残数问题**。

## 与原目标的关系

原混合终端选择引理只要求

\[
2\le n<p
\quad\Longleftrightarrow\quad
E\le4K-2R.
\tag{4}
\]

这里额外要求 \(n\ge(p+1)/2\)，或等价的 \(E<2K\)。故 (1) 严格更强：
证明它会证明原目标；发现一个仅缺少上半区桥的点，却**不会**反驳原目标。

## 当前证据

在 \(p\le5\cdot10^8\) 的完整普通 Type II 双尾遗漏集上，1,717 个回退点均可在
\(m\le215\) 的 Type I 正规形盒中重选为小侧桥，见
[五亿替代正规形剖面](type-I-tail-reverse-even-source-small-side-alternative-profile-500m.md)。

在连续区间

\[
5\cdot10^8<p\le6\cdot10^8
\]

中，621,704 个核心素数有普通双尾；余下 247 个回退点也全部有小侧桥，其中 205 个首次
记录已是小侧，42 个经替代正规形释放，见
[六亿连续小侧剖面](type-I-mixed-terminal-dense-small-side-profile-600m.md)。

以源状态的 \(B=1\) 实现进一步审计时，247 个点中 207 个初始 \(B=1\) 记录已经在上半区；
其余 40 个均可经同一盒的完整上半区源重选恢复为 \(B=1\)，见
[六亿上半区 B等于一重选剖面](type-I-mixed-terminal-dense-upper-b1-reselection-profile-600m.md)。
这为“先重选源、再取小 \(B\)”提供独立区间证据，但不能与五亿范围的 \(B=3\) 例外合并为
统一 \(B=1\) 定理。

这些是精确整数与分数恒等式重建的有限证据，不给出 \(m\)、\(B\)、\(R\) 或 \(E\) 的全称界。

同一五亿盒的完整 \(p-1\) 子选择器只覆盖 1,532 个普通双尾遗漏，另有 185 个没有任何
\(p-1\) 桥，见 [p减一桥边界](type-I-tail-reverse-pminusone-boundary-500m.md)。由于所有
1,717 点仍有小侧桥，这 185 点确认一般 Type I 分支不能在该模型中收缩为 \(p-1\) 源。

进一步地，这 185 点的最短桥全部仍是小侧上半区桥，但源距离从 \(3\) 延伸到
\(48{,}244{,}917\)，并出现 127 个不同的 \((s=p-n,E)\) 源状态，见
[p减一遗漏上半区剖面](type-I-pminusone-miss-upper-half-profile-500m.md)。这些状态组成的固定
菜单又被一条显式 Dirichlet 进程同时逃开，见
[127状态CRT逃逸](type-I-pminusone-miss-state-menu-crt-escape-500m.md)。因此，短源集中性、
\(p-1\) 子选择器和当前经验桥菜单都不能代替一个随实际因子状态变化的选择原理。

同一批最短源状态中，\(66\) 个没有 \(B=1\) 的正规形实现；其中一个最小实现需要三级
指数溢出，见[三级溢出边界](type-I-pminusone-miss-source-overflow-profile-500m.md)。但这也不是
目标级障碍：逐点重选同一有限盒中的上半区源后，\(65\) 个恢复 \(B=1\)，唯一余点
\(p=218{,}482{,}009\) 的最小上半区实现为 \(B=3\)，从而全部 \(185\) 点仍有
\(B\le3\) 的上半区桥，见[源重选 B不大于三剖面](type-I-pminusone-miss-upper-b3-reselection-profile-500m.md)。
所以“固定源上的低指数溢出”与“任意重选后固定 \(B=1\)”都已在此有限压力集失败；
源状态和正规形必须作为耦合变量选择。

## 研究任务

证明 (1) 的本质不是增加扫描范围，而是构造一个跨正规形、跨源状态的**二层**选择原理：它必须
先从 \(p\) 的实际因子状态产生一个菜单外的 \((s,E)\)，再通过
[源状态实现判据](type-I-normal-source-state-realization.md)选择 \(BC\mid K\) 的小侧对；或者直接
强制普通双尾。这里第一层不能固定桥菜单、源距离或预先选定源状态，第二层也不能全局固定为
\(B=1\) 或固定指数溢出阈值。只跟踪字符核、总积同余或固定有限候选盒均不足以完成这一步；
这些信息不会控制因子指数、源状态和跨正规形的重选。
