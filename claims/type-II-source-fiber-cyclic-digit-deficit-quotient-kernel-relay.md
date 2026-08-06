---
kind: claim
claim_id: type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
title: Type II 循环 ell-primary 数字缺口的商缺失—顶层核 Fourier 回执
statement: 设 H_a=C_{ell^a}、S 为固定参数纤维内合法二点关系块的和集、t 不属于 S。沿自然投影 H_a 到 H_j=C_{ell^j} 取第一个目标缺失层 j_0。若 j_0<a，则目标在严格较小的 ell-primary 商中缺失；若所有 j<a 的投影都命中，则顶层核 K_{a-1} 同构 C_ell 中的目标纤维是非空真子集，因而存在非平凡核角色和精确 Parseval Fourier 负证书。若所有精确赋值层都有 ell-1 个合法独立块，前一引理排除两种缺失；所以任意缺失都伴随某层 c_k<=ell-2。低商或核角色回译仍须通过 source-switch 参数纤维和源关系格相容性。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-source-fiber-anchor-separating-character-certificate
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-source-lattice-fibered-kneser-selector
topics:
- type-II
- source-fiber
- cyclic
- primary
- digit-deficit
- quotient
- kernel-fourier
- descent
- source-switch
- proof-program
sources:
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: layer-capacity-and-deficit
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: quotient-kernel-dichotomy
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: top-kernel-fourier-energy
  - claim: type-II-source-fiber-anchor-separating-character-certificate
    role: anchor-separation-negative-branch
visibility: public
last_checked: '2026-08-05'
---

# Type II 循环 \(\ell\)-primary 数字缺口的商缺失—顶层核 Fourier 回执

## \(\ell\)-primary 投影塔

令

\[
H_a=C_{\ell^a},\qquad
\pi_j:H_a\longrightarrow H_j=C_{\ell^j},
\qquad
K_j=\ker\pi_j,
\tag{1}
\]

其中 \(0\le j\le a\)，并令 \(S\subseteq H_a\) 是同一参数纤维内合法二点关系块
\(B_i=\{0,v_i\}\) 的和集。固定目标 \(t\notin S\)，记
\(S_j=\pi_j(S)\)、\(t_j=\pi_j(t)\)。因为 \(t_a\notin S_a\)，定义第一个缺失层

\[
j_0=\min\{j\in\{1,\ldots,a\}:t_j\notin S_j\}.
\tag{2}
\]

## 商缺失分支

若 \(j_0<a\)，则

\[
\boxed{t_{j_0}\notin S_{j_0}}
\tag{3}
\]

是一个严格较小的 \(\ell\)-primary 商中的目标缺失。把每个 \(v_i\) 投影到
\(C_{\ell^{j_0}}\)，所有原来赋值至少 \(j_0\) 的块变成零块；若对每个
\(k<j_0\) 都有至少 \(\ell-1\) 个精确层 \(k\) 的非零块，循环进位层终端会在
\(C_{\ell^{j_0}}\) 中覆盖全群，与 (3) 矛盾。因此存在

\[
\boxed{\exists k<j_0:\ c_k\le\ell-2.}
\tag{4}
\]

若该商目标纤维存在合法的 source-switch 参数，则 (3) 可作为严格较小状态的
目标缺失回执；若参数纤维为空，回执为低商 LIFT_OBSTRUCTED，而不是原模数
Type II 命中。

### 算术 source-switch 提升门

抽象商只有在满足下面的有限算术条件时，才可解释为实际 Type II 状态。固定当前
候选 \(D_0\mid D\)，取两两互素的来源块

\[
h_i\mid p+4D_0a_i,\qquad
h=\prod_{i\in J}h_i,\qquad
h\equiv-1\pmod{4D_0}.
\tag{A1}
\]

由来源 CRT 取 \(a_0\) 使
\(h\mid p+4D_0a_0\)。定义有限提升候选集

\[
\mathscr L_{D_0}(h,a_0;p)=
\left\{(D',A):
\begin{array}{l}
D'\mid D_0,\ A\mid D',\ D'/A\text{ 平方自由},\\
4AD'<p,\quad AD'\equiv D_0a_0\pmod h
\end{array}
\right\}.
\tag{A2}
\]

由于 \((h,4D_0)=1\)，有精确等价

\[
(D',A)\in\mathscr L_{D_0}(h,a_0;p)
\iff h\mid p+4AD'.
\tag{A3}
\]

又因 \(D'\mid D_0\)，\(h\equiv-1\pmod{4D'}\)。于是每个候选都给出

\[
K'=\frac{h+1}{4D'},\qquad
B'=\frac{K'p+A}{h},
\tag{A4}
\]

