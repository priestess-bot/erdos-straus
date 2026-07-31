---
kind: claim
claim_id: type-I-formal-single-external-smith-parity-selector
title: 一层周期单外部行的 Smith 奇偶选择器与容量边界
statement: 在形式周期的奇次节点组合问题中，若 K 外恰有一个非零素数行，其节点指数为 e_i，令 g=gcd_i|e_i|、f_i=e_i/g，则存在整数 c_i 使 sum c_i e_i=0 且 sum c_i 为奇数，当且仅当并非所有 f_i 都是奇数。等价地，一行 Smith 不变量 gcd(e_i-e_0,2e_0) 在全奇时为 2g，否则为 g。因此全奇恰给出 MISS_EXTERNAL；混合奇偶只排除 MISS_EXTERNAL，仍可能是 MISS_CAPACITY。完整 m=1 超高图的同标号非自环周期会在标号行产生相邻高度 r,r-1；若该标号是唯一 K 外素数便必可消去外部行。p=178513、R=183 的外部 13 三周期精确落在 MISS_CAPACITY，并在周期外由内部缺口 7 的 Type II 证书终端。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-formal-cycle-representation-lattice-capacity
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-formal-target-pair-descent-cycle-boundary
  - internal-support-gap-residue-pullback
  - type-I-f-psi-one-nearest-fiber-escape-boundary
topics:
  - type-I
  - formal-cycle
  - representation-lattice
  - Smith-normal-form
  - parity
  - external-support
  - MISS_EXTERNAL
  - MISS_CAPACITY
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-formal-cycle-representation-lattice-capacity
    role: odd-coset-and-capacity-criterion
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: complete-formal-cycle-setting
  - claim: internal-support-gap-residue-pullback
    role: independent-direct-terminal
visibility: public
last_checked: '2026-07-31'
---

# 一层周期单外部行的 Smith 奇偶选择器与容量边界

## 1. 单外部行的充要条件

沿用周期表示格的记号。周期节点定向为指数向量 \(z_0,\ldots,z_{r-1}\)，要进入原
\(K\) 支撑盒，首先必须用奇数次节点组合消去全部 \(K\) 外坐标。假设外部部分恰有一个
非零素数行，其节点指数为

\[
e_0,e_1,\ldots,e_{r-1}\in\mathbb Z,
\qquad
(e_0,\ldots,e_{r-1})\ne0.
\tag{1}
\]

改变单个节点的方向只把相应 \(e_i\) 与组合系数同时改号，不影响下面的奇偶判据。令

\[
g=\gcd_i|e_i|,
\qquad
f_i=\frac{e_i}{g}.
\tag{2}
\]

则

\[
\boxed{
\exists c_i\in\mathbb Z:
\sum_i c_ie_i=0,
\quad
\sum_i c_i\equiv1\pmod2
\iff
\text{并非所有 }f_i\text{ 都是奇数}.}
\tag{3}
\]

若全部 \(f_i\) 为奇数，把外部消元式模 2 化简便有

\[
0\equiv\sum_i c_if_i\equiv\sum_i c_i\pmod2,
\]

与奇次要求矛盾。反之，因 \(\gcd_i f_i=1\)，只要不全为奇数，就同时存在偶数
\(f_a\) 与奇数 \(f_b\)。取

\[
c_a=f_b,
\qquad
c_b=-f_a,
\qquad
c_i=0\quad(i\ne a,b),
\tag{4}
\]

便有 \(\sum c_if_i=0\)，而系数和为奇数。这还给出只用两个节点的显式外部消元器。

## 2. 一行 Smith 不变量

周期关系格可用列

\[
e_i-e_0\quad(1\le i<r),
\qquad
2e_0
\tag{5}
\]

描述外部行。其唯一非零 Smith 不变量为

\[
s=\gcd(e_1-e_0,\ldots,e_{r-1}-e_0,2e_0).
\tag{6}
\]

