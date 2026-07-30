---
kind: claim
claim_id: type-I-ordered-r-migration-min-cost-duality
title: 有序 R 位置的迁移最小费用对偶与局部容量升级准则
statement: 对有限有序 R 节点上的 Pareto 需求和 q 进资源容量，任意全局分配都等价于一条线网络流，其费用精确等于各切口前缀不平衡的加权绝对值之和；凸化最小费用的对偶是满足相邻 Lipschitz 约束的非恒定价格势。若某局部 R 窗口有共同价格缺口 \(\delta>0\)，窗口外的折扣容量为 \(E\)，而每条实际算术迁移的收费支配指定切口费用且总收费预算至多 \(B\)，则 \(E+B<\delta\) 足以排除全局修复。对 \(p=62704849\) 的现有局部证书有 \(\delta\ge1\)；因此证明 \(E+B<1\)，或相应整数切口费用超过 \(B\)，即可把该条件性局部超载升级为完整容量矛盾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-pareto-overflow-capacity-separation-theorem
  - type-I-f-overflow-lower-modulus-pareto-capacity-flow-boundary
  - type-I-cross-state-q-adic-capacity-bound
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
topics:
- type-I
- F-state
- ordered-moduli
- min-cost-flow
- prefix-imbalance
- convex-duality
- integer-flow
- migration-cost
- q-adic
- capacity
- locality
- proof-program
sources:
- claim: type-I-f-overflow-lower-modulus-pareto-capacity-flow-boundary
  role: local-price-certificate-and-global-flow
- claim: type-I-pareto-overflow-capacity-separation-theorem
  role: unlocated-convex-separation-baseline
- claim: type-I-cross-state-q-adic-capacity-bound
  role: possible-migration-budget
- claim: type-I-linear-hybrid-label-modulus-q-adic-capacity
  role: arithmetic-resource-capacity
visibility: public
last_checked: '2026-07-30'
---

# 有序 \(R\) 位置的迁移最小费用对偶与局部容量升级准则

## 1. 有序运输模型

取有限有序位置

\[
R_1<R_2<\cdots<R_n
\]

及有限资源方向集 \(\mathcal Q\)。若需要保留块、标签差和模数差三种颜色，可把
\(q\) 替换为复合方向 \((q,c)\)；下述证明不变。

状态 \(s\) 位于节点 \(i(s)\)，并有非空有限需求集

\[
D_s\subseteq\mathbb R_{\ge0}^{\mathcal Q}.
\]

节点 \(i\) 在方向 \(q\) 上有容量 \(c_{i,q}\ge0\)。相邻节点
\((i,i+1)\) 的一个 \(q\)-层若穿过该切口，赋予非负迁移费
\(\tau_{i,q}\)。令

\[
d_{i,q}
=
\sum_{s:i(s)=i}e_{s,q},
\qquad
e_s\in\operatorname{conv}(D_s).
\]

变量 \(u_{i,q}\in[0,c_{i,q}]\) 是实际使用的节点容量；
\(f_{i,q}\in\mathbb R\) 是切口 \((i,i+1)\) 上向右为正的净流，并约定
\(f_{0,q}=f_{n,q}=0\)。流守恒为

\[
f_{i,q}-f_{i-1,q}=d_{i,q}-u_{i,q}.
\tag{1}
\]

凸最小迁移费用定义为

\[
\mathcal T_{\mathbb R}
=
\min
\sum_{q\in\mathcal Q}\sum_{i=1}^{n-1}
\tau_{i,q}|f_{i,q}|,
\tag{2}
\]

其中极小化遍历上述全部变量。当 \(D_s\subseteq\mathbb Z_{\ge0}^{\mathcal Q}\)
且容量为整数时，若进一步要求 \(e_s\in D_s\) 且 \(u,f\) 为整数，得到整数值
\(\mathcal T_{\mathbb Z}\)。显然

\[
\mathcal T_{\mathbb Z}\ge\mathcal T_{\mathbb R}.
\tag{3}
\]

## 2. 前缀不平衡恒等式

对固定的需求选择 \(e_s\) 和已用容量 \(u\)，式 (1) 逐项求和给出

\[
\boxed{
f_{k,q}
=
\sum_{i\le k}(d_{i,q}-u_{i,q}).
}
\tag{4}
\]

因此

\[
\boxed{
\mathcal T
=
\min_{\substack{0\le u\le c\\
\sum_i u_{i,q}=\sum_i d_{i,q}}}
\sum_{q\in\mathcal Q}\sum_{k=1}^{n-1}
\tau_{k,q}
\left|
\sum_{i\le k}(d_{i,q}-u_{i,q})
\right|.
}
\tag{5}
\]

