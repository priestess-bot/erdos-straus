---
kind: claim
claim_id: type-II-owner-weighted-stabilizer-annihilator-well-founded-selector
title: Type II owner 加权稳定子—annihilator 良基选择器
statement: 对固定目标纤维的 owner 加权谱，按命中、支撑分离、加权稳定子商和 Fourier—q 进 annihilator 顺序分派。未命中且稳定子非平凡时，谱严格下降到较小商；稳定子平凡时，规范 Fourier 角色只有在源关系、相位、owner 和容量门通过后才可产生 annihilator。若其 q 进缺口是 source-dominating-cut，则目标在 annihilator 核内外分别产生严格子群或商 relay，核为平凡时是顶层 primary 终端。所有通过的有限 relay 都严格降低群阶势；任何未通过的门都输出可定位的源列逃逸、算术提升或容量未闭合障碍，不被误记为递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-target-fiber-owner-weighted-fourier-capacity-bridge
  - type-II-cross-state-qcapacity-deficit-annihilator-relay
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-I-fg-fourier-to-type-II-role-demand-bridge
topics:
  - type-II
  - owner-weight
  - stabilizer
  - annihilator
  - well-founded-descent
  - Fourier
  - q-adic-capacity
  - source-switch
  - proof-program
sources:
  - claim: type-II-target-fiber-owner-weighted-fourier-capacity-bridge
    role: weighted-target-spectrum-and-canonical-Fourier
  - claim: type-II-cross-state-qcapacity-deficit-annihilator-relay
    role: Rado-deficit-to-annihilator
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: two-sided-finite-relay
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: fixed-layer-modulus-potential
  - reproduction: reproductions/type_ii_owner_weighted_stabilizer_annihilator_selector.py
    role: weighted-versus-support-stabilizer-and-selector-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 加权稳定子—annihilator 良基选择器

## 1. 输入与选择顺序

固定一个已经通过 source profile 声明、目标纤维条件和固定层合法性检查的状态。把
其稳定子约化后的目标商写为 \(H\)，规范化源集和目标写为

\[
1\in R\subset H,\qquad t\in H\setminus R.
\tag{1}
\]

