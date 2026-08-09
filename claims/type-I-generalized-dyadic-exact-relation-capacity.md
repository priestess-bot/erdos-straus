---
kind: claim
claim_id: type-I-generalized-dyadic-exact-relation-capacity
title: 广义二进偶终端的精确关系格容量定理
statement: >-
  设 4K=pR+1、R>1 为奇数、L=2K。全部合法广义 2^j 自由除子对在终端结果
  (E,n) 上去重后，与满足 E|L^2、2|E、E=1 (mod R)、0<E<4K 的偶除子 E，
  以及乘法关系格在非对称盒 -v_2(K)-1<=lambda_2<=v_2(K)、
  |lambda_q|<=v_q(K) 内满足 rho(lambda)<1 的点自然双射。若 B_K 是对应对称盒，
  O_K^- 是唯一二进外层 lambda_2=-v_2(K)-1 中的定向关系点集，则终端数精确等于
  (|Lambda_R intersect B_K|-1)/2+|O_K^-|。因此 j>1 不增加终端容量；相对普通
  短关系终端唯一的新容量是 v_2(E)=1 的单层。该结论只分类算术偶前驱，不提供
  E1--E5 所需的标记源、全域解提升或良基递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-generalized-dyadic-j-one-terminal-normalization
  - type-I-short-relation-even-terminal
  - type-I-generalized-dyadic-natural-lift-equivalence
topics:
  - type-I
  - generalized-dyadic
  - terminal-normalization
  - relation-lattice
  - exact-capacity
  - two-adic
  - target-fiber
  - F-state
  - G-state
  - proof-boundary
sources:
  - claim: type-I-generalized-dyadic-j-one-terminal-normalization
    role: unique-j-one-normal-form
  - claim: type-I-short-relation-even-terminal
    role: symmetric-box-terminal-family
  - claim: type-I-generalized-dyadic-natural-lift-equivalence
    role: marked-lift-boundary
visibility: public
last_checked: '2026-08-09'
---

# 广义二进偶终端的精确关系格容量定理

## 1. 设置

设

\[
R>1\text{ 为奇数},
\qquad 4K=pR+1,
\qquad L=2K.
\tag{1}
\]

式 (1) 自动给出 \((L,R)=1\)。令

\[
Q_L=\{q:q\text{ 为素数且 }q\mid L\},
\qquad \nu_q=v_q(K).
\tag{2}
\]

无论 \(2\mid K\) 与否都保留坐标 \(q=2\)；当 \(K\) 为奇数时，约定
\(\nu_2=0\)。定义模 \(R\) 的乘法关系格和有理高度

\[
\Lambda_R=
\left\{\lambda\in\mathbb Z^{Q_L}:
\prod_{q\in Q_L}q^{\lambda_q}\equiv1\pmod R\right\},
\qquad
\rho(\lambda)=\prod_{q\in Q_L}q^{\lambda_q}.
\tag{3}
\]

负指数在 \((\mathbb Z/R\mathbb Z)^\times\) 中解释。考虑非对称二进盒

\[
\mathcal B_K^{\rm dy}=
\left\{\lambda:
-\nu_2-1\le\lambda_2\le\nu_2,
\quad |\lambda_q|\le\nu_q\ (q\ne2)
\right\}
\tag{4}
\]

及其中的定向关系点集

\[
\mathcal D_K=
\left\{\lambda\in\Lambda_R\cap\mathcal B_K^{\rm dy}:
\rho(\lambda)<1\right\}.
\tag{5}
\]

## 2. 三个有限集合

广义二进自由除子对数据是满足

\[
(A,B)=1,
\quad A,B\mid L,
\quad A\equiv2^jB\pmod R,
\tag{6}
\]

\[
1\le j\le v_2(L)+v_2(A)-v_2(B),
\qquad A<2^jB
\tag{7}
\]

的三元组 \((A,B,j)\)。其算术终端为

\[
E=2^{1-j}L\frac AB,
\qquad
n=\frac{4K-E}{R}.
\tag{8}
\]

令 \(\mathcal T_K\) 为所有合法三元组产生的**不同** \((E,n)\)；原始三元组与
source label 不属于 \(\mathcal T_K\)，只在另表保存 provenance。另令

\[
\mathcal E_K=
\left\{E\in\mathbb N:
E\mid L^2,
\quad 2\mid E,
\quad E\equiv1\pmod R,
\quad E<4K
\right\}.
\tag{9}
\]

## 3. 精确双射定理

存在自然双射

\[
\boxed{
\mathcal T_K\ \longleftrightarrow\
\mathcal E_K\ \longleftrightarrow\
\mathcal D_K.}
\tag{10}
\]

其中关系点到终端的映射为

\[
\boxed{
E=4K\rho(\lambda),
\qquad
n=\frac{4K-E}{R},}
\tag{11}
\]

反向映射为

