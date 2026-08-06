---
kind: claim
claim_id: type-II-source-fiber-anchor-separating-character-certificate
title: Type II 源纤维锚点外置的分离角色证书
statement: 设固定目标纤维的稳定子商为有限阿贝尔群 Gbar，目标差分群为 Delta，规范化目标截面为 S=alpha R 且 R 包含于 Delta。若 alpha 不属于 Delta（等价于 alpha^{-1} 不属于 Delta），则存在角色 chi 属于 Gbar^，使 chi 在 Delta 上恒为 1 而 chi(alpha) 不等于 1；该角色在 S 上为常相位，并给出幅度等于 |R| 的精确 Fourier 负证书。角色能否降到较小同余商，等价于其对商核平凡；再加源关系格的仿射相容性才可回译为低模数证书，否则必须标记 LIFT_OBSTRUCTED。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-low-rank-lock-cyclic-terminal
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
topics:
- type-II
- source-fiber
- anchor-obstruction
- separating-character
- fourier
- quotient
- lift-obstruction
- constructive-certificate
- proof-program
sources:
  - claim: type-II-source-fiber-low-rank-lock-cyclic-terminal
    role: normalized-target-difference-and-anchor
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: source-relation-affine-lift-gate
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: lower-quotient-versus-kernel-branch
visibility: public
last_checked: '2026-08-05'
---

# Type II 源纤维锚点外置的分离角色证书

## 规范化目标截面

令固定源盒在稳定子商中的像为 \(\overline G=G/T\)。取目标支撑中的一个
基点 \(z_0\)，定义规范化差分支撑

\[
R_Q=
\{\phi(z)\phi(z_0)^{-1}T:z\in Q\}
\subseteq \Delta_Q,
\tag{1}
\]

以及目标锚点

\[
\alpha=t^{-1}\phi(z_0)T.
\tag{2}
\]

于是目标相对截面写成

\[
S_t=\alpha R_Q\subseteq\alpha\Delta_Q.
\tag{3}
\]

目标命中身份元的必要条件是
\(\alpha^{-1}\in\Delta_Q\)。由于 \(\Delta_Q\) 是子群，这等价于
\(\alpha\in\Delta_Q\)。

## 对偶分离定理

假设 \(\alpha\notin\Delta_Q\)。则 \(\alpha\Delta_Q\) 是非平凡的商群
\(\overline G/\Delta_Q\) 中的非单位陪集。有限阿贝尔群的角色分离给出

\[
\exists\chi\in\widehat{\overline G}:
\qquad
\chi|_{\Delta_Q}=1,\quad \chi(\alpha)\ne1.
\tag{4}
\]

对任意 \(r\in R_Q\)，由 (4) 有 \(\chi(\alpha r)=\chi(\alpha)\)。因此在 Fourier
约定

\[
\widehat{1_{S_t}}(\chi)
=\sum_{x\in\overline G}1_{S_t}(x)\overline{\chi(x)}
\tag{5}
\]

下得到精确系数

\[
\boxed{
\widehat{1_{S_t}}(\chi)
=\overline{\chi(\alpha)}\,|R_Q|,
\qquad
|\widehat{1_{S_t}}(\chi)|=|R_Q|.
}
\tag{6}
\]

身份元的角色值为 \(1\)，而 \(S_t\) 全部落在相位
\(\chi(\alpha)\ne1\) 上，所以身份元不可能属于 \(S_t\)。式 (6) 是一个
ANCHOR_SEPARATING_CHARACTER 的构造性负证书；它不把相对关系覆盖误报成目标命中。

### 证明

商群 \(\overline G/\Delta_Q\) 中的非单位元 \(\alpha\Delta_Q\) 可被某个非平凡
角色分离。将该商角色与自然投影复合，得到 (4)。式 (3) 和
\(\chi|_{\Delta_Q}=1\) 给出 \(\chi(\alpha r)=\chi(\alpha)\)，代入 (5) 即得 (6)。
证毕。

## 降模与源关系相容性

设 \(\pi:\overline G\to\overline G'\) 是候选低模数商，核为 \(K_\pi\)。角色
\(\chi\) 能降到商上，当且仅当

\[
\boxed{K_\pi\subseteq\ker\chi.}
\tag{7}
\]

即存在 \(\chi'\in\widehat{\overline G'}\) 使
\(\chi=\chi'\circ\pi\)。这只是群论降模条件；要把 (6) 回译成
Type II source-switch 证书，还必须通过源关系格的仿射相容性判据。若 (7) 或该
关系格条件失败，回执必须标记 LIFT_OBSTRUCTED，而不能把抽象分离角色算入低模
容量。

因此锚点外置分支的严格分派为：

1. 存在满足 (7) 且源关系相容的角色：输出可计算的低商 Fourier 负证书；
2. 角色只能在原模数存在，或关系格相容性失败：输出
   ANCHOR_SEPARATING_CHARACTER/LIFT_OBSTRUCTED；
3. 若目标其实满足 \(\alpha^{-1}\in\Delta_Q\)，则转入循环容量或 Type II 命中分支，
   不得使用本证书。

## 边界例子

在 \(p=97\)、\(G=U(24)\) 的伪命中纤维中，
\(\Delta_Q=1\)、\(\alpha=13\)。取角色
\(\chi(5)=1\)、\(\chi(13)=\chi(17)=-1\)，则
\(\chi|_{\Delta_Q}=1\)、\(\chi(\alpha)=-1\)，给出最大幅度的锚点外置证书。
但该角色不对模 \(4\) 商核平凡，故不能回译为模 \(4\) 的低模数 Type II 证书；
这正是 LIFT_OBSTRUCTED 而非“降模命中”的边界。

## 研究边界

本证书把 ANCHOR_OUTSIDE_DIFFERENCE 从一个集合论标签提升为可枚举的角色和相位。
它仍不保证每个分离角色都对应 Type I/II 分解；决定性后续是证明某类角色必满足
(7) 与源关系相容，或把 LIFT_OBSTRUCTED 的核角色转入已有的核 Fourier、F/G
或良基递降分支。
