---
kind: claim
claim_id: type-I-linear-order-four-separator-boundary-57399241
title: 57,399,241 的真正四阶线性 G 型分离角色
statement: 对核心素数p=57399241的完整线性谱，R=444955=5*7*12713给出K=6385019819789=13*51341*9566533的G型状态。所有在K的素因子支持上平凡且阶整除4的Dirichlet角色中，恰有两个使-1取值为-1；它们互为共轭、阶恰为4、导子均为7*12713=88991。不存在二次分离角色。因此此状态是当前四个真实对抗核心中纯二次跨源兼容律的明确且不可省略的边界；本结果不提供四次互反拉回，也不推出另一线性源命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- order-four-character
- fourth-reciprocity-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 57,399,241 的真正四阶线性 G 型分离角色

## 状态

在完整的一般 \(B\) 线性谱中取

\[
p=57{,}399{,}241,\qquad
R=444{,}955=5\cdot7\cdot12{,}713.
\]

该模数由两条有向线性源

\[
(a,s)=(3,43),\qquad(43,3)
\]

诱导，且

\[
K=\frac{pR+1}{4}
=6{,}385{,}019{,}819{,}789
=13\cdot51{,}341\cdot9{,}566{,}533. \tag{1}
\]

完整 \(K^2\) 除子枚举没有目标，且 \(-1\notin\mathcal H_R(K)\)，故这是 G 型状态。

对局部分量 \(5,7,12{,}713\) 分别选原根 \(2,3,3\)。三个 \(K\) 素因子和 \(-1\) 的离散对数
坐标依次为

\[
\begin{array}{c|ccc}
 &5&7&12{,}713\\ \hline
13&3&3&7{,}710\\
51{,}341&0&1&5{,}046\\
9{,}566{,}533&3&4&44\\ \hline
-1&2&3&6{,}356
\end{array}. \tag{2}
\]

## 定理

所有在 \((\mathbb Z/R\mathbb Z)^\times\) 上阶整除 \(4\) 的角色，可写成

\[
\chi_{b_5,b_7,b_{12713}}(x)
=i^{\,b_5\ell_5(x)+2b_7\ell_7(x)+b_{12713}\ell_{12713}(x)}, \tag{3}
\]

其中

\[
b_5,b_{12713}\in\mathbb Z/4\mathbb Z,\qquad
b_7\in\mathbb Z/2\mathbb Z.
\]

在三个 \(K\) 素因子上都取 \(1\) 的角色恰为

\[
(0,0,0),\quad(0,0,2),\quad(0,1,1),\quad(0,1,3). \tag{4}
\]

其中前两个在 \(-1\) 上也取 \(1\)；后两个都在 \(-1\) 上取 \(-1\)，且互为共轭。因此：

\[
\boxed{
\begin{gathered}
\text{没有二次角色在 }K\text{ 的素因子支持上平凡而分离 }-1;\\
\text{恰有两个最小四阶分离角色，导子均为 }7\cdot12{,}713=88{,}991.
\end{gathered}}
\tag{5}
\]

## 证明

把 (2) 代入 (3)，令三个 \(K\) 素因子的指数都为 \(0\pmod4\)。第二行先给出

\[
2b_7+2b_{12713}=0\pmod4,
\]

第三行给出 \(3b_5=0\pmod4\)，故 \(b_5=0\)。第一行于是与第二行等价，留下

\[
b_7\equiv b_{12713}\pmod2. \tag{6}
\]

这正好给出 (4)。由 \(-1\) 的对数坐标，

\[
\chi_{b_5,b_7,b_{12713}}(-1)=i^{2b_5+6b_7+6356b_{12713}}
=(-1)^{b_7}. \tag{7}
\]

故在 (4) 中只有 \((0,1,1)\) 与 \((0,1,3)\) 分离 \(-1\)。两者的 \(12{,}713\) 分量是本原四次角色，
\(7\) 分量是非平凡二次角色，所以阶为 \(4\)，导子为 \(7\cdot12{,}713\)。而阶至多二的候选只有
\((0,0,0)\)、\((0,0,2)\)，均由 (7) 在 \(-1\) 上取 \(1\)。

## 含义与边界

这给出一个精确的高阶边界，而不是新的跨源定理。现有
[二次分离子的跨模数相容律](type-I-linear-cross-state-quadratic-separator-compatibility.md)
故意排除了本状态；不能把它扩展为“所有 G 型状态都有二次导子”。下一步若要吸收此状态，必须：

1. 为 (3) 的四次分量建立可跨模数的互反拉回；或
2. 证明该状态总可由同一 \(p\) 的另一线性源、这里为 \(R=19\)，替代为命中。

第二项在这个有限实例中已经成立，但不构成全称选择引理。

## 复现

~~~bash
python3 reproductions/type_i_linear_order_four_separator_boundary_57399241.py
python3 -m unittest tests.test_type_i_linear_order_four_separator_boundary_57399241 -v
~~~
