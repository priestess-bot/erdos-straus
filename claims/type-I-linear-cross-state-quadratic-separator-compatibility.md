---
kind: claim
claim_id: type-I-linear-cross-state-quadratic-separator-compatibility
title: 线性二次 G 型分离子的跨模数共享素因子相容律
statement: 固定核心素数p。两个不同线性源模数R,R'的K值若共享奇素因子q，且各自存在奇平方自由二次G型分离导子m|R、m'|R'，满足m=m'=3 mod 4并在各自K的全部素因子上平凡，则q整除abs(R-R')/4且Jacobi符号(mm'/q)=1。故共享碰撞素因子同时被模数差和二次剩余条件限制。四个唯一一般B命中且全谱无B=1的对抗核心中，116个二次G型状态的1,011条共享奇素因子关系均逐项复核；另有一个四阶角色状态不适用本定理。该兼容律不强制目标命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- quadratic-character
- quadratic-reciprocity
- gcd-rigidity
- shared-factors
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性二次 G 型分离子的跨模数共享素因子相容律

## 定理

固定核心素数 \(p\)。令两个不同线性源状态诱导的模数为

\[
R\ne R',
\qquad K_R=\frac{pR+1}{4},
\qquad K_{R'}=\frac{pR'+1}{4}. \tag{1}
\]

设它们都是二次 G 型状态：存在奇平方自由数

\[
m\mid R,\qquad m'\mid R',\qquad m\equiv m'\equiv3\pmod4, \tag{2}
\]

使得二次角色 \(\chi_m=(\cdot/m)\) 与 \(\chi_{m'}=(\cdot/m')\) 分别在
\(K_R,K_{R'}\) 的每个素因子残数上平凡，而在 \(-1\) 上取 \(-1\)。

若奇素数 \(q\) 同时整除 \(K_R) 和 \(K_{R'}\)，则

\[
\boxed{
q\mid\frac{|R-R'|}{4},
\qquad
\left(\frac{mm'}q\right)=1.
} \tag{3}
\]

所以跨状态的共享奇素因子不但来自明确的模数差，而且必须在二次域
\(\mathbb Q(\sqrt{mm'})\) 中分裂。

## 证明

[跨模数 \(K\) 公因子刚性](type-I-linear-cross-modulus-gcd-rigidity.md)直接给出

\[
\gcd(K_R,K_{R'})=
\gcd\left(K_R,\frac{|R-R'|}{4}\right), \tag{4}
\]

故 (3) 的第一个结论成立。又 \(q\nmid RR'\)，因而 \(q\) 与 \(m,m'\) 互素。两个分离角色
在 \(q\) 上都平凡，所以

\[
1=\left(\frac qm\right)\left(\frac q{m'}\right)
=\left(\frac q{mm'}\right). \tag{5}
\]

因为 \(mm'\equiv1\pmod4\)，二次互反律没有符号项，给出

\[
\left(\frac q{mm'}\right)=\left(\frac{mm'}q\right).
\]

这完成证明。

也可从[二次障碍的互反拉回](type-I-linear-quadratic-obstruction-reciprocity-pullback.md)
直接看到同一关系：对 \(c=R/m,c'=R'/m'\)，两个状态都给出
\((pc/q)=(pc'/q)=1\)。相乘后，由 \(R\equiv R'\pmod q\) 得到
\((cc'/q)=(mm'/q)=1\)。这说明相容律同时保留了固定核心素数和跨模数碰撞信息。

## 对抗核心审计

在四个“全谱无 \(B=1\)、一般 \(B\) 命中唯一”的核心

\[
p\in\{878089,26034649,57399241,283319689\} \tag{6}
\]

中，最小二幂分离角色为二阶的 G 型状态分别有 \(21,20,29,46\) 个。程序枚举任意两个这类
状态的 \(K\) 公因子，得到：

| (p) | 二次 G 型状态 | 含共享奇素因子的 \(R,R'\) 对 | 共享素因子关系 |
| ---: | ---: | ---: | ---: |
| 878,089 | 21 | 94 | 113 |
| 26,034,649 | 20 | 73 | 84 |
| 57,399,241 | 29 | 155 | 190 |
| 283,319,689 | 46 | 488 | 624 |
| **合计** | **116** | **810** | **1,011** |

每一条关系均直接验证 (3)。\(p=57{,}399{,}241\) 另有一个最小分离角色阶为四的 G 型状态，
它不满足本定理的二次假设，因而被明确排除而非强行归入。

## 含义与边界

这不是“所有 G 型障碍互不相容”的结论；上表中的 G 型状态确实可以同时存在。它提供的是更细的
输入：任意利用跨源共享素因子构造的筛法，都必须同时处理模数差与 (3) 的二次剩余限制。

该定理仍不能处理私有素因子、F 型有限指数障碍或高阶角色，也不推出某个 \(R\) 必定命中。
它的作用是把跨源角色比较从抽象单位群语言压缩为可检验的、位于具体碰撞素因子上的分裂条件。

## 复现

~~~bash
python3 reproductions/type_i_linear_cross_state_quadratic_separator_compatibility_profile_600m.py
python3 -m unittest tests.test_type_i_linear_cross_state_quadratic_separator_compatibility_profile_600m -v
~~~
