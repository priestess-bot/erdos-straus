---
kind: claim
claim_id: type-II-kernel-fourier-support-uncertainty-demand
title: Type II 核 Fourier 支撑不确定性下界与 simultaneous-role 容量门
statement: 对有限阿贝尔核 K 中的非空真目标截面 S_t，非零 Fourier 支撑满足 |supp(F_t)|>=ceil(|K|/|S_t|)，因而非平凡支撑至少有 ceil(|K|/|S_t|)-1 个角色；但该数量只是候选角色证书，只有在同一构造中同时映射到互异 q 槽、且其源关系限制线性独立并共同实现的角色才可计入 Hall/q 容量。否则必须输出 Fourier 支撑证书而非容量需求；C4 的两点截面给出按非零系数数量收费的反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-kernel-fourier-energy-role-capacity-dispatch
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-annihilator-two-sided-subgroup-quotient-descent
topics:
- type-II
- kernel-fourier
- support
- uncertainty
- simultaneous-role
- capacity
- Hall
- Rado
- source-relation
- counterexample
- proof-program
sources:
  - claim: type-II-kernel-fourier-energy-role-capacity-dispatch
    role: parseval-energy-role-dispatch
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: independent-role-capacity
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: affine-source-compatibility
visibility: public
last_checked: '2026-08-05'
---

# Type II 核 Fourier 支撑不确定性下界与 simultaneous-role 容量门

## 1. 支撑下界

令 \(K\) 为有限阿贝尔群，记

\[
N=|K|,\qquad S_t\subset K,\qquad n=|S_t|,
\qquad 0<n<N,
\]

并采用未归一化 Fourier 变换

\[
F_t(\chi)=\sum_{x\in S_t}\overline{\chi(x)},
\qquad \chi\in\widehat K.
\tag{1}
\]

定义全支撑与非平凡支撑

\[
\Sigma_t=\{\chi:F_t(\chi)\ne0\},
\qquad
\Sigma_t^\circ=\Sigma_t\setminus\{1\}.
\tag{2}
\]

平凡角色的系数为 \(F_t(1)=n\)。Parseval 给出

\[
\sum_{\chi\in\widehat K}|F_t(\chi)|^2=Nn,
\qquad
\sum_{\chi\ne1}|F_t(\chi)|^2=n(N-n).
\tag{3}
\]

另一方面，每个系数满足 \(|F_t(\chi)|\le n\)。令

\[
r_{\mathrm{supp}}=|\Sigma_t^\circ|,
\]

则

\[
n(N-n)
\le r_{\mathrm{supp}}n^2.
\]

所以得到一个完全可计算的有限群支撑下界

\[
\boxed{
r_{\mathrm{supp}}
\ge \left\lceil\frac{N-n}{n}\right\rceil
=\left\lceil\frac Nn\right\rceil-1,
\qquad
|\Sigma_t|\ge\left\lceil\frac Nn\right\rceil.
}
\tag{4}
\]

这是由 Parseval 和逐项幅度上界得到的支撑型不确定性下界；它不声称已经达到
Donoho--Stark 一类更强的有限群不确定性常数，也不把支撑个数自动解释成独立
源方向。

## 2. 相容性与支撑负证书

沿用核 Fourier 能量分派中的源关系格相容角色集合
\(\mathcal X_{\mathrm{comp}}\)。在非平凡支撑上定义

\[
\Sigma_{\mathrm{comp}}=\Sigma_t^\circ\cap\mathcal X_{\mathrm{comp}},
\qquad
\Sigma_{\mathrm{obs}}=\Sigma_t^\circ\setminus\mathcal X_{\mathrm{comp}}.
\tag{5}
\]

若 \(\Sigma_{\mathrm{obs}}\ne\varnothing\)，按

\[
\bigl(\operatorname{ord}\chi,-|F_t(\chi)|^2,
\operatorname{SNF\_index}(\chi)\bigr)
\]

的字典序选取规范角色 \(\chi_{\mathrm{obs}}\)，并输出

\[
\mathrm{FOURIER\_SUPPORT\_LIFT\_OBSTRUCTED}
 =\bigl(K,S_t,\chi_{\mathrm{obs}},F_t(\chi_{\mathrm{obs}}),
        \Sigma_t^\circ,\Sigma_{\mathrm{obs}}\bigr).
\tag{6}
\]

这是一个带精确非零系数的有限负证书；不相容角色不能进入 q-height、Kneser 或
Hall 价格。若同时存在相容支撑，只能把相容部分另行处理，不能用它抵销式 (6)
中的 lift 障碍。

若 \(\Sigma_{\mathrm{obs}}=\varnothing\)，式 (4) 只说明候选相容角色至少有
\(r_{\mathrm{supp}}\) 个；下一节的 simultaneous-role 门仍然是容量计费的必要条件。

## 3. simultaneous-role 不是默认事实

令 \(A\subseteq\Sigma_{\mathrm{comp}}\) 为准备送入容量证明的角色集。称
\(A\) 满足 **SIMULTANEOUS_ROLE**，若证书中同时给出下列数据：

1. 一个到当前合法源槽集合 \(C_q\) 的单射
   \(\iota:A\hookrightarrow C_q\)；不同角色使用不同 q 槽，且同一槽的重复 q
   账本已被去重；
2. 每个角色在相同的源关系商或同一 primary 层上有源限制向量
   \(d_\chi\)，并证明 \(\{d_\chi:\chi\in A\}\) 线性独立；
3. 同一个源选择同时满足所有角色的相位/非零系数约束，而不是为每个角色分别
   选择一套互不兼容的源块；
4. 每个 \(\iota(\chi)\) 的 SNF、范围和来源标签回译均已通过。

