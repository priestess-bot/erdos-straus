---
kind: claim
claim_id: type-II-top-kernel-pair-overflow-capacity
title: 奇素数顶层核反足表示的短关系—有符号溢出容量二分
statement: 设目标 t 为二阶元，K 为奇素数阶顶层核，且目标陪集 tK 可由对称有限指数盒命中而 t 本身未命中。则陪集源纤维在指数取反下无固定点；每一对反足表示的两倍差向量都映射到 K 的非单位生成元。该向量若落在原指数预算内，给出短的 K 源生成关系；否则给出至少一个有方向的盒外单位。对带有已验证 q 进槽合同的跨状态单位集合，所有盒外单位满足 Hall 全匹配或严格容量缺口二分。该结果不把 tK 命中升级为 t 的 Type I/II 证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-source-fiber-multiprimary-digit-terminal
  - type-II-kernel-fourier-source-relation-compatibility
  - type-I-target-fiber-joint-capacity-signed-carrier-dictionary
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
  - type-II
  - top-kernel
  - odd-primary
  - source-relation
  - target-fiber
  - signed-overflow
  - q-adic-capacity
  - Hall
  - Fourier
  - proof-program
sources:
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: top-kernel-target-coset
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: intrinsic-kernel-source-relation
  - claim: type-I-target-fiber-joint-capacity-signed-carrier-dictionary
    role: signed-overflow-coordinate-dictionary
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: cross-state-slot-Hall-interface
  - reproduction: reproductions/top_kernel_pair_overflow_capacity.py
    role: C2xC3-short-and-overflow-controls
visibility: public
last_checked: '2026-08-09'
---

# 奇素数顶层核反足表示的短关系—有符号溢出容量二分

## 1. 顶层核设置

使用加法记号。令 \(H\) 为有限阿贝尔群，令

\[
K=\langle\kappa\rangle\cong C_\ell,
\qquad
\ell\ \text{为奇素数},
\]

并令 \(\pi:H\to H/K\) 是商映射。固定一个二阶目标
\(t=-t\)，满足

\[
t\notin K,
\qquad
t\notin S.
\tag{1}
\]

令 \(g_1,\ldots,g_r\in H\)，指数盒和映射为

