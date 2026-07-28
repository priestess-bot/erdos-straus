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
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK},\qquad
\frac4n=\frac1{nK/E}+\frac1{AC}+\frac1{ACH}.
\tag{2}
\]

所以 (1) 确实给出一张 \(B=1\) Type I 正规形及严格偶源终端桥。上半区条件
\(E<2K\) 强于原终端选择器仅要求的 \(E\le4K-2R\)。

## 源优先的精确等价形式

第二分支不必先选择缺口 \(m\)。对固定核心素数 \(p\)，它等价于存在正整数

\[
\begin{aligned}
&s\equiv1\pmod2,\qquad 1\le s\le\frac{p-1}{2},\qquad
n=p-s,\\
&R\equiv3\pmod4,\qquad R\ge3,\qquad
K=\frac{pR+1}{4},\qquad E=sR+1,\\
&E\mid\frac{n^2}{\gcd(E,4)},\qquad
C\mid K,\qquad 4C\equiv-1\pmod R.
\end{aligned}
\tag{3}
\]

这是一种源优先的两层因子选择：\(E\) 是近目标偶源 \(n\) 的归一化平方因子，
而 \(C\) 是 \(K\) 中落入指定剩余类的普通除子。它不再显式搜索 \(m\) 或目标
平方除子。

确实，若 (1) 的第二分支成立，令 \(s=p-n\)。由 \(4K=pR+1\) 得

\[
E=4K-nR=sR+1. \tag{4}
\]

\(E\) 为偶数且 \(R\) 为奇数，故 \(s\) 为奇数；上半区条件给出
\(s\le(p-1)/2\)。又 \(mR=4C+1\) 给出 \(R\equiv3\pmod4\)、
\(4C\equiv-1\pmod R\)，且 \(B=1\) 时 \(C\mid K\)。
[归一化源平方等价](type-I-normal-source-square-bridge-equivalence.md) 把
\(E\mid4K^2\) 精确改写为 (3) 中的平方整除条件。

反过来，假设 (3)，写 \(H=K/C\)。由 \(4K\equiv1\pmod R\) 及
\(4C\equiv-1\pmod R\) 得 \(H\equiv-1\pmod R\)。故

\[
A=\frac{H+1}{R},\qquad m=\frac{4C+1}{R} \tag{5}
\]

均为正整数，且 \(m\equiv3\pmod4\)。并有

\[
p=4AC-m,\qquad
K=CH=ACR-C,\qquad
x=AC=\frac{p+m}{4}. \tag{6}
\]

这里 \(m<(4C+1)/3<2C\le2AC\)，所以 \(m<p=4AC-m\)。平方整除条件与
(4) 通过同一源平方等价给出 \(E\mid4K^2\)。最后

\[
n=p-s\ge\frac{p+1}{2}
\quad\Longleftrightarrow\quad
E=4K-nR<2K, \tag{7}
\]

从而完全恢复 (1) 的第二分支。

## 源谱与目标谱相交的精确等价表述

固定同一个核心素数 \(p\)。定义正模数的源可达谱

\[
\mathcal R_{\rm src}(p)=
\left\{
\begin{array}{ll}
R\in\mathbb Z_{>0}:& R\ge3,\quad R\equiv3\pmod4,\\
&\exists\ s\equiv1\pmod2,\quad
1\le s\le\dfrac{p-1}{2},\\
&sR+1\mid\dfrac{(p-s)^2}{\gcd(sR+1,4)}
\end{array}
\right\}, \tag{S1}
\]

以及 \(B=1\) 的目标命中谱

\[
\mathcal R_{\rm tgt}(p)=
\left\{
\begin{array}{ll}
R\in\mathbb Z_{>0}:& R\ge3,\quad R\equiv3\pmod4,\\
&K=\dfrac{pR+1}{4},\quad
\exists\ H\in\mathbb Z_{>0},\quad H\mid K,\quad
H\equiv-1\pmod R
\end{array}
\right\}. \tag{S2}
\]

这里的正性条件不可省略：\(H\) 是 \(K\) 的正除子，两个谱中的 \(R\) 也都限制为
正整数。由于 \(p\equiv1\pmod4\) 且 \(R\equiv3\pmod4\)，(S2) 中的 \(K\) 自动为
正整数。

对固定的 \(p,R\) 和 \(K=(pR+1)/4\)，映射

\[
C\longmapsto H=\frac KC \tag{S3}
\]

在下列两个正除子集合之间给出双射：