式 (5) 是线上的精确 earth-mover 表达式，而不是总需求和总容量的一次凸分离。
每个前缀缺多少资源，就必须有相同净流穿过其右侧切口；相反，由 (4) 定义的流自动
满足全部节点守恒，所以没有遗漏约束。

若 \(D_s\) 都是单点且需求、容量为整数，(1) 的约束矩阵是有向线图的关联矩阵加单位
列，因而全幺模。此时存在整数最优解，并有

\[
\mathcal T_{\mathbb Z}=\mathcal T_{\mathbb R}.
\tag{6}
\]

一般多列选择可能有整数间隙，但任意凸对偶下界仍是
\(\mathcal T_{\mathbb Z}\) 的有效下界。

## 3. Lipschitz 价格势对偶

对每个节点和方向取实势 \(\phi_{i,q}\)，满足

\[
|\phi_{i+1,q}-\phi_{i,q}|
\le\tau_{i,q}.
\tag{7}
\]

则凸最小费用的精确对偶为

\[
\boxed{
\mathcal T_{\mathbb R}
=
\max_{\phi\ {\rm satisfies}\ (7)}
\left[
\sum_s
\min_{e\in D_s}
\sum_q\phi_{i(s),q}e_q
-
\sum_{i,q}c_{i,q}(\phi_{i,q})_+
\right].
}
\tag{8}
\]

### 证明

把 \(f_{i,q}=f^+_{i,q}-f^-_{i,q}\)，其中
\(f^\pm_{i,q}\ge0\)，并对守恒式

\[
d_{i,q}-u_{i,q}-f_{i,q}+f_{i-1,q}=0
\]

引入乘子 \(\phi_{i,q}\)。对一条边的 \(f^+\) 和 \(f^-\) 取下确界有限，当且仅当

\[
\phi_{i,q}-\phi_{i+1,q}\le\tau_{i,q},
\qquad
\phi_{i+1,q}-\phi_{i,q}\le\tau_{i,q},
\]

即 (7)。对 \(0\le u_{i,q}\le c_{i,q}\) 取下确界得到

\[
\min_{0\le u\le c}(-\phi u)
=
-c(\phi)_+.
\]

对 \(e_s\in\operatorname{conv}(D_s)\) 取下确界得到

\[
\min_{e\in D_s}\phi_{i(s)}\cdot e.
\]

剩余表达式正是 (8)。原问题是有限线性规划，故可行且有限时由强对偶得到等号；
不可行情形按扩展实数的线性规划替代定理解释。证毕。

精确等号 (8) 使用了有限列线性规划；但后文所需的下界不需要这一有限性。对任意
非空需求集 \(D_s\subseteq\mathbb R_{\ge0}^{\mathcal Q}\)，即使它是无限离散集，
逐项取下确界仍给出弱对偶

\[
\mathcal T
\ge
\sum_s\inf_{e\in D_s}\phi_{i(s)}\cdot e
-\sum_{i,q}c_{i,q}(\phi_{i,q})_+.
\tag{8a}
\]

因此只要各需求集在指定势下的下确界已有独立证明，窗口切口界和第 5 节的帐篷势
下界都可直接用于完整目标纤维，无须先把纤维截断成有限列。

若 \(\phi_{i,q}\) 与 \(i\) 无关，(8) 退化为普通共同价格分离。这里新增的信息正是
非恒定势的 Lipschitz 约束：价格从局部窗口向外衰减的速度不能超过已经证明的切口
迁移费。

## 4. 局部窗口的切口逃逸下界

固定连续窗口

\[
I=[a,b]\cap\mathbb Z
\]

和共同非负价格 \(w=(w_q)\)。定义窗口需求价格下界、容量价格及缺口

\[
L_I(w)
=
\sum_{s:i(s)\in I}\inf_{e\in D_s}w\cdot e,
\]

\[
C_I(w)
=
\sum_{i\in I}\sum_qw_qc_{i,q},
\qquad
\delta_I(w)=L_I(w)-C_I(w).
\tag{9}
\]

假设 \(\delta_I(w)>0\)。对任意全局流，把 (1) 在 \(I\) 上求和并乘以 \(w_q\)，得到

\[
\sum_qw_q(f_{b,q}-f_{a-1,q})
=
\sum_qw_q(d_{I,q}-u_{I,q})
\ge\delta_I(w).
\]

于是必有

\[
\boxed{
\sum_qw_q
\left[
(f_{b,q})_+
+(-f_{a-1,q})_+
\right]
\ge\delta_I(w).
}
\tag{10}
\]

这说明局部价格缺口不能由窗口外的“免费总容量”消失；至少
\(\delta_I(w)\) 的加权需求必须跨过左右边界之一。

