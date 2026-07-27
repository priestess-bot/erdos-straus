---
kind: claim
claim_id: h19-k23-global-one-factor-prime-families-2097152
title: H19-k23 全局尾的一因子必要且可持续素数族
statement: H19-k23 二百万层的22条全局规范基底压力记录各自可提升为一条原始核心素数等差进程。在每条进程上，72个全局尾均无规范基底零缺陷证书，但一个固定的规范Type II除子持续提供恰含一枚新增素因子的证书；由于相应全局尾满足 m+1|p-1，它直接给出严格双尾递降。22条进程使用21个不同的新素因子。
claim_status: established
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- factor-support
- affine-progressions
- dirichlet
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾的一因子必要且可持续素数族

[无限素数参数障碍](h19-k23-global-base-only-prime-obstruction-2097152.md) 已证明，二百万层的
22 条压力种子各自给出无穷多个实际核心素数，在完整 72 尾菜单中均不存在规范基底
零缺陷证书。这里对每条种子进一步保留其最小规范一因子 Type II 证书。

每条压力记录在其当前尾 \(m=4q-1\) 都有一个除子

\[
d\mid(qu)^2,\qquad d\equiv-qu\pmod m,
\]

其中 \(d\) 的非基底部分恰为一个素数 \(\ell\) 的一次幂。精确分解给出

\[
22_{\text{records}}=22_{\text{one new prime, exponent }1},
\]

并出现 21 个不同的 \(\ell\)；唯一重复的是 \(79\)。

## 同时冻结失败与证书

对一个压力种子，先取冻结所有全局尾基底状态的周期 \(M_0\)。再令

\[
M=\operatorname{lcm}\bigl(M_0,\ell^{v_\ell(u)+1}\bigr). \tag{1}
\]

于是沿 \(t=t_0+Mn\)：

1. 每条全局尾仍无规范基底目标残数除子；
2. 当前尾的 \(\ell\)-赋值不变；
3. 固定的 \(d\) 仍整除 \((qu)^2\)，仍命中同一目标余数，且对 \(n\ge0\) 仍满足
   \(d\le qu\)。

脚本在每个族的种子和一个周期平移上以精确有理数重验该证书及严格双尾源。相应素数
进程均原始且恒为 \(1\pmod{24}\)，所以 Dirichlet 定理给出每条进程中的无穷多个素数。

因此这 22 条进程中的每个素数同时具有以下两项性质：

\[
\begin{array}{c}
\text{任何全局尾都没有规范基底零缺陷证书},\\
\text{某个全局尾有固定的一新增素因子严格双尾证书}.
\end{array} \tag{2}
\]

这说明变量因子不是有限样本中偶然替换固定基底的现象；它在无穷多个实际核心素数上是
该规范框架内必要且足够的。不过 (2) 并不说明每个核心素数都进入这些进程，也不证明一般的
一因子选择器。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_one_factor_prime_families.py \
  --input reproductions/h19-k23-global-tail-base-only-descent-2097152.json \
  --output reproductions/h19-k23-global-one-factor-prime-families-2097152.json
python3 -m unittest tests/test_h19_k23_global_one_factor_prime_families.py -q
~~~
