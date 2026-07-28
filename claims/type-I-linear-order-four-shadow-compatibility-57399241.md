---
kind: claim
claim_id: type-I-linear-order-four-shadow-compatibility-57399241
title: 四阶分离角色的二次影子跨源相容律
statement: 设一个线性G型状态具有在K的素因子支持上平凡、在-1上非平凡的四阶角色chi，且chi^2=(./D)是偶二次角色；设另一状态具有奇二次G型分离导子m。若奇素数q同时整除两个K，则q整除两个源模数差的四分之一，且Jacobi符号(mD/q)=(-1/q)。在p=57399241的R=444955四阶状态，D=12713；它与五个二次G型状态的全部五条共享奇素因子关系均为q=13并逐条满足该式。该约束是必要而非矛盾，不能推出目标命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- order-four-character
- quadratic-character
- quadratic-reciprocity
- shared-factors
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 四阶分离角色的二次影子跨源相容律

## 定理

固定一个核心素数 \(p\)，取两个不同的线性源模数 \(R,R'\)，并记

\[
K_R=\frac{pR+1}{4},\qquad K_{R'}=\frac{pR'+1}{4}. \tag{1}
\]

设第一个状态有四阶分离角色 \(\chi\)：它在 \(K_R\) 的每个素因子上取 \(1\)，而
\(\chi(-1)=-1\)。假定其平方是由奇平方自由数 \(D\mid R\) 给出的偶二次角色

\[
\chi^2(x)=\left(\frac{x}{D}\right),\qquad D\equiv1\pmod4. \tag{2}
\]

设第二个状态是二次 G 型：存在奇平方自由数

\[
m\mid R',\qquad m\equiv3\pmod4, \tag{3}
\]

使 \((\cdot/m)\) 在 \(K_{R'}\) 的素因子支持上平凡、在 \(-1\) 上取 \(-1\)。
若奇素数 \(q\) 同时整除 \(K_R,K_{R'}\)，则

\[
\boxed{
q\mid\frac{|R-R'|}{4},
\qquad
\left(\frac{mD}{q}\right)=\left(\frac{-1}{q}\right).
} \tag{4}
\]

## 证明

跨模数 \(K\) 公因子刚性给出 (4) 的第一式。又 \(q\nmid RR'\)，故所有 Jacobi 符号都定义。
由 \(\chi^2\) 在 \(q\) 上平凡以及第二个分离角色在 \(q\) 上平凡，

\[
\left(\frac qD\right)=1,\qquad
\left(\frac qm\right)=1. \tag{5}
\]

因为 \(D\equiv1\pmod4\)，二次互反律给出

\[
\left(\frac Dq\right)=\left(\frac qD\right)=1. \tag{6}
\]

而 \(m\equiv3\pmod4\)，故

\[
1=\left(\frac qm\right)
=\left(\frac{-1}{q}\right)\left(\frac mq\right),
\qquad
\left(\frac mq\right)=\left(\frac{-1}{q}\right). \tag{7}
\]

乘上 (6) 即得 (4) 的第二式。

## 四阶边界的应用

在 [57,399,241 的真正四阶分离角色](type-I-linear-order-four-separator-boundary-57399241.md)
中，

\[
R=444{,}955,\qquad
K_R=13\cdot51{,}341\cdot9{,}566{,}533,
\qquad
D=12{,}713. \tag{8}
\]

完整同源谱中，它只与二次 G 型状态在素数 \(q=13\) 上发生五条共享关系：

| 二次 G 模数 \(R'\) | 最小二次导子 \(m\) | \((mD/13)\) |
| ---: | ---: | ---: |
| 95 | 95 | 1 |
| 5,451 | 5,451 | 1 |
| 5,607 | 623 | 1 |
| 7,687 | 7,687 | 1 |
| 8,519 | 8,519 | 1 |

这里 \((-1/13)=1\)，所以五条关系均满足 (4)。这证实相容律，却不构成不相容性或命中证明。

## 边界

该命题只使用 \(\chi^2\)，因此它没有保留四次角色的相位信息，也不是四次互反拉回。
它的作用是把高阶状态纳入现有的跨模数碰撞框架，同时精确显示：仅靠这个二次影子，五条实际
碰撞仍完全相容。下一步必须使用 \(\chi\) 本身的四次值，或从有限指数 F 型建立反足点逃逸。

## 复现

~~~bash
python3 reproductions/type_i_linear_order_four_shadow_compatibility_57399241.py
python3 -m unittest tests.test_type_i_linear_order_four_shadow_compatibility_57399241 -v
~~~