该窗口推论只使用每个状态的价格下界
\(\inf_{e\in D_s}w\cdot e\)。因此即使 \(D_s\) 是完整目标纤维像这样的无限离散集，
只要相应下确界已有严格证明，式 (9)--(13) 仍然成立，不需要把整个纤维预先枚举为
有限列。

假设 \(I\) 是真窗口，并令
\(\partial I\subseteq\{-,+\}\) 为实际存在的边界方向，即
\(-\in\partial I\) 当且仅当 \(a>1\)，而
\(+\in\partial I\) 当且仅当 \(b<n\)。定义

\[
\rho_I
=
\min_{\substack{q:w_q>0\\\sigma\in\partial I}}
\frac{\tau^\sigma_q}{w_q},
\qquad
\tau^-_q=\tau_{a-1,q},
\quad
\tau^+_q=\tau_{b,q}.
\]

则凸流满足

\[
\boxed{
\mathcal T_{\mathbb R}
\ge\rho_I\,\delta_I(w).
}
\tag{11}
\]

整数流还有不经过分数松弛的精确切口下界

\[
\kappa_{\mathbb Z}(\delta)
=
\min
\left\{
\sum_q(\tau^-_qm^-_q+\tau^+_qm^+_q):
\begin{array}{l}
m^\pm_q\in\mathbb Z_{\ge0},\\
\sum_qw_q(m^-_q+m^+_q)\ge\delta
\end{array}
\right\},
\tag{12}
\]

其中不存在的边界方向不引入变量 \(m^\sigma_q\)。因而

\[
\mathcal T_{\mathbb Z}
\ge\kappa_{\mathbb Z}(\delta_I(w)).
\tag{13}
\]

### 硬切口容量版本

若算术侧能直接证明每个切口至多允许 \(M_{k,q}\) 个 \(q\)-层通过，即

\[
|f_{k,q}|\le M_{k,q},
\]

则由 (10) 立即得到必要条件

\[
\boxed{
\delta_I(w)
\le
\sum_qw_q\bigl(M_{a-1,q}+M_{b,q}\bigr),
}
\]

其中不存在的边界项删去。特别地，对前缀 \(I=[1,k]\)，式 (4) 还给出逐方向约束

\[
\boxed{
\sum_{i\le k}(d_{i,q}-c_{i,q})
\le M_{k,q}.
}
\]

因此若任一窗口的局部价格缺口严格超过两侧可迁移层容量，或任一前缀不平衡超过
相应切口容量，则不需要引入费用预算，已经可由 cut bound 排除全局修复。

## 5. 外部容量折扣与帐篷势

对节点 \(i\) 到窗口 \(I\) 的 \(q\)-方向路径距离记为

\[
\operatorname{dist}_q(i,I)
=
\min_{j\in I}
\sum_{\text{edges }k\text{ between }i\text{ and }j}\tau_{k,q}.
\]

定义帐篷势

\[
\phi_{i,q}
=
\left(w_q-\operatorname{dist}_q(i,I)\right)_+.
\tag{14}
\]

距离函数沿边 \(k\) 的变化不超过 \(\tau_{k,q}\)，取正部后仍然如此，故 (14)
满足 (7)。它在窗口内等于 \(w_q\)。窗口外各状态的需求项非负，因此代入 (8) 并
舍去这些非负项，得到

\[
\boxed{
\mathcal T_{\mathbb R}
\ge
\delta_I(w)-E_I(w,\tau),
}
\tag{15}
\]

其中

\[
E_I(w,\tau)
=
\sum_{i\notin I}\sum_q
c_{i,q}
\left(w_q-\operatorname{dist}_q(i,I)\right)_+.
\tag{16}
\]

\(E_I\) 是仍然“离窗口太近”的折扣外部容量。若每个具有正容量的外部
\((i,q)\) 都满足

\[
\operatorname{dist}_q(i,I)\ge w_q,
\tag{17}
\]

则 \(E_I=0\)，局部价格缺口完整保留下来：

\[
\mathcal T_{\mathbb R}\ge\delta_I(w).
\]

式 (15) 比“禁止全部外部资源”更精确：远处容量自动被迁移费屏蔽，近处容量只按
\(w_q-\operatorname{dist}\) 的剩余折扣进入账本。

## 6. 算术迁移升级准则

上述流定理本身没有声称盒外层真的支付 \(\tau\)。要把它升级为算术矛盾，需要在
“尚无 Type I/II 短证书且尚无严格可提升递降”的分支中，构造一个非负算术收费
\(\mathscr A\)，并证明：

1. **位置保持**：每个目标纤维需求层要么在某个明确的 \(R_i\) 资源槽支付，要么已经
   产生短证书或递降；
