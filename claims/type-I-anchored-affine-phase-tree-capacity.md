---
kind: claim
claim_id: type-I-anchored-affine-phase-tree-capacity
title: 锚定仿射相位图的无竖直元与条件相位树容量
statement: '对有限锚定集 J_t 的 q-primary 锚定相位，若 anchor t 的阶与奇素数 q 互素，则其带标记相位图没有非零纯标签元。若一个已经证明 sound 且 complete 的物理 source 表具有共同的仿射整数标签律、统一区间和重复度界，则该表的总 q-height 被完整锚定集的逐层相位数 D_{J_t,k} 严格控制。带标记 SNF 饱和只保持角色约束，不能把 D_{J_t,k} 替换为压缩菜单的相位数；C_6 反例显示这种替换可给出错误容量界。该结论不提供实际 source map、E2 carry、E4 解提升或 E5 递降。'
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-fg-marked-source-menu-saturation
  - type-I-phase-clearing-cell-capacity-contract
  - type-I-fg-physical-carry-arc-lift-interface
topics:
  - type-I
  - F-state
  - anchored-phase
  - affine-source-map
  - q-primary
  - phase-tree
  - capacity
  - marked-source
  - SNF
  - counterexample
  - proof-boundary
  - proof-program
sources:
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: anchored-q-primary-phase-interface
  - claim: type-I-fg-marked-source-menu-saturation
    role: marked-source-saturation-semantics
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: nested-phase-tree-capacity-template
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: physical-source-and-carry-interface
visibility: public
last_checked: '2026-08-07'
---

# 锚定仿射相位图的无竖直元与条件相位树容量

## 1. 锚定相位图

固定一个有限阿贝尔群 \(\bar H\)、奇素数 \(q\)、整数 \(e\ge1\)，以及一个
\(q\)-primary 角色

\[
\psi:\bar H\longrightarrow\mu_{q^e}.
\tag{1}
\]

令 \(t\in\bar H\) 的阶与 \(q\) 互素，并令 \(J_t\) 是非空有限锚定集，满足

\[
x_j:=tj^{-1}\in\operatorname{im}\bar\phi
\qquad(j\in J_t).
\tag{2}
\]

固定兼容的根
\(\zeta_{q^k}=\zeta_{q^e}^{q^{e-k}}\)。对 \(1\le k\le e\)，写

\[
\psi_k=\psi^{q^{e-k}},
\qquad
\psi_k(j)=\zeta_{q^k}^{-\gamma_{j,k}},
\qquad
\gamma_{j,k}\in\mathbb Z/q^k\mathbb Z.
\tag{3}
\]

这与既有锚定相位记号一致。定义第 \(k\) 层的完整锚定相位数

\[
D_{J_t,k}:=|\psi_k(J_t)|
=|\{\gamma_{j,k}:j\in J_t\}|.
\tag{4}
\]

### 无竖直元引理

令

\[
\mathcal A^{\mathrm{anc}}_{t,k}
=\{(x_j,\gamma_{j,k}):j\in J_t\}
\subseteq\langle x_j:j\in J_t\rangle\oplus\mathbb Z/q^k\mathbb Z.
\tag{5}
\]

则其生成子群没有非零纯标签元：

\[
\boxed{
\Gamma(\mathcal A^{\mathrm{anc}}_{t,k})
\cap(\{1\}\oplus\mathbb Z/q^k\mathbb Z)
=\{(1,0)\}.}
\tag{6}
\]

**证明。** \(\psi_k(t)=1\)，因为它的阶同时整除 \(q^k\) 与
\(\operatorname{ord}(t)\)。于是

\[
\psi_k(x_j)=\psi_k(t)\psi_k(j)^{-1}
=\zeta_{q^k}^{\gamma_{j,k}}.
\tag{7}
\]

若 \(\prod_jx_j^{a_j}=1\)，对 (7) 取积即有
\(\zeta_{q^k}^{\sum_ja_j\gamma_{j,k}}=1\)，故标签和为零。这正是 (6)。
证毕。

因此，任何菜单 \(\mathcal M\subseteq\mathcal A^{\mathrm{anc}}_{t,k}\) 若满足

\[
\Gamma(\mathcal M)=\Gamma(\mathcal A^{\mathrm{anc}}_{t,k}),
\tag{8}
\]

就可进入既有的带标记 SNF 饱和门，检验其角色约束是否完整；但 (8) 本身不保存
\(D_{J_t,k}\)。

## 2. 条件相位树容量定理

令 \(\mathcal W\) 是同一个声明参数纤维中的有限**物理** source 行表。要应用本节，
\(\mathcal W\) 及其物理 transition relation 必须已经由独立算术命题证明 sound 且
complete；每行还必须保存实际整数载体、因子分解和 carry 账本。对每个
\(w\in\mathcal W\)，给定 \(L\in\mathbb Z\)、\(B\in\mathbb Z_{\ge0}\)，以及

