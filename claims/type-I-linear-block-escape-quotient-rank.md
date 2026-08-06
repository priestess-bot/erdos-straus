---
kind: claim
claim_id: type-I-linear-block-escape-quotient-rank
title: 线性两块 source escape 的商秩需求证书
statement: 设线性 F/G 状态的活跃源群为 H_act，线性两块奇部生成子群为 L_blk=<U°,V°>，并令 E=H_act/(H_act∩L_blk)。将目标纤维差分群投影到 E，记其 ell 初等商秩为 r_ell^esc。若该秩非零，则任何 alternate source、扩展 Hall 菜单或严格回译后继若要覆盖当前差分，至少必须提供 r_ell^esc 个独立的 ell 方向；两块高度不能填补该缺口。若所有候选 alternate 的投影都被有限 SNF/CRT/范围门排除，则得到 LINEAR_BLOCK_ESCAPE_ARITHMETIC_OBSTRUCTED；若候选菜单未封闭，则保留 LINEAR_BLOCK_ESCAPE_SOURCE_UNCLOSED。若投影差分为零，才可回到两块 source-map 的 SNF 四分。该证书不把相对两块商分离自动升级为原状态 G 证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-two-block-source-map-completeness
  - type-I-fg-role-snf-terminal-dispatch
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-source-fiber-elementary-rank-qheight-injection
topics:
- type-I
- linear-source
- source-map
- source-escape
- quotient-rank
- alternate-source
- Hall
- SNF
- CRT
- capacity
- proof-program
sources:
  - claim: type-I-linear-two-block-source-map-completeness
    role: block-subgroup-and-closed-branch
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: finite-source-menu-expansion
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: rank-to-source-capacity
visibility: public
last_checked: '2026-08-05'
---

# 线性两块 source escape 的商秩需求证书

## 1. 逃逸商

在线性状态中，令 \(H_{\rm act}\le H\) 是当前 Fourier/目标纤维实际使用的活跃源群，
并令

\[
L_{\rm blk}=\langle U^\circ,V^\circ\rangle.
\tag{1}
\]

设

\[
I_{\rm blk}=H_{\rm act}\cap L_{\rm blk},\qquad
E_{\rm esc}=H_{\rm act}/I_{\rm blk},\qquad
\pi_{\rm esc}:H_{\rm act}\to E_{\rm esc}.
\tag{2}
\]

对目标差分群 \(\Delta_Q\le H_{\rm act}\)，定义其逃逸像

\[
\overline{\Delta}_{\rm esc}
=\pi_{\rm esc}(\Delta_Q).
\tag{3}
\]

当 \(\overline{\Delta}_{\rm esc}=1\) 时，\(\Delta_Q\le L_{\rm blk}\)，两块 source-map
已经覆盖目标差分，可以调用
[线性两块 source-map 完备性](type-I-linear-two-block-source-map-completeness.md)
的 SNF 四分。否则两块模型缺少实际源方向；不能把
\(\operatorname{ord}(\chi)\)、块高度或 Fourier 幅度直接当作补偿。

## 2. 逃逸初等秩

对每个素数 \(\ell\)，定义

\[
\boxed{
r_\ell^{\rm esc}
=\dim_{\mathbb F_\ell}
\bigl(\overline{\Delta}_{\rm esc}/\ell\overline{\Delta}_{\rm esc}\bigr).
}
\tag{4}
\]

若 \(r_\ell^{\rm esc}>0\)，则输出最小 typed 请求

\[
\mathrm{LINEAR\_BLOCK\_ESCAPED\_RANK\_DEMAND}
(\ell,r_\ell^{\rm esc},E_{\rm esc},\overline{\Delta}_{\rm esc}).
\tag{5}
\]

这不是把两个块再收费一次，而是对**块外**源方向收费；同一 \(\ell\) 的多个角色只按
\(r_\ell^{\rm esc}\) 计数。

## 3. 最低 alternate-source 需求定理

令 \(W\le H_{\rm act}\) 是任意一组 alternate source 列所生成的子群。若它们与
两块源共同覆盖当前差分，即

\[
\Delta_Q\le\langle L_{\rm blk},W\rangle,
\tag{6}
\]

则在逃逸商中有

\[
\overline{\Delta}_{\rm esc}
\le
\pi_{\rm esc}(W).
\tag{7}
\]

有限阿贝尔群的子群初等商秩不超过母群，故

\[
\boxed{
r_\ell^{\rm esc}
\le
\dim_{\mathbb F_\ell}
\bigl(\pi_{\rm esc}(W)/\ell\pi_{\rm esc}(W)\bigr).
}
\tag{8}
\]

