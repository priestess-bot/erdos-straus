---
kind: claim
claim_id: type-I-generalized-dyadic-second-layer-d-only-terminal-classification
title: 广义二进关系点的第二层 D-only 提升与 Type I/II 完整终端分类
statement: >-
  设核心图表 4K=pR+1 的广义二进关系点给出 E 与较小偶数
  n=(4K-E)/R。对该 n 枚举全部 D-only 因子 Delta|n^2p^2、
  0<Delta<n^2、Delta=np (mod 4(p-n))、n^2p^2/Delta=np (mod 4(p-n))，
  可恢复唯一替换坐标 a_Delta,a'_Delta，并在标记集
  W_Delta={(a_Delta,b,c) in Sol(4,n)} 上以保留双尾的公式全域提升到 p。
  反向给定目标首坐标 p*ell，保留两尾回到 n 当且仅当
  H_*=n+4(p-n)ell 整除 npell，且恢复的 Delta 唯一。
  自然标记唯一对应 Delta=n^2/E；保持当前图表双尾的 marking 不可能非自然。
  更一般地，只要 W_Delta 非空，该提升就已坍缩为原 p 的直接终端：
  Delta|n^2 时等价于另一张中心 Type I 图表，Delta不整除n^2时目标解恰有两个
  p-整除分母，因而条件性给出直接 Type II 除子证书。后续负 Pell 全分类进一步证明
  核心域后一支恒空，所以核心第二层实际只有中心 Type I 或空纤维，不产生递归状态。
  p=433、R=15、K=1624 的
  E=16 有非自然 Delta=2916 正例，但属于前一种 Type I；同图表外层 E=n=406
  则只有自然候选 Delta=406。故精确关系容量不保证非自然 D-only 候选或标记非空，
  且一旦第二层非空性被显式证明便没有新的递归状态类型。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-generalized-dyadic-exact-relation-capacity
  - type-I-generalized-dyadic-natural-lift-equivalence
  - two-denominator-lift-d-only-marked-normal-form
  - two-denominator-lift-source-supported-tail-ratio-rigidity
  - two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
  - type-II-coprime-factor-normal-form
  - two-denominator-lift-nonsource-pell-terminal-classification
topics:
  - type-I
  - type-II
  - generalized-dyadic
  - relation-lattice
  - D-only
  - marked-solution
  - solution-lift
  - terminal-collapse
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_generalized_dyadic_second_layer_d_only_terminal_classification.py
    role: focused-nonnatural-lift-natural-only-and-type-II-boundary-controls
visibility: public
last_checked: '2026-08-11'
---

# 广义二进关系点的第二层 (D)-only 提升与 Type I/II 完整终端分类

## 1. 两个不同的有限层

设

\[
p\equiv1\pmod {24},\qquad 4K=pR+1,
\tag{1}
\]

且取广义二进精确关系盒中的一个定向点 \(\lambda\in\mathcal D_K\)。第一层关系容量
唯一给出

\[
E=4K\rho(\lambda),
\qquad
n=\frac{4K-E}{R},
\qquad
0<n<p,\qquad 2\mid n.
\tag{2}
\]

这一层只构造算术偶前驱。为寻找保留两个源分母的 E4 映射，必须另行枚举与
\(\mathcal D_K\) 不同的第二层因子集。记

\[
r=p-n,\qquad N=np,\qquad C=4r,
\tag{3}
\]

并定义

\[
\mathfrak D(p,n)=
\left\{
\Delta:
\begin{array}{l}
\Delta\mid N^2,\quad0<\Delta<n^2,\\
\Delta\equiv N\pmod C,\\
N^2/\Delta\equiv N\pmod C
\end{array}
\right\}.
\tag{4}
\]

对 \(\Delta\in\mathfrak D(p,n)\)，置

\[
a_\Delta=\frac{N-\Delta}{C},
\qquad
a'_\Delta=\frac{N^2/\Delta-N}{C}.
\tag{5}
\]

式 (4) 保证二者为正整数。上界 \(\Delta<n^2\) 的准确作用不是单纯保证坐标正性；
它等价于源端剩余双尾具有正质量。事实上

\[
\frac4n-\frac1{a_\Delta}
=\frac{n^2-\Delta}{rna_\Delta}>0.
\tag{6}
\]