\[
j(w)\in J_t,\qquad
1\le h_w\le e,\qquad
s_w\in[L,L+B]\cap\mathbb Z.
\tag{9}
\]

假设存在对整个表共同的

\[
u\in(\mathbb Z/q^e\mathbb Z)^\times,
\qquad
c\in\mathbb Z/q^e\mathbb Z
\tag{10}
\]

使所有 \(w\) 及所有 \(1\le k\le h_w\) 都满足统一的仿射标签律

\[
s_w\equiv c+u\gamma_{j(w),k}\pmod {q^k}.
\tag{11}
\]

再假设任一整数标签的物理重复度至多为 \(\mu\)。

\[
\boxed{
\sum_{w\in\mathcal W}h_w
\le
\mu\sum_{k=1}^{e}
D_{J_t,k}
\left(\left\lfloor\frac{B}{q^k}\right\rfloor+1\right).}
\tag{12}
\]

**证明。** 对每层设

\[
\mathcal W_k=\{w\in\mathcal W:h_w\ge k\}.
\]

由 (11)，\(\mathcal W_k\) 的所有标签只落在
\(c+u\{\gamma_{j,k}:j\in J_t\}\) 的 \(D_{J_t,k}\) 个模 \(q^k\) 残基类。
单位仿射变换不改变该残基数。长度为 \(B\) 的整数区间在一个固定残基类中至多有
\(\lfloor B/q^k\rfloor+1\) 个不同标签；计入重复度得到

\[
|\mathcal W_k|
\le
\mu D_{J_t,k}
\left(\left\lfloor\frac{B}{q^k}\right\rfloor+1\right).
\]

对 \(k\) 求和并用
\(\sum_wh_w=\sum_{k=1}^{e}|\mathcal W_k|\)，即得 (12)。证毕。

若共同的 \(u,c\) 只在有限 chart 家族内成立，正确的第 \(k\) 层相位数应改为

\[
|\Omega_k|,
\qquad
\Omega_k=
\{c_a+u_a\gamma_{j,k}:a\text{ 为 chart},\ j\in J_{t,a}\},
\tag{13}
\]

而不能继续写成单一的 \(D_{J_t,k}\)。若 \(u,c\) 随物理行改变，(12) 完全不能从
锚定相位数据推出。

## 3. 菜单压缩的严格反例

取加法群 \(\bar H=C_6=\langle g\rangle\)，目标对合
\(\tau=g^3\)，并令

\[
J=\{1,g^4,g^5\},
\qquad
t=1,
\qquad
q=3,
\qquad
\psi(g)=\zeta_3.
\tag{14}
\]

\(J\) 的稳定子平凡、\(1\in J\)、且 \(\tau\notin J\)，所以它具有 F 型目标缺失的
有限群形状。取 \(\operatorname{im}\bar\phi=\bar H\)，则 \(J_t=J\)，而 (5) 的三行是

\[
\begin{array}{c|c|c}
j&x_j=tj^{-1}&\gamma_{j,1}\\ \hline
1&1&0\\
g^4&g^2&2\\
g^5&g&1.
\end{array}
\tag{15}
\]

因此

\[
\Gamma(\mathcal A^{\mathrm{anc}}_{t,1})
=\langle(g,1)\rangle
=\Gamma(\{(g,1)\}),
\qquad
D_{J_t,1}=3.
\tag{16}
\]

也就是说，单行菜单已经带标记饱和，却只显式携带一个相位值。令一个抽象的三行物理表
有标签 \(0,1,2\)、高度都为 \(1\)、区间宽度 \(B=2\)、重复度 \(\mu=1\)，并分别选择
\(j=1,g^5,g^4\)。它满足 (11) 的 \(u=1,c=0\) 版本，且真实容量正好是

\[
3
\le
3\left(\left\lfloor\frac23\right\rfloor+1\right)
=3.
\tag{17}
\]

若错误地将 \(D_{J_t,1}=3\) 换成压缩菜单的 \(1\)，会得出假不等式

\[
3\le1.
\tag{18}
\]

故带标记群饱和只能压缩角色约束，绝不能压缩物理相位胞数、物理 multiplicity
或 \(q\)-height。

## 4. 选择器边界

本卡在下列字段已经同时存在时，才允许输出
\(\mathrm{ANCHORED\_AFFINE\_PHASE\_TREE\_CAPACITY}\)：

~~~text
source_complete = true
physical_transition_complete = true
common_affine_chart = (u, c)
physical_label_interval = [L, L+B]
physical_label_multiplicity <= mu
physical_carry_status = checked
~~~

缺少任一项时，输出必须保持
\(\mathrm{ANCHORED\_PHASE\_MAP\_UNCLOSED}\)。即使 (12) 可用，它仍不构造实际
source、E2 carry、E4 全域解提升或 E5 良基下降；因此它是条件性容量证书，而不是
verified edge。

窄复现：

~~~bash
python3 reproductions/type_i_anchored_affine_phase_tree_capacity.py --verify
~~~
