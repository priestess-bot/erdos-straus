---
kind: claim
claim_id: type-II-stabilizer-tower-weighted-defect-conservation
title: Type II 稳定子塔的加权价格与逐层缺陷守恒
statement: 对同一已实现参数纤维中的有限源块序列，按当前积集的稳定子定义块价格 \(\kappa_k=|D_kT_k/T_k|-1\)，则 Kneser 增长、目标缺失和稳定子升链给出精确的缺陷守恒恒等式与望远镜容量界。该界在 q 前缀块上化为 \(\kappa_k=\min(e_k,\operatorname{ord}_{H/T_k}(u_kT_k)-1)\)，并严格区分非吸收价格、稳定子增长和已吸收的零价格块；它是跨状态容量合并的有限账本接口，但不替代 source-switch、SNF、标签、范围和整数回译门。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-stabilizer-tower-price-recursion
  - type-II-full-match-stabilizer-relay-certificate
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-final-stabilizer-q-fold-collapse
topics:
- type-II
- stabilizer
- tower
- Kneser
- weighted-capacity
- defect-conservation
- q-prefix
- quotient
- source-switch
- proof-program
sources:
  - claim: type-II-stabilizer-tower-price-recursion
    role: prior-unweighted-ledger
  - claim: type-II-full-match-stabilizer-relay-certificate
    role: Kneser-growth-step
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: q-prefix-specialization
visibility: public
last_checked: '2026-08-05'
---

# Type II 稳定子塔的加权价格与逐层缺陷守恒

## 1. 状态和精确块价格

固定一个已经通过 'FIBER_REALIZED'、source-switch、SNF、shared-q、标签和范围门的
参数纤维。令 \(H\) 为有限阿贝尔群，\(A_0\ne\varnothing\) 为初始源积集，目标为
\(t\in H\)。给定有限源块
\[
D_k\subseteq H,\qquad 1\in D_k,\qquad
P_k=P_{k-1}D_k,\qquad P_0=A_0,
\tag{1}
\]
并记
\[
T_k=\operatorname{Stab}_H(P_k)
 =\{h\in H:hP_k=P_k\}.
\tag{2}
\]
由于 \(T_{k-1}P_{k-1}=P_{k-1}\) 且
\(P_k=P_{k-1}D_k\)，有稳定子升链
\[
T_0\le T_1\le\cdots\le T_m.
\tag{3}
\]

在第 \(k\) 步用当前稳定子商
\(\pi_k:H\to H/T_k\) 定义块的精确商价格
\[
\boxed{
\kappa_k
  =|\pi_k(D_k)|-1
  =|D_kT_k/T_k|-1
  =\frac{|D_kT_k|}{|T_k|}-1
  \in\mathbb Z_{\ge0}.
}
\tag{4}
\]
真正记入原群容量的加权价格是
\[
\rho_k=\kappa_k|T_k|.
\tag{5}
\]
因此 \(\kappa_k\) 只数当前商中新增的陪集数，\(\rho_k\) 才数原群中的新增元素
下界。它不把同一稳定子陪集中的多个原始 q 层或多个标签重复收费。

令 \(L_0\le |P_0|\) 为已有的精确容量下界，并递归定义
\[
L_k=L_{k-1}+\rho_k,\qquad
\delta_k=|H|-|T_k|-L_k.
\tag{6}
\]
这里 \(L_k\) 是账本下界，不声称等于 \(|P_k|\)；所有块必须先通过其整数来源
回译门，才允许进入 (6)。

## 2. 一步 Kneser 增长

令 \(P=P_{k-1}\)、\(D=D_k\)、\(T=T_k\)。Kneser 不等式给出
\[
\begin{aligned}
|P_k|
 &=|PD|\\
 &\ge |PT|+|DT|-|T|\\
 &\ge |P|+\bigl(|DT/T|-1\bigr)|T|\\
 &=|P_{k-1}|+\kappa_k|T_k|.
\end{aligned}
\tag{7}
\]
其中第二个不等号只用到 \(P\subseteq PT\)。于是归纳得到
\[
\boxed{L_k\le |P_k|\quad(0\le k\le m).}
\tag{8}
\]
与旧的“每个非吸收块收费 \(|T_k|\)”规则相比，(4) 允许一个块在当前商中
只贡献部分独立方向，也允许一个完整 q 前缀在达到有限阶后只贡献实际的商阶。

## 3. 目标缺失时的缺陷守恒

假设在第 \(k\) 步之后目标仍缺失，即 \(t\notin P_k\)。因为 \(T_k\) 稳定
\(P_k\)，有 \(P_kT_k=P_k\)，故目标陪集 \(tT_k\) 与 \(P_k\) 不交：
\[
tT_k\cap P_k=\varnothing.
\tag{9}
\]
因此
\[
|P_k|\le |H|-|T_k|,
\qquad
\delta_k\ge0.
\tag{10}
\]
由 (6) 可得逐层精确恒等式
\[
\boxed{
\delta_k-\delta_{k-1}
 =|T_{k-1}|-|T_k|-\kappa_k|T_k|
 =-\bigl((|T_k|-|T_{k-1}|)+\kappa_k|T_k|\bigr).
}
\tag{11}
\]
望远镜相加得到
\[
\boxed{
\delta_m
 =\delta_0-\sum_{k=1}^m
 \bigl((|T_k|-|T_{k-1}|)+\kappa_k|T_k|\bigr).
}
\tag{12}
\]
结合 \(\delta_m\ge0\)，任何全程缺失序列都满足精确容量界
\[
\boxed{
L_0+\sum_{k=1}^m\kappa_k|T_k|
 \le |H|-|T_m|.
}
\tag{13}
\]
若某个前缀在 (13) 的左端首次严格超过右端，则此前提“目标仍缺失”不可能成立；
由 (8)--(10) 得到显式 \(t\in P_k\)，再经已登记的来源标签回译为 Type II
表示。这个结论只依赖有限群积集和已验证的来源块，不把抽象容量自动当成
整数表示。

