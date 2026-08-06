---
kind: claim
claim_id: type-II-cross-state-tower-weighted-surplus-selector
title: Type II 跨参数纤维稳定子塔的加权 surplus 选择器
statement: 对有限个已经实现且来源合同闭合的参数纤维，分别运行稳定子塔并以 \(\rho_{k,f}=\kappa_{k,f}|T_{k,f}|\) 计费。若所有纤维都遗漏目标，则任意正权重的加权总需求不超过各自稳定子缺口预算之和；因此可验证的严格加权 surplus 强制某个纤维命中。该选择器不池化不同目标群，只合并标量账本，并把标签分派、稳定子商和整数提升障碍保留为明确的失败分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-stabilizer-tower-weighted-defect-conservation
  - type-II-cross-state-fiber-capacity-surplus-certificate
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-q-prefix-source-label-finite-closure
topics:
- type-II
- cross-state
- parameter-fiber
- stabilizer
- tower
- weighted-capacity
- surplus
- q-adic
- Hall
- source-switch
- proof-program
sources:
  - claim: type-II-stabilizer-tower-weighted-defect-conservation
    role: per-fiber-weighted-ledger
  - claim: type-II-cross-state-fiber-capacity-surplus-certificate
    role: cross-fiber-surplus-interface
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: label-and-resource-dispatch
visibility: public
last_checked: '2026-08-05'
---

# Type II 跨参数纤维稳定子塔的加权 surplus 选择器

## 1. 有限纤维族和独立账本