\[
\left\{C\in\mathbb Z_{>0}:C\mid K,\ 4C\equiv-1\pmod R\right\}
\longleftrightarrow
\left\{H\in\mathbb Z_{>0}:H\mid K,\ H\equiv-1\pmod R\right\}. \tag{S4}
\]

确实，恒等式 \(4K=pR+1\) 给出 \(4K\equiv1\pmod R\)。若左侧的 \(C\) 已知，
则 \(4CH=4K\) 与 \(4C\equiv-1\pmod R\) 推出 \(H\equiv-1\pmod R\)。反过来，
若右侧的 \(H\) 已知，取正整数 \(C=K/H\)，则同一恒等式与
\(H\equiv-1\pmod R\) 推出 \(4C\equiv-1\pmod R\)。两次变换互为逆映射，因而
这不是单向的充分条件。

于是 (3) 的第二分支精确等价于

\[
\boxed{\mathcal R_{\rm src}(p)\cap\mathcal R_{\rm tgt}(p)\ne\varnothing}. \tag{S5}
\]

因此整个开放猜想也可等价地写成

\[
\boxed{
p\text{ 有普通 Type II }(p-1)\text{ 双尾证书}
\quad\lor\quad
\mathcal R_{\rm src}(p)\cap\mathcal R_{\rm tgt}(p)\ne\varnothing.} \tag{S6}
\]

这只是本页现有猜想的另一种精确表述，不是新增的开放猜想。源谱本身总是非空：取
\(s=1,R=3\) 时 \(sR+1=4\)，而 \(p\equiv1\pmod{24}\) 保证
\(4\mid(p-1)^2/4\)。真正的选择问题是让同一个源可达模数同时落入目标命中谱。

[Type I 源平方状态的唯一正规分解与双因子块](type-I-source-square-normal-factorization.md)
进一步令

\[
\lambda=\gcd(p-s,4)=\gcd(sR+1,4),\qquad
u=\frac{p-s}{\lambda},\qquad D=\frac{sR+1}{\lambda},
\]

并把 (S1) 中每个源状态唯一写成

\[
u=\alpha\beta\gamma,\qquad D=\beta^2\gamma,\qquad
K=(\beta\gamma)L,\qquad
L=\frac{\alpha R+\beta}{4/\lambda}, \tag{S7}
\]

其中 \(D\mid u^2\)。因此目标谱条件可等价读成

\[
-1\in\{d\bmod R:d\mid(\beta\gamma)L,\ d>0\}. \tag{S8}
\]

谱相交表述仍然严格强于[允许一般 \(B\) 的原混合终端目标](type-I-target-divisor-even-terminal-selector.md)：
它把目标因子限制为
\(e=C\mid x\)，即强制 \(B=1\)，并把偶源限制在上半区；原选择器则允许
\(e=B^2C\mid x^2\) 的任意溢出因子 \(B\)，且只要求 \(n\ge2\)。这里的“严格强于”
指证书条件确有这两层额外限制；它不表示已经证明两个全称命题在逻辑上不等价。

## \(E=n\) 走廊与外部源的边界

源优先式 (3) 的特例 \(E=n\) 不是新的终端机制。此时

\[
n=sR+1=p-s,\qquad
p=s(R+1)+1.
\tag{8}
\]

令 \(k=(R+1)/4\)，则

\[
k\mid\frac{p-1}{4},\qquad
n=\frac{Rp+1}{R+1},\qquad
K=kn.
\tag{9}
\]

又令 \(H=K/C\)。源优先条件给出 \(H\equiv-1\pmod R\)，故

\[
C\mid K^2,\qquad C\le K,\qquad C\equiv-K\pmod R.
\tag{10}
\]

所以 \((q,M,e)=(R,K,C)\) 正是
[完整平方因子外部源](quadratic-factor-external-source-descent.md) 的因子条件；其恢复的
Type I 证书满足 \(u=(K+C)/R=AC\)、\(v=Ku/C=ACH\)，并且 \(B=1\)。反过来，
任何偶数源、且正规化后 \(B=1\) 的该外部源见证都落回 (3) 的 \(E=n\) 特例。这与
[外部源到正规形桥](type-I-even-external-source-normal-bridge.md) 相容。

