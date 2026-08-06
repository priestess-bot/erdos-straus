---
kind: claim
claim_id: type-II-weighted-source-saturated-quotient-kernel-dispatch
title: Type II 带权源饱和幂块的严格商缺失—核 Fourier 分派
statement: 设有限阿贝尔源群 G 的积集 P 含有幂块 B={1,g,...,g^e}，并取商 pi:G->Q。若 H=<pi(g)> 的阶为 o 且 e>=o-1，则 pi(P)H=pi(P)。对缺失目标 t not in P，令 K=pi^{-1}(H) 和 rho:Q->Q/H，则必有二分：若 rho(pi(t)) 不在 rho(pi(P))，得到严格较小商 G/K 中的目标缺失；若其在商像中，则目标核截面 S_t={k in K:tk in P} 是非空真子集，并给出精确非平凡 Fourier 能量 |S_t|(|K|-|S_t|)。因此饱和幂块的非零来源重数角色不能悬空：要么进入可提升的商递降门，要么进入核 Fourier；要升级为 E1--E5 降模边还必须通过来源标签参数纤维、同余稳定子和整数回译，且 h_S=-1 (mod 4D') 的子列表应先作为直接 Type II 终端；否则抽象商的算术提升失败仍必须标记为 LIFT_OBSTRUCTED。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-qheight-fourier-set-vs-multiplicity-saturation-boundary
  - type-II-stabilizer-kernel-failure-dual-certificate
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-same-modulus-source-switch-crt-criterion
topics:
- type-II
- weighted-source
- saturated-block
- quotient-descent
- kernel-fourier
- Parseval
- source-switch
- lift-obstruction
- proof-program
sources:
  - claim: type-II-qheight-fourier-set-vs-multiplicity-saturation-boundary
    role: set-versus-multiplicity-saturation-input
  - claim: type-II-stabilizer-kernel-failure-dual-certificate
    role: kernel-fourier-energy
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: source-relation-lift-gate
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: arithmetic-quotient-lift-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II 带权源饱和幂块的严格商缺失—核 Fourier 分派

## 1. 饱和块给出的不变性

令 \(G\) 为有限阿贝尔群，\(P\subseteq G\) 为同一来源纤维中的源积集，并假设
其中一个来源块为

\[
B=\{1,g,g^2,\ldots,g^e\}.
\tag{1}
\]

取群满射 \(\pi:G\to Q\)，令

\[
\bar g=\pi(g),\qquad
H=\langle\bar g\rangle,\qquad
o=|H|.
\tag{2}
\]

若 \(e\ge o-1\)，则

\[
\pi(B)=\{1,\bar g,\ldots,\bar g^{\,o-1}\}=H.
\tag{3}
\]

把 \(P\) 写成 \(P=P_0BP_1\)（允许 \(P_0\) 或 \(P_1\) 为空），则在阿贝尔商群
\(Q\) 中

\[
\pi(P)=\pi(P_0)\,H\,\pi(P_1),
\qquad
\pi(P)H=\pi(P).
\tag{4}
\]

所以饱和块不只是让一个重数 Fourier 系数出现余段；它使整个源集合像对
\(H\) 平移不变。

## 2. 严格商缺失—核截面二分

令

\[
K=\pi^{-1}(H)\le G,
\qquad
\rho:Q\longrightarrow Q/H
\tag{5}
\]

为自然商映射，并固定目标 \(t\notin P\)。考虑目标在严格商中的像
\(\rho(\pi(t))\)。

### 分支 A：严格较小商缺失

若

\[
\rho(\pi(t))\notin\rho(\pi(P)),
\tag{6}
\]

则目标在 \(G/K\) 中缺失。只要 \(H\ne1\)，有

\[
|G/K|=|Q/H|<|Q|,
\tag{7}
\]

所以这是一个严格较小的有限群商。其证书可记录为

\[
\mathrm{SATURATED\_QUOTIENT\_MISS}
=(G,K,\rho,\pi(P),\pi(t)).
\tag{8}
\]

若 \(G,Q\) 来自 Type II 单位群和合法 source-switch，且该商可回译为
较小 \(D'\) 或较小模数，则 (8) 进入严格可提升递降候选；若没有整数坐标、
来源标签或 \(E1\)--\(E5\)，只能记录
ARITHMETIC_QUOTIENT_LIFT_OBSTRUCTED，不能把抽象群商直接当作素数递降。

### 分支 B：目标核截面

若

\[
\rho(\pi(t))\in\rho(\pi(P)),
\tag{9}
\]

则存在 \(x\in P\) 使

\[
\pi(x)\in\pi(t)H.
\tag{10}
\]

等价地，存在 \(k=x\,t^{-1}\in K\) 满足 \(tk=x\in P\)。定义目标核截面

\[
S_t=\{k\in K:tk\in P\}.
\tag{11}
\]

由 (10) 有 \(S_t\ne\varnothing\)；又因 \(t\notin P\)，有 \(1\notin S_t\)。因此

\[
\varnothing\ne S_t\subsetneq K.
\tag{12}
\]

对 \(K\) 的 Fourier 变换，Parseval 给出精确能量

\[
\boxed{
\sum_{\substack{\psi\in\widehat K\\\psi\ne1}}
\left|\sum_{k\in S_t}\overline{\psi(k)}\right|^2
=|S_t|(|K|-|S_t|)>0.
}
\tag{13}
\]

故分支 B 输出

\[
\mathrm{SATURATED\_KERNEL\_SPLIT}
=(K,S_t,\text{非平凡角色}).
\tag{14}
\]

若要把 (13) 回译成原始单位群的目标截面 Fourier，还必须通过真实碰撞商、
源关系格锚点相容性和 arithmetic source-switch；任何失败都保留
LIFT_OBSTRUCTED，而不是把 (13) 当作整数 Type II 证书。

## 3. 与 WEIGHTED_SOURCE_ONLY 的接线

若选定的 \(\pi\) 就是角色商（或至少满足
\(o=\operatorname{ord}(\bar g)=d=\operatorname{ord}(\chi(\bar g))\)），令
\(d=\operatorname{ord}(\chi(\bar g))\)。当 \(e\ge d-1\) 时，前一分流把该块标记为
集合饱和；即便
\((e+1)\bmod d\ne0\) 使带来源重数 Fourier 非零，式 (4) 仍成立，只能采用上面的
商缺失—核截面二分：

1. 若 (6) 成立，非零重数角色不能作为集合容量，必须尝试
   SATURATED_QUOTIENT_MISS 的整数提升；
2. 若 (9) 成立，非零角色由 SATURATED_KERNEL_SPLIT 的截面能量承接；
3. 若两种承接都不能通过源关系和算术提升门，输出显式
   ARITHMETIC_QUOTIENT_LIFT_OBSTRUCTED 或
   KERNEL_SOURCE_RELATION_LIFT_OBSTRUCTED。

这说明饱和带权角色不会产生未分类的第三种“抽象容量”出口。

## 4. 最小例子

下面用加法记号给出两个分支的最小实例。分支 A 取
\(G=C_8\)、\(\pi=\operatorname{id}\)、\(B=\{0,4\}\)、\(P=B\)、\(t=1\)。
此时 \(H=\{0,4\}\)、\(K=H\)、\(G/K\simeq C_4\)，且目标在严格商中缺失。
分支 B 取 \(\pi:C_8\to C_4\) 为模 4 投影，\(B=\{0,2\}\)（所以
\(H=\{0,2\}\)）、再令 \(P=\{1,3\}\)、\(t=5\)。这里
\(\pi(P)=\{1,3\}\) 在 \(H\) 下不变，目标在 \(C_4/H\) 中命中，但
\(t\notin P\)；于是 \(K=\{0,2,4,6\}\)，
\(S_t=\{4,6\}\) 是非空真核截面，式 (13) 给出非零 Fourier 能量。

在角色 \(\chi(g)=-1\)、\(e=2\) 的带权例中，来源重数系数为
\(1-1+1=1\)，但集合商块 Fourier 为零；本定理把它送入上述两个集合级出口，
而不是把系数 1 解释为新的 Kneser 层。

## 5. 同余核与参数纤维边界

前面的严格商缺失只是有限群层面的结论。要把它登记为较小模数的 Type II
后继，必须同时保留来源标签；一个饱和子群条件本身不能替代这个整数回译。
令

\[
G_*=U(4D_*),\qquad G'=U(4D'),\qquad D'\mid D_*,\qquad
C_{D'}=\ker\bigl(G_*\to\rho_{D'}(G_*)\bigr).
\tag{16}
\]

