---
kind: claim
claim_id: type-II-dyadic-relation-subgroup-target-preserving-quotient
title: Type II 二进关系子群的目标保持严格商与算术 Q-lift 门
statement: 对最大二进深度顶位装箱簇生成的非平凡关系子群 R_C，因 R_C 包含于 L_d=2^{d+1}K 且最大深度目标纤维满足 F_t 与 L_d 不相交，商映射 H 到 H/R_C 仍保持目标缺失并严格降低有限群阶；该下降不要求 R_C 已包含于源积集稳定子。把源指数映射沿 R_C 的原像格下降后，任意整数化必须通过有限的目标映射、来源 CRT/SNF、源盒像和 E1–E5 门；通过则得到严格 Q-lifted source-switch，失败则输出带最小门的关系商提升障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-dyadic-target-fiber-packing-cluster-subgroup-capacity
  - type-II-dyadic-target-fiber-max-depth-relay
  - type-II-dyadic-target-fiber-maximal-quotient-dedup
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-source-label-snf-failure-anchor-relation-dichotomy
topics:
  - type-II
  - dyadic
  - relation-subgroup
  - target-preserving-quotient
  - strict-descent
  - source-lattice
  - quotient-lift
  - SNF
  - CRT
  - E1-E5
  - proof-program
sources:
  - claim: type-II-dyadic-target-fiber-packing-cluster-subgroup-capacity
    role: nontrivial-relation-subgroup
  - claim: type-II-dyadic-target-fiber-max-depth-relay
    role: target-fiber-disjoint-layer
  - claim: type-II-dyadic-target-fiber-maximal-quotient-dedup
    role: maximum-target-preserving-layer
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: quotient-descent-dispatch
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: source-lattice-quotient
  - claim: type-II-source-label-snf-failure-anchor-relation-dichotomy
    role: labelled-Q-lift-failure-menu
  - reproduction: reproductions/dyadic_target_fiber_max_depth.py
    role: target-preserving-cluster-quotient-control
visibility: public
last_checked: '2026-08-09'
---

# Type II 二进关系子群的目标保持严格商与算术 Q-lift 门

## 输入状态

令 \(H\) 为有限阿贝尔群，\(K=\langle\kappa\rangle\simeq C_{2^a}\) 为核，\(\phi\)
为源指数同态，\(\mathcal B_\nu\) 为有限对称指数盒，\(S=\phi(\mathcal B_\nu)\) 为
源像集。固定二阶目标 \(t\) 并假设

\[
t\notin S,\qquad
F_t=\{k\in K:t+k\in S\}\ne\varnothing,\qquad
0\notin F_t.
\]

令 \(d\) 是 \(F_t\) 的最大二进深度，且

\[
L_d=2^{d+1}K,\qquad
F_t\cap L_d=\varnothing.
\tag{1}
\]

后一等式是最大深度商引理的目标保持结论。

从一个最大符号装箱簇取出的关系子群满足

\[
1\ne R_C\le L_d.
\tag{2}
\]

这里 \(R_C\) 可以只是源像差分生成的子群，并不假设
\(R_C\le\operatorname{Stab}_H(S)\)。

## 目标保持严格商定理

令

\[
\pi_R:H\longrightarrow Q_R:=H/R_C
\]

为商映射。则

\[
\boxed{
\pi_R(t)\notin\pi_R(S),
\qquad
|Q_R|=|H|/|R_C|<|H|.
}
\tag{3}
\]

因此每个非平凡装箱簇关系子群都给出一个目标保持的严格有限群下降。

### 证明

若 \(\pi_R(t)\in\pi_R(S)\)，则存在 \(s\in S\) 和 \(r\in R_C\) 使

\[
s=t+r.
\]

因为 \(R_C\le L_d\le K\)，这说明 \(r\in F_t\)。但 (1) 给出
\(F_t\cap L_d=\varnothing\)，与 \(r\in R_C\le L_d\) 矛盾。故
\(\pi_R(t)\notin\pi_R(S)\)。有限群 \(H\) 中 \(R_C\ne1\)，所以商阶严格减小。
证毕。

这个证明只使用目标纤维的最大深度分离，不使用积集稳定子。因而它与
“先证明同余核包含于稳定子再降模”的路线不同：关系子群即使未饱和源积集，也能
先产生一个目标保持的有限群商；稳定子只在后续价格计算中决定吸收量。

## 源指数格的精确下降

令

\[
\Lambda=\ker\phi,\qquad
\widetilde R_C=\phi^{-1}(R_C).
\]

则 \(\Lambda\subseteq\widetilde R_C\)，且 \(\pi_R\circ\phi\) 因子化为

\[
\overline\phi:
\mathbb Z^r/\widetilde R_C
\longrightarrow Q_R,
\qquad
[z]\longmapsto\pi_R(\phi(z)).
\tag{4}
\]

源盒在商中的真实像是

\[
\overline S_R
=\overline\phi\bigl((\mathcal B_\nu+\widetilde R_C)/\widetilde R_C\bigr)
=\pi_R(S).
\tag{5}
\]

式 (5) 是源盒像等式，而不是只检查生成子群 \(H\) 的商；它保留了有限指数盒的
范围和来源标签。由 (3)，\(\overline S_R\) 不含 \(\pi_R(t)\)。

因此有限群阶段的严格下降回执可规范写为

\[
\mathrm{DYADIC\_RELATION\_QUOTIENT\_DESCENT}
=
(R_C,\widetilde R_C,Q_R,\overline\phi,\overline S_R,\pi_R(t)).
\tag{6}
\]

## 算术 Q-lift 门

式 (6) 还不是 Erdős--Straus 的整数递降。固定当前整数状态的原始参数 \(D\)、核心素数
\(p\) 和已实现来源记录

