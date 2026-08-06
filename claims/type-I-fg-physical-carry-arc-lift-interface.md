---
kind: claim
claim_id: type-I-fg-physical-carry-arc-lift-interface
title: F/G 相位到 E2 的物理 carry 短弧 lift 接口
statement: 固定 overflow 纤维 (p,A,d) 的 E2 carry 已由行列式在整条纤维上唯一确定，故有限相位行不能在纤维内选择性地修复 E2。只有一个已由独立算术命题证明 sound/complete 的跨 A/d/bundle source 与 transition universe，才可把每条物理行的实际整数 M_w、参数 a_w、短弧 u_w 与有限带标记像 (h_w,lambda_w) 结合为有限 E2 谓词。任何仅保存 (h,lambda) 的压缩不能自动推出 E2。坐标 Theta_a(M)=(M mod p,kappa_a(M)) 等价于 M mod ap，且有精确乘法 carry 律；E2 行集一般不乘法封闭，而仅以两个 Theta 状态不能决定 lcm carry。complete-excess 转移必须由外部物理账本或另一个经证明充分的增强状态重算 E2。本接口精确定位跨纤维 source-lift 缺口，不构成全局 source-completeness、短证书或递降定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-marked-source-menu-saturation
  - type-I-fg-phase-e2-carry-independence
  - type-I-overflow-cofactor-ledger-e2-gate
  - type-I-overflow-e2-fixed-fiber-constancy
  - type-I-high-anchor-e2-residue-arc-criterion
topics:
  - type-I
  - F-state
  - G-state
  - source-map
  - physical-carrier
  - carry
  - no-carry
  - E2
  - finite-abelian
  - SNF
  - lcm
  - proof-boundary
sources:
  - claim: type-I-fg-marked-source-menu-saturation
    role: finite-marked-phase-interface
  - claim: type-I-fg-phase-e2-carry-independence
    role: phase-only-no-go
  - claim: type-I-overflow-cofactor-ledger-e2-gate
    role: ledger-preserving-E2-equivalence
  - claim: type-I-overflow-e2-fixed-fiber-constancy
    role: fixed-fiber-carry-collapse
  - claim: type-I-high-anchor-e2-residue-arc-criterion
    role: short-arc-normal-form
visibility: public
last_checked: '2026-08-06'
---

# F/G 相位到 E2 的物理 carry 短弧 lift 接口

## 1. 同一物理行上的最小整数坐标

固定素数 \(p\)、\(A>0\) 与

\[
0<d<p,
\qquad
a=\frac{A}{(A,p-d)},
\tag{1}
\]

并考虑一个已经被独立算术定理证明完整的、固定参数纤维的物理 source 行集 \(W\)。每行
\(w\in W\) 必须保存一个真正的 overflow 行列式

\[
\bigl(w,M_w,h_w,\lambda_w\bigr),
\qquad
A\mid M_w,\qquad p\nmid M_w,
\qquad
\exists n_w>0:\quad pn_w=4dM_w+1,
\qquad
4M_w-n_w>p.
\tag{2}
\]

其中 \((h_w,\lambda_w)\) 是现有有限带标记 SNF/Fourier 投影，而 \(M_w\) 是这**同一行**的
实际整数 carrier。令

\[
u_w=\left[\frac{M_w}{a}\right]_p\in\{1,\ldots,p-1\},
\qquad
\kappa_w=\left\lfloor\frac{M_w}{p}\right\rfloor\bmod a
\in\{0,\ldots,a-1\}.
\tag{3}
\]

因为 \(a\mid A\mid M_w\) 且 \((a,p)=1\)，有

\[
M_w\equiv a u_w\pmod {ap},
\qquad
\boxed{\ \kappa_w=\left\lfloor\frac{a u_w}{p}\right\rfloor\ }.
\tag{4}
\]

令

\[
I_{p,a}=\left\{1,\ldots,\left\lfloor\frac{p-1}{a}\right\rfloor\right\}.
\tag{5}
\]

则有逐行的精确判据

\[
\boxed{
\kappa_w=0
\quad\Longleftrightarrow\quad
u_w\in I_{p,a}
\quad\Longleftrightarrow\quad
a\mid(M_w\bmod p)
\quad\Longleftrightarrow\quad
\mathrm{E2}(w).
}
\tag{6}
\]

