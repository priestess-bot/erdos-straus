---
kind: claim
claim_id: type-II-source-fiber-elementary-rank-qheight-injection
title: Type II 源纤维 q-height 到目标关系格初等商秩的列注入
statement: 对固定参数纤维的源指数盒、目标关系核和稳定子商，目标差分群的 ell 初等商秩不超过由目标关系格 L_{pi,J} 产生的源列秩；重复 q 来源及在商群中相同的残数列自动合并。只有保持参数纤维的源列组合才计入容量，单个改变纤维的源列不能直接收费。该结论是固定纤维内的严格 rank-capacity 映射，不自动给出跨纤维容量矛盾或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-source-fiber-shared-q-ledger
  - type-II-kernel-fourier-pair-energy-qheight-demand
topics:
- type-II
- source-fiber
- q-height
- elementary-rank
- finite-abelian-groups
- Kneser
- stabilizer
- repeated-q
- capacity
- proof-program
sources:
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: source-power-block-and-stabilizer
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-collision-merge
  - claim: type-II-kernel-fourier-pair-energy-qheight-demand
    role: target-difference-rank-demand
visibility: public
last_checked: '2026-08-05'
---

# Type II 源纤维 q-height 到目标关系格初等商秩的列注入

## 固定纤维与源列

令 \(G\) 为有限阿贝尔群，\(T\le G\) 为当前积集的稳定子，写
\(\overline G=G/T\)。设 \(\pi_0:G\to G_0\) 是定义当前参数纤维的目标商映射；
若没有额外参数商，则取 \(\pi_0\) 为平凡映射。固定一个源指数盒

\[
\mathcal Z=\prod_{i=1}^{r}\{0,1,\ldots,d_i\},
\qquad
\phi(z)=\prod_{i=1}^{r}u_i^{z_i},
\qquad
P=\phi(\mathcal Z).
\tag{1}
\]

这里 \(u_i=q_i\bmod M_*\) 可以来自 Type II 参数纤维的互异 q 幂块，
\(d_i\) 是由 q-height relay 得到的可用层数。若同一个 q 有多个来源，先按共同
账本合并为一个源列；若不同 q 在 \(\overline G\) 中给出同一元素，也只保留一个
商群列。

设 \(Q\subseteq\mathcal Z\) 是目标陪集的去重源指数支撑。令
\(J=\{i:d_i>0\}\)，并定义目标关系格

\[
L_{\pi,J}
=\{n\in\mathbb Z^J:\pi_0(\phi(n))=1\}.
\tag{2}
\]

它的源列像为

\[
A_{\pi,J}
=\{\phi(n)T:n\in L_{\pi,J}\}
\le\overline G.
\tag{3}
\]

只有 \(L_{\pi,J}\) 中的组合保持当前目标纤维，因此 \(A_{\pi,J}\) 才是可收费的
source-relation carrier。目标差分群定义为