除以 \(g\) 后，若所有 \(f_i\) 为奇数，(6) 中每项均为偶数，而归一化向量的最大公因子
为 1，故 \(s=2g\)。若奇偶混合，某个差为奇数，故 \(s=g\)。于是

\[
s=
\begin{cases}
2g,&f_i\text{ 全奇},\\
g,&f_i\text{ 奇偶混合}.
\end{cases}
\tag{7}
\]

目标外部坐标是 \(e_0\)。全奇时 \(2g\nmid e_0\)，恰为 `MISS_EXTERNAL`；混合时
\(g\mid e_0\)，外部方程可解。因此 (3) 与完整 Smith 判定严格一致。

必须保留第二阶段：外部方程可解只说明状态不是 `MISS_EXTERNAL`，消元后的内部向量
还要落入 \(K\) 的指数容量盒。它仍可能是 `MISS_CAPACITY`，并不自动给出 Type I。

## 3. 同一边标号周期的两节点消元器

考虑完整 \(m=1\) 超高形式图中的周期，并假设每条边都标记同一素数 \(\ell\)。把每条
边所选坐标的 \(\ell\)-进高度记为 \(h_i>0\)。不取补数时下一高度为 \(h_i-1\)；取
补数时，由 \(\ell\nmid R\) 可知要使下一条边仍标 \(\ell\)，必须有 \(h_i=1\)。

闭环必含取补边，故某个高度等于 1，进而 \(\gcd_i h_i=1\)。非自环周期不可能全部
取补，因此还含一条不取补边，并出现相邻高度

\[
r,\quad r-1.
\tag{8}
\]

对这两个节点取系数

\[
r-1,\quad-r,
\tag{9}
\]

便消去 \(\ell\) 行，且系数和为 \(-1\)。若所有边都取补，仿射压缩映射
\(u\mapsto R-u/\ell\) 只能有固定点；在 \(R\) 为奇数、节点互素的核心范围内，唯一
可能是

\[
(R,\ell)=(3,2),
\qquad
\{1,2\}\to\{1,2\}.
\tag{10}
\]

所以同标号非自环周期的标号行总可由 (9) 消去。只有在 \(\ell\) 还是周期中唯一的
\(K\) 外素数时，这才排除完整 `MISS_EXTERNAL`；其它外部素数行仍须联合消元。

这个唯一性限制不能删去。对

\[
(p,R,K)=(73,11,201),
\qquad
K=3\cdot67,
\tag{11}
\]

完整图有纯标号 2 的五周期

\[
\{1,10\}\to\{5,6\}\to\{3,8\}\to
\{4,7\}\to\{2,9\}\to\{1,10\}.
\tag{12}
\]

按节点顺序，其三个外部素数行是

\[
\begin{aligned}
v_2&=(1,1,3,2,1),\\
v_5&=(1,-1,0,0,0),\\
v_7&=(0,0,0,-1,0).
\end{aligned}
\tag{13}
\]

\(v_2\) 单行满足 (3)，但三行联立的任意零组合都有偶系数和，因此整个周期仍为
`MISS_EXTERNAL`。

## 4. \(p=178513\) 的精确 `MISS_CAPACITY` 边界

取

\[
p=178513,
\qquad
R=183,
\qquad
K=8166970=2\cdot5\cdot7\cdot17\cdot6863.
\tag{14}
\]

\(p\) 为 \(1\pmod{24}\) 素数，且 \(4K=pR+1\)。模 61 以 2 为原根时，五个
\(K\)-素数的离散对数为

\[
(1,22,49,47,59),
\tag{15}
\]

而目标 \(-1\) 的对数为 30。式 (15) 的 \(\{-1,0,1\}^5\) 组合不能得到 30，故中心
盒 miss。完整一层壳恰有四个指数向量

\[
\begin{aligned}
&(-1,1,-2,1,0),\qquad(1,-1,2,-1,0),\\
&(0,1,-2,1,1),\qquad(0,-1,2,-1,-1).
\end{aligned}
\tag{16}
\]