固定核心素数 \(p\)，以及一个有限的已实现参数纤维族
\[
\mathcal F=\{f\}.
\]
每个 \(f\) 有自己的有限阿贝尔目标群 \(H_f\)、目标 \(t_f\)、初始源积集
\(P_{0,f}\ne\varnothing\) 和已通过 source-switch、SNF、CRT、范围以及
\(B'>A\) 门的源块列
\[
P_{k,f}=P_{k-1,f}D_{k,f},
\qquad
T_{k,f}=\operatorname{Stab}_{H_f}(P_{k,f}),
\qquad
1\le k\le m_f.
\tag{1}
\]
对每个纤维定义
\[
\kappa_{k,f}
  =|D_{k,f}T_{k,f}/T_{k,f}|-1,
\qquad
\rho_{k,f}=\kappa_{k,f}|T_{k,f}|.
\tag{2}
\]
允许使用一个已验证的下界
\[
0\le\underline\rho_{k,f}\le\rho_{k,f}
\tag{3}
\]
（例如 q 前缀匹配得到的
\(\min(d_{k,f},\operatorname{ord}_{H_f/T_{k,f}}(u_{k,f}T_{k,f})-1)|T_{k,f}|\)）。

令 \(L_{0,f}\le|P_{0,f}|\) 是初始容量下界，定义最终稳定子预算
\[
\mathcal B_f=|H_f|-|T_{m_f,f}|-L_{0,f},
\qquad
\underline{\mathcal Q}_f=\sum_{k=1}^{m_f}\underline\rho_{k,f}.
\tag{4}
\]
这里 \(\mathcal B_f\) 是该纤维在目标缺失假设下可支付的全部剩余元素预算；
它不是另一个目标群，也不允许把 \(H_f\) 与 \(H_{f'}\) 识别。

## 2. 加权 surplus 定理

取任意正有理权重 \(w_f>0\)，并令
\[
\underline{\mathcal Q}_w
  =\sum_{f\in\mathcal F}w_f\underline{\mathcal Q}_f,
\qquad
\mathcal B_w
  =\sum_{f\in\mathcal F}w_f\mathcal B_f,
\qquad
\operatorname{Surplus}_w
  =\underline{\mathcal Q}_w-\mathcal B_w.
\tag{5}
\]
则有如下二分：

\[
\boxed{
\begin{array}{ll}
\text{若所有 }f\text{ 都满足 }t_f\notin P_{m_f,f},
 &\underline{\mathcal Q}_w\le\mathcal B_w;\\[1mm]
\text{若 }\underline{\mathcal Q}_w>\mathcal B_w,
 &\text{至少有一个 }f\text{ 满足 }t_f\in P_{m_f,f}.
\end{array}}
\tag{6}
\]

第二行给出一个显式的
'TOWER_WEIGHTED_SURPLUS_HIT'：记录违反预算的纤维、其源块顺序、每一步的
\((T_{k,f},\underline\kappa_{k,f},\underline\rho_{k,f})\) 和来源回译数据，即可
回译为 Type II 短证书。

### 证明

若 \(t_f\notin P_{m_f,f}\)，加权价格引理的望远镜界给出
\[
L_{0,f}+\sum_k\rho_{k,f}
\le |H_f|-|T_{m_f,f}|,
\]
故
\[
\underline{\mathcal Q}_f
\le\sum_k\rho_{k,f}
\le\mathcal B_f.
\tag{7}
\]
乘以 \(w_f>0\) 并对 \(f\) 求和，得到第一行。若第二行成立，则 (7) 不可能对所有
\(f\) 成立；某个纤维的目标缺失假设失败，即 \(t_f\in P_{m_f,f}\)。由于每个
\(D_{k,f}\) 已通过整数来源合同，积集中成员按记录的标签和参数直接回译为
Type II 表示。证毕。

正权重不制造新的群论事实：若每个纤维的单独 surplus 都不正，则任何正权重
仍不能得到正总 surplus。它的作用是允许在已知不同纤维证书可信度、来源阶数或
共享 q 资源时，统一比较标量缺口；真正的命中仍由至少一个纤维的预算违约承担。

## 3. q 前缀和 Hall 分派的下界注入

对每个纤维，先将 q 层请求通过
[Type II q 前缀来源标签与候选纤维的有限穷尽闭包](type-II-q-prefix-source-label-finite-closure.md)
分成一个实际的、来源标签不重复的分派
\[
\mathcal R=\bigsqcup_{f\in\mathcal F}\mathcal R_f.
\tag{8}
\]
每个 \(\mathcal R_f\) 还需通过前缀 Hall 条件、shared-q 合并以及 CRT/SNF/范围门。
对同一 q 方向合并后的高度记为 \(d_{q,f}\)，令 \(k(q,f)\) 是这个合并 q 幂块
在稳定子塔中的实际插入步，并以插入稳定子 \(T_{k(q,f),f}\) 计算下界
\[
\underline\kappa_{q,f}
=\min\!\left(
d_{q,f},
\operatorname{ord}_{H_f/T_{k(q,f),f}}
  (u_{q,f}T_{k(q,f),f})-1
\right),
\qquad
\underline\rho_{q,f}
=\underline\kappa_{q,f}|T_{k(q,f),f}|.
\tag{9}
\]
若达到有限阶，插入稳定子上的折叠按稳定子塔处理；不能把之后的最终稳定子价格
与 (9) 重复计费。若使用 q 前缀主张中的最终稳定子压缩，则必须把整个 q 方向
重新声明为一个独立的最终块并验证其最终块回执，然后以该块替换而不是叠加 (9)。
把所有实际插入步的 (9) 加入 \(\underline{\mathcal Q}_f\)，再检验 (6)，即可得到
一个带 q-height 证书的跨纤维选择器。

若同一请求有多个候选纤维，不能把它复制进 (8)。应枚举有限标签/纤维分派，
逐分支运行 (6)，并输出下列之一：

* 'TOWER_WEIGHTED_SURPLUS_HIT'：某分支的加权下界严格超过预算；
* 'TOWER_WEIGHTED_DEFICIT'：该分支的每个纤维都保留非负预算缺口，记录
  \(\mathcal B_f-\underline{\mathcal Q}_f\)；
* 'TOWER_LABEL_ASSIGNMENT_UNCLOSED'：候选标签或候选纤维族没有有限化；
* 'TOWER_INTEGER_LIFT_OBSTRUCTED'：群账本成立，但某个分支未通过 source-switch、
  SNF、范围、\(B'>A\) 或 E1--E5，不能回译。

这保证跨状态加权只发生在“已选分支的标量账本”上，而不是把不同 \(H_f\) 的积集
误合成为一个虚构的 Kneser积集。

## 4. 与逐纤维稳定子下降的接口

若某个分支的 surplus 不正，不能把缺口称为失败；对该纤维保留完整塔记录
\[
\Delta_f=\mathcal B_f-\sum_k\underline\rho_{k,f}\ge0.
\tag{10}
\]
按以下顺序继续处理：

1. \(T_{m_f,f}>1\)：用稳定子商和来源保持门尝试严格较小的整数 relay；
2. \(T_{m_f,f}=1\) 且存在 primary/annihilator 角色：转入 Fourier、格或
   广义 \(2^j\) 数字终端；
3. q/Hall 分派有缺口：调用跨状态 q 进容量切割和 annihilator 对偶；
4. 来源合同未闭合：保存最小 CRT/SNF/标签障碍，不向 (5) 注入价格。

因此这个选择器把“某个纤维必须命中”与“所有纤维各自递降/终端”连接起来，但
不声称仅凭加权和就能替代后续整数提升。

## 5. 边界检查和非池化原则

单纤维目标缺失时 (7) 是逐层缺陷守恒的直接推论。跨纤维时即使
\(H_f\cong H_{f'}\)，也只能分别计算 \(\mathcal B_f\) 和
\(\mathcal B_{f'}\)；不同的来源标签、CRT 纤维和目标识别不允许把
\(P_{m_f,f}\) 与 \(P_{m_{f'},f'}\) 相乘。正权重的求和只是对不等式做线性组合，
不会制造跨纤维成员或新的 source-switch。

若选 \(w_f=a_f/b_f\)，乘以所有分母的最小公倍数即可得到整数 surplus 证书；
所以 (6) 是有限可计算的，而非依赖实数极限。若某个纤维没有任何已验证块，
\(\underline{\mathcal Q}_f=0\)，它只能贡献预算，不能凭空产生需求。

## 6. 研究边界

本主张完成了跨纤维稳定子塔的加权容量映射：它把最终稳定子下的粗 q-height
比较替换为逐步、不重复、以原群元素计量的价格，并给出严格 surplus 时的
Type II 选择器。剩余的全局决定性缺口是：

* 证明有限来源标签族存在一个完整的实际分派 (8)，而不是只得到
  'TOWER_LABEL_ASSIGNMENT_UNCLOSED'；
* 在所有分支 \(\Delta_f\ge0\) 时，把至少一个非零缺口升级为可提升的稳定子
  下降、规范 Fourier/格分离或广义 \(2^j\) 终端；
* 证明这些分支在核心素数 \(p\equiv1\pmod{24}\) 的全部参数范围内闭合。

因此 (6) 是新的全局接口和正 surplus 证书，不把条件性的来源分派误报为猜想的
完整证明。