这条识别给出明确的路线边界：\(E=n\) 只能复用已有外部源选择问题，不能单独构成新的
全称证明。但一般的 \(E\ne n\) 不自动离开外部源走廊：同一张 \(B=1\) 正规形可有多个
反向源。精确的回缩判据见
[B等于一正规形回缩到完整平方因子外部源](type-I-b1-external-source-retraction-criterion.md)。
它表明，令 \(k=(R+1)/4\)，只要 \(k\mid K\)，该证书仍以同一 \((R,K,C)\) 回缩到典范
外源 \(N=K/k\)，即使当前选择的 \(E\ne n\)。

事实上，在五亿普通双尾遗漏的 1,717 张**按当前目标级规则选定**的上半区 \(B=1\) 证书中，
逐条都有 \(E\ne n\)，但其中 1,132 张仍可作这种外源回缩（636 张的典范源为偶数）；只有
585 张所选正规形满足 \(k\nmid K\)。因此，下一阶段不应把 \(E\ne n\) 笼统称为“新机制”，
而应分开研究可回缩外源的标记递降，以及这 585 张非回缩正规形的源平方选择。

## 与原目标的关系

[目标除子与偶终端桥的双因子选择器](type-I-target-divisor-even-terminal-selector.md)
允许第一层取平方除子 \(e\mid x^2\)，其溢出因子就是正规形的 \(B\)。本猜想额外要求

\[
e=C\mid x,\qquad B=1,
\tag{11}
\]

并把源限制在上半区。因此

\[
\text{自适应上半区 \(B=1\) 选择器}
\Longrightarrow
\text{上半区混合终端选择器}
\Longrightarrow
\text{原混合终端选择引理}.
\tag{12}
\]

反向蕴含目前没有证明，也不应从有限样本推断。

## 已证的密度一 \(B=1\) 子分支

上式第二分支并非只由有限扫描支持。两条独立移位因子机制逐点构造上半区偶桥：

- 若 \((p+1)/2\) 有 \(q\equiv3\pmod4\) 的素因子，则
  [\(p+1\) 分支](type-I-p-plus-one-b1-upper-bridge.md)取
  \(A=B=1\)、\(E=((p+1)/q)^2\)；
- 若 \((3p+1)/4\) 有 \(q\equiv2\pmod3\) 的素因子，则
  [三p加一分支](type-I-three-p-plus-one-b1-upper-bridge.md)取
  \(R=3\)、\(E=2q\)，把已有的奇源递降完成为偶终端桥。

[两条分支的联合筛界](type-I-b1-two-shift-density-bridge.md)已经证明：同时逃过它们的核心
素数至多有 \(O(X/(\log X)^2)\) 个。其补集仍可能无限，故这条正面结果缩小的是最终逐点选择
问题，而非完成它。

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

## 已证的不可收缩边界

两个无穷射线进一步限定了任何全称证明可以采用的归约。第一，
[无界平方缺额射线](type-I-b1-square-essential-same-gap-nonoverlap-ray.md) 对任意
\(a\ge1\) 给出核心素数，其 \(B=1\) 的 \(p-1\) 桥满足

\[
v_2\!\left(\frac{R+1}{4}\right)-v_2\!\left(\frac{p-1}{4}\right)=a,
\tag{13}
\]

并且同缺口 Type II 双尾不存在。故不能把 \(p-1\) 桥统一压缩成外源的线性条件
\(E\mid p-1\)，也不能给平方缺额设绝对上界后交给同缺口 Type II。

第二，[移位源非重叠射线](type-I-b1-shifted-source-pminusone-nonoverlap-ray.md) 给出无穷多
核心素数：同一 \(B=1\) 正规形以 \(s=3\) 有偶终端桥，但其 \(p-1\) 桥条件和同缺口
Type II 双尾条件都失败。故“先只选 \(p-1\) 源”不是可无损使用的归约。

因此 (13) 的自适应量词至少必须同时允许非零源距离与无界的源平方指数；真正需要证明的
是这些变量与 \(K\) 的指定剩余类除子之间的正向选择关系，而不是再试图删去其中一个变量。

## 下一条定理

证明 (1) 的最小非平凡步骤是建立下列因子状态析取：

\[
\boxed{
\begin{aligned}
\text{对每个没有普通双尾的核心素数 \(p\)，}\\
\text{自适应地构造 \(s,R,C\) 满足源优先条件 (3)。}
\end{aligned}}
\tag{14}
\]

其第一层是 \(E=sR+1\) 对近目标源平方的整除，第二层是 \(K\) 中普通除子 \(C\) 的
指定残数命中。因而证明必须同时选择源距离、源平方因子和目标因子；单独控制任一个量、
固定有限菜单或把某个选定源状态的缺口当作下界，都不足以推出 (3)。
