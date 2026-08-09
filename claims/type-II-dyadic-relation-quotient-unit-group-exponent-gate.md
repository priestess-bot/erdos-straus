---
kind: claim
claim_id: type-II-dyadic-relation-quotient-unit-group-exponent-gate
title: Type II 二进关系商的单位群指数—目标对合可提升判据
statement: 设关系商的规范二进因子为 C_{2^b}，候选整数状态的单位群为 U(4D')。忽略额外来源标签时，存在满射 U(4D') 到 C_{2^b} 且把 -1 送到目标顶位对合，当且仅当 b 不超过 v_2(lambda(4D'))；该指数精确等于 max(1,v_2(D'), max_{q|D', q odd} v_2(q-1))。加入来源标签后，存在性精确化为一个有限的二进同态—标签 SNF 系统；指数门失败时立即给出 DYADIC_TARGET_EXPONENT_OBSTRUCTED，指数门通过但联合系统失败时给出带标签的目标映射障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-dyadic-relation-subgroup-target-preserving-quotient
  - type-II-annihilator-unit-group-target-map-snf-criterion
  - type-II-source-label-snf-failure-anchor-relation-dichotomy
topics:
  - type-II
  - dyadic
  - relation-quotient
  - unit-group
  - Carmichael-exponent
  - target-map
  - source-label
  - SNF
  - arithmetic-lift
  - proof-program
sources:
  - claim: type-II-dyadic-relation-subgroup-target-preserving-quotient
    role: dyadic-quotient-factor
  - claim: type-II-annihilator-unit-group-target-map-snf-criterion
    role: full-target-surjection-SNF
  - claim: type-II-source-label-snf-failure-anchor-relation-dichotomy
    role: labelled-source-obstruction
  - reproduction: reproductions/dyadic_unit_group_target_gate.py
    role: Carmichael-exponent-and-target-gate-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II 二进关系商的单位群指数—目标对合可提升判据

## 二进关系商因子

设前一引理产生

\[
R_C=2^sK\ne\{0\},
\qquad
K\simeq C_{2^a}.
\]

则

\[
K/R_C\simeq C_{2^b},
\qquad
b=s,
\qquad
0\le b<a.
\tag{1}
\]

\(b=0\) 时商的二进因子是平凡群；以下只讨论 \(b\ge1\)。在关系商
\(Q_R=H/R_C\) 中，这个 \(C_{2^b}\) 是由原核 \(K\) 继承的 distinguished dyadic
factor；\(Q_R\) 还可能含有其它二进或奇数 primary 因子。

固定候选整数参数 \(D'\)，写

\[
A_{D'}=U(4D'),
\qquad
\lambda_{D'}=\lambda(4D')
\]

其中 \(\lambda\) 是 Carmichael 函数。目标 \(C_{2^b}\) 的顶位对合记为
\(2^{b-1}\in\mathbb Z/2^b\mathbb Z\)。

## 无来源标签的精确判据

有如下充要条件：

\[
\boxed{
\exists\ \eta:A_{D'}\twoheadrightarrow C_{2^b},
\quad
\eta(-1)=2^{b-1}
\iff
2^b\mid\lambda_{D'}.
}
\tag{2}
\]

等价地，定义

\[
e_2(D')=v_2(\lambda(4D')),
\]

则目标门通过当且仅当

\[
\boxed{b\le e_2(D').}
\tag{3}
\]

当 \(b>e_2(D')\) 时，输出

\[
\mathrm{DYADIC\_TARGET\_EXPONENT\_OBSTRUCTED}
=(D',b,e_2(D'),\lambda(4D')).
\tag{4}
\]

这个障碍只针对 distinguished dyadic factor；若 \(Q_R\) 还有其它因子，(3) 通过后仍
必须对完整 \(Q_R\) 运行一般目标满射 SNF。

## \(e_2(D')\) 的显式公式

写

\[
D'=2^u\prod_{i=1}^r q_i^{f_i},
\qquad q_i\ \text{为互异奇素数}.
\]

则

\[
\boxed{
e_2(D')
=
\max\left(
1,\,
u,\,
v_2(q_1-1),\ldots,v_2(q_r-1)
\right).
}
\tag{5}
\]

约定空的奇素数最大值不参与；因此 \(D'\) 为奇数时 \(e_2(D')\ge1\)。

### 证明

单位群的中国剩余分解把 \(A_{D'}\) 的 2-primary 指数写成各素幂单位群指数的
最大值。对 \(2^{u+2}\) 部分，

\[
v_2\!\left(\lambda(2^{u+2})\right)=\max(1,u),
\]

对奇素数幂 \(q_i^{f_i}\) 部分，

\[
v_2\!\left(\lambda(q_i^{f_i})\right)=v_2(q_i-1).
\]

取最大值得到 (5)。

## 目标对合的充要性证明

必要性很直接：任何商群的指数整除源群指数，所以若
\(\eta:A_{D'}\twoheadrightarrow C_{2^b}\)，必有
\(2^b\mid\lambda_{D'}\)。

为证充分性，取 \(A_{D'}\) 的 2-primary 循环分解。标准单位群分解具有一个 sign
\(C_2\) 因子，\(-1\) 在该因子上是生成元；其余循环因子上的 \(-1\) 坐标或者是
零（来自 \(2\)-幂单位群的长因子），或者是该循环因子的唯一顶位对合（来自奇素数
幂单位群）。由 \(b\le e_2(D')\)，存在一个阶 \(2^f\) 且 \(f\ge b\) 的循环因子。

- 若选中的因子 \(f=b\) 上 \(-1\) 是顶位对合，把该因子的生成元送到
  \(C_{2^b}\) 的生成元，其它因子送零；\(-1\) 正好送到 \(2^{b-1}\)，且映射满射。
- 若选中的因子 \(f>b\)，其顶位对合映到 \(C_{2^b}\) 时为零；把该因子生成元送到
  \(C_{2^b}\) 生成元，再把 sign \(C_2\) 因子送到 \(2^{b-1}\)，即可同时得到
  满射和 \(\eta(-1)=2^{b-1}\)。
- 若 \(f=b\) 而该因子的 \(-1\) 坐标为零，则同样用 sign 因子承担目标对合，并由
  该 \(f=b\) 因子承担满射。

\(b=1\) 时直接使用 sign \(C_2\) 因子。故 (2) 成立。

## 带来源标签的二进 SNF 判据

指数门只处理 distinguished dyadic factor。若还要求来源元素
\(u_1,\ldots,u_m\in A_{D'}\) 映到指定标签
\(v_1,\ldots,v_m\in C_{2^b}\)，将 \(A_{D'}\) 的 2-primary 部分写成

\[
A_{D',2}=\bigoplus_{j=1}^{r_2}C_{2^{e_j}},
\]

并在此坐标中记 \(-1\) 和 \(u_i\) 的坐标为
\(a=(a_j)\) 和 \(c_i=(c_{ij})\)。未知同态由
\(y_j\in\mathbb Z/2^b\mathbb Z\) 给出，完整条件为

\[
2^{e_j}y_j\equiv0\pmod{2^b},
\tag{6}
\]

\[
\sum_j a_jy_j\equiv2^{b-1}\pmod{2^b},
\tag{7}
\]

\[
\sum_j c_{ij}y_j\equiv v_i\pmod{2^b}
\qquad(1\le i\le m).
\tag{8}
\]

同时满射性等价于

\[
\gcd(2^b,y_1,\ldots,y_{r_2})=1.
\tag{9}
\]

把 (6)--(8) 加入整数辅助变量并运行 SNF，得到：

\[
\boxed{
\text{存在带来源标签的目标满射}
\iff
\text{该联合 SNF 可解且存在满足 (9) 的解}.
}
\tag{10}
\]

若 (3) 失败，无需构造 (6)--(10)；若 (3) 通过但 (10) 失败，输出
\[
\mathrm{DYADIC\_TARGET\_LABEL\_SNF\_OBSTRUCTED}
\]
及最小失败行或非平凡商因子。若 (10) 通过但 \(Q_R\) 的其它 primary 因子无法同时
满射，则输出完整 G1/SNF 的
\(\mathrm{DYADIC\_FULL\_TARGET\_MAP\_OBSTRUCTED}\)，不能把纯二进门误记为完整
Q-lift。

## 与关系商 Q-lift 的接线

对关系商 \(Q_R=H/R_C\)，先从 \(R_C=2^sK\) 读出 distinguished factor
\(C_{2^s}\)，再按如下顺序处理候选 \(D'\)：

1. 计算 \(e_2(D')\)；
2. 若 \(s>e_2(D')\)，输出 (4)，该候选在二进目标阶上不可能；
3. 若 \(s\le e_2(D')\)，运行带来源的 (6)--(10)；
4. 对 \(Q_R\) 的其它 invariant factors 运行一般单位群—目标满射 SNF；
5. 只有完整目标映射、源盒像、来源 CRT、范围和 E1--E5 全部通过，才把关系商记为
   \(\mathrm{DYADIC\_RELATION\_STRICT\_Q\_LIFT}\)。

因此这个门可以在 Q1 菜单阶段提前删除一批不可能的 \(D'\)，并把纯二进指数
障碍与标签/全目标障碍分开。

## 控制例

### \(D'=1\)：纯 \(C_2\) 通过、\(C_4\) 失败

\[
U(4)\simeq C_2,\qquad
e_2(1)=1.
\]

所以 \(C_2\) 目标可由模 4 符号映射承载，而 \(C_4\) 目标输出
\(\mathrm{DYADIC\_TARGET\_EXPONENT\_OBSTRUCTED}\)。

### \(D'=5\)：\(C_4\) 通过、\(C_8\) 失败

\[
U(20)\simeq C_2\times C_4,\qquad
e_2(5)=2.
\]

因此 \(C_4\) 的 distinguished factor 通过指数门，\(C_8\) 被指数门排除。

### 关系商 \(C_2\times C_2\) 的分离

上一个 \(C_2\times C_{16}\) 控制例的关系商为
\(Q_R\simeq C_2\times C_2\)。其 distinguished \(C_2\) 因子在 \(D'=1\) 时通过
(3)，但 \(U(4)\) 本身只有 2 个元素，不能满射到整个 \(C_2\times C_2\)；完整
G1/SNF 因而输出群阶/满射障碍。这说明“二进指数门通过”不是完整 Q-lift 的充分条件。

## 复现

~~~bash
python3 -m py_compile reproductions/dyadic_unit_group_target_gate.py
python3 reproductions/dyadic_unit_group_target_gate.py --verify
~~~

复现器在 \(1\le D'\le40\) 的有限控制上直接计算 \(U(4D')\) 的群指数，并与 (5)
比较；同时验证 \(D'=1,3,5,15,4,8\) 的 \(C_{2^b}\) 目标门边界。

## 研究边界

该判据把关系商的二进目标映射从一般抽象 G1 菜单中分离成一个闭式算术筛，但它
只处理 distinguished dyadic factor。它不自动实现其它 primary 因子、来源标签或
有限盒像；这些仍需完整联合 SNF、source-switch 和 E1--E5。指数门通过而完整门
失败时，失败本身是可继续送入 Fourier/格/容量分派的精确障碍，不是猜想反例。

