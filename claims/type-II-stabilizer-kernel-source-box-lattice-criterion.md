---
kind: claim
claim_id: type-II-stabilizer-kernel-source-box-lattice-criterion
title: Type II 稳定子同余核的源指数盒格判据
statement: 设 G 为有限阿贝尔单位群，源块 B_i={1,g_i,...,g_i^{e_i}} 的乘积 P 由指数盒 B 映射 phi:Z^r->G 生成，Lambda=ker(phi)，K<=G 为候选降模同余核。则 K<=Stab_G(P) 当且仅当 K<=im(phi) 且在有限商 Q=Z^r/Lambda 中有 Bbar+Kbar=Bbar，其中 Bbar=(B+Lambda)/Lambda、Kbar=phi^{-1}(K)/Lambda。K<=im(phi) 和盒不变性均可由有限 SNF/生成元平移检查；若某个源块子盒直接映出 K，则给出立即的稳定子包含证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-source-fiber-qheight-kneser-bridge
topics:
  - type-II
  - stabilizer
  - congruence-kernel
  - source-lattice
  - exponent-box
  - SNF
  - quotient-descent
  - finite-abelian
sources:
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: source-labelled-exponent-box
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: q-height-block-input
visibility: public
last_checked: '2026-08-05'
---

# Type II 稳定子同余核的源指数盒格判据

## 1. 源指数盒模型

把有限阿贝尔群 \(G\) 写成 invariant-factor 形式，并用乘法记号表示。令
\[
\varphi:\mathbb Z^r\longrightarrow G,\qquad
\varphi(z_1,\ldots,z_r)=\prod_{i=1}^r g_i^{z_i},
\]
其中第 \(i\) 个真实源块为
\[
B_i=\{1,g_i,\ldots,g_i^{e_i}\}.
\]
定义指数盒
\[
\mathcal B=\prod_{i=1}^r\{0,1,\ldots,e_i\},
\qquad
P=\varphi(\mathcal B),
\qquad
\Lambda=\ker\varphi,
\qquad
H=\operatorname{im}\varphi.
\tag{1}
\]
\(\Lambda\) 是一个有限指数格，且
\[
Q=\mathbb Z^r/\Lambda\simeq H.
\tag{2}
\]