只有在这四项都成立时，才定义

\[
r_{\mathrm{sim}}=|A|
\]

为真实的 typed demand。若只知道式 (4) 的支撑个数，或角色限制向量有依赖，或
不同角色需要相互冲突的源选择，则回执为

\[
\mathrm{FOURIER\_SUPPORT\_NOT\_A\_DEMAND}
 = (\Sigma_t^\circ,A,r_{\mathrm{supp}},r_{\mathrm{sim}},\text{reason}),
\tag{7}
\]

并保留支撑列表和精确系数作为 Fourier 证书，不得按 \(r_{\mathrm{supp}}\) 收费。
特别地，\(r_{\mathrm{sim}}\) 不能仅由 Parseval 能量、角色阶或非零系数数量定义。

## 4. 通过 simultaneous-role 后的 Hall/q 分派

在 SIMULTANEOUS_ROLE 已通过的前提下，把 \(A\) 的角色限制向量作为 Rado 请求。
对任意请求子集 \(U\subseteq A\)，令 \(W(U)\) 为其合法源槽向量张成空间，令
\(\mathsf C_q(U)\) 为相同来源标签和 q 层账本允许的独立槽容量。若

\[
\operatorname{rank}W(U)<|U|,
\]

先输出

\[
\mathrm{KERNEL\_FOURIER\_SUPPORT\_RANK\_DEFICIT}(U,
\operatorname{rank}W(U),|U|),
\]

而不是把缺口写成 Fourier 能量不足。若线性 Rado 条件通过，再检查分层 q 容量：

\[
\mathsf C_q(U)<|U|
\quad\Longrightarrow\quad
\mathrm{KERNEL\_FOURIER\_SUPPORT\_CAPACITY\_DEFICIT}
  (U,\mathsf C_q(U),|U|).
\tag{8}
\]

只有所有请求子集都通过，才允许把这组角色送入 Kneser 稳定子价格或 Type II
目标纤维回译。式 (8) 的需求是 \(r_{\mathrm{sim}}\) 个独立角色的需求，不是
\(r_{\mathrm{supp}}\) 条系数的自动总和。

## 5. 证明

式 (3) 是有限阿贝尔群 Fourier Parseval 恒等式。因为平凡系数为 \(n\)，非平凡
能量为 \(n(N-n)\)；又因每个系数的模长不超过 \(n\)，若只有
\(r_{\mathrm{supp}}\) 个非零非平凡系数，则能量至多为
\(r_{\mathrm{supp}}n^2\)，从而得到 (4)。

相容/不相容划分只是对有限角色支撑做集合分割，因此存在不相容非零系数时，(6)
是直接的规范负证书。SIMULTANEOUS_ROLE 的四个条件分别保证角色没有重复槽、没有
线性依赖、没有相互冲突的独立构造，并且确实属于当前算术纤维；因此只有在这些
条件下，角色集才可作为 Rado 请求。Rado 定理和分层 q 容量切割随后给出 (8)。
若任一条件缺失，不能推出独立需求，故 (7) 是唯一保守的回执。证毕。

## 6. C4 反例：支撑数量不能直接收费

取加法群

\[
K=C_4=\{0,1,2,3\},
\qquad S_t=\{0,1\},
\]

并令 \(\chi_j(x)=i^{jx}\)。则

\[
F_t(\chi_0)=2,
\quad F_t(\chi_1)=1-i,
\quad F_t(\chi_2)=0,
\quad F_t(\chi_3)=1+i.
\tag{9}
\]

所以

\[
\Sigma_t^\circ=\{\chi_1,\chi_3\},
\qquad r_{\mathrm{supp}}=2,
\]

而式 (4) 只要求 \(r_{\mathrm{supp}}\ge1\)。若把两个非零非平凡系数都当作
两个独立 q 需求，便会错误地收费两次：一个源块

\[
B=\{0,1\}
\]

已经同时生成整个截面 \(S_t\)，当前构造没有两个互异源槽，也没有两个独立源
关系方向。这里正确回执是
\(\mathrm{FOURIER\_SUPPORT\_NOT\_A\_DEMAND}\)，除非另行给出满足
SIMULTANEOUS_ROLE 的双槽、独立关系和共同实现证书。

更极端地，若 \(S_t=\{0\}\)，则三个非平凡角色的系数都非零，但单个源点已经
完全决定截面；这再次说明非零支撑计数不是源容量计数。

## 7. 规范证书字段与研究边界

实现时至少保存

\[
K,S_t,n,N,\Sigma_t^\circ,\{F_t(\chi)\},
 \Sigma_{\mathrm{comp}},\Sigma_{\mathrm{obs}},
 A,\iota,\{d_\chi\},r_{\mathrm{supp}},r_{\mathrm{sim}},
 \mathrm{simultaneous\_role\_status},\mathsf C_q.
\]

该引理把“支撑足够大”与“容量足够紧”严格分成两步：支撑下界是已证明的
Parseval 事实，容量需求还需要 simultaneous-role、Rado 独立性和 q 槽价格。它
消除了按非零 Fourier 系数数量自动收费的逻辑跳步，但仍不证明每个全相容支撑都
能构造出足够大的 SIMULTANEOUS_ROLE 集；若该门失败，支撑证书本身就是当前状态
的完整输出。若失败发生在固定纤维并已得到 Rado 对偶角色，则先做有限源列逃逸
扩张；达到 SCClosed 后，目标相位非平凡走 annihilator 商，目标相位平凡走
[Type II 全源列闭合的 annihilator 子群—商双向严格递降](type-II-annihilator-two-sided-subgroup-quotient-descent.md)，
再由 SNF/source-switch 门决定是否成为保持标签的严格递降。
