---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-omega-carrier-boundary
title: 低模数 Omega 的双向分母表示与直接载体收费边界
statement: 对 t=R/m 的低模数目标纤维，任一关系向量 z 的盒外向量恰等于两个相反方向形式 Type I 首分母约分缺陷的逐素数赋值之和；因而任意正权 Omega_w 都等于这两个分母缺陷乘积的最小加权素因子赋值。对已有 36 个 Omega_1<=9 的精确 F-box miss，完整枚举 204 个最优向量和 93 种最优溢出模式后，17 个状态无法把任何最优模式逐坐标注入当前块高度；即使加入完整线性源谱中各坐标的最佳标签差与模数差高度，仍有 8 个状态不可注入，加入原平衡约分端点高度后仍是同 8 个。故 Omega 可规范解释为缩放实例 p*m 的双向分母缺陷，但不能无条件地逐层收费到现有局部三通道高度。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-f-overflow-rational-gap-denominator
  - type-I-linear-multi-active-fourier-carrier-vector
  - type-I-f-overflow-lower-modulus-min-overflow-shared-gap
  - type-I-f-overflow-repair-transition-potential-boundary
topics:
  - type-I
  - F-state
  - lower-modulus
  - overflow
  - rational-denominator
  - q-adic
  - carrier
  - capacity
  - finite-audit
  - proof-program
sources:
  - claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
    role: weighted-Omega-definition
  - claim: type-I-f-overflow-rational-gap-denominator
    role: oriented-rational-denominator-interface
  - claim: type-I-linear-multi-active-fourier-carrier-vector
    role: linear-block-and-difference-capacity-interface
  - claim: type-I-f-overflow-lower-modulus-min-overflow-shared-gap
    role: exact-minimum-shell-Type-II-cross-classification
  - claim: type-I-f-overflow-repair-transition-potential-boundary
    role: exact-unit-cost-completion-beyond-cap-nine
visibility: public
last_checked: '2026-07-30'
---

# 低模数 Omega 的双向分母表示与直接载体收费边界

## 双向分母表示定理

设

\[
4K=pR+1,\qquad R=mt,
\qquad K=\prod_iq_i^{\nu_i},
\]

且

\[
z=(z_i)\in F_t,
\qquad \prod_iq_i^{z_i}\equiv-1\pmod t.
\]

写

\[
A(z)=\prod_iq_i^{(z_i)_+},
\qquad
B(z)=\prod_iq_i^{(-z_i)_+}.
\]

则 \((A,B)=1\)、\(t\mid A+B\)。因为

\[
4K=(pm)t+1,
\]

低模数关系自然对应的源分子是

\[
P=\frac{4K-1}{t}=pm,
\tag{1}
\]

而不是原素数 \(p\)。对方向 \(z\) 和反方向 \(-z\)，分别定义形式 Type I
首分母的约分缺陷

\[
X_-(z)=\frac{B(z)}{(B(z),K)},
\qquad
X_+(z)=\frac{A(z)}{(A(z),K)}.
\tag{2}
\]

逐素数有

\[
v_{q_i}(X_-(z))=(-z_i-\nu_i)_+,
\qquad
v_{q_i}(X_+(z))=(z_i-\nu_i)_+.
\tag{3}
\]

因此

\[
\boxed{
X_-(z)X_+(z)
=\prod_iq_i^{(|z_i|-\nu_i)_+}
}
\tag{4}
\]

且对任意正权 \(w=(w_i)\)，若记

\[
V_w(n)=\sum_iw_i v_{q_i}(n),
\]

则选择不变价格具有精确算术表示

\[
\boxed{
\Omega_w(t)
=\min_{z\in F_t}V_w\!\left(X_-(z)X_+(z)\right).
}
\tag{5}
\]

证明只需对 (2) 逐素数约分。对每个坐标，\(z_i>\nu_i\) 时只有 \(X_+\)
贡献 \(z_i-\nu_i\) 层，\(z_i<-\nu_i\) 时只有 \(X_-\) 贡献
\(-z_i-\nu_i\) 层，其余情况两边都不贡献，得到 (3)--(5)。这也可由
[盒外目标见证的精确有理缺口分母](type-I-f-overflow-rational-gap-denominator.md)
分别应用于 \(z\) 与 \(-z\) 得到。