**证明。** 写 \(M_w/a=pq+u_w\)，并将 \(au_w=pv+r\) 写成
\(0\le v<a\)、\(1\le r<p\)。于是
\(M_w=p(aq+v)+r\)，故 \(\kappa_w=v=\lfloor au_w/p\rfloor\)。这为零当且仅当
\(au_w<p\)，即 \(u_w\in I_{p,a}\)。最后一项与 E2 的等价正是带账本 cofactor 门。
证毕。

但这并不在固定纤维内制造 source 选择器。由固定纤维常值定理，所有 \(w\in W\) 的
\(M_w\bmod ap\)、\(u_w\)、\(\kappa_w\) 都相同；(6) 只能拒绝或接受整条
\((p,A,d)\) 纤维，不能由某个 Fourier/SNF 行命中来修复。

## 2. 跨纤维表与带标记 SNF 的精确拼接

要让 E2 对 source 行具有非平凡选择性，考虑固定 \(p\)、但允许跨越
\((A,d,\text{bundle})\) 的物理行集 \(\mathcal W\)。每行必须带有自己的参数与真正的
行列式：

\[
\bigl(w,A_w,d_w,M_w,n_w,h_w,\lambda_w,\operatorname{fac}(M_w)\bigr),
\qquad
A_w\mid M_w,
\qquad
pn_w=4d_wM_w+1,
\qquad
4M_w-n_w>p.
\tag{7}
\]

令

\[
a_w=\frac{A_w}{(A_w,p-d_w)},
\qquad
u_w=\left[\frac{M_w}{a_w}\right]_p,
\qquad
\kappa_w=\left\lfloor\frac{M_w}{p}\right\rfloor\bmod a_w.
\tag{8}
\]

假设 \(\mathcal W\) **及其声明的 physical transition relation** 对所指定的
admissible source/edge universe 都已经由独立算术定理证明 sound 且 complete，且带标记
菜单/目标表已经在投影 \((h_w,\lambda_w)\) 上通过 source 饱和、目标相位和固定阶角色门。
则一个跨纤维 E2 谓词回执必须同时给出：

\[
\begin{array}{c|c}
\text{回执字段}&\text{它排除的缺口}\\ \hline
\text{完整的行 ID 集及参数 }(w,A_w,d_w)&\text{遗漏的实际 source/chart}\\
(h_w,\lambda_w)&\text{有限相位或标记关系矛盾}\\
M_w,\operatorname{fac}(M_w),u_w&\text{同一行的 E2 carry 或 lcm 账本失败}\\
\text{已验证的 physical transition relation}&\text{把算术 row 误当作可提升边}
\end{array}
\tag{9}
\]

在这些前提下，遍历同一行 ID 上的相位门与
\(u_w\in I_{p,a_w}\) 对谓词“相位相容且 E2 通过的物理行”是 sound 且 complete：
完整性来自 \(\mathcal W\) 与 transition relation 的穷尽，正确性由 (6) 在每行参数上
逐行给出。这仍不是 E1--E5 递归边的充分条件。

两个有相同 \((h,\lambda)\) 但不同 \(M\) 的行不能仅由群像合并；若另有算术定理证明其
\(u\) 一致，至多可合并 E2 判定。即使 \(u\) 一致，只要 factor profile 或 transition
不等价，后继边和 lcm 行为仍不得合并。

这正是现有 marked-SNF 能够与不能够做的分界。它可在已证明完整的有限 universe 上完成
相位层，却不能仅从群像和标签推出 (6)；\(p=73,A=d=18,M=1242\) 的相位饱和而 E2
失败的反模型已经严格排除了这种推断。

## 3. carry 的精确乘法律

为说明后继 transition relation 必须保存何种信息，暂对任意正整数定义

\[
M=pq+r,
\qquad
0\le r<p,
\qquad
\kappa_a(M)=q\bmod a.
\tag{8}
\]

对 \(N=pt+s\)，记

\[
c(r,s)=\left\lfloor\frac{rs}{p}\right\rfloor,
\qquad
r\odot s=rs-pc(r,s).
\tag{9}
\]

则

\[
\boxed{
\kappa_a(MN)\equiv
p\kappa_a(M)\kappa_a(N)
s\kappa_a(M)+r\kappa_a(N)+c(r,s)\pmod a.
}
\tag{10}
\]

故

