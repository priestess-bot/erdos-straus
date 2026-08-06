---
kind: claim
claim_id: type-II-hall-surplus-stabilizer-absorption-quotient-relay
title: Type II Hall surplus 稳定子吸收的商递降—Fourier 二分
statement: 在同一已实现参数纤维的有序源块积集中，若 Hall surplus 的某些槽在插入时被逐步稳定子吸收，则这些块全部落入最终稳定子并在 H/T_s 商中消失。若目标 t 不在最终积集 P_s，则商目标 tT_s 仍缺失；当 T_s 非平凡且候选降模核 K 包含于 T_s 并通过源盒格 SNF 门时，得到严格可提升的较小商 relay。当核不包含或盒不饱和时，输出 KERNEL_SOURCE_ANNIHILATOR/KERNEL_BOX_FOURIER；T_s 平凡时只删除平凡源块，不能把吸收本身写成整数递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-surplus-kneser-price-injection
  - type-II-full-match-stabilizer-relay-certificate
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-stabilizer-kernel-failure-dual-certificate
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
topics:
- type-II
- Hall
- surplus
- stabilizer
- absorption
- quotient-descent
- Fourier
- source-lattice
- source-switch
- proof-program
sources:
  - claim: type-II-hall-surplus-kneser-price-injection
    role: absorbed-surplus-input
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: kernel-inclusion-SNF-gate
  - claim: type-II-stabilizer-kernel-failure-dual-certificate
    role: failed-kernel-dual-output
visibility: public
last_checked: '2026-08-05'
---

# Type II Hall surplus 稳定子吸收的商递降—Fourier 二分

## 1. 有序积集与吸收槽

固定一个已经通过 FIBER_REALIZED 的参数纤维，令
\[
P_0=A_0,\qquad P_j=P_{j-1}D_j,\qquad
T_j=\operatorname{Stab}_H(P_j),
\quad 1\le j\le s,
\tag{1}
\]
其中 \(D_j=\{1,g_j,\ldots,g_j^{e_j}\}\) 是锚槽或 Hall surplus 槽的真实源块。
稳定子单调：
\[
T_{j-1}\le T_j\le T_s.
\tag{2}
\]
定义被吸收的 surplus 位置
\[
J_{\mathrm{abs}}
=\{j:\ j\text{ 是 surplus 槽且 }g_j\in T_j\},
\qquad
\eta_{\mathrm{abs}}=|J_{\mathrm{abs}}|.
\tag{3}
\]
若 \(j\in J_{\mathrm{abs}}\)，则 \(D_j\subseteq T_j\subseteq T_s\)，所以
\[
\pi_s(D_j)=\{T_s\}
\quad\text{对}\quad
\pi_s:H\to H/T_s.
\tag{4}
\]
吸收槽不产生新的商容量，\(\eta_{\mathrm{abs}}\) 只能作为未定价 surplus 记录。

## 2. 目标缺失的商投影

令
\[
\bar H=H/T_s,\qquad
\bar P=P_s/T_s,\qquad
\bar t=tT_s.
\tag{5}
\]
由于 \(P_sT_s=P_s\)，有精确饱和恒等式
\[
P_s=\pi_s^{-1}(\bar P).
\tag{6}
\]
因此
\[
\boxed{
t\notin P_s\Longrightarrow \bar t\notin\bar P.
}
\tag{7}
\]
由 (4)，删去全部 \(J_{\mathrm{abs}}\) 中的块不改变 \(\bar P\)；被吸收的 Hall
surplus 不得再次进入 \(H/T_s\) 的容量账本。

若 \(1<|T_s|<|H|\)，则
\[
|\bar H|=|H|/|T_s|<|H|.
\tag{8}
\]
这给出抽象有限群势的严格下降。若 \(T_s=H\)，则 (6) 迫使 \(P_s=H\)，与
目标缺失矛盾；若 \(T_s=1\)，吸收条件 \(g_j\in T_j\) 只可能对应
\(g_j=1\) 的平凡源块，输出 TRIVIAL\_SOURCE\_PRICE，不声称商递降。