式 (5) 是目前最精确的规范解释：\(\Omega_w\) 不是抽象的“距离”，而是缩放实例
\((P,t)=(pm,R/m)\) 的两个相反方向首分母中无法被 \(K\) 吸收的总缺陷。它本身仍不
给出从 \(P=pm\) 回到 \(p\) 的解提升。

## 为什么它不是已有块高度

对原线性状态

\[
p=a+s+asR,
\qquad U=aR+1,
\qquad V=sR+1,
\]

有 \(UV=4K\)。对奇素数 \(q_i\mid K\)，

\[
v_{q_i}(U)+v_{q_i}(V)=\nu_i.
\tag{6}
\]

另一方面，\((K,R)=1\) 且 \(m,t\mid R\)，故

\[
v_{q_i}(R)=v_{q_i}(m)=v_{q_i}(t)=0.
\tag{7}
\]

所以对奇坐标，盒外量满足

\[
(|z_i|-\nu_i)_+
=\bigl(|z_i|-v_{q_i}(U)-v_{q_i}(V)\bigr)_+.
\tag{8}
\]

它测量的是**超出当前两个块全部已有高度之后**的层，而不是能在当前块中重新找到的
同一批层；\(R,m,t\) 自身也没有相应的 \(q_i\)-进高度可付费。要使用标签差或模数差
容量，仍需另证这些额外分母层与某个确定差值之间的整除映射。

## 乐观局部三通道测试

对同一核心素数的完整有向线性源谱，令当前模数为 \(R\)。对每个 \(q\mid K\)，脚本
取以下三个刻意放宽的高度：