设 \(K\le G\) 是准备检验的模数降阶同余核，例如
\[
K=\ker\bigl(U(4D_*)\to U(4D')\bigr).
\]

## 2. 精确核包含判据

定义
\[
\widetilde K=\varphi^{-1}(K)\subseteq\mathbb Z^r,
\qquad
\overline{\mathcal B}=(\mathcal B+\Lambda)/\Lambda\subseteq Q,
\qquad
\overline K=\widetilde K/\Lambda\le Q.
\tag{3}
\]

则有
\[
\boxed{
K\le\operatorname{Stab}_G(P)
\iff
\left[
K\le H
\ \text{且}\
\overline{\mathcal B}+\overline K=\overline{\mathcal B}
\right].
}
\tag{4}
\]

这里 \(\operatorname{Stab}_G(P)=\{k\in G:Pk=P\}\)。

### 证明

若 \(K\le\operatorname{Stab}_G(P)\)，则 \(P\subseteq H\) 且 \(Pk=P\) 对每个
\(k\in K\) 成立，故 \(K\le H\)。由于
\[
P K=\varphi(\mathcal B+\widetilde K),
\]
且 \(\varphi(\mathcal B)=\varphi(\mathcal B+\Lambda)\)，有
\[
P K=P
\iff
\mathcal B+\widetilde K\subseteq\mathcal B+\Lambda
\iff
\overline{\mathcal B}+\overline K=\overline{\mathcal B}.
\]
反向同理：若 \(K\le H\) 且盒像在 \(\overline K\) 下不变，则
\(\varphi(\mathcal B+\widetilde K)=\varphi(\mathcal B)\)，即 \(PK=P\)。证毕。

注意 \(K\le H\) 是不可省略的来源条件；若 \(K\) 含有源子群之外的元素，
\(PK\) 会落入不同的 \(H\)-陪集，不可能等于 \(P\)。

## 3. 可构造的 SNF 回执

将 \(G\) 的 invariant-factor 坐标写成
\[
G=\bigoplus_{\nu=1}^s\mathbb Z/n_\nu\mathbb Z,
\]
并令 \(C\) 为源列 \(g_i\) 的坐标矩阵，\(R_K\) 为 \(K\) 的生成元矩阵。

1. **KERNEL\_SOURCE\_MEMBERSHIP**：对每个 \(K\) 生成元 \(k\)，求解
   \[
   Cx\equiv k\pmod{(n_1,\ldots,n_s)}.
   \tag{5}
   \]
   SNF 可解当且仅当 \(k\in H\)；任一失败行直接给出
   KERNEL_NOT_IN_SOURCE，从而证明 \(K\not\le H\)。
2. **BOX\_INVARIANCE**：在有限商 \(Q\simeq H\) 中枚举
   \(\overline{\mathcal B}\) 的有限元素，并对 \(K\) 的一组商生成元检查
   \[
   \overline{\mathcal B}+\bar k=\overline{\mathcal B}.
   \tag{6}
   \]
   生成元逐个通过当且仅当整个 \(\overline K\) 通过；失败的
   \((\bar b,\bar k)\) 给出 KERNEL_BOX_MISS，其中
   \(\bar b+\bar k\notin\overline{\mathcal B}\)。
3. 两步均通过时，回执
   \[
   \mathrm{KERNEL\_STABILIZER\_CERT}
   =(K,C,\Lambda,\overline{\mathcal B},\overline K)
   \tag{7}
   \]
   证明 \(K\le\operatorname{Stab}_G(P)\)，可进入稳定子饱和商
   \(P=\pi^{-1}(\pi(P))\)。

这是一种有限证书：SNF 只处理源子群成员关系，盒平移只处理有限的指数盒像，
二者不把抽象低模数命中误算作原模数命中。

## 4. 立即充分条件：完整核源盒

若存在源块子集 \(J\) 使
\[
\varphi_J\!\left(\prod_{j\in J}\{0,\ldots,e_j\}\right)=K,
\tag{8}
\]
则
\[
P=P_{\bar J}K,\qquad PK=P,
\]
从而 \(K\le\operatorname{Stab}_G(P)\)。这给出无需枚举全盒的
FULL_KERNEL_SOURCE_BOX 证书。更一般地，只要一个子盒的像是 \(K\) 的非空
陪集，同样得到稳定子包含。

条件 (8) 的检查仍是有限的：对每个 \(k\in K\) 解子矩阵 SNF，并验证解的坐标落在
对应的有限区间；若某个坐标超出区间，不能把子群生成性误当作盒覆盖。

## 5. \(p=97\) 的严格失败边界

在
\[
G=U(24),\qquad P=\{1,11\}
\]
中，降到 \(U(4)\) 的核为
\[
K=\{1,5,13,17\}.
\]
源子群为
\[
H=\langle 11\rangle=\{1,11\}.
\]
因为 \(K\not\le H\)，式 (5) 已有失败行；因此
\[
K\not\le\operatorname{Stab}_{U(24)}(P),
\]
即使 \(\pi(P)=\{1,-1\}\) 已在模 \(4\) 命中，也不能回升为模 \(24\) 的 Type II
证书。这正是低模数伪命中的来源格障碍。

## 6. 与稳定子商递降的接线

把 (4) 接入稳定子同余核三分：

- KERNEL_STABILIZER_CERT：可用饱和恒等式
  \(P=\pi^{-1}(\pi(P))\)，原模数和商模数的目标命中等价；双缺失时进入严格
  降模势；
- KERNEL_NOT_IN_SOURCE 或 KERNEL_BOX_MISS：低模数命中若存在，只能进入
  参数纤维/CRT 检查；不能直接称为递降，失败记录 source-fiber 负证书；
- 若盒检验只对某个源子盒失败，可把失败的边界坐标转成一个有限 Fourier/格缺口，
  再交给现有的 annihilator 或 Hall 对偶分派。

因此“核包含”不再是抽象假设，而是一个可计算的来源格门；但该门通过的全称性仍需
由 q-height 结构或其它容量定理证明，不能由群商形式自动推出。