其中 \(85/98\) 只是规范见证之一，不是唯一见证。由它先作内部标号 7 的形式迁移，
可达节点 \(\{14,169\}\)，并进入纯外部标号 13 的三周期

\[
\{14,169\}\to\{13,170\}\to\{1,182\}\to\{14,169\}.
\tag{17}
\]

按素数环境 \((2,5,7,13,17,6863)\) 定向，三个节点向量为

\[
\begin{aligned}
z_0&=(1,0,1,-2,0,0),\\
z_1&=(-1,-1,0,1,-1,0),\\
z_2&=(-1,0,-1,-1,0,0).
\end{aligned}
\tag{18}

唯一外部 13 行的绝对高度为 \((2,1,1)\)，所以 (3) 排除 `MISS_EXTERNAL`。以
\(z_1-z_0,z_2-z_0,2z_0\) 为关系列，外部行是

\[
(3,1,-4),
\]

其消元方程为

\[
3t_1+t_2-4t_*=2.
\tag{19}
\]

写 \(t_1=s,t_*=u,t_2=2-3s+4u\)，消去 13 后的内部坐标
\((2,5,7,17,6863)\) 为

\[
(4s-6u-3,-s,5s-6u-3,-s,0).
\tag{20}
\]

\(K\) 平方自由，容量盒为 \([-1,1]^5\)。由第二、四坐标得 \(s\in\{-1,0,1\}\)：
\(s=0\) 时第一坐标不可能入盒；\(s=1\) 时第一坐标迫使 \(u=0\)，第三坐标为 2；
\(s=-1\) 时第一坐标迫使 \(u=-1\)，第三坐标为 \(-2\)。所以 (20) 与容量盒无交，
严格分类为

\[
\boxed{\texttt{MISS_CAPACITY}.}
\tag{21}
\]

最近的外部消元组合是

\[
z_0+z_1-z_2=(1,-1,2,0,-1,0),
\tag{22}
\]

唯一超界坐标正是 \(v_7=2\)。同一原始图还有周期

\[
\{85,98\}\xrightarrow7\{14,169\}
\xrightarrow{13}\{13,170\}
\xrightarrow2\{85,98\},
\tag{23}
\]

其三条边依次是内部严格缺陷、外部严格缺陷和 \(K\) 容量内边；所以 (17) 只是完整
SCC 的一个子周期。

## 5. 周期外的直接终端不改变格分类

式 (22) 指向内部缺口 7。取

\[
x=44630,
\qquad
d=2,
\tag{24}
\]

则 \(d\mid x^2\)、\(d\le x\)，且 \(4dR\equiv1\pmod7\)。内部缺口拉回定理给出

\[
\boxed{
\frac4{178513}
=\frac1{44630}
+\frac1{1138198888}
+\frac1{25398908185720}.}
\tag{25}
\]

同一缺口另有 Type I 除子 \(d=5\)；按仓库的逐除子顺序，较小的 \(d=2\) Type II
先被选中。式 (25) 是独立的 `terminal-first` 叶，不会把 (17) 的表示格分类从
`MISS_CAPACITY` 改成 `HIT`，也没有把形式周期升级为合法递降。

## 6. 复现入口与证明边界

聚焦复现器与结果文件为

```text
reproductions/type_i_internal_support_gap_single_external_selector.py
reproductions/type-i-internal-support-gap-single-external-selector-results.json
```

脚本锁定 (14)--(25)、完整四见证壳以及 (11)--(13) 的多外部反例。式 (3)、(7) 与
同标号周期推论是整数证明；实例计算只用于可重放核验。

本卡没有证明每个周期只有一个外部行，也没有控制消元后的内部容量。它提供的是周期
选择器中的精确第一阶段：全奇高度立即给出 `MISS_EXTERNAL`；混合高度进入容量判定；
容量失败后仍须使用周期外 Type I/II、跨模数中心谱或满足 E1--E5 的合法 support switch。