## 4. 零价格、稳定子增长和不重复收费

价格为零时有 \(D_kT_k=T_k\)，也就是 \(D_k\subseteq T_k\)。若同时
\(T_k=T_{k-1}\)，则
\[
P_k=P_{k-1}D_k=P_{k-1},
\tag{14}
\]
因为 \(D_k\subseteq T_{k-1}\)。所以这类块是严格冗余的，可以从剩余块列删除；
它不会在商层或最终稳定子层再次收费。

若 \(\kappa_k=0\) 但 \(T_k>T_{k-1}\)，块不产生新的商陪集，却使缺陷下降
\[
\delta_k-\delta_{k-1}=-(|T_k|-|T_{k-1}|)<0.
\tag{15}
\]
若 \(\kappa_k>0\)，则至少额外下降 \(\kappa_k|T_k|\)。因此每一步只有两种
真正的缺陷消耗：稳定子升链的陪集吸收，或当前商中可区分方向的加权价格；
已吸收的方向不会被历史价格重复计算。

这给出旧稳定子塔势函数的更精确第三坐标。沿目标缺失路径，任何满足
\[
|T_k|>|T_{k-1}|\quad\text{或}\quad \kappa_k>0
\tag{16}
\]
的步骤都严格降低 \(\delta\)；而 \(\kappa_k=0\)、稳定子不变的块按 (14)
删除并降低剩余块数。配合稳定子商的 \(|H/T|\) 严格下降，递归仍然是良基的。

## 5. q 前缀的精确特例

设
\[
D_k=\{1,u,u^2,\ldots,u^e\},
\qquad
o=\operatorname{ord}_{H/T_k}(uT_k).
\tag{17}
\]
在 \(H/T_k\) 中，\(\pi_k(D_k)\) 是长度 \(e+1\) 的循环前缀，因此
\[
\boxed{
\kappa_k=\min(e,o-1),
\qquad
\rho_k=\min(e,o-1)|T_k|.
}
\tag{18}
\]

还有一个与最终稳定子相关的边界约束。若 \(e+1\ge o\)，则 \(uT_k=1\)；
否则 \(u^o\in T_k\) 且前缀含有一整圈，乘法 \(x\mapsto xu\) 将
\(P_k=P_{k-1}D_k\) 映到自身，迫使 \(u\in T_k\)，矛盾于 \(o>1\)。
所以对当前步的最终稳定子，(18) 等价于以下互斥二分：
\[
\begin{array}{c|c|c}
\text{商方向} & \text{有限阶条件} & \text{价格}\\ \hline
uT_k\ne1 & e+1<o & \kappa_k=e,\ \rho_k=e|T_k|,\\
uT_k=1 & e+1\ge o\ (\text{自动}) & \kappa_k=0,\ \rho_k=0.
\end{array}
\tag{19}
\]
因此插入时记录的 'Q_PREFIX_ORDER_FOLD' 不能与最终稳定子下的 \(\rho_k\)
相加；折叠部分已由 (15) 的稳定子增长或后继商处理。

## 6. 适用边界和负证书

引理只合并已经处于同一 \(H\)、同一目标纤维和同一来源标签合同中的块。
跨候选参数纤维、跨不同 CRT 选择或跨不同 source map 的 \(\kappa_k\) 不得直接
求和。若某个声称的块没有通过 source-switch/SNF、标签、范围、\(B'>A\) 或
shared-q 门，应输出相应的 'HALL_SURPLUS_UNPRICED'、算术空集或源列逃逸回执，
而不是把它放入 \(L_k\)。

所以 (13) 的失败分支是有限且可审计的：

* 左端严格超过右端：'WEIGHTED_PRICE_HIT'，得到 Type II；
* 左端不超过右端且 \(T_m>1\)：进入保持标签的稳定子商或其整数提升障碍；
* \(T_m=1\) 且仍缺失：进入已有的 primary/Fourier/广义 \(2^j\) 终端；
* 块不在共同纤维或来源合同未闭合：保存逐块的算术/标签缺口，禁止跨状态伪合并。

该引理把“容量不足”精确化为一个可递归更新的缺陷，而不是新的独立表示定理。
它的全局用途是为跨状态选择器提供统一的加权接口；尚未解决的核心问题仍是：
如何证明有限来源标签族中至少有一组块同时落入同一真实纤维并使 (13) 严格，
或如何把所有未严格的分支提升到 Type I 相位、广义 \(2^j\) 终端或严格整数递降。