\[
\begin{aligned}
b_q&=\max_{(a,s)\text{ at }R}
     \max\{v_q(aR+1),v_q(sR+1)\},\\
\ell_q&=\max_{c\in\{a,s\}\text{ at }R,\ c'\ne c\text{ in full spectrum}}
     v_q(c-c'),\\
r_q&=\max_{R'\ne R\text{ in full spectrum}}v_q(R-R').
\end{aligned}
\tag{9}
\]

它们可以来自互不相容的源状态，仍把高度相加为

\[
C_q=b_q+\ell_q+r_q.
\tag{10}
\]

因此若某个最优溢出模式 \(e=(e_q)\) 满足 \(e_q\le C_q\) 对所有 \(q\)，这只说明它
通过了一个必要性很弱的装箱测试，并不证明真实收费映射。反之，如果同一状态的**所有**
最优模式都违反该逐坐标条件，那么“每个状态选一条最佳块梯、最佳标签差梯和最佳模数
差梯直接逐层注入”的模型在该状态上已经不可能。

脚本还计算原盒外见证产生的平衡约分端点 \((\bar u,\bar v)\)，并进一步放宽为

\[
C_q^+=C_q+\max\{v_q(\bar u),v_q(\bar v)\}.
\tag{11}
\]

## 完整最小层审计

复现脚本：

~~~text
reproductions/type_i_f_overflow_lower_modulus_omega_carrier_boundary.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-lower-modulus-omega-carrier-boundary-results.json
~~~

冻结输入为：

~~~text
type-i-f-overflow-lower-modulus-weighted-cost-results.json
sha256: e4bffc9727821fcfd83a5ae0bb02b8d5326ac58a024563e0a9acdfa355fded82

type-i-f-overflow-r-modulus-repair-results.json
sha256: c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

对已有精确值 \(\Omega_1\le9\) 的 36 个 F-box miss，脚本不是只检查保存的字典序代表，
而是完整枚举最小层中的全部目标向量：

~~~text
exact_state_count: 36
unresolved_state_count: 6
minimum_target_vector_count: 204
minimum_overflow_pattern_count: 93
block_infeasible_state_count: 17
three_channel_infeasible_state_count: 8
three_channel_plus_endpoint_infeasible_state_count: 8
~~~

36 个状态的 204 个最优向量全部验证 (1)--(8)。在全部并列最优模式中取最小未付层数

\[
\delta_C=\min_e\sum_q(e_q-C_q)_+,
\tag{12}
\]

仍为正的 8 个状态如下：

| \(p\) | lower \(t\) | \(\Omega_1\) | 最优模式数 | \(\delta_C\) |
|---:|---:|---:|---:|---:|
| 99151369 | 27337 | 9 | 1 | 6 |
| 223474729 | 233 | 8 | 6 | 5 |
| 310002289 | 9173 | 7 | 1 | 2 |
| 331117609 | 15413 | 4 | 1 | 1 |
| 487572409 | 106017 | 8 | 2 | 3 |
| 507599689 | 1897 | 6 | 1 | 2 |
| 507599689 | 813 | 6 | 2 | 2 |
| 570621769 | 113 | 8 | 21 | 1 |

最尖锐的样本 \(p=99151369,t=27337\) 只有一个最优模式

\[
e=(0,0,2,0,7)
\]

（素数顺序为 \(5,11,227,1409,115561\)），而乐观三通道高度为

\[
C=(7,4,2,1,1).
\]

仅 \(q=115561\) 就剩余 6 层无法注入；该坐标在平衡约分端点中的高度也是零。把端点
高度加入 (11) 后，8 个反例状态一个也没有消失。

## 与最小层共享缺口 Type II 的冻结交集

[低模数最小溢出纤维的共享缺口 Type II 覆盖边界](type-I-f-overflow-lower-modulus-min-overflow-shared-gap.md)
独立重枚举了同一批 36 个精确状态的全部 204 个 \(\Omega_1\)-最优向量。将该结果与
本卡的 8 个局部三通道不可装箱状态按 \((p,t,\text{orientation})\) 精确相交，得到：

| \(p\) | lower \(t\) | 方向 | 局部三通道装箱 | 最小层共享缺口 Type II |
|---:|---:|:---:|:---:|:---:|
| 223474729 | 233 | reverse | 不可 | 已命中 |
| 331117609 | 15413 | forward | 不可 | 已命中 |
| 507599689 | 813 | reverse | 不可 | 已命中 |
| 570621769 | 113 | reverse | 不可 | 已命中 |
| 99151369 | 27337 | reverse | 不可 | 未命中 |
| 310002289 | 9173 | reverse | 不可 | 未命中 |
| 487572409 | 106017 | forward | 不可 | 未命中 |
| 507599689 | 1897 | forward | 不可 | 未命中 |

因此局部容量装箱失败并不等于该状态没有短证书：前四个状态已经由同一精确最小层中的
共享缺口 Type II 旁路闭合。当前在这两个接口下同时未闭合的冻结硬核恰为

\[
\boxed{
(99151369,27337),\ (310002289,9173),\
(487572409,106017),\ (507599689,1897),
}
\tag{13}
\]

其中二元组为 \((p,t)\)。这是两个有限审计在 **\(\Omega_1\) 精确最小层**上的交集：
它不排除四个硬核在更高溢出层、不同权 Pareto 面、其它 Type I/II 形式或良基下降中
闭合。另六个在本脚本的成本 9 壳层中没有命中，后续 Cayley 图算法虽已精确求出其
\(\Omega_1=10,11,12,12,15,18\)，但本卡没有重枚举这些更高最小层的载体装箱，
因此也不把它们计入 (13)。

**后续更新（2026-07-30）**：
[四个低模数硬核的 q 可除差候选 Type II 分流](type-I-f-overflow-four-hard-core-collision-selector.md)
在一个明确限定的有限候选菜单中，为 \((310002289,9173)\) 与
\((507599689,1897)\) 给出独立完整的 Type II 证书。因此这四项不是全局未解清单；在
该后续选择器下当前未闭合的是另外两项。候选差本身仍不构成真实载体迁移证明。

结果 JSON 的 SHA-256：

~~~text
695b20832c683222b3021d444f5bdcb04f706ab10aeeec9801a3ad85fe85c0fb
~~~

## 结论边界

本卡证明了一个正面接口，也排除了一个过强的直接收费模型：

- 正面接口是 (5)：\(\Omega_w\) 可规范转成双向有理分母缺陷；
- 负面边界是 8 个选择不变的最小层反例：局部最佳块、标签差、模数差和原端点高度
  仍不足以逐层容纳它们。

它没有排除以下更强机制：跨多个状态或多个差值的非局部匹配、带受控复用的流/匹配
定理、使用非最小目标向量进行因子重分配、把分母缺陷送入 Type II，或以
\((P,t)=(pm,R/m)\) 为标记构造可提升的良基下降。下一步真正需要的是这类非局部匹配
或提升定理，而不是继续假设 \(\Omega_1\) 的每一单位都等于某个现成局部载体层。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_omega_carrier_boundary.py
~~~
