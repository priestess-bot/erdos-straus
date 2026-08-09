---
kind: claim
claim_id: type-II-dyadic-target-fiber-maximal-quotient-dedup
title: Type II 二进目标纤维的最大目标保持商与顶位源类去重
statement: 在 C_{2^a} 核目标纤维中，若 d 是 F_t 的最大二进深度，则 L=2^{d+1}K 是包含关系下最大的二进子群，使 H/L 仍保持目标缺失；所有深度 d 的纤维偏移在 H/L 中都等于唯一顶位类 2^d kappa+L。因而同一状态和商层的多个最大深度表示只能贡献一个顶位源类容量单位；额外表示必须记录为来源标签差异或 lift 候选，不能重复计入 Hall/q 容量。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-dyadic-target-fiber-max-depth-relay
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-source-fiber-shared-q-ledger
topics:
  - type-II
  - dyadic
  - target-fiber
  - maximal-quotient
  - source-deduplication
  - q-adic-capacity
  - Hall
  - source-relation
  - quotient-descent
  - proof-program
sources:
  - claim: type-II-dyadic-target-fiber-max-depth-relay
    role: maximum-depth-quotient
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: typed-capacity-graph
  - claim: type-II-q-prefix-source-crt-fiber-concentration
    role: common-fiber-concentration
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: quotient-source-relation
  - reproduction: reproductions/dyadic_target_fiber_max_depth.py
    role: maximum-quotient-and-top-class-control
visibility: public
last_checked: '2026-08-09'
---

# Type II 二进目标纤维的最大目标保持商与顶位源类去重

## 1. 设置

沿用二进目标纤维设置。令 \(H\) 为有限阿贝尔群，\(K=\langle\kappa\rangle\simeq
C_{2^a}\)，令 \(t=-t\)，并令 \(S=-S\) 满足

\[
t\notin S,
\qquad
F_t=\{k\in K:t+k\in S\}\ne\varnothing,
\qquad
0\notin F_t.
\tag{1}
\]

对 \(k\ne0\) 定义

\[
\operatorname{dep}_2(k)=\max\{j:k\in2^jK\},
\qquad
d=\max_{k\in F_t}\operatorname{dep}_2(k),
\qquad
L_d=2^{d+1}K.
\tag{2}
\]

前一引理已经证明 \(F_t\cap L_d=\varnothing\)，所以目标在 \(H/L_d\) 中仍缺失。
本卡加强这一结论的最大性和容量含义。

## 2. 最大目标保持二进商

对 \(0\le j\le a\)，记 \(L_j=2^jK\)。则

\[
\boxed{
L_j\cap F_t=\varnothing
\quad\Longleftrightarrow\quad
j\ge d+1.
}
\tag{3}
\]

### 证明

若 \(j\ge d+1\)，则 \(L_j\subseteq L_d\)，而
\(F_t\cap L_d=\varnothing\)，故 \(L_j\cap F_t=\varnothing\)。

反之，若 \(j\le d\)，取 \(k_d\in F_t\) 满足
\(\operatorname{dep}_2(k_d)=d\)。由定义
\(k_d\in2^dK=L_d\)，又因 \(L_j\supseteq L_d\)，得到
\(k_d\in L_j\cap F_t\)，矛盾。证毕。

因此 \(L_d=L_{d+1}\) 是包含关系下最大的二进子群，使目标在商中继续缺失：

\[
\boxed{
H/L_d
\text{ 是所有目标保持二进商中阶数最小的规范商。}
}
\tag{4}
\]

这里“最大”指子群包含关系；不能再取 \(L_j\supsetneq L_d\) 而保持目标缺失。
当 \(d=a-1\) 时 \(L_d=\{0\}\)，(4) 说明二进商没有任何非平凡压缩空间，这正是
顶层二进终端，而不是一个尚未选择好的低层商。

## 3. 最大深度表示的唯一顶位类

定义最大深度偏移集

\[
F_t^{(d)}
=\{k\in F_t:\operatorname{dep}_2(k)=d\}.
\tag{5}
\]