若饱和块生成的子群为 \(H\le G_*\)，且

\[
(-1)H\cap P=\varnothing,
\qquad C_{D'}\subseteq H,
\tag{17}
\]

则确有

\[
-1\notin\rho_{D'}(P).
\tag{18}
\]

这只是一个容易检查的充分条件：若低模数像命中，则某个
\(x\in P\) 满足 \(x(-1)^{-1}\in C_{D'}\subseteq H\)，与 (17) 矛盾。真正必要的
稳定子条件是 \(C_{D'}\subseteq\operatorname{Stab}(P)\)；它可能成立而
\(C_{D'}\subseteq H\) 不成立，故不能把 (17) 当成一般降模判据。

设保留来源标签的两两互素因子列表为
\(\mathbf h=(h_1,\ldots,h_r)\)。低模数参数纤维门应写成

\[
\mathscr S_{D'}(p;\mathbf h)=
\left\{A:
\begin{array}{l}
A\mid D',\quad D'/A\text{ 平方自由},\quad 4AD'<p,\\
h_i\mid p+4AD'\quad(1\le i\le r)
\end{array}\right\}.
\tag{19}
\]

若原标签来自 \(h_i\mid p+4Da_i\)，则 (19) 等价于
\(AD'\equiv Da_i\pmod{h_i}\)，这是带来源 CRT/source-switch 条件。

必须先处理一个容易混淆的终端：若某个子列表满足

\[
h_S=\prod_{i\in S}h_i\equiv-1\pmod{4D'},
\tag{20}
\]

且 \(A\in\mathscr S_{D'}(p;\mathbf h)\)，则它已经是直接 Type II 证书，
\[
K_S=(h_S+1)/(4D'),\qquad B_S=(K_Sp+A)/h_S,
\tag{21}
\]
不应再被登记为“目标仍缺失”的递降后继。只有在没有这样的直接命中、
\(C_{D'}\subseteq\operatorname{Stab}(P)\)、参数纤维门非空且投影来源标签精确回译时，
才可输出 \(\mathrm{STABILIZER\_CONGRUENCE\_LOWER\_EDGE}\)；此时目标缺失由 (18) 或
稳定子饱和恒等式传递，E1--E3 重新检查，E4 取图表无关的
\(\operatorname{Sol}(p)\) 恒等提升，E5 由预先固定的势

\[
\Phi_{\mathrm{II}}(D',A)=
\bigl(D',A,|\rho_{D'}(G_*)/\operatorname{Stab}(\rho_{D'}(P))|\bigr)
\tag{22}
\]

和 \(D'<D_*\) 支付。

若 \(C_{D'}\not\subseteq\operatorname{Stab}(P)\)，新三分定理给出
\(\mathrm{CONGRUENCE\_KERNEL\_FOURIER}\)，伪命中时再给出目标核截面；若稳定子
包含但 (19) 为空，输出 \(\mathrm{ARITHMETIC\_LIFT\_OBSTRUCTED}\)。因此
\(\mathrm{SATURATED\_QUOTIENT\_MISS}\) 只有在上述参数纤维和 E1--E5 门全部通过后，
才能升级为递降边。

在 \(p=97\)、\(U(24)\to U(4)\)、\(P=\{1,11\}\) 的边界中，
\(H=\{1,11\}\)，而
\(C_1=\{1,5,13,17\}\not\subseteq H\) 且也不包含于
\(\operatorname{Stab}(P)=H\)。因此模 4 的伪命中只能进入核 Fourier/截面分支，
不能被误记为可提升降模边。

## 6. 结论与边界

本定理把 WEIGHTED_SOURCE_ONLY 从“模式警告”提升为一个完整的集合级分派：

\[
\boxed{
\text{饱和块}
\Longrightarrow
\text{严格商缺失}
\ \text{或}\
\text{非空真核截面 Fourier}.
}
\tag{15}
\]

它无条件证明的是有限群层面的严格商/核 Fourier 二分；要成为原猜想要求的
Type II 短证书或严格可提升递降，还必须验证商的整数 source-switch、同余核识别、
来源标签和良基势下降。满足一般稳定子门
\(C_{D'}\subseteq\operatorname{Stab}(P)\)、参数纤维条件 (19)、没有 (20) 的直接
终端且 \(D'<D_*\) 时，三分定理给出一个完整的可提升降模边；否则失败本身有明确
的提升障碍类型，而不再被误记为容量不足。