\[
\boxed{
\lambda_q=v_q(E)-v_q(4K)
\qquad(q\in Q_L).}
\tag{12}
\]

每个 \(\lambda\in\mathcal D_K\) 的唯一 \(j=1\) 自由除子对由既约分数

\[
\boxed{
\frac{A^\sharp}{B^\sharp}=2\rho(\lambda)=\frac EL}
\tag{13}
\]

给出。不同 \(j\) 的三元组可以保留不同 provenance，但不会增加 (10) 中的终端结果。

### 证明：\(\mathcal E_K\leftrightarrow\mathcal D_K\)

先取 \(E\in\mathcal E_K\)，并按 (12) 定义 \(\lambda\)。对奇素数 \(q\mid K\)，由
\(E\mid L^2=4K^2\) 得

\[
0\le v_q(E)\le2\nu_q,
\qquad
-\nu_q\le\lambda_q\le\nu_q.
\tag{14}
\]

在二进坐标上，

\[
\lambda_2=v_2(E)-(\nu_2+2).
\tag{15}
\]

因为 \(E\) 为偶数且
\(v_2(E)\le v_2(L^2)=2\nu_2+2\)，所以

\[
-\nu_2-1\le\lambda_2\le\nu_2.
\tag{16}
\]

又因 \(E\equiv4K\equiv1\pmod R\)，有
\(\rho(\lambda)=E/(4K)\equiv1\pmod R\)，故
\(\lambda\in\Lambda_R\)。不等式 \(E<4K\) 给出 \(\rho(\lambda)<1\)，所以
\(\lambda\in\mathcal D_K\)。

反过来，取 \(\lambda\in\mathcal D_K\) 并按 (11) 定义 \(E\)。对奇素数 \(q\)，

\[
v_q(E)=\nu_q+\lambda_q\in[0,2\nu_q],
\tag{17}
\]

而

\[
v_2(E)=\nu_2+2+\lambda_2\in[1,2\nu_2+2].
\tag{18}
\]

所以 \(E\) 是正偶整数且 \(E\mid L^2\)。关系格同余给出
\(E\equiv4K\equiv1\pmod R\)，而 \(\rho(\lambda)<1\) 给出 \(E<4K\)。故
\(E\in\mathcal E_K\)。素因子赋值唯一性说明 (11)--(12) 互逆。

此外 \(4K-E\) 是正的 \(R\) 的倍数。它和 \(R\) 都是奇偶性已知的整数：
\(4K-E\) 为偶数而 \(R\) 为奇数，故 \(n\) 为正偶数。由

\[
n=p+\frac{1-E}{R}<p
\tag{19}
\]

还得到严格较小的算术偶前驱。

### 证明：\(\mathcal E_K\leftrightarrow\mathcal T_K\)

取 \(E\in\mathcal E_K\)，把 \(E/L\) 写成既约正分数
\(A^\sharp/B^\sharp\)。对奇素数 \(q\)，其赋值属于
\([-\nu_q,\nu_q]\)；二进赋值为

\[
v_2(E/L)=1+\lambda_2\in[-\nu_2,\nu_2+1].
\tag{20}
\]

因此既约分子、分母都整除 \(L\)。由 \(2L=4K\equiv1\pmod R\) 得
\(L^{-1}\equiv2\pmod R\)，从而

\[
A^\sharp\equiv2B^\sharp\pmod R.
\tag{21}
\]

又 \(E<2L\) 给出 \(A^\sharp<2B^\sharp\)，而

\[
v_2(L)+v_2(A^\sharp)-v_2(B^\sharp)=v_2(E)\ge1.
\tag{22}
\]

故 \((A^\sharp,B^\sharp,1)\) 是合法见证并产生该 \(E\)。反方向由广义二进传输的
终端合法性直接得到 \(E\in\mathcal E_K\)。现有唯一 \(j=1\) 归一化定理说明任意
\((A,B,j)\) 都归一到 (13)，且保持同一 \((E,n)\)。既约分数唯一性完成双射证明。

## 4. 精确容量公式

定义对称盒

\[
\mathcal B_K=
\left\{\lambda:
|\lambda_2|\le\nu_2,
\quad |\lambda_q|\le\nu_q\ (q\ne2)
\right\}
\tag{23}
\]

和定向外层

\[
\mathcal O_K^-=
\left\{\lambda\in\Lambda_R:
\lambda_2=-\nu_2-1,
\quad |\lambda_q|\le\nu_q\ (q\ne2),
\quad \rho(\lambda)<1
\right\}.
\tag{24}
\]

则

\[
\boxed{
|\mathcal T_K|=|\mathcal E_K|=|\mathcal D_K|
=\frac{|\Lambda_R\cap\mathcal B_K|-1}{2}
+|\mathcal O_K^-|.}
\tag{25}
\]

