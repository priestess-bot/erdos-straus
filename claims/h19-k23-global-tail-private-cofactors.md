---
kind: claim
claim_id: h19-k23-global-tail-private-cofactors
title: H19-k23 全局尾菜单的私有余因子分离
statement: 对 H19-k23 纯全局尾菜单的分母d属于{32,36,40,48,60,72,80,92,96}，令u_d=(p+d-1)/d。任意两项的公素因子都整除分母差d-e。故去除碰撞素数集合S={2,3,5,7,11,13}在各u_d中的全部幂后，九个剩余私有余因子两两互素。该引理把变量因子选择精确分解为有限碰撞部分与九个独立私有乘积集，但本身不强制某一尾命中 Type II 目标剩余。
claim_status: established
topics:
- type-II
- descent
- affine-progressions
- divisor-selection
- factor-support
- product-sets
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾菜单的私有余因子分离

纯全局尾闭合使用的分母集合为

\[
\mathcal D=\{32,36,40,48,60,72,80,92,96\}. \tag{1}
\]

对任意满足 \(d\mid p-1\) 的 \(d\in\mathcal D\)，令

\[
u_d=\frac{p+d-1}{d}. \tag{2}
\]

这正是尾缺口 \(m=d-1\) 的 \(x=qu_d\) 中变量因子。任取 \(d\ne e\)，由

\[
d u_d-e u_e=d-e \tag{3}
\]

立刻得到

\[
\gcd(u_d,u_e)mid d-e. \tag{4}
\]

对 (1) 的全部两两差分解，可能的碰撞素数恰为

\[
\mathcal S=\{2,3,5,7,11,13\}. \tag{5}
\]

令 \(u_d^{\mathrm{priv}}\) 为从 \(u_d\) 中除去 \(\mathcal S\) 内每个素数的全部幂后
得到的余因子。若某个素数同时整除 \(u_d^{\mathrm{priv}}\) 与
\(u_e^{\mathrm{priv}}\)，它由 (4) 必在 \(\mathcal S\)，与构造矛盾。因此

\[
\gcd\bigl(u_d^{\mathrm{priv}},u_e^{\mathrm{priv}}\bigr)=1
\qquad(d\ne e). \tag{6}
\]

## 研究含义

每个尾的 Type II 选择仍是相应 \(q^2u_d^2\) 的带大小界乘积集问题。但 (6) 将跨尾的
变量部分严格分解为：

\[
\text{有限碰撞素数 }\mathcal S
\quad+\quad
\text{九个两两互素的私有因子乘积集}. \tag{7}
\]

这比将九个 \(u_d\) 当作任意相关整数更强，也比固定基底路线更贴近剩余障碍。它尚不推出
某一私有乘积集必命中目标剩余：抽象乘积集可保留长的目标缺口。因此下一步应利用
\(p\equiv1\pmod{24}\)、九个线性关系 (3) 与素数参数条件，证明或反驳这种独立私有部分的
联合覆盖。

重建命令：

~~~bash
python3 reproductions/h19_k23_global_tail_private_cofactors.py
python3 -m unittest tests/test_h19_k23_global_tail_private_cofactors.py -q
~~~
