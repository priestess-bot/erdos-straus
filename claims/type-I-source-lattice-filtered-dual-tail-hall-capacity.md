---
kind: claim
claim_id: type-I-source-lattice-filtered-dual-tail-hall-capacity
title: 源格障碍过滤的短正合列与上尾 Hall 容量
statement: >-
  设 L 是 Z^d 的源关系子格，q 是奇素数，并令
  F_J=L∩q^(J+1)Z^d、O_J=(F_J+qL)/qL。层 J 的 q-height
  对偶像 V_J 恰是 O_J 在 Hom(L,F_q) 中的湮灭子，因而有规范短正合列
  0 -> V_J -> Hom(L,F_q) -> O_J^* -> 0。对任意角色子空间 W，固定层
  可实现空间为 W_J=W intersect V_J，其余独立需求数精确等于限制映射的秩。
  对尚未绑定物理层、合法层仅由最小 q-height 决定的请求，若层 1,...,H 的纯代数
  容量为 c_J，且下游合同允许在 W 内换基，则存在一个过滤适配基及无重复层分派，
  当且仅当每个上尾阈值 k 的未实现商维数不超过
  层 k,...,H 的总容量；失败阈值给出严格、基不变的容量缺口。若角色带名且不可
  换基，同一结论改为逐角色最小深度的上尾 Hall 计数。额外的范围、标签、
  occurrence 或 source-switch 边会破坏纯后缀图，届时该判据只保留为必要切割，
  必须返回一般 Hall/Rado 门。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-source-lattice-qheight-dual-valuation-shift-carrier
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-cross-state-layered-rado-qcapacity-cut
  - type-II-rado-linear-rank-hall-capacity-bridge
topics:
  - type-I
  - type-II
  - source-lattice
  - Smith-normal-form
  - exact-sequence
  - filtered-dual
  - q-height
  - Hall
  - Rado
  - tail-capacity
  - strict-obstruction
  - capacity-map
  - proof-program
sources:
  - claim: type-I-source-lattice-qheight-dual-valuation-shift-carrier
    role: exact-single-role-qheight-image-and-Smith-depth
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: general-capacitated-Hall-boundary
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: physical-layer-and-source-column-rank-boundary
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: independent-role-matching-boundary
  - reproduction: reproductions/type_i_source_lattice_filtered_dual_tail_hall_capacity.py
    role: focused-exact-sequence-tail-capacity-and-basis-boundary-controls
visibility: public
last_checked: '2026-08-10'
---

# 源格障碍过滤的短正合列与上尾 Hall 容量

## 1. 障碍商空间与短正合列

固定奇素数 \(q\)、秩为 \(r\) 的子格 \(L\le\mathbb Z^d\)，并沿用

\[
F_J(L)=L\cap q^{J+1}\mathbb Z^d,
\qquad
V_J=\operatorname{im}\rho_J
\le V:=\operatorname{Hom}(L,\mathbb F_q).
\tag{1}
\]

每个 \(V\) 中的角色都通过 \(L/qL\) 因子化。定义第 \(J\) 层仍可见的源格障碍空间

\[
\boxed{
O_J(L)=\frac{F_J(L)+qL}{qL}
\cong\frac{F_J(L)}{F_J(L)\cap qL}
\le \frac L{qL}.}
\tag{2}
\]

把角色限制到 \(O_J(L)\)，得到线性映射

\[
\operatorname{res}_J:V\longrightarrow O_J(L)^*.
\tag{3}
\]

已有单层对偶像公式给出

\[
\ker(\operatorname{res}_J)
=\operatorname{Ann}_V(O_J(L))
=\operatorname{Ann}_V(F_J(L))
=V_J.
\tag{4}
\]

任意有限维向量子空间上的线性泛函都可延拓到 \(L/qL\)，所以
\(\operatorname{res}_J\) 满射。于是有短正合列

\[
\boxed{
0\longrightarrow V_J\longrightarrow V
\mathop{\longrightarrow}^{\operatorname{res}_J}
O_J(L)^*\longrightarrow0.}
\tag{5}
\]

式 (5) 把“某个角色在第 \(J\) 层失败”提升为一个完整的障碍商：它不仅给出单个
阻碍向量，还精确记录该层最多能同时实现多少个独立角色。

## 2. Smith 过滤与任意角色子空间的精确秩

取固定的 Smith 坐标