\[
\mathcal B_\nu=\prod_{i=1}^{r}[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad
\phi(z)=\sum_{i=1}^{r}z_i g_i,
\qquad
S=\phi(\mathcal B_\nu).
\tag{2}
\]

盒的对称性给出 \(S=-S\)。假设低商命中

\[
\pi(t)\in\pi(S).
\tag{3}
\]

定义顶层目标陪集的源纤维

\[
\mathcal Z_{tK}
=\{z\in\mathcal B_\nu:\phi(z)\in t+K\},
\qquad
F_t=\{k\in K:t+k\in S\}.
\tag{4}
\]

由 (1)--(3)，\(F_t\) 非空且不含 \(0\)。由于 \(S=-S\) 且 \(t=-t\)，有

\[
F_t=-F_t.
\tag{5}
\]

当 \(\ell\) 为奇素数时，\(K\) 中的取反只有 \(0\) 一个固定点，所以
\(|F_t|\) 为偶数。注意 \(F_t\ne K\)；否则 \(0\in F_t\)，即 \(t\in S\)，与 (1)
矛盾。这仍然只是顶层陪集命中，不是原目标命中。

## 2. 反足配对与非零核关系

若 \(z\in\mathcal Z_{tK}\)，则

\[
\phi(-z)=-\phi(z)\in t+K,
\]

故 \(-z\in\mathcal Z_{tK}\)。若 \(z=-z\) 作为整数向量，则 \(z=0\)；但
\(\phi(0)=0\in t+K\) 会推出 \(t\in K\)，与 (1) 矛盾。因此
\(\mathcal Z_{tK}\) 是无固定点的反足对并，记其对数为

\[
P_{tK}=\frac{|\mathcal Z_{tK}|}{2}.
\tag{6}
\]

从每一对 \(\{z,-z\}\) 任选一个定向代表 \(z\)，定义

\[
\delta(z)=2z,
\qquad
\rho(z)=\phi(\delta(z))=2\phi(z).
\tag{7}
\]

写 \(\phi(z)=t+k\)，其中 \(k\in F_t\)。由 \(2t=0\) 得

\[
\rho(z)=2k\in K.
\tag{8}
\]

由于 \(0\notin F_t\)、\(\ell\) 为奇素数，\(2k\ne0\)。所以

\[
\boxed{\rho(z)\ \text{是 }K\text{ 的非单位元，并生成整个 }K.}
\tag{9}
\]

这一步把顶层核 Fourier 分支中的每个反足对转成真实源关系：它不是外部参数
频率，而是由两个实际指数向量之差构造出的 \(K\)-生成列。

## 3. 短关系—溢出二分

对每个定向对定义逐坐标盒外量

\[
e_i(z)=\bigl(2|z_i|-\nu_i\bigr)_+,
\qquad
\varepsilon_i(z)=\operatorname{sgn}(z_i)e_i(z).
\tag{10}
\]

于是恰有两种情形：

### A. 短顶层核源关系

若

\[
2|z_i|\le\nu_i\quad(1\le i\le r),
\tag{11}
\]

则 \(\delta(z)\) 是一个坐标受控的非零 \(K\)-生成关系，输出

~~~text
SHORT_KERNEL_SOURCE_GENERATOR
delta = 2*z
kernel_relation = phi(delta)
kernel_order = ell
source_relation_budget = (nu_i)
~~~

任何非平凡顶层核角色 \(\psi\in\widehat K\) 都在
\(\rho(z)\ne0\) 上取非平凡值，因此该关系可直接进入内禀
SOURCE_RELATION_FOURIER 或有限源列 SNF；不需要把它先解释成外部
\(\mathbb Z/h\mathbb Z\) 频率。

### B. 有符号盒外需求

若 (11) 失败，则

\[
\sum_i e_i(z)\ge1.
\tag{12}
\]

每个正的 \(\varepsilon_i(z)\) 保留溢出实际位于源分解的正侧还是负侧。对所有非短
反足对定义总需求

\[
\mathfrak D
=\sum_{\{z,-z\}\ {\rm 非短}}\sum_i e_i(z).
\tag{13}
\]

由 (12) 得到严格下界

\[
\boxed{
\mathfrak D\ge
P_{tK}-P_{\rm short},}
\tag{14}
\]

其中 \(P_{\rm short}\) 是满足 (11) 的反足对数。特别地，若没有任何短关系，
\(\mathfrak D\ge|\mathcal Z_{tK}|/2\)。

式 (14) 是从顶层核表示数到带方向 q 进需求的构造性容量映射下界；它不把表示
重数直接当作可用容量，而是逐坐标产生实际的 signed overflow units。

## 4. 跨状态槽的 Hall 二分

对有限个状态收集所有非短反足对的单位

\[
\mathcal U
=\{(s,\{z,-z\},i,j):
1\le j\le e_i(z)\}.
\tag{15}
\]

假设另有一个已经独立证明的 q 进槽合同：每个物理槽
\(v\in\mathcal V\) 携带 \(q\)、层号、来源标签和整数回译状态，并有容量
\(\kappa(v)\in\mathbb Z_{\ge0}\)；每个需求单位 \(u\in\mathcal U\) 的合法槽邻域
\(\Gamma(u)\subseteq\mathcal V\) 已通过 source-switch、SNF、符号和 E1--E3 门。

则有严格的二分：

1. 若存在一个积分流把全部 \(u\in\mathcal U\) 分配到邻域槽且不超过
   \(\kappa(v)\)，输出
   KERNEL_PAIR_OVERFLOW_SLOT_MAP，并以 (14) 作为已支付需求的下界；
2. 若不存在该流，Hall—最大流最小割给出一个
   \(U\subseteq\mathcal U\) 使

\[
\boxed{
\sum_{v\in\Gamma(U)}\kappa(v)<|U|.}
\tag{16}
\]

输出 KERNEL_PAIR_HALL_QCAPACITY_DEFICIT，其中 \(U\)、邻域和严格缺口
\(|U|-\sum_{v\in\Gamma(U)}\kappa(v)\) 都是有限证书。

若槽合同允许所有需求使用同一槽全集，(16) 退化为总容量判据
\(\mathfrak D>\sum_v\kappa(v)\)。若槽邻域带有 q-prefix 或 source owner 限制，
必须使用完整 Hall 邻域，不能只比较总数。

## 5. 顶层 Fourier 的兼容回执

由 (5) 和 \(0\notin F_t\)，顶层核指示函数的非平凡 Fourier 系数满足

\[
\sum_{\psi\ne1}\widehat{1_{F_t}}(\psi)=-|F_t|.
\tag{17}
\]

反足对称使这些系数的实部可按成对角色重排；因此至少存在非平凡
\(\psi\) 使

\[
\boxed{
-\operatorname{Re}\widehat{1_{F_t}}(\psi)
\ge\frac{|F_t|}{\ell-1}.}
\tag{18}
\]

若第 3 节出现短关系，(9) 说明该 Fourier 角色已经有真实的源生成元可见；若所有
反足对都进入 (13)，则 (14) 把 Fourier 缺失转成有符号盒外需求。角色本身仍不
自动提供外部参数相位；外部回译失败时保留 LIFT_OBSTRUCTED，不能把 (18) 直接
计入 q 容量。

## 6. \(C_2\times C_3\) 控制

取

\[
H=C_2\times C_3,
\qquad
K=\{(0,0),(0,1),(0,2)\},
\qquad
t=(1,0),
\]

以及一个源列 \(g_1=(1,1)\)。当预算 \(\nu_1=1\) 时，盒像为
\(\{(0,0),(1,1),(1,2)\}\)：目标 \(t\) 未命中，但其 \(K\)-陪集命中；唯一反足对
的差向量为 \(\delta=2\)，且

\[
\phi(\delta)=(0,2)\in K\setminus\{0\},
\qquad
e_1=(2-1)_+=1.
\tag{19}
\]

所以该控制输出一个 KERNEL_PAIR_OVERFLOW_DEMAND 单位。若把它接到一个容量为
一的 \(q=3\)、层一槽，存在完整分配；若槽全集为空，则得到缺口一。

当预算改为 \(\nu_1=2\) 时，同一反足对满足
\(2|z_1|=2\le2\)，输出
SHORT_KERNEL_SOURCE_GENERATOR，仍有
\(\phi(2z)=(0,2)\) 生成 \(K\)。将两个独立状态的溢出单位同时接到同一个容量一槽，
Hall 邻域容量为一而需求为二，输出严格缺口一。

复现：

~~~bash
python3 reproductions/top_kernel_pair_overflow_capacity.py --verify
~~~

## 研究边界

本引理新增了顶层奇素数核的实际“表示—对偶—容量”接线：每个陪集反足对要么生成
一个可见的短 \(K\) 源关系，要么支付至少一个带方向盒外单位；在已有物理槽合同下，
这些单位具有完整 Hall 匹配或严格 q 进容量缺口。它没有证明每个核心素数的顶层陪集
都能得到合法外部 owner 槽，也没有把 \(tK\) 的命中变成 \(t\) 的 Type I/II 命中。
奇素数核之外的二阶核应转交广义 \(2^j\) 终端和专门的二进源映射。