\[
\sigma_i=(u_i,a_i,h_i),
\qquad
h_i\mid p+4Da_i.
\]

一个严格整数 Q-lift 候选由 \((D',A,\eta)\) 给出，其中有限门如下：

1. **Q1/势严格下降**
   \[
   D'\mid D,\qquad D'<D,\qquad
   A\mid D',\qquad D'/A\text{ 平方自由},\qquad
   4AD'<p.
   \tag{7}
   \]
2. **Q2/目标映射**
   \[
   \eta:U(4D')\twoheadrightarrow Q_R
   \quad\text{或实际源—目标像},
   \qquad
   \eta(-1)=\pi_R(t).
   \tag{8}
   \]
   若只能映到 \(Q_R\) 的真子群，必须把实际像和目标像同时记录；不能把非满射
   的抽象角色当作商状态。
3. **Q3/来源合同**
   对每条保留来源记录要求
   \[
   AD'\equiv Da_i\pmod{h_i},
   \qquad
   h_i\mid p+4AD',
   \qquad
   \eta(u_i)=\pi_R(u_i),
   \tag{9}
   \]
   并通过 shared-q、互素和 source-switch 标签门。
4. **Q4/源盒与关系格**
   用有限 SNF 检查 \(\widetilde R_C\) 的生成元和 \(\eta\) 的源列关系相容，
   并验证
   \[
   \eta\bigl(\text{候选整数源盒像}\bigr)
   =\overline S_R.
   \tag{10}
   \]
   不能只验证单位群生成子群相等；必须验证实际有限盒像和来源纤维相等。
5. **E1--E5/整数回译**
   来源记录、统一 CRT、范围、正规形以及严格势下降的 E1--E5 全部通过；若
   Q2--Q4 只给出群商而没有保持参数纤维，回执仍是提升障碍。

若 Q1--Q4 和 E1--E5 通过，输出

\[
\boxed{
\mathrm{DYADIC\_RELATION\_STRICT\_Q\_LIFT}
=(D',A,\eta,R_C,\widetilde R_C,\sigma_i).
}
\tag{11}
\]

它是保持来源标签的严格可提升递降，而不只是有限群商。

## Q-lift 失败的最小分派

对固定关系子群和有限候选菜单，失败不能合并成一个模糊标签：

- Q3 的来源合同不相容：输出
  \(\mathrm{DYADIC\_RELATION\_SOURCE\_CRT\_INCONSISTENT}\)，附最小不相容来源对；
- Q4 的源列/关系格 SNF 失败：输出
  \(\mathrm{DYADIC\_RELATION\_SOURCE\_SNF\_OBSTRUCTED}\)，附失败关系向量；
- 源盒像不是 (10)：输出
  \(\mathrm{DYADIC\_RELATION\_FIBER\_UNREALIZED}\)，附缺失的盒像元素；
- Q2 的目标映射失败：输出
  \(\mathrm{DYADIC\_RELATION\_TARGET\_MAP\_OBSTRUCTED}\)，附目标分离角色或
  商像；
- 只有 \(D'=D\) 的菜单元素：记录同模数 relay，不登记严格递降；
- 所有 Q1--Q4 候选均失败：输出
  \(\mathrm{DYADIC\_RELATION\_QUOTIENT\_LIFT\_OBSTRUCTED}\)，保留 (6)。

这些回执把“有限群下降已经存在”和“整数递降尚未实现”严格分开，并且每个失败
分支仍保留一个可继续送入 Fourier、格、q 容量或 Type I 的对象。

## 控制实例

在

\[
H=C_2\times C_{16},\quad
g_1=(1,1),\quad g_2=(0,2),\quad
\mathcal B=[-2,2]^2,\quad
t=(1,0)
\]

中，最大簇关系子群为

\[
R_C=2K,\qquad |R_C|=8.
\]

关系商为

\[
Q_R\simeq C_2\times C_2.
\]

复现器直接检查商模数为 \((2,2)\)，源像的商集合含目标坐标外的两个像，而
\(\pi_R(t)=(1,0)\) 仍未命中。因此 (6) 是严格目标保持下降；是否存在某个
\(U(4D')\) 和来源标签实现这个商，留给 Q1--Q4 菜单，而不在该控制例中擅自宣称。

## 与统一选择器的接线

对一个核心素数状态，选择器可把二进顶位分支规范为：

\[
\begin{aligned}
&m=1
\ \longrightarrow\ \mathrm{TOP\_CLASS\_CLUSTER\_BOUNDARY};\\
&m\ge2
\ \longrightarrow\
\mathrm{DYADIC\_RELATION\_QUOTIENT\_DESCENT};\\
&\text{Q1--Q4/E1--E5 通过}
\ \longrightarrow\
\mathrm{DYADIC\_RELATION\_STRICT\_Q\_LIFT};\\
&\text{任一门失败}
\ \longrightarrow\
\text{带最小障碍的 Fourier/格/q 容量/Type I 分派}.
\end{aligned}
\tag{12}
\]

这一步把目标纤维近邻、二进关系子群和严格下降接口接成一条确定性的有限选择器
链；它仍不证明所有核心素数都落入可提升分支。

## 边界

本引理证明的是目标保持的有限群严格商，以及其整数化所需的完整门集合。它不声称
任意 \(R_C\) 都对应一个实际单位群除子格，也不声称 Q-lift 菜单必然非空。剩余的
全局任务是证明所有 \(\mathrm{DYADIC\_RELATION\_QUOTIENT\_LIFT\_OBSTRUCTED}\) 分支
都能转入 Type I/F/G 证书或另一个严格保持势的递降。