\[
L=\bigoplus_{i=1}^r d_i\mathbb Z e_i,
\qquad t_i=v_q(d_i),
\tag{6}
\]

并记 \(\varepsilon_i\in V\) 为生成元 \(d_i e_i\) 的对偶角色。由
\(F_J(L)\) 的 Smith 生成元可得

\[
\boxed{
O_J(L)=
\left\langle[d_i e_i]:t_i\ge J+1\right\rangle_{\mathbb F_q},}
\qquad
\boxed{
V_J=
\left\langle\varepsilon_i:t_i\le J\right\rangle_{\mathbb F_q}.}
\tag{7}
\]

特别地，\(O_{J+1}\le O_J\)、\(V_J\le V_{J+1}\)，且

\[
\dim O_J=\#\{i:t_i\ge J+1\},
\qquad
\dim V_J=\#\{i:t_i\le J\}.
\tag{8}
\]

现在固定一个真正需要支付的角色子空间 \(W\le V\)，并定义

\[
W_J:=W\cap V_J.
\tag{9}
\]

限制 (5) 到 \(W\)，得到左正合列

\[
0\longrightarrow W_J\longrightarrow W
\mathop{\longrightarrow}^{\operatorname{res}_J|_W}O_J(L)^*.
\tag{10}
\]

因此第 \(J\) 层的精确可实现秩和障碍秩分别为

\[
\boxed{
\dim W_J
=\dim W-\operatorname{rank}(\operatorname{res}_J|_W),}
\tag{11}
\]

\[
\boxed{
b_J(W):=\dim W-\dim W_J
=\operatorname{rank}(\operatorname{res}_J|_W).}
\tag{12}
\]

若 \(W\) 的一组基在 \((\varepsilon_i)\) 中组成行矩阵 \(G\)，并令

\[
I_J=\{i:t_i\ge J+1\},
\tag{13}
\]

则有完全可计算的公式

\[
\boxed{b_J(W)=\operatorname{rank}_{\mathbb F_q}G_{*,I_J}.}
\tag{14}
\]

所以一个非零满秩子式或行阶梯形 pivot 表就是固定层的严格多角色阻碍证书；普通槽数
不能消除这个秩。

## 3. 可换基角色子空间的上尾容量定理

本节只处理**尚未绑定物理层**、其合法层仅由最小 \(q\)-height 决定的新请求。
已经绑定 \(J_{\rm req}\) 的角色必须停留在该层，并由 (11)--(14) 检查
\(W\cap V_{J_{\rm req}}\)；不得把 fixed-layer 失败改成后缀调度。

固定可选物理层 \(1,\ldots,H\)，其中 \(H\ge1\)，第 \(J\) 层有 \(c_J\ge0\) 个
只经过代数 \(q\)-height 门的容量单位。这里暂时没有范围、标签、occurrence 或
source-switch 限制。因为可选物理层从 1 开始，约定

\[
P_0=0,
\qquad
P_J=W\cap V_J\quad(1\le J\le H).
\tag{15}
\]

注意：\(P_0=0\) 是调度约定，不是声称 \(W\cap V_0=0\)；所有深度 0 的角色也在
第一个物理层统一收费。定义过滤增量

\[
a_1=\dim P_1,
\qquad
a_J=\dim P_J-\dim P_{J-1}\ (2\le J\le H),
\qquad
a_{H+1}=\dim W-\dim P_H,
\tag{16}
\]

以及上尾容量

\[
C_{\ge k}=\sum_{J=k}^H c_J
\quad(1\le k\le H),
\qquad C_{\ge H+1}=0.
\tag{17}
\]

**上尾容量定理。** 下列三项等价：

1. 存在 \(W\) 的一组基 \(\mathcal B\) 和分层映射
   \(\lambda:\mathcal B\to\{1,\ldots,H\}\)，使
   \(b\in V_{\lambda(b)}\)，且每层至多接收 \(c_J\) 个基向量；
2. \(W\subseteq V_H\)，并且对每个 \(1\le k\le H\)，
   \[
   \boxed{
   \dim W-\dim P_{k-1}\le C_{\ge k};}
   \tag{18}
   \]
3. 对每个 \(1\le k\le H+1\)，
   \[
   \boxed{
   \sum_{J=k}^{H+1}a_J\le C_{\ge k}.}
   \tag{19}
   \]

### 证明

若已有 (1) 中的分派，则一组基最多有 \(\dim P_{k-1}\) 个向量落在
\(P_{k-1}\) 内。因此至少

