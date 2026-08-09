---
kind: claim
claim_id: type-II-dyadic-relation-quotient-invariant-factor-surjection-gate
title: Type II 关系商完整 Q-lift 的不变因子满射门
statement: 设关系商 Q_R 的非平凡不变因子为 b_1|...|b_s，候选单位群 U(4D') 的不变因子为 a_1|...|a_r。存在群满射 U(4D') 到 Q_R 当且仅当 s<=r 且 b_j 整除 a_{r-s+j} 对每个 j；这一步先于目标 -1、二进因子和来源标签 SNF。失败时给出秩或最小不变因子障碍；通过后仍需目标映射、来源标签、源盒像和 E1–E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-dyadic-relation-subgroup-target-preserving-quotient
  - type-II-dyadic-relation-quotient-unit-group-exponent-gate
  - type-II-annihilator-unit-group-target-map-snf-criterion
topics:
  - type-II
  - relation-quotient
  - invariant-factors
  - finite-abelian
  - surjection
  - q-lift
  - dyadic
  - source-label
  - SNF
  - arithmetic-obstruction
  - proof-program
sources:
  - claim: type-II-dyadic-relation-subgroup-target-preserving-quotient
    role: target-preserving-relation-quotient
  - claim: type-II-dyadic-relation-quotient-unit-group-exponent-gate
    role: distinguished-dyadic-factor-gate
  - claim: type-II-annihilator-unit-group-target-map-snf-criterion
    role: labelled-target-map-completion
  - reproduction: reproductions/quotient_invariant_factor_gate.py
    role: invariant-factor-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II 关系商完整 Q-lift 的不变因子满射门

## 群结构输入

令

\[
Q_R=H/R_C
\simeq C_{b_1}\oplus\cdots\oplus C_{b_s},
\qquad
1<b_1\mid b_2\mid\cdots\mid b_s,
\]

