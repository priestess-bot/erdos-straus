---
kind: claim
claim_id: type-II-source-fiber-low-rank-lock-cyclic-terminal
title: Type II 源纤维低秩锁定与素数阶循环终端
statement: 对固定目标关系纤维的差分群 Delta_Q，所有初等商秩为零当且仅当所有盒内目标关系都被稳定子吸收；若每个 ell 初等商秩至多一，则 Delta_Q 为循环群，目标测试可降为一个有限循环指数集。特别地，在 Delta_Q 为素数阶 ell、目标锚点落在该循环群且存在至少 ell-1 个合法的保持纤维非零关系块时，Cauchy-Davenport 给出目标命中；目标缺失则强制关系块数至多 ell-2，或锚点位于差分群之外。该三分仍是固定纤维结果，素数阶之外需继续处理循环核和稳定子商。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-source-lattice-fibered-kneser-selector
topics:
- type-II
- source-fiber
- low-rank
- cyclic
- cauchy-davenport
- target-fiber
- stabilizer
- anchor-obstruction
- capacity
- proof-program
sources:
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: target-difference-rank
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: saturated-versus-unsaturated-kernel-branch
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: unsaturated-kernel-dual-certificate
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: source-fiber-Type-II-lift
visibility: public
last_checked: '2026-08-05'
---

# Type II 源纤维低秩锁定与素数阶循环终端

## 目标差分群

沿用固定源盒、目标商映射 \(\pi_0\) 和稳定子商
\(\overline G=G/T\) 的设置。对去重目标支撑 \(Q\) 定义

\[
\Delta_Q
=\left\langle \phi(z-z')T:z,z'\in Q\right\rangle
\le\overline G.
\tag{1}
\]

取 \(z_0\in Q\)，并写目标锚点
\(\alpha=t^{-1}\phi(z_0)\)。则目标截面在稳定子商中的相对形式为

\[
\overline S_t=\alpha\,\overline{\phi(Q)}
\subseteq \alpha\Delta_Q.
\tag{2}
\]

目标 \(t\) 能在该相对群中被命中，必要条件是

\[
\alpha^{-1}\in\Delta_Q.
\tag{3}
\]

若 (3) 失败，所有相对关系即使完全覆盖 \(\Delta_Q\)，也只能填满错误的锚点陪集；
这是一条 ANCHOR_OUTSIDE_DIFFERENCE 负证书，而不是 q 进容量矛盾。

## 秩零锁定

对有限阿贝尔群定义

\[
r_\ell(Q)=\dim_{\mathbb F_\ell}(\Delta_Q/\ell\Delta_Q).
\]

则

\[
\boxed{
\bigl(r_\ell(Q)=0\ \forall\ell\bigr)
\iff
\Delta_Q=\{1\}.
}
\tag{4}
\]

固定 \(z_0\) 后，(4) 等价于

\[
\boxed{
\phi(z-z_0)\in T
\quad\text{对每个 }z\in Q.
}
\tag{5}
\]

因此秩零纤维中没有任何未被稳定子吸收的盒内目标关系。若 \(T=1\)，目标支撑
只有一个实际单位，Fourier 证书只检测绝对锚点；若 \(T\ne1\)，必须把剩余的
\(T\)-方向交给同余核商或核分裂 Fourier 分支。

结合稳定子三分，秩零分支严格分为：

1. \(T\) 吸收模数降阶核：按商积集递降或直接命中；
2. \(T\) 不吸收该核：目标截面有非平凡核 Fourier 分裂；
3. 锚点条件 (3) 失败：ANCHOR_OUTSIDE_DIFFERENCE，不能把关系覆盖误称为命中。

## 低秩的循环化

有限阿贝尔群 \(\Delta_Q\) 是循环群，当且仅当对每个素数 \(\ell\) 有
\(r_\ell(Q)\le1\)。因此若所有初等商秩至多一，可取生成元 \(g\) 和阶
\(n=|\Delta_Q|\)，使

\[
\Delta_Q=\langle g\rangle,\qquad
\overline{\phi(Q)}\subseteq\{g^e:e\in E_Q\}
\]

其中 \(E_Q\subseteq\mathbb Z/n\mathbb Z\) 是一个有限循环指数集。目标测试变成

\[
\alpha^{-1}=g^{e_*}
\quad\text{且}\quad e_*\in E_Q.
\tag{6}
\]

这一步不是把任意源盒误写成连续区间；\(E_Q\) 仍可能有孔，孔结构是循环低秩分支
的真实剩余对象。

## 素数阶循环终端

进一步假设 \(\Delta_Q\simeq C_\ell\) 为素数阶循环群，且锚点条件 (3) 成立。设有
\(k\) 个合法的保持纤维关系块

\[
B_j=\{0,v_j\}\subseteq C_\ell,\qquad v_j\ne0,
\qquad 1\le j\le k,
\tag{7}
\]

满足任意选择 \(\varepsilon_j\in\{0,1\}\) 都对应盒内、来源标签合法的目标关系
组合。则

\[
\left|B_1+\cdots+B_k\right|
\ge \min(\ell,k+1)
\tag{8}
\]

由 Cauchy–Davenport 逐次应用得到。当 \(k\ge\ell-1\) 时，右端为 \(\ell\)，故

\[
B_1+\cdots+B_k=C_\ell.
\]

结合锚点条件 (3)，目标 \(-1\) 被命中；再由源纤维 Kneser 选择器的整数回译，
得到 Type II 短证书。

所以在这个严格的素数阶关系块模型中，

\[
\boxed{
\text{目标缺失}
\Longrightarrow
\text{锚点在差分群外，或 }k\le\ell-2.
}
\tag{9}
\]

式 (9) 是一个构造性循环容量缺口，不依赖 pair-energy 的边复用计数。

## 边界例子

### \(p=97\) 的锚点外秩零

对 \(G=U(24)\)、\(P=\{1,11\}\)、\(t=23\)，目标支撑只有一个相对点，
\(\Delta_Q=1\)，而锚点 \(\alpha=13\ne1\)。因此 (3) 失败；这解释了模 \(4\)
投影产生伪命中但模 \(24\) 不命中的原因。

### \(p=5113\) 的素数阶命中

在 \(D_*=1\)、\(G=U(4)\) 的源纤维中，17 的残数为 1，7 的残数为 \(-1\)。
差分群为 \(C_2\)，锚点条件满足，取一个非零关系块即可达到
\(\ell-1=1\) 的阈值，得到 \(P=\{1,-1\}\) 和真实 Type II 降模证书。

## 研究边界

本卡关闭了秩零的关系锁定分类，并在素数阶循环商中给出一个真正的短块终端。
仍未处理：

* \(\Delta_Q\simeq C_{\ell^a}\) 的高阶循环孔结构；
* 素数阶关系块不能独立保持参数纤维时的 source-switch 提升；
* 秩一但锚点外的分支如何转成核心素数递降。

这些残余必须交给循环 Kneser 临界结构、低模数商或其它 Type I/II 证书，不能由
(9) 自动推出全称选择器。
