---
kind: claim
claim_id: type-II-qheight-fourier-set-vs-multiplicity-saturation-boundary
title: Type II q 进幂块的集合 Fourier 与来源重数 Fourier 饱和分流
statement: 设角色商中源幂块的像阶为 d。若指数高度 e<d-1，幂块集合在角色商中没有碰撞，集合 Fourier 与来源重数 Fourier 一致；若 e>=d-1，幂块集合已经饱和为完整循环子群，其任何非平凡集合 Fourier 系数为零，并且 Kneser 活跃容量最多 d-1。可是来源重数 Fourier 仍等于 (e+1) mod d 的余段几何和，可能在 d 不整除 e+1 时非零。因此饱和分支的非零重数角色只能标记 WEIGHTED_SOURCE_ONLY，不能直接进入无重数目标集合的容量账本；只有通过碰撞去重、真实目标截面或显式带权证书后才可继续。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-box-fourier-full-cycle-phase-deficit
  - type-II-qadic-height-kneser-block-bridge
  - type-II-kernel-fourier-source-relation-compatibility
topics:
- type-II
- q-adic-height
- Fourier
- set-measure
- multiplicity
- Kneser
- saturation
- collision
- proof-boundary
sources:
  - claim: type-II-source-box-fourier-full-cycle-phase-deficit
    role: source-multiplicity-geometric-sum
  - claim: type-II-qadic-height-kneser-block-bridge
    role: saturated-kneser-capacity
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: collision-and-target-section-lift-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II q 进幂块的集合 Fourier 与来源重数 Fourier 饱和分流

## 1. 单幂块的两个 Fourier 对象

令 \(G\) 为有限阿贝尔群，\(g\in G\)，并取指数高度 \(e\ge0\)。令

\[
B_e=\{g^a:0\le a\le e\},
\qquad
\mu_e(x)=\#\{0\le a\le e:g^a=x\}.
\tag{1}
\]

取角色 \(\chi\in\widehat G\)，记

\[
d=\operatorname{ord}(\chi(g)).
\tag{2}
\]

把 \(G\) 投影到 \(\bar G=G/\ker\chi\)。在 \(\bar G\) 中，\(\bar g\) 的阶恰为
\(d\)。于是无重数集合 Fourier 和与带来源重数 Fourier 和分别为

\[
\widehat{1_{\bar B_e}}(\chi)
=\sum_{x\in\bar B_e}\overline{\chi(x)},
\qquad
\widehat{\mu_e}(\chi)
=\sum_{a=0}^{e}\overline{\chi(g)}^{\,a}.
\tag{3}
\]

第二项保留指数碰撞的来源标签，第一项先把相同角色商元素去重；两者只有在
\(e<d-1\) 时必然相同。

## 2. 未饱和分支

若 \(e<d-1\)，则

\[
\bar B_e=\{1,\bar g,\ldots,\bar g^e\}
\tag{4}
\]

包含 \(e+1\) 个不同元素，因而

\[
\widehat{1_{\bar B_e}}(\chi)
=\widehat{\mu_e}(\chi)
=\frac{1-\overline{\chi(g)}^{\,e+1}}
{1-\overline{\chi(g)}}.
\tag{5}
\]

这一分支中的相位余段是实际集合支撑；若再通过目标截面与源关系格的仿射门，
可以把角色送入无重数 Fourier 或 Kneser 容量。

## 3. 饱和分支的集合零与重数残段

若 \(e\ge d-1\)，则角色商中的幂块集合已经绕满循环子群：

\[
\bar B_e=\langle\bar g\rangle,
\qquad
|\bar B_e|=d.
\tag{6}
\]

由于 \(\chi(\bar g)\) 是阶 \(d>1\) 的根，

\[
\boxed{
\widehat{1_{\bar B_e}}(\chi)
=\sum_{a=0}^{d-1}\overline{\chi(g)}^{\,a}=0.
}
\tag{7}
\]

另一方面，带来源重数仍按指数长度分解。令

\[
e+1=md+r,\qquad 0\le r<d,
\tag{8}
\]

则

\[
\boxed{
\widehat{\mu_e}(\chi)
=\sum_{a=0}^{r-1}\overline{\chi(g)}^{\,a}.
}
\tag{9}
\]

当 \(r>0\) 时 (9) 一般非零，即使 (7) 严格为零。原因是每个完整循环在重数
Fourier 中相消，只留下最后一个不完整余段；而无重数集合只保留一个完整循环。

这给出一个严格的集合—重数分流：