为二进关系子群商的非平凡不变因子分解。固定候选整数参数 \(D'\)，令

\[
A_{D'}=U(4D')
\simeq C_{a_1}\oplus\cdots\oplus C_{a_r},
\qquad
1<a_1\mid a_2\mid\cdots\mid a_r.
\]

平凡的 \(C_1\) 因子不写入列表。目标 \(Q_R\) 还带有规范目标元素
\(t_R=\pi_R(t)\) 和来源标签 \(\pi_R(u_i)\)；这些标签不包含在本节的纯群结构门中。

## 不变因子满射定理

有群满射

\[
\eta:A_{D'}\twoheadrightarrow Q_R
\]

当且仅当

\[
\boxed{
s\le r,
\qquad
b_j\mid a_{r-s+j}
\quad(1\le j\le s).
}
\tag{1}
\]

若 \(s>r\)，输出

\[
\mathrm{DYADIC\_FULL\_TARGET\_RANK\_OBSTRUCTED}
=(s,r).
\tag{2}
\]

若 \(s\le r\) 但某个 \(b_j\nmid a_{r-s+j}\)，输出

\[
\mathrm{DYADIC\_FULL\_TARGET\_INVARIANT\_OBSTRUCTED}
=(j,b_j,a_{r-s+j}).
\tag{3}
\]

这些回执在目标 \(-1\) 和来源标签尚未参与时已经成立，因此比完整 SNF 菜单更早、
更便宜，也不会把不同 primary 的不可能结构留到最后才发现。

### 证明

把 \(A_{D'}\) 和 \(Q_R\) 写成整数格商：

\[
A_{D'}=\mathbb Z^r/
\operatorname{diag}(a_1,\ldots,a_r)\mathbb Z^r,
\qquad
Q_R=\mathbb Z^s/
\operatorname{diag}(b_1,\ldots,b_s)\mathbb Z^s.
\]

若存在满射，有限阿贝尔群商的不变因子单调性（等价于包含关系下的 Smith
范数判据）给出：目标最少需要 \(s\) 个生成因子，故 \(s\le r\)；在两端补足
\(r-s\) 个 \(1\) 因子后，逐项有

\[
1\mid a_1,\ldots,1\mid a_{r-s},
\qquad
b_j\mid a_{r-s+j}.
\]

反过来，若 (1) 成立，把前 \(r-s\) 个源因子送到单位元，并对最后 \(s\) 个源因子
使用自然约化

\[
C_{a_{r-s+j}}\longrightarrow C_{b_j},
\qquad
x\longmapsto x\bmod b_j.
\]

每个分量满射，直积映射即为 \(A_{D'}\twoheadrightarrow Q_R\)。证毕。

## 与二进目标门的组合

设关系子群 \(R_C=2^uK\)，则 distinguished dyadic factor 是 \(C_{2^u}\)。
因此完整 Q-lift 的第一层筛为：

1. 从 \(Q_R\) 的不变因子列表识别 \(2^u\) 因子；
2. 用
   \[
   u\le v_2(\lambda(4D'))
   \]
   运行二进目标指数门；
3. 用 (1) 检查全部不变因子；
4. 若前三步通过，再运行目标元素 \(t_R\)、来源标签和满射矩阵的联合 SNF；
5. 最后检查源盒像、统一 CRT、范围、正规形和 E1--E5。

不变因子门与二进指数门的作用不同：

- \(u>v_2(\lambda(4D'))\) 时，二进 distinguished factor 本身不可映；
- 二进门通过但 (1) 失败时，其它 primary 或目标秩使完整商不可映；
- (1) 通过但联合 SNF 失败时，是 \(-1\) 或来源标签的仿射障碍；
- 联合 SNF 通过但源盒像或 E1--E5 失败时，是整数回译障碍。

只有全部门通过，才输出

\[
\mathrm{DYADIC\_RELATION\_STRICT\_Q\_LIFT}.
\tag{4}
\]

## 带目标和来源标签的后续 SNF

不变因子门不保证给定 \(t_R\) 可由 \(-1\) 送达，也不保证来源元素有指定像。
在 invariant-factor 坐标中，令 \(Y\) 是 \(A_{D'}\to Q_R\) 的同态矩阵。除同态阶约束
外加入

\[
Y(-1)=t_R,
\qquad
Y(u_i)=\pi_R(u_i).
\tag{5}
\]

按一般单位群—目标 SNF 判据，(5) 的有限解集和满射性分别由联合同余 SNF 与
\([N\mid Y]\) 的商 SNF 判定。若不变因子门已经失败，不需要枚举 \(Y\)；若它通过但
所有 \(Y\) 的目标/来源条件失败，输出

\[
\mathrm{DYADIC\_FULL\_TARGET\_LABEL\_SNF\_OBSTRUCTED}.
\tag{6}
\]

若 \(Y\) 通过但

\[
Y(\text{候选整数源盒像})\ne\pi_R(S),
\tag{7}
\]

输出

\[
\mathrm{DYADIC\_FULL\_TARGET\_FIBER\_UNREALIZED}.
\tag{8}
\]

这一步保留有限盒范围，避免把“群满射”误当成“当前来源盒实际回译”。

## 控制实例

### \(U(4)\) 到 \(C_2\times C_2\)

\(U(4)\simeq C_2\)，故 \(r=1\)；目标 \(C_2\times C_2\) 有 \(s=2\)。
式 (2) 立即输出秩障碍。这正是前一 \(C_2\times C_{16}\) 关系商控制中的完整
Q-lift 障碍，尽管 distinguished \(C_2\) 单独通过二进指数门。

### \(U(12)\) 到 \(C_2\times C_2\)

\(U(12)\simeq C_2\times C_2\)，两侧列表都为 \((2,2)\)，式 (1) 通过。此时
是否把 \(-1\) 送到指定 \(t_R\)，以及是否保持来源标签，要交给联合 SNF；群结构
本身不再阻塞。

### \(C_2\times C_4\) 到 \(C_4\times C_4\)

源列表为 \((2,4)\)，目标列表为 \((4,4)\)。第一项 \(4\nmid2\)，输出式 (3)；
这说明源的一个低阶 C2 因子不能被“池化”成目标所需的 C4 因子。

## 复现

~~~bash
python3 -m py_compile reproductions/quotient_invariant_factor_gate.py
python3 reproductions/quotient_invariant_factor_gate.py --verify
~~~

复现器验证秩不足、因子整除通过/失败、混合 primary 和 \(U(4)\)、\(U(12)\) 控制。

## 研究边界

该门把完整关系商的群结构不可能性前置处理，但不替代目标/来源标签 SNF，也不
证明源盒像等式或 E1--E5。它的价值是：一旦关系商 \(Q_R\) 给定，许多候选 \(D'\)
可以在进入 Fourier、容量或算术菜单前被严格删除；其余候选再进入带标签的完整
Q-lift 分派。