对严格目标 \(f=(d',A)\) 的共同 q 高度和 owner 数按
[目标纤维 owner 加权谱](type-II-target-fiber-owner-weighted-fourier-capacity-bridge.md)
构造 \(W_f\)。只有目标 residue adapter 通过时，才把 \(G_f\) 识别为当前目标商
\(H\) 的子群；否则输出 'OWNER_SPECTRUM_GROUP_LIFT_OBSTRUCTED'，不进入下面的
稳定子或 annihilator 分支。若当前角色只在一个源关系商 \(H_0\) 中定义，则还要
记录其 source-SNF 注入

\[
\iota:H_0\hookrightarrow H.
\tag{2}
\]

选择器严格按以下顺序运行：

1. \(t\notin G_f\)：输出 'G_SOURCE_SUPPORT_SEPARATION'；
2. \(W_f(t)>0\)：输出带 owner 标签的 'OWNER_WEIGHTED_TARGET_HIT'；
3. \(t\in G_f\) 且 \(W_f(t)=0\)：计算加权稳定子 \(P_f\)；若
   \(P_f\ne1\)，执行加权稳定子商下降；
4. \(P_f=1\) 时选择规范非平凡 Fourier 角色，依次通过 source relation、角色阶、
   算术相位和 owner 对齐门，再进入 q 进容量分派；
5. 只有 q 进切割给出严格缺口且该缺口是 'SOURCE-DOMINATING-CUT' 时，才调用
   annihilator 双向 relay。

这个顺序把“有 Fourier 相关性”与“已经获得有限下降”分开。加权谱的系数是
owner 槽数，不是未经核验的 source-row 重复次数。

## 2. 加权稳定子下降

令

\[
P_f=\{x\in G_f:W_f(xg)=W_f(g)\text{ 对所有 }g\in G_f\}.
\tag{3}
\]

这是子群：单位元显然在其中；若 \(x,y\) 稳定 \(W_f\)，则 \(xy\) 稳定；若
\(x\) 稳定，则由 \(W_f(x^{-1}g)=W_f(g)\) 得 \(x^{-1}\) 也稳定。故 \(W_f\) 唯一
下降为 \(\bar W_f\) 于

\[
\bar G_f=G_f/P_f.
\tag{4}
\]

若 \(W_f(t)=0\)，则

\[
\bar W_f(tP_f)=0.
\tag{5}
\]

若 \(P_f\ne1\)，(4) 的群阶严格变小。商群不可能是平凡群：若
\(P_f=G_f\)，则 \(W_f\) 是正总质量 \(V_f\ge1\) 的常函数，从而
\(W_f(t)>0\)，与未命中矛盾。因此未命中分支满足

\[
1<|\bar G_f|<|G_f|,
\tag{6}
\]

并输出

\[
\boxed{\mathrm{OWNER\_SPECTRUM\_STABILIZER\_DESCENT}}
=(G_f,W_f,t;P_f,\bar G_f,\bar W_f).
\tag{7}
\]

使用有限群势

\[
\Phi(H)=\bigl(|H|,\operatorname{rk}_{\rm SNF}H,
                 \sum_{q,j}\omega_q(j)\bigr)
\tag{8}
\]

的词典序。只要 (7) 通过当前纤维的 source-switch 和 E1--E5 提升门，第一坐标
严格下降；若提升门失败，保留 (7) 作为抽象有限 relay，同时输出
'STABILIZER_RELAY_LIFT_OBSTRUCTED'，不能声称已经得到整数递归边。

注意必须使用加权稳定子。令 \(\operatorname{supp}(W)\) 的无权指示函数为
\(1_{\operatorname{supp}(W)}\)。一般有

\[
\operatorname{Stab}(W)\subsetneq
\operatorname{Stab}(1_{\operatorname{supp}(W)}),
\tag{9}
\]

因为不同 owner multiplicity 会破坏支撑的伪周期。若使用无权稳定子，可能把本来
不能下降的状态错误压到过小的商中。

## 3. 稳定子平凡后的对偶分派

当 \(P_f=1\) 且 \(t\) 未命中时，加权 Fourier 正交关系给出

\[
\sum_{\chi\ne1}
\overline{\chi(t)}\,\widehat W_f(\chi)=-V_f.
\tag{10}
\]

因此按相关实部、角色阶和固定坐标字典序选择规范角色 \(\chi_*\)，有

\[
-\operatorname{Re}\bigl(\overline{\chi_*(t)}\widehat W_f(\chi_*)\bigr)
\ge\frac{V_f}{|G_f|-1}.
\tag{11}
\]

此时分派必须保留以下三种互斥结果：

* 若 \(\chi_*\) 在 source difference subgroup 上平凡而在目标锚点上非平凡，输出
  'G_SUPPORT_SEPARATION'，不收费 q 容量；
* 若 \(\chi_*\) 在 source difference subgroup 上非平凡，但 SNF、角色阶、算术相位
  或 owner 对齐失败，输出相应的 'FOURIER_*_LIFT_OBSTRUCTED'，不把式 (11) 计为
  Type II 证书；
* 若上述门通过，按每个 \((q,j)\) 产生独立 'SOURCE_RANK_DEMAND(q,j)'，再检查
  q 进容量。容量没有严格缺口时，输出 'OWNER_FOURIER_CAPACITY_UNCLOSED'；有缺口
  但源列未被支配时，输出 'SOURCE_COLUMN_ESCAPE'。

这一步把 owner 加权谱产生的对偶质量准确地送入已有的 F/G—Type II typed 接口，
但不越过其算术前提。

## 4. annihilator 的严格分支

假设一个通过源关系、SNF、相位和 owner 门的 q 进切割 \(U\) 满足

\[
\mathsf C_q(U)<|U|
\tag{12}
\]

并且是 'SOURCE-DOMINATING-CUT'。Rado 对偶给出阶 \(\ell\) 的线性角色
\(\lambda\)，湮灭所有真实源列并分离至少一个请求方向；令

\[
\chi_\lambda:H\to\mu_\ell,
\qquad K=\ker(\chi_\lambda).
\tag{13}
\]

source-dominating 条件确保 \(R\subseteq K\)。于是：

1. 若 \(\chi_\lambda(t)\ne1\) 且 \(K\ne1\)，则 \(H/K\) 中目标仍缺失，输出
   'ANNIHILATOR_QUOTIENT_LOWER_RELAY'；
2. 若 \(\chi_\lambda(t)\ne1\) 且 \(K=1\)，输出 'TOP_PRIMARY_ANNIHILATOR'；这是
   有限势的终端，不伪造更小商；
3. 若 \(\chi_\lambda(t)=1\)，则 \(t\in K\setminus R\)，输出
   'ANNIHILATOR_SUBGROUP_LOWER_RELAY'。

Type II 的 \(t=-1\) 还有一个额外约束：

\[
\operatorname{ord}(tK)\mid2.
\tag{14}
\]

所以当 \(H/K\) 为奇素数阶时，商外分支不可能发生；奇 primary annihilator 只能
进入子群 relay 或源关系终端。这个阶二塌缩把广义 primary 分支和 Type II 的
\(2^j\) 终端明确接起来。

每个非终端 relay 的新有限群都是 \(H\) 的真子群或真商，故

\[
\Phi(H')<_{\rm lex}\Phi(H).
\tag{15}
\]

只有当整数 source-switch、目标纤维回译、范围 \(B'>A\) 以及 E1--E5 全部通过时，
(15) 才记为“严格可提升递降”；否则保留有限群 relay 和精确的
'*_LIFT_OBSTRUCTED' 回执。

## 5. 证明

式 (3) 的子群性质和 (4)--(6) 已在上节直接证明；(5) 使用的是稳定子定义，
因同一 \(P_f\)-陪集上的权重相等，陪集整体未命中。式 (10) 是有限阿贝尔群的
角色正交关系在 \(W_f(t)=0\) 时的展开；从 \(|G_f|-1\) 个非平凡角色中取最小
相关实部即得 (11)。

通过 source-SNF 和相位门的角色按照其非平凡的 primary 分量产生独立源秩需求；
这是 F/G—Type II role-demand 桥的结论。若 (12) 成立，分层 Hall/Rado 对偶给出
\(\lambda\) 湮灭所有缺口邻域源列并分离需求方向。'SOURCE-DOMINATING-CUT' 把每个
真实源生成元接到这些被湮灭的邻接列，因而 \(R\subseteq K\)。

若目标在 \(K\) 外，投影 \(H\to H/K\) 把源集压到单位元而保留非单位目标；若
目标在 \(K\) 内，缺失直接限制到 \(K\)。\(K\) 是非平凡角色的核，故两个非终端
分支都严格降低群阶；\(K=1\) 正是没有更小 annihilator relay 的顶层情形。
式 (14) 来自 Type II 目标的阶二性质。有限势 (15) 随之成立。所有整数提升条件
都是额外的可检验门，门失败只说明抽象 relay 尚未成为原参数递归边。证毕。

## 6. 构造性控制与研究边界

* 在 \(p=409,D=8,f=(4,2)\) 的实际 owner 谱中，\(G_f=U(16)\)、
  \(W_f(-1)=0\)、\(P_f=\{1,7\}\)，故先得到阶 \(8\to4\) 的
  'OWNER_SPECTRUM_STABILIZER_DESCENT'，再在商中选择 Fourier 角色；这不是把角色
  直接称为容量矛盾。
* 一个 owner 失衡的有限 \(U(16)\) 谱取
  \(\omega_3(1)=1,\omega_7(1)=2\)，得到
  \(W(1),W(3),W(5),W(7)=(1,1,2,2)\)。其无权支撑仍被 \(7\) 稳定，但加权稳定子
  变为平凡群，证明 (9) 是必要的，而不是记号区别。
* 在 \(p=5113,D=6,f=(1,1)\) 中，权重在目标元素 \(3=-1\bmod4\) 上为正，先输出
  'OWNER_WEIGHTED_TARGET_HIT'，并由 \(h=7\) 给出 \((K',B',C')=(2,1461,1)\)。

该选择器仍未证明所有实际核心素数都满足 source-dominating cut、owner 对齐和
整数 E1--E5 提升。当前决定性缺口已收紧为：对稳定子平凡且 Fourier 未命中的实际
纤维，要么证明一个可提升的 q 进缺口，要么构造 Type I/广义 \(2^j\) 终端；不能
再用无权支撑或未提升 Fourier 相关性替代这一步。