## 3. 可提升商与核门

取候选低模映射
\[
\pi:G=U(4D_*)\longrightarrow \bar G=U(4D'),
\qquad
K=\ker\pi.
\tag{9}
\]
若
\[
K\le T_s
\tag{10}
\]
且源盒格判据给出 KERNEL\_STABILIZER\_CERT，则
\[
P_s=\pi_s^{-1}(\bar P)
\]
与参数标签、source-switch 和 E1--E5 提升门相容；式 (7) 的商缺失成为严格较小
的可提升 Type II 后继。该后继的势第一坐标由 \(|H|\) 降至 \(|\bar H|\)，并且
保持来源标签。

若 (10) 不能通过，则不把 (7) 写成递降。按核失败二分输出：

* \(K\not\le\operatorname{im}\varphi\)：KERNEL\_SOURCE\_ANNIHILATOR；
* \(K\le\operatorname{im}\varphi\) 但指数盒不具 K 不变性：
  KERNEL\_BOX\_FOURIER；
* 目标在低模商命中但原模缺失：KERNEL\_SPLIT\_FOURIER 或
  source-fiber 负证书。

这些角色均须继续通过整数关系格；角色存在本身不是核心素数下降。

## 4. 证明

由 (2)，若 \(g_j\in T_j\)，则 \(D_j\subseteq T_j\subseteq T_s\)，得到 (4)。
稳定子定义给出 \(P_sT_s=P_s\)，故 \(P_s\) 是每个 \(T_s\)-陪集的并，得到
(6)；若 \(t\notin P_s\)，其整个陪集 \(tT_s\) 与 \(P_s\) 不交，从而
\(\bar t\notin\bar P\)，即 (7)。

当 \(1<|T_s|<|H|\) 时 (8) 是严格群阶下降。若候选核满足 (10)，源盒格判据把
该抽象商提升为真实低模参数纤维；若不满足，源子群外置或盒平移差分别给出
KERNEL\_SOURCE\_ANNIHILATOR/KERNEL\_BOX\_FOURIER。\(T_s=1\) 和 \(T_s=H\)
是上面的两个边界分支，证毕。

## 5. 边界例子

### 非平凡吸收与商缺失

取加法群 \(H=C_4\)、\(A_0=\{0\}\)、唯一源块
\(D_1=\{0,2\}\)。则
\[
P_1=\{0,2\},\qquad T_1=\{0,2\},
\qquad H/T_1\simeq C_2.
\]
目标 \(t=1\) 在原群缺失，投影目标在 \(C_2\) 中仍为非零元，商缺失严格保留；
若该商有合法低模 source-switch，则给出下降，否则保存核门失败。

### 平凡吸收

若 \(D_j=\{0\}\)，则 \(T_j\) 不变，且 \(g_j=0\)；该槽只输出
TRIVIAL\_SOURCE\_PRICE，不贡献 Hall/Kneser 容量，也不降低商阶。

### 核不包含

若 \(T_s=\{0,4\}\le C_8\)，但候选核含 \(2\notin T_s\)，则低模商的源盒不满足
核稳定子门；即使商中出现目标命中，也只能输出 KERNEL\_SOURCE\_ANNIHILATOR
或 KERNEL\_BOX\_FOURIER，不能回升原模数。

## 研究边界

该桥把 HALL\_SURPLUS\_UNPRICED 的稳定子吸收分支变成“严格商缺失或规范核
Fourier”的二分，证明被吸收槽不应再次收费。仍需证明候选核 (10) 的 source-box
SNF 门在足够多核心纤维中成立，或证明其失败 Fourier/算术回执必转为
Type I/F/G、广义 \(2^j\) 终端或保持标签的严格下降。
