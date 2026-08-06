---
kind: claim
claim_id: type-II-hall-bundle-target-residue-fourier-gate
title: Type II Hall 源块束的目标残数—Fourier 前置门
statement: 对固定模数 M=4D 和一组保持来源标签的 q 进块，有限乘积残数集若含 -1，则任选命中指数进入同模数—降模—raw 算术闭合三分；若不含 -1，则在 Z/MZ 上有规范的非平凡 Fourier 能量证书，且每个频率先通过有限群指数阶筛和源关系 SNF 才能回译为 F/G 对偶。该门把 Hall 匹配后的“目标残数未命中”与 Type II 算术提升严格分开。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-raw-divisor-residue-fourier-certificate
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-source-fiber-shared-q-ledger
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
  - type-II
  - Hall
  - target-residue
  - Fourier
  - source-block
  - SNF
  - q-adic
  - dual-certificate
sources:
  - claim: type-II-hall-fiber-arithmetic-closure-trichotomy
    role: hit-to-arithmetic-trichotomy
  - claim: type-II-raw-divisor-residue-fourier-certificate
    role: finite-anchored-Fourier-template
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: source-character-lift
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-deduplication
visibility: public
last_checked: '2026-08-05'
---

# Type II Hall 源块束的目标残数—Fourier 前置门

## 1. 源块束和有限乘积集

固定 \(M=4D\)，并取互异奇素数 \(q_i\nmid M\) 及来源标签 \(a_i\)，满足
\[
q_i^{e_i}\mid p+4Da_i,\qquad e_i\ge1.
\]
同一 q 的多来源先按 shared-q ledger 合并为一个总层数；否则下面的指数向量会
重复计费。对一组已由 Hall 匹配选出的块，定义
\[
\mathcal P_{\mathcal B}
=\left\{\prod_{i=1}^{r}q_i^{z_i}\pmod M:
0\le z_i\le d_i\right\}
\subseteq \mathbb Z/M\mathbb Z,
\tag{1}
\]
其中 \(d_i\le e_i\) 是实际可用层数，且 \(d_i\) 已满足候选整数的 q-height
共同账本。
目标残数为 \(t=-1\pmod M\)。

## 2. 命中分支进入算术闭合

若
\[
t\in\mathcal P_{\mathcal B},
\]
选择一个指数向量 \(z=(z_1,\ldots,z_r)\) 实现它，并令
\[
h=\prod_iq_i^{z_i}.
\]
去掉 \(z_i=0\) 的空块后，剩余因子两两互素，且
\[
h\equiv-1\pmod{4D},\qquad h_i=q_i^{z_i}\mid p+4Da_i.
\]
因此 \(h\) 满足带来源混合因子的输入条件，直接进入
[Type II Hall 混合因子的同模数—降模—raw 算术闭合三分](../claims/type-II-hall-fiber-arithmetic-closure-trichotomy.md)：
同模数、严格除子格或 raw 候选给出 Type II，三类全空给出
ALL_ARITHMETIC_LIFT_EMPTY。
这里的结论只对选中的 \(h\) 成立；不能因为乘积集命中就跳过来源标签和算术门。

## 3. 未命中分支的规范 Fourier 证书

若
\[
t\notin\mathcal P_{\mathcal B},
\]
在加法群 \(G_M=\mathbb Z/M\mathbb Z\) 上定义
\[
f=1_{\mathcal P_{\mathcal B}}-\delta_t.
\tag{2}
\]
支持不相交，故
\[
\widehat f(0)=|\mathcal P_{\mathcal B}|-1,
\qquad
\sum_{j=0}^{M-1}|\widehat f(j)|^2
=M\bigl(|\mathcal P_{\mathcal B}|+1\bigr).
\]
因此非平凡频率的总能量为
\[
\boxed{
\sum_{j=1}^{M-1}|\widehat f(j)|^2
=M\bigl(|\mathcal P_{\mathcal B}|+1\bigr)
-\bigl(|\mathcal P_{\mathcal B}|-1\bigr)^2>0.
}
\tag{3}
\]
于是取使幅度最大的最小 \(j_*\in\{1,\ldots,M-1\}\)，得到规范证书
\[
\boxed{
|\widehat f(j_*)|
\ge
\sqrt{\frac{
M(|\mathcal P_{\mathcal B}|+1)
-\bigl(|\mathcal P_{\mathcal B}|-1\bigr)^2
}{M-1}}.
}
\tag{4}
\]
其中
\[
\widehat f(j)
=\sum_{x\in\mathcal P_{\mathcal B}}
e^{-2\pi ijx/M}
-e^{-2\pi ijt/M}.
\]
式 (3) 是纯有限群恒等式，不把 Fourier 幅度误写成 Type II 命中。

## 4. 从参数 Fourier 到真实 F/G 角色