以及 Type II 正规形
\((A,D'/A,K')\)，且 \(B'>A\)。反向地，任何由同一来源混合因子 \(h\) 产生的
合法除子格 source-switch，必满足 (A2)；因此 (A2) 是完整的带来源提升判据，而非
启发式筛。

对第一个缺失层 \(j_0<a\)，按 (A2) 分派：

1. 若存在 \(D'<D_0\) 的候选，则抽象商有一个严格较小的算术 Type II 后继；
2. 若只有 \(D'=D_0\) 的候选，则这是同层 source-switch，若目标乘积达到 \(-1\)
   即直接输出 Type II 短证书，不能计作递降；
3. 若 \(\mathscr L_{D_0}(h,a_0;p)=\varnothing\)，则输出
   ARITHMETIC_LIFT_EMPTY；该数字缺口没有沿此混合因子提升到除子格的路径，
   必须转交顶层核 Fourier、另一条 Type I/II 射线或其它带势递降。

这一步把式 (3) 的“低模数候选”变成可枚举且保持来源标签的算术门；没有 (A2)，
不能把群论商缺失登记为全局递降。

## 顶层核分支

若 \(j_0=a\)，则对所有 \(j<a\) 都有 \(t_j\in S_j\)。特别地，
\(t_{a-1}\in S_{a-1}\)，定义顶层核截面

\[
F_t=\{k\in K_{a-1}:t+k\in S\}.
\tag{5}
\]

它满足

\[
\varnothing\ne F_t\subsetneq K_{a-1},
\qquad K_{a-1}\simeq C_\ell.
\tag{6}
\]

非空性来自 \(t_{a-1}\in S_{a-1}\)；若 \(F_t=K_{a-1}\)，则特别有
\(0\in F_t\)，即 \(t\in S\)，与假设矛盾。由 Parseval，

\[
\sum_{\substack{\psi\in\widehat{K_{a-1}}\\\psi\ne1}}
\left|\sum_{k\in F_t}\overline{\psi(k)}\right|^2
=|F_t|(\ell-|F_t|)>0.
\tag{7}
\]

故存在非平凡顶层核角色 \(\psi\) 及精确 Fourier 负证书。因为
\(K_{a-1}\simeq C_\ell\)，该角色可扩展为 \(H_a\) 上的角色；作为内禀角色，
\(\chi\circ\phi\) 自动满足真实源关系格的恒等式，因此这条 Fourier 负证书本身
不应标记为提升阻塞。只有在把它进一步解释成外部加法频率、指定低模商角色或
跨纤维参数相位时，才重新检查仿射相容性；失败时标记 LIFT_OBSTRUCTED。

## 缺口与二分完备性

前一引理说明若所有层 \(c_k\ge\ell-1\)，则 \(S=H_a\)，不可能出现
\(t\notin S\)。因此在 (2) 的任一缺失分支中必有某个精确层

\[
\boxed{c_k\le\ell-2.}
\tag{8}
\]

式 (8) 是数字缺口的算术定位；式 (3) 或 (7) 则分别给出可降模的候选入口或
顶层核 Fourier 入口。两者都保持同一 source-fiber 标签，不能把不同参数纤维的
块合并来消除缺口。

## 例子

在 \(C_4\) 中取两个 \(v=1\) 的块，\(S=\{0,1,2\}\)，目标 \(t=3\)。
模 \(2\) 投影命中，所以 \(j_0=2\)。顶层核为 \(\{0,2\}\)，
\(F_t=\{2\}\)；唯一非平凡二值角色在 \(F_t\) 上给出系数 \(-1\)。
这里精确层 \(1\) 的块数为零，正是 \(c_1\le 0=\ell-2\)。

在 \(C_9\) 中取四个 \(v=1\) 的块，\(S=\{0,1,2,3,4\}\)，目标 \(t=8\)。
模 \(3\) 投影命中而全群缺失，顶层截面为 \(F_t=\{3\}\)，给出三值核角色；
精确层 \(1\) 没有块，数字缺口被顶层 Fourier 直接显现。

## 研究边界

本回执把固定循环纤维的缺失压缩为“严格较小商缺失”或“顶层 \(C_\ell\) 核
Fourier”二分，并把缺口层数明确记录；式 (A2) 又给出低商分支的完整算术提升门。
尚未闭合的是：证明每个核心素数的某个缺失纤维都能找到非空的
\(\mathscr L_{D_0}(h,a_0;p)\)，或证明 ARITHMETIC_LIFT_EMPTY/LIFT_OBSTRUCTED
必能转成 Type I/F/G 证书或保持标记的良基递降。