若只要求 \(a_\Delta,a'_\Delta>0\)，较弱的 \(0<\Delta<np\) 已经足够。

## 2. 第二层的全域 E4 映射与非空判据

定义标记集

\[
W_\Delta=
\left\{(a_\Delta,b,c)\in\operatorname{Sol}(4,n)\right\}.
\tag{7}
\]

由 (5) 直接得到

\[
\frac1{a'_\Delta}
=\frac{\Delta}{Na_\Delta}
=\frac1{a_\Delta}-\frac CN
=\frac1{a_\Delta}+\frac4p-\frac4n.
\tag{8}
\]

所以

\[
\boxed{
\Phi_\Delta(a_\Delta,b,c)=(a'_\Delta,b,c)}
\tag{9}
\]

是 \(W_\Delta\to\operatorname{Sol}(4,p)\) 的全域映射。它不因
\(W_\Delta\) 可能为空而自动成为归纳边。

第二层非空性仍有一个精确的有限因子判据。令

\[
M=4a_\Delta-n,\qquad S=na_\Delta,\qquad
g=(M,S),\qquad \mu=M/g,\qquad\sigma=S/g.
\tag{10}
\]

则

\[
\boxed{
W_\Delta\ne\varnothing
\iff
\exists z\mid\sigma^2:\ z\equiv-\sigma\pmod\mu.}
\tag{11}
\]

命中时可显式取

\[
b=\frac{\sigma+z}{\mu},
\qquad
c=\frac{\sigma+\sigma^2/z}{\mu}.
\tag{12}
\]

因此“给出 \(\Delta\)”与“证明指定标记集非空”是两个不同层次；关系点
\(\lambda\) 更不能跳过 (4) 和 (11)。

这一参数化还有完整反向。给定目标解

\[
(p\ell,b,c)\in\operatorname{Sol}(4,p),
\qquad H_*=n+4r\ell,
\]

它能保留同一有序尾 \((b,c)\) 回到 \(n\) 当且仅当

\[
\boxed{H_*\mid np\ell.}
\]

必要性来自唯一可能的坐标

\[
a=\frac{np\ell}{H_*}.
\]

反之该整除成立时，\(H_*\mid pn^2\) 也成立，因为
\(pnH_*-4r(np\ell)=pn^2\)。于是唯一恢复

\[
\boxed{
a=\frac{np\ell}{H_*},
\qquad
\Delta=np-4ra=\frac{pn^2}{H_*}.}
\]

目标解的正双尾保证 \(0<\Delta<n^2\)，而
\(N^2/\Delta=N+4rp\ell\)，故恢复出的 \(\Delta\) 确在 (4) 中；代回 (8)
即得源解。若尾对按无序处理，只需再商去 \(b,c\) 的交换。

特别地，对中心 Type I 参数 \(4\ell=pk+1\) 令 \(h=1+rk\)，则反向存在当且仅当

\[
h\mid n^2,
\qquad
h\mid n\ell,
\]

此时 \(\Delta=n^2/h\) 唯一。第一项本身不够：
\((p,n,k,\ell,h)=(73,36,35,639,1296)\) 满足 \(h\mid n^2\)，但
\(n\ell/h=71/4\)，所以这张中心图表不能保尾回拉到给定的 \(n\)。

## 3. 自然 marking 的唯一性

由 (2) 令

\[
H_E=\frac{n^2}{E},
\qquad
\alpha=\frac{nK}{E}.
\tag{13}
\]

第一层精确关系定理给出 \(E\mid n^2\)、\(E\mid nK\)，且 \(E>1\)。不借用
只陈述于 \(R>3\) 的旧自然提升合同，也可直接验证

\[
H_E=N-4r\alpha,
\qquad
\frac{N^2}{H_E}-N=4rpK.
\]

所以 \(0<H_E<n^2\)，两条同余均成立，因而对包括 \(R=3\) 在内的当前定义域都有
\(H_E\in\mathfrak D(p,n)\)。并且

\[
\boxed{
\Delta=H_E
\iff
a_\Delta=\alpha,\qquad a'_\Delta=pK.}
\tag{14}
\]

更强地，若要求保留的双尾仍满足当前图表方程

\[
\frac1b+\frac1c=\frac RK,
\tag{15}
\]

则源方程强制

\[
\frac1a=\frac4n-\frac RK=\frac1\alpha.
\tag{16}
\]

故 \(a=\alpha\)，再由 \(\Delta=N-Ca\) 唯一得到 \(\Delta=H_E\)。所以不存在
保持当前图表双尾的非自然 marking。对 finite-exponent F 状态，(15) 没有正整数双尾，
这一整类标记源仍然为空。

## 4. 非空第二层的完整终端坍缩

素数目标的 D-only 刚性给出

\[
a'_\Delta=p\ell
\tag{17}
\]

的唯一正整数 \(\ell\)。令

\[
\delta=(4\ell-1,p)\in\{1,p\}.
\tag{18}
\]

已有支撑二分证明

\[
\boxed{
\delta=p\iff\Delta\mid n^2.}
\tag{19}
\]

这两支给出无遗漏的终端分类。

### 4.1 \(\Delta\mid n^2\)：中心 Type I

令

\[
h=\frac{n^2}{\Delta},
\qquad
k=\frac{h-1}{r}.
\tag{20}
\]

则

\[
4\ell=pk+1,\qquad
a_\Delta=\frac{n\ell}{h},\qquad
a'_\Delta=p\ell,
\tag{21}
\]

并且所有保留尾都满足

\[
\frac1b+\frac1c=\frac{k}{\ell}.
\tag{22}
\]

所以 \(W_\Delta\ne\varnothing\) 当且仅当图表 \((k,\ell)\) 已有中心 Type I 除子；
命中时 (21)--(22) 已是原 \(p\) 的直接 Type I 终端。它可以相对当前
\((R,K,E)\) 为“非自然”，但没有产生新的递归类型。

### 4.2 \(\Delta\nmid n^2\)：直接 Type II

此时 (19) 给出

\[
p\nmid4\ell-1.
\tag{23}
\]

若 \((a_\Delta,b,c)\in W_\Delta\)，目标解为

\[
\frac4p=\frac1{p\ell}+\frac1b+\frac1c.
\tag{24}
\]

将 (24) 清分母并模 \(p\) 化简，得到

\[
(4\ell-1)bc\equiv0\pmod p.
\tag{25}
\]

由 (23)，至少一个 \(b,c\) 被 \(p\) 整除。二者不可能同时被 \(p\) 整除；否则
连同 \(p\ell\) 写成 \(p\) 倍数并把 (24) 乘以 \(p\)，右边三个正单位分数之和
至多为 \(3<4\)。因此恰有一个尾分母不被 \(p\) 整除。

把该分母记为 \(x\)，另一个写成 \(py\)，并把 \(p\ell\) 写成 \(pz\)。将 (24)
乘以 \(p\) 得

\[
4=\frac p x+\frac1y+\frac1z.
\]

正性先给出 \(x>p/4\)；又因 \(1/y+1/z\le2\)，有 \(x\le p/2\)，而 \(p\) 为
奇数，等号不可能。因此

\[
\frac p4<x<\frac p2.
\tag{26}
\]

令

\[
m=4x-p.
\tag{27}
\]

核心同余给出 \(m\equiv3\pmod4\) 且 \(3\le m\le p-2\)。从 (24) 得

\[
\frac1y+\frac1z=\frac mx,
\qquad
(my-x)(mz-x)=x^2.
\tag{28}
\]

又因 \(1/y<m/x\) 且 \(1/z<m/x\)，两个配对因子都严格为正。取其中较小者
\(d\)，便有

\[
d\mid x^2,\qquad d\le x,\qquad d\equiv-x\pmod m.
\tag{29}
\]

这正是缺口 \(m\) 的 Type II 除子证书。因此

\[
\boxed{
W_\Delta\ne\varnothing
\Longrightarrow
\begin{cases}
\text{直接中心 Type I},&\Delta\mid n^2,\\
\text{直接 Type II},&\Delta\nmid n^2.
\end{cases}}
\tag{30}
\]

式 (30) 分类的是“第二层一旦非空”的输出。后续全域定理现已证明，对本卡的核心素数，

\[
\boxed{
\Delta\nmid n^2
\Longrightarrow
W_\Delta=\varnothing.}
\tag{30a}
\]

原因是任意 non-source 非空项都被 Vieta 极小下降强制到
\(p\equiv7\pmod8\)、\(n=p-1\) 的负 Pell 族，与核心同余矛盾。见
[non-source D-only 的负 Pell 全分类](two-denominator-lift-nonsource-pell-terminal-classification.md)。
所以 (30) 的 Type II 行在核心域只是严格的条件分类，其前件由 (30a) 恒假。

## 5. 一个真正非自然的 E4 正例

取

\[
(p,R,K)=(433,15,1624),
\qquad K=2^3\cdot7\cdot29.
\tag{31}
\]

关系点 \(\lambda=(-1,-1,-1)\) 给出

\[
E=16,\qquad n=432,\qquad H_E=11664.
\tag{32}
\]

第二层另有

\[
\Delta=2916=H_E/4\ne H_E.
\tag{33}
\]

它恢复

\[
a_\Delta=46035,\qquad
a'_\Delta=2953060=433\cdot6820,
\tag{34}
\]

并且 (11) 命中，显式给出

\[
\frac4{432}
=\frac1{46035}+\frac1{110}+\frac1{6820}
\longmapsto
\frac4{433}
=\frac1{2953060}+\frac1{110}+\frac1{6820}.
\tag{35}
\]

这是相对自然坐标 \(H_E\) 的真正非自然全域 marking。可是

\[
h=64,\qquad k=63,\qquad\ell=6820,\qquad4\ell=433k+1,
\tag{36}
\]

所以它严格属于 (30) 的中心 Type I 分支，而不是新的递降类型。

纯 Type I 的代数分类不能无条件扩展到所有奇素数 D-only 参数。域外控制

\[
(p,n,\Delta)=(7,6,14)
\tag{37}
\]

给出

\[
(7,2,42)\longmapsto(21,2,42),
\tag{38}
\]

其中 \(\Delta\nmid n^2\)、\(4(a'/p)-1=11\) 不被 \(p\) 整除；目标恰有两个
\(p\)-整除分母。这是否定“所有 D-only 参数都无条件归入纯 Type I”的严格域外
代数控制。负 Pell 全分类现在说明它不是偶然反例，而是全部 non-source 正例的第一项；
同时它证明核心专门域中 \(\Delta\nmid n^2\) 的 marked fiber 全部为空。

## 6. 关系点不保证非自然第二层候选

仍在 (31) 中，取二进外层关系

\[
\lambda=(-4,0,0).
\tag{39}
\]

则

\[
E=n=406,\qquad H_E=406,\qquad
N=175798=2\cdot7\cdot29\cdot433,\qquad C=108.
\tag{40}
\]

对任意 \(\Delta\in\mathfrak D(433,406)\)，第一同余强制
\(v_2(\Delta)=1\)。除以 \(2\) 后模 \(54\)，在
\(7^b29^c433^d\) 的九个 \((b,c)\in\{0,1,2\}^2\) 剩余中，只有
\(b=c=1\) 命中 \(41\)。所以

\[
\Delta=406\cdot433^d.
\tag{41}
\]

\(d=1\) 已使 \(\Delta>n^2\)，故

\[
\boxed{\mathfrak D(433,406)=\{406\}.}
\tag{42}
\]

该关系点只有自然 D-only 坐标。由此不能对任意给定的
\(\lambda\in\mathcal D_K\) 推出其对应的
\(\mathfrak D(p,n)\setminus\{H_E\}\ne\varnothing\)，更不能推出任一非自然
\(W_\Delta\) 非空；同一原图表中另一个关系点有非自然候选，并不改变这个逐点反例。

## 7. 对统一选择器的含义

广义 \(2^j\) 的第一层容量已经全部压缩到 \(\mathcal D_K\)，且 \(j>1\) 不增加
算术结果。本定理又把“为每个关系点再做有限 D-only marking 搜索”精确压缩成：

1. (4) 可能只有自然候选；
2. 候选存在仍可能有 \(W_\Delta=\varnothing\)；
3. 一旦通过 (11) 显式证明非空，输出已经是 Type I 或 Type II 终端。

结合 (30a)，核心第二层搜索只需保留 source-supported 的中心 Type I 去重检查；
non-source 候选应直接标为 `rejected_branch`，不再执行三目标或递归非空性搜索。
真正仍可能推进归纳的方向必须改变两个保留尾、替换坐标或既约尾比；继续扩展 \(j\)、
重复自然 marking 或增加 D-only 因子预算都没有增量。
