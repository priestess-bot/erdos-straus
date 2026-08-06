---
kind: claim
claim_id: type-I-linear-block-escape-hall-annihilator-closure
title: 线性 block escape 到 alternate-source Hall—annihilator 闭合三分
statement: 对线性两块 source escape 的 ell 初等需求，固定逃逸商 E 的需求子空间 D_ell 和一个已经声明有限的 alternate-source 菜单。将每个通过 source-switch、SNF、CRT 与范围门的候选列作为有限槽；若 Rado/Hall 匹配覆盖 D_ell，则得到 source-closed 的 alternate 请求并进入 Type II q 进容量账本。若菜单完备、所有真实源列均已通过或有明确算术障碍，且匹配失败，则 Rado 对偶角色湮灭全部可用源列：目标相位非平凡时进入全源 annihilator 商递降，目标相位平凡时进入关系 Fourier/顶层终端。若菜单未完备或存在未分类边，则只输出 ESCAPE_SOURCE_UNCLOSED/ESCAPE_ARITHMETIC_OBSTRUCTED，不能伪造下降。该桥把线性 block escape 的 rank demand 变成有限可判定的 Type II/商/障碍分派。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-block-escape-quotient-rank
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-hall-source-column-closure-relay
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
- type-I
- linear-source
- block-escape
- alternate-source
- Hall
- Rado
- annihilator
- q-rank
- quotient-descent
- Type-II
- SNF
- proof-program
sources:
  - claim: type-I-linear-block-escape-quotient-rank
    role: escaped-rank-demand
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: Rado-dual
  - claim: type-II-hall-source-column-closure-relay
    role: annihilator-relay
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: finite-menu-expansion
visibility: public
last_checked: '2026-08-05'
---

# 线性 block escape 到 alternate-source Hall—annihilator 闭合三分

## 1. 逃逸需求与有限槽

沿用逃逸商

\[
E_{\rm esc}=H_{\rm act}/(H_{\rm act}\cap L_{\rm blk}),
\qquad
V_\ell=E_{\rm esc}[\ell]/\ell E_{\rm esc}[\ell].
\tag{1}
\]

令

\[
D_\ell\le V_\ell
\tag{2}
\]

是目标差分逃逸像的 \(\ell\)-初等商需求，维数为
\(r_\ell^{\rm esc}\)。选择一个独立需求基
\(d_1,\ldots,d_r\)，其中 \(r=r_\ell^{\rm esc}\)。

alternate-source 菜单是有限槽集合 \(\mathcal C\)。每个槽 \(c\) 带有：

* 逃逸商源向量 \(w_c\in V_\ell\)；
* 一个具体整数标签、参数纤维和 source-switch 记录；
* 通过或失败的 SNF、CRT、范围和互素性门；
* 它可以承接的独立需求索引集合 \(N(c)\subseteq\{1,\ldots,r\}\)。

只把所有算术门通过的槽放入 \(\mathcal C^+\)。对 \(I\subseteq\{1,\ldots,r\}\)，定义

\[
N(I)=\{c\in\mathcal C^+:
N(c)\cap I\ne\varnothing\}.
\tag{3}
\]

菜单的 **source-complete** 条件是：每个实际 escaped source 列都在 \(\mathcal C\)
中出现，或者其全部候选边均附有可复核的算术失败载荷；未枚举的列不能默认为不
存在。

## 2. Rado/Hall 匹配分支

若对于每个 \(I\subseteq\{1,\ldots,r\}\) 都有

\[
|N(I)|\ge |I|,
\tag{4}
\]

并且相应槽向量可以选择为独立的 \(r\) 个源方向，则有限 Rado/Hall 定理给出一个
注入匹配

\[
\mathfrak m:\{d_1,\ldots,d_r\}\hookrightarrow\mathcal C^+.
\tag{5}
\]

记录

\[
\boxed{\mathrm{LINEAR\_ESCAPE\_ALTERNATE\_MATCHED}}
\tag{6}
\]

并把这些实际标签作为新的 source-closed 请求送入 Type II 的 q 进容量、Kneser
稳定子和单 q 来源纤维闭包。匹配本身不是 Type II 命中；只有后续目标积集命中或
稳定子/整数势门通过后，才升级 Type II/verified descent。

## 3. 匹配失败的对偶分支

若 (4) 对某个最小 \(I_0\) 失败，则 Rado 对偶给出一个非零线性泛函

\[
\lambda\in V_\ell^\*,\qquad
\lambda(w_c)=0\quad(c\in N(I_0)),\qquad
\lambda(d_i)\ne0\ \text{for some }i\in I_0.
\tag{7}
\]

### 3.1 source-complete 且所有真实列已闭合

若 source-complete 菜单中所有真实源列都已通过或已有明确失败载荷，并且通过的源列
张成空间正是 \(W_{\rm src}\)，而

\[
\lambda|_{W_{\rm src}}=0,
\tag{8}
\]

则 \(\lambda\) 可提升为当前固定纤维上的阶 \(\ell\) 角色。令目标逃逸像为
\(\tau_{\rm esc}\)：

