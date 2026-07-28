---
kind: claim
claim_id: type-I-adaptive-upper-b1-terminal-selector-conjecture
title: 自适应上半区 B 等于一混合终端选择猜想
statement: 对每个核心素数p，要么p有普通Type II p-1双尾证书，要么存在m=3 mod4、C|(p+m)/4及偶数E，使R=(4C+1)/m、K=((p+m)/4)R-C，满足E|4K^2、E=1 modR及E<2K，并令n=(4K-E)/R后有n>=(p+1)/2。此时p有B=1的Type I正规形和严格上半区偶源桥。该猜想严格强于原混合终端选择引理。
claim_status: open
proof_provenance: mixed
review_status: internal_review
topics:
- type-I
- type-II
- b1
- upper-half-source
- target-divisor
- mixed-selector
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# 自适应上半区 \(B=1\) 混合终端选择猜想

对每个核心素数 \(p\equiv1\pmod {24}\)，提出如下加强析取：

\[
\boxed{
\begin{aligned}
&\text{\(p\) 具有普通 Type II \(p-1\) 双尾证书，}\\
&\quad\text{或}\\
&\exists\ m\equiv3\pmod4,\quad
x=\frac{p+m}{4},\quad C\mid x,\\
&R=\frac{4C+1}{m},\quad K=xR-C,\quad
E\mid4K^2,\quad E\equiv1\pmod R,\\
&2\mid E,\quad E<2K,\quad
n=\frac{4K-E}{R}\ge\frac{p+1}{2}.
\end{aligned}}
\tag{1}
\]

这里 \(C\mid x\) 正是目标除子 \(e=C\) 的 \(B=1\) 情形。令

\[
A=\frac{x}{C},\qquad H=AR-1.
\]

则 \(K=CH\)、\(p=4AC-m\)，并且

\[
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK},
\qquad
\frac4n=\frac1{nK/E}+\frac1{AC}+\frac1{ACH}.
\tag{2}
\]

所以 (1) 确实给出一张 \(B=1\) Type I 正规形及严格偶源终端桥。上半区条件
\(E<2K\) 强于原终端选择器仅要求的 \(E\le4K-2R\)。

## 与原目标的关系

[目标除子与偶终端桥的双因子选择器](type-I-target-divisor-even-terminal-selector.md)
允许第一层取平方除子 \(e\mid x^2\)，其溢出因子就是正规形的 \(B\)。本猜想额外要求

\[
e=C\mid x,\qquad B=1,
\tag{3}
\]

并把源限制在上半区。因此

\[
\text{自适应上半区 \(B=1\) 选择器}
\Longrightarrow
\text{上半区混合终端选择器}
\Longrightarrow
\text{原混合终端选择引理}.
\tag{4}
\]

反向蕴含目前没有证明，也不应从有限样本推断。

## 有限证据与反证边界

在 \(p\le5\cdot10^8\) 的全部 1,717 个普通双尾遗漏中，目标级重选已给出 (1) 的第二分支，
所选最大缺口为 \(5963\)，见
[五亿上半区 B等于一终端闭合](type-I-tail-upper-b1-completion-profile-500m.md)。
在独立连续区间

\[
5\cdot10^8<p\le6\cdot10^8
\]

的 247 个普通双尾遗漏中，第二分支在 \(m\le131\) 闭合，见
[六亿上半区 B等于一重选剖面](type-I-mixed-terminal-dense-upper-b1-reselection-profile-600m.md)。

这些证据支持把 (1) 作为优先的研究假设，但不构成全称证明。固定源状态菜单已经有
CRT 逃逸，固定 \(p-1\) 子选择器也有有限盒遗漏；它们只排除**固定**的 \((m,C,E)\) 或
\((s,E)\) 菜单，并不反驳 (1) 的自适应量词。

## 下一条定理

证明 (1) 的最小非平凡步骤是建立下列因子状态析取：

\[
\boxed{
\begin{aligned}
\text{对每个没有普通双尾的核心素数 \(p\)，}\\
\text{自适应地构造 \(m,C,E\) 满足 (1) 的全部整除与同余。}
\end{aligned}}
\tag{5}
\]

其第一层是普通除子 \(C\mid(p+m)/4\) 的残数命中，第二层是 \(E\mid4K^2\) 的偶桥。
因而证明必须同时选择缺口、目标因子和桥因子；单独控制任一个量、固定有限菜单或把某个
选定源状态的缺口当作下界，都不足以推出 (5)。
