---
kind: claim
claim_id: two-denominator-lift-d-only-marked-normal-form
title: 双尾提升的 D-only 标记正规形与 p 载体刚性
statement: 设 2<=n<p、r=p-n、N=np、C=4r。所有可能承载双尾保留提升的正替换坐标对，恰由满足 D|N^2、0<D<n^2、D=N (mod C)、N^2/D=N (mod C) 的因子 D 参数化；a=(N-D)/C、a'=(N^2/D-N)/C，且对所有 b,c 有 (a,b,c)∈Sol(n) 当且仅当 (a',b,c)∈Sol(p)。若 kappa∈{1,2,3,4} 且 n+kappa=0 (mod 4)，则每个合法 D 都满足 D<=n(n+kappa)-kappa p；特别当 kappa p>=n(n+kappa) 时整个 D 集为空。实际标记提升存在还等价于正因子同余 z|sigma^2、z=-sigma (mod mu)。当 p 为素数时必有 p|a'，所以替换坐标不是目标解的最小分母。D-only 数据只给出局部已验证的条件边；后继标记状态递归闭合后才承载证明，同时给出 z 则已显式闭合为终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - two-denominator-lift-criterion
  - marked-solution-descent-closure
topics:
  - descent
  - marked-solution
  - two-denominator-lift
  - divisor-parametrization
  - factor-congruence
  - p-adic-rigidity
  - solution-lift
  - proof-boundary
sources:
  - claim: two-denominator-lift-criterion
    role: one-coordinate-replacement-identity
  - claim: marked-solution-descent-closure
    role: marked-state-induction-contract
visibility: public
last_checked: '2026-07-31'
---

# 双尾提升的 \(D\)-only 标记正规形与 \(p\) 载体刚性

## 1. 全部正替换坐标对的无尾参数化

设 \(p\) 为奇素数，\(2\le n<p\)，并记

\[
r=p-n,
\qquad N=np,
\qquad C=4r.
\tag{1}
\]

定义因子集合

\[
\mathcal D(p,n)=
\left\{
D:
\begin{array}{l}
D\mid N^2,\quad 0<D<n^2,\\
D\equiv N\pmod C,\\
N^2/D\equiv N\pmod C
\end{array}
\right\}.
\tag{2}
\]

对每个 \(D\in\mathcal D(p,n)\)，令

\[
F=\frac{N^2}{D},
\qquad
a_D=\frac{N-D}{C},
\qquad
a_D'=\frac{F-N}{C}.
\tag{3}
\]