\[
\Theta_a(M)=\bigl(M\bmod p,\kappa_a(M)\bigr)
\tag{11}
\]

等价于 \(M\bmod ap\)，并以 (10) 成为乘法幺半群的精确有限坐标。其 digit-carry
满足结合律强制的恒等式

\[
\tau c(r,s)+c(r\odot s,\tau)
=r c(s,\tau)+c(r,s\odot\tau).
\tag{12}
\]

其中 \(\tau\in\{0,\ldots,p-1\}\) 是第三个模 \(p\) 残数。

但 \(\kappa_a\) 单独既不是乘法同态，也不是普通的加性余循环。特别地，若两个
\(A\)-整除 carrier 都通过 E2，则其残数 \(r,s\) 均被 \(a\) 整除，而 (10) 退化为

\[
\kappa_a(MN)\equiv c(r,s)\pmod a.
\tag{13}
\]

所以 E2 接受集一般不乘法封闭。这个命题只描述整数合成，不声称 \(MN\) 仍落在同一个
Type I 行列式纤维。

在核心域内，取

\[
p=73,
\qquad d=1,
\qquad A=27,
\qquad a=3,
\qquad M=675.
\tag{14}
\]

有 \(73\cdot37=4\cdot675+1\)、\(M\bmod73=18\) 及 \(\kappa_3(M)=9\equiv0\pmod3\)，
故这是一个通过 E2 的实际 overflow carrier；但

\[
\kappa_3(M^2)=\left\lfloor\frac{455625}{73}\right\rfloor
=6241\equiv1\pmod3.
\tag{15}
\]

更强地，在固定 \((p,d,A)\) 的物理 overflow 纤维中，所有 carrier 都有相同残数

\[
r_d\equiv-(4d)^{-1}\pmod p.
\tag{16}
\]

两个有效 physical carrier 的乘积仍留在该 fixed-\(d\) 纤维，当且仅当
\(r_d^2\equiv r_d\pmod p\)，即 \(r_d=1\)。若 \(a>1\) 且 E2 通过，又必须
\(a\mid r_d\)，矛盾。因此非平凡 E2 分支没有同一 fixed-\(d\) 物理 carrier 族的
乘法闭包。

## 4. complete-excess 的 lcm 边界

`complete-excess` 使用 \(\operatorname{lcm}\)，它比 (10) 需要更多信息。即使两行都有
相同的 \(\Theta_a\)，其 lcm 的 \(\kappa\) 仍依赖完整的 \(\gcd\) 与素数赋值账本。
仍取 (14)，三个同一 \((p,d,A)\) 物理纤维中的 carrier

\[
675,\qquad2646,\qquad10530
\tag{17}
\]

都满足 \(\Theta_3=(18,0)\)。然而

\[
\kappa_3\bigl(\operatorname{lcm}(675,2646)\bigr)
=\kappa_3(66150)=0,
\tag{18}
\]

而

\[
\kappa_3\bigl(\operatorname{lcm}(675,10530)\bigr)
=\kappa_3(52650)=1.
\tag{19}
\]

这里的两个 lcm 已离开原 fixed-\(d\) 纤维：

\[
4\cdot66150+1\equiv49\pmod {73},
\qquad
4\cdot52650+1\equiv69\pmod {73}.
\tag{20}
\]

它们只是跨 chart/complete-excess 候选，而不是该纤维的新 carrier。因此不存在只以两个
有限 \(\Theta\) 状态为输入的确定性 lcm carry transition。对于
\(M=\operatorname{lcm}(A,Q)\) 的 complete-excess 发生器，\(\Theta\)-压缩必须由外部
物理 factor profile、实际整数求值，或另一个经独立证明充分的增强状态补回；本例不排除
某个先验有限 universe 存在这样的更强状态。

## 5. 对主目标的精确收束

这张卡把下一个缺口缩为一个可判定对象：对每个候选 F/G source universe，证明一个带
row ID 与 \((A_w,d_w)\) 的跨纤维物理表
\((M_w,h_w,\lambda_w,\operatorname{fac}(M_w))\) 完整，并为实际 product/lcm 变换给出
sound/complete 的 transition relation；随后只接受同一行上同时通过相位与短弧 (6) 的
source。它没有构造这样的全局表，也没有把 E2 通过升级为 E1、E3--E5、Type I/II
短证书或严格可提升递降。