频率 \(j_*\) 首先只是 \(G_M\) 上的加法角色。若真实源关系商为有限阿贝尔群
\(H\)，其指数为 \(E\)，则可提升的必要阶条件是
\[
\frac M{\gcd(M,j_*)}\mid E.
\tag{5}
\]
若 (5) 失败，输出 LIFT_OBSTRUCTED；若 (5) 通过，仍须用有限阿贝尔 SNF 检查
源关系和锚点的仿射相容性。通过时，角色才可送入 F/G 的 Fourier、相位胞或
q-height 容量接口；失败时保留 SOURCE_RELATION_FOURIER/LIFT_OBSTRUCTED，不计
入乘法 Kneser 容量。

因此源块束的完整前置分派是：

1. \(-1\in\mathcal P_{\mathcal B}\)：进入 arithmetic closure trichotomy；
2. \(-1\notin\mathcal P_{\mathcal B}\) 且某个规范频率通过阶筛与 SNF：
   得到 F/G 参数对偶证书；
3. 所有规范频率均不可提升：得到有限 Fourier/LIFT_OBSTRUCTED 回执，转交其它
   Type I/II 射线或良基递降。

## 5. 指数阶筛后的精确能量

令真实源关系商 \(H\) 的指数为 \(E\)，并令
\[
e=\gcd(M,E),\qquad \pi_e:\mathbb Z/M\mathbb Z\to\mathbb Z/e\mathbb Z.
\]
把乘积集投影到 \(\mathbb Z/e\mathbb Z\)，定义重数
\[
m(y)=\#\{x\in\mathcal P_{\mathcal B}:\pi_e(x)=y\},
\qquad
g_e(y)=m(y)-\mathbf 1_{y=\pi_e(t)}.
\tag{6}
\]
所有阶整除 \(E\) 的参数角色恰是 \(\mathbb Z/e\mathbb Z\) 上角色的拉回。对
\(g_e\) 应用 Parseval，得到这些可容许频率的精确非平凡能量
\[
\boxed{
\sum_{\substack{\xi\in\widehat{\mathbb Z/e\mathbb Z}\\ \xi\ne1}}
|\widehat{g_e}(\xi)|^2
=e\sum_y|g_e(y)|^2-\bigl(|\mathcal P_{\mathcal B}|-1\bigr)^2.
}
\tag{7}
\]
因此右端为正时，至少存在一个通过指数阶筛的非平凡频率；它仍需经过源关系
SNF。右端为零时，所有当前源群允许的非平凡角色都看不见这个残数洞，继续枚举
同一源群角色不会增加对偶信息，必须转向另一条 Type I/II 射线或良基递降。

更精确地，右端为零当且仅当 \(g_e\) 在 \(\mathbb Z/e\mathbb Z\) 上为常数，即存在
整数 \(c=(|\mathcal P_{\mathcal B}|-1)/e\) 使
\[
m(y)=c+\mathbf 1_{y=\pi_e(t)}
\qquad\text{对所有 }y\in\mathbb Z/e\mathbb Z.
\tag{8}
\]
这说明零能量不是“尚未找到正确频率”，而是当前源群的全部允许角色都无法区分
源块束和目标投影。任何锚点分离角色若仍存在，必来自更大的环境商或不同的
稳定子纤维，不能冒充当前源关系角色。

## 6. 边界样例

在 \(p=97,D=6,M=24\) 的单状态块
\[
\mathcal P_{\mathcal B}=\{1,11\}
\]
中，目标 \(t=23\) 缺失。故 (3) 的非平凡能量为
\[
24(2+1)-(2-1)^2=71,
\]
存在一个非平凡加法 Fourier 频率。若把该频率解释到 \(U(24)\)，群指数为 2，
而非平凡加法频率的角色阶为 \(24/\gcd(24,j)\)，可能为阶 2、3、4、6、8、12 或 24；
指数阶筛只保留 \(j=12\)，而该频率的系数仍需通过源关系 SNF。这个状态不能因为另一条状态有
残数 13 就把 \(11\cdot13\) 直接池化；那是单纤维实现门排除的伪命中。
在这里 \(e=\gcd(24,2)=2\)，投影重数为 \(m(0)=0,m(1)=2\)，故 (7) 的可容许
非平凡能量为 \(2(1^2)-1^2=1\)，确实留下 \(j=12\) 这一阶 2 候选。

最小零能量边界是 \(M=4\)、源块束 \(\mathcal P_{\mathcal B}=\{1\}\)、目标
\(t=3\)，取 \(E=2\) 时 \(e=2\)，有 \(m(0)=0,m(1)=1\)，于是 \(g_e=0\)。
当前源群的非平凡角色完全不可见；环境群 \(U(4)\) 仍可用角色把 1 与 3 分开，
但那已经是锚点外置/环境商证书，不是该源群的可提升 Fourier。

## 研究边界

该前置门完成了 Hall 源块束的“残数命中 / Fourier 空洞”二分，并把阶筛后的
可容许频率进一步量化；正能量保证至少有一个候选，零能量则给出源群角色的完备
不可见证书和常数背景等价式。它仍不证明某个可提升频率一定造成容量超载，也不把
LIFT_OBSTRUCTED 自动升级为严格递降；这两个出口仍是全局 HC 的待证部分。