2. **切口收费下界**：若一个 \(q\)-层从 \(R_i\) 迁移到 \(R_j\)，其算术收费至少为
   \[
   \sum_{\text{edges }k\text{ between }i\text{ and }j}\tau_{k,q};
   \]
   多个流量单位的收费必须可加，或有显式有界重复度；
3. **收费预算上界**：所有这些收费可注入一族已受控的块、标签差或模数差
   \(q\)-进层，并满足
   \[
   \mathscr A\le B.
   \tag{18}
   \]

例如，若可用算术层的总质量为 \(H\)，且每个层在收费映射中的原像重复度至多为
\(\mu\)，便可取

\[
B=\mu H.
\]

这里的重复度必须对全部状态、方向和切口统一成立；逐状态分别找到一个层不能推出
这个总预算。

对任一实际整数分配，把每个迁移沿唯一线性路径展开。相反方向的路径在同一切口
抵消只会降低绝对净流费用，所以“实际逐层路径费用”不小于该分配诱导的
\(\sum_{k,q}\tau_{k,q}|f_{k,q}|\)，后者又不小于整数最优值。因此前两项给出

\[
\mathscr A\ge\mathcal T_{\mathbb Z}
\ge\mathcal T_{\mathbb R}.
\]

若需求集是无限纤维，则不必声称整数最优值达到；对每个假定存在的实际分配直接使用
上述路径比较和弱对偶 (8a)，得到同样的反证链。

所以以下任一可验证不等式都足以排除该未决分支：

\[
\boxed{
B<\rho_I\delta_I(w),
}
\tag{19}
\]

\[
\boxed{
B<\kappa_{\mathbb Z}(\delta_I(w)),
}
\tag{20}
\]

或更精细地

\[
\boxed{
E_I(w,\tau)+B<\delta_I(w).
}
\tag{21}
\]

这就是把条件性局部超载升级为无条件选择器分支所需的精确桥。这里的“迁移下界”
不能只是端点差值含有某个 \(q\)-幂；还必须证明不同流量单位或不同切口的收费可加，
否则同一个差值高度可能被重复使用，(18)--(21) 便不能合法相接。

## 7. \(p=62704849\) 的接口

现有局部完整纤维证书取

\[
\mathcal Q=(53,349,1650083),
\qquad
w=(5,6,5),
\]

\[
\min_{z\in F_s}w\cdot e_s(z)\ge65,
\qquad
C_I(w)=64,
\]

其中局部因子支撑窗口是

\[
I=\{R=1947\}.
\]

因此

\[
\boxed{\delta_I(w)\ge1.}
\tag{22}
\]

对任何声称用完整线性源谱修复该状态的全局流，式 (10) 强制正加权流量越过
\(R=1947\) 左右某个切口；在实际的整数赋值模型中，这等价于至少一个完整
\(q\)-层越界。由此得到三个可直接检验的闭合目标：

1. 若每个允许的外部资源路径都满足
   \[
   \operatorname{dist}_{53}\ge5,\qquad
   \operatorname{dist}_{349}\ge6,\qquad
   \operatorname{dist}_{1650083}\ge5,
   \]
   则 \(E_I=0\) 且 \(\mathcal T_{\mathbb R}\ge1\)；
2. 在整数模型中，因为 \(\delta_I>0\) 已强制至少一个完整层逃逸，
   \[
   \kappa_{\mathbb Z}(\delta_I)
   \ge
   \min_{q,\sigma}\tau^\sigma_q;
   \]
3. 若无递降分支的算术迁移预算为 \(B\)，只需验证
   \[
   E_I(w,\tau)+B<1
   \]
   或相应的整数切口界大于 \(B\)，即可与 (22) 矛盾。

因此下一步不应继续增加全局容量种类。应围绕 \(R=1947\) 的相邻有序源模数，尝试
证明一个可加的跨切口收费：例如把每个外移 \(q\)-层注入不同的
\(v_q((R-R')/4)\)、标签差层或载体块层；若注入失败，则把该失败直接转成合法且解
可提升的较小状态。

## 8. 逻辑边界

本卡建立的是有限网络流定理和严格的充分条件，尚未建立上述三项算术输入。尤其：

- 有序数值距离 \(|R_i-R_j|\) 本身不是 \(q\)-进迁移费；
- 一个端点差值跨过多个数值切口，不会自动产生多个独立收费单位；
- 完整源谱中的同一个标签差或模数差高度不能未经注入证明被多条流重复使用；
- 若跨切口动作改变源状态，还必须证明所得状态合法且其解可提升。

只有在切口收费下界、可加性和预算上界都被证明后，式 (19)--(21) 才是无条件算术
矛盾；在此之前，它们是下一阶段应验证的精确接口，而不是已经完成的猜想证明。
