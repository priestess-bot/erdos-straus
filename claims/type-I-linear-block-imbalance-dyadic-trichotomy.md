---
kind: claim
claim_id: type-I-linear-block-imbalance-dyadic-trichotomy
title: 线性块不平衡关系与广义二进终端三分
statement: 对完整线性源状态的两个块 U=sR+1、V=aR+1，素指数差的二进坐标为零时，非零奇素数差必在 K 的有限指数盒内并产生偶终端；二进坐标非零时，块差精确转化为一个广义 2^J 传输问题；零差只留下对称状态。对冻结的 200 个核心素数、10292 个模数和 18074 个有向状态，三分统计为 2518 个核关系、2776 个广义二进终端、12580 个未决二进状态和 200 个对称状态；每个核心素数至少有一个局部偶终端。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-short-relation-even-terminal
  - type-I-general-dyadic-terminal-transfer
  - type-I-target-divisor-even-terminal-selector
topics:
- type-I
- linear-source
- block-imbalance
- short-relation
- dyadic
- even-terminal
- descent
- finite-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性块不平衡关系与广义二进终端三分

## 设置

取一个完整线性状态

\[
p=a+s+asR,\qquad s\equiv1\pmod2,\qquad R\equiv3\pmod4,
\]

并定义

\[
U=sR+1,\qquad V=aR+1,\qquad 4K=UV,
\qquad U\equiv V\equiv1\pmod R.
\]

写

\[
K=\prod_{q\mid K}q^{\nu_q},\qquad
\lambda_q=v_q(U)-v_q(V).
\]

对奇素数有

\[
v_q(U)+v_q(V)=\nu_q,
\]

而二进坐标满足

\[
v_2(U)+v_2(V)=\nu_2+2,
\]

其中 \(\nu_2=0\) 表示 \(2\nmid K\)。由于两个块都同余于 \(1\pmod R\)，完整块比值给出

\[
2^{\lambda_2}\prod_{q\text{ odd}}q^{\lambda_q}
\equiv1\pmod R. \tag{1}
\]

## 精确三分

### 1. 二进差为零：核关系分支

若 \(\lambda_2=0\) 且某个奇素数坐标非零，则

\[
\lambda=(\lambda_q)_{q\mid K}\ne0,\qquad
|\lambda_q|\le\nu_q,\qquad
\prod_{q\mid K}q^{\lambda_q}\equiv1\pmod R. \tag{2}
\]

所以 \(\lambda\) 是原始有限指数盒内的非零核关系。取 \(\lambda\) 或 \(-\lambda\) 使

\[
\rho=\prod_{q\mid K}q^{\lambda_q}<1,
\]

则短关系偶终端引理给出

\[
E=4K\rho,\qquad
n=\frac{4K-E}{R},
\]

其中 \(E\mid4K^2\)、\(E\equiv1\pmod R\)、\(4\mid n\) 且 \(0<n<p\)。

### 2. 二进差为零且奇素数差也为零：对称分支

若所有 \(\lambda_q=0\)，则唯一分解给出 \(U=V\)，从而 \(a=s\)。于是

\[
p=a(2+aR).
\]

由于 \(p\) 是素数，只能有

\[
a=s=1,\qquad R=p-2.
\]

这正是完整线性谱中的对称边界；它不由不平衡关系自动产生终端。

### 3. 二进差非零：广义二进传输分支

令 \(j_0=|\lambda_2|>0\)，去掉 \(U,V\) 的二进部分，并令

\[
U_o=\frac U{2^{v_2(U)}},\qquad
V_o=\frac V{2^{v_2(V)}},\qquad g=(U_o,V_o).
\]

若 \(\lambda_2>0\)，取

\[
A=V_o/g,\qquad B=U_o/g;
\]

若 \(\lambda_2<0\)，交换两者。则 \(A,B\) 互素、为奇数、并且是 \(L=2K\) 的除子，且由
(1) 得

\[
A\equiv2^{j_0}B\pmod R. \tag{3}
\]

令 \(o_R(2)\) 为 \(2\) 在模 \(R\) 下的阶。任意整数 \(J\) 满足

\[
1\le J\le\nu_2+1,\qquad
J\equiv j_0\pmod{o_R(2)},\qquad
A<2^JB, \tag{4}
\]

都给出广义二进终端

\[
E_J=2^{1-J}L\frac AB,\qquad
n_J=\frac{2L-E_J}{R}. \tag{5}
\]

由一般 \(2^J\) 传输判据，\(E_J\) 是偶数、整除 \(L^2\)、满足

\[
E_J\equiv1\pmod R,\qquad 0<n_J<p,\qquad 2\mid n_J.
\]

因此，二进差分支的未决性只来自条件 (4) 没有可行的 \(J\)，而不是来自块差公式本身。

## 冻结完整谱审计

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_imbalance_trichotomy.py
~~~

对 200 个冻结核心素数的 10292 个完整模数和 18074 个有向线性状态，哈希锁定输入后得到：

~~~text
kernel_relation:   2518
dyadic_terminal:   2776
dyadic_unresolved: 12580
symmetric:          200
terminal_state_count: 5294
terminal_prime_count: 200
~~~

这说明在该完整有限谱中，每个核心素数至少有一个由块不平衡或广义二进关系构造的偶终端。

随后对 5294 个规范终端调用奇数距离偶源 Type I 提升核：

~~~text
parameter_count: 185
hit_count: 58
hit_state_count: 5
hit_prime_count: 5
hit_primes: 5019529, 70026889, 292485769, 362050441, 508542169
~~~

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_imbalance_lift.py
~~~

## 证明边界

这条三分把“线性状态内是否能构造偶终端”压缩为一个规范块差问题，但它没有完成原猜想的
全称选择器，原因有三：

1. 偶终端不等于目标平方除子，仍需奇数距离平方尾、普通 Type II 或其它提升核；
2. 12580 个二进状态没有通过当前有限 \(J\) 预算和方向条件，不能把形式上的关系当成偶终端；
3. 200 个对称状态需要独立的 Type II、目标命中或跨状态选择机制。

因此本主张的真正增量是：它把跨状态容量问题之前的状态内分支规范化，并证明当前完整样本的
每个核心素数都有一个偶终端候选；尚未证明这些候选总能严格可提升。注意线性源已有平凡
\(E=sR+1=U\) 终端，本主张的增量是块差关系提供的可枚举替代终端族，而不是首次证明
线性状态存在某个终端。