事实上，对称盒内的每个非零关系点与其负向点成对出现。唯一分解保证
\(\rho(\lambda)=1\) 只能发生于 \(\lambda=0\)，故每一对中恰有一个点满足
\(\rho<1\)。这给出 (25) 的第一项；非对称盒比对称盒只多出 (24) 的单层。

对称盒项正是普通短关系偶终端族，且其中 \(v_2(E)\ge2\)。唯一新增部分满足

\[
\lambda_2=-\nu_2-1
\quad\Longleftrightarrow\quad
v_2(E)=1.
\tag{26}
\]

因此不能把普通短关系、目标纤维近邻、不同 \(j\) 的见证和外层终端分别重复计容。

## 5. 目标纤维边界

任意目标纤维近邻对的指数差都落在对称盒 \(\mathcal B_K\)，所以它只能产生 (25)
的内部项。反过来，一个内部关系点来自目标纤维近邻，当且仅当相应平移透镜

\[
\widetilde{\mathcal Z}_{R,K}^-
\cap
\bigl(\widetilde{\mathcal Z}_{R,K}^-+\lambda\bigr)
\ne\varnothing
\tag{27}
\]

被占据。故透镜只记录 target-fiber provenance，不扩张终端集合。外层 (26) 对应
\(v_2(E)=1\)，而近邻终端总有 \(4\mid E\)，所以外层严格不可能来自近邻对。

## 6. 两个有限控制

### \(p=433\)

取

\[
(p,R,K)=(433,15,1624),
\qquad K=2^3\cdot7\cdot29.
\tag{28}
\]

按坐标 \((2,7,29)\)，对称盒中有 \(9\) 个关系点，外层定向点有 \(1\) 个。因此

\[
|\mathcal E_K|=(9-1)/2+1=5.
\tag{29}
\]

对应终端和关系点恰为

\[
\begin{array}{c|c}
E&\lambda\\ \hline
16&(-1,-1,-1)\\
196&(-3,1,-1)\\
256&(3,-1,-1)\\
406&(-4,0,0)\\
3136&(1,1,-1)
\end{array}
\tag{30}
\]

其中 \(E=406\) 是唯一外层结果。终端 \(E=3136\) 至少有三种原始写法

\[
(A,B,j)=(28,29,1),(56,29,2),(112,29,3),
\tag{31}
\]

但三者只占用一个终端容量单位。

### \(p=673\)

取

\[
(p,R,K)=(673,83,13965),
\qquad K=3\cdot5\cdot7^2\cdot19.
\tag{32}
\]

按坐标 \((2,3,5,7,19)\)，对称盒中有 \(3\) 个关系点，外层定向点有 \(1\) 个，故

\[
|\mathcal E_K|=(3-1)/2+1=2.
\tag{33}
\]

两个终端为

\[
E=84,\quad\lambda=(0,0,-1,-1,-1),
\qquad
E=8550,\quad\lambda=(-1,1,1,-2,0).
\tag{34}
\]

外层结果 \(E=8550\) 同时由 \((15,49,1)\) 和 \((30,49,2)\) 表示，仍只计一次。

窄验证：

```bash
python3 reproductions/type_i_generalized_dyadic_exact_relation_capacity.py --verify
```

脚本只枚举 (28) 与 (32)：它独立比较全部合法 \((A,B,j)\) 去重后的 \(E\) 集、
非对称关系盒给出的 \(E\) 集和公式 (25)，不读取或重跑历史审计。

## 7. F/G 状态与 E1--E5 边界

定理 (10) 是 target-independent 的状态内算术分类，因此对 hit、F、G 状态都成立。
它给统一选择器的合法分派是：

1. 若 \(\mathcal D_K=\varnothing\)，则该状态不存在任何 \(j\ge1\) 的广义二进算术终端；
2. 若 \(\lambda\in\mathcal B_K\)，只登记一个规范短关系候选，并按 (27) 单独记录是否有
   target-fiber provenance；
3. 若 \(\lambda\in\mathcal O_K^-\)，只登记一个 `DYADIC_OUTER_LAYER` 容量单位；
4. 任意原始 \(j>1\) 只保存 source provenance，不增加候选或容量。

这里的“终端”仅指已经构造出严格较小偶数 \(n\) 的算术结果。它不自动提供 E1--E5
合同所需的合法标记源、全域解提升和良基图边。尤其已有自然标记提升等价表明：在
\(R>3\) 的 finite-exponent F 状态中，这些偶前驱的自然标记源严格为空。G 状态中的关系同样是
target-neutral，不能单独修复目标不在支撑中的障碍。

因此 (10) 完全关闭的是“继续增加 \(j\) 或重复枚举同类 \(E\) 是否能增加容量”的问题；
它没有关闭的最窄接口仍是：为规范有限集合 \(\mathcal D_K\) 中至少一个点构造非自然且
通过 E1--E5 的标记提升，或者把全部提升失败映射到独立容量缺陷或严格良基递降。