式 (2) 保证 \(a_D,a_D'\) 都是正整数。更重要的是，对任意正整数 \(b,c\) 都有

\[
\boxed{
\frac4n=\frac1{a_D}+\frac1b+\frac1c
\iff
\frac4p=\frac1{a_D'}+\frac1b+\frac1c.}
\tag{4}
\]

反过来，每个实际保留 \(b,c\) 的正整数提升都唯一来自 (2)--(3) 的一个 \(D\)。所以
\(D\) 在读取任何具体源解之前，已经参数化了全部可能的正替换坐标对；它尚不保证存在
承担这对坐标的正整数尾 \(b,c\)。后一个非空问题由第 3 节单独判定。

## 2. 证明

已有的一项替换判据令

\[
D=N-Ca
\tag{5}
\]

并证明提升存在当且仅当 \(D>0\)、\(D\mid Na\)，此时

\[
a'=\frac{Na}{D},
\qquad D(N+Ca')=N^2.
\tag{6}
\]

由源方程剩余两项为正，必有

\[
\frac1a<\frac4n,
\qquad a>\frac n4.
\]

代入 (5) 得到严格上界

\[
D=np-4(p-n)a<n^2.
\tag{7}
\]

这里还有一个对后续候选选择非常强的全域尺寸推论。令唯一的

\[
\kappa\in\{1,2,3,4\},
\qquad
n+\kappa\equiv0\pmod4.
\tag{7a}
\]

因为 \(a=a_D\) 为整数且 \(a_D>n/4\)，有

\[
a_D\ge\frac{n+\kappa}{4}.
\]

代回 \(D=np-4(p-n)a_D\)，得到

\[
\boxed{
D\le n(n+\kappa)-\kappa p.
}
\tag{7b}
\]

所以

\[
\boxed{
\kappa p\ge n(n+\kappa)
\Longrightarrow
\mathcal D(p,n)=\varnothing.
}
\tag{7c}
\]

特别地，若 \(n\equiv3\pmod4\)，则 \(\kappa=1\)，从而

\[
p\ge n(n+1)
\Longrightarrow
\mathcal D(p,n)=\varnothing.
\]

这个结论排除的是全部 D-only 参数，不只是一种标准源坐标。

式 (5)--(7) 立即推出 (2)，并由 (5)--(6) 恢复 (3)。

反向地，(2) 给出 \(D<N\) 及 \(F>N\)，故 (3) 为正整数。又有

\[
a_D'D
=\frac{(F-N)D}{C}
=\frac{N(N-D)}{C}
=Na_D.
\tag{8}
\]

因此

\[
\frac1{a_D'}
=\frac D{Na_D}
=\frac1{a_D}-\frac C N
=\frac1{a_D}+\frac4p-\frac4n,
\tag{9}
\]

这正是 (4)。由 (5) 又可从 \(a_D\) 唯一恢复 \(D\)，故参数化无重复。

## 3. 标记集非空的第二层因子判据

定义

\[
W(p,n,D)=
\left\{
(a_D,b,c)\in\operatorname{Sol}(n)
\right\}.
\tag{10}
\]

要判定它是否非空，令

\[
M=4a_D-n=\frac{n^2-D}{r},
\qquad S=na_D,
\qquad g=(M,S),
\qquad \mu=\frac Mg,
\qquad \sigma=\frac Sg.
\tag{11}
\]

由 \(D<n^2\) 可知 \(M>0\)，而标记源方程等价于

\[
\frac\mu\sigma=\frac1b+\frac1c,
\qquad (\mu,\sigma)=1.
\tag{12}
\]

标准因子化

\[
(\mu b-\sigma)(\mu c-\sigma)=\sigma^2
\tag{13}
\]

给出精确判据

\[
\boxed{
W(p,n,D)\ne\varnothing
\iff
\exists z>0,\quad z\mid\sigma^2:
z\equiv-\sigma\pmod\mu.}
\tag{14}
\]

一旦给出这样的 \(z\)，两个保留分母就是

\[
b=\frac{\sigma+z}{\mu},
\qquad
c=\frac{\sigma+\sigma^2/z}{\mu}.
\tag{15}
\]

因为 \((\mu,\sigma)=1\)，任一 \(z\mid\sigma^2\) 也与 \(\mu\) 互素；所以第一个
同余自动保证互补因子 \(\sigma^2/z\) 也同余于 \(-\sigma\pmod\mu\)。这证明了 (14)
的两个方向。

## 4. 素数目标的 \(p\) 载体刚性

每个 \(D\in\mathcal D(p,n)\) 的正替换坐标都满足

\[
\boxed{p\mid a_D'.}
\tag{16}
\]

若 \(p\nmid D\)，由 \(D\mid Na_D=npa_D\) 及 \((D,p)=1\) 可消去 \(D\)，直接得到
\(a_D'=p(na_D/D)\)。

若 \(p\mid D\)，式 (5) 及 \(p\nmid4r\) 先给出 \(p\mid a_D\)。写

\[
a_D=pu,
\qquad D=p(n-4ru).
\tag{17}
\]

由 \(D>0\) 得 \(0<n-4ru<n<p\)，所以括号内与 \(p\) 互素。将 (17) 代入 (6)，
再用 \(a_D'\) 的整数性，仍得到 \(p\mid a_D'\)。因此 \(a_D'\ge p\)。

另一方面，任意 \(4/p\) 的三分母解，其最小分母 \(w\) 满足

\[
\frac4p\le\frac3w,
\qquad w\le\frac{3p}{4}<p.
\tag{18}
\]

所以替换坐标 \(a_D'\) 不可能成为目标解的最小分母；最小项必是保留下来的 \(b\) 或
\(c\)。这是所有双尾提升共有的结构刚性，不是有限样本现象。

## 5. 递降合同与尚缺的选择器

对根状态 \(W_S=\operatorname{Sol}(p)\)，把 (10) 作为秩 \(n\) 的后继标记集，并定义

\[
\Phi_D(a_D,b,c)=(a_D',b,c).
\tag{19}
\]

则 (2)--(4) 给出确定状态和正规形核验，(19) 是全域解提升，而 \(n<p\) 给出严格秩
下降。因此它是一条 `locally_verified_conditional_edge`。状态 schema 不预设标记集非空，
但这不意味着证明分支可以选择空后继：只有后继标记状态被一个完整递归子树闭合后，
(19) 才能反推根状态非空；若 (14) 已证为空，该 \(D\) 必须标为 `rejected_branch`。

这里必须区分两种输出：

1. 只给出 \(D\)，得到一条读取较小标记状态、仍待递归闭合的条件 E4 边；
2. 同时给出 (14) 的 \(z\)，则 (15) 和 (19) 已经显式写出目标解，应登记为终端叶。

因此新的开放问题被压缩为：对每个仍无短证书的核心素数，规范选择
\(n<p\) 与 \(D\in\mathcal D(p,n)\)，并在不知道 \(z\) 的前提下，把
\(W(p,n,D)\) 递归归约到更小的非空标记状态。普通归纳假设
\(\operatorname{Sol}(n)\ne\varnothing\) 不足以推出这个指定坐标切片非空。

## 6. 正例与空标记警示

取

\[
(p,n,D)=(73,33,9).
\]

则 \(a_D=15\)、\(a_D'=4015\)，并有

\[
(M,S,g,\mu,\sigma)=(27,495,9,3,55).
\]

因子 \(z=11\) 满足 \(z\mid55^2\)、\(z\equiv-55\pmod3\)，从 (15) 恢复
\((b,c)=(22,110)\)，于是

\[
\left(15,22,110\right)
\longmapsto
\left(4015,22,110\right).
\]

这个例子验证局部边非空，但不提供全称 \(D\)-选择定理。

相反，取

\[
(p,n,D)=(73,57,1).
\]

式 (2) 的四个条件全部成立，并给出

\[
a_D=65,
\qquad a_D'=270465,
\qquad(M,S,g,\mu,\sigma)=(203,3705,1,203,3705).
\]

但 \(3705^2\) 没有正因子 \(z\equiv-3705\pmod {203}\)，所以
\(W(73,57,1)=\varnothing\)。这严格说明 \(D\)-坐标正规形与实际非空提升之间仍隔着
(14)，也说明空标记状态上的空映射不能冒充证明递降。

## 7. source-supported 子类已经不能再作为递归出口

若再有

\[
D\mid n^2,
\tag{20}
\]

则该分支可以完全消元。令

\[
h=\frac{n^2}{D},
\qquad
k=\frac{h-1}{p-n},
\qquad
\lambda=\frac{pk+1}{4}.
\tag{21}
\]

已有
[source-supported 尾比刚性定理](two-denominator-lift-source-supported-tail-ratio-rigidity.md)
证明

\[
a_D=\frac{n\lambda}{h},
\qquad
a_D'=p\lambda,
\tag{22}
\]

而标记尾方程恒为

\[
\frac1b+\frac1c=\frac{k}{\lambda},
\qquad
4\lambda=pk+1.
\tag{23}
\]

所以该标记集非空当且仅当图表 \((R,K)=(k,\lambda)\) 已有中心 Type I 命中。
固定这张图表后，只继续替换 distinguished coordinate、保持同一双尾的数值递降，
不会改变尾投影或其非空性：miss 时整类标记集都为空，hit 时已经得到原 \(p\) 的直接
终端。

因此第 5 节的开放递归问题现在必须进一步限定。source-supported 的固定尾比子类已经
关闭为“直接 Type I 或空”；真正未解的 \(D\)-only 候选要么满足 \(D\nmid n^2\)，
要么下一条 E4 边必须改变保留尾、被替换坐标或既约尾比，而不能只在同一双尾恒等类中
继续降低 \(n\)。

## 8. 非自然支撑分支的后续完全消元

\(D\nmid n^2\) 的余项现已进一步化为

\[
\mu=4\lambda-1,
\qquad
\sigma=p\lambda,
\qquad
p+(4\lambda-1)(p-n)\mid4\lambda^2,
\]

其标记非空性等价于 \(\lambda^2\) 的一个真因子命中三个显式模 \(\mu\) 目标之一。
这个分型同时排除了核心状态中的 \(\mu=1\)、\(\mu=2\) 与 \(z=1\) 捷径。完整证明、
反向参数化和边界例见
[核心 D-only 的支撑二分、非自然完全正规形与三目标谱](two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum.md)。