对任意 \(k,k'\in F_t^{(d)}\)，可写成

\[
k=2^d u\kappa,\qquad
k'=2^d u'\kappa,
\qquad
u,u'\text{ 为奇数}.
\tag{6}
\]

于是 \(u-u'\) 为偶数，得到

\[
k-k'=2^d(u-u')\kappa\in2^{d+1}K=L_d.
\tag{7}
\]

所以商映射 \(\pi_d:H\to H/L_d\) 满足

\[
\boxed{
\pi_d(t+k)=\pi_d(t+k')
=\pi_d(t)+\omega_d,
\qquad
\omega_d=2^d\kappa+L_d.
}
\tag{8}
\]

这不是“表示数相同”的计数近似，而是目标纤维中所有最大深度成员的精确商类
恒等式。若 \(z,z'\) 是它们的指数表示，则

\[
\phi(z-z')=k-k'\in L_d,
\tag{9}
\]

说明其源指数差异在该商中完全落入被杀掉的关系子群。

反过来，若 \(k\in F_t\) 的商像等于 \(\omega_d\)，则 \(k\) 不可能有深度
\(<d\)：低于 \(d\) 的二进赋值不可能模 \(2^{d+1}K\) 变成
\(2^d\kappa+L_d\)。由于 \(d\) 是最大深度，故该商顶位类的原像恰为
\(F_t^{(d)}\)。因此

\[
\boxed{
\left|\{\pi_d(t+k):k\in F_t^{(d)}\}\right|=1.
}
\tag{10}
\]

## 4. 对 Hall/q 容量的严格去重

固定一个状态 \(s\) 和最大深度 \(d\)，令 \(\mathcal R_{s,d}\) 是所有仅由
\(F_t^{(d)}\) 的表示产生的请求。把请求映射到其商源类：

\[
\tau_{s,d}:\mathcal R_{s,d}\longrightarrow H/L_d,
\qquad
\tau_{s,d}(r)=\pi_d(t+k_r).
\tag{11}
\]

由 (10)，\(\operatorname{im}\tau_{s,d}\) 只有一个元素。于是对按商源类计容量的
资源图，规范容量不是 \(|\mathcal R_{s,d}|\)，而是

\[
\boxed{
\kappa_{\mathrm{top}}(s,d)
=\left|\operatorname{im}\tau_{s,d}\right|=1
\quad\text{(当 }F_t^{(d)}\ne\varnothing\text{)}.
}
\tag{12}
\]

若 \(m=|\mathcal R_{s,d}|>1\)，且这些请求没有额外的、在商之前保持来源标签的
独立物理槽，则最小 Hall 集直接给出

\[
\boxed{
U=\mathcal R_{s,d},
\qquad
N(U)=\{\omega_d\},
\qquad
|U|-|N(U)|=m-1.
}
\tag{13}
\]

回执为 DYADIC_TOP_CLASS_DUPLICATE。它的含义是同一顶位类被多个表示重复请求，
不是原猜想的反证；额外表示应保留为 DYADIC_TOP_SOURCE_LABEL_RELAY，继续检查
它们在 \(L_d\) 中的来源差、SNF、CRT 和 E1--E5，而不能再次向 \(H/L_d\) 的 q
容量收费。

若不同请求来自不同参数纤维，(10) 只在各自纤维内成立；必须先通过 source-CRT
共同候选和 FIBER_REALIZED。跨纤维的多个顶位类不能直接合并，也不能把每个
纤维的一单位当作同一商中的多单位。

## 5. 与短关系和提升的接线

若 \(t\notin K\)，取两个最大深度表示 \(z,z'\)，(9) 给出一个落入 \(L_d\) 的
源关系。这个关系有三种精确用途：

1. 若其指数差仍在预算内，它是一个层 \(d+1\) 的内部二进源关系；
2. 若超出预算，它产生带方向的 \(L_d\)-溢出单位；
3. 若只在商中使用，则该关系被杀掉，两个表示必须先按 (12) 去重。

因此“多个最大深度表示”不能同时被解释为多个独立顶层 Fourier 角色。只有当
\(L_d\) 中的来源差异经过独立 source-switch 回译为新的、更小状态时，才可能从
去重后的单个顶位类重新产生递降边。

如果 \(d<a-1\)，先在 \(H/L_d\) 中处理唯一顶位类，再运行来源 CRT、SNF、范围和
E1--E5。若通过并且模数或来源势严格下降，得到

~~~text
DYADIC_MAXIMAL_QUOTIENT_SOURCE_SWITCH
quotient = H / (2^(d+1) K)
top_class_capacity = 1
strict_potential_drop = true
~~~

若商中顶位类的来源合同为空，输出

~~~text
DYADIC_MAXIMAL_QUOTIENT_LIFT_OBSTRUCTED
failed_gate = SOURCE_CRT | SNF | RANGE | E1_E5
top_class_capacity = 1
~~~

这比“低层商候选不存在”更精确：它同时证明了任何更大的二进核都会破坏目标
缺失，因而不能通过改选另一个二进商来规避障碍。

## 6. \(C_2\times C_8\) 多表示控制

取

\[
H=C_2\times C_8,\qquad
K=\{0\}\times C_8,\qquad
t=(1,0),
\]

源列

\[
g_1=(1,2),\qquad g_2=(0,4),
\qquad \nu_1=\nu_2=1.
\tag{14}
\]

目标 \(t\) 未命中，而目标陪集中的偏移为 \(F_t=\{2,6\}\)，二进深度最大值
\(d=1\)。因此 \(L_d=4K\)，且

\[
K/L_d\simeq C_4,\qquad
F_t^{(d)}\bmod L_d=\{2+L_d\}.
\tag{15}
\]

不同指数表示可以产生偏移 \(2\) 或 \(6\)，但它们在商中都落到同一个顶位源类；
复现器报告 top_source_class_count = 1。逐级测试 \(K,2K,4K,\{0\}\) 后，第一
个与 \(F_t\) 不相交的尾是 \(4K\)，证明最大性。

改取单列 \(g=(1,4)\)、\(\nu=1\) 时 \(F_t=\{4\}\)、\(d=a-1\)，只有零尾
\(L_d=\{0\}\) 能保持目标缺失；这是顶层去重而不是低模数候选遗漏。

复现：

~~~bash
python3 reproductions/dyadic_target_fiber_max_depth.py --verify
~~~

## 研究边界

本引理新增了两个可直接进入统一选择器的硬约束：二进目标保持商是唯一的最大
dyadic tail，且每个状态/层的最大深度表示在该商中只有一个顶位源类。它能删除
虚假的重复 Hall/q 请求，并把剩余来源差异精确送入 \(L_d\) 的 source-switch 或
溢出分支。

它仍不证明 \(L_d\) 的商一定有合法整数提升；若来源合同或 E1--E5 失败，必须保留
具体 lift obstruction，并转交 Type I/II、广义 \(2^j\) 终端或稳定子塔递降。