\[
\begin{array}{c|c|c}
\text{分支}&\text{无重数集合 Fourier}&\text{来源重数 Fourier}\\
\hline
e<d-1&\text{与重数一致}&\text{余段}\\
e\ge d-1&0&\text{可能非零，取决于 }(e+1)\bmod d
\end{array}
\tag{10}
\]

## 4. 与 Kneser 活跃容量的精确接口

在 \(G/T\) 中令 \(o=\operatorname{ord}(gT)\)。若角色在该商中非平凡且
\(e\ge o-1\)，则幂块集合已经饱和为 \(\langle gT\rangle\)，其 Kneser 活跃容量
恰为

\[
\kappa=\min(e,o-1)=o-1.
\tag{11}
\]

额外的指数高度不再增加无重数目标集合的容量；它只改变来源重数
\((e+1)\bmod d\)，其中 \(d=\operatorname{ord}(\chi(g))\)。因此若
\(d\mid e+1\)，重数角色也由前一引理整周期湮灭；若 \(d\nmid e+1\)，则可能出现

\[
\widehat{\mu_e}(\chi)\ne0,
\qquad
\widehat{1_{\bar B_e}}(\chi)=0,
\qquad
\kappa=o-1.
\tag{12}
\]

式 (12) 是一个不可省略的负边界：非零来源重数角色不能被解释为额外的
Kneser 集合容量。

对多幂块积集 \(P=B_{e_1}\cdots B_{e_r}\)，若第 \(i\) 块在角色商中满足
\(e_i\ge d_i-1\)，则其无重数像包含完整子群
\(\langle\bar g_i\rangle\)。若 \(\chi\) 在该子群上非平凡，任何以无重数
\(1_P\) 定义的 Fourier 系数都因该子群平均而为零；只有带来源的卷积测度
\(\mu_{e_1}*\cdots*\mu_{e_r}\) 仍可能保留余段系数。故多块角色也必须先标明
set-mode 或 weighted-source-mode，不能混用。

## 5. 构造性选择器分派

对每个候选角色和每个源幂块，先计算
\(d_i=\operatorname{ord}(\chi(g_i))\)：

1. 若 \(d_i=1\)，该块对角色不活跃；
2. 若 \(e_i<d_i-1\)，输出 SET_PHASE_REALIZED，集合和重数可在该列合并；
3. 若 \(e_i\ge d_i-1\) 且 \((e_i+1)\bmod d_i=0\)，输出
   FULL_CYCLE_ANNIHILATION，该角色在集合和重数两种模式都删除；
4. 若 \(e_i\ge d_i-1\) 且 \((e_i+1)\bmod d_i\ne0\)，输出
   WEIGHTED_SOURCE_ONLY。此时只能保留带来源重数证书；若目标证明要求
   无重数集合 Fourier 或 Kneser 容量，必须转入饱和稳定子、碰撞去重、另一角色，
   或显式 source-switch/递降。

WEIGHTED_SOURCE_ONLY 不是递降，也不是反例；它是一个精确的证书类型约束，
防止把 (9) 的余段幅度重复计入 (11) 之外的容量。

## 6. 最小反例

取角色商 \(C_4=\langle g\rangle\)，令 \(\chi(g)=i\)。

* \(e=3\) 时，\(B_e=C_4\)，集合 Fourier 为
  \(1-i-1+i=0\)，且 \(e+1=4\) 使重数 Fourier 也为零；
* \(e=4\) 时，仍有 \(B_e=C_4\)，集合 Fourier 仍为零，但重数 Fourier 为
  \(1-i-1+i+1=1\)。

所以 \(e=4\) 是最小的严格分离例：一个非零的来源重数 Fourier 角色，不能作为
无重数目标集合的 Fourier 或额外 Kneser 容量。

## 7. 结论与研究边界

本卡完成了 q-height、Fourier 和 Kneser 之间一个此前缺失的模式判别：

* 未饱和幂块的角色余段可以与实际集合 Fourier 对接；
* 饱和幂块的额外高度只进入稳定子/有限阶关系，不能再次收费；
* 饱和分支仍可能留下非零重数角色，但它必须标为带权来源证书；
* 只有经真实碰撞商、目标截面和 source-switch 验证后，带权角色才可继续寻找
  算术提升或严格递降。

因此，当前决定性缺口被进一步缩小为：对 SET_PHASE_REALIZED 分支证明跨状态
相位胞容量超载，或对 WEIGHTED_SOURCE_ONLY 分支构造保持来源标签的商递降；
不能再用抽象 Fourier 幅度统一覆盖两种模式。
