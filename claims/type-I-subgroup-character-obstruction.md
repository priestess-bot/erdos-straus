---
kind: claim
claim_id: type-I-subgroup-character-obstruction
title: Type I 失败的子群--字符分流
statement: 令 \(x=(p+m)/4\)、\(t=-1/4\bmod m\)，并令 \(H\) 为 \(x\) 的全部素因子模 m 残数生成的 \(U(m)\) 子群。若 \(t\notin H\)，则不存在 Type I 证书，且存在单位群字符 \(\chi\) 在每个 \(q\mid x\) 上取1、但 \(\chi(t)\ne1\)；因此 \(\chi(p)=\chi(4)\ne\chi(-1)\)。若 \(t\in H\) 而仍无证书，失败仅能来自平方除子指数的有限积集限制。对当前84条自适应链的2,155个失败位置，前者1,752个、后者403个。
claim_status: established
topics:
- type-I
- characters
- subgroup
- divisor-residues
- moving-window
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 失败的子群--字符分流

## 定理

固定核心素数 \(p\) 与合法缺口 \(m\)，并写

\[
x=\frac{p+m}{4},\qquad
t=-\frac14\pmod m. \tag{1}
\]

由于 \((x,m)=1\)，令 \(H\le U(m)\) 为所有 \(q\mid x\) 的素因子残数生成的子群。
则有两种互斥的 Type I 失败机制：

1. **子群型：** \(t\notin H\)。此时不存在 Type I 证书，且存在有限阶单位群字符
   \(\chi:U(m)\to\mathbb C^\times\)，使

   \[
   \chi(q)=1\quad(q\mid x),\qquad\chi(t)\ne1. \tag{2}
   \]

   因而

   \[
   \chi(p)=\chi(4)\ne\chi(-1). \tag{3}
   \]

2. **有限积集型：** \(t\in H\)，但 \(t\notin\Pi_m(x^2)\)。这时角色无法区分目标；
   失败只能由每个素因子在平方除子中至多使用两倍原指数的限制造成。

## 证明

Bradford Type I 判据为

\[
t\in\Pi_m(x^2). \tag{4}
\]

显然 \(\Pi_m(x^2)\subseteq H\)，故 \(t\notin H\) 时 (4) 不可能。有限阿贝尔群的角色
分离给出一个在 \(H\) 上平凡、但在 \(t\) 上非平凡的字符，得到 (2)。

又 \(\chi(x)=1\)，且 \(p\equiv4x\pmod m\)，所以

\[
\chi(p)=\chi(4)\chi(x)=\chi(4). \tag{5}
\]

而 \(\chi(t)=\chi(-1)\chi(4)^{-1}\ne1\)，即得 (3)。剩余情形正是
\(t\in H\setminus\Pi_m(x^2)\)，没有角色型障碍，只能由有限指数积集缺口解释。

## 当前状态的剖面

在 [Type I 自适应逃逸深度剖面](type-I-adaptive-escape-seed-profile.md) 的 84 条有限种子
链中，至多第100窗口的最终失败状态共有 2,155 个位置：

| 失败机制 | 位置数 |
|---|---:|
| 子群型 | 1,752 |
| 有限积集型 | 403 |

最深的第97窗口链中，67 个位置属于子群型，30 个属于有限积集型。故当前长链的主要困难
首先是跨缺口字符条件如何共存，而不仅是局部零和指数。

## 研究用途与边界

这条分流给出两条不同任务：

- 对子群型，研究由 (3) 给出的不同模数角色条件是否能在增长窗口中长期兼容；
- 对有限积集型，研究受限幂指数的乘积集何时覆盖 \(t\)，不能只使用生成子群。

但角色条件的存在本身不会自动矛盾：有限个角色核可能通过 CRT 兼容。因此这不是闭合定理；
它只是把“窗口失败”转换成可以逐类研究的、可验证的算术状态。

## 重建

    python3 reproductions/type_i_adaptive_escape_seed_profile.py
    python3 -m unittest tests/test_type_i_adaptive_escape_seed_profile.py -q