所以任意合法 alternate 菜单至少需要 \(r_\ell^{\rm esc}\) 个独立的 \(\ell\) 方向。
若菜单中的投影源列初等秩低于 (4)，则立即输出
\[
\mathrm{LINEAR\_BLOCK\_ESCAPE\_RANK\_INCONSISTENT}.
\tag{9}
\]

若每条候选 alternate 边都已通过 source-switch/SNF/CRT/范围门，(5) 可直接送入
Type II 的 Hall/Rado q 进需求图；若所有候选边均被有限障碍排除，则输出

\[
\mathrm{LINEAR\_BLOCK\_ESCAPE\_ARITHMETIC\_OBSTRUCTED}.
\tag{10}
\]

若候选菜单尚未证明完备，合法回执是

\[
\mathrm{LINEAR\_BLOCK\_ESCAPE\_SOURCE\_UNCLOSED},
\tag{11}
\]

不能把 (10) 当作“没有 alternate”。

## 4. 相对锚点分离的语义边界

若目标 \(t\in H_{\rm act}\) 满足

\[
\pi_{\rm esc}(t)\ne1,
\tag{12}
\]

则存在一个在 \(L_{\rm blk}\) 上恒等、在 \(t\) 上非恒的商角色；它证明目标相对于
**两块模型**是锚点外置。但当 \(H_{\rm act}\) 由 escaped source 列生成时，该角色
不一定在全部真实源列上恒等，因此不能直接登记为原状态的
\(\mathrm{G\_SUPPORT\_SEPARATION}\) 或全局严格下降。只有在 alternate 菜单也被该
角色湮灭，或其所有逃逸边均有明确障碍时，才可转入全源 annihilator/商 relay。

这一区分防止一个常见错误：

\[
\text{块模型中的商分离}
\;\not\Rightarrow\;
\text{原状态的 G 证书}.
\tag{13}
\]

## 5. 证明

由 (2)，\(\pi_{\rm esc}(L_{\rm blk})=1\)。若 (6) 成立，对商映射取像即得 (7)；再用
有限阿贝尔子群的初等商秩不超过母群，得到 (8)。若 \(r_\ell^{\rm esc}>0\)，
\(\Delta_Q\) 的块外像不能由两块源支付，故 (5) 是最小独立请求；若候选源列的
\(\ell\)-秩不足，(9) 是线性不相容。候选边全部失败时保存最小 SNF/CRT/范围行，
得到 (10)；菜单未封闭时只能给 (11)。最后，(12) 只使用
\(L_{\rm blk}\) 的湮灭角色，若逃逸源列上角色非平凡，则它不是原状态的全源分离，
得到 (13)。证毕。

## 6. 具体逃逸证书

取冻结线性状态

\[
(p,R,a,s)=(57{,}399{,}241,59,956{,}654,1).
\]

其

\[
K=846{,}638{,}805=3\cdot5\cdot2693\cdot20959,
\]

而两块为

\[
U=60,\qquad V=56{,}442{,}587,\qquad
U^\circ=15,\qquad V^\circ=56{,}442{,}587.
\]

在 \(U(59)\) 中，\(\langle2693,20959\rangle\) 的阶为 \(58\)，而
\(\langle15,56{,}442{,}587\rangle\) 的阶为 \(29\)。因此逃逸商是

\[
E_{\rm esc}\simeq C_2.
\]

两个活跃方向的差分像非平凡，故

\[
r_2^{\rm esc}=1.
\]

这给出一条明确的
\(\mathrm{LINEAR\_BLOCK\_ESCAPED\_RANK\_DEMAND}(2,1)\)：两块载体模型缺少一个
独立二阶方向。虽然 \(-1\) 在 \(U(59)\) 中不属于 29 阶块子群，因而有相对块模型的
二阶分离角色，但两个活跃源素数本身生成完整 58 阶群，所以不能把该角色直接写成
全局 G 证书；必须先处理这个 rank-1 alternate demand。

## 7. 研究边界

本卡把线性两块 source escape 从“source-map 未闭合”推进为一个可量化的商秩需求，
并给出具体冻结状态的 rank-1 证书。它仍未证明该需求必有 Type II 短证书或严格下降；
下一步应把 (5) 接入有限 Hall/Rado 菜单，或证明所有投影 alternate 边均有可提升
递降。若 \(r_\ell^{\rm esc}=0\)，才回到两块 SNF 四分；若非零，则禁止继续在块内
重复收费。