\[
\dim W-\dim P_{k-1}
\tag{20}
\]

个基向量不在 \(V_{k-1}\)，它们不可能分配到低于 \(k\) 的层，只能占用上尾
\(k,\ldots,H\)。这证明 (18) 的必要性。所有基向量都在某个 \(V_J\subseteq V_H\)
中，还给出 \(W\subseteq V_H\)。

反之，逐层把 \(P_{J-1}\) 的一组基延拓为 \(P_J\) 的基。由
\(W=P_H\)，最终得到一组过滤适配基，恰有 \(a_J\) 个向量第一次出现在层 \(J\)。
这些向量的合法层集合都是后缀

\[
\{J,J+1,\ldots,H\}.
\tag{21}
\]

把每层复制成 \(c_J\) 个单位槽。后缀邻域的 Hall 条件恰是 (19)：阈值不小于
\(k\) 的全部向量只能进入层 \(k,\ldots,H\)。故存在完整匹配；等价地，可按首次
出现层从大到小处理，并总取最小的未用合法层。式 (16) 的望远镜求和给出

\[
\sum_{J=k}^{H+1}a_J
=\dim W-\dim P_{k-1},
\tag{22}
\]

其中 \(k=H+1\) 正好要求 \(W=P_H\)。所以三项等价。证毕。

结合 (12)，判据可以直接写成 Smith 限制秩：

\[
\dim W\le\sum_{J=1}^Hc_J,
\qquad
b_{k-1}(W)\le\sum_{J=k}^Hc_J\quad(2\le k\le H),
\qquad
b_H(W)=0.
\tag{23}
\]

若某个阈值失败，定义

\[
\Delta_k(W,c)
=\dim W-\dim P_{k-1}-C_{\ge k}>0.
\tag{24}
\]

则商空间 \(W/P_{k-1}\)、其规范行阶梯形限制矩阵和层容量表共同构成严格的

~~~text
ROLE_SUBSPACE_QHEIGHT_TAIL_CAPACITY_DEFICIT
~~~

证书。它对 \(W\) 的展示基不变；换一组生成元不能消除 (24)。

## 4. 带名角色的上尾 Hall 判据与换基边界

若下游合同固定的是一组不可重命名、但尚未绑定具体物理层的独立角色

\[
\Gamma=(\gamma_1,\ldots,\gamma_m),
\tag{25}
\]

则不能任意替换为 \(W=\langle\Gamma\rangle\) 的过滤适配基。令截断最小物理深度为

\[
r_i=
\min\bigl(\{J\in\{1,\ldots,H\}:\gamma_i\in V_J\}\cup\{H+1\}\bigr).
\tag{26}
\]

若 \(d_q(L,\gamma_i)\le H\)，则

\[
r_i=\max(1,d_q(L,\gamma_i));
\tag{27}
\]

否则 \(r_i=H+1\)，表示窗口内不可实现。每个角色的纯代数邻域是后缀
\(\{r_i,\ldots,H\}\)。因此带名角色存在无重复层分派，当且仅当

\[
\boxed{
\#\{i:r_i\ge k\}\le C_{\ge k}
\qquad(1\le k\le H+1).}
\tag{28}
\]

这是一般带容量 Hall 定理在嵌套后缀图上的精确压缩。失败时，阈值 \(k\) 和角色集
\(\{i:r_i\ge k\}\) 给出 `NAMED_ROLE_QHEIGHT_TAIL_HALL_DEFICIT`。

式 (18) 与 (28) 不能混用：

* 若 Fourier/格合同只指定角色子空间 \(W\)，允许任何独立基表示同一个需求，则必须
  使用基不变的 (18)，并输出过滤适配基；
* 若 anchor、target、source label 或 occurrence key 绑定到每个 \(\gamma_i\)，这些
  角色不可换基，必须使用 (28)；
* 若 \(\gamma_i\) 已绑定精确层 \(J_i\)，其合法层不是后缀而是 singleton；先在
  \(V_{J_i}\) 检查原层可实现性，再把 singleton 边交给一般 Hall/Rado，禁止加深重标；
* 若物理门从后缀中删除任何边，(18) 与 (28) 都只剩必要条件，充分性必须交回一般
  Hall/Rado 图，不能把代数层容量冒充真实 carrier mapping。

## 5. 严格正负控制

取