* 若 \(\lambda(\tau_{\rm esc})\ne0\)，则
  \(\ker\lambda\) 包含全部源集而不含目标，输出
  \[
  \mathrm{LINEAR\_ESCAPE\_GLOBAL\_ANNIHILATOR}
  \tag{9}
  \]
  并调用全源列闭合的商 relay；当核非平凡且整数 source-switch 通过时，这是严格
  较小群/模数的可提升递降。
* 若 \(\lambda(\tau_{\rm esc})=0\)，角色不分离目标，输出
  \[
  \mathrm{LINEAR\_ESCAPE\_RELATION\_FOURIER}
  \tag{10}
  \]
  并将其送入源关系 SNF、顶层 primary 或另一个 source-map；不得把它重复收费为
  目标 q-height。

若 \(\ker\lambda=1\)，(9) 退化为顶层 primary annihilator；不得虚构同阶递降。

### 3.2 算术边失败

若某个实际 escaped source 列的所有候选边都通过有限菜单被 SNF/CRT/范围门排除，
则保存最小失败行并输出

\[
\mathrm{LINEAR\_ESCAPE\_ARITHMETIC\_OBSTRUCTED}.
\tag{11}
\]

该回执可转入 Type I/F/G 或另一个 Type II 菜单，但不直接等于严格下降。

### 3.3 菜单未闭合

若存在未枚举的 alternate source 列、未证明完备的标签表或跨纤维 source-switch，
则输出

\[
\mathrm{LINEAR\_ESCAPE\_SOURCE\_UNCLOSED}.
\tag{12}
\]

即使有限已知菜单上 Hall 明显失败，也不能据此调用 (9)；未知列可能携带
\(\lambda\) 不湮灭的源方向。

## 4. 有限扩张与良基性

若匹配失败且存在 \(\lambda\)-逃逸的未纳入源列，调用
[源列逃逸的有限独立请求扩张桥](type-II-source-column-escape-finite-expansion-relay.md)。
每加入一个独立外部请求，需求基的已覆盖维数增加至少一，势

\[
\Psi_{\rm esc}=r_\ell^{\rm esc}
-\dim(\text{已覆盖的 }D_\ell)
\tag{13}
\]

严格下降。由于 \(r_\ell^{\rm esc}\) 有限，扩张不可能循环；终止时只能进入
(6)、(9)、(10)、(11) 或 (12)。

注意 (13) 是请求扩张势，不是原素数的递降势；只有 (9) 的整数 relay 或 (6) 后续
真正通过 Type II/Kneser 才能升级原猜想的递归边。

## 5. 证明

条件 (4) 是有限向量拟阵的 Rado/Hall 条件，给出 (5)。若其失败，Rado 对偶构造
(7)。在 source-complete 且 (8) 成立时，\(\lambda\) 在所有实际源列上为零，故
可提升为固定纤维的有限角色；目标相位非零时，核商严格分离源集和目标，调用全源
annihilator relay，目标相位为零时只能留下关系 Fourier。若实际源列的算术边失败，
其最小 SNF/CRT/范围行是 (11)；菜单不完备时必须保留 (12)。有限扩张每步增加已
覆盖的独立需求维数，故 (13) 严格下降并终止。证毕。

## 6. 三个最小边界

### 匹配

取 \(V_\ell=\mathbb F_\ell\)、\(D_\ell=\langle e_1\rangle\)，一个通过全部算术门的
槽 \(c\) 带 \(w_c=e_1\)。则 (4) 通过，输出
\(\mathrm{LINEAR\_ESCAPE\_ALTERNATE\_MATCHED}\)。

### 完备菜单下的 annihilator

取 \(V_\ell=\mathbb F_\ell^2\)、\(D_\ell=V_\ell\)，但完整可用菜单只有
\(w_1=e_1\)。Hall 在 \(I=\{e_1,e_2\}\) 上失败；\(\lambda=e_2^\*\) 湮灭全部可用源列。
若目标像为 \(e_2\)，得到 (9)；若目标像为 0，得到 (10)。

### 未闭合菜单

仍取 \(V_\ell=\mathbb F_\ell^2\)，已知菜单只有 \(e_1\)，但尚未证明没有
\(e_2\)-源列。此时不能使用 \(e_2^\*\) 作全源 annihilator，必须输出 (12)。

## 7. 研究边界

本卡完成了线性 block escape rank demand 到有限 alternate-source/Hall/Rado/annihilator
的结构闭合。它仍未证明实际 Erdős--Straus 线性状态的 alternate 菜单始终
source-complete，也未证明匹配后的源请求必然达到 Kneser 命中或严格整数下降。全局
剩余因此具体化为：

1. 证明一个可检索的有限 alternate source 菜单及其 source-complete 性；
2. 证明 \(\mathrm{LINEAR\_ESCAPE\_ALTERNATE\_MATCHED}\) 后的 Type II 目标纤维
   闭包；
3. 将 source-complete 的 annihilator 分支转成满足 E1--E5 的严格 relay。