\[
\Delta_Q
 =\left\langle
   \phi(z-z')T:
   z,z'\in Q
   \right\rangle
 \le\overline G.
\tag{4}
\]

对每个素数 \(\ell\)，定义其初等商秩

\[
r_\ell(Q)
 =\dim_{\mathbb F_\ell}\bigl(\Delta_Q/\ell\Delta_Q\bigr).
\tag{5}
\]

这个秩等于 \(\Delta_Q\) 上独立 \(\ell\)-阶角色的数量，因此正是目标纤维的
多角色 rank demand，而不是 pair-energy 边数。

## 列注入定理

由 \(z,z'\in Q\) 的差向量都属于 \(L_{\pi,J}\)，有

\[
\boxed{
\Delta_Q\le A_{\pi,J},
\qquad
r_\ell(Q)
\le
\dim_{\mathbb F_\ell}(A_{\pi,J}/\ell A_{\pi,J})
\le |J|.
}
\tag{6}
\]

取 \(L_{\pi,J}\) 的 Smith 或 Hermite 基 \(b_1,\ldots,b_s\)，令
\(v_a=\phi(b_a)T\)。把相同的 \(v_a\) 合并后，关系源列的实际初等商秩为

\[
\boxed{
r_\ell^{\mathrm{src}}(\ell)
=\dim_{\mathbb F_\ell}
\left\langle v_1,\ldots,v_s\right\rangle/
\ell\left\langle v_1,\ldots,v_s\right\rangle
=\dim_{\mathbb F_\ell}(A_{\pi,J}/\ell A_{\pi,J}).
}
\tag{7}
\]

### 证明

任取 \(z,z'\in Q\)。差向量 \(z-z'\) 的第 \(i\) 个坐标在 \(d_i=0\) 时必为零，
且 \(\pi_0(\phi(z-z'))=1\)，所以 \(z-z'\in L_{\pi,J}\)，从而
\(\phi(z-z')T\in A_{\pi,J}\)。这证明 \(\Delta_Q\le A_{\pi,J}\)。

对有限阿贝尔群，子群的 \(\ell\)-秩不超过母群的 \(\ell\)-秩：在
\(\ell\)-primary 分量上这是 \(\Delta_Q[\ell]\subseteq A_{\pi,J}[\ell]\) 的维数
不等式，而
\(\dim\Delta_Q[\ell]=\dim\Delta_Q/\ell\Delta_Q\)。于是得到 (6)。
Smith/Hermite 基的像生成 \(A_{\pi,J}\)，故 (7) 是同一源列秩的规范计算。
若某个关系列落入稳定子 \(T\)，其像为单位元，不贡献任何秩。证毕。

## q-height 的精确含义

在互异 q 的源模型中，\(d_i>0\) 等价于第 \(i\) 个 q 幂块至少有一个可回译层；
因此 (6)--(7) 给出一个不依赖边复用的固定纤维容量回执：

\[
\boxed{
\text{目标 }\ell\text{-差分秩 }r_\ell(Q)
\Longrightarrow
\text{至少 }r_\ell(Q)\text{ 个独立的目标兼容源关系列。}
}
\tag{8}
\]

重复 q 时不能把多个来源标签分别计作列。共同 q 账本只产生一个
\(u_qT\) 列，其可用深度是

\[
d_q(s)=\min\!\left(v_q(p+4s),\sum_i\ell_i(s)\right),
\]

但对初等商秩来说只要 \(d_q(s)>0\) 就至多贡献一个独立列；深度超过一只能
增加该列的有限阶容量，不能增加 \(\ell\)-列秩。

若某些 \(u_iT=1\)，它们虽有正整数 q-height，却完全落入稳定子吸收分支，
不应计入 (8)。这正是 Kneser 活跃容量
\(\kappa_i=\min(d_i,\operatorname{ord}_{\overline G}(u_iT)-1)\)
为零时的线性秩版本。

## 两个边界例子

### \(p=97\) 的秩零目标纤维

取 \(G=U(24)\)、\(P=\{1,11\}\)。对伪命中目标 \(t=23\)，去重目标陪集支撑只有
一个点 \(Q_t=\{0\}\)，所以 \(\Delta_{Q_t}=\{1\}\) 且所有
\(r_\ell(Q_t)=0\)。完整源盒虽然有一条有效列 \(11\)，但该列只出现在绝对锚点，
不能被误算成目标差分秩需求；这正是纯锚点/秩零残余。

把 \(11\) 与另一纤维的 \(13\) 直接合并会得到 \(11\cdot13\equiv-1\pmod{24}\)，
但这两个列不属于同一个参数纤维；列注入定理不能跨纤维相加，正好阻止该 pooled
pseudo-hit。

### \(p=241\) 的重复 q

在 \(p=241,D=6,q=5\) 的候选 \(s=6\) 中，两条来源各含一个 5，但共同账本给
\(d_5(6)=1\)。即使两个来源标签都被保留，商群中仍只有一个 q 列
\(5T\)，所以该 q 对任何初等商至多贡献一个独立方向；不能把两个来源重复计入
秩容量。

## 对统一选择器的分派

对一个未命中目标纤维，先计算 \(r_\ell(Q)\) 和关系源列秩
\(r_\ell^{\mathrm{src}}(\ell)=\dim_{\mathbb F_\ell}(A_{\pi,J}/\ell A_{\pi,J})\)：

1. 若 \(r_\ell(Q)>r_\ell^{\mathrm{src}}(\ell)\)，则该回执与当前源纤维不相容，
   可直接标记 SOURCE_RANK_INCONSISTENT；在真实算术源模型中这意味着至少有一个
   关系或来源标签被错误携带。
2. 若 \(r_\ell(Q)=r_\ell^{\mathrm{src}}(\ell)\)，所有可用的 \(\ell\)-方向都已经
   被源列占满，进入 Kneser 稳定子/有限阶关系分支；不能继续把同一列重复收费。
3. 若 \(r_\ell(Q)<r_\ell^{\mathrm{src}}(\ell)\)，存在未使用的关系源列自由度，才有
   可能从另一列构造 Type II 命中或容量超载。

这三分是固定纤维内的严格线性分派，不声称不同 \(A,D_*\) 之间可以直接合并。

## 研究边界

本引理完成了“目标初等商秩由哪些实际 q 源列支付”的固定纤维映射，但仍没有证明
跨参数纤维的列秩必须超载，也没有把 SOURCE_RANK_INCONSISTENT 自动变成核心素数
递降。下一步的最窄问题是：在 \(r_\ell(Q)=r_\ell^{\mathrm{src}}(\ell)\) 的饱和
分支，能否利用未命中的目标陪集和稳定子有限阶关系，构造 Type II 证书或保持标记的
严格商递降。