\[
q=3,
\qquad
L=3\mathbb Z e_1\oplus9\mathbb Z e_2.
\tag{29}
\]

记 \(\varepsilon_1,\varepsilon_2\) 为两个 Smith 生成元的对偶角色。此时

\[
V_0=0,
\qquad
V_1=\langle\varepsilon_1\rangle,
\qquad
V_2=\langle\varepsilon_1,\varepsilon_2\rangle.
\tag{30}
\]

令 \(W=V_2\)、\(H=2\)。若 \((c_1,c_2)=(1,1)\)，则

\[
\dim W=2=C_{\ge1},
\qquad
\dim W-\dim(W\cap V_1)=1=C_{\ge2}.
\tag{31}
\]

过滤适配基 \((\varepsilon_1,\varepsilon_2)\) 分别进入层 1、2，达到等号。

若改为 \((c_1,c_2)=(2,0)\)，总槽数仍为 2，但

\[
\Delta_2=2-1-0=1.
\tag{32}
\]

所以任何基都至少有一个方向必须进入第二层，而第二层没有容量；这是“总容量通过、
过滤容量失败”的严格反例。

最后展示换基量词。带名基

\[
\beta_1=\varepsilon_1+\varepsilon_2,
\qquad
\beta_2=\varepsilon_2
\tag{33}
\]

的两个角色都有最小深度 2。对容量 \((1,1)\)，它作为不可换名请求满足

\[
\#\{i:r_i\ge2\}=2>1=C_{\ge2},
\tag{34}
\]

故 (28) 严格失败；但它张成的同一个 \(W\) 可换回
\((\varepsilon_1,\varepsilon_2)\)，并由 (31) 通过。这证明“逐个检查当前展示生成元的
最小深度”不是角色子空间的基不变容量判据。

## 6. 统一选择器接口与研究边界

对一个多角色 `SOURCE_RANK_DEMAND(q,W,L)`，规范分派为：

~~~text
compute Smith t_i and obstruction spaces O_J
compute b_J(W) = rank(res_J restricted to W)

request already fixed at J_req:
  W <= V_J_req:
    FIXED_LAYER_ROLE_SUBSPACE_QHEIGHT_READY
    keep the original singleton layer edge
  otherwise:
    FIXED_LAYER_ROLE_SUBSPACE_QHEIGHT_OBSTRUCTED
  never invoke tail scheduling to retag this request

request is unlayered and only minimum q-height restricts its algebraic layers:
  role contract is basis-flexible:
    every tail inequality passes:
      FILTERED_ROLE_BASIS_QHEIGHT_TAIL_MATCH_READY
      emit adapted basis, release layers, and slot assignment
    otherwise:
      ROLE_SUBSPACE_QHEIGHT_TAIL_CAPACITY_DEFICIT(k, quotient witness)

  role contract is named/immutable:
    compute each r_i = max(1, d_q(L, gamma_i)) within the window
    every named tail inequality passes:
      NAMED_ROLE_QHEIGHT_TAIL_MATCH_READY
    otherwise:
      NAMED_ROLE_QHEIGHT_TAIL_HALL_DEFICIT(k, named role subset)

then intersect with range/label/occurrence/source-switch edges
run general layered Hall/Rado on the surviving physical graph
~~~

本卡关闭了上一张 q-height 主张留下的“两个以上尚未绑定层的独立角色如何按最小深度
支付”的纯代数部分，并给出 fixed-layer 角色子空间的精确原层秩，
同时产生一个精确、基不变的容量映射。它没有证明 \(c_J\) 对应真实 owner rows，也没有
自动满足整数范围、标签、occurrence、target state、Kneser 价格、E4 或 E5。特别地，
`TAIL_MATCH_READY` 只是进入物理 Hall/Rado 的准入回执，不是 Type I/II 终端。

下一决定性缺口不再是重复计算单角色深度，而是：从实际 F/G 请求构造完整的物理层槽和
兼容边；若额外门删边后出现 Hall/Rado 缺口，则把该严格缺口接到 Type I/II 终端、完整
kernel source box 或保持标记的良基下降。

## 聚焦验证

~~~bash
python3 \
  reproductions/type_i_source_lattice_filtered_dual_tail_hall_capacity.py \
  --verify
~~~

验证器只核对 (5)、(11)--(14)、fixed-layer 不重标、二维 Smith 控制、上尾充要条件
和换基反例；不运行历史扫描。
